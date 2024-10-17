
--- 
title:  【网络安全】手把手教你利用XSS攻击体验一次黑客 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/f14d193f7e523912e48b4fd462001bcf.jpeg" alt="906501ADEAF08AD26A3F225744EA44BB.jpg">

#### **我们部门首先确定风险来源，并给出了解决方案。前端部分由我解决，并紧急修复上线。**

<img src="https://img-blog.csdnimg.cn/img_convert/ecc322fad2ff64d30017cd52162a6b23.jpeg" alt="5C92478016448CBE2BB5650DAEB40955.jpg">

#### 一：那么什么是XSS攻击呢？

人们经常将跨站脚本攻击（Cross Site Scripting）缩写为CSS，但这会与层叠样式表（Cascading Style Sheets，CSS）的缩写混淆。因此，有人将跨站脚本攻击缩写为XSS。恶意攻击者往Web页面里插入恶意html代码，当用户浏览该页之时，嵌入其中Web里面的html代码会被执行，从而达到恶意用户的特殊目的。主要指的自己构造XSS跨站漏洞网页或者寻找非目标机以外的有跨站漏洞的网页。XSS是web安全最为常见的攻击方式，在近年来，常居web安全漏洞榜首。

光看这个定义，很多同学一定不理解是什么意思，下面我会模拟XSS攻击，同学们应该就知道怎么回事了。 在模拟XSS攻击之前，我们先来看看XSS攻击的分类。

#### 二：XSS攻击有几种类型呢？

###### ①反射型XSS攻击（非持久性XSS攻击）

###### ②存储型XSS攻击（持久型XSS攻击）

###### ③DOM-based型XSS攻击

#### 三：接下来我们将模拟这几种XSS攻击

##### 第一种：反射型XSS攻击（非持久性XSS攻击）

反射型XSS攻击一般是攻击者通过特定手法，诱使用户去访问一个包含恶意代码的URL，当受害者点击这些专门设计的链接的时候，恶意代码会直接在受害者主机上的浏览器执行。此类XSS攻击通常出现在网站的搜索栏、用户登录口等地方，常用来窃取客户端Cookies或进行钓鱼欺骗。

下面我们来看一个例子：

<img src="https://img-blog.csdnimg.cn/img_convert/7fa3c2daa3b62a1d02a540279124b394.png" alt="image.png">

这是一个普通的点击事件，当用户点击之后，就执行了js脚本，弹窗了警告。

<img src="https://img-blog.csdnimg.cn/img_convert/8bcb44b8974bf02c751a9a47c82de8fe.png" alt="image.png">

你会说，这能代表啥，那如果这段脚本是这样的呢？

<img src="https://img-blog.csdnimg.cn/img_convert/ed132ba0b67b4868e00f9054c9980810.png" alt="image.png">

当浏览器执行这段脚本，就盗用了用户的cookie信息，发送到了自己指定的服务器。你想想他接下来会干什么呢？

##### 第二种：存储型XSS攻击（持久型XSS攻击）

攻击者事先将恶意代码上传或者储存到漏洞服务器中，只要受害者浏览包含此恶意代码的页面就会执行恶意代码。这意味着只要访问了这个页面的访客，都有可能会执行这段恶意脚本，因此存储型XSS攻击的危害会更大。此类攻击一般出现在网站留言、评论、博客日志等交互处，恶意脚本存储到客户端或者服务端的数据库中。

增删改查在web管理系统中中很常见，我们找到一个新增功能页面，这以一个富文本输入框为例，输入以下语句，点击保存，再去查看详情，你觉得会发生什么？

<img src="https://img-blog.csdnimg.cn/img_convert/28216cd51f89dbd5de6423d701dfe9f7.png" alt="image.png">

没错，如果是前端的同学或许已经猜到了，h是浏览器的标签，这样传给服务器，服务器再返回给前端，浏览器渲染的时候，会把第二行当成h1标签来渲染，就会出现以下效果，第二行文字被加粗加大了。

<img src="https://img-blog.csdnimg.cn/img_convert/35ad9d6eb7ca192b724003a271a85239.png" alt="image.png">

这里我只是输入了普通的文本，而近几年随着互联网的发展，出现了很多h5多媒体标签，那要是我利用它们呢？ 不清楚的同学，可自行打开W3cschool网站查看：

<img src="https://img-blog.csdnimg.cn/img_convert/5dcdab5672dc3e754af904b068177bcd.png" alt="image.png">

**黑客是怎么攻击我们的呢？黑客会自己写一些脚本，来获取我们的cookies敏感等信息，然后他发送到他自己的服务器，当他拿到我们这些信息后，就能绕过前端，直接调后端的接口，比如提现接口，想想是不是很恐怖！！！**

<img src="https://img-blog.csdnimg.cn/img_convert/687f18da3281e9df07cf2f18b4456458.png" alt="image.png">

这里我利用一个在线远程网站来模拟XSS攻击。地址如下：  目前网站还能访问，同学们可以自己体验一下，如果后期链接失效不可访问了，同学们可以重新找一个，或者自己手写一个脚本，然后伪装成svg上传到自己的服务器。 我们在地址栏输入上面这个地址，来看看实际效果，提示你已经触发了XSS攻击。 <img src="https://img-blog.csdnimg.cn/img_convert/cc38cf8e6c489c77094735f8f91c8a53.png" alt="image.png">

