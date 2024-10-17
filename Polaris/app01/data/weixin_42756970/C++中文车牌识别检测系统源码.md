
--- 
title:  C++中文车牌识别检测系统源码 
tags: []
categories: [] 

---
下载地址：

其目标是成为一个简单、高效、准确的非限制场景(unconstrained situation)下的车牌识别库。

相比于其他的车牌识别系统，EasyPR有如下特点：
- 它基于openCV这个开源库。这意味着你可以获取全部源代码，并且移植到opencv支持的所有平台。- 它能够识别中文。例如车牌为苏EUK722的图片，它可以准确地输出std:string类型的"苏EUK722"的结果。- 它的识别率较高。图片清晰情况下，车牌检测与字符识别可以达到80%以上的精度。
#### 更新

本次更新版本是1.6正式版本，主要有以下几点更新：
1.  修正了多项readme的文本提示。 1.  增加了C#调用EasyPR的一个项目的链接，感谢 @zhang-can 同学。 
**注意**
1.  对于Opencv3.2或以上版本，如果碰到编译问题，例如“ANN_MLP”相关的错误，尝试将config.h中将#define CV_VERSION_THREE_ZERO改为#define CV_VERSION_THREE_TWO试试. 1.  linux系统推荐使用Opencv3.2以上版本。3.2以下的版本例如3.0和3.1在识别时可能会出现车牌识别结果为空的情况。稳妥起见，建议都升级到最新的3.2版本。Windows版本没有这个问题。 
### 待做的工作
- <input type="checkbox" class="task-list-item-checkbox" disabled> 完成一个CNN框架- <input type="checkbox" class="task-list-item-checkbox" disabled> 替换ANN为CNN- <input type="checkbox" class="task-list-item-checkbox" disabled> 增加新能源车的识别（待定）- <input type="checkbox" class="task-list-item-checkbox" disabled> 增加两行车牌的识别（待定）
#### 跨平台

目前除了windows平台以外，还有以下其他平台的EasyPR版本。一些平台的版本可能会暂时落后于主平台。

现在有一个无需配置opencv的1.5版本的。仅仅支持vs2013，也只能在debug和x86下运行，其他情况的话还是得配置opencv。感谢范文捷同学的帮助。页面里的两个文件都要下载，下载后用解压。

|版本|开发者|版本|地址
|------
|C#|zhang-can|1.5|
|android|goldriver|1.4|
|linux|Micooz|1.6|已跟EasyPR整合
|ios|zhoushiwei|1.3|
|mac|zhoushiwei,Micooz|1.6|已跟EasyPR整合
|java|fan-wenjie|1.2|
|懒人版|fan-wenjie|1.5|

#### 兼容性

当前EasyPR是基于opencv3.0版本开发的，3.0及以上的版本应该可以兼容，以前的版本可能会存在不兼容的现象。

#### 例子

假设我们有如下的原始图片，需要识别出中间的车牌字符与颜色：

<img src="https://img-blog.csdnimg.cn/c3e2c04070ce4d6fb3a711a57a8be492.png" alt="在这里插入图片描述">

经过EasyPR的第一步处理车牌检测（PlateDetect）以后，我们获得了原始图片中仅包含车牌的图块：

<img src="https://img-blog.csdnimg.cn/1a5dd70462f6462bbd3ec463cd4fad55.png" alt="在这里插入图片描述">

接着，我们对图块进行OCR过程，在EasyPR中，叫做字符识别（CharsRecognize）。我们得到了一个包含车牌颜色与字符的字符串：

“蓝牌：苏EUK722”

#### 示例

EasyPR的调用非常简单，下面是一段示例代码:

```
	CPlateRecognize pr;
	pr.setResultShow(false);
	pr.setDetectType(PR_DETECT_CMSER);
     
	vector&lt;CPlate&gt; plateVec;
	Mat src = imread(filepath);
	int result = pr.plateRecognize(src, plateVec);

```

我们首先创建一个CPlateRecognize的对象pr，接着设置pr的属性。

```
	pr.setResultShow(false);

```

这句话设置EasyPR是否打开结果展示窗口，如下图。设置为true就是打开，否则就是关闭。在需要观看定位结果时，建议打开，快速运行时关闭。

