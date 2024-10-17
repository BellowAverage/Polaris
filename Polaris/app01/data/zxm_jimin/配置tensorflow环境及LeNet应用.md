
--- 
title:  配置tensorflow环境及LeNet应用 
tags: []
categories: [] 

---
**1、配置环境**： 安装tensorflow主要参考：https://blog.csdn.net/lxy_2011/article/details/79181990

**问题一**：python出现This application failed to stat could not find or load the Qt platform plugin “windows” 问题解决：参考https://blog.csdn.net/qq_36523839/article/details/80495746?utm_source=blogxgwz2

压缩包： <img src="https://img-blog.csdnimg.cn/20190226191131512." alt="在这里插入图片描述"> 解压为： <img src="https://img-blog.csdnimg.cn/20190226191103207.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190226191051685.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **问题二：** 测试代码： import tensorflow as tf hello=tf.constant(“Hello,TensorFlow!”) sess=tf.Session() print(sess.run(hello))

错误：Segmentation fault (core dumped) 原因：编译错误，代码问题 <img src="https://img-blog.csdnimg.cn/20190226191036872.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/201902261910235.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/2019022619095758.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190226190942487.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 输入activate tensorflow，导入import tensorflow as tf，检查Python版本

尝试了无数方法，放弃了spyder打开 比如： https://blog.csdn.net/zsg2063/article/details/72983533?utm_source=itdadao&amp;utm_medium=referral https://blog.csdn.net/weixin_38533896/article/details/80255808 https://blog.csdn.net/u011361880/article/details/76572973

等。

后觉得在PyCharm集成环境下运行： 参考：https://blog.csdn.net/ljp812184246/article/details/52593024 配置python.exe <img src="https://img-blog.csdnimg.cn/20190226190912800.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 成功运行： <img src="https://img-blog.csdnimg.cn/20190226190848960.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

**2、Minst数据集下载** 参考： https://blog.csdn.net/qq_23096723/article/details/80982295 问题一： Input_data.py <img src="https://img-blog.csdnimg.cn/20190226190830866.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 后发现是数据集太大，电脑无法运行。 切换成只有两个数据集，可以加载数据集。 <img src="https://img-blog.csdnimg.cn/20190226190814408.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

**3、LeNet代码调试** 运行代码： （主要参考） https://blog.csdn.net/u012679707/article/details/80365599?utm_source=blogxgwz4 （补充） https://blog.csdn.net/puredreammer/article/details/78395808?utm_source=blogxgwz3

运行代码（下有详细注释）：

```
# !/usr/bin/env python
# _*_ coding: utf-8 _*_

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# 定义神经网络模型的评估部分
def compute_accuracy(test_xs, test_ys):
    # 使用全局变量prediction
    global prediction
    # 获得预测值y_pre
    y_pre = sess.run(prediction, feed_dict={xs: test_xs, keep_prob: 1})
    # 判断预测值y和真实值y_中最大数的索引是否一致，y_pre的值为1-10概率, 返回值为bool序列
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(test_ys, 1))
    # 定义准确率的计算
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))  # tf.cast将bool转换为float32
    # 计算准确率
    result = sess.run(accuracy)
    return result


# 下载mnist数据
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)


# 权重参数初始化
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)  # 截断的正态分布，标准差stddev
    return tf.Variable(initial)


# 偏置参数初始化
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


# 定义卷积层
def conv2d(x, W):
    # stride的四个参数：[batch, height, width, channels], [batch_size, image_rows, image_cols, number_of_colors]
    # height, width就是图像的高度和宽度，batch和channels在卷积层中通常设为1
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

# SAME表示输入和输出是同一尺寸
# 对于图片，因为只有两维，通常strides取[1，stride，stride，1]

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    """
    
#ksize是池化窗口的大小，strides是池化过程的步长

    max_pool(x,ksize,strides,padding)参数含义
        x:input
        ksize:filter，滤波器大小2*2
        strides:步长，2*2，表示filter窗口每次水平移动2格，每次垂直移动2格
        padding:填充方式，补零
    conv2d(x,W,strides=[1,1,1,1],padding='SAME')参数含义与上述类似
        x:input
        W:filter，滤波器大小
        strides:步长，1*1，表示filter窗口每次水平移动1格，每次垂直移动1格
        padding:填充方式，补零('SAME')
    """


# 输入输出数据的placeholder
xs = tf.placeholder(tf.float32, [None, 784])
ys = tf.placeholder(tf.float32, [None, 10])
# dropout的比例
keep_prob = tf.placeholder(tf.float32)

# 对数据进行重新排列，形成图像

# reshape中的-1表示-1代表的含义是不用我们自己指定这一维的大小，
# 函数会自动计算，但列表中只能存在一个-1,
# 其第2、第3维对应图片的宽、高，最后一维代表图片的颜色通道数

x_image = tf.reshape(xs, [-1, 28, 28, 1])  # -1, 28, 28, 1

print(x_image.shape)

# 卷积层一
# patch为5*5，in_size为1，即图像的厚度，如果是彩色，则为3，32是out_size，输出的大小-》32个卷积和（滤波器）
# 第一层卷积 前两个维度是patch的大小，接着是输入的通道数目，最后是输出的通道数目
W_conv1 = weight_variable([5, 5, 1, 32])
# 第一层卷积核的偏置项
b_conv1 = bias_variable([32])
# ReLU操作，输出大小为28*28*32
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
# Pooling操作，输出大小为14*14*32
h_pool1 = max_pool_2x2(h_conv1)

# 卷积层二
# patch为5*5，in_size为32，即图像的厚度，64是out_size，输出的大小
# 第二层卷积层 因为第一层输出的通道数目是32 故第二层输入的通道数目也应该为32

W_conv2 = weight_variable([5, 5, 32, 64])
# 这里的64是自己给定的,可以为其他的值

b_conv2 = bias_variable([64])
# ReLU操作，输出大小为14*14*64
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
# Pooling操作，输出大小为7*7*64
h_pool2 = max_pool_2x2(h_conv2)

# 全连接层一
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])
# 输入数据变换
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])  # 整形成m*n,列n为7*7*64
# 进行全连接操作
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)  # tf.matmul
# 防止过拟合，dropout
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 全连接层二
# 全连接层,假设全连接层的个数为1024，当然也可以设置成其他值
# 两次池化后尺寸由28*28 -&gt; 14*14 -&gt;7*7
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
# 预测
prediction = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

# 计算loss
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))
# 神经网络训练
train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)  # 0.0001

# 定义Session
sess = tf.Session()
init = tf.global_variables_initializer()
# 执行初始化
sess.run(init)

# 进行训练迭代
for i in range(1000):
    # 取出mnist数据集中的100个数据
    batch_xs, batch_ys = mnist.train.next_batch(50)  # 100
    # 执行训练过程并传入真实数据
    sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 0.5})
    if i % 100 == 0:
        print(compute_accuracy(mnist.test.images, mnist.test.labels))

4、理解代码：
# 定义Session
sess = tf.Session()
init = tf.global_variables_initializer()
# 执行初始化
sess.run(init)

```

