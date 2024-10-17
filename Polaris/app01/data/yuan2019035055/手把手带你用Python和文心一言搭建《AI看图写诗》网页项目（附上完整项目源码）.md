
--- 
title:  手把手带你用Python和文心一言搭建《AI看图写诗》网页项目（附上完整项目源码） 
tags: []
categories: [] 

---
今年年初，ChatGPT的火爆在全球掀起AI大模型的开发热潮，国内外的科技公司纷纷加入“百模大战”行列。百度在率先发布了国内第一款人工智能大语言模型“文心一言”后，又推出了文心千帆大模型平台，帮助企业和开发者加速大模型应用落地。

而最近百度创始人、董事长兼首席执行官李彦宏在一场活动上透露了百度世界大会2023的重磅消息，他将在10月17号百度世界大会召开的时候，“手把手教你怎么做AI原生应用”。

我自己也突发奇想用文心一言搭建一个AI小应用：《看图写诗》，说干就干，接下来就跟着博主一起实现这个网页吧！

<img src="https://img-blog.csdnimg.cn/img_convert/a9da5a7cfde665e74bc732cb6370edf6.png" alt=""> 

#### 文章目录
- - - <ul><li>- - <ul><li>- - - - - 


## 一、实现思路

1、设计一款网页实现接受上传图片和接收文心一言令牌Token功能

2、Python调用百度智能云的图片识别接口，识别图片类别和内容

3、Python调用文心一言接口，输入图片类别，通过文心一言写诗

4、Python后端将诗返回到网页上

## 二、《AI看图写诗》网页搭建实现步骤

### 2.1 网页前端

网页前端采用HTML+CSS+JavaScript技术，实现了上传图片、展示图片，传入百度智能云AppId、百度智能云API Key、百度智能云Secret Key、飞浆星河Access Token和点击写诗功能，界面如下：

<img src="https://img-blog.csdnimg.cn/img_convert/83599108d887cbee3fe6806612a004d6.png" alt="">

### 2.2 图像识别

百度智能图像识别接口是百度提供的一项人工智能服务，能够对图片进行高精度的内容识别，该接口支持多种图像识别任务，包括通用物体识别、场景识别、文字识别、动物识别等，这里我们通过Python直接调用免费的通用物体识别图像识别接口，极大的提高了开发工作的效率。

#### 2.2.1 安装百度智能云Python SDK

可以通过pip安装百度智能云Python SDK。在终端下输入以下命令：

```
pip install baidu-aip 

```

安装完毕后，你就可以在Python代码中导入该包了：

```
from aip import AipImageClassify

```

#### 2.2.2 创建应用

1、登录百度智能云的官网：

2、依次找到点击 产品 》人工智能 》图像识别

<img src="https://img-blog.csdnimg.cn/img_convert/1a70750585ce5ef432ca86ce5634effe.png" alt="">

3、登录控制台后点击免费尝鲜：

<img src="https://img-blog.csdnimg.cn/img_convert/919939c5cae1f8bf9ea9d8295c09e393.png" alt="">

4、勾选全部然后点击0元领取：

<img src="https://img-blog.csdnimg.cn/img_convert/f00a0f31d62011a4ed14f832543725c4.png" alt="">

5、创建成功后，点击应用进入应用详情页，进入应用管理菜单，点击API Key，可查看API Key和Secret Key，用于Python代码调用API。

<img src="https://img-blog.csdnimg.cn/a01d8fb01d83463f88badd87bceeec2e.png" alt="在这里插入图片描述">

#### 2.2.3 Python代码测试

经过以上两步准备工作，我们便可以开始编写Python代码，实现百度智能图片识别。以下是一个简单的测试示例，需要修改AppId 、API Key、Secret Key和图片路径：

```
from aip import AipImageClassify

# 定义百度智能云API的参数
APP_ID = '你的API ID'
API_KEY = '你的API Key'
SECRET_KEY = '你的 Secret Key'

# 实例化AipImageClassify
client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

# 读取并设置图片路径
filePath = "1.png"

# 打开图片文件
with open(filePath, 'rb') as fp:
   image = fp.read()

# 定义可选参数
options = {<!-- -->"baike_num": 1}

# 调用图片标签识别接口
result = client.advancedGeneral(image, options)

# 输出结果
for res in result['result']:
   print(res['keyword'], end=", ")

```

