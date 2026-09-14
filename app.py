"""Local educational image-classification demo. Not for medical diagnosis."""
import os
from pathlib import Path
from tempfile import TemporaryDirectory

from flask import Flask, render_template, request
from PIL import Image, UnidentifiedImageError
from werkzeug.utils import secure_filename

from brain_tumor import DEFAULT_MODEL, ROOT, WEB_THRESHOLD, predict_file

MAX_PIXELS = 16_000_000
FORMATS = {".jpg": "JPEG", ".jpeg": "JPEG", ".png": "PNG"}


def validate_image(path, extension):
    """Check the decoded format and pixel budget, not just the filename."""
    try:
        with Image.open(path) as uploaded:
            if uploaded.format != FORMATS[extension]:
                raise ValueError("The file content must match its JPEG or PNG extension.")
            if uploaded.width * uploaded.height > MAX_PIXELS:
                raise ValueError("Use an image with at most 16 million pixels.")
            uploaded.verify()
    except (UnidentifiedImageError, OSError, Image.DecompressionBombError) as exc:
        raise ValueError("Upload a valid, undamaged JPEG or PNG image.") from exc


def create_app(config=None, predictor=None):
    application = Flask(__name__, template_folder=str(ROOT / "templates"))
    model_path = Path(os.environ.get("BRAIN_TUMOR_MODEL_PATH", str(DEFAULT_MODEL)))
    application.config.update(
        MAX_CONTENT_LENGTH=6 * 1024 * 1024,
        MODEL_PATH=model_path if model_path.is_absolute() else ROOT / model_path,
    )
    if config:
        application.config.update(config)
    predict = predictor or predict_file

    def page(status=200, **context):
        return render_template("brain_tumor.html", threshold=WEB_THRESHOLD, **context), status

    @application.get("/")
    def index():
        return page()

    @application.post("/predict")
    def upload():
        uploaded = request.files.get("file")
        if uploaded is None or not uploaded.filename:
            return page(400, error="Choose a JPEG or PNG image first.")
        extension = Path(secure_filename(uploaded.filename)).suffix.lower()
        if extension not in FORMATS:
            return page(400, error="Only JPEG and PNG images are accepted.")
        # A new private directory per request prevents traversal and collisions.
        # The original filename is never used on disk; cleanup also runs on errors.
        try:
            with TemporaryDirectory(prefix="brain-tumor-") as folder:
                path = Path(folder) / ("image" + extension)
                uploaded.save(path)
                validate_image(path, extension)
                score, binary_result = predict(path, application.config["MODEL_PATH"])
            return page(score=score, binary_result=binary_result)
        except ValueError as exc:
            return page(400, error=str(exc))
        except RuntimeError:
            application.logger.warning("Inference unavailable; check the local model environment.")
            return page(503, error="The model is unavailable. Check the model path and project setup guide.")
        except Exception:
            # Do not log submitted filenames, image data, or arbitrary exception text.
            application.logger.error("Image processing failed.")
            return page(500, error="The image could not be processed. Please try another sample image.")

    @application.errorhandler(413)
    def too_large(_error):
        return page(413, error="The upload request must be smaller than 6 MB.")

    @application.after_request
    def response_headers(response):
        response.headers["Cache-Control"] = "no-store"
        response.headers["X-Content-Type-Options"] = "nosniff"
        return response

    return application


app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
