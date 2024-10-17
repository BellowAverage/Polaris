
--- 
title:  XSS跨站脚本攻击详解（包括攻击方式和防御方式） 
tags: []
categories: [] 

---
### 一. XSS概述

人们经常将`跨站脚本攻击`（Cross Site Scripting）缩写为CSS，但这会与层叠样式表（Cascading Style Sheets，CSS）的缩写混淆。因此，有人将跨站脚本攻击缩写为XSS。

XSS（Cross Site Scripting）跨站脚本攻击，**是一种网站应用程序的安全漏洞攻击**。XSS攻击通常指的是`通过利用网页开发时留下的漏洞，通过巧妙的方法注入恶意指令代码到网页，使用户加载并执行攻击者恶意制造的网页程序。`

这些恶意网页程序通常是JavaScript，但实际上也可以包括Java、 VBScript、ActiveX、 Flash 或者甚至是普通的HTML。攻击成功后，攻击者可能得到包括但不限于更高的权限（如执行一些操作）、私密网页内容、会话和cookie等各种内容。

跨站脚本攻击（XSS），是最普遍的Web应用安全漏洞。这类漏洞能够使得攻击者嵌入恶意脚本代码到正常用户会访问到的页面中，当正常用户访问该页面时，则可导致嵌入的恶意脚本代码的执行，从而达到恶意攻击用户的目的。

攻击者可以使用户在浏览器中执行其预定义的恶意脚本，其导致的危害可想而知，如劫持用户会话，插入恶意内容、重定向用户、使用恶意软件劫持用户浏览器、繁殖XSS蠕虫，甚至破坏网站、修改路由器配置信息等。

XSS漏洞可以追溯到上世纪90年代。大量的网站曾遭受XSS漏洞攻击或被发现此类漏洞，如Twitter、Facebook、MySpace、Orkut、新浪微博和百度贴吧。研究表明，最近几年XSS已经超过缓冲区溢出成为最流行的攻击方式，有68%的网站可能遭受此类攻击。根据开放网页应用安全计划（Open Web Application Security Project）公布的2010年统计数据，在Web安全威胁前10位中，XSS排名第2，仅次于代码注入（Injection）。

`XSS 攻击有两大要素`： 1. 攻击者提交恶意代码。 2. 浏览器执行恶意代码。

XSS的重点不在于跨站，而在于脚本的攻击

### 二. 原理

HTML是一种超文本标记语言，通过将一些字符特殊地对待来区别文本和标记，例如，小于符号（&lt;）被看作是HTML标签的开始，

`当动态页面中插入的内容含有这些特殊字符（如&lt;）时，用户浏览器会将其误认为是插入了HTML标签，当这些HTML标签引入了一段JavaScript脚本时，这些脚本程序就将会在用户浏览器中执行。`所以，当这些特殊字符不能被动态页面检查或检查出现失误时，就将会产生XSS漏洞。

### 三. 特点

**特点**：隐蔽性强、发起容易等特点；

与钓鱼攻击相比，XSS攻击所带来的危害更大，通常具有如下特点：
1. 由于XSS攻击在用户当前使用的应用程序中执行，用户将会看到与其有关的个性化信息，如账户信息或“欢迎回来”消息，克隆的Web站点不会显示个性化信息。1. 通常，在钓鱼攻击中使用的克隆Web站点一经发现，就会立即被关闭。1. 许多浏览器与安全防护软件产品都内置钓鱼攻击过滤器，可阻止用户访问恶意的克隆站点。1. 如果客户访问一个克隆的Web网银站点，银行一般不承担责任。但是，如果攻击者通过银行应用程序中的XSS漏洞攻击了银行客户，则银行将不能简单地推卸责任。
### 四. 类型

从攻击代码的工作方式可以分为三个类型：
1. `持久型跨站`：最直接的危害类型，跨站代码存储在服务器（数据库）。经过后端，经过数据库。1. `非持久型跨站`：反射型跨站脚本漏洞，最普遍的类型。用户访问服务器-跨站链接-返回跨站代码。经过后端，不经过数据库。1. `DOM跨站（DOM XSS）`：DOM（document object model文档对象模型），客户端脚本处理逻辑导致的安全问题。
基于DOM的XSS漏洞是指受害者端的网页脚本在修改本地页面DOM环境时未进行合理的处置，而使得攻击脚本被执行。在整个攻击过程中，服务器响应的页面并没有发生变化，引起客户端脚本执行结果差异的原因是对本地DOM的恶意篡改利用。

#### 4.1 非持久型跨站

反射型XSS只是简单的把用户输入的数据从服务器反射给用户浏览器，要利用这个漏洞，攻击者必须以某种方式诱导用户访问一个精心设计的URL（恶意链接），才能实施攻击。

