
--- 
title:  [ XSS-labs通关宝典 ] xss-labs 通关宝典之 less1 - less5 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - <ul><li>- - - - - - - - - - - 


## 第一关： 反射型xss

<img src="https://img-blog.csdnimg.cn/016f989aca0d4dd5a490b9a38e8e3919.png" alt="在这里插入图片描述">

服务器以get方式提交了一个name参数，值为“test”，test为用户名 从页面回显来看，将neme参数的值显示在了页面上，并且显示了name参数值的字符长度

### 网页源码

<img src="https://img-blog.csdnimg.cn/7d95946d8ff3461bb04986e76fd692c1.png" alt="在这里插入图片描述">

可以看到它将name的参数值，插入到了

###  



### 测试：

但是由于不知道服务器端对于提交的敏感字符有没有过滤，所以这里直接在name参数 中赋值一个简单的弹窗来进行测试。 将name参数重新赋值： 我们可以看到用于js弹窗的代码顺利执行了 右键查看源码 <img src="https://img-blog.csdnimg.cn/f55e43d7ced54b318e0d569253a10c46.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/a3f0f411a81849f9be0db2253bbc7504.png" alt="在这里插入图片描述"> 可以看到服务器是将我们的恶意代码原封不动的返回了，浏览器才能成功弹窗

### 服务器端:

<img src="https://img-blog.csdnimg.cn/fd7931b33d9047cc8a6ad41675710b8f.png" alt="在这里插入图片描述">

从源码可以看出，将从服务器获得的name参数的直接值赋值给str变量，又将str变量直接插入到

###  



## 第二关：反射型xss

<img src="https://img-blog.csdnimg.cn/62adc4df324645518eee84012eec180b.png" alt="在这里插入图片描述">

从url入手开始看，依然是get方式传递参数，应该还是反射型xss 只不过这一关加入了“输入框”和“搜索”

### 网页源码

从源码来看，它的功能就是通过点击“搜索”按钮，将输入框内的内容以get方式提交给服务器上的level2.php 经过服务器的动态处理之后又会将参数keyword的值插入到

###  



### 测试：

尝试使用上一关的恶意语句操作进行弹窗

右键查看源码
1.  <h3> </h3>标签之中的恶意代码被编码 其中&lt;和&gt;都被编码成了html字符实体。 
猜测在服务器端用htmlspecialchars()函数对keyword参数的值进行了处理。 2.插入到value参数值中的恶意代码并没有被编码而是直接原样返回 <img src="https://img-blog.csdnimg.cn/91ac56840fac427aa46b44d4878a8c12.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/1046a0c74e57488daf2917d4ffe7b88a.png" alt="在这里插入图片描述">

但是问题是这里的js代码在标签属性值中，浏览器是无法执行的。 既然上面的恶意代码被编码了，那么只能从属性值中的恶意代码处进行突破了。 要想浏览器执行这里的弹窗代码，只需要将属性的引号和标签先闭合就可以了。 将keyword的参数值重新赋值"&gt;//"&gt; 左边的"&gt;去闭合原先的" 右边的//去注释原先的"&gt; 可以看到浏览器成功弹窗了，说明我们提交的恶意代码被浏览器执行了。 <img src="https://img-blog.csdnimg.cn/b56f5be0bd494db58d3c654ab1d42852.png" alt="在这里插入图片描述">

### 服务器端：

get方式传递到服务器端的keyword参数的值赋给str变量。 用htmlspecialchars()函数对变量str进行处理之后echo到网页上。 直接将变量值插入到了标签的value属性值中 因为这里并没有对敏感字符进行编码和过滤，所以可以通过构造实现XSS攻击。 <img src="https://img-blog.csdnimg.cn/b9e0fe29e6ad42d6961f0e5b25835222.png" alt="在这里插入图片描述">

## 第三关：

输入test尝试 右键查看源码 <img src="https://img-blog.csdnimg.cn/27c424d215984f7099d849d515af5f21.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b5bc68bd301e47a58bcdba4d1517341d.png" alt="在这里插入图片描述">

与第二关相似 不确定有没有 敏感字符过滤，编码等操作 构造payload弹窗： 提示没有找到 继续看看网页源码 这两处都将&lt;和&gt;这样的敏感字符编码成了html字符实体。 猜测服务器端在这两处都用htmlspecialchars()函数进行了处理。

