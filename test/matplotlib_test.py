# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D


if __name__ == "__main__":
    # x = np.arange(-10, 10, 0.1)
    # y = np.sin(x)
    # y1 = np.cos(x)
    # y2 = y + y1
    # plt.plot(x, y, color='red')
    # plt.plot(x, y1, color='g')
    # plt.plot(x, y2, color='b')
    # plt.xlim(-10, 10)
    # plt.ylim(-2, 2)
    # ax = plt.gca()
    # # 右边边框隐藏
    # ax.spines['right'].set_color('none')
    # # 顶部边框隐藏
    # ax.spines['top'].set_color('none')
    # # 移动Y轴到0
    # ax.spines['bottom'].set_position(('data', 0))
    # # 移动X轴到0
    # ax.spines['left'].set_position(('data', 0))
    # # print(ax)
    # plt.show()

    # 定义图像窗口
    fig = plt.figure()
    # 在窗口上添加3D坐标轴
    ax = Axes3D(fig)
    # 将X和Y值编织成栅格
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    # 高度值
    Z = np.sin(R)
    # 将colormap rainbow填充颜色，之后将三维图像投影到XY平面做等高线图，其中ratride和cstride表示row和column的宽度
    # rstride表示图像中分割线的跨图
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
    # 添加XY平面等高线 投影到z平面
    # 把图像进行投影的图形 offset表示比0坐标轴低两个位置
    ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
    ax.set_zlim(-2, 2)
    plt.show()
