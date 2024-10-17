
--- 
title:  5 分钟用 Python 实现车牌识别 
tags: []
categories: [] 

---
车牌识别在高速公路中有着广泛的应用，比如我们常见的电子收费（ETC）系统和交通违章车辆的检测，除此之外像小区或地下车库门禁也会用到，基本上凡是需要对车辆进行身份检测的地方都会用到。

### 简介

车牌识别系统（Vehicle License Plate Recognition）是计算机视频图像识别技术在车辆牌照识别中的一种应用，通常一个车牌识别系统主要包括以下这四个部分：
- 车辆图像获取- 车牌定位- 车牌字符分割- 车牌字符识别
我们再来看一下百科中对车牌识别技术的描述：

>  
 车牌识别技术要求能够将运动中的汽车牌照从复杂背景中提取并识别出来，通过车牌提取、图像预处理、特征提取、车牌字符识别等技术，识别车辆牌号、颜色等信息，目前最新的技术水平为字母和数字的识别率可达到 99.7%，汉字的识别率可达到 99%。 


### 实现方式

我们这里不做太复杂的车辆动态识别，只演示从图像中识别车牌信息，车牌识别功能的实现方式大致分为两种，一种是自己编写代码实现，另一种是借助第三方 API 接口实现。

#### 自己实现

如果我们想要通过 Python 自己手动编码实现车牌识别功能，可以借助一些 Python 库，比如：OpenCV、TensorFlow 等，这种方式因为每一个功能点都需要我们自己编码实现，所有会相对复杂一些，另一方面如果我们想要保证识别的准确性，可能需要做大量的实验，也就是说会花费更多的时间。

#### 第三方接口

现在已经有一些第三方平台实现好了车牌识别的功能，并且他们对外提供了 API 接口，我们只需要调用他们提供的接口即可，这种方式实现就相对简单了一些，并且通常接口提供方对外提供的接口功能的准确性也是基本可以保证的，原因很简单，如果接口功能太差的话，一是自己打脸，还有就是基本不会有什么人使用，也就失去了接口对外提供的价值了，另外第三方接口可能会收取一定费用，因此，如果现实中我们具体实现的话要综合考虑。

### 具体实现

综合上面的情况，我们这里采用第三方接口的方式来实现车牌识别的功能，接口提供方我们选择百度云提供的接口，百度云接口提供了免费额度，简单来说就是每天可以免费使用多少次，如果超过了这个次数就需要交钱什么的了，文档地址为：`https://cloud.baidu.com/doc/OCR/index.html`，下面来看一下具体实现过程。

#### SDK 安装

百度云 SDK 对多种语言提供了支持，比如：Python、Java、C++、IOS、Android 等，这里我们安装 Python 版的 SDK，安装很简单，使用 `pip install baidu-aip` 命令即可，SDK 支持 Python 的版本为：2.7+ 与 3.x，SDK 目录结构如下：

```
├── README.md
├── aip                   // SDK 目录
│   ├── __init__.py       // 导出类
│   ├── base.py           // aip 基类
│   ├── http.py           // http 请求
│   └── ocr.py //OCR
└── setup.py              // setuptools 安装

```

#### 创建应用

SDK 安装好后，我们接着需要创建应用了，这里需要一个百度账号或百度云账号，如果没有的话自己注册一个即可，登录及注册地址为：`https://login.bce.baidu.com/?redirect=http%3A%2F%2Fcloud.baidu.com%2Fcampaign%2Fcampus-2018%2Findex.html`，登录之后，我们将鼠标移动到登录头像位置，接着在弹出菜单中单击用户中心，如下图所示： <img src="https://img-blog.csdnimg.cn/20200422084304873.png" alt=""> 如果是首次进入的话，勾选一下相应信息，如下图所示： <img src="https://img-blog.csdnimg.cn/20200422084345822.png" alt=""> 信息勾选完了之后，点击保存按钮。

