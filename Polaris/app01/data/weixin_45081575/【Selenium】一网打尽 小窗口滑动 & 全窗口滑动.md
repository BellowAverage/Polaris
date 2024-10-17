
--- 
title:  【Selenium】一网打尽 小窗口滑动 & 全窗口滑动 
tags: []
categories: [] 

---
## 前言

>  
 收到小伙伴私信，如果web页面中含有小页面，该怎样使用Selenium去滑动小页面，这里总结记录一下。 


## 知识点📖📖

**都是JavaScript的知识~~**

|方法|释义
|------
|window.scrollBy(x,y)|滑动指定的x和y的距离
|document.body.scrollHeight|元素内容高度的度量
|document.querySelector()|根据指定选择器查找元素
|getElementById()|根据id获取元素
|getElementsByClassName()|根据class name 获取元素
|getElementsByName()|根据name 获取元素
|getElementsByTagName()|根据 tag name 获取元素
|…|…

看下图
- **https://developer.mozilla.org/zh-CN/docs/Web/API/Document/querySelector**<img src="https://img-blog.csdnimg.cn/4fb0f13795894244aff1d69135fdec89.png" alt="">
**关于页面滑动**
- window对象可以，Element也可以- **https://developer.mozilla.org/zh-CN/docs/Web/API/Element/scrollBy** <img src="https://img-blog.csdnimg.cn/c8c3e253dc8e4768b1fc63efabe6afcc.png" alt="">
## 完整代码

**window滑动**

```
// 直接滑动
window.scrollBy(0, document.body.scrollHeight)

```

**元素滑动**

```
// 先定位
element = document.getElementsByClassName("xxx")[0]
// 再滑动
element.scrollBy(0, document.body.scrollHeight)

```

123

## 实现🐱‍🏍🐱‍🏍

### Selenium执行Js代码

在使用Selenium时候，需要进行页面滑动都是通过执行Js代码的方式。这里也不例外~ Selenium执行Js代码 示例代码如下

```
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()
    js_code = 'alert("Hello World!")'
    driver.execute_script(script=js_code)


```

代码运行效果如下动图所示：
- 执行了 `alert("Hello World!")`，在浏览器控制台输入 `alert("Hello World!")` 也是一样的效果~ <img src="https://img-blog.csdnimg.cn/ad5aaa77854845a89a44333fcf671443.png" alt=""> ========================================================= <img src="https://img-blog.csdnimg.cn/05f2998372354a36926cb611faaea1ee.gif" alt="">
### 全窗口滑动

从下图中可以看到，
- document.body.scrollHeight，页面高度- window.scrollBy(0, 1500)，将页面往下滚动1500的高度 <img src="https://img-blog.csdnimg.cn/d0831baf00734822850c805ae42dbfa0.png" alt="">
**Selenium执行的代码如下：**

```
js_code = 'window.scrollBy(0, 1500)'	# 滑动指定距离
js_code = 'window.scrollBy(0, document.body.scrollHeight)'	# 滑动到底
driver.execute_script(script=js_code)

```

### 小窗口滑动

>  
 这个比全窗口要多一个操作，那就是先定位到小窗口 


这里不针对任何网站，所以只介绍思路，思路是通用的~

假设小窗口的`html`标签如下，

```
&lt;div class="hello" id="world" name="frica"&gt;

```

通过上面介绍的 `getElementsByClassName()...` 可以轻松定位到，

```
// 这里是三种定位方式，当然，定位的方式还有好几种，不做过多描述！
document.getElementsByClassName("hello")
document.getElementById("world")
document.getElementsByName("frica")

```

然后再进行滑动就完事了
- 这里还需要注意一下返回对象类型，有的是数组对象，有的元素对象~
```
document.getElementsByClassName('hello')[0].scrollBy(0, 1000)
//
document.getElementById("world").scrollBy(0, 1000)
...

```

**Selenium执行的代码如下：**

```
js_code = 'document.getElementsByClassName("hello")[0].scrollBy(0, 1500)'	# 滑动指定距离
js_code = 'document.getElementsByClassName("hello")[0].scrollBy(0, document.body.scrollHeight)'	# 滑动到底
driver.execute_script(script=js_code)

```

## 后话

本次分享先到这， see you.🎈🎈
