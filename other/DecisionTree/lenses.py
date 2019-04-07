#encodint=utf-8
from sklearn import tree
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.externals.six import StringIO
import pydotplus
import graphviz
import os

'''
函数说明：用pandas库处理数据
'''
def change(file_name):
    with open(file_name, 'r') as fr:
        lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    # 提取每组数据的类别，保存在列表里
    lenses_target = []
    for each in lenses:
        lenses_target.append(each[-1])

    # 特征标签
    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
    # 保存lenses数据的临时列表
    lenses_list = []
    # 保存lenses数据的字典，用于生成pandas
    lenses_dict = {}
    # 提取信息，生成字典
    for each_label in lensesLabels:
        for each in lenses:
            lenses_list.append(each[lensesLabels.index(each_label)])
        lenses_dict[each_label] = lenses_list
        lenses_list = []
    print(lenses_dict)
    lenses_pd = pd.DataFrame(lenses_dict)
    print(lenses_pd)
    le = LabelEncoder()
    for col in lenses_pd.columns:
        lenses_pd[col] = le.fit_transform(lenses_pd[col])
    print(lenses_pd)
    print(lenses_target)
    print(le.fit_transform(lenses_target))
    print(lenses_pd.values.tolist())
    return  lenses_pd, lenses_target


if __name__ == '__main__':
    fr = open('lenses.txt')
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    print(lenses)

    data = []
    label = []
    for item in lenses:
        # 数字化
        if item[0] == 'young':
            item[0] = 0
        elif item[0] == 'pre':
            item[0] = 1
        elif item[0] == 'presbyopic':
            item[0] = 2

        if item[1] == 'myope':
            item[1] = 0
        elif item[1] == 'hyper':
            item[1] = 1

        if item[2] == 'no':
            item[2] = 0
        elif item[2] == 'yes':
            item[2] = 1

        if item[3] == 'reduced':
            item[3] = 0
        elif item[3] == 'normal':
            item[3] = 1

        if item[4] == 'no lenses':
            item[4] = 0
        elif item[4] == 'soft':
            item[4] = 1
        elif item[4] == 'hard':
            item[4] = 2
        # 前三列为特征
        data.append(item[0:4:1])
        # 最后一列为结果
        label.append(item[-1])
    print(data)
    print(label)

    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
    clf = tree.DecisionTreeClassifier()
    lenses = clf.fit(data, label)
    # 旧的使用方法
    # lenses = clf.fit(lenses, lensesLabels)
    res = clf.predict([[0,0,0,1]])
    print(res)

    lenses_pd, lenses_target = change('lenses.txt')

    clf = tree.DecisionTreeClassifier(max_depth=4)  # 创建DecisionTreeClassifier()类
    clf = clf.fit(lenses_pd.values.tolist(), lenses_target)  # 使用数据，构建决策树
    dot_data = StringIO()
    # 需要安装pydotplus包和安装Graphviz软件，并把Graphviz安装目录下的bin目录添加到path中
    tree.export_graphviz(clf, out_file=dot_data,  # 绘制决策树
                         feature_names=lenses_pd.keys(),
                         class_names=clf.classes_,
                         filled=True, rounded=True,
                         special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_pdf("tree.pdf")