
--- 
title:  2024最新版PyCharm安装使用指南 
tags: []
categories: [] 

---
## 2024最新版PyCharm安装使用指南

### Installation and Usage Guide for the Latest JetBrains PyCharm Community Edition in 2024

By Jackson

Python 3.12.1最新版已经于2023年12月8日由其官网 python.org发布，这是2024年的最新Python版本。

#### 0. Python的由来

>  
 自从1991年2月20日，荷兰软件工程师 Guido van Rossum先生发布了Python的第一个版本至今，Python编程语言已经伴随我们走过了33个年头。 如今他为微软公司工作，致力于将Python语言集成到Excel这样的Office办公套件中去，以提升人们的工作效能。 


<img src="https://img-blog.csdnimg.cn/direct/823d41b6a6ef4f278073724fefe99283.png" alt="在这里插入图片描述"> *注：Guido先生照片来自于其个人网站

据说Guido先生退休后一年，由于不甘闲适，才又回到工作岗位，看起来他仍然是一个精力充沛、能量满满的小伙子。

#### 1. 下载安装Python最新版3.12.1

打开Chrome浏览器，访问Python官网：, 如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/fe04aea86f3145d7bf80a61f84998955.png" alt="在这里插入图片描述"> 在Python官网下载获取最新版3.12.1，请看笔者另一篇CSDN文档的详细步骤：。

本文不再赘述。

#### 2. 下载最新版PyCharm Community Edition

三十年来，因Python而产生的集成开发环境(IDE, 即Integrated Development Environment) 也发布了不少，例如：IDLE, Visual Studio Code, Jetbrains Pycharm, Sublime Text, Atom, Jupyter以及Spyder等。

其中，东欧国家捷克的高科技公司JetBrains可谓是异军突起，其研发的PyCharm系列IDE开发工具迅速占领全球市场， 在数据科学、人工智能领域和程序员社区引起了广泛关注及重点应用。

本文简要介绍2024年初JetBrains PyCharm Community Edition (JetBrains PyCharm社区版)最新版本的安装使用，希望读者能够得心应手、高效流畅地开启您的Python开发之旅。

访问JetBrains官网：

<img src="https://img-blog.csdnimg.cn/direct/87d91bf6e4f644c0827b56b7b1a012c6.png" alt="在这里插入图片描述"> 点击导航栏上的 **Developer Tools** (开发者工具)菜单，选择**PyCharm**，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/b2204e49fd2549828155e1be500addd8.png" alt="在这里插入图片描述"> 点击进入PyCharm下载页面。

<img src="https://img-blog.csdnimg.cn/direct/a8d798a4aa85435aaebb3471edd06d85.png" alt="在这里插入图片描述"> 点击 **Download** 按钮，进入版本下载页面，有Professional（专业版，需要付费），也有Community（社区版，免费）。 此时滚动鼠标滚轮，向页面下方寻找社区版位置，如下所示： <img src="https://img-blog.csdnimg.cn/direct/e6ac536eaade4caba9e7d1a62c0d2df2.png" alt="在这里插入图片描述"> 我们看到页面中的 **PyCharm Community Edition** (PyCharm社区版)，点击**Download** 按钮下载。 <img src="https://img-blog.csdnimg.cn/direct/78566333139347318485996e2bfb5eba.png" alt="在这里插入图片描述"> Chrome浏览器开始下载软件包（如Chrome浏览器右上方下载记录）。同时，页面提示：如果没有开始，请direct link(直接链接)来下载。如下图所示。 <img src="https://img-blog.csdnimg.cn/direct/32605f7e287e4a648d3b908750c7a0be.png" alt="在这里插入图片描述"> 下载完毕后，找到Windows 10/11的 **下载** 文件夹里的最新版安装可执行文件 **pycharm-community-2023.3.2.exe**, 双击它启动安装向导。

#### 4. 安装最新版PyCharm Community Edition

启动PyCharm安装向导后，出现欢迎画面对话框Welcome to PyCharm Community Edition安装。 <img src="https://img-blog.csdnimg.cn/direct/655ed829abe148e686b065af9932f495.png" alt="在这里插入图片描述"> 点击 **下一步** 继续。 <img src="https://img-blog.csdnimg.cn/direct/bb56260c62c144e8a9902fe5d8898923.png" alt="在这里插入图片描述"> 由于之前安装过PyCharm,被系统检测到，因此，提示需要复选卸载之前的老版本，如上图所示。 <img src="https://img-blog.csdnimg.cn/direct/d91ae9d569e04b95a572ca7faf9f5346.png" alt="在这里插入图片描述"> 在 **Uninstall PyCharm Community Edition** (卸载PyCharm社区版)对话框中，复选两个选项，以卸载删除安装过的老版本。

