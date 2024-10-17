
--- 
title:  java web中url问号传值，中文乱码问题 
tags: []
categories: [] 

---
       首先，贴一下错误信息：“Invalid character found in the request target. The valid characters are defined in RFC 7230 and RFC 3986”，这个错误信息的出现是因为在代码：href:"&lt;%=request.getContextPath() %&gt;/departmentAction!toView?id="+checkeds[0].id中，checkeds[0].id是中文，这个时候就会出现在url有中文的情况，那么这为什么会导致错误呢？下面我们来了解一下相关的原因。

**RFC 3986 文档**  （1）RFC 3986文档规定，Url中只允许包含英文字母（a-z，A-Z）、数字（0-9）、- _ . ~ 4个特殊字符以及所有保留字符。 （2）RFC3986中指定了以下字符为保留字符：! * ’ ( ) ; : @ &amp; = + $ , / ? # [ ]，如果要在url里使用不安全字符，就需要使用转义。关于具体的转义的相关规则，这里就不详细说明了，有兴趣的可以自己查阅相关的资料。

       从上面的我们不难发现，中文出现在url中是非法的，所以如果我们要想使用中文的话，那么就必须做出相应的处理。

下面说一下我出现的问题的解决方法：

我的情况是在javascript中使用url的：

javascript代码使用的是jquery，部分截图如下：

<img src="https://img-blog.csdn.net/20171201105658832?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

java后台的处理代码为：

 

<img src="https://img-blog.csdn.net/20171201105912904" alt=""> 

       对于上面的代码，在谷歌的chrome浏览器中是可以的，但是在ie中就会报出中文乱码的错误，所以，问题就来了，下面是修改的方法：

在javascript中，我们先进行编码处理：

<img src="https://img-blog.csdn.net/20171201110358616" alt=""> 

在java后台的action中再对中文部分进行解码：

<img src="https://img-blog.csdn.net/20171201110231537" alt=""> 

        这样处理后，问题就解决了。
