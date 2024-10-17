
--- 
title:  dedecms5.7(织梦)源码解析之后台登录 
tags: []
categories: [] 

---
##### 前言

在安装完成之后，我们通常会进入后台，那么登录自然是必不可少的一步，下面我们就来看看，织梦的登录在源码中是究竟如何完成的吧。

##### 过程

首先，如果我们直接访问域名/dede,那么程序走的肯定是index.php，文件源码如下：

```
&lt;?php
  /**
   * 管理后台首页
    *
    * @version        $Id: index.php 1 11:06 2010年7月13日Z tianya $
    * @package        DedeCMS.Administrator
    * @copyright      Copyright (c) 2007 - 2010, DesDev, Inc.
    * @license        http://help.dedecms.com/usersguide/license.html
    * @link           http://www.dedecms.com
    */
    require_once(dirname(__FILE__)."/config.php");
    require_once(DEDEINC.'/dedetag.class.php');
    $defaultIcoFile = DEDEDATA.'/admin/quickmenu.txt';
    $myIcoFile =
    DEDEDATA.'/admin/quickmenu-'.$cuserLogin-&gt;getUserID().'.txt';
    
    if(!file_exists($myIcoFile)) $myIcoFile = $defaultIcoFile;
    
    require(DEDEADMIN.'/inc/inc_menu_map.php');
    include(DEDEADMIN.'/templets/index2.htm');
    exit();

```

从源码中不难看出，该页面主要是起统领作用，包含了如下几个文件：
- /dede/config.php : 管理目录配置文件- /include/dedetag.class.php : 模板类- /dede/inc/inc_menu_map.php : 菜单地图- /dede/templates/index2.html :后台首页模板
它的执行顺序分别为：
1. 分别加载config.php和dedetag.class.php两个文件1. 分别载入通用快捷菜单模板和当前用户快捷菜单模板,该模板最终会显示在登录后的首页的快捷操作栏中1. 最后载入菜单地图和首页模板
到此为止，你也许会问，那么程序是在哪里判断登录的呢？从index.php中貌似也没有看到关于登录的地方啊，为什么我输入index.php而会直接跳转到后面跟一堆参数的logo.php呢？别急，其实它就在config.php中，看下面源码：

```
//获得当前脚本名称，如果你的系统被禁用了$_SERVER变量，请自行更改这个选项
$dedeNowurl = $s_scriptName = '';
$isUrlOpen = @ini_get('allow_url_fopen');
$dedeNowurl = GetCurUrl();
$dedeNowurls = explode('?', $dedeNowurl);
$s_scriptName = $dedeNowurls[0];
$cfg_remote_site = empty($cfg_remote_site)? 'N' : $cfg_remote_site;

//检验用户登录状态
$cuserLogin = new userLogin();
if($cuserLogin-&gt;getUserID()==-1)
{<!-- -->
    header("location:login.php?gotopage=".urlencode($dedeNowurl));
    exit();
}

```

在上面代码中，程序首先获取了当前的脚本网址以及对其尽心拆解处理，然后实例化织梦的登录类，根据当前用户id来判断用户是否登录，如果没有，则跳转到login.php，后面的一堆参数也就是之前的脚本网址urlencode之后的结果。 好，既然到了login.php了，那我们就继续来看看，在login.php页面中，是如何处理的吧。 login.php文件源码大概可以分为以下几块：
- 分别载入全局配置文件和登录类- 检测安装目录安全性，如果没有写入锁文件，这里则再次写入一次（双保险），然后将两个可执行的php文件修改备注为php.bak,使其失去可执行性，最后新增index.html文件，内容为dir,增加安全性，这一切都是为了防止恶意用户重复安装，导致网站损坏。
```
//检测安装目录安全性
if( is_dir(dirname(__FILE__).'/../install') )
{<!-- -->
    if(!file_exists(dirname(__FILE__).'/../install/install_lock.txt') )
    {<!-- -->
      $fp = fopen(dirname(__FILE__).'/../install/install_lock.txt', 'w') or die('安装目录无写入权限，无法进行写入锁定文件，请安装完毕删除安装目录！');
      fwrite($fp,'ok');
      fclose($fp);
    }
    //为了防止未知安全性问题，强制禁用安装程序的文件
    if( file_exists("../install/index.php") ) {<!-- -->
        @rename("../install/index.php", "../install/index.php.bak");
    }
    if( file_exists("../install/module-install.php") ) {<!-- -->
        @rename("../install/module-install.php", "../install/module-install.php.bak");
    }
    $fileindex = "../install/index.html";
    if( !file_exists($fileindex) ) {<!-- -->
        $fp = @fopen($fileindex,'w');
        fwrite($fp,'dir');
        fclose($fp);
    }
}

```
- 更新服务器- 检测后台目录是否更名，为了安全性，如果检测到没有更名，则会提示- 登录检测 : 这一步就是检测验证码，用户名，和密码，成功后跳转到首页- 包含登录页面模板
那么，到此登录就基本结束了，其中有两个地方再说一下，一个是参数gotopage和另一个dohost,这两个参数或变量均在login.html中可以找到，具体详细流程大家可自行研究，关于gotopage，为了安全性，在login.html中可以看到，此处用了removeXSS函数，防止xxs攻击：

```
&lt;input type="hidden" name="gotopage" value="&lt;?php if(!empty($gotopage)) echo RemoveXSS($gotopage);?&gt;" /&gt;
&lt;input type="hidden" name="dopost" value="login" /&gt;

```

##### 总结

殊途同归，登录无非就是判断登录状态=》没有登录则跳转到登录页面=》登录了则跳转到首页，剩下的基本就是参数处理和表单验证了，把握好核心，一切都能随心。
