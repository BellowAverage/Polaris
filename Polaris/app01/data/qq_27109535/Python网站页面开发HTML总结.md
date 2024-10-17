
--- 
title:  Python网站页面开发HTML总结 
tags: []
categories: [] 

---
Python网站页面开发HTML总结

## 一、HTML基础语法

### 1.HTML是什么？

**●HTML是HyperText Mark-up Language的首字母简写，即超文本标记语言。 ●HTML不是一种编程语言，而是一种标记语言。 ●超文本指的是超链接，标记指的是标签，是一种用来制作网页的语言，这种语言由一个个的标签组成。 ●用这种语言制作的文件保存的是一个文本文件，文件的扩展名为.html或者.htm ●“html文档也叫Web页面，其实就是一个网页，html文件用编辑器打开显示的是文本，可以用文本的方式编辑它。 ●如果用浏览器打开，浏览器会按照标签描述内容将文件渲染成网页，显示的网页可以从一个网页链接跳转到另外一个网页。**

### 2.HTML基本结构

```
●HTML是由:标签和内容构成。
●HTML标签(标记)的语法是由&lt;和&gt;括起来。
● HTML标签有两种:
   双标签:&lt;标签名&gt;....&lt;/标签名&gt;和单标签:&lt;标签名/&gt;
●HTML标签中还可以添加属性:
  &lt;标签名属性名1=“值1”属性名2=“值2”属性名n=“值n”&gt;..….&lt;/标签名&gt;
●HTML标签规范∶标签名小写、属性使用双引号、标签要闭合。规范不遵守浏览器不会报错，会尽量解析，大不了不显示效果。

```

```
&lt; ! DOCTYPE html&gt;&lt;!--头部，是html的类型，此处代表的是采用html5版本，浏览器可以识别解析--&gt;
&lt;html lang="en"&gt;
	&lt;head&gt;
		&lt;meta charset="UTF-8"&gt;&lt;title&gt;网页标题&lt;/title&gt;
		&lt;!--此处可以写各种页头属性设置、CSS样式和Javascript脚本等...--&gt;
	&lt;/ head&gt;
&lt;body&gt;
	网页显示内容
&lt;/body&gt;
&lt;/ html&gt;

```

### 3.HTML注释

```
html代码文档中可以插入注释，注释是对代码的说明和解释

```

### 4.HTML中head头部信息设置

```
●设置网页编码：&lt;meta charset="utf-8" /&gt;
●关键字：&lt;meta name="Keywords" content="关键字"/&gt;
●描述：&lt;meta name="Description" content="简介、描述"/&gt;
●网页标题：&lt;title&gt;本网页标题&lt;/title&gt;
●导入CSS文件:：&lt;link type="text/css" rel="stylesheet" href="**.css"/&gt;
●CSS代码：&lt;style type="text/css"&gt;嵌入css样式代码&lt;/style&gt;
●JS文件或代码：&lt;script &gt;...&lt;/script&gt;

```

## 二、HTML常用标签介绍

### 1.文本标签

```
●&lt;hn&gt;..&lt;/hn&gt;其中n为1--6的值。标题标签（加粗、独立行)

●&lt;i&gt;...&lt;/i&gt;斜体

●&lt;em&gt;...&lt;/em&gt;强调斜体

●&lt;b&gt;.…/b&gt;加粗

●&lt;strong ...&lt;/strong&gt;强调加粗

●&lt;cite&gt;&lt;/cite&gt;作品的标题（引用)

●&lt;sub&gt;...&lt;/sub&gt;下标

●&lt;sup&gt;...&lt;/sup&gt;上标

●&lt;del&gt;...&lt;/del&gt;删除线

```

### 2.格式化标签

```
●&lt;br/&gt;换行

●&lt;p&gt;….&lt;/p&gt;换段

●&lt;hr /&gt;水平分割线

●列表:
●&lt;ul&gt;...&lt;/ul&gt;无序列表
●&lt;ol&gt;..&lt;/ol&gt;有序列表其中type类型值:Aali 1 start属性表示起始值
●&lt;li&gt;...&lt;/li&gt;列表项
●&lt;dl&gt;..&lt;/dl&gt;自定义列表. &lt;dt&gt;...&lt;/dt&gt;自定义列表头.&lt;dd&gt;...&lt;/dd&gt;自定义列表内容
●&lt;div&gt;...&lt;/div&gt;常用于组合块级元素，以便通过CSS来对这些元素进行格式化
●&lt;span...&lt;/span&gt;常用于包含的文本，您可以使用CSS对它定义样式，或者使用JavaScript对它进行操作。

```

