
--- 
title:  dedecms织梦php7以上版本备份的数据还原不出来正常数据的解决方法 
tags: []
categories: [] 

---
dedecms织梦用php7以上版本备份的数据，在重新安装还原的时候，显示的数据不正常（如图）：

<img src="https://img-blog.csdnimg.cn/20201211212516476.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

出现这个是因为我们的数据是在php版本为7以上备份的，下面织梦58的符老师跟大家分享一下解决这个问题的方法：

首先我们找到后台目录 dede 文件夹(如果你后台改名了就不一定是dede)下的 sys_data_done.php 这个php文件打开,

查找

```
 $fs = $bakStr = '';

```

找到

```
$j = 0;
$fs = $bakStr = '';

```

把上面两行修改成

```
$j = 0;
$fs = array();
$bakStr = '';

```

即可。这样php7以上版本备份数据，还原后的数据就正常了。
