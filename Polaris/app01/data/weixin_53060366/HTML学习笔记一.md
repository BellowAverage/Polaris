
--- 
title:  HTML学习笔记一 
tags: []
categories: [] 

---
## HTML学习笔记一

### 1、HTML简介：

超文本标记语言（英语：HyperText Markup Language，简称：HTML）是一种用于创建网页的标准标记语言。

可以使用 HTML 来建立自己的 WEB 站点，HTML 运行在浏览器上，由浏览器来解析。

HTML的文档后缀名：.html .htm <img src="https://img-blog.csdnimg.cn/e8de3a6fe5ac414b8df5ea6627e2d299.png#pic_center" alt="在这里插入图片描述">

>  
 - **** 声明为 HTML5 文档- **** 元素是 HTML 页面的根元素- **** 元素包含了文档的元（meta）数据，如 **** 定义网页编码格式为 **utf-8**。- **<title></title>** 元素描述了文档的标题- **** 元素包含了可见的页面内容- ****<h2> 元素定义一个大标题</h2>- **** 元素定义一个段落 


注意：在浏览器的页面上使用键盘上的 F12 按键开启调试模式，就可以看到组成标签。

#### 什么是HTML？
- HTML 指的是超文本标记语言: **H**yper**T**ext **M**arkup **L**anguage- HTML 不是一种编程语言，而是一种**标记**语言- 标记语言是一套**标记标签** (markup tag)- HTML 使用标记标签来**描述**网页- HTML 文档包含了HTML **标签**及**文本**内容- HTML文档也叫做 **web 页面**
#### HTML标签：
- HTML 标签是由**尖括号**包围的关键词，比如 - HTML 标签通常是**成对出现**的，比如 ** 和 &lt;/ b&gt;**- 标签对中的第一个标签是**开始标签**，第二个标签是**结束标签**- 开始和结束标签也被称为**开放标签**和**闭合标签**
通常，“HTML 标签” 和 “HTML 元素” 都是描述同样的意思。也就是说标签就是元素。

通用声明：

目前在大部分浏览器中，直接输出中文会出现中文乱码的情况，这时候我们就需要在头部将字符声明为 UTF-8 或 GBK。

```
&lt;meta charset="UTF-8"&gt;

```

### 2、HTML基础：

#### 1）标题标签

HTML 标题 是通过h1-h6 标签来定义的。

```
&lt;h1&gt;
    我是标题一
&lt;/h1&gt;

```

#### 2）段落标签

```
&lt;p&gt;
    这是一个段落
&lt;/p&gt;

```

#### 3）链接标签：

```
&lt;a href="http://www.baidu.com"&gt;这是一个链接&lt;/a&gt;

```

#### 4）图像标签：

```
&lt;img src="/images/logo.png" width="258" height="39" /&gt;

```

换行标签：

```
&lt;br /&gt;

```

注意：HTML标签使用小写字母。

### 3、HTML元素：
- HTML 元素以**开始标签**起始- HTML 元素以**结束标签**终止- **元素的内容**是开始标签与结束标签之间的内容- 某些 HTML 元素具有**空内容（empty content）**- 空元素**在开始标签中进行关闭**（以开始标签的结束而结束）- 大多数 HTML 元素可拥有**属性**
大多数html元素可以嵌套。

没有内容的 HTML 元素被称为空元素。空元素是在开始标签中关闭的。

```
&lt;br&gt; 就是没有关闭标签的空元素（&lt;br&gt; 标签定义换行）。
在开始标签中添加斜杠，比如 &lt;br /&gt;，是关闭空元素的正确方法，HTML、XHTML 和 XML 都接受这种方式。

```

在HTML中 



### 4、HTML属性：
- HTML 元素可以设置**属性**- 属性可以在元素中添加**附加信息**- 属性一般描述于**开始标签**- 属性总是以名称/值对的形式出现，**比如：name=“value”**。
### 5、HTML文本格式化：

|标签|描述
|------
|b|定义粗体文本
|em|定义着重文字
|i|定义斜体字
|small|定义小号字
|strong|定义加重语气
|sub|定义下标字
|sup|定义上标字
|ins|定义插入字
|del|定义删除字

### 6、HTML链接：

HTML 使用超级链接与网络上的另一个文档相连。

HTML中的链接是一种用于在不同网页之间导航的元素。

链接通常用于将一个网页与另一个网页或资源（如文档、图像、音频文件等）相关联。

链接允许用户在浏览网页时单击文本或图像来跳转到其他位置，从而实现网页之间的互联。

```
&lt;p&gt;&lt;a href="http://www.baidu.com/"&gt;本文本&lt;/a&gt; 是一个指向万维网上的页面的链接。&lt;/p&gt;

```

HTML使用标签 **** 来设置超文本链接。

超链接可以是一个字，一个词，或者一组词，也可以是一幅图像，您可以点击这些内容来跳转到新的文档或者当前文档中的某个部分。

默认情况下，链接将以以下形式出现在浏览器中：
- 一个未访问过的链接显示为蓝色字体并带有下划线。- 访问过的链接显示为紫色并带有下划线。- 点击链接时，链接显示为红色并带有下划线。\
元素具有以下属性：
- `href`：指定链接目标的URL，这是链接的最重要属性。可以是另一个网页的URL、文件的URL或其他资源的URL。- `target`（可选）：指定链接如何在浏览器中打开。常见的值包括 `_blank`（在新标签或窗口中打开链接）和 `_self`（在当前标签或窗口中打开链接）。- `title`（可选）：提供链接的额外信息，通常在鼠标悬停在链接上时显示为工具提示。- `rel`（可选）：指定与链接目标的关系，如 nofollow、noopener 等。
```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;

&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta http-equiv="X-UA-Compatible" content="IE=edge"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;超链接标签&lt;/title&gt;
&lt;/head&gt;

&lt;body&gt;
    &lt;!-- 超链接标签 --&gt;
    &lt;!-- 外部链接 --&gt;
    &lt;a href="http://www.baidu.com" target="_blank"&gt;百度一下，你就知道&lt;/a&gt;
    &lt;!-- blank 是在新窗口中打开 --&gt;

    &lt;!-- 内部链接 --&gt;
    &lt;h4&gt;内部的超链接&lt;/h4&gt;
    &lt;a href="体育新闻.html" target="_blank"&gt;体育新闻网站&lt;/a&gt;

    &lt;!-- 空链接 --&gt;
    &lt;a href="#"&gt;空链接&lt;/a&gt;

    &lt;!-- 下载链接 --&gt;
    &lt;h4&gt;下载链接，地址是 文件，.exe 或者是zip等压缩包形式&lt;/h4&gt;
    &lt;a href="./images/cc.zip"&gt;下载文件&lt;/a&gt;
&lt;/body&gt;

&lt;/html&gt;

```
