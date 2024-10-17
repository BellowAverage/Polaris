
--- 
title:  session和cookie的作用原理和区别 
tags: []
categories: [] 

---


#### session和cookie
- - <ul><li>- - - - - - - - - - 


## 简述session

### 一、session的概念及特点

session概念:在计算机中，尤其是在网络应用中，称为“会话控制”。Session 对象存储特定用户会话所需的属性及配置信息。说白了session就是一种可以维持服务器端的数据存储技术。session主要有以下的这些特点：

session保存的位置是在服务端 session一般来说要配合cookie使用，如果用户浏览器禁用了cookie，那么只能使用URL重写来实现session的存储功能

单纯的使用session来存储用户回话信息，那么当用户量较多时，session文件数量会很多，会存在session查询慢的问题

本质上：session技术就是一种基于后端有别于数据库的临时存储技术

### 二、为什么要使用session

我们目前使用的互联网应用层协议基本上都是基于 HTTP 和 HTTPS 的，它们的本身是无状态的， 只负责请求和响应。 我告诉服务器我需要什么，服务器返回给我相应的资源。 如果没有额外处理的话， 服务器是不知道你是谁，更无法根据你是谁给你展现和你相关的内容了。

HTTP 协议一开始被设计成这样还是有一些历史原因的，当时的互联网多用于学术交流，只用于文章信息的展现之类的事情，远没有现在这么丰富多彩。所以在当时的背景下 HTTP 协议被设计成这样其实也是很符合它的场景的。但随着互联网应用越来越广泛，应用的形式也变得越来越多，我们的 Web 应用不只限于提供简单的信息展现了，还需要用户能够登录，可以在论坛发帖子，在购物网站买东西等等。 这就需要 HTTP 协议能够记录用户的状态。也就是我们现在熟悉的 Session 由来。

### 三、session的工作原理

用户第一次请求服务器时，服务器端会生成一个sessionid 服务器端将生成的sessionid返回给客户端，通过set-cookie 客户端收到sessionid会将它保存在cookie中，当客户端再次访问服务端时会带上这个sessionid 当服务端再次接收到来自客户端的请求时，会先去检查是否存在sessionid，不存在就新建一个sessionid重复1,2的流程，如果存在就去遍历服务端的session文件，找到与这个sessionid相对应的文件，文件中的键值便是sessionid，值为当前用户的一些信息 此后的请求都会交换这个 Session ID，进行有状态的会话。

### 四、session与cookies区别

**1、数据存放位置不同：**

cookie数据存放在客户的浏览器上，session数据放在服务器上。e79fa5e98193e4b893e5b19e31333366306536

**2、安全程度不同：**

cookie不是很安全，别人可以分析存放在本地的COOKIE并进行COOKIE欺骗,考虑到安全应当使用session。

**3、性能使用程度不同：**

session会在一定时间内保存在服务器上。当访问增多，会比较占用你服务器的性能,考虑到减轻服务器性能方面，应当使用cookie。

**4、数据存储大小不同：**

单个cookie保存的数据不能超过4K，很多浏览器都限制一个站点最多保存20个cookie，而session则存储与服务端，浏览器对其没有限制。

**5、会话机制不同**

session会话机制：session会话机制是一种服务器端机制，它使用类似于哈希表（可能还有哈希表）的结构来保存信息。 cookies会话机制：cookie是服务器存储在本地计算机上的小块文本，并随每个请求发送到同一服务器。 Web服务器使用HTTP标头将cookie发送到客户端。在客户端终端，浏览器解析cookie并将其保存为本地文件，该文件自动将来自同一服务器的任何请求绑定到这些cookie。

### 五、session的生命周期

**Session何时生效：** Sessinon在用户访问第一次访问服务器时创建，需要注意只有访问JSP、Servlet等程序时才会创建Session，只访问HTML、IMAGE等静态资源并不会创建Session,可调用request.getSession(true)强制生成Session。

**Session何时失效**： 1.服务器会把长时间没有活动的Session从服务器内存中清除，此时Session便失效。Tomcat中Session的默认失效时间为20分钟。从session不活动的时候开始计算，如果session一直活动，session就总不会过期。从该Session未被访问,开始计时; 一旦Session被访问,计时清0;

