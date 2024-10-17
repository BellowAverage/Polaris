
--- 
title:  2024最新版TypeScript安装使用指南 
tags: []
categories: [] 

---
## 2024最新版TypeScript安装使用指南

### Installation and Development Guide to the Latest TypeScript in 2024

By Jackson@ML

#### 1. 什么是TypeScript?

>  
 TypeScript is JavaScript with syntax for types. – typescriptlang.org 

- TypeScript 是 JavaScript 的一个超集，支持 ECMAScript 6 标准。- TypeScript 由微软开发的自由和开源的编程语言。- TypeScript 设计目标是开发大型应用，它可以编译成纯 JavaScript，编译出来的JavaScript 可以运行在任何浏览器上。
#### 2. 获取最新版TypeScript

打开Chrome浏览器，访问TypeScript官网链接： ，如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/d65d879b994544029c5f7bdbb0fabb5a.png" alt="在这里插入图片描述"> 点击主页面链接Try TypeScript Now, 进入下载页面。

<img src="https://img-blog.csdnimg.cn/direct/b0efd8bca38646ff802526c461d480ef.png" alt="在这里插入图片描述"> 出现两个选项： 1） In your browser, 在浏览器中使用，意思是在线使用及开发； 2） On your computer，在计算机中使用，意思是离线在电脑中自行开发。 笔者选择右侧第二项，点击On your computer按钮。

<img src="https://img-blog.csdnimg.cn/direct/23728d89f9e8422d9c8ec846466d3e51.png" alt="在这里插入图片描述">

#### 3. 安装TypeScript

进入到下载页面，仍有两种方式： 选择 使用npm包安装；（另一种方式，采用Visual Studio, 但是该IDE软件较为庞大，对于初学者或者学生，npm安装就足够了）

运行以下命令：

```
npm install typescript --save-dev

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/2767c021b2c24305837671d4e6e96285.png" alt="在这里插入图片描述"> 或者，运行以下命令：

```
npm -g install typescript

```

安装完毕后，运行命令验证typescript版本：

```
tsc –version

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/8866fc363404400fae04e58d2cc914f3.png" alt="在这里插入图片描述"> 结果显示，TypeScript最新版本5.3.3安装完毕！

#### 4. 用Visual Studio Code编程实现

打开Visual Studio Code, 打开专门为开发TypeScript程序创建的文件夹myTypeScript\Lesson\Tutorial。

创建一下新的页面文件index.html, 在代码中，使用！ + tab组合键，创建一个HTML文件草稿，如下图所示： <img src="https://img-blog.csdnimg.cn/direct/cce47b45afe941fd94d95253304ac5d4.png" alt="在这里插入图片描述"> 按tab键后，出现完整的HTML页面标记。修改title标签为A TypeScript Sample, 然后调整页面tag, 保存该HTML文件，后续步骤如下所示。

##### 1） 创建HTML文件

本章节创建了文件夹，例如：存放HTML文件路径为 D:\myTypeScript\Lesson\Tutorial, 新建index.html, 代码如下：

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;A TypeScript Sample&lt;/title&gt;
     
    &lt;script type="text/javascript" src="main.ts"&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body style="background-color: lightyellow;"&gt;
    &lt;h1 style="color: red"&gt;Welcome Jackson's TypeScript Tutorial!&lt;/h1&gt;    
&lt;/body&gt;
&lt;/html&gt;

```

#### 2） 创建CSS文件

在当前目录关联了一个CSS文件styles.css, 如下图所示：

```
body {<!-- -->
    background-color: lightgreen;
}
h1 {<!-- -->
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 22px;
}

```

#### 3） 创建TypeScript文件

此时，在当前目录再创建一个新的TypeScript文件main.ts, 代码如下：

```
let username = "Jackson";
console.log("Welcome, Mr.", username);

```

#### 4） 运行TypeScript程序

点击Terminal菜单，创建一个新的Terminal终端，切换目录到该文件路径，然后执行以下命令：

```
tsc main.ts

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/c53ca8375f7348c397ce5aac5a7d2b4b.png" alt="在这里插入图片描述"> 看到main.ts编译正常，接下来，运行编译产生的main.js：

```
node main

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/4d44ac87498b4d8396be83ccafd16cb2.png" alt="在这里插入图片描述"> 执行成功!

#### 5） 打开Web页面

最后，单击右键，在弹出菜单里选择Open with Live Server(以Liver Server打开)，于是Chrome浏览器显示页面如下：

<img src="https://img-blog.csdnimg.cn/direct/af01628d35b04b5b940a6e1a8af0dfb5.png" alt="在这里插入图片描述">

以上过程，简要介绍和演示了如何构建TypeScript的集成开发环境（IDE），以及如何创建第一个基于TypeScript的Web应用程序。希望对您有所帮助。

技术好文陆续推出，敬请关注。 您的认可，我的动力！ 😊

#### 相关阅读
1. 1. 1. 1. 1. 1. 1. 1. 