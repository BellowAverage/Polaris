
--- 
title:  安装2023最新版PyCharm来开发Python应用程序 
tags: []
categories: [] 

---
## 安装2023最新版PyCharm来开发Python应用程序

### Install the Latest JetBrains PyCharm Community to Develop Python Applications

Python 3.12.0最新版已经由其官网python.org发布，这也是2023年底的最新的版本。

#### 0. PyCharm与Python

**自从1991年2月20日，荷兰程序员Guido van Rossum发布Python的第一个版本至今，Python编程语言已经伴随我们走过了23年。如今Python成长为一个精力充沛、能量满满的“小伙子”。**

>  
 三十年来，因Python而产生的集成开发环境(IDE, 即Integrated Development Environment) 发布了很多种；其中，捷克的高科技公司JetBrains可谓是异军突起，其研发的PyCharm系列IDE开发工具迅速占领全球市场，在数据科学、人工智能领域和程序员社区引起了广泛关注及使用。 


本文简要介绍**JetBrains PyCharm Community Edition** (JetBrains PyCharm社区版)的安装使用过程，希望您用起来得心应手，流畅地开启您的Python开发之旅。

#### 1. 下载安装Python最新版3.12.0

打开Chrome浏览器，访问Python官网：www.python.org, 如下图所示：

<img src="https://img-blog.csdnimg.cn/b2dc7a6cf24a4820839c400c99bb96e3.png" alt="在这里插入图片描述"> 关于如何在Python官网下载并安装最新版Python 3.12.0，请参照文档：。本文不再赘述。

#### 2. 下载 PyCharm Community Edition

访问JetBrains中国官网： , 如下图：

<img src="https://img-blog.csdnimg.cn/28ccd2a88a48433395fa5311f23f026c.png" alt="在这里插入图片描述">

点击导航栏上的开发者工具菜单，选择**PyCharm**，如下图所示：

<img src="https://img-blog.csdnimg.cn/91f2eb192b964dbcb7c778063065ae92.png" alt="在这里插入图片描述"> 进入PyCharm下载页面。 <img src="https://img-blog.csdnimg.cn/da088b1d62414659933f457abe10ba55.png" alt="在这里插入图片描述">

点击**下载**，继续下一步，进入下载选项页面。

<img src="https://img-blog.csdnimg.cn/9c6806dda7d348298b883dbe9954ba91.png" alt="在这里插入图片描述"> 我们看到首先出现的是PyCharm Professional (PyCharm专业版)，专业版许可证需要购买后才能使用 。

为了使用免费版，将鼠标滚动到下载页面下方，选择PyCharm Community Edition (PyCharm社区版)，点击**下载**。 <img src="https://img-blog.csdnimg.cn/cd5dae777d714feaafaa84cfee3c5f08.png" alt="在这里插入图片描述"> Chrome浏览器开始下载软件包（如右上方下载记录）。同时，页面提示：**如果没有开始，请使用直接链接** 来下载。

下载完毕后，找到Windows 10/11的下载 文件夹里的安装可执行文件 **pycharm-community-2023.2.5.exe**, 双击它启动安装向导。

#### 3. 安装PyCharm Community Edition

启动PyCharm安装向导，出现欢迎画面对话框Welcome to PyCharm Community Edition Setup。

<img src="https://img-blog.csdnimg.cn/8c148df3157a4576a6190cb07424f7f8.png" alt="在这里插入图片描述"> 点击 **Next** 进入下一步。

<img src="https://img-blog.csdnimg.cn/2b7ff24f86964fae8eae8ef040b4b6c7.png" alt="在这里插入图片描述"> 进入Choose Install Location(选择安装位置)对话框，保留默认**Desination Foler（目标安装文件夹）**，点击**Next** 进入下一步。

<img src="https://img-blog.csdnimg.cn/245a6738a0664e6a9dfcf80ba747a731.png" alt="在这里插入图片描述">

进入Installation Options(安装选项)对话框，复选四个选项，分别实现1）创建.py文件关联；2）增加上下文菜单；3）创建桌面快捷方式，以及4）增加bin文件夹到PATH环境变量。

点击**Next**进入下一步。

<img src="https://img-blog.csdnimg.cn/0055eeb3174049e3bbdce1b9b4a31612.png" alt="在这里插入图片描述"> 进入Choose Start Menu Folder(选择启动菜单文件夹)对话框，按照默认选项，点击**Install**开始安装。

<img src="https://img-blog.csdnimg.cn/f6aba6d7bf8f40188adb37335911d495.png" alt="在这里插入图片描述"> 进入安装过程，很快安装结束，

<img src="https://img-blog.csdnimg.cn/b9f39c73c9b94378bc26cafeda05c616.png" alt="在这里插入图片描述"> 选择I want to manually reboot later (我想稍后手动重启)，点击Finish退出安装向导。

#### 4. 用PyCharm创建第一个Python应用程序！

安装完成，需要启动PyCharm来进行Python编程。

在Windows搜索栏，搜索PyCharm关键字，找到该程序，选择 **以管理员身份运行启动**PyCharm Community Edition 2023.2.5。

<img src="https://img-blog.csdnimg.cn/d501168e72e244fcb7bc98a5b325039b.png" alt="在这里插入图片描述"> 出现Import PyCharm Settings(输入PyCharm设置)对话框，由于首次启动，尚未设置，遂选择默认选项Do not import settings (不输入设置)，点击OK进入。 <img src="https://img-blog.csdnimg.cn/6c8abd47fe1840fc896f100dad773301.png" alt="在这里插入图片描述"> 这样，就启动了PyCharm Community Edition 2023.2.5版本，如下图：

<img src="https://img-blog.csdnimg.cn/7f8deecb4101486ea31024694d15981e.png" alt="在这里插入图片描述"> 点击**New Project**, 创建一个新的项目（前提是已经在PyCharm之前安装了Python 3.12.0最新版）。 <img src="https://img-blog.csdnimg.cn/11c4d8e9ddbb43429307125114a24bb6.png" alt="在这里插入图片描述"> 按照默认的虚拟环境（Virtualenv）位置，系统已经自动识别了Base Interpreter (基本解释器)，即安装在D:\Python312的Python最新版3.12.0。 点击Create创建这个项目。

打开PyCharm的同时，还会创建一个Main.py的文件，就是第一个Python应用程序的默认文件名。 <img src="https://img-blog.csdnimg.cn/ef6d511f61534cb48b9cc18c2fd00db2.png" alt="在这里插入图片描述"> 可以看出，默认创建的main.py程序文件，添加了一些注释，并且有一个初始化函数判断 **if _ **name** _ == ‘<strong>main**’</strong>: 点击运行**Run ‘main’**, 或者**按组合键Shift + F10**，运行该程序。

<img src="https://img-blog.csdnimg.cn/e6c8189e8be74be0933d17aefa293241.png" alt="在这里插入图片描述">

终端打印输出了**Hi, PyCharm**, 表明运行成功！

同时，为了简化第一个Python应用程序，也可以修改文件内容，力图打印输出Hello, world! 结果。代码如下：

```
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello, {<!-- -->name}！')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
print_hi('World')

```

程序运行结果如下图： <img src="https://img-blog.csdnimg.cn/09ef8fdc242d4498a66d4e61250f2ae9.png" alt="在这里插入图片描述">

可以看到，终端打印输出Hello, world! 说明Python程序运行成功！

接下来，就可以使用PyCharm开发您所需要的应用程序了。

技术好文陆续推出，敬请关注。

喜欢就点赞哈！😊

#### 相关阅读：
1. 1. 1. 1. 1. 1. 