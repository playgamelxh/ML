# -*- coding: utf-8 -*-

import time
import numpy as np
import matplotlib.pyplot as plt

# 正弦余弦函数
# x = np.linspace(-np.pi, np.pi, 512, endpoint=True)
# C, S = np.cos(x), np.sin(x)
# plt.plot(x, C)
# plt.plot(x, S)
# plt.show()

# 从[-1,1]中等距去50个数作为x的取值
# x = np.linspace(-1, 1, 10)
# # print(x)
# y = 2 * x + 1
# # 第一个是横坐标的值，第二个是纵坐标的值
# plt.plot(x, y)
# # 必要方法，用于将设置好的figure对象显示出来
# plt.show()

# x = np.linspace(0, 2, 50)
# y = 2 ** x + 1
# plt.plot(x, y)
# plt.show()

# x = np.linspace(0, 2, 50)
# y1 = 2 * x + 1
# y2 = 2 ** x + 1
# plt.figure()
# plt.plot(x, y1)
# plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--')
# plt.show()

# n = 1024
# X = np.random.normal(0, 1, n)
# Y = np.random.normal(0, 1, n)
# T = np.arctan2(X, Y)
# # print(T)
# plt.scatter(np.arange(10), np.arange(10))
# plt.xticks(())
# plt.yticks(())
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 8))
ax = Axes3D(fig)

# 生成X，Y
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)

# height value
Z = np.sin(R)

# 绘图
# rstride（row）和cstride(column)表示的是行列的跨度
ax.plot_surface(X, Y, Z,
                rstride=1,  # 行的跨度
                cstride=1,  # 列的跨度
                cmap=plt.get_cmap('rainbow'))  # 颜色映射样式设置

# offset 表示距离zdir的轴距离
ax.contourf(X, Y, Z, zdir='z', offest=-2, cmap='rainbow')
ax.set_zlim(-2, 2)
plt.show()
