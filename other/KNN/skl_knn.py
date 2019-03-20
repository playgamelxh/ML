#encoding=utf-8
'''
脚本说明：sklearn包kNN
'''
import numpy as np
import operator
from sklearn.neighbors import KNeighborsClassifier as kNN
from mnist import read_image

if __name__ == '__main__':

    train_image_path = '/www/ML/other/KNN/mnist/train-images-idx3-ubyte'
    train_label_path = '/www/ML/other/KNN/mnist/train-labels-idx1-ubyte'
    test_image_path = '/www/ML/other/KNN/mnist/t10k-images-idx3-ubyte'
    test_label_path = '/www/ML/other/KNN/mnist/t10k-labels-idx1-ubyte'
    a = read_image(train_image_path)
    print(a[0])

