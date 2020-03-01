import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

size = 3 ##取值范围

counts = np.zeros(6)

##计算欧式距离
def distEuclid(x,y):
    return np.sqrt(np.sum((x-y)**2))


## 初始化簇中心点 一开始随机从样本中选择k个 当做各类簇的中心
def initCentroid(data,k):
    num,dim = data.shape
    centpoint = np.zeros((k,dim))
    l = [x for x in range(num)]
    np.random.shuffle(l)
    for i in range(k):
        index = int(l[i])
        centpoint[i] = data[index]
    return centpoint

#自定义中心点：首先此时让中心点靠近每个分类中心，我觉的算法的训练在此种情况下必须识别该有的中心点

def findCenter(data, k):
    num, dim = data.shape
    print(num)
    centpoint = np.zeros((k, dim)) 
    #定义中心点数组， 在原本的函数是获取数组的坐标，然后坐标随机，随机中心点。
    for i in range(k):
        m = random.randint(0,100)
        centpoint[i] = data[m+i*100]
        print(m)
        #print(centpoint[i])S
    return centpoint

##进行KMeans分类
def KMeans(data,k):
    ##样本个数
    num = np.shape(data)[0]
    
    ##记录各样本 簇信息 0:属于哪个簇 1:距离该簇中心点距离 
    cluster = np.zeros((num,2))
    cluster[:,0]=-1
    
    ##记录是否有样本改变簇分类
    change = True
    ##初始化各簇中心点
    cp = findCenter(data,k)
    #cp = initCentroid(data, k)
    print(cp)

    while change:
        change = False
        
        ##遍历每一个样本
        for i in range(num):
            minDist = 100000
            minIndex = -1
            
            ##计算该样本距离每一个簇中心点的距离 找到距离最近的中心点
            for j in range(k):
                dis = distEuclid(cp[j],data[i])
                if dis < minDist:
                    minDist = dis
                    minIndex = j
            
            ##如果找到的簇中心点非当前簇 则改变该样本的簇分类
            ##说明这个点距离其他簇分类更近， 因此分类到其他簇
            if cluster[i,0]!=minIndex:
                change = True
                cluster[i,:] = minIndex,minDist
        
        ## 根据样本重新分类  计算新的簇中心点
        for j in range(k):     
            pointincluster = data[[x for x in range(num) if cluster[x,0]==j]]
            #如果
            if len(pointincluster) != 0:
                cp[j] = np.mean(pointincluster,axis=0)
    
    print("finish!")
    return cp,cluster

##展示结果  各类簇使用不同的颜色  中心点使用X表示
def Show(data,k,cp,cluster):
    num = data.shape[0]
    color = ['r','g','b','c','y','m','k']
    ax = plt.subplot(111,projection ='3d')
    
    for i in range(num):
        #mark就是簇的值，通过mark可以进行正确类的筛选
        #print(cluster[i])
        mark = int(cluster[i,0])
        #print(mark, i//100)
        #在这里进行判断如果所分簇与实际分簇相同则画出
        if i//100 == mark :
            counts[mark] += 1
            #每个簇分类计数
            ax.scatter(data[i,0],data[i,1],data[i,2],c=color[mark])
        
    for i in range(k):
        ax.scatter(cp[i,0],cp[i,1],cp[i,2],c=color[i],marker='x')
    print(counts)
        
    plt.show()


k=6 ##分类个数

reader = pd.read_csv('test2.csv',header=None)
data1 = np.vstack((reader.loc[0:0].values,reader.loc[1:1].values,reader.loc[2:2].values))
reader = pd.read_csv('test2.csv',header=None)
data2 = np.vstack((reader.loc[3:3].values,reader.loc[4:4].values,reader.loc[5:5].values))
reader = pd.read_csv('test2.csv',header=None)
data3 = np.vstack((reader.loc[6:6].values,reader.loc[7:7].values,reader.loc[8:8].values))
reader = pd.read_csv('test2.csv',header=None)
data4 = np.vstack((reader.loc[9:9].values,reader.loc[10:10].values,reader.loc[11:11].values))
reader = pd.read_csv('test2.csv',header=None)
data5 = np.vstack((reader.loc[12:12].values,reader.loc[13:13].values,reader.loc[14:14].values))
reader = pd.read_csv('test2.csv',header=None)
data6 = np.vstack((reader.loc[15:15].values,reader.loc[16:16].values,reader.loc[17:17].values))
data = np.hstack((data1,data2,data3,data4,data5,data6)).transpose()
#print(data)

#data = np.array(genDataset(num,3))
#print(data)
cp,cluster = KMeans(data,k)
Show(data,k,cp,cluster)