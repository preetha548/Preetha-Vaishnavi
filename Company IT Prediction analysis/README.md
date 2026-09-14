# Employee Performance Analytics & Prediction

**Status: learning project.** Historical folder: `Company IT Prediction analysis`.

## Purpose

Explore relationships in a generated company-training dataset and practice classification. All 200 employee records are synthetic, created with NumPy's seeded random generator. These are not actual employee records or evidence of workplace predictive validity.

## Implemented features

- Department, training, attendance, test-score, experience and project-count sample fields.
- pandas data inspection, descriptive statistics and missing-value counts.
- Thirty numbered chart sections: distributions, comparisons, pair plots, correlations, trends and a confusion matrix; an additional feature-importance chart.
- RandomForestClassifier with 100 estimators and an 80/20 split using `random_state=42`.
- Printed holdout accuracy and feature importances for the synthetic exercise.

The outcome is derived from a synthetic performance formula and a median pass/fail split. The classifier learns this constructed relationship; its accuracy is not a measure of real employee performance prediction.

## Technologies

Python, NumPy, pandas, Matplotlib, Seaborn and scikit-learn.

## Run locally

From this directory, with Python 3.11 or newer:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

On Windows, activate with `.venv\Scripts\activate`. Close each chart window to continue; the script uses sequential `plt.show()` calls. No external dataset, credentials, database or web server is required.

For a non-interactive smoke run:

```sh
MPLBACKEND=Agg python app.py
```

This executes the analysis without opening windows; it does not save a new report or establish model quality. See [validation results](../CHANGES_SUMMARY.md#validation).

## Existing screenshots

These are original committed chart images, not newly benchmarked outputs:

![Training-data correlation heatmap](Training%20Data%20Correlation%20HeatMap.png)

[Performance distribution](Performance%20Distribution.png) · [Attendance vs performance](Attendance%20vs%20Performance.png) · [Average training hours](Average%20Training%20Hours.png)

## Limitations

- Single synthetic dataset and split, with no real-world generalization claim.
- Category encoders are reused and not exported with a pipeline.
- No saved model, API, authentication, database or dashboard.
- Charts are interactive windows, not a deployed analytics product.
- Opening many figures can consume memory; use the headless smoke command for validation.

## Future improvements

Separate data generation, plotting and modeling; close/save figures consistently; use a reusable preprocessing pipeline; add repeated evaluation and test fixtures. The [future flagship plan](../FLAGSHIP_PROJECT_PLAN.md) describes a separate full-stack application and is not implemented here.
