
--- 
title:  github入门教程（非常详细）从零基础入门到精通，看完这一篇就够了 
tags: []
categories: [] 

---
如果你是一枚Coder，但是你不知道Github，那么我觉的你就不是一个菜鸟级别的Coder，因为你压根不是真正Coder，你只是一个Code搬运工。说明你根本不善于突破自己！为什么这么说原因很简单，很多优秀的代码以及各种框架源码都存放于github当中！

##### 目录
<li> 
  <ul>- github登录与注册- gitbash安装步骤详解- gitbash常用命令- 获取ssh密钥- 绑定ssh密钥- 代码克隆- 测试提交文件
首先，我先对GitHub来一个简单介绍，GitHub他就是一个远程仓库，远程仓库通俗的理解就是一个可以保存自己代码的地方，在实际开发当中一个项目往往是有多个人来共同协作开发完成的，那么就需要一个统一代码保存的地方，而GitHub就是起到一个共享和汇总代码的作用。

#### github登录与注册

>  
 github属于国外的平台，所以我们打开的时候有时候比较慢，这里我写了一个解决打开慢的解决方案： 


官方登录页: 

<img src="https://img-blog.csdnimg.cn/20210108224745948.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

注册页: 

相对来说注册还是很简单的，只需要一个邮箱即可，邮箱写qq邮箱就行了，假如以后忘记密码了，是可以靠邮箱来找回密码的。

<img src="https://img-blog.csdnimg.cn/20210108225039353.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

官网全是英文的，目前的话，暂未发现有中文版的，对于英语不好的同学建议使用谷歌浏览器，谷歌浏览器可以翻译网页变为中文使用起来十分方便。

登录进去之后，在这里我们可以创建一个自己的库。

<img src="https://img-blog.csdnimg.cn/20210108233427791.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

翻译成中文之后创建库的一些解释已经写得很清楚了哦

这里无非需要注意的就是库分为两种，分为了公有的私有的，上面解释的很清楚了，大家自行选择即可。

<img src="https://img-blog.csdnimg.cn/20210108234242306.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

在创建完成自己的库之后，下面就要让自己的电脑克隆一个自己所创建的库，方面自己电脑上的代码同步到GitHub你所创建的库当中。为了实现，就需要安装一个软件，Git Bash。

#### gitbash安装步骤详解

git bash是Windows下的命令行工具。 基于msys GNU环境，有git分布式版本控制工具。 主要用于git版本控制，上传下载项目代码。

GitHub官网:  首先进入GitHub官网，下载适合自己电脑的版本

下载的时候有的时候特别慢，这里我给大家一个我下载好的，虽然不是最新版本但是绝对是可以用的。

链接:  提取码：aunu

<img src="https://img-blog.csdnimg.cn/20210111001411706.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt=""> <img src="https://img-blog.csdnimg.cn/20210109224242715.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt=""> <img src="https://img-blog.csdnimg.cn/20210110145839970.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt=""> <img src="https://img-blog.csdnimg.cn/20210109224259809.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

**往下我就不给大家截图了，总之就是一路Next就可以了！**

下载好之后随便找个文件夹右键会发现有个git bash这就证明安装好了

<img src="https://img-blog.csdnimg.cn/20210110150130999.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

#### gitbash常用命令

git init 初始化 git，只有初始化了以后才可以使用 git 相关命令。 git clone 获取远程项目，并下载到本地。远程库的地址在 GITHUB 项目中会有提供。 git status 查看本地修改与服务器的差异。 git add . 将这些差异文件添加，这样就可以提交了。 git commit –m “这里是注释” 提交更改到服务器。 git checkout master 更改到master库。 git pull 将服务器最新的更改获取到本地。 git merge local master 将本地的local合并到远程的master上。 git push origin master 正式提交到远程的master服务器上。 还有“git tag”，“git diff”，“git show”，“git log”，“git remote”等。

#### 获取ssh密钥

打开输入：ssh-keygen -t rsa -C “git账号” 输入之后一路Enter（确认）就可以了

<img src="https://img-blog.csdnimg.cn/20210111010036926.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

以上截图就证明成功了，这个时候打开以下地址： id_rsa.pub就是我们需要的ssh密钥了

<img src="https://img-blog.csdnimg.cn/20210110214035273.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

**注意**：有的可能以前生成过，就会报这个错了。

<img src="https://img-blog.csdnimg.cn/20210110150417301.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

报错解决: 

#### 绑定ssh密钥

现在你就需要登录到你的GitHub上边添加这个密匙

<img src="https://img-blog.csdnimg.cn/20210109192647110.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

将整个id_rsa.pub内容复制

<img src="https://img-blog.csdnimg.cn/20210111005907399.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

添加成功

<img src="https://img-blog.csdnimg.cn/20210110214812416.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

之后你就可以回到你的Git bash上边了 输入：ssh -T git@github.com 然后输入上边的代码，来检查是否成功绑定。如果输入之后选择yes出来是这样说明就成功了。

<img src="https://img-blog.csdnimg.cn/20210110215503352.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

接下来还需要简单的设置一些东西。 git config --global user.name “git账号” git config --global user.email “git邮箱，注册时候的邮箱”

<img src="https://img-blog.csdnimg.cn/20210110224155331.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

#### 代码克隆

下面就要将你的库克隆下来到本地电脑中，方便以后进行上传代码。

链接: 

<img src="https://img-blog.csdnimg.cn/20210110224822436.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

下面就要将你的库克隆下来到本地电脑中，方便以后进行上传代码。

在库创建完成之后 会有一个网址出现在网页中，这个地址就是代码地址。 git clone 命令会用的到

<img src="https://img-blog.csdnimg.cn/20210110225411595.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

