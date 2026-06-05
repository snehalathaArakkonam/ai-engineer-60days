"""Data loading and splitting utilities for House Price Prediction.

This module encapsulates dataset access and basic splitting logic. It uses the
California Housing dataset provided by scikit-learn to avoid external downloads
and to keep the project reproducible.
"""

from typing import Tuple

import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split


def load_california_housing() -> Tuple[pd.DataFrame, pd.Series]:
    """Load the California housing dataset and return features and target.

    Returns:
        X (pd.DataFrame): feature dataframe
        y (pd.Series): target series (median house value)
    """
    data = fetch_california_housing(as_frame=True)
    df = data.frame.copy()
    X = df.drop(columns=['MedHouseVal'])
    y = df['MedHouseVal']
    return X, y


def train_test_split_data(X: pd.DataFrame, y: pd.Series, test_size: float = 0.2, random_state: int = 42):
    """Split features and target into train and test sets.

    Args:
        X: feature dataframe
        y: target series
        test_size: fraction of data reserved for testing
        random_state: random seed for reproducibility

    Returns:
        X_train, X_test, y_train, y_test
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