**2.调用Session的invalidate方法**

HttpSession session = request.getSession(); session.invalidate();//注销该request的所有session **3.设置session的失效时间**

a)web.xml中

```
&lt;session-config&gt;
&lt;session-timeout&gt;30&lt;/session-timeout&gt;
&lt;/session-config&gt;

```

b)在程序中手动设置

session.setMaxInactiveInterval(30 * 60);//设置单位为秒，设置为-1永不过期

request.getSession().setMaxInactiveInterval(-1);//永不过期 c)tomcat也可以修改session过期时间，在server.xml中定义context时采用如下定义：

```
&lt;Context path="/livsorder" 
docBase="/home/httpd/html/livsorder" 　　defaultSessionTimeOut="3600" 
isWARExpanded="true" 　　
isWARValidated="false" isInvokerEnabled="true" 　　isWorkDirPersistent="false"/&gt;

```

**4.关闭浏览器，session就会失效**

### 六、session的性能瓶颈

另外一个要聊聊的就是 Session 数据的存储。 通常情况下，如果你不明确的设置， 大多数 Web 框架会把 Session 数据存放到内存中。如果你的 Web 应用用户量不大的话，这也不成问题。 但如果你的用户数比较大的话，就可能发生一个事情 — 内存不够用了。

这很正常，内存容量是非常宝贵的，假设每个用户的 Session 数据是 100K， 1万个用户就会大概占用 1G 的存储空间，如果你的 Session 数据清理机制也恰巧比较慢的话，内存非常容易被占满。这就需要你在设计比较大并发量的站点时，要考虑 Session 的存储方式，比如把它们保存到硬盘文件系统中，或者数据库中。 所以你在开发一个 Web 应用的时候，如果你的用户量很大，你需要有这个意识。另外 Session 放到内存中还有一个弊端，如果你的 Web 服务器发生重启，那么所有的 Session 状态都会被情况，会在一定程度上影响用户体验。

## 简述cookie

### 一、Cookie的概述
- Cookie是客户端的技术(默认把Cookie保存在每个用户的浏览器上)- 程序把每个用户的数据以cookie的形式写给用户各自的浏览器- 当用户使用浏览器再去访问服务器中的web资源时,就会带着各自的数据去
### 二、Cookie的原理
- Cookie基于客户端的技术,Cookie的对象是服务器端创建的,默认把Cookie保存在客户端浏览器上- Cookie基于http的协议,默认有两个(set-cookie是响应头,服务器端到客户端 cookie是请求头,客户端到服务器端)- Cookie可以在客户端与服务器端进数据的传递
### 三、Cookie对象的api

```
Cookie(String name, String value) -- 构造方法，是key:value的形式（强调：Cookie中不支持中文的）
String getName()    -- 获取cookie的名称
String getValue()    -- 获取cookie的值
void setValue(String newValue)    -- 设置值
void setMaxAge(int expiry)    -- 设置Cookie的有效时间

```

如果浏览器关闭了,Cookie默认就被清除了,Cookie默认的情况下是保存在浏览器的缓存中

设置有效的时间,Cookie就变成了持久的Cookie.默认的情况下,把Cookie保存到本地的文件中

需求:显示用户上次访问的时间(和Cookie的原理相同),注意不管是否是第一次访问,都要设置cookie的有效时间

