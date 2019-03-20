#encoding=utf-8
'''
脚本说明：kNN实战，海伦约会
'''
import numpy as np
import operator as oper
import collections
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

'''
函数说明：处理数据集
'''
def fileToMatrix(filename):
    # 打开文件
    fr = open(filename)
    # print(fr)
    # 读取文件内容
    lines = fr.readlines()
    # print(lines)
    # 获取行数
    row = len(lines)
    # print(row)
    # 返回数据
    returnMatrix = np.zeros((row, 3))
    # 返回标签
    returnLabels = []
    # 索引
    index = 0
    for line in lines:
        # s.strip(rm)，当rm空时,默认删除空白符(包括'\n','\r','\t',' ')
        line = line.strip()
        # print(line)
        # break
        # 使用s.split(str="",num=string,cout(str))将字符串根据'\t'分隔符进行切片。
        listFromLine = line.split('\t')
        # print(listFromLine)
        # break
        # 保存数据
        returnMatrix[index,:] = listFromLine[0:3]
        # 保存标签
        if listFromLine[-1] == 'didntLike':
            returnLabels.append(1)
        elif listFromLine[-1] == 'smallDoses':
            returnLabels.append(2)
        elif listFromLine[-1] == 'largeDoses':
            returnLabels.append(3)
        index += 1

    return returnMatrix, returnLabels

'''
函数说明：画图，三维
'''
def show(data, labels):
    fig = plt.figure()
    ax = Axes3D(fig)

    colors = ['black', 'red', 'green', 'blue']
    key = 0;
    for item in data:
        ax.scatter(item[0], item[1], item[2], c=colors[labels[key]])
        key += 1
    # X轴坐标
    ax.set_xlabel('X', fontdict={'size': 12, 'color': 'red'})
    # Y轴坐标
    ax.set_ylabel('Y', fontdict={'size': 12, 'color': 'green'})
    # Z轴坐标
    ax.set_zlabel('Z', fontdict={'size': 12, 'color': 'blue'})
    plt.show()

'''
函数说明：画图，二维
'''
# def show_two(data, labels):
#     colors = ['black', 'red', 'green', 'yellow']
#
#     # 2x2
#     fig, axs = plt.subplots(nrows=2, ncols=2, sharex=False, sharey=False, figsize=(13, 8))
#
#     key = 0
#     for item in data:
#         axs[0][0].scatter(x=item[0], y=labels[key], color=colors[labels[key]])
#         axs[0][1].scatter(x=item[1], y=labels[key], color=colors[labels[key]])
#         axs[1][0].scatter(x=item[2], y=labels[key], color=colors[labels[key]])
#         key += 1;
#
#     # 设置标题,x轴label,y轴label
#     axs0_title_text = axs[0][0].set_title(u'每年飞行常客里程数与分类')
#     axs0_xlabel_text = axs[0][0].set_xlabel(u'每年获得的飞行常客里程数')
#     axs0_ylabel_text = axs[0][0].set_ylabel(u'玩视频游戏所消耗时间占')
#     plt.setp(axs0_title_text, size=1, weight='bold', color='red')
#     plt.setp(axs0_xlabel_text, size=1, weight='bold', color='black')
#     plt.setp(axs0_ylabel_text, size=1, weight='bold', color='black')
#     plt.show()

'''
函数说明：特征缩放 newValue = (oldValue - min) / (max - min)
最大值法:  newValue = oldValue/max
均值归一法：newValue = (oldValue-V平均)/(max-min)
'''
def autoNormal(data):
    # print(data)
    minV = data.min(0)
    maxV = data.max(0)
    # print("最小值",minV, '最大值',maxV)
    ranges = maxV - minV
    # print("差值", ranges)
    normalDataSet = np.zeros(np.shape(data))
    m = data.shape[0]
    normalDataSet = data - np.tile(minV, (m, 1))
    # print(np.tile(minV, (m, 1)))
    # print(normalDataSet)
    normalDataSet = normalDataSet/np.tile(ranges, (m, 1))
    return normalDataSet, minV, ranges

'''
函数说明：精简版kNN算法
'''
def classify_simple(x, data, labels, k):
    # 计算距离
    dist = np.sum((data - x) ** 2, axis=1) ** 0.5
    # k个最近的标签
    k_labels = [labels[index] for index in dist.argsort()[0: k]]
    # 出现次数最多的标签即为最终类别
    label = collections.Counter(k_labels).most_common(1)[0][0]
    return label


if __name__ == '__main__':
    filename = '/www/ML/other/KNN/datingTestSet.txt'
    data, labels = fileToMatrix(filename)

    # 画图
    # show(data, labels)
    # show_two(data, labels)
    # 特征缩放后 能提升准确率
    data, minV, ranges = autoNormal(data)
    # show(data, labels)

    # 取前四分之三数据用于学习  后四分之一数据用于测试
    # print(data)
    # print(data.shape[0], data.shape[1])
    num = 750
    data_learn = data[0:num]
    # print(data_learn, data_learn.shape[0])
    data_test = data[num:]
    # print(data_test, data_test.shape[0])
    labels_learn = labels[0:num]
    labels_test = labels[num:]
    # print(labels_learn)
    # print(labels_test)

    # 正确数量
    right = 0
    wrong = 0
    key = 0
    for item in data_test:
        # 获取分类标签
        label = classify_simple(item, data_learn, labels_learn, 3)
        # 统计正确、错误数量
        if (label == labels_test[key]):
            right += 1
        else:
            wrong += 1
        # 键值+1
        key += 1
    print("正确数量：%s;错误数量：%s,错误率：%s%%"%(right, wrong, wrong*100/(right+wrong)))