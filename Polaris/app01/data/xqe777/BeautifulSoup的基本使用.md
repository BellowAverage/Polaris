
--- 
title:  BeautifulSoup的基本使用 
tags: []
categories: [] 

---
>  
 ✅作者简介：大家好我是hacker707,大家可以叫我hacker 📃个人主页： 🔥系列专栏： 💬推荐一款模拟面试、刷题神器👉 


<img src="https://img-blog.csdnimg.cn/59db859fd0624ae3b182e0fd5ed7ea63.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaGFja2VyNzA3,size_15,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">



#### bs4
- - <ul><li>- - - <ul><li>- <ul><li>- <ul><li>- - 


## bs4的安装

要使用BeautifulSoup4需要先安装lxml,再安装bs4

```
pip install lxml

```

```
pip install bs4

```

使用方法：

```
from bs4 import BeautifulSoup

```

lxml和bs4对比学习

```
from lxml import etree
tree = etree.HTML(html)
tree.xpath()

```

```
from bs4 import BeautifulSoup
soup =  BeautifulSoup(html_doc, 'lxml')

```

注意事项： 创建soup对象时如果不传’lxml’或者features="lxml"会出现以下警告 <img src="https://img-blog.csdnimg.cn/a7bcad884ffb4bacbd448f3534d98eb4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaGFja2VyNzA3,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### bs4的快速入门

### 解析器的比较(了解即可)

|解析器|用法|优点|缺点
|------
|python标准库|BeautifulSoup(markup,‘html.parser’)|python标准库，执行速度适中|(在python2.7.3或3.2.2之前的版本中)文档容错能力差
|lxml的HTML解析器|BeautifulSoup(markup,‘lxml’)|速度快，文档容错能力强|需要安装c语言库
|lxml的XML解析器|BeautifulSoup(markup,‘lxml-xml’)或者BeautifulSoup(markup,‘xml’)|速度快，唯一支持XML的解析器|需要安装c语言库
|html5lib|BeautifulSoup(markup,‘html5lib’)|最好的容错性，以浏览器的方式解析文档，生成HTML5格式的文档|速度慢，不依赖外部扩展

### 对象种类

>  
 Tag：标签 BeautifulSoup：bs对象 NavigableString：可导航的字符串 Comment：注释 


```
from bs4 import BeautifulSoup

# 创建模拟HTML代码的字符串
html_doc = """
&lt;html&gt;&lt;head&gt;&lt;title&gt;The Dormouse's story&lt;/title&gt;&lt;/head&gt;
&lt;body&gt;
&lt;p class="title"&gt;&lt;b&gt;The Dormouse's story&lt;/b&gt;&lt;/p&gt;

&lt;p class="story"&gt;Once upon a time there were three little sisters; and their names were
&lt;a href="http://example.com/elsie" class="sister" id="link1"&gt;Elsie&lt;/a&gt;,
&lt;a href="http://example.com/lacie" class="sister" id="link2"&gt;Lacie&lt;/a&gt; and
&lt;a href="http://example.com/tillie" class="sister" id="link3"&gt;Tillie&lt;/a&gt;;
and they lived at the bottom of a well.&lt;/p&gt;

&lt;p class="story"&gt;...&lt;/p&gt;

&lt;span&gt;&lt;!--comment注释内容举例--&gt;&lt;/span&gt;
"""
# 创建soup对象
soup = BeautifulSoup(html_doc, 'lxml')
print(type(soup.title))  # &lt;class 'bs4.element.Tag'&gt;
print(type(soup))  # &lt;class 'bs4.BeautifulSoup'&gt;
print(type(soup.title.string))  # &lt;class 'bs4.element.NavigableString'&gt;
print(type(soup.span.string))  # &lt;class 'bs4.element.Comment'&gt;

```

#### bs4的简单使用

<font color="#0099ff" size="4"> 获取标签内容</font>