我输出图片是这张风景图，没有文字还是很有挑战的：

<img src="https://img-blog.csdnimg.cn/img_convert/0fa51731d0309c78edac6a681c1726e0.png" alt="">

识别效果，图片上的信息都给识别出来了：

<img src="https://img-blog.csdnimg.cn/46881b40aa7d4fddbcc2b9c3a0692afe.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/img_convert/79b30b8ee230cb23d3811f33be13f71d.png" alt="">

接下来我们就需要把识别出来的图像内容传给文心一言写诗了。

### 2.3 文心一言写诗

这里我是通过ERNIE Bot SDK提供便捷易用的接口，可以调用文心一言的能力，包含文本创作、通用对话、语义向量、Al作图等，并且可以免费调用100万Token：

<img src="https://img-blog.csdnimg.cn/img_convert/61161ba7c9e4734559e4111320173b83.png" alt="">

#### 2.3.1 安装ERNIE Bot SDK

ERNIE Bot SDK是文心&amp;飞桨官方提供的Python软件开发工具包，简称EB SDK，通过下面的pip命令安装：

```
pip install erniebot

```

EB SDK认证鉴权主要是设置后端和access token，分别通过api_type和access_token参数来指定，默认使用aistudio后端（api_type为aistudio），将个人中心令牌Token，复制后填入下面代码中即可（替换{YOUR-ACCESS-TOKEN}）：

<img src="https://img-blog.csdnimg.cn/img_convert/d719dee368b85631cd6430a0bc90f4ba.png" alt="">

#### 2.3.2 获取令牌Token

1、打开飞浆星河社区的官网：

2、注册完账号后，点击查看：

<img src="https://img-blog.csdnimg.cn/img_convert/bdadc5707d2390e49538a739ea45f9fb.png" alt="">

3、获取自己的Token令牌并复制，后面我们用Python去调用接口会使用到：

<img src="https://img-blog.csdnimg.cn/img_convert/c84cb01b82e15c3fccd71ba4d0cbdfde.png" alt="">

#### 2.3.3 Python代码测试

下面我们来单独测试一下通过ERNIE Bot SDK调用文心一言接口写诗的能力，完整代码如下（只需要替换为自己的Token）：

```
import erniebot


if __name__ == '__main__':
   # img_str，access_token需要传入
   img_str = '树, 瀑布, 江河, 峡谷, 山峦' # 这里需要图片识别的内容信息
   access_token = "这里替换为自己的TOken"
   content = '根据'+img_str,'写10首两句七言诗'

   erniebot.api_type = 'aistudio'
   erniebot.access_token = access_token
   response = erniebot.ChatCompletion.create(
       model='ernie-bot',
       messages=[{<!-- -->'role': 'user', 'content': f"{<!-- -->content}”"}],
   )
   print(response.result)

```

运行输出结果还是非常不错的：

<img src="https://img-blog.csdnimg.cn/img_convert/6e8613723f822cd9314f85b1384a086b.png" alt="">

<img src="https://img-blog.csdnimg.cn/b0a96d9680dd42b3bef4a5faa00d75a0.png" alt="在这里插入图片描述">

接下来就只需要将生成的诗句传递给网页端展示出来就可以啦。

### 2.4 网页后端

使用到了下面两个Python库，执行pip命令安装一下：

```
pip install fastapi
pip install pydantic

```

网页后端实现接收前端传入的图片和令牌，然后调用百度智能云的图片识别接口和文心一言大模型接口，然后将生成的诗句返回给网页前端的功能，后端代码如下：