### 3.图片标签

```
●&lt;img/&gt;在网页中插入一张图片
●属性:
        ●src:图片名及url地址
        ●alt:图片加载失败时的提示信息.title:文字提示属性
        ●width:图片宽度
        ● height:图片高度
        ●border:边框线粗细

```

### 4.超级链接标签

```
●&lt;a href=“”&gt;...&lt;/a&gt;超级链接标签，属性如下:
●href:必须，指的是链接跳转地址
●target:表示链接的打开方式:
           ●_blank 新窗口

          ●_parent父窗口

          ●_self本窗口(默认)

          ●_top顶级窗口

          ● framename窗口名

● title:文字提示属性（详情)

●锚点链接:
          ●定义一个锚点:&lt;a id="a1"&gt;&lt;/a&gt;以前使用的是&lt;a name="a1"&gt;&lt;/a&gt;

          ●使用锚点:&lt;a href="#a1"&gt; 跳到a1处&lt;/a&gt;

```

### 5.表格标签（用来显示数据）

```
●&lt;table&gt;..&lt;/table&gt;表格标签:属性: border（表格边框的粗细大小）、 width、cellspacing（单元格之间的间距）. cellpadding（单元格里的内容到单元格边框的距离）

●&lt;caption&gt;...&lt;/caption&gt;表格标题
●&lt;tr&gt;...&lt;/tr&gt;行标签
● &lt;th&gt;.../th&gt;列头标签（内容会加粗，居中显示）
●&lt;td&gt;...&lt;/td&gt;列标签:跨行属性: rowspan 跨列属性:colspan （合并单元格的作用）
●&lt;thead&gt;...&lt;/thead&gt;表头
● &lt;tbody&gt;...&lt;/tbody&gt;表体

●&lt;tfoot&gt;...&lt;/tfoot&gt;表尾

注意：表格里的内容必须放到&lt;th&gt;、&lt;hd&gt;标签中，否则会被挤出表格

```

### 6.表单标签（用来接收数据）

```
●&lt;form&gt;...&lt;/form&gt;表单标签  &lt;form action=""（填写目标地址，填完表单后会跳转该地址） method="post/get"（post是指在跳转到页面后在网址栏那个地方不显示表单的内容，get是指在跳转到页面后在网址栏那个地方显示表单的内容）&gt;

●&lt;input /&gt;表单项标签input定义输入字段，用户可在其中输入数据。

● &lt;select&gt;...&lt;/select&gt;标签创建下拉列表。

● &lt;textarea&gt;..&lt;/textarea&gt;多行的文本输入区域

●&lt;button&gt;...&lt;/button&gt;标签定义按钮。

●&lt;fieldset&gt;--&lt;/fieldset&gt;元素可将表单内的相关元素分组。

●&lt;legend&gt;&lt;/legend&gt; 标签为&lt;fieldest&gt;、&lt;figure&gt;以及&lt;details&gt;元素定义标题。

●&lt;datalist&gt; html5标签--&lt;datalist&gt;  标签定义可选数据的列表。

●&lt;optgroup&gt; html5标签--&lt;optgroup&gt;标签定义选项组。

```

### 7.行内框架标签

```
●&lt;iframe&gt;...&lt;/iframe&gt;行内框架
属性:

        src:规定在iframe中显示的文档的URL

        name:规定iframe的名称

        height:规定 iframe的高度。

        width:定义iframe的宽度。

        frameborder:规定是否显示框架周围的边框。
●例如:&lt;iframe src="1.html" name="myframe" width="700" height="500"&gt;&lt;/iframe&gt;

```

8.多媒体标签

```
●&lt;audio&gt;…&lt;/audio&gt;音频标签
● &lt;video&gt;…&lt;/video&gt;视频标签
●播放Flash的标签
&lt;embed src="./images/haowan.swf" width="300" height="300"/&gt;

```
