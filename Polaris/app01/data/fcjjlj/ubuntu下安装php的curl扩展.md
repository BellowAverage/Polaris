
--- 
title:  ubuntu下安装php的curl扩展 
tags: []
categories: [] 

---
```
apt-get install curl-devel

apt-get install curl


./configure --with-php-config=/usr/bin/php-config

cd /root/php-7.2.24/ext/curl

invoke-rc.d php-cgi restart


/usr/bin/phpize

php -m

sudo apt-get install libcurl4-openssl-dev

cd /root/curl-7.51.0/

./configure -prefix=/usr/bin/curl

php -m

```

<img src="https://img-blog.csdnimg.cn/20200824180325365.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">
