
--- 
title:  Python 爬虫（五）：PyQuery 框架 
tags: []
categories: [] 

---


#### 目录
- - <ul><li><ul><li>- - <ul><li>- 


PyQuery 是仿照 jQuery 实现的，语法与 jQuery 几乎完全相同，如果你熟悉 jQuery，又不想再记一套 BeautifulSoup （） 的调用方法，那么 PyQuery 是一个很好的选择。

## 1 准备工作

#### 1.1 安装

使用如下终端命令安装

`pip install pyquery`

安装完成后导包

`from pyquery import PyQuery as pq`

#### 1.2 初始化

**传入字符串**

```
from pyquery import PyQuery as pq

html = '''
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Hello PyQuery&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;ul id="container"&gt;
            &lt;li class="l1"&gt;l1&lt;/li&gt;
            &lt;li class="l2"&gt;l2&lt;/li&gt;
            &lt;li class="l3"&gt;l3&lt;/li&gt;
        &lt;/ul&gt;
    &lt;/body&gt;
&lt;/html&gt;
'''
doc = pq(html)
print(type(doc))
print(doc)

```

**传入文件**

```
from pyquery import PyQuery as pq

doc= pq(filename='p.html')
print(type(doc))
print(doc)

```

**传入 lxml.etree**

```
from pyquery import PyQuery as pq
from lxml import etree

doc = pq(etree.fromstring('&lt;html&gt;&lt;title&gt;Hello PyQuery&lt;/title&gt;&lt;/html&gt;'))
print(type(doc))
print(doc)

```

**传入 URL**

```
from pyquery import PyQuery as pq
doc = pq('http://www.baidu.com')
print(type(doc))
print(doc)

```

## 2 快速上手

#### 2.1 基本使用

**获取元素**

首先，我们使用 PyQuery 的 CSS 选择器获取指定元素。示例如下：

```
from pyquery import PyQuery as pq

html = '''
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Hello PyQuery&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;ul id="container"&gt;
            &lt;li class="l1"&gt;l1&lt;/li&gt;
            &lt;li class="l2"&gt;l2&lt;/li&gt;
            &lt;li class="l3"&gt;l3&lt;/li&gt;
        &lt;/ul&gt;
    &lt;/body&gt;
&lt;/html&gt;
'''
doc = pq(html)
# 获取 ul
ul = doc('#container')
# 获取 li
li = doc('ul li')
print(ul)
print(li)

```

**遍历元素**

```
from pyquery import PyQuery as pq

html = '''
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Hello PyQuery&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;ul id="container"&gt;
            &lt;li class="l1"&gt;l1&lt;/li&gt;
            &lt;li class="l2"&gt;l2&lt;/li&gt;
            &lt;li class="l3"&gt;l3&lt;/li&gt;
        &lt;/ul&gt;
    &lt;/body&gt;
&lt;/html&gt;
'''
doc = pq(html)
# 遍历 li
lis =doc('li').items()
for li in lis:
     print(li)

```

**存在多个相同元素时，获取指定元素**

```
from pyquery import PyQuery as pq

html = '''
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Hello PyQuery&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;ul id="container"&gt;
            &lt;li class="l1"&gt;l1&lt;/li&gt;
            &lt;li class="l2"&gt;l2&lt;/li&gt;
            &lt;li class="l3"&gt;l3&lt;/li&gt;
        &lt;/ul&gt;
    &lt;/body&gt;
&lt;/html&gt;
'''
doc = pq(html)
lis =doc('li').items()
# 获取第二个 li
l2 = list(lis)[1]
print(l2)

```

**获取父、子、兄弟元素**

PyQuery 可以通过方法直接获取指定元素的父、子、兄弟元素。示例如下：

```
from pyquery import PyQuery as pq

html = '''
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Hello PyQuery&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;

        &lt;ul&gt;&lt;/ul&gt;
        &lt;ul id="container"&gt;
            &lt;li class="l1"&gt;l1&lt;/li&gt;
            &lt;li class="l2"&gt;l2&lt;/li&gt;
            &lt;li class="l3"&gt;l3&lt;/li&gt;
        &lt;/ul&gt;
        &lt;ul&gt;&lt;/ul&gt;
    &lt;/body&gt;
&lt;/html&gt;
'''
doc = pq(html)
ul = doc('#container')
l2 = doc('#container .l2')
# 获取 ul 父元素
ul_parent = ul.parent()
# 获取 ul 子元素
ul_child = ul.children()
# 获取第二个 li 兄弟元素
l2_sib = l2.siblings()
print(ul_parent)
print(ul_child)
print(l2_sib)

```

**获取属性、文本信息**

```
from pyquery import PyQuery as pq

html = '''
&lt;html&gt;
    &lt;head&gt;
        &lt;title name='title'&gt;Hello PyQuery&lt;/title&gt;
    &lt;/head&gt;
&lt;/html&gt;
'''
doc = pq(html)
title =doc('title')
# 获取 name 属性
print(title.attr('name'))
# 获取 title 标签文本信息
print(title.text())

```

**获取 html**

```
from pyquery import PyQuery as pq

html = '''
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Hello PyQuery&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;ul id="container"&gt;
            &lt;li class="l1"&gt;l1&lt;/li&gt;
            &lt;li class="l2"&gt;l2&lt;/li&gt;
            &lt;li class="l3"&gt;l3&lt;/li&gt;
        &lt;/ul&gt;
    &lt;/body&gt;
&lt;/html&gt;
'''
doc = pq(html)
# 获取 ul 中 html
ul =doc('ul')
print(ul.html())

```

#### 2.2 伪类选择器

伪类可以根据一个元素的特征进行分类，下面通过示例了解下伪类选择器的使用。

```
from pyquery import PyQuery as pq

html = '''
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Hello PyQuery&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;ul id="container"&gt;
            &lt;li class="l1"&gt;l1&lt;/li&gt;
            &lt;li class="l2"&gt;l2&lt;/li&gt;
            &lt;li class="l3"&gt;l3last&lt;/li&gt;
        &lt;/ul&gt;
    &lt;/body&gt;
&lt;/html&gt;
'''
doc = pq(html)
# 设置起始位置
lis = doc('li:gt(-1)')
# 获取第一个 li
fli = doc('li:first-child')
# 获取最后一个 li
lli = doc('li:last-child')
# 获取指定 li
l2 = doc('li:nth-child(2)')
# 获取包含 last 的 li
cli = doc('li:contains("last")')
print(lis)
print(fli)
print(lli)
print(l2)
print(cli)

```

参考：



<img src="https://img-blog.csdnimg.cn/20191007101439261.JPG#pic_center" alt="在这里插入图片描述" width="600" height="350">