反射型XSS通常出现在搜索等功能中，需要被攻击者点击对应的链接才能触发，且受到XSS Auditor(chrome内置的XSS保护)、NoScript等防御手段的影响较大，所以它的危害性较存储型要小。

**攻击流程**： <img src="https://img-blog.csdnimg.cn/84372cfc7894483bbfc08cf210fd2d89.png" alt="在这里插入图片描述">

**漏洞原因**： 当用户的输入或者一些用户可控参数未经处理地输出到页面上，就容易产生XSS漏洞。主要场景有以下几种：
-  将不可信数据插入到HTML标签之间时；// 例如div, p, td； -  将不可信数据插入到HTML属性里时；// 例如：`&lt;div width=$INPUT&gt;&lt;/div&gt;` -  将不可信数据插入到SCRIPT里时；// 例如：`&lt;script&gt;var message = ” $INPUT “;&lt;/script&gt;` -  还有插入到Style属性里的情况，同样具有一定的危害性；// 例如`&lt;span style=” property : $INPUT ”&gt;&lt;/span&gt;` -  将不可信数据插入到HTML URL里时，// 例如：`&lt;a href=”[http://www.abcd.com?param=](http://www.ccc.com/?param=) $INPUT ”&gt;&lt;/a&gt;` -  使用富文本时，没有使用XSS规则引擎进行编码过滤。 
对于以上的几个场景，若服务端或者前端没有做好防范措施，就会出现漏洞隐患。

#### 4.2 持久型跨站

存储型（或 HTML 注入型/持久型）XSS 攻击最常发生在由社区内容驱动的网站或 Web 邮件网站，不需要特制的链接来执行。黑客仅仅需要提交 XSS 漏洞利用代码（反射型XSS通常只在url中）到一个网站上其他用户可能访问的地方。这些地区可能是博客评论，用户评论，留言板，聊天室，HTML 电子邮件，wikis，和其他的许多地方。

一旦用户访问受感染的页，执行是自动的。攻击流程： <img src="https://img-blog.csdnimg.cn/6b0629eca52c4cca8086b740a5504da7.png" alt="在这里插入图片描述"> **漏洞成因**：`存储型XSS漏洞的成因与反射型的根源类似，不同的是恶意代码会被保存在服务器中，导致其它用户（前端）和管理员（前后端）在访问资源时执行了恶意代码，用户访问服务器-跨站链接-返回跨站代码。`

#### 4.3 DOM跨站（DOM XSS）

通过修改页面的DOM节点形成的XSS，称之为DOM Based XSS。

攻击案例：在这段代码中，submit按钮的onclick事件调用了xsstest()函数。而在xsstest()中，修改了页面的DOM节点，通过innerHTML把一段用户数据当作HTML写入到页面中，造成了DOM Based XSS。

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;DOM Based XSS Demo&lt;/title&gt;
        &lt;script&gt;
        function xsstest() {<!-- -->
        var str = document.getElementById("input").value;
        document.getElementById("output").innerHTML = "&lt;img
        src='"+str+"'&gt;&lt;/img&gt;";
        }
        &lt;/script&gt;
    &lt;/head&gt;
    &lt;body&gt;
    &lt;div id="output"&gt;&lt;/div&gt;
    &lt;input type="text" id="input" size=50 value="" /&gt;
    &lt;input type="button" value="submit" onclick="xsstest()" /&gt;
    &lt;/body&gt;
&lt;/html&gt;

