
--- 
title:  css3实现吃豆豆动画效果 
tags: []
categories: [] 

---
## 一、预备知识

### z-index属性

`z-index`属性是用来设置元素的堆叠顺序或者叫做元素层级，`z-index`的值越大，元素的层级越高。当元素发生重叠时，层级高的元素会覆盖在层级低的元素的上面，使层级低的元素的重叠部分被遮盖住。

`z-index`属性只能在设置了`position: relative | absolute | fixed`的元素和父元素设置了 `display: flex`属性的子元素中起作用，在其他元素中是不作用的。

原文链接：

### ::before和::after的使用

原文链接： 

### overflow:hidden

 原文链接：

### animation属性

原文链接：

## box-shadow属性

通过 box-shadow 属性设置盒子阴影。box-shadow 有四个值:

第一个值是水平偏移量（水平阴影）：即向右的距离，阴影被从原始的框中偏移(如果值为负的话则为左)。 第二个值是垂直偏移量（垂直阴影）：即阴影从原始盒子中向下偏移的距离(或向上，如果值为负)。 第三个值是模糊半径（影子大小）：即在阴影中应用的模糊度。 第四个值是阴影的基本颜色。你可以使用任何长度和颜色单位来定义这些值。

原文链接：

## 二、代码

### index.html

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;Document&lt;/title&gt;
    &lt;link rel="stylesheet" href="./style.css"&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="eat-peas"&gt;
        &lt;div class="head"&gt;
            &lt;div class="eye"&gt;&lt;/div&gt;
        &lt;/div&gt;
        &lt;div class="pea"&gt;&lt;/div&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
```

### style.css

```
body {
    margin: 0;
}
.eat-peas {
    width: 600px;
    height: 200px;
    /* background-color: antiquewhite; */
    margin: 150px auto 0;
    position: relative;
}
.eat-peas .head {
    width: 200px;
    height: 200px;
    /* border: 2px solid blue; */
    border-radius: 50%;
    /* 超出圆的部分设置为隐藏 */
    overflow: hidden;
    position: relative;
    /* 提高head的层级 */
    z-index: 2;
}
/* 首尾元素 */
.eat-peas .head::before {
    content: "";
    display: block;
    width: 200px;
    height: 100px;
    background-color: tomato;
    /* 设置旋转基点 */
    transform-origin: bottom center;
    /* 往上旋转30度 */
    transform: rotate(0deg);
    /* alternate往上走了以后 在动画的下一个周期 逆向动画 */
    animation: rotate1 0.4s ease infinite alternate;
}
.eat-peas .head::after {
    content: "";
    display: block;
    width: 200px;
    height: 100px;
    background-color: tomato;
    transform-origin: top center;
    transform: rotate(0deg);
    animation: rotate2 0.4s ease infinite alternate;
}
.eye {
    width: 20px;
    height: 20px;
    background-color: black;
    border: 2px solid white;
    border-radius: 50%;
    position: absolute;
    top:20px;
    left: 75px;
}
.eat-peas .pea {
    width: 40px;
    height: 40px;
    background-color: tomato;
    border-radius: 50%;
    position: absolute;
    top: 50%;
    left: 150px;
    margin-top: -20px;
    /* 盒子阴影：水平偏移 竖直阴影 模糊程度 背景颜色*/
    box-shadow: 70px 0px 0px tomato,70px 0px 0px tomato,140px 0px 0px tomato,210px 0px 0px tomato,280px 0px 0px tomato,350px 0px 0px tomato;
    animation: move 0.8s ease infinite;
}


/* animation动画 */
@keyframes rotate1 {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(-30deg);
    }
}

@keyframes rotate2 {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(30deg);
    }
}

@keyframes move {
    from {
        transform: translateX(0px);
    }
    to {
        transform: translateX(-70px);
    }
}
```


