# encoding=utf-8
'''
脚本说明：kNN算法，分类器
'''
import numpy as np
import operator as oper
import collections
import matplotlib.pyplot as plt

'''
函数说明：构造数据
'''
def createData():
    data = np.array([[1, 2], [2, 3], [7, 8], [9,8]])
    labels = [1, 1, 2, 2]
    return data, labels

'''
函数说明：特征缩放
最大值法：X/最大值，分布到[0, 1]之间
均值归一：(X-平均)/(最大值-最小值)
'''

'''
函数说明：kNN核心算法
'''
def classify(x, data, labels, k):
    # 求差
    diffM = data - x
    print("求差：",diffM)
    # 平方
    sqrtM = diffM**2
    print("平方：", sqrtM)
    # 求和 sum(0)列相加，sum(1)行相加
    sumM = sqrtM.sum(axis=1)
    print("求和：", sumM)
    # 开方
    distances = sumM**0.5
    print("开方求距离：", distances)
    # 精简
    # distances = np.sum((data-x)**2, axis=1)**0.5

    sortD = distances.argsort()
    print("排序取key排序：", sortD)

    classCount = {}
    for i in range(k):
        label = labels[sortD[i]]
        classCount[label] = classCount.get(label, 0) + 1
    print("分类统计数据：", classCount)
    # 分类字典，根据值排序 key=operator.itemgetter(1)根据字典的值进行排序 key=operator.itemgetter(0)根据字典的键进行排序
    sortClass = sorted(classCount.items(), key=oper.itemgetter(1),reverse=True)
    print("排序分类：", sortClass)

    return sortClass[0][0]

'''
函数说明：精简版kNN算法
'''
def classify_simple(x, data, labels, k):
    # 计算距离
	dist = np.sum((data - x)**2, axis=1)**0.5
	# k个最近的标签
	k_labels = [labels[index] for index in dist.argsort()[0 : k]]
	# 出现次数最多的标签即为最终类别
	label = collections.Counter(k_labels).most_common(1)[0][0]
	return label


if __name__ == '__main__':

    data, labels = createData()
    # print(data,labels)
    # plt.scatter(data[:,0], data[:,1])
    colors = ['black', 'red', 'green']
    plt.scatter(data[0, 0], data[0, 1], c=colors[labels[0]])
    plt.scatter(data[1, 0], data[1, 1], c=colors[labels[1]])
    plt.scatter(data[2, 0], data[2, 1], c=colors[labels[2]])
    plt.scatter(data[3, 0], data[3, 1], c=colors[labels[3]])
    # X轴坐标
    plt.xticks(range(0, np.amax(data[:,0])+1))
    # Y轴坐标
    plt.yticks(range(0, np.amax(data[:,1])+1))

    x = [6, 6]
    type = classify(x, data, labels, 3)
    plt.scatter(x[0], x[1], c=colors[type])

    x = [3, 3]
    type = classify(x, data, labels, 3)
    plt.scatter(x[0], x[1], c=colors[type])

    x = [5, 5]
    type = classify(x, data, labels, 3)
    plt.scatter(x[0], x[1], c=colors[type])

    x = [4, 4]
    type = classify_simple(x, data, labels, 3)
    plt.scatter(x[0], x[1], c=colors[type])
    plt.show()
