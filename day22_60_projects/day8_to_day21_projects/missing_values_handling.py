"""
Project Title: Missing Values Handling (Data Cleaning)

Project Description:
Demonstrates detecting, counting, filling and dropping missing values using
Pandas. Shows before and after views.

Concepts Used:
- pandas DataFrame, isnull, fillna, dropna

Run:
python missing_values_handling.py
"""

import pandas as pd
import os


DEFAULT_CSV = 'sample_weather_data.csv'


def main():
    print('Missing Values Handling')
    try:
        path = input(f"Enter CSV path (default: {DEFAULT_CSV}): ").strip() or DEFAULT_CSV
        if not os.path.exists(path):
            print('CSV file not found.')
            return

        df = pd.read_csv(path)
        print('\nOriginal data sample:')
        print(df.head())

        print('\nMissing values per column:')
        print(df.isnull().sum())

        # Fill numeric missing values with column mean
        numeric_cols = df.select_dtypes(include='number').columns
        df_filled = df.copy()
        for col in numeric_cols:
            mean_val = df[col].mean()
            df_filled[col].fillna(mean_val, inplace=True)

        # Drop rows where all elements are missing
        df_dropped = df.dropna(how='all')

        print('\nAfter filling numeric missing values (show sample):')
        print(df_filled.head())

        print('\nAfter dropping all-empty rows (show sample):')
        print(df_dropped.head())

    except Exception as exc:
        print(f'Error: {exc}\nMake sure pandas is installed: pip install pandas')


if __name__ == '__main__':
    main()
