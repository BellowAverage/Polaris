
--- 
title:  数据分析：基于随机森林(RFC)对酒店预订分析预测 
tags: []
categories: [] 

---
## 数据分析：基于随机森林(RFC)对酒店预订分析预测

#### 文章目录
- - - - <li> 
  <ul>- - - - - - - - - - - - - 
## 1、前言

数据准备 <img src="https://img-blog.csdnimg.cn/17b95dbe6b9046e090428bb6acd08a10.png" alt="在这里插入图片描述">

## 2、数据探索

1.导入所需模块

```
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline 
import os
for dirname, _, filenames in os.walk('/home/mw/input/'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

```

<img src="https://img-blog.csdnimg.cn/b9f137d6be26474fa2c9e6d0d23ef652.png" alt="在这里插入图片描述"> 2.导入数据

```

df=pd.read_csv('/home/mw/input/1119442/hotel_bookings.csv')
df.head()

```

<img src="https://img-blog.csdnimg.cn/51ff681c1ede4bc98d44d19f72099e71.png" alt="在这里插入图片描述">

3.查看每列空值占比

```
df.isnull().mean()

```

<img src="https://img-blog.csdnimg.cn/846ad8dec9a94bc8b3a3fcea96f1ea71.png" alt="在这里插入图片描述">

4.查看数据基本信息

```
df.info()

```

<img src="https://img-blog.csdnimg.cn/6b85a2e9e3a04bff9ece84d1d2113678.png" alt="在这里插入图片描述">

5.使用describe()函数，计算数据集中每列的总数、均值、、最小值、25%、50%、75%分位数以及最大值并转置。

```
df.describe([0.01,0.05,0.1,0.25,0.5,0.75,0.99]).T

```

<img src="https://img-blog.csdnimg.cn/56eaa17d6ca440ffa389af246a2bd9b4.png" alt="在这里插入图片描述">

## 3、数据可视化分析

### 3.1酒店预订量和取消量

```
plt.figure(figsize=(15,8))
sns.countplot(x='hotel'
             ,data=df
             ,hue='is_canceled'
             ,palette=sns.color_palette('Set2',2)
            )

```

<img src="https://img-blog.csdnimg.cn/3f56850933784e888d97a1705e2ac0ae.png" alt="在这里插入图片描述">

```
hotel_cancel=(df.loc[df['is_canceled']==1]['hotel'].value_counts()/df['hotel'].value_counts()).sort_values(ascending=False)
print('酒店取消率'.center(20),hotel_cancel,sep='\n')

```

<img src="https://img-blog.csdnimg.cn/69363a33c4934a4b90a639cac4e92b9d.png" alt="在这里插入图片描述">

>  
 City Hotel的预定量与取消量都高于Resort Hotel，但Resort Hotel取消率为27.8%，而City Hotel的取消率达到了41.7% 


### 3.2酒店各月份预定量

```
city_hotel=df[(df['hotel']=='City Hotel') &amp; (df['is_canceled']==0)]
resort_hotel=df[(df['hotel']=='Resort Hotel') &amp; (df['is_canceled']==0)]
for i in [city_hotel,resort_hotel]:
    i.index=range(i.shape[0])

```

```
city_month=city_hotel['arrival_date_month'].value_counts()
resort_month=resort_hotel['arrival_date_month'].value_counts()
name=resort_month.index
x=list(range(len(city_month.index)))
y=city_month.values
x1=[i+0.3 for i in x]
y1=resort_month.values
width=0.3
plt.figure(figsize=(15,8),dpi=80)
plt.plot(x,y,label='City Hotel',color='lightsalmon')
plt.plot(x1,y1,label='Resort Hotel',color='lightseagreen')
plt.xticks(x,name)
plt.legend()
plt.xlabel('Month')
plt.ylabel('Count')
plt.title('Month Book')
for x,y in zip(x,y):
    plt.text(x,y+0.1,'%d' % y,ha = 'center',va = 'bottom')
    
for x,y in zip(x1,y1):
    plt.text(x,y+0.1,'%d' % y,ha = 'center',va = 'bottom')

```