接下来就开始选择文件存储地方了。

<img src="https://img-blog.csdnimg.cn/20210110225903563.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

git clone后边的网址就是你创建库成功之后的网址

git clone 地址（这个地址就是刚刚创建的库那个页面上代码地址）

**在执行命令过程有时候会让你输入账号密码啥的，这个不要输错了就行！**

<img src="https://img-blog.csdnimg.cn/20210111010201542.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

可以看到，指定目录已经存在了我们的库文件

<img src="https://img-blog.csdnimg.cn/20210110231511349.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

#### 测试提交文件

打开这个文件夹，然后在其中创建一个任意格式，任意名称的文件。

<img src="https://img-blog.csdnimg.cn/20210110232359167.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

然后在这个文件里面右键git bash进黑框框 git add我们新增的文件

<img src="https://img-blog.csdnimg.cn/20210110232529407.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

之后输入然后git commit -m “cc” 引号内的内容可以随意改动，这个语句的意思是 给你刚刚上传的文件一个备注，方便查找记忆而已

<img src="https://img-blog.csdnimg.cn/20210110232623696.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

然后在输入git push origin master 这个就代表成功了

<img src="https://img-blog.csdnimg.cn/20210111010300987.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

现在打开你的GitHub网站，找到你创建的库。 文件上传成功。

<img src="https://img-blog.csdnimg.cn/20210110233509888.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NjEwMTgzOQ==,size_16,color_FFFFFF,t_70" alt="">

**点个赞吧！**

希望更多的人看得到！

**学习网络安全技术的方法无非三种:**

第一种是报网络安全专业，现在叫网络空间安全专业，主要专业课程:程序设计、计算机组成原理原理、数据结构、操作系统原理、数据库系统、 计算机网络、人工智能、自然语言处理、社会计算、网络安全法律法规、网络安全、内容安全、数字取证、机器学习，多媒体技术，信息检索、舆情分析等。

第二种是自学，就是在网上找资源、找教程，或者是想办法认识一-些大佬，抱紧大腿，不过这种方法很耗时间，而且学习没有规划，可能很长一段时间感觉自己没有进步，容易劝退。

如果你对网络安全入门感兴趣，那么你需要的话可以点击这里**👉**

第三种就是去找培训。

<img src="https://img-blog.csdnimg.cn/img_convert/58bec76876e81d23709a090231e9e0bf.png" alt="image.png">

接下来，我会教你零基础入门快速入门上手网络安全。

网络安全入门到底是先学编程还是先学计算机基础？这是一个争议比较大的问题，有的人会建议先学编程，而有的人会建议先学计算机基础，其实这都是要学的。而且这些对学习网络安全来说非常重要。但是对于完全零基础的人来说又或者急于转行的人来说，学习编程或者计算机基础对他们来说都有一定的难度，并且花费时间太长。

##### 第一阶段：基础准备 4周~6周

这个阶段是所有准备进入安全行业必学的部分，俗话说：基础不劳，地动山摇 <img src="https://img-blog.csdnimg.cn/img_convert/44dd65e103a3ce90b8500717e19b108d.png" alt="image.png">

##### 第二阶段：web渗透

**学习基础 时间：1周 ~ 2周：**

① 了解基本概念：（SQL注入、XSS、上传、CSRF、一句话木马、等）为之后的WEB渗透测试打下基础。 ② 查看一些论坛的一些Web渗透，学一学案例的思路，每一个站点都不一样，所以思路是主要的。 ③ 学会提问的艺术，如果遇到不懂得要善于提问。 <img src="https://img-blog.csdnimg.cn/img_convert/442b7a338582713846cc447ecff221bd.png" alt="image.png">

**配置渗透环境 时间：3周 ~ 4周：**

① 了解渗透测试常用的工具，例如（AWVS、SQLMAP、NMAP、BURP、中国菜刀等）。 ② 下载这些工具无后门版本并且安装到计算机上。 ③ 了解这些工具的使用场景，懂得基本的使用，推荐在Google上查找。

##### **渗透实战操作 时间：约6周：**

① 在网上搜索渗透实战案例，深入了解SQL注入、文件上传、解析漏洞等在实战中的使用。 ② 自己搭建漏洞环境测试，推荐DWVA，SQLi-labs，Upload-labs，bWAPP。 ③ 懂得渗透测试的阶段，每一个阶段需要做那些动作：例如PTES渗透测试执行标准。 ④ 深入研究手工SQL注入，寻找绕过waf的方法，制作自己的脚本。 ⑤ 研究文件上传的原理，如何进行截断、双重后缀欺骗(IIS、PHP)、解析漏洞利用（IIS、Nignix、Apache）等，参照：上传攻击框架。 ⑥ 了解XSS形成原理和种类，在DWVA中进行实践，使用一个含有XSS漏洞的cms，安装安全狗等进行测试。 ⑦ 了解一句话木马，并尝试编写过狗一句话。 ⑧ 研究在Windows和Linux下的提升权限，Google关键词：提权 <img src="https://img-blog.csdnimg.cn/img_convert/820f500673a4a0a2432e6c3d7e2ba80e.png" alt="image.png"> 以上就是入门阶段

##### 第三阶段：进阶

已经入门并且找到工作之后又该怎么进阶？详情看下图 <img src="https://img-blog.csdnimg.cn/img_convert/b28d31c9a3414e91ec46eb307d360eab.png" alt="image.png">

给新手小白的入门建议： 新手入门学习最好还是从视频入手进行学习，视频的浅显易懂相比起晦涩的文字而言更容易吸收，这里我给大家准备了一套网络安全从入门到精通的视频学习资料包免费领取哦！

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
