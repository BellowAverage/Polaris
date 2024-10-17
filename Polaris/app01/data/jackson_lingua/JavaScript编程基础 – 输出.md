
--- 
title:  JavaScript编程基础 – 输出 
tags: []
categories: [] 

---
## JavaScript编程基础 – 输出

### JavaScript Programming Essentials – Output

>  
 JavaScript广泛应用于Web开发，但是它不提供任何内建的打印输出或者显示的函数。 在实际开发、学习及应用过程中，仍然需要这样的输出功能，怎么解决呢？ 


本文简要介绍如何显示数据到网页，也就是通过HTML输出，或者通过控制台输出的方法，供读者参考。

#### 0. JavaScript 可选的几种显示方案

JavaScript 实际能够以以下不同方式来“显示”数据：
1. 使用 window.alert() 写入警告框1. 使用 document.write() 写入 HTML 输出1. 使用 innerHTML 写入 HTML 元素1. 使用 console.log() 写入浏览器控制台
以下分别简要介绍各种显示方案及用法。

#### 1. 使用 innerHTML

如需访问 HTML 元素，JavaScript 可使用 **document.getElementById(id)** 方法。

**id** 属性定义 HTML 元素。innerHTML 属性定义 HTML 内容，例如下面的代码：

```
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;body&gt;
&lt;h1&gt;The First Web Page&lt;/h1&gt;
&lt;p&gt;The first paragraph&lt;/p&gt;
&lt;p id="demo"&gt;&lt;/p&gt;
&lt;script&gt;
   document.getElementById("demo").innerHTML = "Inner HTML Result";
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;

```

Chrome浏览器显示效果如下图（检查模式）： <img src="https://img-blog.csdnimg.cn/740bb6b4137f40a49b9b0379fa52e271.png" alt="在这里插入图片描述">

#### 2. 使用 document.write()

出于测试目的，使用 document.write() 比较方便，如下方示例：

```
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;body&gt;
&lt;h1&gt;My First Web Page&lt;/h1&gt;
&lt;p&gt;My First Paragraph&lt;/p&gt;

&lt;script&gt;
document.write(10 + 28);
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;

```

Chrome浏览器显示结果如下图（document.write( ) 计算结果：38）： <img src="https://img-blog.csdnimg.cn/0ed3bb6d93a94e9c9d01b9395ce04001.png" alt="在这里插入图片描述"> ***注意**：在 HTML 文档完全加载后使用 document.write() 将删除所有已有的 HTML；因此，document.write() 仅用于测试，开发时需要谨慎选择。

#### 3. 使用 window.alert()

您能够使用警告消息框来显示数据：

```
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;body&gt;
&lt;h1&gt;My First Web Page with Alert Dialog&lt;/h1&gt;
&lt;p&gt;My First Paragraph&lt;/p&gt;

&lt;script&gt;
	window.alert(13 + 24);
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;

```

Chrome浏览器运行结果如下图（加法计算结果为：37）：

<img src="https://img-blog.csdnimg.cn/228e12df5c08439cb79f061e86c81a8d.png" alt="在这里插入图片描述">

#### 4. 使用 console.log( )

在浏览器中，您可使用 console.log() 方法来显示数据。

请通过 F12 来激活浏览器控制台，并在菜单中选择“控制台”。

```
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;body&gt;
&lt;h1&gt;The First Web Page with Console.log&lt;/h1&gt;
&lt;p&gt;The First Paragraph&lt;/p&gt;
&lt;script&gt;
	console.log(1024 + 256);
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;

```

运行结果如下图（Chrome检查模式, 控制台结果：1280）： <img src="https://img-blog.csdnimg.cn/6cbba6549061497cb46963c1d8776b23.png" alt="在这里插入图片描述">

JavaScript编程基础，将不断推出博文。敬请关注。

您的支持，我的动力！喜欢就点赞哈。😊

###### 相关阅读：
1. 1. 