# Glass Type Prediction Using Machine Learning

This project uses the uploaded glass composition dataset to predict glass category (Type)
from nine chemical/refractive features: RI, Na, Mg, Al, Si, K, Ca, Ba and Fe.

## Files
- `glass_type_prediction.py` - complete training, evaluation, chart generation and prediction program
- `glass_dataset.csv` - dataset extracted from the uploaded file
- `glass_type_model.pkl` - generated after running the program
- `Glass_Charts/` - generated visualization images

## Requirements
Python 3.10 or newer, pandas, numpy, matplotlib, scikit-learn and joblib.

## Install packages (Windows)
```bash
py -m pip install pandas numpy matplotlib scikit-learn joblib
```

## Run
Open Command Prompt in this folder and run:
```bash
py glass_type_prediction.py
```

The program trains a Random Forest classifier, prints evaluation results, saves charts and the model,
then asks for nine numeric values to predict a glass type.

Note: prediction is an educational classification result, not a certified material-testing result.
