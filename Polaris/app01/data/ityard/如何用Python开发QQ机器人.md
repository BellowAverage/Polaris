
--- 
title:  如何用Python开发QQ机器人 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/07dafc07c8cab1cfdbddb0d7106b9453.png">

>  
  作者：tanleiDD 
  https://blog.csdn.net/TL18382950497/article/details/112321956 
 

### 前言
- 虽然该文最终是达到以python开发mirai机器人的目的，但起步教程，尤其是环境配置上仍然有大量的相同操作，对其他编程语言仍有借鉴之处- 假设你已经安装好了 `Java`、`Python`等运行必须的环境
### mirai生态
- mirai官方生态文档<sup>[1]</sup>- 要使用mirai开发QQ机器人，首先要对其生态有一定的了解，因为它太复杂了，坑特别多，所以多了解一点，遇到问题之后解决起来也会更快- mirai生态汇总图- 简单来说，mirai生态的核心是Mirai框架，其中包含了`mirai-core`及`mirai-core-api`两部分。- 其中，前者负责协议相关的内容，而后者负责对外提供操作前者的接口。因此与程序员直接打交道的是mirai-core-api，而mirai-core，对我们是不可见的。- 使用mirai-core-api就已经可以开发QQ机器人了，但对萌新来说难度还是太大，于是mirai官方开发组编写了一个QQ机器人程序，`mirai-console`，它在 mirai 框架提供的基础功能的基础上进行了封装并进一步提供了更方便的开放接口。- 有了mirai-console，我们就不用直接去开发mirai的QQ机器人了，而是去开发mirai-console的插件，如下面的模式：<img src="https://img-blog.csdnimg.cn/img_convert/44657d093a261e0ed8317eb279cd1acf.png">- 尴尬的是，开发mirai-console的插件，又需要使用java或者kotlin。如果你跟我一样，对他们都不熟悉，那么官方的另一个插件`mirai-api-http`，则可以解决这个问题。- 于是借助mirai-api-http开发QQ机器人，就成了下面这种模式：<img src="https://img-blog.csdnimg.cn/img_convert/1aec296545177ccb2e4a6f2ee955185c.png">- 可以看到，当我们使用了mirai-api-http后，我们就有了更多的开发语言选择。此处我选择python。
### 起步

#### 使用 mirai-console-loader 启动 mirai-console
- 根据上面的介绍，要开发一个mirai的QQ机器人，我们首先需要将mirai-console给运行起来，而要做到这一步，可难。例如你需要准备`mirai-core`，`mirai-console` 和 `mirai-console-terminal`，然后还需要通过一大串指令来启动它。- 而官方显然考虑到这一点，为了挽回被这一高难度操作劝退的萌新，官方又推出了`mirai-console-loader`(简称mcl) —— mirai-console 的官方一键启动器。因此你仅需要下载它即可(第一步说的都不用管0.0)。github仓库位置：mirai-console-loader<sup>[2]</sup>- 下载完成mcl之后，解压、打开cmd、切换到mcl所在目录、运行mcl。如下图：<img src="https://img-blog.csdnimg.cn/img_convert/62853674ae3464f459efdd938945bd64.png">- 不出意外的话，mirai-console就成功启动了，如下图：<img src="https://img-blog.csdnimg.cn/img_convert/a556a59189adca1c10af04ef24febb16.png">- 然而，咱从官方下载的项目，运行时却出错了0.0 ( 如果你没有出错，忽略此步骤 )。原因是配置文件出错 (太倒霉了 - -)。修改方式如图：<img src="https://img-blog.csdnimg.cn/img_convert/05f65a657dcb035f0690821da2874afc.png">- 然后再重新运行一下，mcl，不出意料的话，能成功运行。- 第一个大坎就迈过了…接下来是另一个大坎
#### 使用 mirai-login-solver-selenium 处理滑块验证辅助登录
- 在成功启动的mcl窗口，运行命令登录qq：`login 账号 密码`- 应该是会出错的，因为mirai-console在登录时，不能处理滑块验证：<img src="https://img-blog.csdnimg.cn/img_convert/7815ffd685337928f2724b81b3626e50.png">- 于是我们需要mirai的另一个项目 mirai-login-solver-selenium<sup>[3]</sup> 来辅助登录- mirai-login-solver-selenium安装步骤 (**需要先安装 Chrome 浏览器**)- 先结束掉之前运行的 mirai-console, 然后在命令行运行如下命令，添加该包
```
mcl --update-package net.mamoe:mirai-login-solver-selenium --channel nightly --type plugin

```
- 然后再重新运行mcl，这样mcl就会去尝试下载mirai-login-solver-selenium。- 然而，我这一步也出现问题了（如果你没有问题，也请跳过）。因为它用到了selenium，所以就要用chromedriver。但是chromedriver总是下载失败，所以这一步需要手动下载chromedriver，然后替换到对应目录。步骤如下：1. 查看cmd窗口，找到mcl正在下载的chromedriver是什么版本<img src="https://img-blog.csdnimg.cn/img_convert/792d2352aeff7175995088ab8d16ece6.png">1. 然后去chromedriver的另一个镜像源下载，推荐：chromedriver<sup>[4]</sup>1. 找到一个版本号相近的即可，例如我就下载 `86.0.4240.22`<img src="https://img-blog.csdnimg.cn/img_convert/df8f8d1e576e8990652dc8c02a56c332.png">1. 将下载好的文件解压，再重命名成`chromedriver-86.0.4240.198.exe`，也就是刚刚我们在命令行窗口查看的文件名，一定要跟它想下载的文件名一致1. 结束之前运行的mcl命令行程序，然后将准备好的`chromedriver-86.0.4240.198.exe`, 替换到以下目录<img src="https://img-blog.csdnimg.cn/img_convert/baa9a8c5bff258b47c11da5526fec87a.png">1. 重新运行mcl程序，如果一切顺利，就可以继续之前的步骤，输入命令：`login 账号 密码` 尝试登录。接下来会弹出一个浏览器窗口，你只需要傻瓜式的完成登录验证即可。如果登录成功，以后的每次登录，应该都是不需要再次验证的。- 又跨过一个坎…接下来就到了另外一个坎<li><h4>使用 mirai-api-http 增加语言拓展性 (为了能用其他语言来开发)</h4> 
 <ul>- 前面一直在说 mirai-api-http，但是到目前为止，我们都还没有用上它。前面的工作就做了两个事情1. 使用mcl运行mirai-console1. 使用 mirai-login-solver-selenium 辅助通过滑块验证码，完成登录
