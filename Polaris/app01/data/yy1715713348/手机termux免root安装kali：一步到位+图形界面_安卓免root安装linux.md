
--- 
title:  手机termux免root安装kali：一步到位+图形界面_安卓免root安装linux 
tags: []
categories: [] 

---
1.工具：

安卓（包括鸿蒙）手机、WiFi、充足的电量、脑子

2.浏览器搜索termux，vnc viewer，下载安装。

3.对抗华为纯净模式需要一些操作，先断网，弹窗提示先不开，等到继续安装的时候连上网，智能检测过后就可以了（termux正常版本可以通过智能监测，失败了就说明安装包是盗版）

4.以后出现类似

After this operation, 967 kB of additional disk space will be used.

Do you want to continue? [Y/n]

的东西，输入y按回车就好了。

打开termux，输入下面这些代码（直接粘贴）：

（先不要轻举妄动看完这篇文章不然你可能后悔）

下面是安装kali nethunder的：

pkg update &amp;&amp; pkg upgrade &amp;&amp; pkg install python &amp;&amp; pkg install git &amp;&amp; pkg install python2 &amp;&amp; git clone https://gitee.com/zhang-955/clone.git &amp;&amp; cd clone &amp;&amp; cd AutoInstallKali &amp;&amp; chmod +x kalinethunter finaltouchup.sh &amp;&amp; ./kalinethunter

下面是安装kali linux的：

pkg install wget openssl-tool proot -y &amp;&amp; hash -r &amp;&amp; wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh &amp;&amp; bash kali.sh

我会以上面那个为案例，下面的安装特别精简，懒得整。

估计安装需要30分钟到8小时。以前特别慢，几十k每秒，现在我这边能到5m每秒。

进入kali方式：<img src="https://img-blog.csdnimg.cn/direct/96342871352947f98f1fee77a7216495.png" alt="在这里插入图片描述">

默认root没有密码，kali密码是kali，输密码是看不到的

接下来又来到图形界面了，root权限下执行：

wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/DesktopEnvironment/Apt/Xfce4/de-apt-xfce4.sh &amp;&amp; bash de-apt-xfce4.sh

执行完后会让你输入密码，输入一个自定密码即可。<img src="https://img-blog.csdnimg.cn/direct/1ce722333a94410e8a77eadfd701758c.png" alt="在这里插入图片描述">

打开vnc的APP，像这样设置

<img src="https://img-blog.csdnimg.cn/direct/d91aac841b2d4afbb0c96e1c562ebc47.png" alt="在这里插入图片描述">

输入密码，进入！<img src="https://img-blog.csdnimg.cn/direct/39b4633f82c949cf854b8bad77c929c3.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/6fbdfac462014448bfca7850e41265ee.jpg" alt="6fbdfac462014448bfca7850e41265ee.jpg">

Ok愉快的结束了，有问题评论区指正，求赞！谢谢！

**今天只要你给我的文章点赞，我私藏的网安学习资料一样免费共享给你们，来看看有哪些东西。**

### 网络安全学习资源分享:

最后给大家分享我自己学习的一份全套的网络安全学习资料，希望对想学习 网络安全的小伙伴们有帮助！

零基础入门

对于从来没有接触过网络安全的同学，我们帮你准备了详细的学习成长路线图。可以说是最科学最系统的学习路线，大家跟着这个大的方向学习准没问题。



## 学习资料分享

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
