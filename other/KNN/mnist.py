#encoding=utf-8
'''
脚本说明：手写识别
'''
import numpy as np
import pandas as pd
from struct import unpack
from sklearn.neighbors import KNeighborsClassifier as kNN
''''
函数说明：读取图片文件
'''
def read_image(path):
    with open(path, 'rb') as f:
        magic, num, rows, cols = unpack('>4I', f.read(16))
        img = np.fromfile(f, dtype=np.uint8).reshape(num, 784)
    return img

'''
函数说明：读取标签
'''
def read_label(path):
    with open(path, 'rb') as f:
        magic, num = unpack('>2I', f.read(8))
        lab = np.fromfile(f, dtype=np.uint8)
    return lab

def normalize_image(image):
    img = image.astype(np.float32) / 255.0
    return img

def one_hot_label(label):
    lab = np.zeros((label.size, 10))
    for i, row in enumerate(lab):
        row[label[i]] = 1
    return lab


def load_mnist(train_image_path, train_label_path, test_image_path, test_label_path, normalize=True, one_hot=True):
    '''读入MNIST数据集 会导致报错
    Parameters
    ----------
    normalize : 将图像的像素值正规化为0.0~1.0
    one_hot_label :
        one_hot为True的情况下，标签作为one-hot数组返回
        one-hot数组是指[0,0,1,0,0,0,0,0,0,0]这样的数组
    Returns
    ----------
    (训练图像, 训练标签), (测试图像, 测试标签)
    '''
    image = {
        'train': read_image(train_image_path),
        'test': read_image(test_image_path)
    }

    label = {
        'train': read_label(train_label_path),
        'test': read_label(test_label_path)
    }

    # if normalize:
    #     for key in ('train', 'test'):
    #         image[key] = normalize_image(image[key])
    #
    # if one_hot:
    #     for key in ('train', 'test'):
    #         label[key] = one_hot_label(label[key])

    return (image['train'], label['train']), (image['test'], label['test'])
'''
函数说明：打印图像矩阵
'''
def print_num(data):
    key = 0
    str = ''
    for item in data:
        str += "%d\t" % (item)
        key += 1
        if (key == 28):
            print(str)
            str = ''
            key = 0

if __name__ == '__main__':

    train_image_path = '/www/ML/other/KNN/mnist/train-images-idx3-ubyte'
    train_label_path = '/www/ML/other/KNN/mnist/train-labels-idx1-ubyte'
    test_image_path = '/www/ML/other/KNN/mnist/t10k-images-idx3-ubyte'
    test_label_path = '/www/ML/other/KNN/mnist/t10k-labels-idx1-ubyte'

    # 此方法存在不兼容问题
    # image_train, label_train, image_test, label_test = load_mnist(train_image_path, train_label_path, test_image_path,
    #                                                               test_label_path)
    # print(image_test, label_test);

    image_test = read_image(test_image_path)
    label_test = read_label(test_label_path)

    image_train = read_image(train_image_path)
    label_train = read_label(train_label_path)
    # print_num(image_train[0])
    # print(label_train)

    knn = kNN(n_neighbors = 3, algorithm = 'auto')
    knn.fit(image_train, label_train)

    res = knn.predict(image_test[:100])
    #
    right = 0
    wrong = 0
    for i in range(len(res)):
        if (res[i] == label_test[i]):
            right += 1
            print("预测值：%s，真是值：%s" % (res[i], label_test[i]))
        else:
            wrong += 1
            print("\033预测值：%s，真是值：%s\033" % (res[i], label_test[i]))
    print("准确率：%2f%%" % (right*100/(right+wrong)))