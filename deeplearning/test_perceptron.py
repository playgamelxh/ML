# -*- coding: utf-8 -*-
from perceptron import Perceptron
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    '''
    定义激活函数f
    '''
    return 1 if x > 0 else 0


def get_training_dataset():
    '''
    基于and真值表构建训练数据
    '''
    # 构建训练数据
    # 输入向量列表
    input_vecs = [[1, 1], [0, 0], [1, 0], [0, 1]]
    # 期望的输出列表，注意要与输入一一对应
    # [1,1] -> 1, [0,0] -> 0, [1,0] -> 0, [0,1] -> 0
    labels = [1, 0, 0, 0, 0]
    return input_vecs, labels


def train_and_perceptron():
    '''
    使用and真值表训练感知器
    '''
    # 创建感知器，输入参数个数为2（因为and是二元函数），激活函数为f
    p = Perceptron(2, f)
    # 训练，迭代10轮, 学习速率为0.1
    input_vecs, labels = get_training_dataset()
    p.train(input_vecs, labels, 10, 0.1)
    # 返回训练好的感知器
    # 画点
    for i in input_vecs:
        plt.plot(i[0], i[1], '.')
        print(i[0], i[1])
    plt.show()
    return p


if __name__ == '__main__':
    # 训练and感知器
    and_perception = train_and_perceptron()
    # 打印训练获得的权重
    print(and_perception)
    # 测试
    print('1 and 1 = %d' % and_perception.predict([1, 1]))
    print('0 and 0 = %d' % and_perception.predict([0, 0]))
    print('1 and 0 = %d' % and_perception.predict([1, 0]))
    print('0 and 1 = %d' % and_perception.predict([0, 1]))
    print('0 and 2 = %d' % and_perception.predict([0, 2]))
    print('1 and 2 = %d' % and_perception.predict([1, 2]))
    print('0 and 3 = %d' % and_perception.predict([0, 3]))
    print('0.5 and 0.5 = %d' % and_perception.predict([0.5, 0.5]))
    print('-1 and -1 = %d' % and_perception.predict([-1, -1]))
