
--- 
title:  8种Python字符串拼接的方法，你知道几种？ 
tags: []
categories: [] 

---
### 一、join函数

join 是 python 中字符串自带的一个方法，返回一个字符串。使用语法为：

<img src="https://img-blog.csdnimg.cn/img_convert/52e5f478f9938c06dfa2c29807c98f31.png#pic_center" alt="img">

将一个包含多个字符串的可迭代对象（字符串、元组、列表），转为用分隔符sep连接的字符串。

**列表**

列表必须为非嵌套列表，列表元素为字符串（str）类型

<img src="https://img-blog.csdnimg.cn/img_convert/12177a1cbf65b89c82a8bbfd28fa083d.png#pic_center" alt="img">

**元组**

<img src="https://img-blog.csdnimg.cn/img_convert/018988598547340dd2c6ac00b16f1335.png#pic_center" alt="img">

**字符串**

<img src="https://img-blog.csdnimg.cn/img_convert/883ea002e2788ecf369b7852a2351523.png#pic_center" alt="img">

**字典**

默认拼接 key 的列表，取 values 之后拼接值。

<img src="https://img-blog.csdnimg.cn/direct/7d2552f043d6465fa556d1b258b4e218.png#pic_center" alt="在这里插入图片描述">

### 二、os.path.join函数

os.path.join函数将多个路径组合后返回，使用语法为：

<img src="https://img-blog.csdnimg.cn/img_convert/38c02c16534e3da7d3a936ca49d519c6.png#pic_center" alt="img">

注：第一个绝对路径之前的参数将被忽略

<img src="https://img-blog.csdnimg.cn/img_convert/ca6d032459efb2746b56aa53fce992b2.png#pic_center" alt="img">

### 三、`+` 号连接

最基本的方式就是使用 “+” 号连接字符串。

<img src="https://img-blog.csdnimg.cn/img_convert/b3fb130e0c8a1fb64e66a65f4c70ddac.png#pic_center" alt="img">

该方法性能差，因为 Python 中字符串是不可变类型，使用“+”号连接相当于生成一个新的字符串，需要重新申请内存，当用“+”号连接非常多的字符串时，将会很耗费内存，可能造成内存溢出。

### 四、`，`连接成tuple（元组）类型

使用逗号“，”连接字符串，最终会变成 tuple 类型。

<img src="https://img-blog.csdnimg.cn/img_convert/1f1ba2aef6d9df16366011cdd04499e3.png#pic_center" alt="img">

### 五、`%s`占位符 or format连接

借鉴C语言中的 printf 函数功能，使用%号连接一个字符串和一组变量，字符串中的特殊标记会被自动使用右边变量组中的变量替换。

<img src="https://img-blog.csdnimg.cn/img_convert/dc09e84f2692b23f2c4e19031a6265ef.png#pic_center" alt="img">

使用 format 格式化字符串也可以进行拼接。

<img src="https://img-blog.csdnimg.cn/img_convert/74c6a5ca0ae81d186d449e60b6442fa2.png#pic_center" alt="img">

### 六、空格自动连接

<img src="https://img-blog.csdnimg.cn/img_convert/83b89e743fffa20132b87ccf073a91e7.png#pic_center" alt="img">

不支持使用参数代替具体的字符串，否则报错。

### 七、`*`号连接

这种连接方式相当于 copy 字符串，例如：

<img src="https://img-blog.csdnimg.cn/img_convert/b4a1e61dfc2232340da48101cd8b9cbb.png#pic_center" alt="img">

### 八、多行字符串连接()

Python遇到未闭合的小括号，自动将多行拼接为一行，相比3个引号和换行符，这种方式不会把换行符、前导空格当作字符。

<img src="https://img-blog.csdnimg.cn/direct/b17309f35d5a4e67b7f5d2e5f4011d2a.png#pic_center" alt="在这里插入图片描述">

**-END-**

<mark>**读者福利：如果大家对Python感兴趣，这套python学习资料一定对你有用**</mark>

**对于0基础小白入门：**

>  
 如果你是零基础小白，想快速入门Python是可以考虑的。 
 一方面是学习时间相对较短，学习内容更全面更集中。 二方面是可以根据这些资料规划好学习计划和方向。 


<mark>包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、机器学习、Python量化交易等习教程。带你从零基础系统性的学好Python！</mark>

## 零基础Python学习资源介绍

① Python所有方向的<mark>学习路线图</mark>，清楚各个方向要学什么东西

② 600多节<mark>Python课程视频</mark>，涵盖必备基础、爬虫和数据分析

③ 100多个<mark>Python实战案例</mark>，含50个超大型项目详解，学习不再是只会理论

④ 20款主流手游迫解 <mark>爬虫手游逆行迫解教程包</mark>

⑤ <mark>爬虫与反爬虫攻防</mark>教程包，含15个大型网站迫解

⑥ <mark>爬虫APP逆向实战</mark>教程包，含45项绝密技术详解

⑦ 超<mark>300本Python电子好书</mark>，从入门到高阶应有尽有

⑧ 华为出品独家<mark>Python漫画教程</mark>，手机也能学习

⑨ 历年互联网企业<mark>Python面试真题</mark>,复习时非常方便

<img src="https://img-blog.csdnimg.cn/7c1055f9bb6e41af9262556bdf20e084.png#pic_center" alt="在这里插入图片描述">

### 👉Python学习路线汇总👈

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<mark>**（全套教程文末领取哈）**</mark> <img src="https://img-blog.csdnimg.cn/9f969354b48f4e3ab0253e89203deca2.png#pic_center" alt="在这里插入图片描述">

### 👉Python必备开发工具👈

<img src="https://img-blog.csdnimg.cn/img_convert/6be280b059df8debff4a4b52d6a6ad1f.png#pic_center" alt="">

**温馨提示：篇幅有限，已打包文件夹，获取方式在：文末**

### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。 <img src="https://img-blog.csdnimg.cn/img_convert/f2a1e9c7368b6ac7d169ab4147b537f4.png#pic_center" alt="">

### 👉实战案例👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/6cf364e7eeb64b0da07021bce5a59ec6.png#pic_center" alt="在这里插入图片描述">

### 👉100道Python练习题👈

检查学习结果。<img src="https://img-blog.csdnimg.cn/img_convert/15bc30b75e1de8c9fa2daab3742d4430.png#pic_center" alt="">

### 👉面试刷题👈

<img src="https://img-blog.csdnimg.cn/img_convert/99f6475fb1237ba21e45d55c67bf83f4.png#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/3360d1bcb588491dac483ff4c30fb05c.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/49fe592a1ae644c2822a1b4a850724cd.png#pic_center" alt="在这里插入图片描述">

## 资料领取

<mark>这份完整版的Python全套学习资料已为大家备好，朋友们如果需要可以微信扫描下方二维码添加，输入"领取资料" 可免费领取全套资料</mark>【<font color="#CC0033" size="3" face="微软雅黑">有什么需要协作的还可以随时联系我</font>】<mark>朋友圈也会不定时的更新最前言python知识。↓↓↓</mark><font color="red" size="3"> **或者**</font> 【】领取
