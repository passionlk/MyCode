#coding:utf-8

from numpy import *
import operator
import sys

##给出训练数据以及对应的类别
def createDataSet():
    group = array([[1.0,2.0],[1.2,0.1],[0.1,1.4],[0.3,3.5],[0.9,2.5],[1.3,2.5],[4.3,5.5],[2.3,6.0]])
    labels = ['A','A','B','B','B','C','C','C']
    return group,labels

###通过KNN进行分类
def classify(input,dataSet,label,k):
    #是array的属性，描述一个多维数组的维度
    dataSize = dataSet.shape[0]
    ####计算欧式距离
    ##把inX二维数组化，dataSetSize表示生成数组后的行数，1表示列的倍数。
    ##整个这一行代码表示前一个二维数组矩阵的每一个元素减去后一个数组对应的元素值;
    ##这样就实现了矩阵之间的减法，简单方便得不让你佩服不行！
    diff = tile(input,(dataSize,1)) - dataSet
    sqdiff = diff ** 2
    squareDist = sum(sqdiff,axis = 1) ###向量按行相加，从而得到新的一个行向量
    dist = squareDist ** 0.5
    
    ##对距离进行排序
    sortedDistIndex = argsort(dist)  ##argsort()根据元素的值从大到小对元素进行排序，返回下标

    classCount={}
    
    for i in range(k):
        voteLabel = label[sortedDistIndex[i]]
        ###对选取的K个样本所属的类别个数进行统计
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1
    
    ###选取出现的类别次数最多的类别
    maxCount = 0
    for key,value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key

    return classes

##KNN算法测试

dataSet,labels = createDataSet()
input = array([2.1,2.0])
K = 3
output = classify(input,dataSet,labels,K)
print("测试数据为:",input,"分类结果为：",output)