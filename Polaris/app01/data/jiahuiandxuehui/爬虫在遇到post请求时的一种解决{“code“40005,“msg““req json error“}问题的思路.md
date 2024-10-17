
--- 
title:  爬虫在遇到post请求时的一种解决{“code“:40005,“msg“:“req json error“}问题的思路 
tags: []
categories: [] 

---
## 我的情况

我在爬取某网站的时候发现网站做了防爬措施，在请求api的时候返回`{"code":40005,"msg":"req json error"}`遇到这种问题就要多分析你所爬取的网站是如何请求数据的，然后相应的修改你的请求头信息。

## 附上我的问题解决

<img src="https://img-blog.csdnimg.cn/bc98ca44b9ae42879ecd1380ec14f1d6.png" alt="在这里插入图片描述"> 然后发现在payload（负载）里面 <img src="https://img-blog.csdnimg.cn/f33773c847f4450ba074d8a6af19bad6.png" alt="在这里插入图片描述"> 这些请求负载也要转为json格式封装到请求头里面就可顺利请求api数据了。

## 总结

遇到请求数据返回失败的情况要多分析网站是如何请求的。查看自己是否请求头里面缺少必要的数据。
