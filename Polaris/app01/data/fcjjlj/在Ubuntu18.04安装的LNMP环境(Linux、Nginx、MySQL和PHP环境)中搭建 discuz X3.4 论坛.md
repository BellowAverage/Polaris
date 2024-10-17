
--- 
title:  在Ubuntu18.04安装的LNMP环境(Linux、Nginx、MySQL和PHP环境)中搭建 discuz X3.4 论坛 
tags: []
categories: [] 

---
1.在搭建`discuz`论坛时,先在`Ubuntu18.04`上搭建好`LNMP`环境,`LNMP`环境比以前的`LAMP`环境更加安全和全面,`https://blog.csdn.net/fcjjlj/article/details/106930077`(搭建`LNMP`参照此文档),多的不说,先开始安装吧! 2.在`LNMP`环境搭建好后先下载`discuz`安装包,可以上`discuz`找最近安装包,我现在用的是 Discuz_X3.4_SC_UTF8【20191201】 下载地址：https://gitee.com/3dming/DiscuzL/attach_files

php:

如果采用apt-get安装，安装路径应在 /etc/目录下

php的配置文件:/etc/php/7.2/fpm/php.ini

如果采用源代码安装，一般默认安装在/usr/local/lib目录下

php配置文件: /usr/local/lib/php.ini

或/usr/local/php/etc/php.ini

curl

如果采用源代码安装，一般默认安装在/usr/bin/curl

mysql:

如果采用apt-get安装，安装路径应在/usr/share/mysql目录下

mysqldump文件位置：/usr/bin/mysqldump

mysqli配置文件:

/etc/mysql/my.cnf或/usr/share/mysql/my.cnf

mysql数据目录在/var/lib/mysql目录下

如果采用源代码安装，一般默认安装在/usr/local/mysql目录下

### 步骤

1.将下载好的Discuz_X3.4_SC_UTF8【20191201】.zip文件通过ftp上传到服务器/var/cache/apt/archives目录下（为什么放到/var/cache/apt/archives？个人喜好，一般apt-get命令直接下载的文件都是在这个目录下，所以为了方便管理，我的习惯是把上传的压缩文件也放到这里）

2.执行命令 ~# unzip /var/cache/apt/archives/Discuz_X3.4_SC_UTF8【20191201】 ~# chmod -R 777 /root/upload ~# cp -r /root/upload/. /var/www/html

说明：由于我们在执行unzip命令的时候没有指定解压目录，所以系统默认解压到了/root文件夹下

~# 解压xxx.zip里面的yyy文件到dir目录 ~# unzip xxx.zip yyy -d dir ~# 如果解压的是tar.gz文件 ~# tar -zxvf 文件名 -C 指定目录 这里的/root/var/www/html路径是与前面nginx服务器区块配置里的路径一致

3.环境配置完成，最后就可以用浏览器直接访问 直接在浏览器中输入IP就会显示如下图所示页面， <img src="https://img-blog.csdnimg.cn/20200715200755313.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 然后点击 我同意! <img src="https://img-blog.csdnimg.cn/20200715200831218.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

出现下图 如果图中画红圈的位置出现不可写的情况，需要在文件对应目录下chmod -R 777 /对应文件/ 设置权限 <img src="https://img-blog.csdnimg.cn/20200715201902748.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 继续

#### linux上安装php的curl扩展

##### wget https://curl.haxx.se/download/curl-7.51.0.tar.gz

##### tar -zvxf curl-7.51.0.tar.gz

##### cd curl-7.51.0/

##### ./configure -prefix=/usr/local/curl

##### make

##### make install

##### export PATH=$PATH:/usr/local/curl/bin

测试是否可用

##### curl http://www.baidu.com

Cannot find config.m4.

Make sure that you run ‘/usr/bin/phpize’ in the top level source directory of the module

解决方法是

1进入到模块源码目录下

我的源码目录/root/php-7.2.24/

我安装的 插件是curl

也就是/root/php-7.2.24/ext/curl 目录下

2 执行phpize文件

/usr/bin/phpize

<img src="https://img-blog.csdnimg.cn/20200716192417434.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

得到以下结果就成功了 Configuring for: PHP Api Version: 20170718 Zend Module Api No: 20170718 Zend Extension Api No: 320170718