```

**漏洞原因**：DOM型XSS是基于DOM文档对象模型的。对于浏览器来说，DOM文档就是一份XML文档，当有了这个标准的技术之后，通过JavaScript就可以轻松的访问DOM。当确认客户端代码中有DOM型XSS漏洞时，诱使(钓鱼)一名用户访问自己构造的URL，利用步骤和反射型很类似，但是唯一的区别就是，构造的URL参数不用发送到服务器端，可以达到绕过WAF、躲避服务端的检测效果。

### 五. 攻击方式

常用的XSS攻击手段和目的有：

1、盗用cookie，获取敏感信息。 2、利用植入Flash，通过crossdomain权限设置进一步获取更高权限；或者利用Java等得到类似的操作。 3、利用iframe、frame、XMLHttpRequest或上述Flash等方式，以（被攻击）用户的身份执行一些管理动作，或执行一些一般的如发微博、加好友、发私信等操作。 4、利用可被攻击的域受到其他域信任的特点，以受信任来源的身份请求一些平时不允许的操作，如进行不当的投票活动。 5、在访问量极大的一些页面上的XSS可以攻击一些小型网站，实现DDoS攻击的效果。

### 六. 防御方法

#### 6.1 `基于特征的防御`

XSS漏洞和著名的SQL注入漏洞一样，都是利用了Web页面的编写不完善，所以每一个漏洞所利用和针对的弱点都不尽相同。这就给XSS漏洞防御带来了困难，不可能以单一特征来概括所有XSS攻击。

传统的XSS防御在进行攻击鉴别时多采用特征匹配方式，主要是针对“javascript”这个关键字进行检索，但是这种鉴别不够灵活，凡是提交的信息中各有“javascript”时，就被硬性的被判定为XSS攻击。

#### 6.2 `基于代码修改的防御`

Web页面开发者在编写程序时往往会出现一些失误和漏洞，XSS攻击正是利用了失误和漏洞，因此一种比较理想的方法就是通过优化Web应用开发来减少漏洞，避免被攻击：
- 1)用户向服务器上提交的信息要对URL和附带的的HTTP头、POST数据等进行查询，对不是规定格式、长度的内容进行过滤。- 2)实现Session标记（session tokens）、CAPTCHA系统或者HTTP引用头检查，以防功能被第三方网站所执行。- 3)确认接收的的内容被妥善的规范化，仅包含最小的、安全的Tag（没有javascript），去掉任何对远程内容的引用（尤其是样式表和javascript），使用HTTP only的cookie。
当然，如上操作将会降低Web业务系统的可用性，用户仅能输入少量的制定字符，人与系统间的交互被降到极致，仅适用于信息发布型站点。并且考虑到很少有Web编码人员受过正规的安全培训，很难做到完全避免页面中的XSS漏洞。

##### 6.2.1 XSS 防御之 HTML 编码

**应用范围**：将不可信数据放入到 HTML 标签内（例如div、span等）的时候进行HTML编码。 **编码规则**：将 &amp; &lt; &gt; " ’ / 转义为实体字符（或者十进制、十六进制）。 **示例代码**：

```
function encodeForHTML(str, kwargs){<!-- -->     return ('' + str)
 
      .replace(/&amp;/g, '&amp;amp;')
 
      .replace(/&lt;/g, '&amp;lt;')     // DEC=&gt; &amp;#60; HEX=&gt; &amp;#x3c; Entity=&gt; &amp;lt;
 
      .replace(/&gt;/g, '&amp;gt;')
 
      .replace(/"/g, '&amp;quot;')
 
      .replace(/'/g, '&amp;#x27;')   // &amp;apos; 不推荐，因为它不在HTML规范中
 
      .replace(/\//g, '&amp;#x2F;');
 
  }; 

```

HTML 有三种编码表现方式：十进制、十六进制、命名实体。例如小于号（&lt;）可以编码为 “十进制&gt; &lt;”, “十六进制=&gt; &lt;”, “命名实体=&gt; &lt;” 三种方式。对于单引号（’）由于实体字符编码方式不在 HTML 规范中，所以此处使用了十六进制编码。

##### 6.2.2 XSS 防御之 HTML Attribute 编码

**应用范围**：将不可信数据放入 HTML 属性时（不含src、href、style 和事件处理属性），进行 HTML Attribute 编码

**编码规则**：除了字母数字字符以外，使用 &amp;#xHH;(或者可用的命名实体)格式来转义 ASCII值小于256所有的字符

**示例代码**：

```
function encodeForHTMLAttibute(str, kwargs){<!-- -->
    let encoded = ''
    for(let i = 0; i &lt; str.length; i++) {<!-- -->       
        let ch = hex = str[i]     
        if (!/[A-Za-z0-9]/.test(str[i]) &amp;&amp; str.charCodeAt(i) &lt; 256) {<!-- -->         
            hex = '&amp;#x' + ch.charCodeAt(0).toString(16) + ';'
        }
        encoded += hex
    }
    return encoded
}

```

##### 6.2.3 XSS 防御之 JavaScript 编码

**作用范围**：将不可信数据放入事件处理属性、JavaScirpt值时进行 JavaScript 编码

**编码规则**：除字母数字字符外，请使用\xHH格式转义ASCII码小于256的所有字符

**示例代码**：

```
function encodeForJavascript(str, kwargs) {<!-- -->     
    let encoded = '';     
    for(let i = 0; i &lt; str.length; i++) {<!-- -->       
        let cc = hex = str[i];       
        if (!/[A-Za-z0-9]/.test(str[i]) &amp;&amp; str.charCodeAt(i) &lt; 256) {<!-- -->         
            hex = '\\x' + cc.charCodeAt().toString(16);
 
        }
        encoded += hex;
    }
    return encoded;   
};

```

##### 6.2.4 XSS 防御之 URL 编码

**作用范围**：将不可信数据作为 URL 参数值时需要对参数进行 URL 编码

**编码规则**：将参数值进行 encodeURIComponent 编码

**示例代码**：

```
function encodeForURL(str, kwargs){<!-- -->     
    return encodeURIComponent(str);   
};

```

##### 6.2.5 XSS 防御之 CSS 编码

**作用范围**：将不可信数据作为 CSS 时进行 CSS 编码

**编码规则**：除了字母数字字符以外，使用\XXXXXX格式来转义ASCII值小于256的所有字符

**示例代码**：

```
function encodeForCSS (attr, str, kwargs){<!-- -->     
    let encoded = '';     
    for (let i = 0; i &lt; str.length; i++) {<!-- -->       
        let ch = str.charAt(i);       
        if (!ch.match(/[a-zA-Z0-9]/) {<!-- -->         
            let hex = str.charCodeAt(i).toString(16);         
            let pad = '000000'.substr((hex.length));         
            encoded += '\\' + pad + hex;
        } else {<!-- -->         
            encoded += ch;
        }     
    }
    return encoded;
}; 

```

任何时候用户的输入都是不可信的。对于 HTTP 参数，理论上都要进行验证，例如某个字段是枚举类型，其就不应该出现枚举以为的值；对于不可信数据的输出要进行相应的编码。

XSS 漏洞有时比较难发现，所幸当下React、Vue等框架都从框架层面引入了 XSS 防御机制，一定程度上解放了我们的双手。 但是作为开发人员依然要了解 XSS 基本知识、于细节处避免制造 XSS 漏洞。框架是辅助，我们仍需以人为本，规范开发习惯，提高 Web 前端安全意识。

#### 6.3 `客户端分层防御策略`

客户端跨站脚本攻击的分层防御策略是基于独立分配线程和分层防御策略的安全模型。它建立在客户端(浏览器)，这是它与其他模型最大的区别，之所以客户端安全性如此重要，客户端在接受服务器信息，选择性的执行相关内容。这样就可以使防御XSS攻击变得容易，该模型主要由三大部分组成：
- 1)对每一个网页分配独立线程且分析资源消耗的“网页线程分析模块”；- 2)包含分层防御策略四个规则的用户输入分析模块；- 3)保存互联网上有关XSS恶意网站信息的XSS信息数据库。
XSS攻击主要是由程序漏洞造成的，要完全防止XSS安全漏洞主要依靠程序员较高的编程能力和安全意识，当然安全的软件开发流程及其他一些编程安全原则也可以大大减少XSS安全漏洞的发生。这些防范XSS漏洞原则包括： （1）`不信任用户提交的任何内容，对所有用户提交内容进行可靠的输入验证`，包括对URL、查询关键字、HTTP头、REFER、POST数据等，仅接受指定长度范围内、采用适当格式、采用所预期的字符的内容提交，对其他的一律过滤。尽量采用POST而非GET提交表单；对“&lt;”，“&gt;”，“；”，“””等字符做过滤；任何内容输出到页面之前都必须加以en-code，避免不小心把htmltag显示出来。 （2）`实现Session 标记（session tokens）、CAPTCHA（验证码）系统或者HTTP引用头检查`，以防功能被第三方网站所执行，对于用户提交信息的中的img等link，检查是否有重定向回本站、不是真的图片等可疑操作。 （3）`cookie 防盗`。避免直接在cookie中泄露用户隐私，例如email、密码，等等；通过使cookie和系统IP绑定来降低cookie泄露后的危险。这样攻击者得到的cookie没有实际价值，很难拿来直接进行重放攻击。 （4）`确认接收的内容被妥善地规范化`，仅包含最小的、安全的Tag（没有JavaScript），去掉任何对远程内容的引用（尤其是样式表和JavaScript），使用HTTPonly的cookie。

#### 6.4 其它类型的防范

虽然在渲染页面和执行javascript时，通过谨慎的转义可以防止xss的发生，但完全依赖开发的严谨任然是不够的，以下介绍一些通用的方案，可以降低xss带来的风险和后果。 **1、`CSP`**： Content Security Policy: 严格的CSP在XSS的防范中可以起到以下作用：

```
禁止加载外域代码，防止复杂的攻击逻辑。
禁止外域提交，网站被攻击后，用户的数据不会泄露到外域。
禁止内联脚本执行（规则较严格，目前发现 GitHub 使用）。
禁止未授权的脚本执行（新特性，Google Map 移动版在使用）。
合理使用上报可以及时发现 XSS，利于尽快修复问题。

```

**2、`输入内容长度控制`**

对于不受信任的输入，都应该限定一个合理的长度。虽然无法完全防止XSS发生，但可以增加xss攻击的难度。

**3、`其他安全措施`**

http-only cookie:禁止javascript读取某些敏感的cookie，攻击者完成xss注入后无法窃取此cookie.

验证码:防止脚本冒充用户提交危险操作。
