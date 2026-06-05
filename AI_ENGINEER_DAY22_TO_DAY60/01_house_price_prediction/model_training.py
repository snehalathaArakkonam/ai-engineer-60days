"""Train and save a house price prediction model."""

import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import joblib


def load_dataset(csv_path):
    """Load dataset from CSV file."""
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Dataset not found: {csv_path}")
    data = pd.read_csv(csv_path)
    return data


def prepare_features(data):
    """Prepare features and target for training."""
    features = data.drop(columns=["MedHouseVal"])
    target = data["MedHouseVal"]
    return features, target


def train_model(features, target):
    """Train a random forest regression model."""
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    return model, mse, r2


def save_model(model, output_path):
    """Save trained model to disk."""
    directory = os.path.dirname(output_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    joblib.dump(model, output_path)


def main():
    """Train the model and save it."""
    dataset_path = os.path.join(os.path.dirname(__file__), "dataset.csv")
    model_path = os.path.join(os.path.dirname(__file__), "house_price_model.joblib")
    try:
        data = load_dataset(dataset_path)
        features, target = prepare_features(data)
        model, mse, r2 = train_model(features, target)
        save_model(model, model_path)
        print(f"Training completed. MSE: {mse:.4f}, R2: {r2:.4f}")
        print(f"Model saved to: {model_path}")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
