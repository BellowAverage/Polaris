
--- 
title:  【渗透测试实战】PHP语言有哪些后门？以及利用方法 
tags: []
categories: [] 

---
**目录**































好了。上课了，上课了

<img alt="" height="418" src="https://img-blog.csdnimg.cn/86851444fdc646e1aac0ab12936d33c2.gif" width="279">

## 后门

###  php.ini构成的后门

```
利用 auto_prepend_file 和 include_path
```

###  .user.ini文件构成的PHP后门

.user.ini可运行于所有以fastcgi运行的server。

利用方式同php.ini

##  反序列化

###  PHP序列化实现

####  常见处理器

PHP序列化处理共有几种，分别为php、php_serialize、php_binary和WDDX(需要编译时开启支持)，默认为php，可通过配置中的 `session.serialize_handler` 修改。

如果 PHP 编译时加入了 WDDX 支持，则只能用 WDDX，WDDX从PHP 7.4版本后开始弃用。从 PHP 5.5.4 起可以使用 php_serialize。 php_serialize 在内部简单地直接使用 serialize/unserialize 函数，并且不会有 php 和 php_binary 所具有的限制。

其中PHP处理器的格式为：键名 + 竖线 + 经过serialize()函数序列化处理的值。

其中php_binary处理器的格式为：键名的长度对应的 ASCII 字符 + 键名 + 经过serialize()函数序列化处理的值。

其中php_serialize处理器的格式为：经过serialize()函数序列化处理的数组。

####  序列化格式

其中php_serialize的实现在 `php-src/ext/standard/var.c` 中，主要函数为 `php_var_serialize_intern` ，序列化后的格式如下：

```
boolean

    b:&lt;value&gt;;
    b:1; // true
    b:0; // false

integer

    i:&lt;value&gt;;

double

    d:&lt;value&gt;;

NULL

    N;

string

    s:&lt;length&gt;:"&lt;value&gt;";
    s:1:"s";

array

    a:&lt;length&gt;:{key, value};
    a:1:{s:4:"key1";s:6:"value1";} // array("key1" =&gt; "value1");

object

    O:&lt;class_name_length&gt;:"&lt;class_name&gt;":&lt;number_of_properties&gt;:{&lt;properties&gt;};

reference

    指针类型
    R:reference;
    O:1:"A":2:{s:1:"a";i:1;s:1:"b";R:2;}
    $a = new A();$a-&gt;a=1;$a-&gt;b=&amp;$a-&gt;a;
```

####  private与protect

private与protect变量和public变量不同，不能直接设置。

private属性只能在其被定义的类内部访问，且不会被继承，在属性前加上类名，即 `%00className%00` 用于标定其是私有的。

protected属性可以在父类和子类中访问，变量前添加 `%00*%00` 用于标定其是受保护的。



###  PHP反序列化漏洞

php在反序列化的时候会调用 `__wakeup` / `__sleep` 等函数，可能会造成代码执行等问题。若没有相关函数，在析构时也会调用相关的析构函数，同样会造成代码执行。

另外 `__toString` / `__call` 两个函数也有利用的可能。

其中 `__wakeup` 在反序列化时被触发，`__destruct` 在GC时被触发， `__toString` 在echo时被触发, `__call` 在一个未被定义的函数调用时被触发。

下面提供一个简单的demo.

```
class Demo
{

    public $data;

    public function __construct($data)
    {
        $this-&gt;data = $data;
        echo "construct&lt;br /&gt;";
    }

    public function __wakeup()
    {
        echo "wake up&lt;br /&gt;";
    }

    public function __destruct()
    {
        echo "Data's value is $this-&gt;data. &lt;br /&gt;";
        echo "destruct&lt;br /&gt;";
    }
}

var_dump(serialize(new Demo("raw value")));
```

输出

```
construct
Data's value is raw value.
destruct
string(44) "O:4:"Demo":1:{s:4:"data";s:9:"raw value";}"
```

把序列化的字符串修改一下后，执行

```
unserialize('O:4:"Demo":1:{s:4:"data";s:15:"malicious value";}');
```

输出

```
wake up
Data's value is malicious value.
destruct
```

这里看到，值被修改了.

上面是一个 `unserialize()` 的简单应用，不难看出，如果 `__wakeup()` 或者 `__desturct()` 有敏感操作，比如读写文件、操作数据库，就可以通过函数实现文件读写或者数据读取的行为。

那么，在 `__wakeup()` 中加入判断是否可以阻止这个漏洞呢？ 在 `__wakeup()` 中我们加入一行代码

