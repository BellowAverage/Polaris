
--- 
title:  html+css经典案例--时间轴 
tags: []
categories: [] 

---
## 一、预备知识

### CSS盒子塌陷及解决方法

主流解决方法：

为外部盒子添加after伪类，设置clear属性清除浮动。

```
父盒子::after {
    content: "";
    /* 清除两边的浮动 */
    clear: both;
    /* 也可以使用display:table; */
    display: block;
    /* 兼容IE浏览器 */
    zoom: 1;
}

```

原文链接：

### margin设置

margin 简写属性在一个声明中设置所有当前或者指定元素外边距属性。该属性可以有 1 到 4 个值。 

margin写法有4种，分别如下：

```
 margin: 像素值1;
 margin: 像素值1  像素值2;
 margin: 像素值1  像素值2  像素值3;
 margin: 像素值1  像素值2  像素值3  像素值4;
```

以上四个位置按顺序分别为：**margin-top**------，即“**上**-**右**-**下**-**左**”。以下简写为**top**--**right**--**bottom**--**left**。其中需要注意的是后三种情况，当有缺省时，浏览器会自动对缺省像素按照“**bottom**=**top**”和“**left**=**right**”的方法进行赋值。

例如：

“margin:20px;”表示四个方向的外边距都是20px；

“margin:20px 40px;”表示top为20px，right为40px；由于bottom和left缺省，所以自动将它们分别设为20px和40px。转化为第4种写法为：“margin:20px 40px 20px 40px;”。

“margin:20px 40px 60px;”表示top为20px，right为40px，bottom为60px；由于left缺省，所以自动将它设为40px。转化为第4种写法为：“margin:20px 40px 60px 40px;”。

需要注意的是一种情况不能写为缺省写法：“margin:20px 40px 20px 60px;”。该例中，由于top和bottom相同，但right和left不同，所以不能将bottom缺省，否则会等同于“margin:20px 40px 60px 40px;”。

### 浮动

浮动最典型的应用：可以让多个块级元素一行内排列显示。

网页布局第一准则：多个块级元素纵向排列找标准流，多个块级元素横向排列找浮动！

原文链接：

### border-radius使用详解

 

## 二、代码

### index.html

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;Document&lt;/title&gt;
    &lt;link rel="stylesheet" href="style.css"&gt;

&lt;/head&gt;
&lt;body&gt;
    &lt;div class="tit"&gt;
        &lt;h3&gt;今天也有在认真生活&lt;/h3&gt;
    &lt;/div&gt;
    &lt;div class="time-axis  clearfix"&gt;
        &lt;div class="left"&gt;
            &lt;span class="dot"&gt;&lt;/span&gt;
            &lt;span class="jiantou"&gt;&lt;/span&gt;
            &lt;div class="con"&gt;&lt;/div&gt;
        &lt;/div&gt;
        &lt;div class="right"&gt;
            &lt;span class="dot"&gt;&lt;/span&gt;
            &lt;span class="jiantou"&gt;&lt;/span&gt;
            &lt;div class="con"&gt;&lt;/div&gt;
        &lt;/div&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
```

### style.css

```
body {
    margin: 0;
    background-image: linear-gradient(to right,#fdf1d8,#b1bbf9);

}
.tit {
    width: 500px;
    /* border: 2px solid red; */
    margin: 50px auto 0px;
    text-align: center;
    font-size: 40px;
    /* color: #b1bbf9; */
}
.clearfix::after {
    content: "";
    clear: both;
    display: block;
}
.time-axis {
    /* 右边盒子设为右浮动 最外层盒子的宽度+4 则右边盒子右移4px 使得时间轴对齐 */
    width: 604px;
    /* height:700px; */
    /* border:2px solid red; */
    /* 上右下左 左缺省 和右边保持一致 */
    margin: 50px auto 10px;
}
.time-axis .left {
    width: 300px;
    /* height: 300px; */
    /* background-color: beige; */
    float: left;
    border-right: 4px solid #b1bbf9;
    position: relative;
}
.time-axis .right {
    width: 300px;
    /* height: 300px; */
    /* background-color: azure; */
    float: right;
    border-left: 4px solid #b1bbf9;
    position: relative;
}


.time-axis .dot {
    width: 10px;
    height: 10px;
    display: block;
    background-color: #fff;
    border: 2px solid #b1bbf9;
    border-radius: 7px;
    position: absolute;
    /* right:0的时候圆点到左盒子的最右边，为了使其在时间轴的正中间，需要继续右移圆点大小的一半（即7px）+时间轴的宽度一半（即2px） */
    top: 50%;
    margin-top: -7px;
}
.time-axis .left .dot {
    right: -9px;
}
.time-axis .right .dot {
    left: -9px;
}

.time-axis .jiantou {
    width: 0px;
    height: 0px;
    /* background-color: red; */
    display: block;
    border: 20px solid transparent;
    border-left: 20px solid white;
    position: absolute;
    right: -8px;
    top: 50%;
    margin-top: -20px;
}
.time-axis .right .jiantou {
    border: 20px solid transparent;
    border-right: 20px solid white;
    position: absolute;
    left: -8px;
}

.time-axis .con {
    /* height: 200px; */
    background-color: #fff; 
    padding: 15px;
    border-radius: 20px;
    text-align: center;
}
.time-axis .left .con {
    margin-right: 30px;
}
.time-axis .right .con {
    margin-left: 30px;
}

h3{
    margin: 0;
}
.time-axis .con h3 {
    /* border: 1px solid red; */
    font-size: 400;
}
.time-axis .con h3 span {
    font-size: 38px;
    font-family:Arial, Helvetica, sans-serif;
    color: #b1bbf9;
}
```
