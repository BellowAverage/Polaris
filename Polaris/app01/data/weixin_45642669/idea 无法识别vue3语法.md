
--- 
title:  idea 无法识别vue3语法 
tags: []
categories: [] 

---
## 问题描述：
- 整合了vue3.js插件- 能够识别到vue标准语法和html语法- 第三方库的语法不支持
## 原因

因为没配置项目根路径，导致无法识别配置文件 而配置文件是识别第三方库语法所必须的。

我用vite操作的，需要这么几个包： <img src="https://img-blog.csdnimg.cn/791eb026d3ec4df2b481aaa02f727cd2.png" alt="在这里插入图片描述">
- 当识别到这几个配置文件以后，才能自动import- 如果没有解析这个文件，那就得主动imprt才能有语法提示
## 解决方案

<img src="https://img-blog.csdnimg.cn/1f9a60be4e5045b583dabd1c78d23b9e.png" alt="在这里插入图片描述">标注为源根即可。
