
--- 
title:  《软件安装与使用教程》— Git 在Windows的安装教程 
tags: []
categories: [] 

---


#### 目录
- - <ul><li>- - - - <ul><li>- - - - - - - - - - - - - - - 


## Git在Windows安装教程

### 1 获得安装包

本文提供Windows 64bit下载链接：

或2贰进制公众号获取

>  
 或者在文末公众号下载 


也可以在官网下载安装包，下载速度较慢，下载地址： 

根据操作系统选择，本文以Windows 64bit为例 <img src="https://img-blog.csdnimg.cn/direct/42b3e41901f54951abf538496731e3ca.png#pic_center" alt="在这里插入图片描述" width="600"> 根据系统选择32或者64bit <img src="https://img-blog.csdnimg.cn/direct/eff65b5b63ee4127a8c37fe500d34761.png" alt="在这里插入图片描述">

### 2 解压文件

打开下载链接，下载提供的压缩包，解压后获得下图文件

### 3 注意事项

1、该安装包对Windows操作系统适用 2、安装包大小约50M，下载路径磁盘空间余量需满足 3、安装后约700M，C盘空间不够的话，不推荐安装到C盘

### 4 安装步骤

#### 4.1 运行安装程序

#### 4.2 声明许可

**点击Next** <img src="https://img-blog.csdnimg.cn/direct/9abfe8c2a1954aacb3b2c2f3bf8e8577.png#pic_center" alt="在这里插入图片描述" width="500">

#### 4.3 选择安装路径

选择安装路径，C盘空间不足的，建议安装到其他位置，安装路径不要有中文字符 完成后，**点击Next** <img src="https://img-blog.csdnimg.cn/direct/75321a2a558c423ab6951ef9bd3f6f74.png#pic_center" alt="在这里插入图片描述" width="500">

#### 4.4 选择需要安装的组件

选择需要安装的组件，根据需求选择，这里默认，**点击Next** <img src="https://img-blog.csdnimg.cn/direct/25f1a3c208514e9d92bffafba296f125.png#pic_center" alt="在这里插入图片描述" width="500">

#### 4.5 选择开始菜单

选择开始菜单文件夹，如不需要创建开始菜单文件夹，勾选上复选框， 此处按照默认，**点击Next** <img src="https://img-blog.csdnimg.cn/direct/a2621e9457c649b299e7edac49a95bf9.png#pic_center" alt="" width="500">

#### 4.6 选择默认编辑器

选择哪一个作为Git的默认编辑器，Windows系统按照建议，选择第一个Vim就好， **点击Next** <img src="https://img-blog.csdnimg.cn/direct/71df7ecb75074f68b29f6c9debf28e64.png#pic_center" alt="在这里插入图片描述" width="500"> <img src="https://img-blog.csdnimg.cn/direct/cb155a27624648e3bcf2242082de6387.png#pic_center" alt="在这里插入图片描述" width="500">

#### 4.7 选择PATH环境

此处按照建议，选择第二个选项：Git从命令行和第三方软件，**点击Next**

第一个：只使用Git Bash中的Git。这是最谨慎的选择，因为您的路径根本不会被修改，只能使用Git命令行工具Git Bash。

第二个：来自命令行和第三方软件的Git 该选项是推荐的，只向PATH添加一些最小的Git包装器，以避免使用可选的Unix工具，您将能够使用Git来自Git Bash、命令提示符和PowerShell以及任何第三方软件寻找Git的路径。

第三个：使用命令PromptBothGit中的Git和可选Unix工具，并将可选的Unix工具添加到PATH中。Warning：这将覆盖Windows工具，如“find”和“Sort”。只有当你理解它的含义时，才使用这个选项。 <img src="https://img-blog.csdnimg.cn/direct/8c5a043d3d7d4f879c0f3550cb52cace.png#pic_center" alt="在这里插入图片描述" width="500">

#### 4.8 选择HTTPS后端传输

此处一般按照默认选择第一个选项，**点击Next**

第一个：使用OpenSSL库，服务器证书将使用ca-bundle.crt文件进行验证；

第二个：是使用本地Windows安全通道库。服务器证书将使用Windows证书存储进行验证，还允许使用公司的内部根CA证书，例如通过ActiveDirectory域服务分发的 <img src="https://img-blog.csdnimg.cn/direct/fc52c288fcac43ce8ffa59b116976be1.png#pic_center" alt="在这里插入图片描述" width="500">

#### 4.9 配置行尾巴符转换

