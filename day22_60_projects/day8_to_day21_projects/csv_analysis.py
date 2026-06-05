"""
Project Title: CSV Analysis (Pandas Basics)

Project Description:
Read a CSV file, display rows/columns, summary statistics and filter data using
Pandas. Uses `sample_weather_data.csv` or any provided CSV.

Concepts Used:
- pandas DataFrame, read_csv, describe, filtering

Run:
python csv_analysis.py
"""

import pandas as pd
import os


DEFAULT_CSV = 'sample_weather_data.csv'


def main():
    print('CSV Analysis')
    try:
        path = input(f"Enter CSV file path (default: {DEFAULT_CSV}): ").strip() or DEFAULT_CSV
        if not os.path.exists(path):
            print(f"File not found: {path}")
            return

        df = pd.read_csv(path)
        print('\nFirst 5 rows:')
        print(df.head())

        print('\nColumns:')
        print(df.columns.tolist())

        print('\nSummary statistics:')
        print(df.describe(include='all'))

        # Example filter: temperature > 25 if column exists
        if 'temperature_C' in df.columns:
            hot = df[df['temperature_C'] > 25]
            print(f"\nRows with temperature_C > 25: {len(hot)}")
            print(hot.head())

    except Exception as exc:
        print(f'Error: {exc}\nMake sure pandas is installed: pip install pandas')


if __name__ == '__main__':
    main()