```
// 设置输出到页面的编码格式,解决字符流的中文乱码问题
response.setContentType("text/html;charset=UTF-8");

// 首先判断是否是第一次访问
Cookie[] cookies = request.getCookies();

// 查找名称为lasttime的cookie
Cookie cookie = CookieUtils.getCookieByName(cookies, "lasttime");
// 处理当前时间
String currentTime = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date());

if (cookie==null) {<!-- -->
// 第一次访问
cookie = new Cookie("lasttime", currentTime);
// 设置cookie的有效时间 1小时
cookie.setMaxAge(60*60);
// 向浏览器回写cookie
response.addCookie(cookie);
// 输出一句话
response.getWriter().write("欢迎,第一次访问!");

} else {<!-- -->
// 不是第一次访问,取cookie中的值
String lastTime = cookie.getValue();
// 输出一句话
response.getWriter().write("欢迎,上次访问时间为: " + lastTime + ", 下次早点来啊!");
// 设置cookie的有效时间 1小时
cookie.setMaxAge(60*60);
// 将cookie的值设置为当前时间(记录这一次的时间)
cookie.setValue(currentTime);
// 向浏览器回写cookie
response.addCookie(cookie);

}
void setPath(String uri) -- 设置Cookie的有效路径

```
-  第一次访问的时候，/lasttime的默认的有效路径是/day11 -  访问demo2.jsp http://localhost/day11/pages/demo2.jsp 如果访问的是/day11/下的任何资源，都会携带cookie的数据! -  第二次访问的时候，/web/lasttime，默认的有效路径是/day11/web -  访问demo2.jsp http://localhost/day11/pages/demo2.jsp ,不会携带cookie的数据! -  如果访问的是 http://localhost/day11/web/pages/demo2.jsp ,携带cookie的数据! 有效路径决定什么事情呢? 
访问项目中其他资源时,是否携带cookie!!

cookie.setPath(“/personal”);// 设置cookie的有效路径,那么访问/personal下(personal项目)的任何资源,都会携带cookie的数据!这就是设置有效路径的作用!! 操作Cookie对象的方法

response.void addCookie(Cookie cookie) – 向浏览器回写cookie对象 request Cookie[] getCookies() – 获取浏览器发送过来的Cookie，返回的数组

## 区别与联系

### 一、cookie 和session 的区别：

1、cookie数据存放在客户的浏览器上，session数据放在服务器上。 2、cookie不是很安全，别人可以分析存放在本地的COOKIE并进行COOKIE欺骗,考虑到安全应当使用session。 3、session会在一定时间内保存在服务器上。当访问增多，会比较占用你服务器的性能,考虑到减轻服务器性能方面，应当使用COOKIE。

4、单个cookie保存的数据不能超过4K，很多浏览器都限制一个站点最多保存20个cookie。

cookie 和session 的联系：session是通过cookie来工作的session和cookie之间是通过 
     
      
       
        
         
        
          C 
         
        
       
         O 
        
       
         O 
        
       
         K 
        
       
         I 
        
       
         E 
        
        
        
          [ 
         
        
          ′ 
         
        
       
         P 
        
       
         H 
        
       
         P 
        
       
         S 
        
       
         E 
        
       
         S 
        
       
         S 
        
       
         I 
        
        
        
          D 
         
        
          ′ 
         
        
       
         ] 
        
       
         来联系的，通过 
        
       
      
        _COOKIE['PHPSESSID']来联系的，通过 
       
      
    C​OOKIE[′PHPSESSID′]来联系的，通过_COOKIE[‘PHPSESSID’]可以知道session的id，从而获取到其他的信息cookie 和session 的区别： 1、cookie数据存放在客户的浏览器上，session数据放在服务器上。 2、cookie不是很安全，别人可以分析存放在本地的COOKIE并进行COOKIE欺骗,考虑到安全应当使用session。 3、session会在一定时间内保存在服务器上。当访问增多，会比较占用你服务器的性能,考虑到减轻服务器性能方面，应当使用COOKIE。

4、单个cookie保存的数据不能超过4K，很多浏览器都限制一个站点最多保存20个cookie。

### 二、cookie 和session 的联系：

session是通过cookie来工作的session和cookie之间是通过 
     
      
       
        
         
        
          C 
         
        
       
         O 
        
       
         O 
        
       
         K 
        
       
         I 
        
       
         E 
        
        
        
          [ 
         
        
          ′ 
         
        
       
         P 
        
       
         H 
        
       
         P 
        
       
         S 
        
       
         E 
        
       
         S 
        
       
         S 
        
       
         I 
        
        
        
          D 
         
        
          ′ 
         
        
       
         ] 
        
       
         来联系的，通过 
        
       
      
        _COOKIE['PHPSESSID']来联系的，通过 
       
      
    C​OOKIE[′PHPSESSID′]来联系的，通过_COOKIE[‘PHPSESSID’]可以知道session的id，从而获取到其他的信息
