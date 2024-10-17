
--- 
title:  sdl2.0使用SDL_RenderCopyEx进行图片旋转 
tags: []
categories: [] 

---
在sdl中，SDL_RenderCopyEx函数可以用来对图片进行旋转。

函数原型为：





renderer是我们当前窗口的渲染器。

texture是我们 将要旋转的图片资源。

srcrect代表我们将要旋转的texture中的某个矩形区域，如果为NULL则表示将会旋转整个texture图片。

dstrect代表旋转后的texture是在renderer上的dstrect的矩形区域内渲染（即出现），如果为NULL则表示作用在整个renderer上。

angle代表旋转的角度（360度为一个整圆），angle为正表示顺时针旋转angle角度，angle为负则逆时针旋转相应的角度。

center代表图片将要围绕旋转的点（即你的图片是围绕哪个点去旋转的），

flip表示旋转的方式，其中SDL_FLIP_HORIZONTAL 代表水平旋转,SDL_FLIP_VERTICAL 代表垂直翻转,SDL_FLIP_NONE 代表正常旋转。

关于例子我就不举了，因为我在另一篇博客中使用到了这个函数，有兴趣的可以去看下，

地址为：http://blog.csdn.net/qq_29883591/article/details/52824049。

 
