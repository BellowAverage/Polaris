
--- 
title:  不需要K值实现打开链接、扫码即可在手机、电脑端弹出QQ添加好友框的方法 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解：pc与手机端浏览器打开链接即可弹出QQ好友添加框的代码实现方式 日期：2022年10月22日 


有很多朋友，会觉得qq添加好友需要提供链接里的k值，但是实际上方向错了，k值是腾讯那边加密过的，因为看过很多QQ开放社区文档，没有找到K值的获取方式，所以我们是拿不到的。但是qq那边不仅仅只是提供了一种弹出框方法而是多种，我们可以用其他方法来解决这个问题。

#### 一、效果说明

1.pc电脑端浏览器打开即可弹出添加好友框。 <img src="https://img-blog.csdnimg.cn/57bafa9688f741dba339e1fcc6039716.png" alt="在这里插入图片描述">

2.手机浏览器无论是安卓还是苹果ios系统打开即可弹出添加好友框。 <img src="https://img-blog.csdnimg.cn/0369b85b31b846c6a7df94876d2dfdeb.png" alt="在这里插入图片描述">

#### 二、实现思路

1.PC端使用如下链接

```
//支持pc任意浏览器
tencent://AddContact/?fromId=45&amp;fromSubId=1&amp;subcmd=all&amp;uin=改成你的QQ

```

2.手机端使用如下链接

```
//支持ios、andorid
mqqapi://card/show_pslcard?src_type=internal&amp;version=1&amp;uin=改成你的QQ&amp;card_type=person&amp;source=sharecard

```

#### 三、嵌入html界面，利用js进行执行

```
&lt;html&gt;
&lt;script language="javascript" type="text/javascript"&gt;
    /**适用于PC和任何手机跳转qq添加好友界面的实例**/
    const uag = navigator.userAgent;
    const ipad = uag.match(/(iPad).*OS\s([\d_]+)/),
    isMqVer = !ipad &amp;&amp; uag.match(/(iPhone\sOS)\s([\d_]+)/) || uag.match(/(Android)\s+([\d.]+)/);
    if(isMqVer){<!-- -->
        //手机端自动打开弹出 包括苹果ios、安卓等均可弹出
        location.href="mqqapi://card/show_pslcard?src_type=internal&amp;version=1&amp;uin=改成你的QQ&amp;card_type=person&amp;source=sharecard";
    }else{<!-- -->
        //pc浏览器默认打开弹出
        location.href="tencent://AddContact/?fromId=45&amp;fromSubId=1&amp;subcmd=all&amp;uin=改成你的QQ";
    }
&lt;/script&gt;
&lt;/html&gt;
 

```

#### 四、其他界面应用说明

##### 1.实现一个界面自适应动态弹出添加框的方式

思路：利用get参数获取qq，并通过上述的html界面进行执行弹出框，以php为例，如下：

```
&lt;html&gt;
&lt;script language="javascript" type="text/javascript"&gt;
    /**适用于PC和任何手机跳转qq添加好友界面的实例**/
    const uag = navigator.userAgent;
    const ipad = uag.match(/(iPad).*OS\s([\d_]+)/),
    isMqVer = !ipad &amp;&amp; uag.match(/(iPhone\sOS)\s([\d_]+)/) || uag.match(/(Android)\s+([\d.]+)/);
    if(isMqVer){<!-- -->
        //手机端自动打开弹出 包括苹果ios、安卓等均可弹出
        location.href="mqqapi://card/show_pslcard?src_type=internal&amp;version=1&amp;uin=&lt;?php echo $_GET['you_qq_number'];?&gt;&amp;card_type=person&amp;source=sharecard";
    }else{<!-- -->
        //pc浏览器默认打开弹出
        location.href="tencent://AddContact/?fromId=45&amp;fromSubId=1&amp;subcmd=all&amp;uin=&lt;?php echo $_GET['you_qq_number'];?&gt;";
    }
&lt;/script&gt;
&lt;/html&gt;

```

##### 2.实现二维码扫码后弹出添加好友弹出框

思路：利用上述的链接，我们把url用qcorde.js插件进行生成一个二维码，并绑定这个链接。

>  
 扫码功能实现教程【附qcoder.js插件下载】：https://blog.csdn.net/hj960511/article/details/70184003 


```
//引入我们的插件文件
&lt;script type="text/javascript" src="assets/js/qrcode.min.js"&gt;&lt;/script&gt;
					&lt;div style="margin-top:10px; float: left"&gt;
						&lt;div class="pull-left"&gt;
							&lt;div id="qrcode" style="width: 100px;margin:0 auto"&gt;&lt;/div&gt;
						&lt;/div&gt;
						&lt;div class="pull-left"&gt;
							&lt;p style="margin-left: 10px"&gt;扫一扫，手机打开浏览。&lt;/p&gt;
						&lt;/div&gt;
					&lt;/div&gt;
    					&lt;script type="text/javascript"&gt;
                        var qrcode = new QRCode(document.getElementById("qrcode"), {<!-- -->
                        width : 100,
                        height : 100
                        });
                        function makeCode () {<!-- -->
                        qrcode.makeCode("http://你所定义的qq好友弹出框添加界面地址?you_qq_number=你的qq号。");
                        }
                        makeCode();
                        &lt;/script&gt;


```

#### 五、其他运用方法

##### 1.一个界面多个按钮实现添加好友的方式

思路：利用a便签牵引到我们上方设定的动态页面，带入qq参数

```
&lt;a href="/add_qq?you_qq_number=你的qq"/&gt;

```

##### 2.弹出咨询框的方法

tips：需要我们先在qq的隐私设置中打开公开咨询的设置

```
http://wpa.qq.com/msgrd?v=3&amp;uin=你的QQ号&amp;site=qq:你的QQ号&amp;menu=yes

```
