
--- 
title:  Ubuntu安装指定Python版本详解，理论上各版本通用 
tags: []
categories: [] 

---
>  
 此方法理论上讲适用于所有<font color="OrangeRed" size="3">**Ubuntu**</font>版本（可能太老的不行）本文章中写的是<font color="OrangeRed" size="3">**18.04**</font>的，之前我在<font color="OrangeRed" size="3">**16.04**</font>，<font color="OrangeRed" size="3">**20.04**</font>上均安装成功 




#### 文章目录
- <ul><li>- - - - <ul><li>- 


我们首先查看一下当前系统自带的<font color="OrangeRed" size="3">**Python**</font>版本及指向：

```
ls -l /usr/bin | grep python

```

<img src="https://img-blog.csdnimg.cn/f4d50fe05ea346e6a899d1a98e08c1d4.png" alt="请添加图片描述">

从上图可以看出是我们输入<font color="OrangeRed" size="3">**python3**</font>指向的是<font color="OrangeRed" size="3">**Python3.6**</font>的版本

我们再输入条命令：<font color="OrangeRed" size="3">**`python3`**</font> 试试：

<img src="https://img-blog.csdnimg.cn/54bab4f7617b4d268b6d1d269b49a4e9.png" alt="请添加图片描述">

就进入了<font color="OrangeRed" size="3">**Python**</font>命令行运行方式，可以看到我们的<font color="OrangeRed" size="3">**Python**</font>具体版本为<font color="OrangeRed" size="3">**3.6.9**</font>的，然后我们输入：<font color="OrangeRed" size="3">**`exit();`**</font> 然后回车就退出了命令行运行方式

### 下载Python

下载链接：

自己找到需要的版本（我这里以安装<font color="OrangeRed" size="3">**3.8.5**</font>版本为例子）

往里面翻找到这个就好了哈

<img src="https://img-blog.csdnimg.cn/ec1824e3237e4d81bc7ae6070b40b2fd.png" alt="请添加图片描述">

在<font color="OrangeRed" size="3">**Ubuntu**</font>里我们需要下载安装<font color="OrangeRed" size="3">**Python**</font>到自己指定的路径（我这里直接在当前用户目录下了：<font color="OrangeRed" size="3">**`cd ~`**</font>）

然后我们复制刚刚自己需要的版本的下载链接，在<font color="OrangeRed" size="3">**Ubuntu**</font>里输入命令：

```
sudo wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz

```

<img src="https://img-blog.csdnimg.cn/889a95bdc2d44f968257f3efe71a0547.png" alt="请添加图片描述">

### 安装Python（方法一：默认安装路径）

解压安装包到当前目录下并且进入：

```
sudo tar -zxvf Python-3.8.5.tgz -C ~
cd Python-3.8.5

```

然后我们进行初始化：

```
sudo ./configure

```

>  
 **注意！** 
 如果你输入这条命令后出现下图错误的： 
 <img src="https://img-blog.csdnimg.cn/a6eb513439084ca19687a1ede71bf6be.png" alt="请添加图片描述"> 
 输入以下命令安装一下编译环境： 
 <pre><code class="prism language-shell">sudo apt-get install zlib1g-dev libbz2-dev libssl-dev libncurses5-dev  libsqlite3-dev libreadline-dev tk-dev libgdbm-dev libdb-dev libpcap-dev xz-utils libexpat1-dev   liblzma-dev libffi-dev  libc6-dev
</code></pre> 
 如果这里没报错，而是后面make编译的时候报错的话，也一样输入这条命令即可解决 


完成后再编译测试安装：（其实<font color="OrangeRed" size="3">**`sudo make test`**</font>这条不输入也没事，只是测试一下，而且这条时间比较久，可能要用5-20分钟，后面安装不成功的时候再输入查看问题也行）

```
sudo make
sudo make test
sudo make install

```

好了，安装完了

>  
 小提示：这时候<font color="OrangeRed" size="3">**Python**</font>已经安装完成，可执行文件在/usr/local/bin下，库文件在/usr/local/lib下，配置文件在/usr/local/include下，其他资源文件在/usr/local/share下，大家用<font color="OrangeRed" size="3">**Pycharm**</font>等编辑器使用<font color="OrangeRed" size="3">**Python**</font>时就用这些路径 


此时你会发现，我们输入命令：<font color="OrangeRed" size="3">**`python3`**</font> 还是出现的<font color="OrangeRed" size="3">**python3.6.9**</font>，但是你试着尝试输入：<font color="OrangeRed" size="3">**`python3.8`**</font> 出现的就是我们刚刚安装的<font color="OrangeRed" size="3">**python3.8.5**</font>版本

