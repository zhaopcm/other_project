import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

size = 3 ##取值范围

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
    centpoint = np.zeros((k, dim)) 
    #定义中心点数组， 在原本的函数是获取数组的坐标，然后坐标随机，随机中心点。
    for i in range(k):
        l = num//k
        m = random.randint(0,l)
        centpoint[i] = data[m+i*l]
        #print(m)
        #print(centpoint[i])
    return centpoint

##进行KMeans分类
def KMeans(data,k):
    ##样本个数
    num = np.shape(data)[0]
    
    ##记录各样本 簇信息 0:属于哪个簇 1:距离该簇中心点距离
    cluster = np.zeros((num,2))
    cluster[:,0] = -1

    
    ##记录是否有样本改变簇分类
    change = True
    ##初始化各簇中心点
    cp = findCenter(data,k)
    #cp = initCentroid(data, k)
    #print(cp)

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

            ##此时点已经分好类
        
        ## 根据样本重新分类  计算新的簇中心点
        for j in range(k):     
            pointincluster = data[[x for x in range(num) if cluster[x,0]==j]]
            #print(pointincluster)
            #如果
            if len(pointincluster) != 0:
                cp[j] = np.mean(pointincluster,axis=0)
    
    print("finish!")
    return cp,cluster

def merge(cluster, data, krange):
    #定义半径
    k = krange.shape[0]
    num = cluster.shape[0]
    margelist = np.zeros((k,2))

    ## 如果存在两个聚类x,y,z有相交， 那么记录两个聚类便于融合
    for i in range(k):
        for j in range(i+1,k):
            if(((krange[j,0]>krange[i,0])and(krange[j,0]<krange[i,1]))\
                or((krange[j,1]>krange[i,0])and(krange[j,1]<krange[i,1]))\
                or((krange[j,2]>krange[i,2])and(krange[j,2]<krange[i,3]))\
                or((krange[j,3]>krange[i,2])and(krange[j,3]<krange[i,3]))\
                or((krange[j,4]>krange[i,4])and(krange[j,4]<krange[i,5]))\
                or((krange[j,5]>krange[i,4])and(krange[j,5]<krange[i,5]))):
                    margelist[i] = i,j
                    break

    #定义汇聚节点将数组同一在一个祖先下， findroot[]中存储合并类
    findroot = []
    for i in range(k): 
        findroot.append(-1)

    for i in range(k):
        a = int(margelist[i,0])
        b = int(margelist[i, 1])
        find_root(findroot, a, b)

    #改变分类值符合预期
    set1 = set(findroot)
    for i in range(k):
        if(findroot[i] != -1):
            findroot[i] = findroot[i] % (len(set1))
        else:
            findroot[i] = len(set1) + 1

    print(findroot)
    #重新定义cluster
    for i in range(num):
        root = int(cluster[i,0])
        if(findroot[root] != -1):
            cluster[i, 0] = findroot[root]
    
    #重定义cluster后的自动生成的k 
    k = len(set1)

    return cluster,k

# 寻找根阶段数组
def find_root(findroot, a, b):
    if(findroot[a] == -1): 
        findroot[a] = a
    if(findroot[b]==-1):
        findroot[b] = findroot[a]
    else:
        for i in range(len(findroot)):
            if(findroot[i]==findroot[b]):
                findroot[i] = findroot[a]



def make_range(data, cluster, k):
    num = cluster.shape[0]
    #用来记录每一个区间的范围,0最小x, 1最大x， 2最小y, 3最大y， 4最小z， 5最大z
    krange = np.zeros((k,6))
    krange[:,0] = 999
    krange[:,1] = -1
    krange[:,2] = 999
    krange[:,3] = -1
    krange[:,4] = 999
    krange[:,5] = -1

    for i in range(num):
        m = int(cluster[i,0])
        if(krange[m,0] > data[i,0]): krange[m,0] = data[i,0]
        if(krange[m,1] < data[i,0]): krange[m,1] = data[i,0]
        if(krange[m,2] > data[i,1]): krange[m,2] = data[i,1]
        if(krange[m,3] < data[i,1]): krange[m,3] = data[i,1]
        if(krange[m,4] > data[i,2]): krange[m,4] = data[i,2]
        if(krange[m,5] < data[i,2]): krange[m,5] = data[i,2]

    #print(krange)
    return krange



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
        #if i//100 == mark :
        #counts[mark] += 1
            #每个簇分类计数
        ax.scatter(data[i,0],data[i,1],data[i,2],c=color[mark])
        
    #for i in range(k):
        #ax.scatter(cp[i,0],cp[i,1],cp[i,2],c=color[i],marker='x')
    #print(counts)
        
    plt.show()


k=30 ##分类个数
counts = np.zeros(k)


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

krange = make_range(data,cluster, k)
cluster,newk = merge(cluster,data, krange)
print(cluster)

Show(data,newk,cp,cluster)