
--- 
title:  构造user-agent池爬虫faker_useragent 
tags: []
categories: [] 

---
原因 一部分网站反爬，会通过检查请求的请求头里是否有浏览器的user-agent来判断请求是否是爬虫。当你在请求头里加上user-agent，然后，进行反复的请求后，系统又会判断请求时爬虫，因为单一版本浏览器请求过多，为了达到以假乱真的目的，你需要构建一个user-agent池，然后随机调用，那样相对比较繁琐但有效，如果你不想构造池呢，请看下面。

解决方法

```
pip install fake_useragent

from fake_useragent import UserAgent

headers = {<!-- -->
‘User-Agent’: UserAgent().random,
}

```
