
--- 
title:  iis7.5 的解析漏洞(iis7.5 解析漏洞解决方案) 
tags: []
categories: [] 

---
### 一、iis7.5 的解析漏洞介绍

漏洞影响 IIS7 及IIS7.5 在使FastCGI方式调用php时，在php.ini里设置

cgi.fix_pathinfo=1，使得访问任意文件URL时，在URL后面添加“/x.php”等字符时，该文件被iis当php文件代码解析。

如 http://127.0.0.1/1.gif 的内容如下：

当访问 http://127.0.0.1/1.gif/1.php

可以看到1.gif里的php代码被iis解析执行了。 那么“黑客”在具体攻击网站的时候，先可以通过网站提供的图片上传功能（也可以是其他的手段）上传一个包含了恶意PHP代码的图片文件。然后通过上面描叙方法，让iis解析执行任意恶意的php代码，控制网站及主机，最终导致网站被“脱库”、“挂马”、“植入非法seo链接”等等严重后果。

### 二、iis7.5 的解析漏洞解决方案

第1种方案：继续使用FastCGI方式调用PHP，要解决这个安全问题可以在php.ini里设置 cgi.fix_pathinfo=0 ，修改保存后建议重启iis(注意可能影响到某些应用程序功能)。

第2种方案：使用ISAPI的方式调用PHP。（注意：PHP5.3.10已经摒弃了 ISAPI 方式）

第3种方案：可以使用其他web服务器软件，如apache等。

【实战解决方案】增强IIS设置（IIS7站长之家 测试通过）

在IIS里找到“处理程序映射”，然后对PHP这一项进行编辑，点击“请求限制”，把“仅当请求映射至以下内容时才调用处理程序”这个选项勾上即可；

### 具iis7.5 解析漏洞解决方案体操作步骤如下

#### 1、打
