# Brain Tumor Image Classification — Educational Prototype

**Status: prototype.** Educational / research image-classification prototype. **Not intended for medical diagnosis.**

## Purpose

Practice a small convolutional neural network, image preprocessing and Flask integration. The model returns two class scores for a resized image. It cannot establish a diagnosis, image suitability or clinical reliability.

## Implemented features and technologies

- CNN training with three convolution/pooling stages, a dense layer, dropout and a two-class softmax output.
- Local JPEG/PNG upload form with size/content checks, temporary storage and cleanup.
- Single-image CLI inference without loading training data or retraining.
- Explicit setup errors and a local-only development server.
- Python, TensorFlow/Keras, OpenCV, Pillow, NumPy, Flask and scikit-learn (training split).

## Structure and compatibility

Source and trained models remain at root so old paths are not broken:

```text
app.py                         Flask entry point
brain_tumor.py                 Shared inference/preprocessing
mainTrain.py                   Explicit training command
mainTest.py                    Single-image prediction command
templates/brain_tumor.html     Flask UI
BrainTumor10EpochsCategorical.h5  Original two-class model (used)
BrainTumor10Epochs.h5          Original one-output model (preserved, not interchangeable)
ml/brain-tumor-classification/ README, requirements, examples and tests
archive/brain-tumor-original/  Original scripts, retained for comparison
```

The categorical HDF5 metadata records Keras 3.3.3; the other model records Keras 2.4.0 and has one output. These are distinct artifacts, not duplicates. Neither saved model was modified. The unrelated root `Untitled57.ipynb` draws a random smoothie chart; no matching training notebook or dataset is supplied.

## Run locally

Use **Python 3.11 or 3.12** for the documented TensorFlow compatibility environment. Python 3.14 is not the target for this pinned TensorFlow build. Run these commands from the repository root:

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r ml/brain-tumor-classification/requirements.txt
python app.py
```

On Windows, use `py -3.12 -m venv .venv` and activate with `.venv\Scripts\activate`. Open `http://127.0.0.1:5000`. Keep the service local and use non-sensitive sample images.

The default model resolves relative to the script, not the working directory. To select a different **trusted two-output** model, set the `BRAIN_TUMOR_MODEL_PATH` process environment variable before starting. The example file documents the setting; there is no automatic `.env` loader. No API key is required.

The UI loads without eagerly importing TensorFlow. A missing/incompatible model produces a 503 setup message when predicting; installing only test dependencies does not enable real inference.

### CLI inference

```sh
python mainTest.py /absolute/path/to/sample.png
```

An optional `--model /absolute/path/to/model.h5` selects another trusted categorical model. The CLI processes local files and is not an upload boundary; use appropriately sized sample images. It does not read pickle files, fit a model or save weights.

## Training and missing data

The dataset is **not included**. Supply authorized JPEG samples under `datasets/no/` and `datasets/yes/`, then run:

```sh
python mainTrain.py --dataset /absolute/path/to/datasets
```

The architecture, split (`test_size=0.2`, `random_state=0`), training normalization, batch size 16, nine epochs and `shuffle=False` are preserved. The default new output is `ml/brain-tumor-classification/models/BrainTumor9EpochsCategorical.h5`, matching the configured epoch count. Existing output files are not overwritten; pass a new `--output` path for another run. The historical `10Epochs` filenames remain unchanged because their full training provenance cannot be reconstructed.

The code now checks class folders, JPEG decoding and output collisions. These checks do not establish class balance, sufficient data, subject-independent splits or reproducible training. No training run or performance benchmark is claimed without the dataset.

## Preserved behavior and important limitations

| Component | Existing behavior retained |
| --- | --- |
| Web prediction | Class-1 score × 100; “Yes” when score is at least **30%** |
| CLI prediction | Class-1 score × 100; “Yes” when score is at least **50%** |
| Inference input | OpenCV BGR array → Pillow resize to 64×64 → float32 divided by 255 → batch dimension |
| Training input | OpenCV-loaded image arrays normalized with `keras.utils.normalize(axis=1)` |

**Both thresholds are manual and not medically validated.** Scores are not calibrated disease probabilities. Training/inference normalization differs, and OpenCV's BGR channel ordering is retained rather than silently corrected. Aligning preprocessing, changing thresholds or retraining requires a separate experiment with appropriate evaluation. The original prediction script's retraining block is preserved in the archive, not in the supported inference path.

No diagnostic accuracy, sensitivity, specificity, deployment readiness or clinical validation is claimed. The model can score arbitrary non-scan images; a successful request is not evidence of useful prediction.

## Tests and verification

Lightweight upload/preprocessing tests can run without TensorFlow:

```sh
python -m pip install -r ml/brain-tumor-classification/requirements-test.txt
python -m pytest -q ml/brain-tumor-classification/tests
```

Tests cover invalid/missing files, mismatched file content, request/pixel limits, unique temporary paths, cleanup on failure, safe setup errors, launch-directory independence, preserved preprocessing and threshold behavior. Predictor doubles are used for boundary tests; they do not validate learned weights.

A separate local smoke run loaded the original categorical HDF5 and performed inference on a generated RGB image. Verified environment: Python 3.12.14, TensorFlow 2.16.2, Keras 3.15.1, NumPy 1.26.4, OpenCV 4.11.0, Pillow 12.3.0 and Flask 3.1.3. See [changes and validation](../../CHANGES_SUMMARY.md#validation). This older TensorFlow pin is for artifact compatibility, not a production security recommendation; consult [TensorFlow's installation guide](https://www.tensorflow.org/install/pip) before changing runtime/platform versions.

## Screenshots

No original screenshot could be confidently attributed to this Flask UI. Run the app to view it; unrelated screenshots are not presented as model evidence.

## Future improvements

Document dataset provenance and consent, prevent subject leakage, align preprocessing in a measured experiment, compare baselines, report uncertainty, and calibrate/justify any threshold. Separate training artifacts with versioned metadata and add real-model regression fixtures using licensed non-sensitive images. Read the [security notes](../../SECURITY_NOTES.md) before extending the service.
