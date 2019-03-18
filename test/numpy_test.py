# -*- coding: utf-8 -*-
import numpy as np


if __name__ == "__main__":
    array = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int)
    print(array)

    a = np.zeros((2, 3))
    print(a)

    b = np.empty((2, 3), dtype=np.int)
    print(b)
    print()
    a = np.array([[1, 1], [0, 1]], dtype=np.int)
    b = np.arange(4).reshape((2, 2))
    c = np.dot(a, b)
    print(a)
    print(b)
    print(c)
