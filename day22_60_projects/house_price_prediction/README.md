# House Price Prediction

This project implements a complete machine learning pipeline for predicting
median house values using the California Housing dataset provided by
scikit-learn. It is designed as a production-ready, well-documented example
for learning and portfolio use.

## Features

- Load and inspect dataset
- Preprocessing using scikit-learn pipelines
- Train multiple models (Linear Regression, Random Forest)
- Cross-validation and evaluation metrics (RMSE, MAE, R2)
- Save best model and metrics
- Interactive prediction using saved model

## Folder Structure

```
house_price_prediction/
├── train_predict.py        # Main script (train / predict)
├── requirements.txt       # Python dependencies
└── README.md
```

## Setup

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows PowerShell
```

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Train models and evaluate:

```bash
python train.py train --output-dir models
```

After training, the best model and metrics are saved under `models/`.

Use the saved model to make interactive predictions:

```bash
python train.py predict --model-path models/best_model.joblib
```

Batch prediction on a CSV (CSV must have the same features in order):

```bash
python train.py batch-predict --csv sample_input.csv --model-path models/best_model.joblib
```

Run tests:

```bash
pytest -q
```

You will be prompted to enter values for each feature.

## Notes

- This project uses `fetch_california_housing` from scikit-learn to avoid
  distributing datasets directly.
- The saved model is a joblib file for easy loading.
- Expand the project by adding hyperparameter tuning, persistence for trained
  models, model serving (FastAPI), or feature importance visualizations.