<img src="https://img-blog.csdnimg.cn/1b16b61205e14a9186ddd8cd8d7f6af4.png" alt="在这里插入图片描述">

### 3.3客源地与预订取消率

```
country_book=df['country'].value_counts()[:10]
country_cancel=df[(df.country.isin (country_book.index)) &amp; (df.is_canceled==1)]['country'].value_counts()
plt.figure(figsize=(15,8))
sns.countplot(x='country'
              ,data=df[df.country.isin (country_book.index)]
              ,hue='is_canceled'
              ,palette=sns.color_palette('Set2',2)
             )
plt.title('Main Source of Guests')

```

<img src="https://img-blog.csdnimg.cn/3995a3edbf0b4d2f85a413729dab5a1c.png" alt="在这里插入图片描述">

```
country_cancel_rate=(country_cancel/country_book).sort_values(ascending=False)
print('各国客户取消率'.center(10),country_cancel_rate,sep='\n')

```

<img src="https://img-blog.csdnimg.cn/27868e2514a64ea4a3d9f38ed3a1d7d4.png" alt="在这里插入图片描述">

>  
 Resort hotel和City hotel的旺季均为夏季7、8月份，且客源主要为欧洲国家，符合欧洲游客偏爱夏季出游的特点，需要重点关注来自葡萄牙(PRT)和英国(BRT)等取消率高的主要客源 


### 3.4客户类型

```
city_customer=city_hotel.customer_type.value_counts()
resort_customer=resort_hotel.customer_type.value_counts()
plt.figure(figsize=(21,12),dpi=80)
plt.subplot(1,2,1)
plt.pie(city_customer,labels=city_customer.index,autopct='%.2f%%')
plt.legend(loc=1)
plt.title('City Hotel Customer Type')
plt.subplot(1,2,2)
plt.pie(resort_customer,labels=resort_customer.index,autopct='%.2f%%')
plt.title('Resort Hotel Customer Type')
plt.legend()
plt.show()

```

<img src="https://img-blog.csdnimg.cn/f3d3017f9c3540e99aca50c7f397beb4.png" alt="在这里插入图片描述">

>  
 酒店的主要客户类型都是散客(Transient)，占比均为70%左右 


### 3.5酒店预订途径

```
city_segment=city_hotel.market_segment.value_counts()
resort_segment=resort_hotel.market_segment.value_counts()
plt.figure(figsize=(21,12),dpi=80)
plt.subplot(1,2,1)
plt.pie(city_segment,labels=city_segment.index,autopct='%.2f%%')
plt.legend()
plt.title('City Hotel Market Segment')
plt.subplot(1,2,2)
plt.pie(resort_segment,labels=resort_segment.index,autopct='%.2f%%')
plt.title('Resort Hotel Market Segment')
plt.legend()
plt.show()

```

<img src="https://img-blog.csdnimg.cn/9007f2a1c70f4290a1c4102bab5650ed.png" alt="在这里插入图片描述">

>  
 两间酒店的客源主要来自线上旅游机构，其在City Hotel的占比甚至超过5成；线下旅游机构的比重次之，均为20%左右 


### 3.6各类旅客日均开销

```
plt.figure(figsize=(15,8))
sns.boxplot(x='customer_type'
            ,y='adr'
            ,hue='hotel'
            ,data=df[df.is_canceled==0]
            ,palette=sns.color_palette('Set2',2)
           )
plt.title('Average Daily Rate of Different Customer Type')

```

<img src="https://img-blog.csdnimg.cn/79f55e92fddb4b44aba6aae8d92f3e67.png" alt="在这里插入图片描述">

>  
 City Hotel各类客户的日均开销均高于Resort Hotel；在四种类型的客户中，散客（Transient）的消费最高，团体客（Group）最低 


### 3.7新老客数量与取消预订率

```
plt.figure(figsize=(15,8))
sns.countplot(x='is_repeated_guest'
              ,data=df
              ,hue='is_canceled'
              ,palette=sns.color_palette('Set2',2)
             )
plt.title('New/Repeated Guest Amount')
plt.xticks(range(2),['no','yes'])

```

