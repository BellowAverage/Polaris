
--- 
title:  刚学Python，遇到No Python Interpreter configured for the project，怎么解决? 
tags: []
categories: [] 

---
### 欢迎关注公众号【Python开发实战】，免费领取Python、PyCharm安装教程和Python学习电子书！

### 刚学Python，你肯定遇到过这个问题

刚学Python时，拿到一个Python项目，想用pycharm打开运行，pycharm界面却显示`No Python Interpreter configured for the project`，翻译一下是：没有为项目配置Python解释器。

<img src="https://img-blog.csdnimg.cn/img_convert/e700e8b2b11d20836890452f7503ac7e.png" alt="image-20220517172553174">

解决这个问题也很简单，只需要为当前打开的这个Python项目配置一个Python解释器即可，具体操作如下：
1.  在显示的`No Python Interpreter configured for the project`一栏的右侧，点击`Configure Python Interpreter`，进入Python解释器配置页面。也可以直接打开pycharm的settings页面，找到Project下的Python Interpreter，进入Python解释器配置页面。 <img src="https://img-blog.csdnimg.cn/img_convert/a8b1059ef6b565e47e9d8bce3381f38f.png" alt=""> 1.  在Python解释器配置页面，可以看到No Interpreter，即没有Python解释器。点击后面的齿轮按钮，会出现两个选项：Add和 Show All。Add是添加一个新的Python解释器环境，Show All是展示所有已经添加过的Python解释器环境。 <img src="https://img-blog.csdnimg.cn/img_convert/13ee4c1ae6012019a3be09f5a226e1ef.png" alt=""> 下图是点击Show All的界面，由于没有已经添加过的Python解释器环境显示nothing to show，可以点击右侧的`+`，添加一个新的Python解释器环境。如果添加过Python解释器环境，则会列出所有已经添加过的Python解释器环境。添加过的Python环境中，如果有某一个已经安装了要运行的项目的所有依赖包，则可以直接选择它。 <img src="https://img-blog.csdnimg.cn/img_convert/7f20c4b8165b18bdf80fb899c48f4a10.png" alt="image-20220606213502324"> <li> 添加新的Python解释器环境的界面如下图所示，点击第一步中的齿轮按钮，再点击Add可进入该页面。在Show All的界面点击右侧的`+`也可以进入该页面。 <img src="https://img-blog.csdnimg.cn/img_convert/4dbe95ffd04c79afdffda796fc601182.png" alt=""> 在添加新的Python解释器环境的界面中，左侧是选择要添加一个什么样的Python环境，右侧是对应的配置选项。简单介绍一下常用的前三种： 
  <ul><li> Virtualenv Environment：使用Python第三方包virtualenv管理的虚拟环境，有新建虚拟环境和选择已经存在的虚拟环境两个选项。virtualenv是能管理Python虚拟环境的第三方库，详情可查看这篇文章—— 
    1. 选择新建虚拟环境时，需要设置虚拟环境的存储路径（最好不要包含中文和空格），还需要设置基础的Python解释器，一般是系统Python解释器或者Anaconda的Python解释器，但是要确保基础的Python解释器中已经安装了virtualenv。Inherit global site-packages是继承全局环境里面的包，不勾选。Make available to all projects是所有的项目都可以用这个环境，可选也可不选。1. 选择已经存在的虚拟环境时，点击`...`选择virtualenv已经创建的虚拟环境中`python.exe`的路径即可。 </li><li> Conda Environment：使用conda管理的虚拟环境，同样也有新建虚拟环境和选择已经存在的虚拟环境两个选项。了解**conda**可以查看这篇文章—— 
    1. 选择新建虚拟环境时，需要设置虚拟环境的存储路径（最好不要包含中文和空格），还可以选择新建的虚拟环境中python的版本，因为conda把python也看成是一个包。如果安装了Anaconda，Conda executable会默认是conda的路径，不用动。Make available to all projects是所有的项目都可以用这个环境，可选也可不选。1. 选择已经存在的虚拟环境时，点击`...`选择conda已经创建的虚拟环境中`python.exe`的路径即可。Conda executable也不用动。 <img src="https://img-blog.csdnimg.cn/img_convert/38d307de1f9409a802a97642b2c53d7f.png" alt=""> </li>1.  System Environment：使用系统Python解释器环境，可以是从Python官网下载安装包后安装的python.exe路径，安装教程：。也可以是安装Anaconda后python.exe的路径，安装教程：。 <img src="https://img-blog.csdnimg.cn/img_convert/380e6bf95ed9e82107499df64bc6c8ef.png" alt=""> </ul> </li>1.  不论选择添加的是一个什么样的Python环境，添加成功后就会在Show All页面显示，选中这个已经添加成功的Python环境，再点击OK，即为现在打开的项目配置了Python解释器环境。 <img src="https://img-blog.csdnimg.cn/img_convert/20973a7ed8b8d4af9bec9f8a54e5249e.png" alt=""> 1.  现在可以查看一下Python解释器配置页面，不再显示No Interpreter，而是对应显示刚刚添加的Python环境。在该环境中，安装好项目所有的依赖包后就可以运行项目了！ <img src="https://img-blog.csdnimg.cn/img_convert/20429708f4c26adfde9877efd6a8aca0.png" alt=""> - 选择新建虚拟环境时，需要设置虚拟环境的存储路径（最好不要包含中文和空格），还可以选择新建的虚拟环境中python的版本，因为conda把python也看成是一个包。如果安装了Anaconda，Conda executable会默认是conda的路径，不用动。Make available to all projects是所有的项目都可以用这个环境，可选也可不选。- 选择已经存在的虚拟环境时，点击`...`选择conda已经创建的虚拟环境中`python.exe`的路径即可。Conda executable也不用动。
如果这篇内容对你有所帮助，欢迎**点赞，收藏，在看，转发**，让更多的小伙伴也能看到哦~
