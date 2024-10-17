
--- 
title:  最新Linux系统安装织梦DedeCMS V5.7 SP2模板图文教程 
tags: []
categories: [] 

---
第一步： 上传所有文件到服务器,并设置根目录有写入权限,

第二步： 打开浏览器输入http://你的网址/install/index.php 如果出现Dir 看，请往下看。

当打开安装页面的时候，你就会看到以下页面

<img src="https://img-blog.csdnimg.cn/20200718140120126.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

如果没有出现该页面，而是出现了一个空白页面写着dir

打开install目录 module-install.php.bak 和index.php.bak 把两个文件后面的.bak去掉 删除

install_lock.txt和index.html文件

同意协议勾上，然后点继续,之后会出现以下页面

<img src="https://img-blog.csdnimg.cn/2020071814015594.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

再继续。。下步讲进入填写数据库的步骤。 这个数据库是什么大家应该知道了吧。。 织梦

程序所需要的是 php空间 和 mysql数据库接上一步骤后。我们进入第三步

第三步： 你将看到以下页面。按照图示，填写相应的内容即可。 <img src="https://img-blog.csdnimg.cn/20200718140229661.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20200718140229600.png" alt="在这里插入图片描述">

（注意：默认数据包那个地方一定不能勾上，否则安装不成功）

以上填写好了就可以，其他地方，不修改，全默认。继续。

<img src="https://img-blog.csdnimg.cn/20200718140307306.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

第四步：点击“登录进入后台” 或者输入http://您的域名/dede/ 为了安全起见，dede这个文

件夹的名字一定要改掉，这个文件夹就是你后台登陆的网址

<img src="https://img-blog.csdnimg.cn/2020071814033239.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 按照图片提示步骤。进入系统数据库恢复页面

<img src="https://img-blog.csdnimg.cn/20200718140410184.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

点了数据还原后。你将看到的是我们程序备份的数据库。

<img src="https://img-blog.csdnimg.cn/20200718140512380.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

当数据库恢复完成以后，你将看到以下提示：

<img src="https://img-blog.csdnimg.cn/20200718140526761.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

数据还原到此就还原了，现在后台登陆的账号密码都变成admin了，不再是你安装时候所填

写的了

解释：因为小编在测试的时候用的都是admin，所以数据库备份后的账号密码都是admin，当你进行数据库还原后，账号和密码就都恢复到了admin，不再是你安装时候填写的账号和密码。所以数据库后还原后，大家需要修改密码。

所以大家还原数据后，要记得把密码修改下，

我们来继续下一步（设置网站系统参数）操作：

<img src="https://img-blog.csdnimg.cn/20200718140554578.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

到这里网站的设置就完成了。最后步骤。我们来生成整个站点的html页面。

先更新缓存，再生成全部

<img src="https://img-blog.csdnimg.cn/20200718140616895.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

因为是首次更新，所以要更新所有！（最好单独更新主页HTML 、更新栏目HTML、更新文档HTML）

如果更新栏目没反应 删除data/cache目录下的inc_catalog_base.inc 这个缓存文件即可更新栏目

<img src="https://img-blog.csdnimg.cn/20200718140631497.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

认真按照以上步骤安装后，织梦网站就能正常使用了

#### 常见问题汇总：

1、生成首页html的时候，后台是可以生成的，只是前台会

提示：……(略)/include/***/templets/default/index.htm Not Found!

然后栏目和文档则无法生成，后台会提示找不到模板文件。

解决思路：

出现问题的第一反应自然是百度找解决方法了，遗憾的是没找到……

所以，61源码网言梦小编就只能根据搜索来的信息自己想办法解决了。

首先可以确定的一点是：问题出在程序对网站的安装目录的读取。

解决方法：

在后台系统基本参数-核心设置里把DedeCMS安装目录设置为空。一般问题就解决了，如果还没解决：

打开data里的config.cache.bak.php和config.cache.inc.php

检查cfg_cmspath 的值是否为空，否则设置为空：$cfg_cmspath = ‘’;

2、后台左侧显示出现空白

解决： 修改/data/tplcache/ 文件夹的权限 chmod -R 777 tplcache tplcache