```
from bs4 import BeautifulSoup

# 创建模拟HTML代码的字符串
html_doc = """
&lt;html&gt;&lt;head&gt;&lt;title&gt;The Dormouse's story&lt;/title&gt;&lt;/head&gt;
&lt;body&gt;
&lt;p class="title"&gt;&lt;b&gt;The Dormouse's story&lt;/b&gt;&lt;/p&gt;

&lt;p class="story"&gt;Once upon a time there were three little sisters; and their names were
&lt;a href="http://example.com/elsie" class="sister" id="link1"&gt;Elsie&lt;/a&gt;,
&lt;a href="http://example.com/lacie" class="sister" id="link2"&gt;Lacie&lt;/a&gt; and
&lt;a href="http://example.com/tillie" class="sister" id="link3"&gt;Tillie&lt;/a&gt;;
and they lived at the bottom of a well.&lt;/p&gt;

&lt;p class="story"&gt;...&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
"""
# 创建soup对象
soup = BeautifulSoup(html_doc, 'lxml')
print('head标签内容:\n', soup.head)  # 打印head标签
print('body标签内容:\n', soup.body)  # 打印body标签
print('html标签内容:\n', soup.html)  # 打印html标签
print('p标签内容:\n', soup.p)  # 打印p标签

```

✅注意：在打印p标签对应的代码时，可以发现只打印了第一个p标签内容，这时我们可以通过find_all来获取p标签全部内容

```
print('p标签内容:\n', soup.find_all('p'))

```

✅这里需要注意使用find_all里面必须传入的是字符串 <font color="#0099ff" size="4"> 获取标签名字</font> 通过name属性获取标签名字

```
from bs4 import BeautifulSoup

# 创建模拟HTML代码的字符串
html_doc = """
&lt;html&gt;&lt;head&gt;&lt;title&gt;The Dormouse's story&lt;/title&gt;&lt;/head&gt;
&lt;body&gt;
&lt;p class="title"&gt;&lt;b&gt;The Dormouse's story&lt;/b&gt;&lt;/p&gt;

&lt;p class="story"&gt;Once upon a time there were three little sisters; and their names were
&lt;a href="http://example.com/elsie" class="sister" id="link1"&gt;Elsie&lt;/a&gt;,
&lt;a href="http://example.com/lacie" class="sister" id="link2"&gt;Lacie&lt;/a&gt; and
&lt;a href="http://example.com/tillie" class="sister" id="link3"&gt;Tillie&lt;/a&gt;;
and they lived at the bottom of a well.&lt;/p&gt;

&lt;p class="story"&gt;...&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
"""
# 创建soup对象
soup = BeautifulSoup(html_doc, 'lxml')
print('head标签名字:\n', soup.head.name)  # 打印head标签名字
print('body标签名字:\n', soup.body.name)  # 打印body标签名字
print('html标签名字:\n', soup.html.name)  # 打印html标签名字
print('p标签名字:\n', soup.find_all('p').name)  # 打印p标签名字

```

✅如果要找到两个标签的内容，需要传入列表过滤器，而不是字符串过滤器 使用字符串过滤器获取多个标签内容会返回空列表

```
print(soup.find_all('title', 'p'))

```

```
[]

```

需要使用列表过滤器获取多个标签内容

```
print(soup.find_all(['title', 'p']))

```

```
[&lt;title&gt;The Dormouse's story&lt;/title&gt;, &lt;p class="title"&gt;&lt;b&gt;The Dormouse's story&lt;/b&gt;&lt;/p&gt;, &lt;p class="story"&gt;Once upon a time there were three little sisters; and their names were
&lt;a class="sister" href="http://example.com/elsie" id="link1"&gt;Elsie&lt;/a&gt;,
&lt;a class="sister" href="http://example.com/lacie" id="link2"&gt;Lacie&lt;/a&gt; and
&lt;a class="sister" href="http://example.com/tillie" id="link3"&gt;Tillie&lt;/a&gt;;
and they lived at the bottom of a well.&lt;/p&gt;, &lt;p class="story"&gt;...&lt;/p&gt;]

```

