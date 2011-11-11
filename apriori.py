# -*- coding: cp936 -*-
import copy

#D=[['A','B','C','D'],
#   ['B','C','E'],
#   ['A','B','C','E'],
#   ['B','D','E'],
#   ['A','B','C','D']
#   ]
D=[['I1','I2','I5'],
   ['I2','I4'],
   ['I2','I3'],
   ['I1','I2','I4'],
   ['I1','I3'],
   ['I2','I3'],
   ['I1','I3'],
   ['I1','I2','I3','I5'],
   ['I1','I2','I3']
   ]
L = []
for T in D:
    print T
print

#找频繁1项集，扫描一遍数据库
def find_frequent_1_itemsets(D):
    mapI = {}
    F1 = []
    for T in D:
        for i in T:
            if mapI.has_key(i):
                mapI[i]+=1
            else:
                mapI[i]=1
    for k in [k for k,v in mapI.items() if v>=2]:
        l=[]
        l.append(k)
        F1.append(l)
    return F1

#连接步
def comb(arr1,arr2):
    tmap={}
    for v in arr1+arr2 : tmap[v]="" 
    return tmap.keys()

#生成比L高一项的候选项集
def apriori_gen(L):
    nextL = {}
    s=""
    for i in L:
        for j in L:
            com=comb(i,j)
            if len(com)!=len(j)+1:
                continue
            com.sort()
            if has_infrequent_subset(com, L):
                continue
            key=s.join(com)
            if not nextL.has_key(key):
                nextL[key] = com
    return nextL.values()

def subset(c,l):
    for i in c:
        if i not in l:
            return False
    return True

#剪枝步
def has_infrequent_subset(c,preL):
    for i in c:
        work = copy.copy(c)
        work.remove(i)
        if work not in preL:
            return True
    return False
        

L.append(find_frequent_1_itemsets(D))
print "第1 次项频繁项集："
print L[0]
i=0
s=""
while len(L[i])!=0:
    L.append([])
    C = apriori_gen(L[i])
    print "第",i+2,"次项候选项集："
    print C
    CMap = {}
    CMapCnt = {}
    
    #计数，每一项集扫描一趟
    for T in D:
        for item in C:
            if subset(item,T):
                key=s.join(item)
                if CMap.has_key(key):
                    CMapCnt[key] +=1
                else:
                    CMap[key]=item
                    CMapCnt[key]=1
    for k in [k for k,v in CMapCnt.items() if v>=2]:
        L[i+1].append(CMap[k])
    i+=1
    print "第",i+1,"次项频繁项集："
    print L[i]
    