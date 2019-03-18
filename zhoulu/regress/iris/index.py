# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()
x = iris.data
y = iris.target
# print(x)
# print(y)
DD = iris.data
X = [x[0] for x in DD]
Y = [x[1] for x in DD]

# # 散点图绘制
# plt.scatter(X[:50], Y[:50], color='red', marker='o', label='setosa')
# plt.scatter(X[50:100], Y[50:100], color='blue', marker='x', label='versicolor')
# plt.scatter(X[100:], Y[100:], color='green', marker='+', label='Virginica')
# plt.legend(loc=2)
# plt.show()

# 逻辑回归
X = X = iris.data[:, :2]
# X = X = X = X = iris.data[:, :4]
Y = iris.target
lr = LogisticRegression(C=1e5)
lr.fit(X, Y)
# print(lr)

# meshgrid函数生成两个网格矩阵
h = 0.02
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
# x1_min, x1_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
# x2_min, x2_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
# x3_min, x3_max = X[:, 2].min() - 0.5, X[:, 2].max() + 0.5
# x4_min, x4_max = X[:, 3].min() - 0.5, X[:, 3].max() + 0.5
# x1x, x2x, x3x, x4x = np.meshgrid(np.arange(x1_min, x1_max, h), np.arange(x2_min, x2_max, h), np.arange(x3_min, x3_max, h), np.arange(x4_min, x4_max, h))

# pcolormesh函数xx, yy两个网格举证和对应的预测结构Z绘制在图片上
# 预测
Z = lr.predict(np.c_[xx.ravel(), yy.ravel()])
# Z = lr.predict(np.c_[x1x.ravel(), x2x.ravel(), x3x.ravel(), x4x.ravel()])
# 调用reshape()函数修改形状，将其Z转换为两个特征（长度和宽度）
Z = Z.reshape(xx.shape)
# 尺寸参数
plt.figure(1, figsize=(8, 6))
# 调用pcolormesh()函数将xx、yy两个网格矩阵和对应的预测结果Z绘制在图片上
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)
# plt.pcolormesh(x1x, x2x, x3x, x4x, Z, cmap=plt.cm.Paired)

# 散点图绘制
plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
plt.scatter(X[100:, 0], X[100:, 1], color='green', marker='s', label='Virginica')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
# plt.xticks(())
# plt.yticks(())
plt.legend(loc=2)
plt.show()
