
--- 
title:  计算智能学习1_感知机原理_水果生熟分类器_matlab实现 
tags: []
categories: [] 

---


#### 文章目录
- - - - - - - - - - - - - - - 


## 感知机（Perceptron）原理

单层感知机是最早使用的，也是最简单的神经网络结构，由一个或多个线性阈值单元组成。

**单层感知机模型：** <img src="https://img-blog.csdnimg.cn/20210204090129420.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210204090917138.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

**线性阈值单元：**

**在生物神经网络中，每个神经元（neuron）与其他神经元连接，当它“兴奋”时，就会向相连的神经元发送化学物质，从而改变这些神经元内的电位；如果某个神经元的电位已经超过一个阈值，那么它就会被激活。** <img src="https://img-blog.csdnimg.cn/20210204092528650.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

输入x是一个n维实数矢量，权W也是一个n维实数 矢量，阈值θ是一个实数，而输出y是一个二值变量。

综合在一起得： <img src="https://img-blog.csdnimg.cn/20210204092640775.png" alt="在这里插入图片描述">

作为最原始、最简单的神经网络结构，单层感知机是很多其他网络结构的基本单元(人工神经元）。

感知机能容易的实现逻辑与、或、非运算。 <img src="https://img-blog.csdnimg.cn/2021020409311986.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210204093134877.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210204093157154.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210204093219319.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210204100428730.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210204100447325.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 感知机不能拟合XOR函数，它只能产生线性分割面 <img src="https://img-blog.csdnimg.cn/089626d8415e4eefac2b216b02826f8e.png" alt="在这里插入图片描述"> 多层感知机可以解决此问题

**感知机算法** <img src="https://img-blog.csdnimg.cn/20210204103308462.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/890ceebacd6f4e6c8e86b4fc1e66b23d.png" alt="在这里插入图片描述">

感知机只有输出层神经元进行激活函数处理，即只拥有一层功能神经元（functional neuron），其学习能力非常有限。 <img src="https://img-blog.csdnimg.cn/ad050f612a6b414481455dc93e054b23.png" alt="在这里插入图片描述">

## 实验部分 matlab实现

## 小实验一：分析水果是生是熟

## 一、需求分析

自己设计数据进行感知机的测试,并进行一个小实验一，测试提取的图片是生的还是熟的，进行数据分类。

## 二、概要设计

**1.感知神经网络的构建**

1.1 生成网络

```
net=newp([-1 1],1) %单输入，输入值为[-1,1]之间的数

```

1.2 网络仿真

```
net.IW{1,1}
net.b{1}
%权重，net.IW{i,j}表示第i层网络第j个神经元的权重向量

```

PS：此处也有其他方式

```
% 改变权值和阈值为随机数
net.inputweights{1,1}.initFcn='rands';
net.biases{1}.initFcn='rands';

```

**2.感知器神经网络的学习和训练** 2.1 网络学习 样本值大于0，标记为0；样本值小于0，标记为1

```
P=[1 -3 0.9 -0.1];
T=[0 1 0 1]; %训练数据
net=adapt(net,P,T);  %利用输入样本调节神经网net

```

2.2 网络训练

```
net.adaptParam.passes=3;      %在训练过程中重复次数为3
net.adaptParam.passes=6; %在训练过程中重复次数为6
%passes决定在训练过程中训练值重复的次数。
net=adapt(net,P,T);

```

**3.二输入感知器分类可视化问题** 3.1 画出分类线

```
net.IW{1,1}
net.b{1}
plotpc(net.IW{1,1},net.b{1})

```

3.1仿真

```
%a=sim(net,p);
%plotpv(p,a)
p=[0.5;1.0];
a=sim(net,p);
plotpv(p,a);
hold on;
plotpv(P,T);
plotpc(net.IW{1},net.b{1})

```

**4.读取图片颜色** 4.1提取红分量，不满足阈值的变为白色

```
a=imread('D:\workspace\Matlab workspace\人工智能\sy1\test\芒果\熟的\2.jpg');%读取彩图
[m,n,d]=size(a);
b=uint8(a);%转为uint8数据类型，计算图像像素
imshow(b);
level=0;%设置阈值
figure(5);
subplot(2,2,1);imshow(a);title('原图');%显示原图

%提取红分量，不满足阈值的变为白色
for i=1:m
    for j=1:n
        if((a(i,j,1)-a(i,j,2)&gt;level)&amp;&amp;(a(i,j,1)-a(i,j,3)&gt;level))
            b(i,j,1)=a(i,j,1);
            b(i,j,2)=a(i,j,2);
            b(i,j,3)=a(i,j,3);
        else b(i,j,1)=255;
            b(i,j,2)=255;
            b(i,j,3)=255;
        end
    end
end
subplot(2,2,2);imshow(b);title('提取红分量后');%显示提取红分量后的图

```

4.2将修改后的图片与原图相比较，如果差别较大，判断为生的，差别不大，判断为熟的

```
sum1=sum(sum(b));
sum2=255*m*n;
if(sum1&gt;0.8*sum2)
    pp=[-0.5];%负数对应生的
else
    pp=[0.5];%正数对应熟的
end

```

因为网络相对比较简单，所以改变参数无法看到比较明显的效果。 参数设置方面在“测试上课是否迟到”小实验中体现。

## 三、详细设计(完整代码）

```
% 水果是生是熟
P=[1 -3 0.9 -0.1];
T=[0 1 0 1];
net=newp([-1 1],1);

figure(1);
plotpc(net.IW{1,1},net.b{1})  %%画分类线
plotpv(P,T);                % plotpv函数利用感知器的输入向量和目标向量来画输入向量的图像
net=adapt(net,P,T);  %利用输入样本调节神经网net 
net.IW{1,1}
net.b{1}
plotpc(net.IW{1,1},net.b{1})  %重新画分类线
net.adaptParam.passes=3;      %在训练过程中重复次数为3
net=adapt(net,P,T);
net.IW{1,1}
net.b{1}
plotpc(net.IW{1},net.b{1})
net.adaptParam.passes=6;
net=adapt(net,P,T);
net.IW{1,1}
net.b{1}
plotpc(net.IW{1},net.b{1})
% %仿真
% a=sim(net,p);
% plotpv(p,a)
figure(1);
p=[0.5];
a=sim(net,p);
plotpv(p,a);
hold on;
plotpv(P,T);
plotpc(net.IW{1},net.b{1})
%感知器能够正确分类，从而网络可行)

figure(3);
a=imread('D:\workspace\Matlab workspace\人工智能\sy1\test\芒果\熟的\2.jpg');%读取彩图
[m,n,d]=size(a);
b=uint8(a);%转为uint8数据类型，计算图像像素
imshow(b);
level=0;%设置阈值
figure(5);
subplot(2,2,1);imshow(a);title('原图');%显示原图

%提取红分量，不满足阈值的变为白色
for i=1:m
    for j=1:n
        if((a(i,j,1)-a(i,j,2)&gt;level)&amp;&amp;(a(i,j,1)-a(i,j,3)&gt;level))
            b(i,j,1)=a(i,j,1);
            b(i,j,2)=a(i,j,2);
            b(i,j,3)=a(i,j,3);
        else b(i,j,1)=255;
            b(i,j,2)=255;
            b(i,j,3)=255;
        end
    end

end
subplot(2,2,2);imshow(b);title('提取红分量后');%显示提取红分量后的图
sum1=sum(sum(b));
sum2=255*m*n;
if(sum1&gt;0.8*sum2)
    pp=[-0.5];
else
    pp=[0.5];
end

figure(4);
b=sim(net,pp);
plotpv(pp,b);
hold on;
plotpv(P,T);
plotpc(net.IW{1},net.b{1})

```

## 四、实验结果总结

**数据解释：** 读取已有图片，根据图片中是否可以提取出红色色素，设非红色的像素点为白色，将得出的图片与全白的图片进行比较，如果得到的值太小，说明没有提取到红色像素；则结果为水果是生的，pp=[-0.5]；如果值数合理，则结果为水果是熟的，pp=[0.5]。结果输出正确。

训练后的网络： <img src="https://img-blog.csdnimg.cn/20190226171607352.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 放入生的芒果的图片： <img src="https://img-blog.csdnimg.cn/20190226171654944.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190226171722444.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">仿真结果： <img src="https://img-blog.csdnimg.cn/20190226171734997." alt="在这里插入图片描述"> 可视化分类： <img src="https://img-blog.csdnimg.cn/2019022617174559.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 放入熟的芒果的图片： <img src="https://img-blog.csdnimg.cn/20190226171818494.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

仿真结果： <img src="https://img-blog.csdnimg.cn/20190226171832510." alt="在这里插入图片描述"> 可视化分类： <img src="https://img-blog.csdnimg.cn/20190226171841138.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

## 小实验二：测试上课是否迟到

## 一、需求分析

自己设计数据进行感知机的测试,并进行一个小实验二，测试上课是否迟到，设计数据，在trainData.txt中读入测试数据，进行数据分类（迟到与不迟到）。

## 二、概要设计

**1. 感知器神经网络的构建**

```
%读取训练数据
[f1,f2,class] = textread('test/trainData.txt' , '%f%f%f',10);
P=[f1 f2];
T=[class];
P=P';
T=T';
disp(P);
disp(T);
net=newp([-1 1;-1 1],1);
net.b{1}=[0];
w=[0.5 -0.6];
plotpc(net.IW{1,1},net.b{1}) 	 %画分类线
plotpv(P,T);               		 % plotpv函数利用感知器的输入向量和目标向量来画输入向量的图像

```

发现数据与分类线相隔太远，没有联系 换成随机的权重与阈值

```
net.inputweights{1,1}.initFcn='rands';
net.biases{1}.initFcn='rands';

```

也是没有联系

**2.感知器神经网络的学习和训练** 2.1 网络学习

```
net=adapt(net,P,T);  %利用输入样本调节神经网net 
net.IW{1,1}
net.b{1}
plotpc(net.IW{1,1},net.b{1})  %重新画分类线

```

分类线效果很不好 2.2 网络训练

```
net.adaptParam.passes=30;      %在训练过程中重复次数为30
net=adapt(net,P,T);
net.IW{1,1}
net.b{1}
plotpc(net.IW{1},net.b{1})

```

训练30次后，效果不是很理想

```
net.adaptParam.passes=60;

```

训练60次后，效果比较理想 可以看到三次变化。 3.仿真

```
figure(2);
p=[19;5];
a=sim(net,p);
plotpv(p,a);
hold on;
plotpv(P,T);

plotpc(net.IW{1},net.b{1});

```

## 三、详细设计(完整代码）

```
%测试上课是否迟到
%读取训练数据
[f1,f2,class] = textread('test/trainData.txt' , '%f%f%f',10);
P=[f1 f2];
T=[class];
P=P';
T=T';
disp(P);
disp(T);



net=newp([-1 1;-1 1],1);
plotpc(net.IW{1,1},net.b{1})  %%画分类线
plotpv(P,T);                % plotpv函数利用感知器的输入向量和目标向量来画输入向量的图像
net=adapt(net,P,T);  %利用输入样本调节神经网net 
net.IW{1,1}
net.b{1}
plotpc(net.IW{1,1},net.b{1})  %重新画分类线
net.adaptParam.passes=30;      %在训练过程中重复次数为30
net=adapt(net,P,T);
net.IW{1,1}
net.b{1}
plotpc(net.IW{1},net.b{1})
net.adaptParam.passes=60;
net=adapt(net,P,T);
net.IW{1,1}
net.b{1}
figure(1);
plotpc(net.IW{1},net.b{1})
%仿真
%a=sim(net,p);
%plotpv(p,a)
figure(2);
p=[19;5];
a=sim(net,p);
plotpv(p,a);
hold on;
plotpv(P,T);

plotpc(net.IW{1},net.b{1});

%感知器能够正确分类，从而网络可行

```

## 四、实验结果总结

测试数据：

<img src="https://img-blog.csdnimg.cn/20190226171855693.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **数据解释：** 第一项为距离点名所剩的时间； 第二项为当前距离上课地点的路程； 假设一个时间单位可以走完一个路程单位的路程。 第三项为标记，0代表成功点名，1代表点名失败（迟到）。 <img src="https://img-blog.csdnimg.cn/2019022617191256.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> p=[19;5]; 点名成功 <img src="https://img-blog.csdnimg.cn/2019022617192763." alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20190226171943944.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> p=[10;25]; 点名失败。 <img src="https://img-blog.csdnimg.cn/20190226172000819." alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190226172015834.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

## 总体实验总结

在开始时我对与神经网络的工具包不是很了解，于是先到网上取查阅相关资料，进行初步了解，然后才初步运行分析实验。 在做第一个小实验的时候，我曾尝试做出苹果和梨子的差别，但是实验效果不理想，在从图片中提取像素时我曾采取了很多办法，最后才采用上述的方法，实验也修改为水果的生和熟。因为我发现梨子的黄色好像会归为红色素的提取，直接取像素的大小也只能得到图片的灰度，导致图片中的黄色与红色不能很好的区别，所以换来比较简单的，苹果和梨的问题我会再思考有什么其他的解决方法。 第二个小实验进行时，再开始时遇到不少的小错误，主要还是我对调用的函数理解不深的原因，比如出现了索引超过了矩阵长度的问题，后来才发现是flag的大小有问题，应为[0 1],而我不小心写成了[1 2]；开始无法正确的显示分类线，后来发现是我的测试数据的值不够多，但是数值大小又写的太过相近导致。

通过这次实验，我学到的很多，也明白自己经验不足，有不少知识盲点，以后会继续学习的。

## 附录：

实验主要是用到了**Matlab工具包**，下面粗略介绍： Neural Network Toolbox为各种复杂的非线性系统的建模提供多种函数和应用程序。该工具箱提供各种监督学习模型：前向反馈，径向基核函数和动态网络等模型。同时也提供自组织图和竞争层结构（competitive layers）的非监督学习模型。该工具箱具有设计、训练、可视化与仿真神经网络的功能。基于该工具箱可以进行数据拟合、模式识别、分类和时间序列预测及其动态系统的建模和控制。
1.  网络创建函数 newp 创建感知器网络 1.  网络应用函数 sim 仿真一个神经网络 init 初始化一个神经网络 adapt 神经网络的自适应化 train 训练一个神经网络 1.  学习函数 learnp 感知器学习函数 1.  绘图函数 plotec 用于显示最后出来的分类线 plotev 用于显示感知器(绘制点) 
神经网络训练参数解释 1．训练参数.trainParam

```
trainParam.goal=0.1                 % 训练目标最小误差，这里设置为0.1
trainParam.epochs=300;             % 训练次数，这里设置为300次
trainParam.show=20;            % 现实频率，这里设置为没训练20次显示一次
trainParam.mc=0.95;                    % 附加动量因子
trainParam.lr=0.05;                       % 学习速率，这里设置为0.05
trainParam.min_grad=1e-6;        % 最小性能梯度
trainParam.min_fail=5;                 % 最大确认失败次数

```

2．设置网络的训练参数

```
net.trainParam.epochs―最大收敛次数；
net.trainParam.goal―收敛误差；
net.trainParam.show―显示间隔；

```

3．权值/阈值

```
net.iw                 
% 权值元包：net.iw{1}——当网络只有一层时，net.iw是一个1x1的cell；
%net.iw{1,1}——当网络有多层时，net.iw是一个元包矩阵。

net.b                                % 阈值/偏置值，也是一个元包

```

## 代码下载：

**注意，代码下载后仍需自行调试~** 积分值为5（如果有变为csdn自行修改）——完整代码其实和上面贴出的差别不大，酌情下载~ https://download.csdn.net/download/zxm_jimin/10977018

**感谢各位大佬看到最后~** **本文为原创。转载请注明出处。 注：原理部分，参考了一些文章，博客，如有侵权请联系，我附上原出处。**
