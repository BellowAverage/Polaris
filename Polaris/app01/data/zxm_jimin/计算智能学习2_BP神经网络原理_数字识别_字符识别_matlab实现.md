
--- 
title:  计算智能学习2_BP神经网络原理_数字识别_字符识别_matlab实现 
tags: []
categories: [] 

---


#### 文章目录
- - - - - - - - 


## 人工神经网络的基本结构

人工神经网络的互连结构（或称拓扑结构）是指单个神经元之间的连接 模式，它是构造神经网络的基础，也是神经网络诱发偏差的主要来源。从互连结构的角度： <img src="https://img-blog.csdnimg.cn/2021020409590274.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

## BP神经网络原理

误差反传（error BackPropagation，简称BP）算法是迄今为止最成功的神经网络学习算法。通过迭代处理的方法，不断调整连接神经元的网络权重，使最终输出结果和预期结果的误差最小。

BP网络一般是指用BP算法训练的多层前馈神经网络。 理论已经证明一个三层网络可以无限近似任意连续函数。下图为经典三层BP网络结构为例： <img src="https://img-blog.csdnimg.cn/20210204103634363.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **网络结构** <img src="https://img-blog.csdnimg.cn/20210204104636683.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210204114201839.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210204114227404.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210204114304304.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210204114322896.png" alt="在这里插入图片描述">

**算法总体流程如下：** <img src="https://img-blog.csdnimg.cn/2021020411381952.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **BP网络优点：** 具有非线性映射能力，理论上可以无限逼近任意复杂函数； 网络结构简单，计算复杂度低； 具有较好的容错能力，网络结构部分受损不会对结果产生很大的影响；

**BP网络问题：** 样本依赖性强，比较容易过拟合； 误差反传有**水波现象(gradient diffusion（梯度扩散）)**，梯度越来越稀疏， 从顶层越往下，误差校正信号越来越小。 网络结构和初始参数对结果影响很大，容易收敛到局部最小值； 训练速度比较慢，效率相比SVM和boosting没有优势； 多层网络参数存在组合爆炸问题。

## 实验部分（matlab实现）

## 一、需求分析

本实验为了解和测试BP神经网络在**数字识别上的应用**。 1、 根据老师提供的测试代码，进行分析。 2、 修改网络的架构（修改参数）。 3、 根据识别的正确率进行相关网络参数的分析。

## 二、概要设计

```
feature_lattice.m
输入:黑底白字的二值图像。输出：35维的网格特征

```

提取特征，转成5**7的特征矢量,把图像中每10**10的点进行划分相加，进行相加成一个点;即统计每个小区域中图像象素所占百分比作为特征数据. read_train.m 读取文件夹, 读取文件。 network_train.m 训练BP网络 输入：训练图像特征和label。输出：训练好的神经网络 network_test.m BP网络预测 输入：测试数据的特征和真值。输出：测试数据的label以及误差图 main.m 调用各个函数，实现BP数字识别

## 三、详细设计（代码）

feature_lattice.m

```
function feature = feature_lattice(img)
% 输入:黑底白字的二值图像。输出：35维的网格特征

% ======提取特征，转成5*7的特征矢量,把图像中每10x10的点进行划分相加，进行相加成一个点=====%
%======即统计每个小区域中图像象素所占百分比作为特征数据====%

for i=1:length(img);
bw2=im2bw(img{i},graythresh(img{i}));
bw_7050=imresize(bw2,[70,50]);%放大
for cnt=1:7%切割
    for cnt2=1:5
        Atemp=sum(bw_7050(((cnt*10-9):(cnt*10)),((cnt2*10-9):(cnt2*10))));%10*10box
        lett((cnt-1)*5+cnt2)=sum(Atemp);%每个像素点里面不为0的个数
    end
end
lett=((100-lett)/100);%缩小
lett=lett';
feature(:,i)=lett;
end
read_train.m
function [imglist] = read_train(root)
% ni为读取图片张数，n为文件夹数目
%========读取文件夹========%
out_Files = dir(root);%展开
tempind=0;
imglist=cell(0);
n=length(out_Files);
%========读取文件========%
for i = 1:n;
    if strcmp(out_Files(i).name,'.')|| strcmp(out_Files(i).name,'..')
    else
        rootpath=strcat(root,'/',out_Files(i).name);
        in_filelist=dir(rootpath);
        ni=length(in_filelist);
        for j=1:ni
            if strcmp(in_filelist(j).name,'.')|| strcmp(in_filelist(j).name,'..')|| strcmp(in_filelist(j).name,'Desktop_1.ini')|| strcmp(in_filelist(j).name,'Desktop_2.ini')
            else
                tempind=tempind+1;
                imglist{tempind}=imread(strcat(rootpath,'/',in_filelist(j).name));
            end
        end
    end
end
end

```

network_train.m

```
function net = network_train(train_data,train_label )
% 输入：训练图像特征和label。输出：训练好的神经网络

% BP网络训练
% 初始化网络结构
layer=25;
net=newff(train_data,train_label,layer);
net.trainParam.epochs=700;%回滚次数
net.trainParam.lr=0.3;%学习率
net.trainParam.goal=0.0007;%最后总误差在0.001以内
net.trainFcn='trainrp';%训练方法

% net_1.trainParam.show=50;
% net_1.trainParam.lr=0.05;
% net_1.trainParam.mc=0.9;
% net_1.trainParam.epochs=5000;
% net_1.trainParam.goal=0.05;
%net.trainFcn='trainlm';
% 网络训练
net=train(net,train_data,train_label);
end

```

