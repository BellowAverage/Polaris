
--- 
title:  Android Studio生成aar并导入使用 
tags: []
categories: [] 

---
### aar简单介绍

aar是安卓的库文件，与java的jar包区别在于aar可包含资源文件而jar包不行。类似于MFC的AppWizard[dll]。

### 生成步骤

#### 1、右键选择工程New Moulde

<img src="https://img-blog.csdn.net/20161118141042838" alt="这里写图片描述" title="">

#### 2、选择Android Library

<img src="https://img-blog.csdn.net/20161118141153511" alt="这里写图片描述" title="">

#### 3、编写库文件

在这里笔者随便写了个view，并画成红色的。  <img src="https://img-blog.csdn.net/20161118141455121" alt="这里写图片描述" title="">

#### 4、编译工程
- 生成debug的aar  最好是rebuild一下，编译完成后aar就在lib的build/outputs下生成了。  <img src="https://img-blog.csdn.net/20161118141828730" alt="这里写图片描述" title=""><li>生成release的aar  
  <ul>- 点击generate signed apk可生成release版本的aar<li>选择compile方式生成realease版本的aar  
    <ul>- 进入moulde setting界面  <img src="https://img-blog.csdn.net/20161121175814175" alt="这里写图片描述" title="">- 添加moudle依赖  <img src="https://img-blog.csdn.net/20161121180034535" alt="这里写图片描述" title="">- 选择编译方式  <img src="https://img-blog.csdn.net/20161121180122895" alt="这里写图片描述" title="">- 编译工程  可看到多出了一个realse版本的aar  <img src="https://img-blog.csdn.net/20161121180324661" alt="这里写图片描述" title="">
### 导入步骤

#### 1、右键选择工程New Moulde

为了避免混淆笔者新建了一个工程。重复生成步骤中的New Moudle步骤

#### 2、拷贝aar

将刚才生成的aar复制后粘贴在新工程的libs文件夹下。  <img src="https://img-blog.csdn.net/20161118142246798" alt="这里写图片描述" title="">

#### 3、选择import JAR/.AAR Package

<img src="https://img-blog.csdn.net/20161118142122297" alt="这里写图片描述" title="">

#### 4、选择路径

选择我们刚才拷贝过来的aar，选择完成后系统会自动帮我们填写那两行东西。  <img src="https://img-blog.csdn.net/20161118142648585" alt="这里写图片描述" title="">

#### 5、导入成功

<img src="https://img-blog.csdn.net/20161118142847572" alt="这里写图片描述" title="">

#### 6、测试

刚才笔者写了个view，我们在layout文件中添加这个自定义view  <img src="https://img-blog.csdn.net/20161118143554147" alt="这里写图片描述" title="">  可见布局中添加了这个红色的view。

### 结束

这就是生成一个aar 和导入aar的步骤。  参考代码: 