<img src="https://img-blog.csdnimg.cn/f660f6ea011e4918baea105605f5680b.png" alt="在这里插入图片描述">

```
	pr.setDetectType(PR_DETECT_CMSER);

```

这句话设置EasyPR采用的车牌定位算法。CMER代表文字定位方法，SOBEL和COLOR分别代表边缘和颜色定位方法。可以通过"|"符号结合。

```
	pr.setDetectType(PR_DETECT_COLOR | PR_DETECT_SOBEL);

```

除此之外，还可以有一些其他的属性值设置：

```
	pr.setLifemode(true);

```

这句话设置开启生活模式，这个属性在定位方法为SOBEL时可以发挥作用，能增大搜索范围，提高鲁棒性。

```
	pr.setMaxPlates(4);

```

这句话设置EasyPR最多查找多少个车牌。当一副图中有大于n个车牌时，EasyPR最终只会输出可能性最高的n个。

下面来看pr的方法。plateRecognize()这个方法有两个参数，第一个代表输入图像，第二个代表输出的车牌CPlate集合。

```
	vector&lt;CPlate&gt; plateVec;
	Mat src = imread(filepath);
	int result = pr.plateRecognize(src, plateVec);

```

当返回结果result为0时，代表识别成功，否则失败。

CPlate类包含了车牌的各种信息，其中重要的如下：

```
	CPlate plate = plateVec.at(i);
	Mat plateMat = plate.getPlateMat();
	RotatedRect rrect = plate.getPlatePos();
	string license = plate.getPlateStr();

```

plateMat代表车牌图像，rrect代表车牌的可旋转矩形位置，license代表车牌字符串，例如“蓝牌：苏EUK722”。

这里说下如何去阅读如下图的识别结果。

<img src="https://img-blog.csdnimg.cn/997bbd3bff8c4331a61bee059737aaa1.png" alt="在这里插入图片描述">

第1行代表的是图片的文件名。

第2行代表GroundTruth车牌，用后缀（g）表示。第3行代表EasyPR检测车牌，用后缀（d）表示。两者形成一个配对，第4行代表两者的字符差距。

下面同上。本图片中有3个车牌，所有共有三个配对。最后的Recall等指标代表的是整幅图片的定位评价，考虑了三个配对的结果。

有时检测车牌的部分会用“无车牌”与“No string”替代。“无车牌”代表“定位不成功”，“No string”代表“定位成功但字符分割失败”。

#### 目录结构

以下表格是本工程中所有目录的解释:

|目录|解释
|------
|src|所有源文件
|include|所有头文件
|test|测试程序
|model|机器学习的模型
|resources/text|中文字符映射表
|resources/train|训练数据与说明
|resources/image|测试用的图片
|resources/doc|相关文档
|tmp|训练数据读取目录，需要自建

以下表格是resources/image目录中子目录的解释:

|目录|解释
|------
|general_test|GDTS（通用数据测试集）
|native_test|NDTS（本地数据测试集）
|tmp|Debug模式下EasyPR输出中间图片的目录，需要自建

以下表格是src目录中子目录的解释:

|目录|解释
|------
|core|核心功能
|preprocess|SVM预处理
|train|训练目录，存放模型训练的代码
|util|辅助功能

以下表格是src目录下一些核心文件的解释与关系:

|文件|解释
|------
|plate_locate|车牌定位
|plate_judge|车牌判断
|plate_detect|车牌检测，是车牌定位与车牌判断功能的组合
|chars_segment|字符分割
|chars_identify|字符鉴别
|chars_recognise|字符识别，是字符分割与字符鉴别功能的组合
|plate_recognize|车牌识别，是车牌检测与字符识别的共有子类
|feature|特征提取回调函数
|plate|车牌抽象
|core_func.h|共有的一些函数

以下表格是test目录下文件的解释:

|文件|解释
|------
|main.cpp|主命令行窗口
|accuracy.hpp|批量测试
|chars.hpp|字符识别相关
|plate.hpp|车牌识别相关

以下表格是train目录下文件的解释:

|文件|解释
|------
|ann_train.cpp|训练二值化字符
|annCh_train.hpp|训练中文灰度字符
|svm_train.hpp|训练车牌判断
|create_data.hpp|生成合成数据

#### 使用

请参考

下载地址：
