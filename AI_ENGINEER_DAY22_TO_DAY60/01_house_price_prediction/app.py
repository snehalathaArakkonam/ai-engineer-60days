"""House Price Prediction application."""

import os
import joblib
import pandas as pd


MODEL_FILENAME = "house_price_model.joblib"
DATASET_FILENAME = "dataset.csv"


def load_model():
    """Load the pre-trained model from disk."""
    model_path = os.path.join(os.path.dirname(__file__), MODEL_FILENAME)
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Model file not found. Run model_training.py first to create {MODEL_FILENAME}."
        )
    return joblib.load(model_path)


def prompt_for_value(prompt_text):
    """Prompt the user for a floating point value."""
    while True:
        try:
            value = float(input(prompt_text).strip())
            return value
        except ValueError:
            print("Invalid input. Enter a numeric value.")


def get_sample_data():
    """Load the dataset and return sample rows when requested."""
    dataset_path = os.path.join(os.path.dirname(__file__), DATASET_FILENAME)
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")
    data = pd.read_csv(dataset_path)
    return data


def main():
    """Run the prediction application."""
    try:
        print("House Price Prediction")
        print("Enter the property details to predict median house value.")
        print("To see sample dataset rows, type SAMPLE and press Enter.")

        user_input = input("Type SAMPLE or press Enter to continue: ").strip().upper()
        if user_input == "SAMPLE":
            sample_data = get_sample_data()
            print(sample_data.head())
            return

        med_inc = prompt_for_value("Median Income (10k USD): ")
        house_age = prompt_for_value("House Age (years): ")
        ave_rooms = prompt_for_value("Average Rooms: ")
        ave_bedrms = prompt_for_value("Average Bedrooms: ")
        population = prompt_for_value("Neighborhood Population: ")
        ave_occup = prompt_for_value("Average Occupants: ")
        latitude = prompt_for_value("Latitude: ")
        longitude = prompt_for_value("Longitude: ")

        model = load_model()
        features = [
            med_inc,
            house_age,
            ave_rooms,
            ave_bedrms,
            population,
            ave_occup,
            latitude,
            longitude,
        ]
        prediction = model.predict([features])[0]
        print(f"Predicted Median House Value: {prediction:.3f} (in 100k USD)")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
