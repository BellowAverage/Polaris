
--- 
title:  网站/App都变灰了，是怎么实现的呢？ 
tags: []
categories: [] 

---
估计大家发现了，各大网站、APP都变灰了，原因想必大家都知道了。

粉丝群里有人在问，这是如何做到的？

<img src="https://img-blog.csdnimg.cn/img_convert/251a14ff7aa0f4188d4b547963f4f67e.png" alt="251a14ff7aa0f4188d4b547963f4f67e.png">

随便打开这些任何一个网站，全站的内容都变成了灰色，包括按钮、图片等等。相信这时候从事程序开发的粉丝可能会好奇这是怎么做到的呢？

有人会以为所有的内容都统一换了一个 CSS 样式，图片也全换成灰色的了，按钮等样式也统一换成了灰色样式。但你想想这个成本也太高了，而且万一某个控件忘记加灰色样式了岂不是太突兀了。

其实，解决方案很简单，只需要几行代码就能搞定了。

我们选择一个网站，比如CSDN官网，打开浏览器开发者工具。

审查一下网页的源代码，我们可以发现在 html 的这个地方多了一个疑似的 class，叫做 gray，gray 中文即灰色。

从事前端开发的朋友会以为所有的内容都统一换了一个 CSS 样式，图片也全换成灰色的了，按钮等样式也统一换成了灰色样式。如下图，有一个灰色样式：[filter: grayscale(100%);]，也许就是这一个样式控制着整个网页显示效果。

它也是用的这个 CSS 样式，其内容为：

```
html {
    -webkit-filter: grayscale(100%);
    -moz-filter: grayscale(100%);
    -ms-filter: grayscale(100%);
    -o-filter: grayscale(100%);
    filter: grayscale(100%);
    filter: progid:DXImageTransform.Microsoft.BasicImage(grayscale=1);
}
```

这个实现看起来兼容性会更好一些。

因此我们可以确定，通过一个全局的 CSS 样式就能将整个网站变成灰色效果。

方法教到这里，我们就来详细了解一下这究竟是一个什么样的 CSS 样式。

这个样式名叫做 filter，搜下 MDN 的官方介绍，其链接为：**https://developer.mozilla.org/zh-CN/docs/Web/CSS/filter。**

官方介绍内容如下：

>  
  **`filter`** CSS 属性将模糊或颜色偏移等图形效果应用于元素。滤镜通常用于调整图像，背景和边框的渲染。 
  CSS 标准里包含了一些已实现预定义效果的函数。你也可以参考一个 SVG 滤镜，通过一个 URL 链接到 SVG 滤镜元素 (SVG filter element<sup>[1]</sup>)。 
 

其实就是一个滤镜的意思。

官方有一个 Demo，可以看下效果，如图所示。

比如这里通过 filter 样式改变了图片、颜色、模糊、对比度等等信息。

其所有用法示例如下：

```
/* URL to SVG filter */
filter: url("filters.svg#filter-id");


/* &lt;filter-function&gt; values */
filter: blur(5px);
filter: brightness(0.4);
filter: contrast(200%);
filter: drop-shadow(16px 16px 20px blue);
filter: grayscale(50%);
filter: hue-rotate(90deg);
filter: invert(75%);
filter: opacity(25%);
filter: saturate(30%);
filter: sepia(60%);


/* Multiple filters */
filter: contrast(175%) brightness(3%);


/* Global values */
filter: inherit;
filter: initial;
filter: unset;
```

再说回刚才的灰色图像，这里其实就是设置了 grayscale，其用法如下：

```
filter: grayscale(percent)
```

将图像转换为灰度图像。值定义转换的比例。percent 值为 100% 则完全转为灰度图像，值为 0% 图像无变化。值在 0% 到 100% 之间，则是效果的线性乘子。若未设置，值默认是 0。另外除了传递百分比，还可以传递浮点数，效果是一样的。

如：

```
filter: grayscale(1)
filter: grayscale(100%)
```

都可以将节点转化为 100% 的灰度模式。

所以一切到这里就清楚了，如果我们想要把全站变成灰色，再考虑到各浏览器兼容写法，可以参考下 CSDN 的写法：

```
.gray {
    -webkit-filter: grayscale(100%);
    -moz-filter: grayscale(100%);
    -ms-filter: grayscale(100%);
    -o-filter: grayscale(100%);
    filter: grayscale(100%);
    filter: progid:DXImageTransform.Microsoft.BasicImage(grayscale=1);
}
```

这样想要变灰的节点只需要加上 gray 这个 class 就好了，比如加到 html 节点上就可以全站变灰了。

最后呢，看一下浏览器对 filter 这个样式的兼容性怎样，如图所示：

这里我们看到，这里除了 IE，其他的 PC、手机端的浏览器都支持了，Firefox 的 PC、安卓端还单独对 SVG 图像加了支持，可以放心使用。
- - - 