```
public function __wakeup()
{
    if($this-&gt;data != 'raw value') $this-&gt;data = 'raw value';
    echo "wake up&lt;br /&gt;";
}
```

但其实还是可以绕过的，在 PHP5 &lt; 5.6.25， PHP7 &lt; 7.0.10 的版本都存在wakeup的漏洞。当反序列化中object的个数和之前的个数不等时，wakeup就会被绕过，于是使用下面的payload

```
unserialize('O:7:"HITCON":1:{s:4:"data";s:15:"malicious value";}');
```

输出

```
Data's value is malicious value.
destruct
```

这里wakeup被绕过，值依旧被修改了。

<img alt="" height="225" src="https://img-blog.csdnimg.cn/189a629b6f3542378e05b755216e0ab4.gif" width="400">



###  利用点

####  SoapClient 原生利用

php中的SoapClient类可以创建soap数据报文，在非wsdl模式下，SoapClient的实例反序列化的时候会对第二个参数指明的url进行soap请求，该特性可用于SSRF。

####  ZipArchive 原生利用

php原生类 `ZipArchive::open()` 中的flag参数如果设置为 `ZipArchive::OVERWRITE` 时，会删除指定文件，该特性在一定条件下可以用于删除文件。



####  Session

PHP中session默认是以文件形式存储的，文件以sess_sessionid命名，在session一定程度可控的情况下，可通过session触发反序列化。

###  相关CVE

####  CVE-2016-7124

在PHP 5.6.25 之前版本和 7.0.10 之前的版本，当对象的属性(变量)数大于实际的个数时， `__wakeup()` 不会被执行。

####  【资源推荐】
-  <h4 id="%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%93%E7%94%A8%E7%B3%BB%E7%BB%9F">**渗透测试专用系统**</h4> - kali-linux-e17-2019.1a-amd64.iso系统镜像- - kali-linux-2018.4-amd64 操作系统- - manjaro-xfce-17.1.7-stable-x86_64.iso系统镜像- - WiFi专用渗透系统 nst-32-11992.x86_64.iso操作系统镜像- - Parrot-security-4.1_amd64.iso 操作系统镜像- - manjaro-xfce-17.1.7-stable-x86_64 操作系统- - cyborg-hawk-linux-v-1.1 操作系统- - <li> <h4 id="%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E7%9B%B8%E5%85%B3%E5%B7%A5%E5%85%B7">渗透测试相关工具</h4> - **<strong><strong><strong>**</strong></strong></strong>- 【kali常用工具】上网行为监控工具       - - 【kali常用工具】抓包工具Charles Windows64位 免费版- - 【kali常用工具】图印工具stamp.zip- - 【kali常用工具】brutecrack工具[WIFIPR中文版]及wpa/wpa2字典- - 【kali常用工具】EWSA 5.1.282-破包工具- - 【kali常用工具】Realtek 8812AU KALI网卡驱动及安装教程- - 【kali常用工具】无线信号搜索工具_kali更新- - 【kali常用工具】inssider信号测试软件_kali常用工具- - 【kali常用工具】MAC地址修改工具 保护终端不暴露- - 【kali常用工具】脚本管理工具 php和jsp页面 接收命令参数 在服务器端执行- 
#### 渗透测试相关工具


- **Java实现照片GPS定位【完整脚本】**- - **Python实现照片GPS定位【完整脚本】**- - **女神忘记相册密码 python20行代码打开【完整脚本】**- - **<strong><strong><strong>**</strong></strong></strong>- 
**python实战**
- **<strong><strong><strong>**</strong></strong>**<strong><strong>**</strong></strong></strong>- **<strong><strong><strong>**</strong></strong></strong>- **<strong><strong><strong>**</strong></strong>...</strong>- **<strong><strong><strong>**</strong></strong></strong>- **<strong><strong><strong>**</strong></strong></strong>- **<strong><strong><strong>**</strong></strong>**<strong><strong>**</strong></strong>**<strong><strong>**</strong></strong></strong>
**【pygame开发实战开发30例 完整源码】**
- 
**【pygame游戏开发专栏，获取完整源码+教程】**
- **<strong><strong><strong>**</strong></strong></strong>- **<strong><strong><strong>**</strong></strong></strong>- **<strong><strong><strong>**</strong></strong></strong>- **<strong><strong><strong>**</strong></strong></strong>- **<strong><strong><strong>**</strong></strong> </strong>- **<strong><strong><strong>**</strong></strong></strong>
#### CSDN官方学习推荐 ↓ ↓ ↓
- **CSDN出的Python全栈知识图谱，太强了，推荐给大家！**
<img alt="" height="625" src="https://img-blog.csdnimg.cn/20210607120133619.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="351">

 
