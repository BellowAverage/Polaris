
--- 
title:  JavaScript的发展史及其应用领域 
tags: []
categories: [] 

---
### 1.JavaScript发展史

#### 1.1 Nombas 和 ScriptEase

大概在 1992 年，一家称作 Nombas 的公司开发了一种叫做 C 减减（C-minus-minus，简称 Cmm）的嵌入式脚本语言。Cmm背后的理念很简单：一个足够强大可以替代宏操作（macro）的脚本语言，同时保持与 C （和 C ++）足够的相似性，以便开发人员能很快学会。这个脚本语言捆绑在一个叫做 CEnvi 的共享软件中，它首次向开发人员展示了这种语言的威力。

Nombas 最终把 Cmm 的名字改成了 ScriptEase，原因是后面的部分（mm）听起来过于消极，同时字母 C “令人害怕”。现在 ScriptEase 已经成为了 Nombas 产品背后的主要驱动力。

当 Netscape Navigator 崭露头角时，Nombas 开发了一个可以嵌入网页中的 CEnvi 的版本。这些早期的试验被称为 Espresso Page（浓咖啡般的页面），它们代表了第一个在万维网上使用的客户端语言。而 Nombas 丝毫没有料到它的理念将会成为万维网的一块重要基石。

#### 1.2 Netscape 发明了 JavaScript

JavaScript因互联网而生，紧随着浏览器的出现而问世。回顾它的历史，就要从浏览器的历史讲起。

1990年底，欧洲核能研究组织（CERN）科学家Tim Berners-Lee，在全世界最大的电脑网络——互联网的基础上，发明了万维网（World Wide Web），从此可以在网上浏览网页文件。最早的网页只能在操作系统的终端里浏览，也就是说只能使用命令行操作，网页都是在字符窗口中显示，这当然非常不方便。

1992年底，美国国家超级电脑应用中心（NCSA）开始开发一个独立的浏览器，叫做Mosaic。这是人类历史上第一个浏览器，从此网页可以在图形界面的窗口浏览。

1994年10月，NCSA的一个主要程序员Marc Andreessen联合风险投资家Jim Clark，成立了Mosaic通信公司（Mosaic Communications），不久后改名为Netscape。这家公司的方向，就是在Mosaic的基础上，开发面向普通用户的新一代的浏览器Netscape Navigator。

1994年12月，Navigator发布了1.0版，市场份额一举超过90%。Netscape公司很快发现，Navigator浏览器需要一种可以嵌入网页的脚本语言，用来控制浏览器行为。管理层对这种浏览器脚本语言的设想是：功能不需要太强，语法较为简单，容易学习和部署。那一年，正逢Java语言开始推向市场，Netscape公司决定，脚本语言的语法要接近Java，并且可以支持Java程序。这些设想直接排除了使用现存语言，比如perl、python和TCL。

1995年，Brendan Eich开发这种网页脚本语言。Brendan Eich有很强的函数式编程背景，希望以Scheme语言（函数式语言鼻祖LISP语言的一种方言）为蓝本，实现这种新语言。1995年5月，Brendan Eich只用了10天，就设计完成了这种语言的第一版。它是一个大杂烩，语法有多个来源：
- 基本语法：借鉴C语言和Java语言。- 数据结构：借鉴Java语言，包括将值分成原始值和对象两大类。- 函数的用法：借鉴Scheme语言和Awk语言，将函数当作第一等公民，并引入闭包。- 原型继承模型：借鉴Self语言（Smalltalk的一种变种）。- 正则表达式：借鉴Perl语言。- 字符串和数组处理：借鉴Python语言。
为了保持简单，这种脚本语言缺少一些关键的功能，比如块级作用域、模块、子类型（subtyping）等等，但是可以利用现有功能找出解决办法。这种功能的不足，直接导致了后来JavaScript的一个显著特点：对于其他语言，你需要学习语言的各种功能，而对于JavaScript，你常常需要学习各种解决问题的模式。而且由于来源多样，从一开始就注定，JavaScript的编程风格是函数式编程和面向对象编程的一种混合体。

#### 1.3 JavaScript和Java的关系

Netscape公司的这种浏览器脚本语言，最初名字叫做Mocha，1995年9月改为LiveScript。12月，Netscape公司与Sun公司（Java语言的发明者和所有者）达成协议，后者允许将这种语言叫做JavaScript。这样一来，Netscape公司可以借助Java语言的声势，而Sun公司则将自己的影响力扩展到了浏览器。

之所以起这个名字，并不是因为JavaScript本身与Java语言有多么深的关系（事实上，两者关系并不深），而是因为Netscape公司已经决定，使用Java语言开发网络应用程序，JavaScript可以像胶水一样，将各个部分连接起来。当然，后来的历史是Java语言的浏览器插件（applet）失败了，JavaScript反而发扬光大。

