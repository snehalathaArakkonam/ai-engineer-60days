"""
Project Title: Matplotlib Charts (Line, Bar, Pie)

Project Description:
Create line, bar and pie charts using matplotlib. Uses simple sample data and
saves charts as images in the working directory.

Concepts Used:
- matplotlib plotting, labels, titles, saving figures

Run:
python matplotlib_charts.py
"""

import matplotlib.pyplot as plt


def main():
    print('Matplotlib Charts')
    # Sample data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [150, 200, 250, 220, 300, 310]

    # Line chart
    plt.figure()
    plt.plot(months, sales, marker='o')
    plt.title('Monthly Sales (Line)')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.savefig('line_chart.png')
    print('Saved line_chart.png')

    # Bar chart
    plt.figure()
    plt.bar(months, sales, color='skyblue')
    plt.title('Monthly Sales (Bar)')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.savefig('bar_chart.png')
    print('Saved bar_chart.png')

    # Pie chart
    categories = ['A', 'B', 'C', 'D']
    values = [40, 25, 20, 15]
    plt.figure()
    plt.pie(values, labels=categories, autopct='%1.1f%%')
    plt.title('Category Distribution (Pie)')
    plt.savefig('pie_chart.png')
    print('Saved pie_chart.png')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f'Error: {exc}\nEnsure matplotlib is installed: pip install matplotlib')