<font color="#0099ff" size="4"> 获取a标签的href属性值</font>

```
from bs4 import BeautifulSoup

# 创建模拟HTML代码的字符串
html_doc = """
&lt;html&gt;&lt;head&gt;&lt;title&gt;The Dormouse's story&lt;/title&gt;&lt;/head&gt;
&lt;body&gt;
&lt;p class="title"&gt;&lt;b&gt;The Dormouse's story&lt;/b&gt;&lt;/p&gt;

&lt;p class="story"&gt;Once upon a time there were three little sisters; and their names were
&lt;a href="http://example.com/elsie" class="sister" id="link1"&gt;Elsie&lt;/a&gt;,
&lt;a href="http://example.com/lacie" class="sister" id="link2"&gt;Lacie&lt;/a&gt; and
&lt;a href="http://example.com/tillie" class="sister" id="link3"&gt;Tillie&lt;/a&gt;;
and they lived at the bottom of a well.&lt;/p&gt;

&lt;p class="story"&gt;...&lt;/p&gt;
"""
# 创建soup对象
soup = BeautifulSoup(html_doc, 'lxml')
a_list = soup.find_all('a')
# 遍历列表取属性值
for a in a_list:
    # 第一种方法通过get去获取href属性值(没有找到返回None)
    print(a.get('href'))
    # 第二种方法先通过attrs获取所有属性值，再提取出你想要的属性值
    print(a.attrs['href'])
    # 第三种方法获取没有的属性值会报错
    print(a['href'])

```

✅扩展：使用prettify()美化 让节点层级关系更加明显 方便分析

```
print(soup.prettify())

```

不使用prettify时的代码

```
&lt;html&gt;&lt;head&gt;&lt;title&gt;The Dormouse's story&lt;/title&gt;&lt;/head&gt;
&lt;body&gt;
&lt;p class="title"&gt;&lt;b&gt;The Dormouse's story&lt;/b&gt;&lt;/p&gt;
&lt;p class="story"&gt;Once upon a time there were three little sisters; and their names were
&lt;a class="sister" href="http://example.com/elsie" id="link1"&gt;Elsie&lt;/a&gt;,
&lt;a class="sister" href="http://example.com/lacie" id="link2"&gt;Lacie&lt;/a&gt; and
&lt;a class="sister" href="http://example.com/tillie" id="link3"&gt;Tillie&lt;/a&gt;;
and they lived at the bottom of a well.&lt;/p&gt;
&lt;p class="story"&gt;...&lt;/p&gt;
&lt;/body&gt;&lt;/html&gt;

```

使用prettify时的代码

```
&lt;html&gt;
 &lt;head&gt;
  &lt;title&gt;
   The Dormouse's story
  &lt;/title&gt;
 &lt;/head&gt;
 &lt;body&gt;
  &lt;p class="title"&gt;
   &lt;b&gt;
    The Dormouse's story
   &lt;/b&gt;
  &lt;/p&gt;
  &lt;p class="story"&gt;
   Once upon a time there were three little sisters; and their names were
   &lt;a class="sister" href="http://example.com/elsie" id="link1"&gt;
    Elsie
   &lt;/a&gt;
   ,
   &lt;a class="sister" href="http://example.com/lacie" id="link2"&gt;
    Lacie
   &lt;/a&gt;
   and
   &lt;a class="sister" href="http://example.com/tillie" id="link3"&gt;
    Tillie
   &lt;/a&gt;
   ;
and they lived at the bottom of a well.
  &lt;/p&gt;
  &lt;p class="story"&gt;
   ...
  &lt;/p&gt;
 &lt;/body&gt;
&lt;/html&gt;

```

##### 遍历文档树

