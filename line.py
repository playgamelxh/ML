# -*- coding: utf-8 -*-

# 最小二乘法，线性回归
import numpy as np
import matplotlib.pyplot as plt
data = np.array([
    [1, 6],
    [2, 5],
    [3, 7],
    [4, 10]
])
m = len(data)
X = np.array([np.ones(m), data[:, 0]]).T
print("X:", X)
y = np.array(data[:, 1]).reshape(-1, 1)
print("y:", y)
# # 求解XW=y的值，W
W = np.linalg.solve(X.T.dot(X), X.T.dot(y))
print("W:", W)

# show
plt.figure(1)
xx = np.linspace(0, 5, 2)
yy = np.array(W[0] + W[1] * xx)
plt.plot(xx, yy.T, color='b')
plt.scatter(data[:, 0], data[:, 1], color='r')
plt.show()