<img src="https://img-blog.csdnimg.cn/direct/465d90a73d6543e981547a75e924446f.png" alt="在这里插入图片描述"> 如上图，卸载过程进行顺利。

<img src="https://img-blog.csdnimg.cn/direct/ba2ce5b84186403187b2477667f2867b.png" alt="在这里插入图片描述">

点击**Close**，完成卸载。 此时，安装向导继续。

<img src="https://img-blog.csdnimg.cn/direct/c96a649e01c24588892d4b3c614410ea.png" alt="在这里插入图片描述"> 按照默认安装目录，如上图所示，点击 **下一步** 继续。 <img src="https://img-blog.csdnimg.cn/direct/ec15d52da2f14499bc764cc9e691497e.png" alt="在这里插入图片描述"> 复选全部四项，其中包括 **添加“bin”文件夹到PATH**，这意味着环境变量自行添加，为安装后启动Python应用程序并运行它，提供了方便。

点击 **下一步** 继续。

<img src="https://img-blog.csdnimg.cn/direct/a7107c773636492e85b0a9be1192dc2c.png" alt="在这里插入图片描述"> 选择开始菜单文件夹，保持默认名称JetBrains，点击 **安装** 按钮继续。 <img src="https://img-blog.csdnimg.cn/direct/0e4683bf175f4ee4ae39cf54a768f60f.png" alt="在这里插入图片描述"> 进入安装过程，很快安装结束。

<img src="https://img-blog.csdnimg.cn/direct/f6d362015112475e8841b7e62eaaa09c.png" alt="在这里插入图片描述"> 安装向导结束，按照默认选项“否，我会在之后重新启动“，并点击完成推出向导。

#### 5. 用最新版PyCharm创建第一个Python应用程序！

安装完成，需要启动PyCharm来进行Python编程。

在Windows搜索栏，搜索PyCharm关键字，找到该程序，选择“以管理员身份运行启动PyCharm Community Edition 2023.3.2。

<img src="https://img-blog.csdnimg.cn/direct/3a3ffb21aa58447fbd357fc2af4a77ec.png" alt="在这里插入图片描述"> 这样，就启动了PyCharm Community Edition 2023.3.2版本，如下图：

<img src="https://img-blog.csdnimg.cn/direct/14e917379d8b4646900b48a93a166232.png" alt="在这里插入图片描述">

点击New Project, 创建一个新的项目（前提是已经在PyCharm之前安装了Python 3.12.1最新版）。 <img src="https://img-blog.csdnimg.cn/direct/bc060e0b73f143c7b6cc430d795d6a71.png" alt="在这里插入图片描述"> 按照默认的虚拟环境（Virtualenv）位置，以及默认的项目名称pythonProject1；系统已经自动识别了Python Version (Python版本)，即安装在D:\Python312的Python最新版3.12.1。 点击 **Create** 创建这个项目。

<img src="https://img-blog.csdnimg.cn/direct/5475f84ab82c4dc8956675fbcd67d865.png" alt="在这里插入图片描述"> 打开PyCharm的集成开发环境，如上图所示。

选择 File(文件)菜单 &gt; New &gt; Python file &gt; 输入新程序名 **hello_world.py**, 按Enter（回车），于是创建了第一个Python程序文件，如下图所示。

<img src="https://img-blog.csdnimg.cn/direct/1e5dd44a27684684a1600a9f30675c90.png" alt="在这里插入图片描述"> 在hello_world.py文件正文，写入最简单的程序语句：

```
print(“Hello, world!”)

```

也可添加一行注释，如下图所示。 <img src="https://img-blog.csdnimg.cn/direct/80fa25ccf4b245e7abbaeed39a19ba51.png" alt="在这里插入图片描述"> 点击运行按钮，程序得到结果：Hello, world! 运行成功！ 如下图所示： <img src="https://img-blog.csdnimg.cn/direct/c3c40e63e3214c90a746513290bf07e6.png" alt="在这里插入图片描述"> 现在，稍作修改，新建第二个Python应用程序hi.py，编写程序代码如下：

```
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello, {<!-- -->name}！')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	print_hi('World')

```

程序运行结果如下图： <img src="https://img-blog.csdnimg.cn/direct/3d77a37da26f4f7f8066db210150d13f.png" alt="在这里插入图片描述"> 可以看到，终端打印输出Hello, world! 说明Python程序运行成功！

接下来，就可以使用PyCharm为所欲为，来开发您所需要的各类应用程序了。

技术好文陆续推出，敬请关注。

喜欢就点赞哈！您的认可，我的动力。😊

#### 相关阅读：
1. 1. 1. 1. 