<img src="https://img-blog.csdnimg.cn/ed4dc0bf365b43e190f90011ca9b23f7.png" alt="在这里插入图片描述">

```
guest_cancel=(df.loc[df['is_canceled']==1]['is_repeated_guest'].value_counts()/df['is_repeated_guest'].value_counts()).sort_values(ascending=False)
guest_cancel.index=['New Guest', 'Repeated Guest']
print('新老客取消率'.center(15),guest_cancel,sep='\n')

```

<img src="https://img-blog.csdnimg.cn/3948440d826943668bed16d80f8fcd68.png" alt="在这里插入图片描述">

>  
 老客的取消率为14.4%，而新客的取消率则达到了37.8%，高出老客24个百分点 


### 3.8押金方式与预定取消率

```
print('三种押金方式预定量'.center(15),df['deposit_type'].value_counts(),sep='\n')

```

<img src="https://img-blog.csdnimg.cn/da8f46db224c42d0b06b14ded222c397.png" alt="在这里插入图片描述">

```
deposit_cancel=(df.loc[df['is_canceled']==1]['deposit_type'].value_counts()/df['deposit_type'].value_counts()).sort_values(ascending=False)
plt.figure(figsize=(8,5))
x=range(len(deposit_cancel.index))
y=deposit_cancel.values
plt.bar(x,y,label='Cancel_Rate',color=['orangered','lightsalmon','lightseagreen'],width=0.4)
plt.xticks(x,deposit_cancel.index)
plt.legend()
plt.title('Cancel Rate of Deposite Type')
for x,y in zip(x,y):
    plt.text(x,y,'%.2f' % y,ha = 'center',va = 'bottom')

```

<img src="https://img-blog.csdnimg.cn/e9ba3fa4a6c04256ac6190f9cc849326.png" alt="在这里插入图片描述">

>  
 无需押金(‘No Deposit’)是预定量最高的方式，且取消率较低，而不退押金(Non Refund)这一类型的取消预订率高达99%，可以减少这一类型的押金方式以减少客户取消率 


### 3.9房间类型与预定取消量

```
plt.figure(figsize=(15,8))
sns.countplot(x='assigned_room_type'
              ,data=df
              ,hue='is_canceled'
              ,palette=sns.color_palette('Set2',2)
             )
plt.title('Book &amp; Cancel Amount of Room Type')

```

<img src="https://img-blog.csdnimg.cn/78a8cb8d8329475592caa88e4faea746.png" alt="在这里插入图片描述">

```
room_cancel=df.loc[df['is_canceled']==1]['assigned_room_type'].value_counts()[:7]/df['assigned_room_type'].value_counts()[:7]
print('不同房型取消率'.center(5),room_cancel.sort_values(ascending=False),sep='\n')

```

<img src="https://img-blog.csdnimg.cn/78ac8773f2534db8a9849f94d90df66a.png" alt="在这里插入图片描述">

>  
 在预定量前7的房型中，A、G房型的取消率均高于其他房型，A房型的取消率更是高达44.5% 


## 4.数据预处理

建模的目的是为了预测旅客是否会取消酒店的预订，后续需要将’is_canceled’设为标签y，其余为特征x。日期特征’is_cance’reservation_status_date’不会直接影响标签，所以删除

```
df1=df.drop(labels=['reservation_status_date'],axis=1)

```

### 4.1处理分类型变量

```

cate=df1.columns[df1.dtypes == "object"].tolist()
#用数字表现的分类型变量
num_cate=['agent','company','is_repeated_guest']
cate=cate+num_cate

```

```
results={<!-- -->}
for i in ['agent','company']:
    result=np.sort(df1[i].unique())
    results[i]=result
results

```

<img src="https://img-blog.csdnimg.cn/7811cbaa15f94a799519cb5011cdd32f.png" alt="在这里插入图片描述">

**agent和company列空值占比较多且无0值，所以用0填补**

```
df1[['agent','company']]=df1[['agent','company']].fillna(0,axis=0)

```

