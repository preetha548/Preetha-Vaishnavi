"""Regression checks on input preprocessing and manual thresholds."""
import sys
from pathlib import Path

import cv2
import numpy as np
import pytest
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
import brain_tumor


def test_preprocessing_matches_original(tmp_path):
    path = tmp_path / "sample.png"
    pixels = np.arange(15 * 19 * 3, dtype=np.uint8).reshape(15, 19, 3)
    Image.fromarray(pixels).save(path)
    original = np.expand_dims(np.array(Image.fromarray(cv2.imread(str(path))).resize((64, 64))).astype("float32") / 255.0, axis=0)
    np.testing.assert_array_equal(brain_tumor.preprocess_image(path), original)


@pytest.mark.parametrize("value,web,cli", [(0.25, "No", "No"), (0.30, "Yes", "No"), (0.50, "Yes", "Yes")])
def test_thresholds_preserved(monkeypatch, value, web, cli):
    class FakeModel:
        def predict(self, _image, verbose=0):
            return np.array([[1 - value, value]])

    monkeypatch.setattr(brain_tumor, "load_model", lambda _path: FakeModel())
    monkeypatch.setattr(brain_tumor, "preprocess_image", lambda _path: np.zeros((1, 64, 64, 3)))
    assert brain_tumor.predict_file("unused")[1] == web
    assert brain_tumor.predict_file("unused", threshold=brain_tumor.CLI_THRESHOLD)[1] == cli


def test_missing_model_has_setup_error(tmp_path):
    with pytest.raises(RuntimeError, match="Model unavailable"):
        brain_tumor.load_model(str(tmp_path / "missing.h5"))


def test_one_class_model_is_rejected(monkeypatch):
    class BinaryModel:
        def predict(self, _image, verbose=0):
            return np.array([[0.8]])

    monkeypatch.setattr(brain_tumor, "load_model", lambda _path: BinaryModel())
    monkeypatch.setattr(brain_tumor, "preprocess_image", lambda _path: np.zeros((1, 64, 64, 3)))
    with pytest.raises(RuntimeError, match="two-class"):
        brain_tumor.predict_file("unused")