设置Git怎样处理文本文件中的行末符，默认第一个选项，**点击Next**

第一个：签出Windows样式，提交Unix样式的行尾。建议在Windows上选择该选项。

第二个：提交文本文件，CRLF将被转换为LF。对于跨平台项目，建议在Unix上选择该选项。

第三个：按照原样提交。当签出或提交文本文件时，git将不会执行任何转换。对于跨平台项目，不建议选择该选项。 <img src="https://img-blog.csdnimg.cn/direct/43b660227cbd4547a326de02721cccd0.png#pic_center" alt="在这里插入图片描述" width="500">

#### 4.10 配置Git Bash终端仿真器

默认选择第一个选项，**点击Next**

第一个： 使用MinTTY(MSYS2的默认终端)。 Git Bash将使用MinTTY作为终端仿真器，它具有可调整大小的窗口、非矩形选择和Unicode字体。Windows控制台程序(suchas交互式Python)必须通过“winpty”启动才能在MinTTY中工作。

第二个：使用Windows的默认控制台窗口。 Git将使用Windows的默认控制台窗口(“cmd.exe”)，该窗口适用于Win 32控制台程序，如交互式Python或node.js，但其默认回滚功能非常有限，需要配置为使用Unicode字体才能正确显示非ASCII字符，而在Windows 10之前，它的窗口不能自由调整大小，只允许矩形文本选择。 <img src="https://img-blog.csdnimg.cn/direct/f3bf3851eb55444ca582a43d8a26a65c.png#pic_center" alt="在这里插入图片描述" width="500">

#### 4.11 选择 git pull的默认操作

选择git pull的默认操作，此处默认选择第一个，**点击Next**

第一个：默认的(快进或合并)，这是“git pull”的标准行为，如果可能的话，将当前分支快速转发到获取的分支，否则将创建合并提交。

第二个：将当前分支重新定位到获取的分支上。如果没有要重基的本地提交，这相当于快速转发。

第三个：快进到提取的分支。如果不可能，则失败。 <img src="https://img-blog.csdnimg.cn/direct/ede08cdbdaa34a3982dcefc97926e006.png#pic_center" alt="在这里插入图片描述" width="500">

#### 4.12 配置额外选项

配置额外的选项，此处按照默认，选择第一个和第二个，**点击Next**

第一个：启用文件系统缓存。文件系统数据将大容量读取，并缓存在内存中以进行确定操作(“core.fscache”设置为“true”)，这将大大提高性能。

第二个：启用Git凭据管理器。Windows的Git凭据管理器为Windows提供安全的Git凭据存储，最显著的是对VisualStudioTeam服务和GitHub的多因素身份验证支持(需要.NET Framework v4.5.1或更高版本)。

第三个：启用符号链接。启用符号链接(需要SeCreateSymbolicLink权限)。请注意，现有存储库不受此设置的影响。

<img src="https://img-blog.csdnimg.cn/direct/2006c43b9e3c4af8b789845f979c60ef.png#pic_center" alt="在这里插入图片描述" width="500">

#### 4.13 配置实验选项

此处选择实验选项，按照默认，不勾选，**点击Install**

是否启用对伪控制台的实验支持。(新的！)这允许在gitBash窗口中运行本地控制台程序，如Node或Python，而无需使用winpty，但它仍存在已知的bug。

<img src="https://img-blog.csdnimg.cn/direct/8bdf9c31ffe64d24a8d630f1fb2e8088.png#pic_center" alt="在这里插入图片描述" width="500">

#### 4.14 开始安装

等待安装完成 <img src="https://img-blog.csdnimg.cn/direct/78a1249906674aac9ef6a9964e8a93b5.png#pic_center" alt="在这里插入图片描述" width="500">

#### 4.15 安装完成

安装完成，**点击Next** <img src="https://img-blog.csdnimg.cn/direct/1c9cfb84541e4387b228fa6a9841f9ad.png#pic_center" alt="在这里插入图片描述" width="500">

### 5 验证测试

#### 5.1 运行软件

打开Win开始菜单，打开Git Bash <img src="https://img-blog.csdnimg.cn/direct/2e7a44b5d4c441e09be00f58c57ed7be.png#pic_center" alt="在这里插入图片描述" width="300">

<img src="https://img-blog.csdnimg.cn/direct/b8984741a35a446b916c2250972c2d9d.png#pic_center" alt="在这里插入图片描述" width="500">

更多内容，点击如下公众号，查看获取
