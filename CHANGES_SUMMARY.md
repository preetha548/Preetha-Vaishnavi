# Changes Summary

This repository was reorganized into a truthful junior-developer portfolio for Preetha Vaishnavi. The work keeps the original projects available for review, documents their real status, and fixes only the areas needed to make the featured work safer and easier to understand.

No GitHub push or public deployment was performed from this workspace.

## Main portfolio updates

- Added a professional root [README](README.md) with Preetha's learning profile, skills evidenced by the repository, featured work and contact details.
- Added [PROJECTS.md](PROJECTS.md) as a categorized index for all 117 project folders.
- Added hub pages for [web](web/README.md), [machine learning](ml/README.md), [data analysis](data-analysis/README.md), [Node projects](node-projects/README.md) and miscellaneous [projects](projects/README.md).
- Added [REPOSITORY_AUDIT.md](REPOSITORY_AUDIT.md) to record the original repository state before the portfolio cleanup.
- Added [SECURITY_NOTES.md](SECURITY_NOTES.md) for security findings and practical remediation priorities.
- Added [FLAGSHIP_PROJECT_PLAN.md](FLAGSHIP_PROJECT_PLAN.md) for a future employee analytics platform, clearly marked as a roadmap.

## Featured project guides

Five projects now have reviewer-friendly guides:

- [Brain tumor classification prototype](ml/brain-tumor-classification/README.md)
- [Company IT Prediction analysis](<Company IT Prediction analysis/README.md>)
- [Marketing Website](<Marketing Website/README.md>)
- [Jewellery Website](<Jewellery Website/README.md>)
- [Rock Paper Scissors](<rock paper scissors/README.md>)

The guides describe what each project actually does, how to run it, what was verified, and what still needs improvement.

## Safe file organization

Seventy-nine loose or obsolete root-level files were moved into archive folders without rewriting their contents. The move list is recorded in [archive/MOVED_FILES.md](archive/MOVED_FILES.md).

The main move groups were:

- 61 loose screenshot/image files moved into [screenshots/archive](screenshots/archive/).
- 5 empty unused root placeholders moved into [archive/unused](archive/unused/).
- `Projects.zip` moved into [archive/Projects.zip](archive/Projects.zip).
- 12 old GitHub Skills workflow files moved into [archive/github-skills](archive/github-skills/).

The earlier personal page made for Preetha is not part of this repository cleanup. It was moved outside the repository to `/Users/helvinjohnson/Documents/preetha-personal-page`.

## Brain tumor prototype fixes

The root Flask prototype was updated as an educational demo while preserving the original model behavior:

- Kept the original categorical `.h5` artifact unchanged.
- Preserved the original preprocessing path used by the legacy script, including 64x64 resizing and the OpenCV/Pillow data flow.
- Added `brain_tumor.py` so model loading and inference are isolated and testable.
- Reworked `app.py` with an app factory, safer upload validation, temporary-file cleanup, explicit error responses and no debug public server.
- Added an educational/non-medical disclaimer to the web UI and documentation.
- Replaced the old retraining-on-test behavior in `mainTest.py` with inference-only CLI behavior.
- Updated `mainTrain.py` so training requires an explicit dataset path and writes a new output model without overwriting the original artifact by default.
- Archived exact copies of the original scripts in [archive/brain-tumor-original](archive/brain-tumor-original/).

## Targeted frontend fixes

The Jewellery Website and Marketing Website were kept close to their original designs, with targeted repairs:

- Jewellery Website JavaScript was simplified to one guarded setup path, avoiding duplicate handlers and syntax issues.
- Jewellery Website contact form is clearly marked as a static demo, so it no longer suggests a live backend submission.
- Marketing Website carousel controls received clearer accessible state labels and the page count now matches the actual two-page carousel.
- Rock Paper Scissors gained a small Node.js test suite for all nine rule combinations, persistence and reset behavior.

## Validation

The following checks were run locally:

- Brain tumor Flask/inference tests: `18 passed`.
- Rock Paper Scissors logic tests: `10 passed`.
- Real categorical HDF5 model loaded in a TensorFlow 2.16.2 environment and produced a two-class prediction on a generated image.
- Brain tumor training CLI was checked for the missing-dataset path and exits safely instead of silently retraining.
- Company IT Prediction analysis smoke run completed with a non-interactive Matplotlib backend.
- Featured JavaScript syntax was checked with Node.js.
- Python source syntax was checked.
- Maintained Markdown links and anchors were checked.
- The root README was rendered in a local Markdown preview and inspected visually.
- The Marketing Website and Jewellery Website were opened in a browser and checked for the main interaction paths.
- All original tracked files were accounted for against baseline commit `663ccbe3c51ac2441f059395f7a7f44d1f2c0016`; archived moves were hash-checked except for the intentionally edited files.

## Remaining limitations

This cleanup does not make every project production-ready. Many older demos still have missing manifests, missing public/static folders, placeholder code, broken external assets, localStorage-only authentication, or incomplete backend wiring. These are documented rather than hidden.

The Company IT Prediction project still uses synthetic data generated inside the script. It should not be presented as a hiring, HR, attrition or operational model.

The brain tumor prototype remains an educational image-classification demo. It is not a medical device, diagnostic tool or clinical workflow. The displayed score is a model class score, not a calibrated disease probability.

## Recommended next work

- Pick one flagship project and finish it end-to-end instead of trying to polish all demos at once.
- Replace localStorage password demos with proper authentication patterns before publishing any login-style project.
- Add package manifests and simple run checks to the strongest web projects.
- Replace broken or externally dependent image assets with committed project-local assets.
- Build the employee analytics roadmap from [FLAGSHIP_PROJECT_PLAN.md](FLAGSHIP_PROJECT_PLAN.md) as a fresh project with real validation boundaries.
