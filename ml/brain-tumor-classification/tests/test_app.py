"""Upload boundaries use a fake predictor; they do not validate model accuracy."""
import io
import sys
from pathlib import Path

import pytest
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from app import create_app


def png_bytes(size=(12, 12)):
    data = io.BytesIO()
    Image.new("RGB", size, (10, 40, 90)).save(data, format="PNG")
    data.seek(0)
    return data


@pytest.fixture
def setup():
    seen = []

    def predictor(path, model):
        assert path.is_file()
        seen.append(path)
        return 42.5, "Yes"

    application = create_app({"TESTING": True}, predictor)
    return application.test_client(), seen


def test_home_and_method_boundaries(setup):
    client, _ = setup
    response = client.get("/")
    assert response.status_code == 200
    assert b"Not intended for medical diagnosis" in response.data
    assert client.get("/predict").status_code == 405
    assert not client.application.debug
    assert response.headers["Cache-Control"] == "no-store"


@pytest.mark.parametrize("filename,content", [("file.html", b"<h1>bad</h1>"), ("bad.png", b"not an image"), ("", b"empty")])
def test_rejected_files_never_reach_predictor(setup, filename, content):
    client, seen = setup
    response = client.post("/predict", data={"file": (io.BytesIO(content), filename)})
    assert response.status_code == 400
    assert seen == []


def test_missing_file(setup):
    client, seen = setup
    assert client.post("/predict").status_code == 400
    assert seen == []


def test_content_extension_mismatch(setup):
    client, seen = setup
    assert client.post("/predict", data={"file": (png_bytes(), "pretend.jpg")}).status_code == 400
    assert seen == []


def test_unique_paths_and_cleanup(setup):
    client, seen = setup
    for _ in range(2):
        result = client.post("/predict", data={"file": (png_bytes(), "../../same.PNG")})
        assert result.status_code == 200
        assert b"42.50%" in result.data
        assert b"not a calibrated disease probability" in result.data
    assert seen[0] != seen[1]
    assert all(not path.exists() and not path.parent.exists() for path in seen)


def test_oversized_request(setup):
    client, seen = setup
    client.application.config["MAX_CONTENT_LENGTH"] = 100
    assert client.post("/predict", data={"file": (png_bytes(), "sample.png")}).status_code == 413
    assert seen == []


def test_pixel_limit(setup, monkeypatch):
    import app
    client, seen = setup
    monkeypatch.setattr(app, "MAX_PIXELS", 100)
    assert client.post("/predict", data={"file": (png_bytes(), "large.png")}).status_code == 400
    assert seen == []


@pytest.mark.parametrize("error,status", [(RuntimeError("private model path"), 503), (OSError("private image path"), 500)])
def test_failure_cleanup_and_no_detail_leak(error, status):
    seen = []

    def fail(path, _model):
        seen.append(path)
        raise error

    client = create_app({"TESTING": True}, fail).test_client()
    result = client.post("/predict", data={"file": (png_bytes(), "sample.png")})
    assert result.status_code == status
    assert b"private" not in result.data
    assert not seen[0].parent.exists()


def test_template_and_model_paths_do_not_depend_on_working_directory(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    application = create_app({"TESTING": True})
    assert application.test_client().get("/").status_code == 200
    assert application.config["MODEL_PATH"].is_absolute()
