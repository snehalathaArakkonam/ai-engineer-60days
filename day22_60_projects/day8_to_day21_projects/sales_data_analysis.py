"""
Project Title: Sales Data Analysis (Mini Project)

Project Description:
Load `sample_sales_data.csv` and perform total, average, highest, lowest sales,
monthly analysis and category-wise analysis. Produce bar and line charts saved
to files and print simple business insights.

Concepts Used:
- pandas for data analysis
- matplotlib for charts
- groupby and aggregation

Run:
python sales_data_analysis.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import os


DEFAULT_CSV = 'sample_sales_data.csv'


def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"CSV not found: {path}")
    return pd.read_csv(path, parse_dates=['date'])


def main():
    print('Sales Data Analysis')
    try:
        path = input(f"Enter sales CSV path (default: {DEFAULT_CSV}): ").strip() or DEFAULT_CSV
        df = load_data(path)

        # Ensure total_sales exists or compute
        if 'total_sales' not in df.columns:
            df['total_sales'] = df['quantity'] * df['unit_price']

        total_sales = df['total_sales'].sum()
        avg_sales = df['total_sales'].mean()
        max_row = df.loc[df['total_sales'].idxmax()]
        min_row = df.loc[df['total_sales'].idxmin()]

        print(f"Total Sales: ${total_sales:.2f}")
        print(f"Average Sale: ${avg_sales:.2f}")
        print(f"Highest Sale: ${max_row['total_sales']:.2f} (Product: {max_row['product']}, Date: {max_row['date'].date()})")
        print(f"Lowest Sale: ${min_row['total_sales']:.2f} (Product: {min_row['product']}, Date: {min_row['date'].date()})")

        # Monthly sales analysis
        df['month'] = df['date'].dt.to_period('M')
        monthly = df.groupby('month')['total_sales'].sum().sort_index()
        print('\nMonthly Sales:')
        print(monthly)

        # Category-wise analysis
        cat = df.groupby('category')['total_sales'].sum().sort_values(ascending=False)
        print('\nCategory-wise Sales:')
        print(cat)

        # Plot monthly sales (line)
        plt.figure()
        monthly.index = monthly.index.astype(str)
        plt.plot(monthly.index, monthly.values, marker='o')
        plt.title('Monthly Total Sales')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('monthly_sales_line.png')
        print('Saved monthly_sales_line.png')

        # Plot category sales (bar)
        plt.figure()
        cat.plot(kind='bar')
        plt.title('Category-wise Sales')
        plt.xlabel('Category')
        plt.ylabel('Total Sales')
        plt.tight_layout()
        plt.savefig('category_sales_bar.png')
        print('Saved category_sales_bar.png')

        # Business insights
        top_cat = cat.idxmax()
        print(f"\nBusiness Insight: Top category by sales is '{top_cat}'")

    except Exception as exc:
        print(f'Error: {exc}\nMake sure pandas and matplotlib are installed: pip install pandas matplotlib')


if __name__ == '__main__':
    main()