```
df1.loc[:,cate].isnull().mean() 

```

<img src="https://img-blog.csdnimg.cn/ef88703aad564077ac8368ed7b5da2f8.png" alt="在这里插入图片描述">

**创造新变量in_company和in_agent对旅客分类,company和agent为0的设为NO,非0的为YES**

```
df1.loc[df1['company'] == 0,'in_company']='NO'
df1.loc[df1['company'] != 0,'in_company']='YES'
df1.loc[df1['agent'] == 0,'in_agent']='NO'
df1.loc[df1['agent'] != 0,'in_agent']='YES'

```

**创造新特征same_assignment,若预订的房间类型和分配的类型一致则为yes，反之为no**

```
df1.loc[df1['reserved_room_type'] == df1['assigned_room_type'],'same_assignment']='Yes'
df1.loc[df1['reserved_room_type'] != df1['assigned_room_type'],'same_assignment']='No'

```

**删除’reserved_room_type’,‘assigned_room_type’,‘agent’,'company’四个特征**

```
df1=df1.drop(labels=['reserved_room_type','assigned_room_type','agent','company'],axis=1)

```

**重新设置’is_repeated_guest’，常客标为YES，非常客为NO**

```
df1['is_repeated_guest'][df1['is_repeated_guest']==0]='NO'
df1['is_repeated_guest'][df1['is_repeated_guest']==1]='YES'

```

```
df1['country']=df1['country'].fillna(df1['country'].mode()[0])

```

```
for i in ['in_company','in_agent','same_assignment']:
    cate.append(i)

for i in ['reserved_room_type','assigned_room_type','agent','company']:
    cate.remove(i)
cate

```

<img src="https://img-blog.csdnimg.cn/84b546c4691d4ffa86b94730b35ec0bf.png" alt="在这里插入图片描述"> **对分类型特征进行编码**

```
from sklearn.preprocessing import OrdinalEncoder
oe = OrdinalEncoder()
oe = oe.fit(df1.loc[:,cate])
df1.loc[:,cate] = oe.transform(df1.loc[:,cate])

```

### 4.2处理连续型变量

**筛选出连续型变量，需要先删除’is_canceled’这一标签**

```
col=df1.columns.tolist()
col.remove('is_canceled')
for i in cate:
    col.remove(i)
col

```

<img src="https://img-blog.csdnimg.cn/e64dff3772964de59adb4e74c8a0bb50.png" alt="在这里插入图片描述"> **统计空值**

```
df1[col].isnull().sum()

```

<img src="https://img-blog.csdnimg.cn/5ec8c374f2364d8fa3549ff74e2d5111.png" alt="在这里插入图片描述"> **使用众数填补xtrain children列的空值**

```
df1['children']=df1['children'].fillna(df1['children'].mode()[0])

```

**连续型变量进行无量纲化**

```
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss = ss.fit(df1.loc[:,col])
df1.loc[:,col] = ss.transform(df1.loc[:,col])

```

### 4.3各变量的相关性系数

```
cor=df1.corr()
cor=abs(cor['is_canceled']).sort_values()
cor

```

<img src="https://img-blog.csdnimg.cn/f73097a1a75b4e9d866a95a82e243012.png" alt="在这里插入图片描述">

```
plt.figure(figsize=(8,15))
x=range(len(cor.index))
name=cor.index
y=abs(cor.values)
plt.barh(x,y,color='salmon')
plt.yticks(x,name)
for x,y in zip(x,y):
    plt.text(y,x-0.1,'%.2f' % y,ha = 'center',va = 'bottom')
plt.xlabel('Corrleation')
plt.ylabel('Varriance')
plt.show()

```

<img src="https://img-blog.csdnimg.cn/fe217cb53ae34d6e901b6cd23337e522.png" alt="在这里插入图片描述">

>  
 预订状态（‘reservation_status’)与是否取消预订的相关性最高，达到了0.92，但考虑到后续可能会导致模型过拟合，所以删除；押金类型(‘deposit_type’)则达到了0.47，创造的特征预订和分配房型是否一致(‘same_assignment’)也有0.25的相关性 


