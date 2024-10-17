
--- 
title:  如何扩展Unity URP的后处理Volume组件 
tags: []
categories: [] 

---
### 如何扩展Unity URP的后处理Volume组件

Unity在更新到Unity2019.4之后，大家或许已经发现，在使用URP（通用渲染管线）的情况下，Unity原来的Post Processing插件好像不起效了。 原来Unity在Unity2019.4之后在URP内部集成了屏幕后处理的功能，使用方法也很简单，直接在Hierachy视图右键，选择Volume/Global Volume，我们就可以在Hierarchy视图看到一个Global Volume游戏对象。选中它，在资源检视面板可以看到有一个Volume组件，这就是URP实现屏幕后处理的核心组件。

<img src="https://img-blog.csdnimg.cn/img_convert/48258561ab4856c84f698dafec1e8ef3.webp?x-oss-process=image/format,png" alt="">

在资源检视面板上，我们看到Volume组件下面有个Profile选项，要求我们给Volume组件选定一个volume profile文件，这个文件保存了我们为场景添加的屏幕后处理特效和效果参数，Volume需要通过读取这个文件的数据来实现我们需要的效果。我们可以直接点击New按钮，unity会自动在当前场景所在目录下新建一个和场景同名的目录，然后在该目录下生成一个profile文件。或者我们可以在Project视图右键选择Create/Volume profile在当前目录下生成一个profile文件。

给Volume配置好profile文件之后，检视面板会变成下图所示：


