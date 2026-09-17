# Contributing

Keep changes small, truthful and easy to review. Start with the audit and the README for the project you plan to change.

1. Work on a branch and preserve unrelated experiments.
2. Keep historical folder names unless all incoming and relative references are understood. Archive uncertain artifacts rather than deleting them.
3. Document the real scope, dependencies, exact run command, limitations and author/media credits. Do not label a rule-based demo as trained AI or a visual form as a working service.
4. Use isolated Python environments and project-local Node dependencies. Never commit `.env`, credentials, uploaded images, real personal records or generated datasets.
5. For behavior changes, test relevant failure cases as well as the happy path. Check relative links and mobile/keyboard behavior for changed interfaces.
6. Make focused commits and describe validation results and remaining blockers. Do not invent metrics, screenshots, deployment links or authorship.

## Validation

Run the relevant featured-project checks documented in its README. `python3 scripts/check_repository.py` checks maintained Markdown links, preservation of archived moves and Python/JavaScript syntax where supported. Historical archived course links and ZIP contents are not active documentation.

Do not run unknown model, pickle, archive or script files from third parties. Use only the repository’s known artifacts and synthetic fixtures for local verification.