## 5.建模预测

**划分特征x和标签y**

```
df2=df1.drop('reservation_status',axis=1)
x=df2.loc[:,df2.columns != 'is_canceled' ]
y=df2.loc[:,'is_canceled']
from sklearn.model_selection import train_test_split as tts
xtrain,xtest,ytrain,ytest=tts(x,y,test_size=0.3,random_state=90)
for i in [xtrain,xtest,ytrain,ytest]:
    i.index=range(i.shape[0])

```

### 5.1随机森林

```
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score as cvs,KFold
from sklearn.metrics import accuracy_score
rfc=RandomForestClassifier(n_estimators=100,random_state=90)
cv=KFold(n_splits=10, shuffle = True, random_state=90)
rfc_score=cvs(rfc,xtrain,ytrain,cv=cv).mean()
rfc.fit(xtrain,ytrain)
y_score=rfc.predict_proba(xtest)[:,1]
rfc_pred=rfc.predict(xtest)
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score as AUC
FPR, recall, thresholds = roc_curve(ytest,y_score, pos_label=1)
rfc_auc = AUC(ytest,y_score)

```

**绘制ROC曲线**

```
plt.figure(figsize=(8,8))
plt.plot(FPR, recall, color='red',label='ROC curve (area = %0.2f)' % rfc_auc)
plt.plot([0, 1], [0, 1], color='black', linestyle='--')
plt.xlim([-0.05, 1.05])
plt.ylim([-0.05, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('Recall')
plt.title('Random Forest Classifier ROC Curve')
plt.legend(loc="lower right")
plt.show()

```

<img src="https://img-blog.csdnimg.cn/583c5ea504d443d98004e4a2fd494b8b.png" alt="在这里插入图片描述"> **查看模型classification_report**

```
from sklearn.metrics import classification_report as CR
print('随机森林'.center(50), CR(ytest,rfc_pred),sep='\n')

```

<img src="https://img-blog.csdnimg.cn/81beb6741b254f92aad755af56578b65.png" alt="在这里插入图片描述">

```
score={<!-- -->'Model_score':[rfc_score],'Auc_area':[rfc_auc]}
score_com=pd.DataFrame(data=score,index=['RandomForest'])
score_com.sort_values(by=['Model_score'],ascending=False)

```

<img src="https://img-blog.csdnimg.cn/b3cf9eb6611d4cdeb0718e60c370ea24.png" alt="在这里插入图片描述">

>  
 随机森林的准确度达到了88.8%，AUC面积也有0.95，可以通过调参来继续提升模型的效果 


## 分析总结

1.City Hotel的预定量和取消率都远高于Resort Hotel，该酒店应对客户展开调研，深入了解导致客户最终放弃预订的因素从而降低客户的取消率

2.酒店应利用好每年7、 8月的旅游旺季，可以在保证服务质量的同时适当提高价格获取更多利润，在淡季（冬季）的时候进行优惠活动，如圣诞大促和新年活动，减少酒店空房率

3.酒店需分析来自葡萄牙、英国等主要客源国的客户画像，了解这些客户的属性标签、偏好与消费特征，推出专属服务从而降低客户的取消率

4.由于散客是酒店的主要客户群且消费水平较高，酒店可以通过线上和线下旅游机构的途径，加大对自由行的宣传营销，从而吸引更多该类型的游客

5.新客的取消率比老客高24%，因此，酒店应重点关注新客的预订与入住体验，为新客提供更多指引与优惠，如为首次入住的客户提供折扣，调研新客对入住满意与不满意的反馈以提升日后服务，同时维护好老客

6.不退押金(Non Refund)这一类型的取消预订率高达99%，酒店应优化这种方式，如返还50%的押金，或者可以直接取消这一种方式，从而提高入住率

7.A、G房型的取消率远高于其他房型，酒店方应在客户在预订的时候跟客户仔细确认房间信息，让客户对房间情况有充分了解，避免认知错误，同时可以对房间设施进行优化并提高服务水平

转：https://blog.csdn.net/AOAIYI/article/details/129381319
