"""
Project Title: Data Visualizations (Histogram, Scatter, Box)

Project Description:
Create histogram, scatter plot and box plot using matplotlib and sample data.
Includes comments explaining each chart.

Concepts Used:
- matplotlib: histogram, scatter, boxplot
- statistical interpretation

Run:
python data_visualizations.py
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    print('Data Visualizations')
    # Sample distributions
    np.random.seed(0)
    data_normal = np.random.normal(loc=50, scale=10, size=200)
    data_x = np.random.rand(100) * 100
    data_y = data_x * 0.5 + np.random.normal(scale=10, size=100)

    # Histogram: shows distribution of a single numeric variable
    plt.figure()
    plt.hist(data_normal, bins=20, color='skyblue', edgecolor='black')
    plt.title('Histogram of Normally Distributed Data')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig('histogram.png')
    print('Saved histogram.png')

    # Scatter plot: relationship between two numeric variables
    plt.figure()
    plt.scatter(data_x, data_y, alpha=0.7)
    plt.title('Scatter Plot (x vs y)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('scatter.png')
    print('Saved scatter.png')

    # Box plot: summary of distribution with quartiles and outliers
    plt.figure()
    plt.boxplot([data_normal, data_x], labels=['normal', 'x'])
    plt.title('Box Plot Comparison')
    plt.savefig('boxplot.png')
    print('Saved boxplot.png')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f'Error: {exc} \nMake sure matplotlib and numpy are installed: pip install matplotlib numpy')
