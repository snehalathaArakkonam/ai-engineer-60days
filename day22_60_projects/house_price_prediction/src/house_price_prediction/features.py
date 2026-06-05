"""Feature engineering helpers for House Price Prediction.

This module provides deterministic, explainable feature transformations which
are commonly used for housing datasets.
"""

from typing import Tuple

import pandas as pd


def add_engineered_features(X: pd.DataFrame) -> pd.DataFrame:
    """Add a few engineered features and return a new DataFrame.

    Engineering is kept simple and numerical to remain beginner-friendly.
    Features added:
      - rooms_per_household
      - bedrooms_per_room
      - population_per_household

    Args:
        X: original feature dataframe

    Returns:
        X_new: dataframe with additional features
    """
    X_new = X.copy()
    # Ensure expected columns exist before computing
    # California dataset columns include: MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude
    if 'AveRooms' in X_new.columns and 'AveBedrms' in X_new.columns:
        # Avoid division by zero by adding a tiny epsilon where necessary
        eps = 1e-6
        X_new['bedrooms_per_room'] = X_new['AveBedrms'] / (X_new['AveRooms'] + eps)

    if 'Population' in X_new.columns and 'AveOccup' in X_new.columns:
        # Population per household estimate
        X_new['population_per_household'] = X_new['Population'] / (X_new['AveOccup'] + 1e-6)

    if 'AveRooms' in X_new.columns and 'AveOccup' in X_new.columns:
        X_new['rooms_per_household'] = X_new['AveRooms'] / (X_new['AveOccup'] + 1e-6)

    return X_new
