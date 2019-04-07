#encoding=utf-8
import math
import pickle
from tree_view import *
# import operator
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties
'''
函数说明：构造决策树数据
'''
def createDataSet():
    # 数据集
    dataSet = [[0, 0, 0, 0, 'no'],
               [0, 0, 0, 1, 'no'],
               [0, 1, 0, 1, 'yes'],
               [0, 1, 1, 0, 'yes'],
               [0, 0, 0, 0, 'no'],
               [1, 0, 0, 0, 'no'],
               [1, 0, 0, 1, 'no'],
               [1, 1, 1, 1, 'yes'],
               [1, 0, 1, 2, 'yes'],
               [1, 0, 1, 2, 'yes'],
               [2, 0, 1, 2, 'yes'],
               [2, 0, 1, 1, 'yes'],
               [2, 1, 0, 1, 'yes'],
               [2, 1, 0, 2, 'yes'],
               [2, 0, 0, 0, 'no']]
    # 分类属性
    labels = ['年龄', '有工作', '有自己的房子', '信贷情况']
    return dataSet, labels

'''
函数说明：计算经验熵
计算公式：$$H=-\sum _{i=1}^n p(x_i)log_2p(x_i)$$
'''
def calculateEntropy(dataSet):
    dict = {}
    for item in dataSet:
        key = item[-1]
        if (key not in dict.keys()):
            dict[key] = 1
        else:
            dict[key] += 1
    entropy = 0
    for key in dict:
        px = dict[key]/len(dataSet)
        entropy += (-px * math.log2(px))
    return entropy

'''
函数说明：计算条件熵
计算公式：$$H(Y|X)=\sum _{i=1}^np_iH(Y|X=x_i)$$
'''
def calculateConditionEntropy(dataSet, key=0):
    condition_entropy = 0
    # 获取列的可取值
    dict = {}
    for item in dataSet:
        if item[key] not in dict.keys():
            dict[item[key]] = {}
    for value in dict.keys():
        li = splitDataSet(dataSet, key, value)
        condition_entropy += (len(li) / len(dataSet)) * calculateEntropy(li)
    return condition_entropy
'''
函数说明：获取信息增益最大key
计算公式：ID3    信息增益    取最大    $$G(D, A)=H(D) - H(D|A)$$
计算公式：C4.5   信息增益比   取最大   $$I(D,A)=\frac{G(D,A)}{H(D)}$$
计算公式：CHART  Gini系数  取最小  $$Gini(D,A)=\frac{|D_1|}{|D|}Gini(D_1)+\frac{|D_2|}{|D|}Gini(D_2)$$
参考：https://shuwoom.com/?p=1452
'''
def getMaxCalculateInformationGainKey(dataSet):
    Hd = calculateEntropy(dataSet)
    dict = {}
    # return len(dataSet[0])
    for key in range(0, len(dataSet[0])-1):
        condition_entropy = calculateConditionEntropy(dataSet, key)
        # print(condition_entropy, Hd - condition_entropy)
        dict[key] = Hd - condition_entropy
    # print(dataSet)
    # print(dict)
    return max(dict, key=dict.get)

'''
函数说明：递归构建决策树
'''
def createDecisionTree(dataSet, labels):
    decision_tree = {}
    # 仅剩最后一列数据
    if len(dataSet[0]) <= 1 :
        return dataSet[0][-1]
    # 获取最大的列
    key = getMaxCalculateInformationGainKey(dataSet)
    label = labels[key]
    # print(dataSet)
    # print(key)
    # print(label)
    # 根节点
    decision_tree[label] = {}
    # print(decision_tree)
    # 切分数据
    # 获取列的可取值
    dict = {}
    res  = {}
    for item in dataSet:
        if item[key] not in dict.keys():
            dict[item[key]] = {}
        if item[-1] not in res.keys():
            res[item[-1]] = 1
        else:
            res[item[-1]] += 1
    # 如果特征只有一个值，或者 结果只有一个值
    # if len(dict.keys()) <= 1:
    if len(res) <= 1:
        # pass
        # 这里需要取最多结果的值
        decision_tree = max(res, key=res.get)
    else:
        for value in dict.keys():
            li = splitDataSet(dataSet, key, value)
            if value not in decision_tree[label].keys():
                decision_tree[label][value] = {}
            decision_tree[label][value] = createDecisionTree(li, labels)
            # print(li)
    return decision_tree

'''
函数说明，根据某列的值，切分数据
'''
def splitDataSet(dataSet, key, value):
    # 创建返回的数据集列表
    retDataSet = []
    # 遍历数据集
    for featVec in dataSet:
        if featVec[key] == value:
            # # 去掉特征
            # reducedFeatVec = featVec[:key]
            # # # 将符合条件的添加到返回的数据集
            # reducedFeatVec.extend(featVec[key+1:])
            # retDataSet.append(reducedFeatVec)
            # 不去特征
            retDataSet.append(featVec)
    return retDataSet

'''
函数说明：决策树存储
'''
def storeTree(input_tree, file_name):
    with open(file_name, 'wb') as fw:
        pickle.dump(input_tree, fw)

'''
函数说明：读取决策树
'''
def getTree(file_name):
    fr = open(file_name, 'rb')
    return pickle.load(fr)

'''
函数说明：决策树分类
'''
def classify(inputTree, featLabels, testVec):
    # 获取决策树结点
    firstStr = next(iter(inputTree))
    # 下一个字典
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else: classLabel = secondDict[key]
    return classLabel

if __name__ == "__main__":
    dataSet, labels = createDataSet()
    # #　计算熵
    # Hd = calculateEntropy(dataSet)
    # print(Hd)
    # #　计算各维度的增益
    # for key in range(0, len(dataSet[0])-1):
    #     condition_entropy = calculateConditionEntropy(dataSet, key)
    #     print(condition_entropy, Hd - condition_entropy)
    # 获取最大增益的列
    # key = getMaxCalculateInformationGainKey(dataSet)
    # print(key)
    # 生成决策树
    decision_tree = createDecisionTree(dataSet, labels)
    print(decision_tree)
    storeTree(decision_tree, 'a.txt')
    tree = getTree('a.txt')
    print(tree)
    # labels = ['年龄', '有工作', '有自己的房子', '信贷情况']
    featLabels = ['年龄', '有工作', '有自己的房子', '信贷情况']
    testVec = [0, 0, 0, 0]
    result = classify(decision_tree, featLabels, testVec)
    if result == 'yes':
        print('放贷')
    if result == 'no':
        print('不放贷')
    # print(getNumLeafs(decision_tree))
    # print(getTreeDepth(decision_tree))
    # createPlot(decision_tree)