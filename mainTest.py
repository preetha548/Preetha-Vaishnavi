"""Single-image prediction only; no data unpickling or retraining."""
import argparse
from pathlib import Path

from brain_tumor import CLI_THRESHOLD, DEFAULT_MODEL, predict_file


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path, help="Path to a trusted local sample image")
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    args = parser.parse_args()
    if not args.image.is_file():
        parser.error("The image path does not exist.")
    try:
        score, result = predict_file(args.image, args.model, CLI_THRESHOLD)
    except (RuntimeError, ValueError) as exc:
        parser.exit(1, f"Prediction unavailable: {exc}\n")
    print("Educational / research prototype. Not intended for medical diagnosis.")
    print(f"Class-1 score: {score:.2f}% (not a calibrated disease probability)")
    print(f"Legacy threshold output: {result}; manual threshold: {CLI_THRESHOLD:g}%")


if __name__ == "__main__":
    main()
