
--- 
title:  Python口罩识别检测全网最全OpenCV训练分类器具体步骤（以训练口罩检测分类器为例）附分类器和数据集下载地址 
tags: []
categories: [] 

---
 https://blog.csdn.net/meenr/article/details/115825671

## OpenCV训练口罩检测分类器

### Python版本

**训练好的口罩检测分类器和正负样本数据集在本文。** 

#### 目录
- - <ul><li>- - - - - <ul><li>- - - - - - - - <ul><li>- - - - - - <ul><li>- - 


## 1. 概述

本文系统全面的总结了用OpenCV训练分类器的方法和步骤，案例是在Python环境下训练口罩识别分类器。作者能力有限，本文仅供参考，如有错误之处，恳请留言指出。

## 2. 数据收集

### 2.1 正样本

正样本是戴口罩的人脸数据，尽量包含少的背景，案例是1100张，文件夹命名为have。 <img src="https://img-blog.csdnimg.cn/2021041918304974.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

### 2.2 负样本

负样本是不戴口罩的人脸数据或者其他数据，但不能包含正样本，尽可能多的提供场景的背景图且要多样化。 <img src="https://img-blog.csdnimg.cn/20210419183107287.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

案例是3420张，正负样本推荐比例在1:3左右时效果最理想。文件夹命名为no。 <img src="https://img-blog.csdnimg.cn/20210419183123317.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 数据存放路径无中文字符，have和no的外层文件夹命名为mask。

## 3. 资料获取

如果您需要训练好的分类器或者需要正负样本数据集的读者可通过下面方式获取：

2贰进制社区“ **480558240** ”，下载群文件或者联系管理员咨询。 <img src="https://img-blog.csdnimg.cn/2020071217121655.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="10" height="10"> “ **2贰进制** ”，回复对应的关键词，“口罩数据集”，“口罩分类器”。 <img src="https://img-blog.csdnimg.cn/2020070300554991.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="二维码" width="00" height="00">

## 4. 数据预处理

### 4.1 文件归一化

统一图片类型为jpg格式，批量重命名文件名，以便于迭代。正负样本都需要修改，正负样本分别执行下面代码，在代码中修改对应的路径和样本个数即可。

```
# 代码略


```

### 4.2 图像处理

#### 4.2.1 灰度处理

新建have1和no1两个文件夹用来存放灰度处理后的图像。

正负样本都需要转成灰度图像。根据实际情况将下面代码修改正负样本读路径、转换后的灰度图像写路径以及迭代次数（即样本个数），分别对正负样本进行处理。 灰度处理前路径是have和no，处理后路径是have1和no1。 <img src="https://img-blog.csdnimg.cn/20210419183249672.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

```
# 代码略


```

如果新旧地址一致，则进行覆盖操作，建议先备份原数据文件。

#### 4.2.2 像素处理

本文先用了默认的Haar特征来训练（LBP特征阅读第7节），需要将正样本像素统一为成20×20； LBP特征要统一为24×24大小。负样本对尺寸没有统一要求，在训练对应的分类器时，选择的负样本尺寸一定要大于等于正样本规定的尺寸。

新建classifier文件夹，在该文件中新建have_mask和no_mask两个文件夹。 <img src="https://img-blog.csdnimg.cn/20210419183321113.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 在灰度图像基础上对正负样本像素裁剪，案例正样本像素推荐20×20，负样本像素推荐80×80。代码需要修改迭代次数以及读写路径（读写路径是同一个，即覆盖操作）。

正样本像素处理代码：

```
# 代码略


```

负样本像素处理代码：

```
# 代码略


```

预处理结束分别得到正负样本文件格式和像素统一的灰度图像数据，分别存放在have_mask和no_mask文件夹中。

## 5. 训练前准备

### 5.1 安装OpenCV

安装包链接：，提取码：8lty

下载完成后，双击运行，按照提示进行安装，记住安装路径。

### 5.2 拷贝文件

将OpenCV安装路径“opencv\build\x64\vc14\bin”下的opencv_createsamples.exe、opencv_traincascade.exe两个.exe可执行文件和另外两个.dll文件（见下图），复制到classifier文件夹中与数据同级目录。 <img src="https://img-blog.csdnimg.cn/20210419183415505.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

