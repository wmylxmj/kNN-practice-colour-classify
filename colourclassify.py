# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 20:05:14 2018

@author: wmy
"""

import numpy
import operator

def CreatCommonColourTable():    
    ColourValue=numpy.array([[0,0,0],[192,192,192],[255,255,255],
                      [255,250,250],[255,0,0],[163,148,128],
                      [255,255,0],[65,105,225],[0,255,255],
                      [135,206,235],[127,255,0],[0,255,0],
                      [160,32,240],[221,160,221],[0,0,255],
                      [128,42,42],[107,142,35],[250,128,114]])
    ColourName=['黑色','灰色','白色',
                '雪白','红色','米色',
                '黄色','品蓝','青色',
                '天蓝','黄绿','绿色',
                '紫色','梅红','蓝色',
                '棕色','草绿','橙红']                
    return ColourValue,ColourName
    
ColourValue,ColourName=CreatCommonColourTable()

#print(ColourValue)
#print(ColourName)
print('已学习的颜色有'+':'+str(ColourName))

def ColourClassify(incolour,traindata,traincolour,k):
    '''训练的颜色个数'''
    #shape为numpy模块中的方法 shape[0]为矩阵第二维的长度
    trainsize=traindata.shape[0]
    #计算各个维度的差值并储存在向量diffmat中
    diffmat=numpy.tile(incolour,(trainsize,1))-traindata
    #计算误差的平方
    squarediffmat=diffmat**2
    #计算向量间的欧式距离
    errordistance=squarediffmat.sum(axis=1)**0.5
    #排序
    sorteddistance=errordistance.argsort()
    classcount={}
    for i in range(k):
        #选取前k个最符合要求的颜色
        selectedcolour=traincolour[sorteddistance[i]]
        classcount[selectedcolour]=classcount.get(selectedcolour,0)+1
    sortedclasscount=sorted(classcount.items(),
                            key=operator.itemgetter(1),reverse=True)
    return sortedclasscount[0][0]

print('\n')

colourinputR=input('请输入任一种颜色的R值 ')
colourinputG=input('请输入任一种颜色的G值 ')
colourinputB=input('请输入任一种颜色的B值 ')

colourinput=[int(colourinputR),int(colourinputG),int(colourinputB)]

print('\n'+'根据已学习样本，此颜色为'+
      str(ColourClassify(colourinput,ColourValue,ColourName,3)))
    
