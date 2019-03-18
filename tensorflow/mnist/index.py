# -*- coding: utf-8 -*-
import tensorflow as tf
import input_data

# 数据集
mnist = input_data.read_data_sets("../data/", one_hot=True)
# 占位符placeholder
x = tf.placeholder("float", [None, 784])
# 权重值
W = tf.Variable(tf.zeros([784, 10]))
# 偏置量
b = tf.Variable(tf.zeros([10]))
# 模型 tf.matmul(​​X，W)表示x乘以W
y = tf.nn.softmax(tf.matmul(x, W) + b)
# 为了计算交叉熵，我们首先需要添加一个新的占位符用于输入正确值：
y_ = tf.placeholder("float", [None, 10])
# 计算交叉熵
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
# 梯度下降算法学习
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
# 初始化变量
# init = tf.initialize_all_variables()
init = tf.global_variables_initializer()
# 在session里启动模型
sess = tf.Session()
sess.run(init)
# 开始训练模型，循环训练1000次
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
res = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
print(res)