<img src="https://img-blog.csdnimg.cn/42e33920993c4bbc9eadfbd17b439963.png" alt="请添加图片描述">

<font color="OrangeRed" size="3">**<strong>（欲知后事如何，请翻到本文最后，现在讲第二种安装方法）**</strong></font>

### 安装Python（方法二：自定义安装路径）

这里按同样，解压安装包到当前目录下并且进入：

```
sudo tar -zxvf Python-3.8.5.tgz -C ~
cd Python-3.8.5

```

然后我们进行和方法一不一样的初始化：

```
./configure --prefix=/usr/local/python3.8.5

```

>  
 解释：<font color="OrangeRed" size="3">**`--prefix`**</font>后面的参数为指定安装路径 
 注意：如果这里初始化有问题则与方法一的解决方式一样 


后面和上面方法一安装过程一样，完成后再编译测试安装：

```
sudo make
sudo make test
sudo make install

```

然后我们需要添加一下环境变量：

```
PATH=$PATH:$HOME/bin:/usr/local/python3.8.5/bin

```

好了，安装完了（大家可以输入：<font color="OrangeRed" size="3">**`echo $PATH`**</font> 查看一下环境变量有没有添加进去）

>  
 小提示：这时候<font color="OrangeRed" size="3">**Python**</font>已经安装完成，可执行文件在/usr/local/python3.8.5/bin下，库文件在/usr/local/python3.8.5/lib下，配置文件在/usr/local/python3.8.5/include下，其他资源文件在/usr/local/python3.8.5/share下，大家用<font color="OrangeRed" size="3">**Pycharm**</font>等编辑器使用<font color="OrangeRed" size="3">**Python**</font>时就用这些路径 


然后就和方法一的问题一样，我们输入命令：<font color="OrangeRed" size="3">**`python3`**</font> 还是出现的<font color="OrangeRed" size="3">**python3.6.9**</font>，但是你试着尝试输入：<font color="OrangeRed" size="3">**`python3.8`**</font> 出现的就是我们刚刚安装的<font color="OrangeRed" size="3">**python3.8.5**</font>版本，接下来讲更新<font color="OrangeRed" size="3">**Python**</font>默认指向

### 更新命令‘python’默认指向为我们所安装的版本

我们回到本文最开头的查看<font color="OrangeRed" size="3">**Python**</font>指向命令：

```
ls -l /usr/bin | grep python

```

因为我们现在啥也没设置，所以输入了还是和上面显示的一样，然后我们现在有两种情况：
1. 你安装的是对应你这个系统的<font color="OrangeRed" size="3">**Python**</font>当前版本号1. 你安装的是其他<font color="OrangeRed" size="3">**Python**</font>版本号
>  
 什么是<font color="OrangeRed" size="3">**Python**</font>当前版本号，什么是其他版本号？ 
 现在以我这里为例，我们从下图可得： 
 <img src="https://img-blog.csdnimg.cn/45710df0984a4ca395bee458cca884c9.png" alt="请添加图片描述"> 
 我们输入命令：<font color="OrangeRed" size="3">**`python3`**</font> 对应的版本为<font color="OrangeRed" size="3">**python3.6.9**</font>，那么，我们安装的版本如果是<font color="OrangeRed" size="3">**python3.6.11**</font>，或者是<font color="OrangeRed" size="3">**python3.6.5**</font>啥的，只要是在这个<font color="OrangeRed" size="3">**3.6**</font>的版本内就是**当前版本号**，本文安装的版本号为<font color="OrangeRed" size="3">**3.8**</font>，所以安装的是其他版本号 


两种情况有不同的更新指向方式：

#### 方式一：当前版本号直接将指向链接更新

删除原有链接：

```
sudo rm /usr/bin/python

```

建立新链接：

```
sudo ln -s /usr/bin/python3.8 /usr/bin/python3
sudo ln -s /usr/bin/python3.8 /usr/bin/python

```

>  
 解释：当中的<font color="OrangeRed" size="3">**python3.8**</font>就是我们上面在输入<font color="OrangeRed" size="3">**python3.8**</font>的时候就出现我们安装的<font color="OrangeRed" size="3">**python3.8.5**</font>的版本嘛，然后这里改为输入<font color="OrangeRed" size="3">**python3**</font>和<font color="OrangeRed" size="3">**python**</font>都指向我们的<font color="OrangeRed" size="3">**python3.8.5**</font> 


然后输入<font color="OrangeRed" size="3">**`python3`**</font>或者<font color="OrangeRed" size="3">**`python`**</font>就会发现已经好了，方式二就不用再进行了

#### 方式二：指向其他版本号