### 5.3 创建xml文件夹

在正负样本同级目录创建新的文件夹命名为xml，用于存放训练好的xml文件。 <img src="https://img-blog.csdnimg.cn/20210419183427514.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

### 5.4 生成样本路径txt文件

**第一步**： win+R 打开运行窗口，输入 cmd 回车进入命令提示符窗口，用 cd 命令进入have_mask（no_mask）文件夹。 <img src="https://img-blog.csdnimg.cn/20210419183437445.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

```
D:

cd D:\\classifier\\have_mask

```

**第二步**：输入以下命令，回车执行。

```
dir /b/s/p/w \*.jpg \&gt; have_mask.txt

```

<img src="https://img-blog.csdnimg.cn/20210419183506972.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

**第三步**：负样本同前两步处理，注意修改have_mask为no_mask。

<img src="https://img-blog.csdnimg.cn/20210419183515854.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> **第四步**：将生成的have_mask.txt和no_mask.txt文件，剪切到classifier文件夹中。 <img src="https://img-blog.csdnimg.cn/20210419183526733.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

### 5.5 补写生成的txt文件

**第一步**：在另一个文件夹中备份have_mask.txt和no_mask.txt文件，稍后还将使用这两个文件。

<img src="https://img-blog.csdnimg.cn/20210419183540327.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> **第二步**：样本需要生成 .vec格式的描述文件，在此之前需要对txt文档进行预处理，向have_mask.txt文件中末尾加入： 1 0 0 20 20，向no_mask.txt文件中末尾加入： 1 0 0 80 80。

补写后缀含义：1：文件，0 0即坐标(0,0)，20 20即坐标(20,20)，根据坐标从左下角扫描到右上角。 <img src="https://img-blog.csdnimg.cn/20210419183712286.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 打开have_mask.txt文件利用记事本的查找替换功能将 jpg 替换为 jpg 1 0 0 20 20，no_mask.txt文件同理。若用此方法可跳过第三步

### 5.6 生成样本描述文件

#### 5.6.1 正样本描述文件

**第一步**：cd 命令进入classifier文件夹中

**第二步**：输入一下命令，注意命令中的num后面的数字是正样本数量，按实际修改。回车执行后将生成havemask.vec文件。

vec：样本描述文件名和路径

info：样本说明文件

num：样本个数，正样本为1100个样本

w h：样本尺寸，正样本为20×20

```
opencv_createsamples.exe -vec havemask.vec -info have_mask.txt -num 1100 -w 20 -h 20

```

<img src="https://img-blog.csdnimg.cn/20210419183847509.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

#### 5.6.2 负样本描述文件

将第二步命令修改为如下内容即可。回车执行后将生成nomask.vec文件。

```
opencv_createsamples.exe -vec nomask.vec -info no_mask.txt -num 3420 -w 80 -h 80

```

<img src="https://img-blog.csdnimg.cn/20210419183902168.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/20210419183910821.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

## 6. 开始训练

### 6.1 替换txt文件

将在4.5节中备份的have_mask.txt和no_mask.txt文件复制到classifier文件夹中，替换掉有后缀的txt文件。

### 6.2 新建traincascade.bat文件

在classifier文件夹中创建一个新的.txt文件，写入以下内容：

```
opencv_traincascade.exe -data xml -vec havemask.vec -bg no_mask.txt -numPos 500 -numNeg 1000 -numStages 30 -w 20 -h 20 -mode ALL

pause

```

将该txt文件命名为：traincascade.bat，后缀是.bat。

<img src="https://img-blog.csdnimg.cn/20210419183923787.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

指令各参数含义：

-data xml：指定存放训练好的分类器的路径名，也就是前文的xml文件夹；

-vec havemask.vec：正样本文件名；

-bg no_mask.txt：背景描述文件；

-numPos 500：取500个正样本，小于正样本总数，否则会报错；

-numNeg 1000：取1000个负样本，小于负样本总数，否则会报错；

-numStages 30：指定训练层数为30层，层数越高耗时越长，根据需求自行调整；

-w 20：样本宽度，20；

-h 20：样本高度，20；

下面四个参数可选可不选。

-mem 2048：提供的以MB为单位的内存，值越大，提供的内存越多，运算也越快，根据实际电脑内存情况自行调整选择，案例是2048MB。

