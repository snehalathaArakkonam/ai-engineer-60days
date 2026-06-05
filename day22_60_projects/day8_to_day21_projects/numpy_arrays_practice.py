"""
Project Title: NumPy Arrays Practice

Project Description:
Examples demonstrating NumPy array creation, indexing, slicing, reshaping,
and basic mathematical operations. Requires `numpy` installed.

Concepts Used:
- numpy arrays, slicing, reshaping, broadcasting

Run:
python numpy_arrays_practice.py
"""

import numpy as np


def main():
    print('NumPy Arrays Practice')
    # Create arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    print('\n1D array:', arr1)

    # Indexing
    print('First element:', arr1[0])
    print('Last element:', arr1[-1])

    # Slicing
    print('Slice [1:4]:', arr1[1:4])

    # Reshaping
    arr2 = np.arange(1, 13)
    print('\nOriginal arr2:', arr2)
    arr2_reshaped = arr2.reshape((3, 4))
    print('Reshaped to 3x4:\n', arr2_reshaped)

    # Mathematical operations
    print('\nSum of arr1:', arr1.sum())
    print('Mean of arr1:', arr1.mean())
    print('arr1 * 2:', arr1 * 2)

    # Broadcasting example
    mat = np.array([[1, 2, 3], [4, 5, 6]])
    vec = np.array([10, 20, 30])
    print('\nMatrix:\n', mat)
    print('Vector:', vec)
    print('Matrix + Vector (broadcast):\n', mat + vec)


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f'Error: {exc}\nMake sure numpy is installed: pip install numpy')
