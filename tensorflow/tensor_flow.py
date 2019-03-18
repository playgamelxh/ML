# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np

# greeting = tf.constant('Hello Google Tensorflow')
# sess = tf.Session()
# result = sess.run(greeting)
# print(result)
# sess.close()


# matrix1 = tf.constant([[3., 3.]])
# matrix2 = tf.constant([[2.], [2.]])
# product = tf.matmul(matrix1, matrix2)
# # print(product)
# linear = tf.add(product, tf.constant(2.0))
#
# with tf.Session() as sess:
#     result = sess.run(linear)
#     print(result)

# 交互式使用
# sess = tf.InteractiveSession()
# x = tf.Variable([1.0, 2.0])
# y = tf.constant([3.0, 3.0])
# x.initializer.run()
#
# sub = tf.subtract(x, y)
# print(sub.eval())

# # 变量
# # 创建一个变量, 初始化为标量 0.
# state = tf.Variable(0, name="counter")
# # 创建一个 op, 其作用是使 state 增加 1
# one = tf.constant(1)
# new_value = tf.add(state, one)
# update = tf.assign(state, new_value)
# # 启动图后, 变量必须先经过`初始化` (init) op 初始化,
# # 首先必须增加一个`初始化` op 到图中.
# init_op = tf.global_variables_initializer()
# # 启动图, 运行 op
# with tf.Session() as sess:
#     # 运行 'init' op
#     sess.run(init_op)
#     # 打印 'state' 的初始值
#     print(sess.run(state))
#     # 运行 op, 更新 'state', 并打印 'state'
#     for _ in range(3):
#         sess.run(update)
#         print(sess.run(state))

# # fetch 取回操作的输出内容
# input1 = tf.constant(3.0)
# input2 = tf.constant(2.0)
# input3 = tf.constant(5.0)
# intermed = tf.add(input2, input3)
# #  tf.mul 改成 tf.multiply tf.sub 和 tf.neg 也要相应修改为 tf.subtract 和 tf.negative
# mul = tf.multiply(input1, intermed)
#
# with tf.Session() as sess:
#     result = sess.run([mul, intermed])
#     print(result)

# feed
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run([output], feed_dict={input1: [7.], input2: [2.]}))
