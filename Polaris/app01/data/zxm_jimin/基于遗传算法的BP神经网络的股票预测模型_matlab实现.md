
--- 
title:  基于遗传算法的BP神经网络的股票预测模型_matlab实现 
tags: []
categories: [] 

---


#### 文章目录
- - - - - 


## 摘要

在目前的股票投资市场，不少自然人股民的投资主要方式使根据对当天或者一个较长周期对股票数据的预测，来得到下一天的股票数据，从而进行相应的投资。为了满足股民希望能更为理性合理准确的预测股票走向，需要借助机器的帮助。本文主要是利用优化过的遗传算法，利用遗传算法调整BP三层神经网络的权重与阈值，使BP神经网络的训练效果得到提升，从而对股票市场的行情有比较好的预测效果。

**关键词** BP神经网络 遗传算法 特征选取

**实验论文节选**

## bp神经网络

<img src="https://img-blog.csdnimg.cn/20190226153010527.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="bp神经网络">

## 遗传算法

<img src="https://img-blog.csdnimg.cn/20190226153110875.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="遗传算法">

遗传算法的过程： <img src="https://img-blog.csdnimg.cn/20190226153908663.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190226153924744.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2019022615400833.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190226154031602.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190226154100188.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190226154135660.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2019022615421150.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

## 实验结果与分析

3.1 实验设置 3.1.1 股票数据库的选择 本实验使用了两种股票种类，为某单支股票（150个）数据与上证综合指数前复权日线（533个）数据，分别保存在两个文件中，将两个数据集的特征向量人工设定为同一列位置，方便后续实验。

3.1.2 实验参数设置 本次实验在Matlab环境上运行，分析给予遗传算法的BP神经网络与随机初始化的BP神经网络在股票预测上的差距。 本次实验所采用的为BP神经网络：训练次数epochs为1000，训练目标goal为0.01，学习速率lr为0.1；遗传算法：群体规模为N=60。

3.2 实验结果与分析 **实验1：测试未优化的遗传算法运行的预测效果** 本次实验，隐含层神经元个数为3，交叉概率为p_c=0.8，变异概率为p_m=0.05，交叉位置为15L到20L。迭代次数分别设为10次，50次，100次，比较区别。 <img src="https://img-blog.csdnimg.cn/20190226155218810.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt=""> <img src="https://img-blog.csdnimg.cn/20190226155250155.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 本次测试出的每一代的最小误差波动很大，而且随着迭代次数的增加，最新一带的最小误差没有明显减小，达不到预期效果。

**实验2：测试带指标变异操作的遗传算法优化的预测效果** 本次实验，隐含层神经元个数为3，群体规模为N=60，交叉概率为p_c=0.8，变异概率为p_m=0.05，双点交叉，交叉位置为15L到20L。迭代次数分别设为10次，50次，100次，比较区别。 <img src="https://img-blog.csdnimg.cn/2019022615530769.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190226155322702.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 本次测试出的每一代的最小误差虽然波动很大，但是可以看出随着迭代次数的增加，最后一代的最小误差有下降的趋势，但是容易陷入局部最优解，可能使由于参数设置的问题。

**实验3：测试优劣同时保留的遗传算法优化的预测效果** 本次实验，隐含层神经元个数为3，群体规模为N=60，交叉概率为p_c=0.8，变异概率为p_m=0.05，交叉位置为15L到20L。迭代次数分别设为10次，50次，100次，比较区别。 <img src="https://img-blog.csdnimg.cn/20190226155351674.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190226155405653.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 本次测试出的每一代的最小误差虽然还是有波动，但是较前两个实验，已经是降低的趋势了，最优误差也是下降的趋势，说明此优化可以帮助算法跳出局部最差解，逼近局部最优解。

**实验4：测试大变异值的自适应的遗传算法优化的预测效果** 本次实验，隐含层神经元个数为3，群体规模为N=60，交叉概率为p_c=0.8，交叉位置为15L到20L。迭代次数分别设为10次，50次，100次，比较区别。 <img src="https://img-blog.csdnimg.cn/20190226155431410.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190226155444508.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 本次测试出的每一代的最小误差波动相较前几个实验，波动十分巨大，但是产生当前最优解的个数是最大的，说明可以帮助算法跳出局部最优解。

**实验5：遗传算法不同参数的遗传算法优化的预测效果** <img src="https://img-blog.csdnimg.cn/20190226155520730.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt=""> 可以看出，虽然最终的最终误差相差很小，但是种群个数为100的遗传算法明显要比种群个数为60的遗传算法收敛效果要好，相应的，算法的运行时间也有所增加。

**实验6：BP神经网络算法不同参数的预测效果** <img src="https://img-blog.csdnimg.cn/2019022615554128." alt="在这里插入图片描述"> 可以看出，隐含层神经元个数为3个时，BP神经网络的预测效果更好。

股票预测模型实验结果对比：实验结果选取证综合指数前复权日线数据的总预测曲线。 <img src="https://img-blog.csdnimg.cn/20190226155623642.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190226155855198." alt="在这里插入图片描述">图1 普通BP神经网络的预测效果 图1中，绿色线为股票真实值。可以看出，进行4次的普通BP神经网络算法的预测，预测效果十分不稳定。

<img src="https://img-blog.csdnimg.cn/2019022615584290.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 图2 优化BP神经网络的预测效果 图2中，绿色线为股票真实值，红色线为带指标变异操作的遗传算法优化后的BP神经网络的预测值，蓝色线为优劣同时保留的遗传算法优化后的BP神经网络的预测值，黑色线为普通遗传算法优化后的BP神经网络的预测值，紫色线为大变异值的自适应的遗传算法优化后的BP神经网络的预测值。可以看出，这四次实验的预测效果比普通BP神经网络算法的预测效果稳定很多，也更为准确。

<img src="https://img-blog.csdnimg.cn/20190226155829156.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190226155740179.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">图3 优化BP神经网络的预测效果（放大节选） 从图3中，可以看出，预测效果的最好的是优劣同时保留的遗传算法优化后的BP神经网络，其次是带指标变异操作的遗传算法优化后的BP神经网络，然后是普通遗传算法优化后的BP神经网络，最差的是大变异值的自适应的遗传算法优化后的BP神经网络。

针对以上实验，可以得知，在遗传算法的优化下BP神经网络的预测值明显比未优化的普通BP神经网络的预测值更为准确和稳定。更进一步对遗传算法进行优化，优化的关键点在于遗传算法的选择、交叉、变异三大操作，优化后预测的准确度也有了进一步的提升

**参考到的资料**： https://download.csdn.net/download/u010667861/9617803 [1] 史峰，王辉，郁磊，胡斐. MATLAB智能算法30个案例分析——基于遗传算法的BP神经网络优化算法[M]. 北京航空航天大学出版社，2011：27-37. [2] 翁苏骏. 遗传算法改进的新思路及其在股市投资中的应用[D]. 厦门：厦门大学，1999.

## 完整代码下载：

**注意，代码下载后仍需自行调试~** **有调试能力的人再下载，问关于代码问题的不会回复，应该每个人环境不同，会出现各种问题，需要大家自己解决！！！** 积分值为5（如果有变为csdn自行修改） **更新下载地址（抱歉这么久）** https://download.csdn.net/download/zxm_jimin/25625013

本文为原创，转载请注明出处。