<img src="https://img-blog.csdnimg.cn/20190226190711129.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20190226190657711.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 了解tensorflow中神经网络的基础概念： 参考： https://blog.csdn.net/wwwdc1012/article/details/76641229

卷积神经网络的深入了解： https://blog.csdn.net/yunpiao123456/article/details/52437794?utm_source=blogxgwz0

## ReLU操作，输出大小为28**28**32

h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1) <img src="https://img-blog.csdnimg.cn/20190226191531941.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 运行结果：训练运行大概要十分钟 <img src="https://img-blog.csdnimg.cn/20190226190604413.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

运行结果（节选）： Extracting MNIST_data\train-images-idx3-ubyte.gz Successfully downloaded train-labels-idx1-ubyte.gz 28881 bytes. Extracting MNIST_data\train-labels-idx1-ubyte.gz Extracting MNIST_data\t10k-images-idx3-ubyte.gz Extracting MNIST_data\t10k-labels-idx1-ubyte.gz (?, 28, 28, 1) print(x_image.shape) 2018-10-27 11:02:05.726650: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 2018-10-27 11:02:07.329384: W tensorflow/core/framework/allocator.cc:113] Allocation of 1003520000 exceeds 10% of system memory. 2018-10-27 11:02:13.489113: W tensorflow/core/framework/allocator.cc:113] Allocation of 250880000 exceeds 10% of system memory. 2018-10-27 11:02:14.063240: W tensorflow/core/framework/allocator.cc:113] Allocation of 501760000 exceeds 10% of system memory. 2018-10-27 11:03:27.435921: W tensorflow/core/framework/allocator.cc:113] Allocation of 125440000 exceeds 10% of system memory. 0.1871 2018-10-27 11:03:52.014847: W tensorflow/core/framework/allocator.cc:113] Allocation of 1003520000 exceeds 10% of system memory. 0.9532 print( compute_accuracy(mnist.test.images, mnist.test.labels) ) 0.967 0.9697 0.9721 0.9801 0.9792 0.9819 0.9845 0.9833

Process finished with exit code 0

分析： 训练网络后，测试时准确率可以达到0.9833，达到目标。

实验总结： 在开始时，安装tensorflow并没有遇到很多问题，遇到一些小问题在百度的帮助下也可以解决。 在使用tensorflow框架时，我发现不少问题，有许多错误（比如无法打开spyder(tensorflow),但是可以打开spyder(python2.7)），实际上就是无法正确的打开tensorflow中之前配置好的python3.5（python.exe）,具体原因不清（我认为可能是和我电脑上之前配置的起冲突，或者是和tensorflow 自带的python2.7起冲突）,最后我使用PyCharm，配置tensorflow中之前配置好的python3.5（python.exe），可以正常运行。 后来调程序时也遇到不少问题，比如代码看不太懂，原理理解不清晰，在查阅了网上的资料后，我在源码上jia一些注释，帮助我理解。