-minHitRate 0.999：分类器的每一级希望得到的最小检测率。设置最小检测率为0.999。

-maxFalseAlarmRate 0.4：分类器的每一级希望得到的最大误检率。设置最大误检率为0.4。

-nsplits 2：分裂子节点数目，默认值为2(该参数不建议使用修改)。

### 6.3 开始训练

双击打开运行traincascade.bat文件，开始训练，最后是漫长的等待训练结束。

<img src="https://img-blog.csdnimg.cn/20210419183936121.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 训练过程各参数含义：

N：层数

SMP：样本的使用率

F：+表示通过翻转，否则是-

ST.THR：分类器的阈值

HR：当前分类器对正样本识别正确的概率

FA：当前分类器对负样本识别错误的概率

EXP.ERR：分类器的期望错误率

<img src="https://img-blog.csdnimg.cn/20210419183948997.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 当 opencv_traincascade 程序训练结束以后，训练好的级联分类器将存储于文件 cascade.xml 中，这个文件位于-data指定的目录中即xml文件夹。这个目录中的其他文件是训练的中间结果，当训练程序被中断后，再重新运行训练程序将读入之前的训练结果，而不需从头重新训练。训练结束后，可以删除这些中间文件，只保留 cascade.xml 即可。 <img src="https://img-blog.csdnimg.cn/20210419183958228.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

### 6.4 常见错误处理

#### 6.4.1 参数等于样本总数

-npos ，-neg 两个参数若直接与正负样本总数相同，则在训练过程中会出现错误：训练中途，程序突然终止，提示： “OpenCV Error: Assertion failed (elements_read == 1) in icvGetHaarTraininDataFromVecCallback,file…\…\…\opencv\apps\haartraining\cvhaartraining.cpp, line 1861”。

-npos的意思是每次训练从.vec文件中随机选取npos个正样本。由于存在虚警，在每一次训练一个强分类器之后，会把那些分类错误的从整个样本库中剔除掉，总的样本就剩下 CountVec = CountVec - （1 - minhitrate）**npos，在第二个强分类器的训练过程中就是从剩下的Countvec抽样，一直这样进行nstage次，所以就有CountVec&gt;= (npos + (nstages - 1)**(1 -minhitrate) * npos ) + nneg。当把npos设置与vec中总样本数相同时，第二个强分类器训练时，必然就会报错，提示样本数不足，将取值改小即可。

#### 6.4.2 训练卡住长时间不更新

可能是负样本数量不足或者负样本不具有多样性造成的。利用ctrl+c指令中断重新进行训练增加负样本的数目及多样性。可以生成分辨率不同的分类器这样子分类器就会具有尺度不变性。

## 7. 测试

通过下面python代码测试训练得到的分类器检测效果。导入cv2，需要先安装opencv-python库，人脸检测的opencv官方分类器文件在：opencv安装目录\sources\data\haarcascades中可调用。

```
import cv2


# opencv自带人脸识别人分类器
face_detector = cv2.CascadeClassifier('OpenCV_xml\\haarcascade_frontalface_default.xml')
# 训练好的口罩检测分类器
mask_detector = cv2.CascadeClassifier('D:\\classifier\\xml\\cascade.xml')
video = cv2.VideoCapture(0)
while True:
	# 读取摄像头
    flag, img = video.read()
    # 转灰度
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.05, 3)
    for (x1, y1, w1, h1) in faces:
        face = img[y1:y + h, x1:x + w]  # 裁剪坐标
        mask_face = mask_detector.detectMultiScale(gray, 1.1, 4)
        for (x2, y2, w2, h2) in mask_face:
        	# 画矩形框
            cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 255), 2)
            pass
 		pass
    cv2.imshow('mask', img)
    cv2.waitKey(5)
    pass
cap.release()
cv2.destroyAllWindows()

```

## 8. 扩展比较

前文训练基于Haar算法的特征，下面介绍用另一种算法——LBP特征来训练分类器，HOG特征同理。

**第一步**：另新建文件夹用来保存重新调整像素后的正负样本，LBP特征需要修改正样本像素值为24×24，之后重复之后操作到5.2节过程中各步骤都需要修改宽高值为24×24，负样本可不做修改。

