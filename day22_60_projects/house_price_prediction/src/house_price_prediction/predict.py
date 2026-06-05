"""Interactive and batch prediction utilities using a trained model."""

import json
import os
from typing import List

import pandas as pd

from .modeling import load_model


def interactive_predict(model_path: str, feature_names: List[str]):
    """Prompt the user for features and print a prediction."""
    model = load_model(model_path)
    print('\nInteractive prediction: enter feature values')
    values = []
    try:
        for feat in feature_names:
            while True:
                raw = input(f"{feat}: ").strip()
                try:
                    val = float(raw)
                    values.append(val)
                    break
                except ValueError:
                    print('Enter a numeric value')

        X_new = pd.DataFrame([values], columns=feature_names)
        pred = model.predict(X_new)[0]
        print(f"Predicted median house value: {pred:.3f}")
    except Exception as exc:
        print(f"Prediction failed: {exc}")


def batch_predict_csv(model_path: str, csv_path: str, output_path: str = None):
    """Run predictions on a CSV file with the same feature columns and save output."""
    model = load_model(model_path)
    df = pd.read_csv(csv_path)
    preds = model.predict(df)
    df['predicted_med_house_val'] = preds
    out = output_path or f"{os.path.splitext(csv_path)[0]}_predictions.csv"
    df.to_csv(out, index=False)
    print(f"Saved predictions to: {out}")
    return out