```
from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import erniebot
from aip import AipImageClassify

app = FastAPI()
origins = [
   "http://localhost.tiangolo.com",
   "https://localhost.tiangolo.com",
   "http://localhost",
   "http://localhost:8000",
   "http://localhost:63342",
   # "http://127.0.0.1:8000"
]
app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)
class PoeSimpleReq(BaseModel):
   access_token: str
   app_id: str
   api_key: str
   classify_secret_key: str
   file: bytes = File(default=None)

@app.post("/poe")
async def read_root(access_token: str = Form(), app_id: str = Form(), api_key: str = Form(),
                   classify_secret_key: str = Form(), image: UploadFile = File()):
   if access_token is None or app_id is None or api_key is None or classify_secret_key is None or classify_secret_key is None or image is None:
       return "Supplementary information on the left"
   access_token = access_token

   APP_ID = app_id
   API_KEY = api_key
   CLASSIFY_SECRET_KEY = classify_secret_key

   client = AipImageClassify(APP_ID, API_KEY, CLASSIFY_SECRET_KEY)
   # 定义可选参数
   options = {<!-- -->"baike_num": 5}
   # 调用图片标签识别接口
   result = client.advancedGeneral(image.file.read(), options)
   print("pic result:", result)
   keyword_list = []

   for res in result['result']:
       keyword_list.append(res['keyword'])
   keyword_string = ', '.join(keyword_list)
   content = '根据' + keyword_string + '写10首两句七言诗'
   erniebot.api_type = 'aistudio'
   erniebot.access_token = access_token
   response = erniebot.ChatCompletion.create(
       model='ernie-bot',
       messages=[{<!-- -->'role': 'user', 'content': f"{<!-- -->content}”"}],
   )

   data_str = response.result
   return data_str.replace("\n", "  ")

```

### 2.5 完整项目拷贝

博主已经将这个项目的完整源码上传到Gitee上开源，小伙伴们可以自行下载和修改项目： 

<img src="https://img-blog.csdnimg.cn/img_convert/0b3b6bddbf9434aaf75bf1d309e1b74f.png" alt="">

### 2.6 项目运行步骤

1、根据上面教程提前准备好百度智能云AppId、百度智能云API Key、百度智能云Secret Key、飞浆星河Access Token

2、下载拷贝完整源码，创建虚拟环境，pip安装依赖包

3、进入源码路径，启动对应虚拟环境，在cmd输入下面命令启动代码：

```
uvicorn main:app --reload

```

如图：

<img src="https://img-blog.csdnimg.cn/093e08f792aa444e8455185a756fcbaa.png" alt="在这里插入图片描述">

4、选择HTML代码，从pycharm点击打开网页：

<img src="https://img-blog.csdnimg.cn/942f517e92ff4233b7c0f2b272beb5b5.png" alt="在这里插入图片描述">

5、打开主界面如下所示：

<img src="https://img-blog.csdnimg.cn/4935d7e828ae41deb149ad1d4e06aee3.png" alt="在这里插入图片描述">

6、点击选择图片，并展示图片：

<img src="https://img-blog.csdnimg.cn/img_convert/877c3230b6114ae650094a6d634f7eb5.png" alt="">

7、填写根据上面教程准备好的百度智能云AppId、百度智能云API Key、百度智能云Secret Key、飞浆星河Access Token（注意：这个四个都需要填写）：

<img src="https://img-blog.csdnimg.cn/img_convert/67b05deaa8e5bd4dbb9c0b9024246744.png" alt="">

8、点击生成诗句：

<img src="https://img-blog.csdnimg.cn/30ca8ebab2f045f3ad1c77484b115ff3.png" alt="在这里插入图片描述">

9、等待一会就生成完成了：

<img src="https://img-blog.csdnimg.cn/409833569bfd4776a5af233ec207f758.png" alt="在这里插入图片描述">

OK这里完整项目运行流程就结束了，大家还不速度上号体验一番！

### 2.7 运行流程视频



《AI看图写诗》项目运行流程



## 三、未来优化

1、网页主页界面UI设计优化。

2、增强新功能，如：通过文心一言的接口实现根据文字绘画、文档整理等功能。

3、网站部署上线

**大家有更好多想法可以评论区留言我们一起去实现！**

## 四、总结

通过这小案例我们了解到了如何通过AI实现了看图写诗应用，主要依靠的还是百度智能云的图片识别接口和文心一言大模型的文本生成能力，当然除了文本生成以外，文心一言大模型还可以生成图片、音频和视频功能等等，这些非常都值得我们后续不断去探索和应用。

以“生成未来”为主题的百度世界大会将于10月17日在北京首钢园举行,除了李彦宏的现场教学“手把手教你怎么做AI原生应用”，百度世界大会2023还将带来大模型、AI原生应用、生成式AI生态等内容的最新进展。让我们一起抓住大模型应用这场机遇吧！

<img src="https://img-blog.csdnimg.cn/img_convert/368fcbbb0baec33040311076dc312e19.png" alt="">

直播地址分享给大家：
