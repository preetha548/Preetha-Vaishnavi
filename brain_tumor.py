"""Shared legacy inference pipeline. Educational use only, not medical diagnosis."""
from functools import lru_cache
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent
DEFAULT_MODEL = ROOT / "BrainTumor10EpochsCategorical.h5"
INPUT_SIZE = 64
WEB_THRESHOLD = 30.0
CLI_THRESHOLD = 50.0


def preprocess_image(path):
    """Preserve the original OpenCV BGR -> Pillow -> float32 / 255 pipeline.

    Do not silently align this with training's axis-1 normalization: that would
    change the behavior of the existing prototype and needs separate evaluation.
    """
    pixels = cv2.imread(str(path))
    if pixels is None:
        raise ValueError("The image could not be decoded.")
    resized = Image.fromarray(pixels).resize((INPUT_SIZE, INPUT_SIZE))
    return np.expand_dims(np.asarray(resized).astype("float32") / 255.0, axis=0)


@lru_cache(maxsize=2)
def load_model(model_path):
    """Load only a trusted local model, without restoring its training optimizer."""
    path = Path(model_path)
    if not path.is_file():
        raise RuntimeError("Model unavailable. Check the configured model path.")
    try:
        from tensorflow.keras.models import load_model as keras_load_model
        return keras_load_model(str(path), compile=False)
    except (ImportError, OSError, ValueError, TypeError) as exc:
        raise RuntimeError("Model unavailable. Check the documented TensorFlow environment.") from exc


def predict_file(image_path, model_path=DEFAULT_MODEL, threshold=WEB_THRESHOLD):
    model = load_model(str(Path(model_path).resolve()))
    predictions = np.asarray(model.predict(preprocess_image(image_path), verbose=0))
    if predictions.shape != (1, 2) or not np.isfinite(predictions).all():
        raise RuntimeError("Expected a finite two-class model output.")
    score = float(predictions[0][1]) * 100
    if not 0 <= score <= 100:
        raise RuntimeError("Expected a class score between zero and one.")
    return score, "Yes" if score >= threshold else "No"