当我们点击确定，出现了一个黑人，哈哈哈，恭喜你，你银行卡里的钱已经全被黑客取走了。这就是黑客得逞后的样子，他得逞后还在嘲讽你。

<img src="https://img-blog.csdnimg.cn/img_convert/d6236e86ab9f193a208e1e602c576b5b.png" alt="image.png">

**接下来，我们利用多媒体标签和这个脚本来攻击我们实际的的网站。**

这里记得在地址前面加上//表示跨越，如图：

<img src="https://img-blog.csdnimg.cn/img_convert/1ca931af1b6c197b7a62a7eb1f7ea3fe.png" alt="image.png"> 当我们点击保存之后，再去查看详情页面发现。

<img src="https://img-blog.csdnimg.cn/img_convert/f83b948cf01ec2d84c1f08100588ca89.png" alt="image.png">

哦豁，刚刚那个网站的场景在我们的web管理系统里面触发了，点击确定，那个小黑人又来嘲讽你了。

<img src="https://img-blog.csdnimg.cn/img_convert/d7353c99bed30db7f758ecc8eed754b9.png" alt="image.png">

**这脚本在我们的管理系统成功运行，并获取了我们的敏感信息，就可以直接绕过前端，去直接掉我们后端银行卡提现接口了。并且这类脚本由于保存在服务器中，并存着一些公共区域，网站留言、评论、博客日志等交互处，因此存储型XSS攻击的危害会更大。**

##### 第三种：DOM-based型XSS攻击

客户端的脚本程序可以动态地检查和修改页面内容，而不依赖于服务器端的数据。例如客户端如从URL中提取数据并在本地执行，如果用户在客户端输入的数据包含了恶意的JavaScript脚本，而这些脚本没有经过适当的过滤或者消毒，那么应用程序就可能受到DOM-based型XSS攻击。

下面我们来看一个例子

<img src="https://img-blog.csdnimg.cn/img_convert/8768dd3a357acee3753f8b8c6b779162.png" alt="image.png">

这段代码的意思是点击提交之后，将输入框中的内容渲染到页面。效果如下面两张图。

①在输入框中输入内容

<img src="https://img-blog.csdnimg.cn/img_convert/d5042eb7983acf328485b0571055c355.png" alt="image.png">

②点击确定，输入框中的内容渲染到页面

<img src="https://img-blog.csdnimg.cn/img_convert/2329df5c660d6782242dece3e78f1612.png" alt="image.png">

那如何我们输内容是不是普通文本，而是恶意的脚本呢？

<img src="https://img-blog.csdnimg.cn/img_convert/08bf7d8acea728eca0a06bf4518cfd7c.png" alt="image.png">

没错，恶意的脚本在渲染到页面的时候，没有被当成普通的文本，而是被当成脚本执行了。 <img src="https://img-blog.csdnimg.cn/img_convert/f382b6b6e70bf19ee9667d62c616a1f6.png" alt="image.png">

**总结：XSS就是利用浏览器不能识别是普通的文本还是恶意代码，那么我们要做的就是阻止恶意代码执行，比如前端的提交和渲染，后端接口的请求和返回都要对此类特殊标签做转义和过滤处理，防止他执行脚本，泄露敏感的数据。感兴趣的同学可以根据我上面的步骤，自己去模拟一个XSS攻击，让自己也体验一次当黑客的感觉。**

**题外话**

随着信息技术的快速发展和互联网的普及，IT行业 成为一个非常热门的领域，也是目前就业前景非常广阔的领域之一。

IT行业是一个非常庞大和多样化的行业，包括软件开发、网络安全、数据分析、云计算等等领域。因此，就业前景也是非常广泛和多样化的，不同的领域和职位都具有不同的就业前景和发展机会。

在软件开发领域，由于软件已经成为现代社会不可或缺的一部分，因此对软件开发人才的需求也越来越大。特别是在移动应用、大数据、人工智能等领域，软件开发人才的需求更是迅速增长。因此，软件开发人才的就业前景非常广阔，尤其是那些熟练掌握多种编程语言和技术的人才。

有幸看到一篇这样一组数据。

<img src="https://img-blog.csdnimg.cn/c3114b9c3bf947adb177b7aaf91e1be5.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/d5f06d6b9945fd6e8a5f92a0198e5446.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/9cf857398f52a97ff49d437ac5fe690a.png" alt="">

根据这些我不得总结，it行业确实人才紧缺，

##### 行业发展空间大，岗位非常多

网络安全行业产业以来，随即新增加了几十个网络安全行业岗位︰网络安全专家、网络安全分析师、安全咨询师、网络安全工程师、安全架构师、安全运维工程师、渗透工程师、信息安全管理员、数据安全工程师、网络安全运营工程师、网络安全应急响应工程师、数据鉴定师、网络安全产品经理、网络安全服务工程师、网络安全培训师、网络安全审计员、威胁情报分析工程师、灾难恢复专业人员、实战攻防专业人员…

##### 职业增值潜力大

网络安全专业具有很强的技术特性，尤其是掌握工作中的核心网络架构、安全技术，在职业发展上具有不可替代的竞争优势。

随着个人能力的不断提升，所从事工作的职业价值也会随着自身经验的丰富以及项目运作的成熟，升值空间一路看涨，这也是为什么受大家欢迎的主要原因。

从某种程度来讲，在网络安全领域，跟医生职业一样，越老越吃香，因为技术愈加成熟，自然工作会受到重视，升职加薪则是水到渠成之事。

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
