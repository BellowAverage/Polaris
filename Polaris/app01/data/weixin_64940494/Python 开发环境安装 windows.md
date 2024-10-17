
--- 
title:  Python 开发环境安装 windows 
tags: []
categories: [] 

---
        Python语言目前已经登顶编程语言的榜首了，主要原因在于Python 简单、易学、开发效率高，同时也在各行业中使用，例如AI人工智能，大数据分析，科学计算等领域。Python现在基本支持所有的操作系统了，今天我们主要演示一下windows下的安装流程。

        电脑环境：windows10 64位。

        安装python版本：3.10.6。

1. 先从Python官网中下载安装包，下载地址： 。目前最新的Python版本是3.10.6。

<img alt="" height="425" src="https://img-blog.csdnimg.cn/9e4737d12f564aaeb55087b23b8b433e.png" width="784">

点击下载到本机。

2. 找到刚刚下载的安装包点击右键&gt;以管理员身份运行，进入到安装流程。

<img alt="" height="261" src="https://img-blog.csdnimg.cn/79ee9e05969948a1879309324fea57ed.png" width="433">

3. 安装弹框中，勾选 Add Python 3.10.6 to PATH,勾选上后在安装完成时会自动添加好环境变量。然后选择  Customize installation（客户自定义安装），直接选择下一步。

<img alt="" height="410" src="https://img-blog.csdnimg.cn/43093f174c4e41208c2c04ea80148f73.png" width="667">

 4. 选择需要安装的路径，点击安装。<img alt="" height="411" src="https://img-blog.csdnimg.cn/c3244c3abe0b46f48acf271e5d5a402d.png" width="669">

 5. 安装完成的确认页面，点击 Disable path lenth limit (关闭路径的长度限制)。

<img alt="" height="414" src="https://img-blog.csdnimg.cn/45d0289bd2114b5e96989e5e005dff67.png" width="667">

6. 验证安装是否成功，进入到windows cmd，在输入python命令，如果会出现如下图显示python的版本则证明安装成功。

<img alt="" height="219" src="https://img-blog.csdnimg.cn/b8f7d7bcb7f64df0b12c3e1c01fb9334.png" width="825">

        刚刚我们在安装第一步时勾选了Add Python 3.10.6 to PATH，如果你没注意没有勾选上这个那么在命令行输入时则会提示没有python 这个命令，这时就需要手工添加环境变量。

        找到环境变量编辑页面，把python的安装路径添加到环境变量中。我这里是安装在F:\python3.10.6。

<img alt="" height="187" src="https://img-blog.csdnimg.cn/d174394abf1e4324a73abe206807ade0.png" width="513">

 配置完之后再cmd 再次输入 python 就能显示正常。
