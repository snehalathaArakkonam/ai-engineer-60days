"""Simple smoke tests for the house_price_prediction package."""

from src.house_price_prediction.data import load_california_housing


def test_load_dataset():
    X, y = load_california_housing()
    assert X.shape[0] == y.shape[0]
    assert X.shape[1] > 0