因为我们安装的<font color="OrangeRed" size="3">**Python3.8**</font>是不同于系统自带<font color="OrangeRed" size="3">**python**</font>的版本号，不在/usr/bin下而在/usr/local/bin或者/usr/local/python3.8.5/bin下（取决于前面执行的是<font color="OrangeRed" size="3">**`./configure`**</font>还是<font color="OrangeRed" size="3">**`./configure --prefix=/usr/local/python3.8.5`**</font>，因此需要先加一条软链接并且把之前的<font color="OrangeRed" size="3">**python**</font>命令改为<font color="OrangeRed" size="3">**python.bak**</font>，同时<font color="OrangeRed" size="3">**pip**</font>也需要更改

**若<font color="OrangeRed" size="3"><strong>Python3.8**</font>安装时，执行的是<font color="OrangeRed" size="3">**`./configure`**</font>，则依次输入</strong>：

```
# 将原python与python3命令改为python.bak与python.bak
sudo mv /usr/bin/python /usr/bin/python.bak
sudo mv /usr/bin/python3 /usr/bin/python3.bak
# 将我们刚装的python3.8.5指定运行命令为python与python3
sudo ln -s /usr/local/bin/python3 /usr/bin/python
sudo ln -s /usr/local/bin/python3 /usr/bin/python3
# 将原pip和pip3命令改为pip.bak与pip3.bak
sudo mv /usr/bin/pip /usr/bin/pip.bak
sudo mv /usr/bin/pip3 /usr/bin/pip3.bak
# 将我们刚装的python3.8.5的pip指定运行命令为pip与pip3
sudo ln -s /usr/local/bin/pip3 /usr/bin/pip
sudo ln -s /usr/local/bin/pip3 /usr/bin/pip3

```

>  
 注意：如果你的系统不自带<font color="OrangeRed" size="3">**Python2**</font>，则第一句与第五句命令会报错，或者你的系统不自带<font color="OrangeRed" size="3">**Python3**</font>，则第二句与第六句命令会报错，<font color="OrangeRed" size="3">**pip**</font>也一样，这是正常的，不用理会，报错内容如下（报错意思其实就是你没有这个）： 
 <img src="https://img-blog.csdnimg.cn/cebe4c8894004ed6a58e1198117aa518.png" alt="请添加图片描述"> 
 上面的思路梳理一下： 
 更改完成之后，现在输入<font color="OrangeRed" size="3">**`python`**</font>或者是<font color="OrangeRed" size="3">**`python3`**</font>将会指向<font color="OrangeRed" size="3">**python3.8.5**</font> 
 输入<font color="OrangeRed" size="3">**`python.bak`**</font>或者是<font color="OrangeRed" size="3">**`python3.bak`**</font>将会分别指向系统自带的<font color="OrangeRed" size="3">**python2**</font>与<font color="OrangeRed" size="3">**python3**</font> 
 输入<font color="OrangeRed" size="3">**`pip`**</font>或者是<font color="OrangeRed" size="3">**`pip3`**</font>将会指向<font color="OrangeRed" size="3">**python3.8.5**</font>的将会指向<font color="OrangeRed" size="3">**pip**</font> 
 输入<font color="OrangeRed" size="3">**`pip.bak`**</font>或者是<font color="OrangeRed" size="3">**`pip3.bak`**</font>将会分别指向系统自带的<font color="OrangeRed" size="3">**python2**</font>与<font color="OrangeRed" size="3">**python3**</font>的<font color="OrangeRed" size="3">**pip**</font> 


**若<font color="OrangeRed" size="3"><strong>Python3.8**</font>安装时，执行的是<font color="OrangeRed" size="3">**`./configure --prefix=/usr/local/python3.8.5`**</font>，则依次输入</strong>：

```
# 将原python与python3命令改为python.bak与python.bak
sudo mv /usr/bin/python /usr/bin/python.bak
sudo mv /usr/bin/python3 /usr/bin/python3.bak
# 将我们刚装的python3.8.5指定运行命令为python与python3
sudo ln -s /usr/local/python3.8.5/bin/python3.8 /usr/bin/python
sudo ln -s /usr/local/python3.8.5/bin/python3.8 /usr/bin/python3
# 将原pip和pip3命令改为pip.bak与pip3.bak
sudo mv /usr/bin/pip /usr/bin/pip.bak
sudo mv /usr/bin/pip3 /usr/bin/pip3.bak
# 将我们刚装的python3.8.5的pip指定运行命令为pip与pip3
sudo ln -s /usr/local/python3.8.5/bin/pip3 /usr/bin/pip
sudo ln -s /usr/local/python3.8.5/bin/pip3 /usr/bin/pip3

```

这里的话呢，上面已经解释过了

好啦，这篇教程到这结束了，如果还有啥不懂的在评论区留言或者私信都可以
