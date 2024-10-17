
--- 
title:  【Java】Java编程相关 
tags: []
categories: [] 

---
## JDK安装

**Win11 + JDK17**
- JDK 官网：
**1.选择Java17、Windows 版本，下载 Installer：**

<img src="https://img-blog.csdnimg.cn/e7e8b6182d454c0f8fe89c957eb71d92.png#pic_center" alt="在这里插入图片描述"> **2.运行安装包**

**3.配置环境变量** ①【高级系统设置】 → 【环境变量】 → 【新建】系统变量

```
变量名：JAVA_HOME
变量值：（JDK安装路径）

```

<img src="https://img-blog.csdnimg.cn/bd6d10a53af14b42a43472f71fb2f64c.png" alt="在这里插入图片描述">

②【编辑】系统变量下的【PATH】/【Path】变量，【新建】：

```
%JAVA_HOME%\bin

```

<img src="https://img-blog.csdnimg.cn/f0a4ef39aa6d427e92cdebc08b890d9f.png" alt="在这里插入图片描述">
- 这个操作让系统在任何路径下都可以识别java、javac等命令
**4.测试安装是否成功** cmd（win + R）中输入：

```
java -version

```

<img src="https://img-blog.csdnimg.cn/4b8f460d22b647cda637206c735ee575.png" alt="在这里插入图片描述">

```
javac

```

<img src="https://img-blog.csdnimg.cn/2b11825d35db4e4190fb52861ddd1de9.png" alt="在这里插入图片描述">

```
java

```

<img src="https://img-blog.csdnimg.cn/b59c0ef87ff147638f49af9c8f900abd.png" alt="在这里插入图片描述">

## 问题记录

### JDK安装问题

#### 1.cmd 中输入javac、java 无输出（在安装目录中正常输出）：

**在系统变量 Path 中将 新增JDK <strong>上移**至最上方</strong>
- 我认为这样做的原因是 Path 中本身存在一个 javapath，所以准确来说，只要上移到原本的这个路径之上就好了： <img src="https://img-blog.csdnimg.cn/7b5844d1237f476eb6f8f9923178ed24.png#pic_center" alt="在这里插入图片描述">
#### 2.JDK17 之后版本无 jre：

**运行指令：**

```
 bin\jlink.exe --module-path jmods --add-modules java.desktop --output jre

```

### 编程相关问题
