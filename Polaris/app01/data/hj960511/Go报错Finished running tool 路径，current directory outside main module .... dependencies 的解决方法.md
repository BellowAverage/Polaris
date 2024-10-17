
--- 
title:  Go报错Finished running tool: 路径，current directory outside main module .... dependencies 的解决方法 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解go项目下，output报错：Finished running tool: C:\Program Files\Go\bin\go.exe build -o C:\Users\admin\AppData\Local\Temp\vscode-goCewfEl\go-code-check . current directory outside main module or its selected dependencies 的解决方法。 作者：任聪聪 日期：2023年4月19日 go版本：1.20.3、cursor0.2.5 


### 报错现象

idea中存在红标现象，并且在情况1和二中存在提示“current directory outside main module or its selected dependencies ”。 <img src="https://img-blog.csdnimg.cn/7727090235ff4caf88837509db19366e.png" alt="在这里插入图片描述">

#### 情况1，output下

<img src="https://img-blog.csdnimg.cn/94974d8f445b473583d1e8930d3fe1a0.png" alt="在这里插入图片描述">

#### 情况2，执行build时

<img src="https://img-blog.csdnimg.cn/c005123db21e4e9b8d5e310001a22091.png" alt="在这里插入图片描述">

### 原因一、目录问题

说明：存在汉字或特殊符号，笔者的不是这个问题，如果在您检查后发现目录中存在汉字或者特殊符号，那么建议优先剔除，使用英文再次执行命令尝试。

解决办法：修改文件目录为英文。

### 原因二、没有初始化项目

说明：没有使用命令进行初始化项目。

解决办法：`go mod init 你的目录`

<img src="https://img-blog.csdnimg.cn/e67efc08c04a4da2b27ae1f7b2844cfe.png" alt="在这里插入图片描述">

tips：这个命令会在目录下生成一个mod文件，不要删除，删除后还会报错。

### 解决后：

<img src="https://img-blog.csdnimg.cn/8a5338cc3e0940e9b4afde52e3dcdb7d.png" alt="在这里插入图片描述"> 不再提示红标。