<img src="https://img-blog.csdnimg.cn/ee2f39d8d98d47768292e8963eac8d2c.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ec67060e92ec4ae787cfbff5670a1612.png" alt="在这里插入图片描述">

### 服务器端：

<img src="https://img-blog.csdnimg.cn/61aec7612f6e42d3b5ef698e63e4e13c.png" alt="在这里插入图片描述">

确认我们的猜测 这里可以通过标签的一些特殊事件来执行js代码 构造代码：level3.php?keyword='οnfοcus=javascript:alert(‘xss’) &gt; //&amp;submit=搜索 <img src="https://img-blog.csdnimg.cn/1c3778b85c6543768f88d2a3213cfba5.png" alt="在这里插入图片描述">

发现没有直接弹窗，点击当前页面的输入框完成弹窗。 <img src="https://img-blog.csdnimg.cn/8ac6dc2563fb40db8168c95b4bae5f2d.png" alt="在这里插入图片描述">

这是因为onfocus事件的特殊性造成的 onfocus 事件 onfocus 事件在对象获得焦点时发生。 onfocus 通常用于 , , 和. 最简单的实例就是网页上的一个输入框,当使用鼠标点击该输入框时输入框被选中可以 输入内容的时候就是该输入框获得焦点的时候,此时输入框就会触发onfocus事件 网页源码：

## 第四关：

这一关很明显还是用的get方式请求参数 并且该参数值在页面上有两处显示 上弹窗代码测试一下  <img src="https://img-blog.csdnimg.cn/827a5fe9c56d42f8b6ca445234101c9a.png" alt="在这里插入图片描述">

输入框中与我们提交的参数值有出入，&lt;和&gt;没有了

### 网页源码

<img src="https://img-blog.csdnimg.cn/09c7711035ab4ae4a1edd6d8eebfc639.png" alt="在这里插入图片描述">

一处直接将&lt;和&gt;编码转换了 一处却是把&lt;和&gt;删除了 但是，事件触发却不需要使用这两个符号。

### 测试

用上一关的代码： "&gt;οnfοcus=javascript:alert(‘xss’)// 或者 "οnfοcus=javascript:alert(‘xss’)&gt; 在点击输入框之后成功触发了事件进行弹窗。 <img src="https://img-blog.csdnimg.cn/899f015e352840cdbbcd18a8cdcb7286.png" alt="在这里插入图片描述">

### 服务器端源码

分析一下 <img src="https://img-blog.csdnimg.cn/4c5dc618c5f74a149a867a2340b9cb41.png" alt="在这里插入图片描述">

将get方式传递到服务器端的keyword参数的值赋给str变量。 将变量中的&lt;和&gt;删除 对变量进行编码然后显示在页面上 将去除&lt;和&gt;的变量值插入到标签的value属性值中。

## 第五关：

还是get方式请求参数，所以还是反射型的xss 上弹窗代码：测试一下 <img src="https://img-blog.csdnimg.cn/318e77433bab407cb1043b79e47fb53c.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/4f3e0856df2f494e99c74700f04d3858.png" alt="在这里插入图片描述">

### 网页源码：

<img src="https://img-blog.csdnimg.cn/50081f34c8d742bf881f6af6e33c54da.png" alt="在这里插入图片描述">

应该是被htmlspecialchars()函数将&lt;和&gt;进行了编码处理 在显示位可以看到，它在我们的恶意代码

这里居然对onfocus这一类的事件字符也进行了防范。 从刚才的响应来看提交的javascript字符并没有被过滤或者转义等 所以此处既然无法通过

<img src="https://img-blog.csdnimg.cn/7f83b5cb7b664ec791e046fc4942c3e1.png" alt="在这里插入图片描述">

### 服务器源码

将get方式传递到服务器端的keyword参数的值进行全小写的转换，然后赋值给str变量。 通过str_replace()函数来破坏变量值中的敏感字符的语义。On o_n 通过htmlspecialchars()函数处理之后显示到网页上， 直接将进行敏感字符处理之后的变量值插入到标签的value属性值中。

<img src="https://img-blog.csdnimg.cn/a125b39655294c87bb54d2a8c7691701.png" alt="">