network_test.m

```
function out = network_test(test_data,net)
% 输入：测试数据的特征和真值。输出：测试数据的label以及误差图
% BP网络预测

an=sim(net,test_data);
for i=1:length(test_data)
    out(i)=find(an(:,i)==max(an(:,i)));
end

end

```

main.m

```
clc;
clear all;
close all;
%% 读取图像
root='./data';
img=read_train(root);
%% 提取特征
img_feature=feature_lattice(img);
%% 构造标签
class=10;%10行
numberpclass=500;%500列
ann_label=zeros(class,numberpclass*class);
ann_data=img_feature;
for i=1:class
 for j=numberpclass*(i-1)+1:numberpclass*i
     ann_label(i,j)=1;
     %给每一列打上一个标签，方便后面训练
 end
end

%% 选定训练集和测试集
k=rand(1,numberpclass*class);  
[m,n]=sort(k);  
ntraindata=4500;
ntestdata=500;
train_data=ann_data(:,n(1:ntraindata));
test_data=ann_data(:,n(ntraindata+1:numberpclass*class));
%数据切割，数据打上标签 10行n列
train_label=ann_label(:,n(1:ntraindata));
test_label=ann_label(:,n(ntraindata+1:numberpclass*class));
%% BP神经网络创建，训练和测试
net=network_train(train_data,train_label);
predict_label=network_test(test_data,net);%预测
%% 正确率计算
[u,v]=find(test_label==1);
label=u';
error=label-predict_label;
accuracy=size(find(error==0),2)/size(label,2)

```

## 四、实验结果总结

实验结果与分析： layer=25; net=newff(train_data,train_label,layer); net.trainParam.epochs=900;%回滚次数 net.trainParam.lr=0.1;%学习率 net.trainParam.goal=0.001;%最后总误差在0.001以内 net.trainFcn=‘trainrp’;%训练方法 <img src="https://img-blog.csdnimg.cn/20190226161957449.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 正确率基本稳定在86%左右。

1、进行修改： （仅仅修改隐含层节点数）layer=20; <img src="https://img-blog.csdnimg.cn/20190226161912257." alt="在这里插入图片描述"> 正确率下降，分析原因：隐藏层含节点数太少,BP神经网络不能建立复杂的映射关系,精度下降。

2、进行修改： （仅仅修改隐含层节点数）layer=30; <img src="https://img-blog.csdnimg.cn/20190226161900643." alt="在这里插入图片描述"> 正确率上升，分析原因：隐藏层含节点数合适，精度上升。

3、进行修改： 在layer=30的基础上，修改迭代次数： net.trainParam.epochs=700;%回滚次数 <img src="https://img-blog.csdnimg.cn/20190226161850659." alt="在这里插入图片描述"> 正确率上升，分析原因：可能是回滚次数比较少，反而减少了数据的过拟合，从而精度上升。

4、进行修改： 在layer=30 ;net.trainParam.epochs=700;的基础上，修改学习率： net.trainParam.lr=0.2; <img src="https://img-blog.csdnimg.cn/20190226161837350." alt="在这里插入图片描述"> 正确率下降，分析原因：学习率较大，导致网络的权重和阈值震动太大，从而精度下降。

5、进行修改： layer=30 ;net.trainParam.epochs=700; net.trainParam.lr=0.1;的基础上，修改误差参数： net.trainParam.goal=0.0007; <img src="https://img-blog.csdnimg.cn/2019022616182475." alt="在这里插入图片描述"> 正确率下降，分析原因：期望误差过小，反而导致了数据的过拟合，精度下降。

6、进行修改： layer=30 ;net.trainParam.epochs=700; net.trainParam.lr=0.1;的基础上，添加隐含层： net=newff(train_data,train_label,{layer 27}) ;加了1个隐含层 <img src="https://img-blog.csdnimg.cn/20190226161812613." alt="在这里插入图片描述"> 正确率略有上升，分析原因：增加隐含层，进一步降低误差，精度提高。

7、进行修改： layer=30 ;net.trainParam.epochs=700; net.trainParam.lr=0.1;的基础上，添加隐含层： net=newff(train_data,train_label,{layer 30 30}) ; <img src="https://img-blog.csdnimg.cn/20190226161756434." alt="在这里插入图片描述"> 正确率略有上升，分析原因：增加隐含层，进一步降低误差，精度提高，并且，精度的提高实际上也可以通过增加隐层神经元的数目来获得。

8、进行修改： layer=30 ;net.trainParam.epochs=700; net.trainParam.lr=0.1;的基础上，添加隐含层节点数： net=newff(train_data,train_label,{layer 40 40}) ;

<img src="https://img-blog.csdnimg.cn/20190226161727838." alt="在这里插入图片描述"> 正确率略有上升，分析原因：精度的提高实际上也可以通过增加隐层神经元的数目来获得。

## 代码下载

**注意，代码下载后仍需自行调试~** 积分值为5（如果有变为csdn自行修改）——完整代码其实和上面贴出的差别不大，酌情下载~ https://download.csdn.net/download/zxm_jimin/10976756

**感谢各位大佬看到最后~ 本文为原创。转载请注明出处。 注：原理与实验部分，参考了一些文章，博客，如有侵权请联系，我附上原出处。**
