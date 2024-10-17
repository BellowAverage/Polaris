
--- 
title:  【Python】Windows如何在cmd中切换python版本 
tags: []
categories: [] 

---


#### 相信很多小伙伴都会有像我一样经历，在windows中装了很多python版本，那么如果我们正式使用的时候应该如何切换呢？
- - <ul><li>- - - - - - - 


>  
 （关注“测试开发自动化” 弓中皓，查看历史文章，获取更多知识） 


## 【方法一】从环境变量中切换python

这是我最喜欢用的方法，但是也是比较笨的一种方法，但是这种方法有一定的好处。

### 第一步： 打开环境变量

<img src="https://img-blog.csdnimg.cn/c968329c97ff443f86cb4b5d5db72158.png" alt="在这里插入图片描述">

### 第二步：打开系统变量中Path变量

<img src="https://img-blog.csdnimg.cn/9c86302215ff4c38b5572ebd3f6dc6f4.png" alt="在这里插入图片描述">

可以看到，目前我们3.6版本的python是置顶的，因此说明，目前如果在cmd中输入python使用的将是3.6版本的python，不信可以看下面： <img src="https://img-blog.csdnimg.cn/ec2c605a05be46e2a8a65ea71fe95bba.png" alt="在这里插入图片描述">

### 第三步：将你想使用的Python版本提前

<img src="https://img-blog.csdnimg.cn/a4c6192dc192480f8e94fcd8b4a7f22a.png" alt="在这里插入图片描述">

然后，点击<kbd>确定</kbd>并保存环境变量即可。 **【注意 】**：必须重新打开一个cmd，否则不会生效。

<img src="https://img-blog.csdnimg.cn/e85107e114cc448f8b824e7acd75b666.png" alt="在这里插入图片描述">

### 第四步：使用pip安装第三方库

为什么说这种方法好呢？就是因为这种方法可以使用<kbd>pip</kbd>非常方便（可以对比后面的方法）。 我们可以指定pip的版本来使用pip来安装第三方库： <img src="https://img-blog.csdnimg.cn/e9054651c5fa4aa4862f39a801048acb.png" alt="在这里插入图片描述"> 查看对应版本的第三方库：<kbd>pip3.9 list</kbd>

<img src="https://img-blog.csdnimg.cn/e64ef068429b460aad2fd04f525dfa04.png" alt="在这里插入图片描述">

## 【方法二】直接从cmd中任选python版本

使用这种方法的前提是需要对安装在根目录下的python做一定的修改

### 第一步：查看安装的python版本的路径

打开<kbd>cmd</kbd>，输入<kbd>where python</kbd>

<img src="https://img-blog.csdnimg.cn/aaee2be76855482e8a19f727c655edea.png" alt="在这里插入图片描述">

### 第二步：修改python.exe的版本号

我们要做的是将每个版本的<kbd>python.exe</kbd>文件修改为<kbd>python+版本号.exe</kbd> 以python3.9为例，我们将<kbd>C:\Users\mech-mind_lcl\AppData\Local\Programs\Python\Python39\python.exe</kbd> 路径下的<kbd>python.exe</kbd>文件修改为<kbd>python3.9.exe</kbd>

<img src="https://img-blog.csdnimg.cn/c36ecc7f4145451bbd773a5b62284706.png" alt="在这里插入图片描述">

### 第三步：使用对应的python版本

重新打开一个<kbd>cmd</kbd>，输入<kbd>python3.9</kbd> 即可使用对应的版本 <img src="https://img-blog.csdnimg.cn/ffb363befcd24288b3276ed658403add.png" alt="在这里插入图片描述">

### 第四步：使用pip安装第三方库

为什么说这种方式不好呢？ 是因为这种方式使用pip会报错。不信？你看： <img src="https://img-blog.csdnimg.cn/4a22b169e10f4eefa53f8f3693ad01f7.png" alt="在这里插入图片描述"> 所以，如果不适用pip的话，可以用这种办法。如果使用pip的话，我推荐大家使用第一种方法。