那么接下来就开始用mirai-api-http，首先在mirai-api-http项目地址，下载mirai-api-http<sup>[5]</sup>

然后将下载到的jar包，放在plugin文件夹下，如图<img src="https://img-blog.csdnimg.cn/img_convert/b7e0bbec6d245332b95eaa3a7c5f4a46.png">

然后再重启mcl，重新进行登录。这样准备工作就完成了，但是我出现了一些错误，看意思应该是签名验证的问题，错误如下：<img src="https://img-blog.csdnimg.cn/img_convert/584bc6f3608130b95616e79657f8106a.png">

四处咨询后了解到，是oracle JDK的问题，因此只需要将orcaleJDK 替换成为 open JDK即可，步骤如下：
1. 下载 open JDK<sup>[6]</sup>，例如我下载如图所示的版本：<img src="https://img-blog.csdnimg.cn/img_convert/c45987444acce4aa02f79389f7c7fe87.png">1. 解压open JDK, 并放在你认为合适的位置，例如我放在如下图所示的位置：<img src="https://img-blog.csdnimg.cn/img_convert/2a16530a705bf8386d8f58d1f5dc40d9.png">1. 添加 jdk 所在路径到环境变量：此电脑 -&gt;右键属性 -&gt; 高级系统设置 -&gt; 高级 -&gt; 环境变量, 再按下图操作<img src="https://img-blog.csdnimg.cn/img_convert/c64bfaf230b47c0d8df8e567159165fb.png">
#### 通过 graia-application-mirai 使用 python 开发 mirai 机器人
- 前面的操作，直到该步为止，基本对所有使用`除java/kotlin`语言的程序员，都是通用的。而后面的操作，仅写给使用python的程序员- graia-application-mirai官方文档<sup>[7]</sup>- 首先对mirai-api-http进行配置，如图：<img src="https://img-blog.csdnimg.cn/img_convert/6720aac1389d88c20ab9b1dd897ab727.png">以下是参考，自己看着配就行
```
# file: mcl-1.0.3/config/net.mamoe.mirai.api.http/setting.yml
authKey: graia-mirai-api-http-authkey # 你可以自己设定, 这里作为示范

# 可选，缓存大小，默认4096.缓存过小会导致引用回复与撤回消息失败
cacheSize: 4096

enableWebsocket: true # 是否启用 websocket 方式, 若使用 websocket 方式交互会得到更好的性能
host: '0.0.0.0' # httpapi 服务监听的地址, 错误的设置会造成 Graia Application 无法与其交互
port: 8080 # httpapi 服务监听的端口, 错误的设置会造成 Graia Application 无法与其交互

```
- 重启mcl, 更新配置<li>接着，安装 python 操作 mirai-api-http 接口的模块：graia-application-mirai<pre class="has"><code class="language-go">pip install graia-application-mirai
</code></pre></li>- 将以下代码复制到bot.py，按注释提示，再结合刚刚对mirai-api-http的配置，稍作修改。然后运行
```
from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
from graia.application.message.chain import MessageChain
import asyncio

from graia.application.message.elements.internal import Plain
from graia.application.friend import Friend

loop = asyncio.get_event_loop()

bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://localhost:8080", # 填入 httpapi 服务运行的地址
        authKey="graia-mirai-api-http-authkey", # 填入 authKey
        account=5234120587, # 你的机器人的 qq 号
        websocket=True # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    )
)

@bcc.receiver("FriendMessage")
async def friend_message_listener(app: GraiaMiraiApplication, friend: Friend):
    await app.sendFriendMessage(friend, MessageChain.create([
        Plain("Hello, World!")
    ]))

app.launch_blocking()

```
- 然后向你的QQ机器人，随便发送一条消息，如果它回复你Hello, World!，则表示运行成功- 成功所示如下：<img src="https://img-blog.csdnimg.cn/img_convert/7d60ed99caf752fea5321d3af6f0e418.png">
### 结语

上面的全部操作，不过是使用mirai进行开发QQ机器人的起步教程而已，需要了解更多，还是去阅读官方文档，以学习更多的api。

#### 参考资料

[1]

mirai官方生态文档: https://github.com/mamoe/mirai/blob/dev/docs/mirai-ecology.md

mirai-console-loader: https://github.com/iTXTech/mirai-console-loader/tree/master

mirai-login-solver-selenium: https://github.com/project-mirai/mirai-login-solver-selenium/tree/master

chromedriver: http://npm.taobao.org/mirrors/chromedriver/

mirai-api-http: https://github.com/project-mirai/mirai-api-http

open JDK: http://jdk.java.net/archive/

graia-application-mirai官方文档: https://graia-document.vercel.app/

<img src="https://img-blog.csdnimg.cn/img_convert/7a3e3939e0739b3c2d258a7f177ef129.png">

**长按识别上方二维码**加我个人微信，

备注**666**免费领取电子书