```
from bs4 import BeautifulSoup

# 创建模拟HTML代码的字符串
html_doc = """
&lt;html&gt;&lt;head&gt;&lt;title&gt;The Dormouse's story&lt;/title&gt;&lt;/head&gt;
&lt;body&gt;
&lt;p class="title"&gt;&lt;b&gt;The Dormouse's story&lt;/b&gt;&lt;/p&gt;

&lt;p class="story"&gt;Once upon a time there were three little sisters; and their names were
&lt;a href="http://example.com/elsie" class="sister" id="link1"&gt;Elsie&lt;/a&gt;,
&lt;a href="http://example.com/lacie" class="sister" id="link2"&gt;Lacie&lt;/a&gt; and
&lt;a href="http://example.com/tillie" class="sister" id="link3"&gt;Tillie&lt;/a&gt;;
and they lived at the bottom of a well.&lt;/p&gt;

&lt;p class="story"&gt;...&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
"""
soup = BeautifulSoup(html_doc, 'lxml')
head = soup.head
# contents返回的是所有子节点的列表 [&lt;title&gt;The Dormouse's story&lt;/title&gt;]
print(head.contents)
# children返回的是一个子节点的迭代器 &lt;list_iterator object at 0x00000264BADC2748&gt;
print(head.children)
# 凡是迭代器都是可以遍历的
for h in head.children:
    print(h)
html = soup.html  # 会把换行也当作子节点匹配到
# descendants 返回的是一个生成器遍历子子孙孙  &lt;generator object Tag.descendants at 0x0000018C15BFF4C8&gt;
print(html.descendants)
# 凡是生成器都是可遍历的
for h in html.descendants:
    print(h)

'''
需要重点掌握的
string获取标签里面的内容
strings 返回是一个生成器对象用过来获取多个标签内容
stripped_strings 和strings基本一致 但是它可以把多余的空格去掉
'''
print(soup.title.string)
print(soup.html.string)
# 返回生成器对象&lt;generator object Tag._all_strings at 0x000001AAFF9EF4C8&gt;
# soup.html.strings 包含在html标签里面的文本都会被获取到
print(soup.html.strings)
for h in soup.html.strings:
    print(h)
# stripped_strings可以把多余的空格去掉
# 返回生成器对象&lt;generator object PageElement.stripped_strings at 0x000001E31284F4C8&gt;
print(soup.html.stripped_strings)
for h in soup.html.stripped_strings:
    print(h)
'''
parent直接获得父节点
parents获取所有的父节点
'''
title = soup.title
# parent找直接父节点
print(title.parent)
# parents获取所有父节点
# 返回生成器对象&lt;generator object PageElement.parents at 0x000001F02049F4C8&gt;
print(title.parents)
for p in title.parents:
    print(p)
# html的父节点就是整个文档
print(soup.html.parent)
# &lt;class 'bs4.BeautifulSoup'&gt;
print(type(soup.html.parent))

```

###### 案例练习

获取所有职位名称

```
html = """
&lt;table class="tablelist" cellpadding="0" cellspacing="0"&gt;
    &lt;tbody&gt;
        &lt;tr class="h"&gt;
            &lt;td class="l" width="374"&gt;职位名称&lt;/td&gt;
            &lt;td&gt;职位类别&lt;/td&gt;
            &lt;td&gt;人数&lt;/td&gt;
            &lt;td&gt;地点&lt;/td&gt;
            &lt;td&gt;发布时间&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="even"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=33824&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;22989-金融云区块链高级研发工程师（深圳）&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;1&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-25&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="odd"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=29938&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;22989-金融云高级后台开发&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;2&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-25&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="even"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=31236&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;SNG16-腾讯音乐运营开发工程师（深圳）&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;2&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-25&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="odd"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=31235&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;SNG16-腾讯音乐业务运维工程师（深圳）&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;1&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-25&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="even"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=34531&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;TEG03-高级研发工程师（深圳）&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;1&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-24&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="odd"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=34532&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;TEG03-高级图像算法研发工程师（深圳）&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;1&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-24&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="even"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=31648&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;TEG11-高级AI开发工程师（深圳）&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;4&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-24&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="odd"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=32218&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;15851-后台开发工程师&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;1&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-24&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="even"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=32217&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;15851-后台开发工程师&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;1&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-24&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="odd"&gt;
            &lt;td class="l square"&gt;&lt;a id="test" class="test" target='_blank' href="position_detail.php?id=34511&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;SNG11-高级业务运维工程师（深圳）&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;1&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-24&lt;/td&gt;
        &lt;/tr&gt;
    &lt;/tbody&gt;
&lt;/table&gt;
"""

```

