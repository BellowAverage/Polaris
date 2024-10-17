
--- 
title:  【Python实例】-模拟发牌机器 
tags: []
categories: [] 

---
##### 实现随机发牌

```
import random
n=52
def gen_pocker(n):  #交换牌的顺序100次，达到洗牌目的
    x=100
    while(x&gt;0):
       x=x-1
       p1=random.randint(0,n-1)
       p2=random.randint(0,n-1)
       t=pocker[p1]
       pocker[p1]=pocker[p2]
       pocker[p2]=t 
    return pocker 
def getColor(x):   #获取牌的花色
    color=["草花","方块","红桃","黑桃"]
    c=int(x/13)
    if c&lt;0 or c&gt;=4:
        return "ERROR!"
    return color[c] 
def getValue(x):  #获取牌的牌面大小
    value=x % 13
    if value==0:
        return 'A'
    elif value&gt;=1 and value&lt;=9:
        return str(value+1)
    elif value==10:
        return 'J'
    elif value==11:
        return 'Q'
    elif value==12:
        return 'K'
 
def getPuk(x):
    return getColor(x)+getValue(x)
 #主程序
(a,b,c,d)=([],[],[],[])          # a,b,c,d四个列表分别存储4个人的牌
pocker=list(range(0,52))    #未洗牌之前
pocker=gen_pocker(n)        #洗牌目的
print(pocker)
for x in range(13):           #每人13张牌
    m=x*4
    a.append(getPuk(pocker[m]))
    b.append(getPuk(pocker[m+1]))
    c.append(getPuk(pocker[m+2]))
    d.append(getPuk(pocker[m+3]))

print("牌手1",end=":")
for x in a:
    print (x,end=" ")
print("\n牌手2",end=": ")
for x in b:
    print (x,end=" ")
print("\n牌手3",end=": ")   
for x in c:
    print (x,end=" ")
print("\n牌手4",end=": ")  
for x in d:
    print (x,end=" ")


```
