"""Check maintained documentation, preserved moves and scoped source syntax."""
import ast
import hashlib
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
BASE = "663ccbe3c51ac2441f059395f7a7f44d1f2c0016"
errors = []


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def slug(text):
    text = re.sub(r"[*`\[\]]", "", text).lower()
    return re.sub(r"[^\w\- ]", "", text).replace(" ", "-")


# This manifest preserves historical names as text, not active relative links.
manifest = (ROOT / "archive/MOVED_FILES.md").read_text()
moves = dict(re.findall(r"\| `([^`]+)` \| `([^`]+)` \|", manifest))
base_files = git("ls-tree", "-r", "--name-only", "-z", BASE).decode().split("\0")
allowed_changes = {
    ".gitignore", "README.md", "app.py", "mainTrain.py", "mainTest.py",
    "Marketing Website/index.html", "Marketing Website/script.js",
    "Jewellery Website/index.html", "Jewellery Website/script.js",
}
checked = 0
for name in filter(None, base_files):
    target = ROOT / moves.get(name, name)
    if not target.is_file():
        errors.append(f"Missing original file: {name}")
        continue
    original = git("show", f"{BASE}:{name}")
    if name not in allowed_changes and hashlib.sha256(original).digest() != hashlib.sha256(target.read_bytes()).digest():
        errors.append(f"Unexpected original-content change: {name}")
    checked += 1
for name in ("app.py", "mainTrain.py", "mainTest.py"):
    if (ROOT / "archive/brain-tumor-original" / name).read_bytes() != git("show", f"{BASE}:{name}"):
        errors.append(f"Historical script snapshot changed: {name}")

# Only tracked and explicitly maintained new files; never scan node_modules/venvs.
paths = set(git("ls-files", "-z").decode().split("\0"))
paths.update({"CHANGES_SUMMARY.md", "scripts/check_repository.py"})
md_count = 0
for name in sorted(paths):
    source = ROOT / name
    if source.suffix != ".md" or not source.is_file() or name.startswith("archive/github-skills/"):
        continue
    text = source.read_text()
    # Ignore fenced code and inline code when collecting active Markdown links.
    body = re.sub(r"```.*?```", "", text, flags=re.S)
    body = re.sub(r"`[^`]*`", "", body)
    for match in re.finditer(r"!?\[[^\]]*\]\(([^)]+)\)", body):
        url = match.group(1).strip().strip("<>")
        parts = urlsplit(url)
        if parts.scheme or url.startswith("//"):
            continue
        target = (source.parent / unquote(parts.path)).resolve() if parts.path else source
        if not target.exists():
            errors.append(f"Broken Markdown link: {name} -> {url}")
        elif parts.fragment and target.suffix == ".md":
            anchors = {slug(h) for h in re.findall(r"^#{1,6}\s+(.+)$", target.read_text(), re.M)}
            if unquote(parts.fragment) not in anchors:
                errors.append(f"Broken Markdown anchor: {name} -> {url}")
    if not text.endswith("\n") and name not in {"ATTRIBUTIONS.md", "Birthday Card/README.md"}:
        errors.append(f"Missing final newline: {name}")
    md_count += 1

for source in [ROOT / name for name in paths if name.endswith(".py")]:
    if source.is_file():
        try:
            ast.parse(source.read_text())
        except SyntaxError as error:
            errors.append(f"Python syntax: {source.relative_to(ROOT)}:{error.lineno}")

node = shutil.which("node")
if node:
    for name in ["Marketing Website/script.js", "Jewellery Website/script.js"]:
        result = subprocess.run([node, "--check", str(ROOT / name)], capture_output=True)
        if result.returncode:
            errors.append(f"JavaScript syntax error: {name}")
else:
    print("Node unavailable: skipped featured JavaScript syntax checks.")

for error in errors:
    print(error)
print(f"Checked {checked} original files, {len(moves)} intact moves and {md_count} maintained Markdown files.")
raise SystemExit(bool(errors))
