
--- 
title:  github数据怎么Python爬取 
tags: []
categories: [] 

---
## 爬虫流程

在上周写完用scrapy爬去知乎用户信息的爬虫之后，github上star个数一下就在公司小组内部排的上名次了，我还信誓旦旦的跟上级吹牛皮说如果再写一个，都不好意思和你再提star了，怕你们伤心。上级不屑的说，那就写一个爬虫爬一爬github，找一找python大牛，公司也正好在找人。临危受命，格外激动，当天就去研究github网站，琢磨怎么解析页面以及爬虫的运行策略。意外的发现github提供了非常nice的API以及文档文档，让我对github的爱已经深入骨髓。

说了这么多废话，讲讲真题吧。我需要下载github用户还有他们的reposities数据，展开方式也很简单，根据一个用户的following以及follower关系，遍历整个用户网就可以下载所有的数据了，听说github注册用户才几百万，一下就把所有的数据爬下来想想还有点小激动呢，下面是流程图：<img alt="" height="315" src="https://img-blog.csdnimg.cn/bbd2d626a19a4c4eba0098f1e3ffad5e.png" width="668">

## 递归实现

 

运行命令 看到这么简单的流程，内心的第一想法就是先简单的写一个递归实现呗，要是性能差再慢慢优化，所以第一版代码很快就完成了（在目录recursion下）。数据存储使用mongo，重复请求判断使用的redis，写mongo数据采用celery的异步调用，需要rabbitmq服务正常启动，在settings.py正确配置后，使用下面的步骤启动：

进入github_spider目录
