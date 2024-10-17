
--- 
title:  mysql写Shell小技巧_mysql写shell有几种方法 
tags: []
categories: [] 

---
1.Mysql数据库支持union的时候写文件小技巧： 采用常规的union写入，可以看到前面的字段占位数肯定也会被写入，替换成null也是一样的结果，这个对于写shell没啥大碍，mysql写Shell小技巧，但是如果用来写bat,mof,vbs等文件就会出问题了，那么怎么去掉这个只写入我们需要的内容呢？采用hex编码就好了。  

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/27427f8fdc234b51b0213590ab47d6aa.png">

将我们要写入的内容使用hex编码在分段写在每个字段位上，这样就可以只写入我们需要的内容了。 2.不支持union的时候写入，很多人都不知道这个办法，以为要写入内容必须要支持union，看到一篇文章，可以不需要支持这个办法。 语法：select * from admin where id=1 into outfile ‘F:\WWW\phpinfo.php’ fields terminated by ‘&lt;? phpinfo(); ?&gt;’%23   可以看到成功写入，但是这个方法有一个弊病就是查询出来的数据必须大于或等于2以上才可以写入内容，写入的内容数=查询出来的数据-1   可以看到，当我们使前面的数据出错查不到数据的时候，写入是失败的。 看看sqlmap中的情况：   可以很明显的看到sqlmap中也有这种办法写入。（burp抓取sqlmap数据包：加上 --proxy "http://127.0.0.1:8080/" 在burp里可以看到请求）   当然可