###### 思路

不难看出想要的数据在tr节点的a标签里，只需要遍历所有的tr节点，从遍历出来的tr节点取a标签里面的文本数据

###### 代码实现

```
from bs4 import BeautifulSoup

html = """
&lt;table class="tablelist" cellpadding="0" cellspacing="0"&gt;
    &lt;tbody&gt;
        &lt;tr class="h"&gt;
            &lt;td class="l" width="374"&gt;职位名称&lt;/td&gt;
            &lt;td&gt;职位类别&lt;/td&gt;
            &lt;td&gt;人数&lt;/td&gt;
            &lt;td&gt;地点&lt;/td&gt;
            &lt;td&gt;发布时间&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="even"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=33824&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;22989-金融云区块链高级研发工程师（深圳）&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;1&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-25&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="odd"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=29938&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;22989-金融云高级后台开发&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;2&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-25&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="even"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=31236&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;SNG16-腾讯音乐运营开发工程师（深圳）&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;2&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-25&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="odd"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=31235&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;SNG16-腾讯音乐业务运维工程师（深圳）&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;1&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-25&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="even"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=34531&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;TEG03-高级研发工程师（深圳）&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;1&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-24&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="odd"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=34532&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;TEG03-高级图像算法研发工程师（深圳）&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;1&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-24&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="even"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=31648&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;TEG11-高级AI开发工程师（深圳）&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;4&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-24&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="odd"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=32218&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;15851-后台开发工程师&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;1&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-24&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="even"&gt;
            &lt;td class="l square"&gt;&lt;a target="_blank" href="position_detail.php?id=32217&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;15851-后台开发工程师&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;1&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-24&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr class="odd"&gt;
            &lt;td class="l square"&gt;&lt;a id="test" class="test" target='_blank' href="position_detail.php?id=34511&amp;keywords=python&amp;tid=87&amp;lid=2218"&gt;SNG11-高级业务运维工程师（深圳）&lt;/a&gt;&lt;/td&gt;
            &lt;td&gt;技术类&lt;/td&gt;
            &lt;td&gt;1&lt;/td&gt;
            &lt;td&gt;深圳&lt;/td&gt;
            &lt;td&gt;2017-11-24&lt;/td&gt;
        &lt;/tr&gt;
    &lt;/tbody&gt;
&lt;/table&gt;
"""
# 创建soup对象
soup = BeautifulSoup(html, 'lxml')
# 使用find_all()找到所有的tr节点(经过观察第一个tr节点为表头,忽略不计)
tr_list = soup.find_all('tr')[1:]
# 遍历tr_list取a标签里的文本数据
for tr in tr_list:
    a_list = tr.find_all('a')
    print(a_list[0].string)

```

运行结果如下：

```
22989-金融云区块链高级研发工程师（深圳）
22989-金融云高级后台开发
SNG16-腾讯音乐运营开发工程师（深圳）
SNG16-腾讯音乐业务运维工程师（深圳）
TEG03-高级研发工程师（深圳）
TEG03-高级图像算法研发工程师（深圳）
TEG11-高级AI开发工程师（深圳）
15851-后台开发工程师
15851-后台开发工程师
SNG11-高级业务运维工程师（深圳）

```

🔥以上就是bs4的基本使用，如果有改进的建议，欢迎在评论区留言奥~

<img src="https://img-blog.csdnimg.cn/849fcb7d8485429c853317b25fcce340.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaGFja2VyNzA3,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">
