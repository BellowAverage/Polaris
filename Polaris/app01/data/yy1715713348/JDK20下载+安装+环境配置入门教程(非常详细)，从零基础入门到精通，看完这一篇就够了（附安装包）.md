
--- 
title:  JDK20下载+安装+环境配置入门教程(非常详细)，从零基础入门到精通，看完这一篇就够了（附安装包） 
tags: []
categories: [] 

---
**软件下载**
<td rowspan="1" colspan="2" width="260">软件：JDK</td><td rowspan="1" colspan="2" width="277">版本：20</td>
<td rowspan="1" colspan="2" width="258">语言：简体中文</td><td rowspan="1" colspan="2" width="277">大小：159.60M</td>
<td rowspan="1" colspan="4" width="298">安装环境：Win7及以上版本；64位操作系统</td>
<td colspan="4" rowspan="1" height="24" width="585">硬件要求：CPU@2.0GHz ；内存@4G(或更高）</td>
<td rowspan="1" colspan="4" width="298">下载通道①百度网盘丨64位下载链接：https://pan.baidu.com/s/1AbHK3yqFHhlxb1VX1LnJ7g?pwd=6789提取码：6789</td>

提取码：6789
<td rowspan="1" colspan="4" width="298"> </td>

1、**软件介绍**

## JDK全称Java SE Development kit(JDK)，即java标准版开发包，是Oracle提供的一套用于开发java应用程序的开发包，它提供编译，运行java程序所需要的各种工具和资源，包括java编译器，java运行时环境，以及常用的java类库等。

2，切换Windows系统，然后点击下载（初学者下载X64 Installer就可）

<img src="https://img-blog.csdnimg.cn/c0ad576cec8140198a8046e3c140c7d7.png" alt="">

3，下载完成后可移动到指定文件夹进行解压（本贴选择放在D盘目录下）

<img src="https://img-blog.csdnimg.cn/a9a4c01029bc479b8bedc67e2f14719c.png" alt="">

4，配置JDK的环境变量，开始-&gt;设置-&gt;系统-&gt;关于-&gt;高级系统设置-&gt;环境变量（本帖以win10为例）

<img src="https://img-blog.csdnimg.cn/1de62ae355bf4ac5a09aca586ac4036c.png" alt="">

5，点击新建系统变量名为"JAVA_HOME"，变量值为"%JDK-20%"，此处可以配置多个JDK版本用于以后的开发需求，切换JDK版本时更改"JAVA_HOME"的变量值即可快速切换。

<img src="https://img-blog.csdnimg.cn/b62232d7e933491fbc87e52df5186184.png" alt="">

<img src="https://img-blog.csdnimg.cn/d76ce90b249d499daacc161313337211.png" alt="">

6，再次新建系统变量名为"JDK-20"，变量值指定路径为"D:\jdk-20"(第三步中解压后存放jdk-20的路径)

设置成功后点击确定

<img src="https://img-blog.csdnimg.cn/ebfef174041b44dcb4e066a3c2bb3f0d.png" alt="">

7，点击新建系统变量名为"CLASSPATH"，变量值为".;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar;%JAVA_HOME%\lib;"

设置成功后点击确定

<img src="https://img-blog.csdnimg.cn/5939124287d0471b9ec834b85524678a.png" alt="">

8，在系统变量中找到Path变量点击进行编辑

<img src="https://img-blog.csdnimg.cn/2fb52262c0fe4d109d1c6ceb23a39664.png" alt="">

9，点击新建输入"%JAVA_HOME%\bin"，并将其上移到最上方后确定保存（操作如下）

<img src="https://img-blog.csdnimg.cn/6a415324ddc846c38acf0b8cf192d97f.png" alt="">

<img src="https://img-blog.csdnimg.cn/920c422ec0f44e42a6ce920c3349f570.png" alt="">

10，开始测试JDK20是否安装成功，使用快捷指令"Win+R"输入"cmd"打开命令窗口，输入"java"，点击回车，输入"java -version"，点击回车出现JDK20的版本信息则表示JDK已经安装成功，如下：

<img src="https://img-blog.csdnimg.cn/b100a51617e449348027c2d59962334c.png" alt="">

<img src="https://img-blog.csdnimg.cn/a7d5a947b16c4748bb026f24746261be.png" alt="">

11，（有基础的可以试试）用记事本编辑一个简单的java文件进行编译输出

<img src="https://img-blog.csdnimg.cn/023875b078e943dc9229cbd9c9489059.png" alt="">

<img src="https://img-blog.csdnimg.cn/b789e753df4c4bdca62e8d24d4e9b781.png" alt="">

随着信息技术的快速发展和互联网的普及，IT行业 成为一个非常热门的领域，也是目前就业前景非常广阔的领域之一。

IT行业是一个非常庞大和多样化的行业，包括软件开发、网络安全、数据分析、云计算等等领域。因此，就业前景也是非常广泛和多样化的，不同的领域和职位都具有不同的就业前景和发展机会。

在软件开发领域，由于软件已经成为现代社会不可或缺的一部分，因此对软件开发人才的需求也越来越大。特别是在移动应用、大数据、人工智能等领域，软件开发人才的需求更是迅速增长。因此，软件开发人才的就业前景非常广阔，尤其是那些熟练掌握多种编程语言和技术的人才。

有幸看到一篇这样一组数据。

<img src="https://img-blog.csdnimg.cn/c3114b9c3bf947adb177b7aaf91e1be5.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/d5f06d6b9945fd6e8a5f92a0198e5446.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/9cf857398f52a97ff49d437ac5fe690a.png" alt="">

根据这些我不得总结，it行业确实人才紧缺，

##### **网络安全行业特点**

1、就业薪资非常高，涨薪快 2021年猎聘网发布网络安全行业就业薪资行业最高人均33.77万！

2、人才缺口大，就业机会多

2019年9月18日《中华人民共和国中央人民政府》官方网站发表：我国网络空间安全人才 需求140万人，而全国各大学校每年培养的人员不到1.5W人。猎聘网《2021年上半年网络安全报告》预测2027年网安人才需求300W，现在从事网络安全行业的从业人员只有10W人。

##### 行业发展空间大，岗位非常多

网络安全行业产业以来，随即新增加了几十个网络安全行业岗位︰网络安全专家、网络安全分析师、安全咨询师、网络安全工程师、安全架构师、安全运维工程师、渗透工程师、信息安全管理员、数据安全工程师、网络安全运营工程师、网络安全应急响应工程师、数据鉴定师、网络安全产品经理、网络安全服务工程师、网络安全培训师、网络安全审计员、威胁情报分析工程师、灾难恢复专业人员、实战攻防专业人员…

##### 职业增值潜力大

网络安全专业具有很强的技术特性，尤其是掌握工作中的核心网络架构、安全技术，在职业发展上具有不可替代的竞争优势。

随着个人能力的不断提升，所从事工作的职业价值也会随着自身经验的丰富以及项目运作的成熟，升值空间一路看涨，这也是为什么受大家欢迎的主要原因。

从某种程度来讲，在网络安全领域，跟医生职业一样，越老越吃香，因为技术愈加成熟，自然工作会受到重视，升职加薪则是水到渠成之事。

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

**如果你对网络安全感兴趣，学习资源免费分享，保证100%免费！！！（嘿客入门教程）**

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
