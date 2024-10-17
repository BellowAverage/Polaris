
--- 
title:  接入谷歌AdSense后浏览器控制台报错：Failed to load resource: the server responded with a status of 403的原因及解决办法、 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解，接入谷歌AdSense后浏览器控制台报错：Failed to load resource: the server responded with a status of 403 ads 的原因及解决办法。 日期：2023年6月1日 作者：任聪聪 


### 主要现象：

<img src="https://img-blog.csdnimg.cn/2ae6801808054dd4aa3c665bc8c29ec8.png" alt="在这里插入图片描述"> ads:1的具体报错内容：

```
https://googleads.g.doubleclick.net/pagead/ads.......此处省略大部分参数信息。

```

### 主要原因及解决办法

说明：这个报错其实就是审核权限没有通过的原因，不必惊慌或者进行变更操作。

#### 主要原因

谷歌AdSense为审核通过导致。

#### 解决办法

等待谷歌审核通过即可。

### 其他问题解答

#### 1.ads.txt一直提示找不到是什么原因？

答：ads.txt一般要等网站审核通过后的一到两周会出现变化。但前提一定要记得robots.txt协议没有禁止抓取ads文件，同时防火墙没有墙掉外部访问这个文件的可能。

robots.txt协议建议不限制抓取配置:

```
User-Agent: *
Allow: /

```

#### 2.AdSense网站审核一般是多久时间？

答：一般是1-4周，大部分在2-3周审核通过，基本上只要是网站有内容，最近有更新且网站内容符合法律规定那么就能够通过审核。
