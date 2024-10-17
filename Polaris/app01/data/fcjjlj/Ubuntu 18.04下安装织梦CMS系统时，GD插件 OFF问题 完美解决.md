
--- 
title:  Ubuntu 18.04下安装织梦CMS系统时，GD插件 OFF问题 完美解决 
tags: []
categories: [] 

---
出现这个问题一般是php-gd没有安装的问题，因此需要安装php-gd。

<img src="https://img-blog.csdnimg.cn/20200717192608520.png#pic_center" alt="在这里插入图片描述"> 安装如下：

```
~# sudo apt install php-gd

```

查看｀php-gd｀ 版本

```
~# php --ri gd

```

可以看到安装版本为2.2.5

```
gd

GD Support =&gt; enabled
GD headers Version =&gt; 2.2.5
GD library Version =&gt; 2.2.5
FreeType Support =&gt; enabled
FreeType Linkage =&gt; with freetype
FreeType Version =&gt; 2.8.1
GIF Read Support =&gt; enabled
GIF Create Support =&gt; enabled
JPEG Support =&gt; enabled
libJPEG Version =&gt; 8
PNG Support =&gt; enabled
libPNG Version =&gt; 1.6.34
WBMP Support =&gt; enabled
XPM Support =&gt; enabled
libXpm Version =&gt; 30411
XBM Support =&gt; enabled
WebP Support =&gt; enabled

Directive =&gt; Local Value =&gt; Master Value
gd.jpeg_ignore_warning =&gt; 1 =&gt; 1

```

重点来了，如果安装完php-gd插件之后，同时也确定gd为enable状态，但是DEDE安装界面显示gd依然为off，则说明还有某个地方有问题。

```
~# vim /var/www/www1/install/install.inc.php

```

打开目标文件夹里的install.inc.php，其中有个函数如下

```
function gdversion()

{<!-- -->

  //没启用php.ini函数的情况下如果有GD默认视作2.0以上版本

  //因为我是ubuntu服务器，没有配置php.ini，所以这里返回的是GD2.0版本，然而我的GD版本为2.2.5，所以手动配置版本号

  if(!function_exists('phpinfo'))
  {<!-- -->
   //if(function_exists('imagecreate')) return '2.0';注释掉这里改为下面的
     if(function_exists('imagecreate')) return '2.2.5';
     else return 0;
  }
  else
  {<!-- -->
    ob_start();
    phpinfo(8);
    $module_info = ob_get_contents();
    ob_end_clean();
    if(preg_match("/\bgd\s+version\b[^\d\n\r]+?([\d\.]+)/i", $module_info,$matches)) {<!-- -->   $gdversion_h = $matches[1];  }
    else {<!-- -->  $gdversion_h = 0; }
  //return $gdversion_h;把这一行也注释掉，修改为下面的代码
      return '2.2.5';
  }
}



```

查看结果 <img src="https://img-blog.csdnimg.cn/20200717193659422.png#pic_center" alt="在这里插入图片描述">
