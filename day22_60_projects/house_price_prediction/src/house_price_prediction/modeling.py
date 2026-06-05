"""Modeling utilities: build pipelines, train, evaluate and persist models."""

import json
import os
from typing import Dict, Tuple

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Default output locations
MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'models')
MODEL_FILENAME = 'best_model.joblib'
METRICS_FILENAME = 'metrics.json'


def build_model_pipelines() -> Dict[str, Pipeline]:
    """Return a dict of model name -> sklearn Pipeline objects."""
    pipelines = {
        'linear_regression': Pipeline([
            ('scaler', StandardScaler()),
            ('lr', LinearRegression())
        ]),
        'random_forest': Pipeline([
            ('scaler', StandardScaler()),
            ('rf', RandomForestRegressor(n_estimators=100, random_state=42))
        ])
    }
    return pipelines


def evaluate(model: Pipeline, X_test: pd.DataFrame, y_test: pd.Series) -> Dict[str, float]:
    """Return evaluation metrics for a trained model on test data."""
    preds = model.predict(X_test)
    rmse = float(np.sqrt(mean_squared_error(y_test, preds)))
    mae = float(mean_absolute_error(y_test, preds))
    r2 = float(r2_score(y_test, preds))
    return {'rmse': rmse, 'mae': mae, 'r2': r2}


def cross_val_rmse(model: Pipeline, X: pd.DataFrame, y: pd.Series, cv: int = 5) -> float:
    """Return mean RMSE from cross-validation (using neg_mean_squared_error)."""
    scores = cross_val_score(model, X, y, scoring='neg_mean_squared_error', cv=cv)
    rmse_scores = np.sqrt(-scores)
    return float(np.mean(rmse_scores))


def save_model_and_metrics(model: Pipeline, metrics: Dict, output_dir: str = MODEL_DIR) -> Tuple[str, str]:
    """Persist model and metrics to disk and return their paths."""
    os.makedirs(output_dir, exist_ok=True)
    model_path = os.path.join(output_dir, MODEL_FILENAME)
    metrics_path = os.path.join(output_dir, METRICS_FILENAME)
    joblib.dump(model, model_path)
    with open(metrics_path, 'w', encoding='utf-8') as f:
        json.dump(metrics, f, indent=2)
    return model_path, metrics_path


def load_model(path: str) -> Pipeline:
    """Load a persisted joblib model from disk."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found: {path}")
    return joblib.load(path)