1995年12月4日，Netscape公司与Sun公司联合发布了JavaScript语言。

1996年3月，Navigator 2.0浏览器正式内置了JavaScript脚本语言。

### 1.4 三足鼎立

因为 JavaScript 1.0 如此成功，Netscape 在 Netscape Navigator 3.0 中发布了 1.1 版。恰巧那个时候，微软决定进军浏览器，发布了 IE 3.0 并搭载了一个 JavaScript 的克隆版，叫做 JScript（这样命名是为了避免与 Netscape 潜在的许可纠纷）。微软步入 Web 浏览器领域的这重要一步虽然令其声名狼藉，但也成为 JavaScript 语言发展过程中的重要一步。（注：这里就是前端开发的痛苦之源）

在微软进入后，有 3 种不同的 JavaScript 版本同时存在：
1. Netscape Navigator 3.0 中的 JavaScript；1. IE 中的 JScript；1. CEnvi 中的 ScriptEase
与 C 和其他编程语言不同的是，JavaScript 并没有一个标准来统一其语法或特性，而这 3 种不同的版本恰恰突出了这个问题。随着业界担心的增加，这个语言的标准化显然已经势在必行。

#### 1.5 走向统一

1996年11月，网景公司决定将JavaScript提交给国际标准化组织ECMA（European Computer Manufacturers Association），希望JavaScript能够成为国际标准，以此抵抗微软。

1997年7月，ECMA组织发布262号标准文件（ECMA-262）的第一版，规定了浏览器脚本语言的标准，并将这种语言称为ECMAScript。这个版本就是ECMAScript 1.0版。之所以不叫JavaScript，一方面是由于商标的关系，Java是Sun公司的商标，根据一份授权协议，只有Netscape公司可以合法地使用JavaScript这个名字，且JavaScript已经被Netscape公司注册为商标，另一方面也是想体现这门语言的制定者是ECMA，不是Netscape，这样有利于保证这门语言的开放性和中立性。因此，ECMAScript和JavaScript的关系是，前者是后者的规格，后者是前者的一种实现。在日常场合，这两个词是可以互换的。

ECMAScript只用来标准化JavaScript这种语言的基本语法结构，与部署环境相关的标准都由其他标准规定，比如DOM的标准就是由W3C组织（World Wide Web Consortium）制定的。

ECMA-262标准后来也被另一个国际标准化组织ISO（International Organization for Standardization）批准，标准号是ISO-16262。

#### 1.6 混乱的根源—浏览器之战

1991年，WorldWideWeb 浏览器发布。这款由 Web 之父 Tim Berners-Lee 亲手设计的图形化浏览器还包含一个所见即所得 HTML 编辑器，为了避免同 WWW 混淆，这个浏览器后来改名为 Nexus.

1993年，Mosaic 发布。Internet 的流行应该归功于 Mosaic，这款浏览器将 Web 带向了大众。诸如 IE， Firefox 一类的当代浏览器仍然在延用 Mosaic 的图形化操作界面思想。

1994年，Netscape 成立。Marc Andreessen 带领 Mosaic 的程序员成立了 Netscape 公司，并发布了第一款商业浏览器 Netscape Navigator.

1995年，IE 发布。浏览器之战即将爆发，微软针对 Netscape 发布了他们自己的浏览器 IE，第一场浏览器之战爆发。

1996年，Opera 发布。Telenor 是挪威最大的通讯公司，他们推出了 Opera，并在两年后进军移动市场，推出 Opera 的移动版。

1998年，Mozilla 项目成立。Netscape 成立 Mozilla 开源项目，开发下一代浏览器，后来证明，使用原有代码开发新东西是一种负担，接着他们着手从新开发。

1998年，Netscape 浏览器走向开源。随着同 IE 征战的失利，Netscape 市场份额急剧下降，Netscape 决定将自己的浏览器开源以期重整山河。

2002年，IE 开始主导浏览器市场。市场份额达到95%，借助同操作系统的捆绑优势，IE 赢得第一场浏览器之战。战争是痛苦的，战后阴影对世界的影响更大。IE和网景当年大战期间，置网页标准W3C相关标准于不顾，互相不兼容对方浏览器，严重增加了网站开发者的成本，影响了用户的体验和选择权。这个影响一直持续到15年后的现在。看看身边仍然被IE奴役却无法放弃IE的人们，看看那些只兼容IE不兼容FF、Chrome的网站们，都与浏览器一战的阴影有关。

2003年，苹果 Safari 浏览器登场。苹果进入了浏览器市场，推出自己的 Webkit 引擎，该引擎非常优秀，后来被包括 Google， Nokia 之类的厂商用于手机浏览器。