**第二步**：修改5.2节traincascade.bat文件中的命令为如下内容：

```
opencv_traincascade.exe -data xml -vec havemask.vec -bg no_mask.txt -numPos 500 -numNeg 1000 -numStages 30 -featureType LBP -mem 2048 -w 24 -h 24 -mode ALL

pause

```

新增以下指令：

-featureType LBP：特征类型设置为LBP - 局部纹理模式特征，另外宽高值也必须修改。

附录

官方训练参数含义描述：

下面是 opencv_traincascade 的命令行参数，以用途分组介绍：

1、通用参数：

-data &lt;cascade_dir_name&gt;，目录名，如不存在训练程序会创建它，用于存放训练好的分类器。

-vec &lt;vec_file_name&gt;，包含正样本的vec文件名（由 opencv_createsamples 程序生成）。

-bg &lt;background_file_name&gt;，背景描述文件，也就是包含负样本文件名的那个描述文件。

-numPos &lt;number_of_positive_samples&gt;，每级分类器训练时所用的正样本数目。

-numNeg &lt;number_of_negative_samples&gt;，每级分类器训练时所用的负样本数目，可以大于 -bg 指定的图片数目。

-numStages &lt;number_of_stages&gt;，训练的分类器的级数。

-precalcValBufSize &lt;precalculated_vals_buffer_size_in_Mb&gt;，缓存大小，用于存储预先计算的特征值(featurevalues)，单位为MB，默认值是256MB。

-precalcIdxBufSize &lt;precalculated_idxs_buffer_size_in_Mb&gt;，缓存大小，用于存储预先计算的特征索引(feature indices)，单位为MB，默认值是256MB。内存越大，训练时间越短。 -baseFormatSave，这个参数仅在使用Haar特征时有效。如果指定这个参数，那么级联分类器将以老的格式存储。

2、级联参数：

-stageType &lt;BOOST(default)&gt;，级别（stage）参数。目前只支持将BOOST分类器作为级别的类型。

-featureType &lt;{HAAR(default), LBP,HOG}&gt;，特征的类型： HAAR - 类Haar特征； LBP - 局部纹理模式特征； HOG - 方向梯度直方图特征，默认值是HAAR。

-w &lt;sampleWidth&gt; -h &lt;sampleHeight&gt;，训练样本的尺寸（单位为像素）。必须跟训练样本创建（使用 opencv_createsamples 程序创建）时的尺寸保持一致。

3、Boosted分类器参数：

-bt &lt;{DAB, RAB, LB, GAB(default)}&gt;，Boosted分类器的类型： DAB - Discrete AdaBoost, RAB - Real AdaBoost, LB - LogitBoost, GAB - Gentle AdaBoost。

-minHitRate &lt;min_hit_rate&gt;，分类器的每一级希望得到的最小检测率。总的检测率大约为min_hit_rate^number_of_stages。

-maxFalseAlarmRate &lt;max_false_alarm_rate&gt;，分类器的每一级希望得到的最大误检率。

总的误检率大约为 max_false_alarm_rate^number_of_stages.

-weightTrimRate &lt;weight_trim_rate&gt;，Specifies whether trimming should be used and its weight. 一个还不错的数值是0.95。

-maxDepth &lt;max_depth_of_weak_tree&gt;，弱分类器树最大的深度。一个还不错的数值是1，是二叉树（stumps）。

-maxWeakCount &lt;max_weak_tree_count&gt;，每一级中的弱分类器的最大数目。The boosted classifier (stage) will have so many weak trees (&lt;=maxWeakCount), as needed to achieve the given -maxFalseAlarmRate.

4、类Haar特征参数：

-mode &lt;BASIC (default) | CORE | ALL&gt;，选择训练过程中使用的Haar特征的类型。 BASIC 只使用右上特征， ALL 使用所有右上特征和45度旋转特征。更多细节请参考 [Rainer2002] 。 5、LBP特征参数： LBP特征无参数。

## 文末

### **2贰进制–Echo 2021年3月**

资源获取见2贰进制 如果您觉得本文还不错，请点赞＋评论＋收藏+关注 <img src="https://img-blog.csdnimg.cn/20210424133535613.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="00" height="00">

感谢您的阅读、点赞、评论、收藏与打赏。

**参考地址：**




