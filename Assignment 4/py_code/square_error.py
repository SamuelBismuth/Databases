import numpy as np


def square_error(new_y, y):
    new_y = np.array(new_y, dtype='float64')
    y = np.array(y, dtype='float64')
    total = 0
    for index in range(len(y)):
        total += pow((new_y[index] - y[index]), 2)
    return total / len(y)