2004年，Firefox 引发第二场浏览器之战。Firefox 1.0 推出。早在 Beta 测试期间就积累了大量人气的 Firefox 引发了第二场浏览器之战，当年年底，Firefox 已经赢得 7.4% 的市场份额。

2006年，IE7 发布。IE6 发布后的第六年，迫于 Firefox 的压力，微软匆匆推出 IE7 应战，吸取了 Firefox 的一些设计思想，如标签式浏览，反钓鱼等。但这款浏览器现在看来并不成功。

2008年，Google 携 Chrome 参战。Google 发布了他们自己的浏览器，加入这场战争。轻量，快，异常的稳固让这款浏览器成为不可轻视的一个对手。

2013年，历史重演。Google宣布从 WebKit分支出自己的浏览器渲染引擎 Blink。Opera放弃自己的Presto渲染和软件引擎，转而使用Chrome和Safari浏览器WebKit。

### 2. JavaScript 能做什么？

>  
 Atwood’s Law: any application that can be written in JavaScript, will eventually be written in JavaScript. Atwood 定律：凡是能用JavaScript写出来的，最终都会用JavaScript写出来。 


#### 2.1 Web前端开发

通信：Ajax/WebSocket 库：jQuery/zeptoUI/Dojo 框架：Bootstrap/Amaze UI依赖管理：RequireJS/SeaJs MVVM：AngularJS/Avalon

#### 2.2 后端服务开发

NodeJS的流行，让JavaScript可以作为后端语言，加之JavaScript的异步特性，以及灵活的函数式编程，针对高并发有独特的优势！相对于Java，C#等后端语言，它也更显得小而美，一个文件即可实现一个Server功能。

#### 2.3 桌面应用
- NW.js (Linux, Mac OS X, Windows)：http://nwjs.io/ ；- 有道heX：http://hex.youdao.com/zh-cn/index.html#bottom ；
#### 2.4 本地化存储

由于JavaScript一直没有存储数据的能力，导致JavaScript处在一个“辅助”的地位，HTML5的推广，JS有了Storage,IndexDB等特性，可以存储适量（Storage大约在5M）的数据。不要小看这适量的存储，妥善设计，可以让你的系统脱离后端的制约。目前各大平台都已支持，包括Android,IOS.

#### 2.5 ApplicationCache

俗称“高级缓存”，HTTP协议本身会针对请求文件进行缓存，但是由于这个缓存是协议层的设计，应用层要灵活控制比较麻烦。而ApplicationCache就是针对应用层的API，结合本地存储，可以实现离线应用！ 大家看到离线应该就明白了。目前类似淘宝京东这样的电商App端，不联网照样可以正常操作。更换缓存文件，就可在应用内部失效小版本更新。

#### 2.6 图形编程/数据可视化

JavaScript在图形处理方面一直是比较弱的。之前处理图形用的是SVG，SVG完全用XML来是实现图形。大型的图形处理，类似游戏中，就不太方便（目前主流的游戏引擎还是使用DOM来开发的）。而HTML5的Canvas，完全使用编程来实现图形，较之SVG更加灵活。虽然目前并没有成为主流，但是已经暂露头脚，其在游戏开发中的份额已经越来越多。世界上最流行的 2D 游戏引擎之一 Cocos2d 和最流行的 3D 游戏引擎之一 Unity3D 均支持 JS 开发游戏。

#### 2.7 构建高扩展的架构

JavaScript作为动态语言，加上其继承的灵活性，又兼具函数式编程的特性，在针对JavaScript设计架构时，相较于Java会更具扩展性！ JavaScript从一开始被被冠以“难以管理”，但是在经过了CMD，MVC等等的发展，早已不是当初的JavaScript，如果设计得当，它的兼容扩展性秒杀传统的后端语言。

#### 2.8 Hybrid移动应用开发

PhoneGap的问世使得JavaScript从开发传统移动Web应用转向混合移动应用。PhoneGap是一个能够让你用普通的web技术编写出能够轻松调用API接口和进入应用商店的混合移动应用开发平台。是唯一的一个支持iOS、Android、BlackBerry、Windows Phone 7、webOS、Bada、和Symbian7 7个平台的开源移动框架。它的优势是无以伦比的：开发成本低——据估算，至多Native App的五分之一！ Written Once，Run Everywhere!

#### 2.9 Native移动应用开发

Facebook 在 React.js Conf 2015 大会上推出了基于 JavaScript 的开源框架 React Native，React Native 结合了 Web 应用和 Native 应用的优势，可以使用 JavaScript 来开发 iOS 和 Android 原生应用。在 JavaScript 中用 React 抽象操作系统原生的 UI 组件，代替 DOM 元素来渲染等。 Learn Once，Write Everywhere!

#### 2.10 嵌入式/物联网开发

https://software.intel.com/zh-cn/iot/hardware/devkit

### 3.参考文献

1.《》 2.《》