接着将鼠标移动到左侧栏中 `&gt;` 符号位置，再依次选择人工智能和文字识别，如下图所示： <img src="https://img-blog.csdnimg.cn/20200422084412859.png" alt=""> 点击之后会进入到下图中： <img src="https://img-blog.csdnimg.cn/20200422084434970.png" alt=""> 我们点击创建应用，进入下图中： <img src="https://img-blog.csdnimg.cn/20200422084454132.png" alt=""> 这里我们只需要填一下应用名称和下面的应用描述即可，填写完毕之后点击立即创建。

创建完后，我们再返回应用列表，如下图所示： <img src="https://img-blog.csdnimg.cn/20200422084513137.png" alt=""> 这里我们需要用到三个值：AppID、API Key 和 Secret Key。

#### 具体实现

应用创建完了，我们就可以调用接口实现车牌识别功能了。

首先，我们要创建 AipOcr，AipOcr 是 OCR 的 Python SDK 客户端，为使用 OCR 的开发人员提供了一系列的交互方法，代码实现也比较简单，如下所示：

```
from aip import AipOcr

# 自己的 APPID AK SK
APP_ID = '自己的 App ID'
API_KEY = '自己的 Api Key'
SECRET_KEY = '自己的 Secret Key'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

```

在上面代码中，常量 APP_ID、API_KEY 和 SECRET_KEY 就是我们在查看应用列表时说的需要用到的常量值，这些值均为字符串，用于标识用户，为访问做签名验证。

如果我们需要配置 AipOcr 的网络请求参数，可以在构造 AipOcr 之后调用接口设置参数，目前支持两个参数，看一下代码实现：

```
# 建立连接的超时时间，单位为毫秒
client.setConnectionTimeoutInMillis(5000)
# 通过打开的连接传输数据的超时时间，单位为毫秒
client.setSocketTimeoutInMillis(5000)

```

总的来说通过接口方式实现车牌识别功能是比较简单的，以如下图为例： <img src="https://img-blog.csdnimg.cn/20200422084534922.png" alt=""> 实现代码如下：

```
from aip import AipOcr

APP_ID = '自己的 App ID'
API_KEY = '自己的 Api Key'
SECRET_KEY = '自己的 Secret Key'
# 创建客户端对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# 建立连接的超时时间，单位为毫秒
client.setConnectionTimeoutInMillis(5000)
# 通过打开的连接传输数据的超时时间，单位为毫秒
client.setSocketTimeoutInMillis(5000)

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('car.jpeg')
res = client.licensePlate(image)
print('车牌号码：' + res['words_result']['number'])
print('车牌颜色：' + res['words_result']['color'])

```

执行结果：

```
车牌号码：川QK9777
车牌颜色：blue

```

上面代码实现的是对一张图片中的一个车牌进行识别，当然接口还支持对一张图片中的多个车牌进行识别，只需使用 licensePlate(image, options) 即可， 以如下图为例： <img src="https://img-blog.csdnimg.cn/20200422084557293.png" alt=""> 实现代码如下：

```
from aip import AipOcr

APP_ID = '自己的 App ID'
API_KEY = '自己的 Api Key'
SECRET_KEY = '自己的 Secret Key'
# 创建客户端对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# 建立连接的超时时间，单位为毫秒
client.setConnectionTimeoutInMillis(5000)
# 通过打开的连接传输数据的超时时间，单位为毫秒
client.setSocketTimeoutInMillis(5000)

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('cars.png')
options = {<!-- -->}
# 参数 multi_detect 默认为 false
options['multi_detect'] = 'true'
res = client.licensePlate(image, options)
for wr in res['words_result']:
    print('车牌号码：' + wr['number'])
    print('车牌颜色：' + wr['color'])

```

执行结果：

```
车牌号码：京N6HZ61
车牌颜色：blue
车牌号码：鲁NS1A26
车牌颜色：blue

```

### 总结

本文我们先对车牌识别进行了一些介绍，之后利用百度云接口实现了单个和多个车牌的识别功能，通过本文我们可以对车牌识别的相关概念和具体实现有一些了解。

>  
 本文作者为本人，但非首发于个人号 


<img src="https://img-blog.csdnimg.cn/20200321222018500.PNG?#pic_center" alt="" width="500">
