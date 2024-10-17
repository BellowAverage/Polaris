
--- 
title:  SQL server 2017安装教程 
tags: []
categories: [] 

---
>  
 ✅作者简介：CSDN内容合伙人、阿里云专家博主、51CTO专家博主🏆 📃个人主页： 🔥系列专栏：🥇 💬个人格言：不断的翻越一座又一座的高山，那样的人生才是我想要的。这一马平川，一眼见底的活，我不想要,我的人生，我自己书写，余生很长，请多关照，我的人生，敬请期待💖💖💖 


<img src="https://img-blog.csdnimg.cn/a833ad51811042b8b4c2cc73310cee0d.png#pic_center" alt="在这里插入图片描述">



#### SQL server 2017安装教程
- - - 


## SQL server简介

由Microsoft公司公布的SQL server是一种典型的关系型数据库管理系统。（功能强大，操作便捷，具有稳定安全的性能） 在SQL server的发展历史中，SQL server 2017是具有里程碑意义的一个版本，因为这是跨出Windows的第一个版本，标志着SQL server在linux平台上首次使用。 SQL server 2017的版本包括企业（Enterprise）版、标准（Standard）版、网页（Web）版、开发者（Developer）版、和精简（Express）版。其中【Express】版是免费版

## 安装步骤

**安装SQL server 2017 【Express】版步骤如下：**

💬下载地址： 【提取码】<font color="red" size="3">HCMY</font>

✅打开解压后的文件夹，选中【jdk-8u144-windows-x64.exe】点击鼠标【右键】&gt;【以管理员身份运行】

<img src="https://img-blog.csdnimg.cn/371956666cbf4039a354616b01cecf44.png" alt="在这里插入图片描述"> ✅点击【下一步】

<img src="https://img-blog.csdnimg.cn/771f7d327414463582670e9a52d220db.png" alt="在这里插入图片描述">

✅点击【下一步】（请勿更改安装路径）

<img src="https://img-blog.csdnimg.cn/07009c37bdb349ec98a28e1c8df0a02b.png" alt="在这里插入图片描述"> ✅点击【下一步】

<img src="https://img-blog.csdnimg.cn/326b81b49ede42b0a6aab8efd4572f2c.png" alt="在这里插入图片描述"> ✅点击【关闭】

<img src="https://img-blog.csdnimg.cn/0737f957db064d209f8d6ecb4496d851.png" alt="在这里插入图片描述"> ✅选中【此电脑】点击鼠标【右键】&gt;【属性】

<img src="https://img-blog.csdnimg.cn/0a6eaf3ce1704e43910c79ccc94d8893.png" alt="在这里插入图片描述"> ✅点击【高级系统设置】&gt;【高级】&gt;【环境变量】

<img src="https://img-blog.csdnimg.cn/d79ac1bac1824708877aa3a76fc65d2b.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/28c5d191d45f4d638950f25f369a0aa2.png" alt="在这里插入图片描述"> ✅在【用户变量】这里，点击【新建】，输入变量名【JAVA_HOME】，变量值【C:\Program Files\Java\jdk1.8.0_144】，点击【确定】

<img src="https://img-blog.csdnimg.cn/1d2630c120074f8aa3d934bd2c169f2a.png" alt="在这里插入图片描述"> ✅在【用户变量】处，继续点击【新建】，输入变量名【CLASSPATH】，变量值【.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar】，点击【确定】

<img src="https://img-blog.csdnimg.cn/54de5b5e94ad46549e9fe97c7eb6cf96.png" alt="在这里插入图片描述"> ✅继续在【用户变量】处点击【新建】，输入变量名【Path】，变量值【.;%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin】，点击【确定】

<img src="https://img-blog.csdnimg.cn/4ce23c7b7f294d6eb72ae8ec2102e4b0.png" alt="在这里插入图片描述"> ✅新建好3个用户变量后，点击【确定】

<img src="https://img-blog.csdnimg.cn/0e93181118944980b5c30dc335702f0f.png" alt="在这里插入图片描述">

✅命令行输入java -version

<img src="https://img-blog.csdnimg.cn/bb2f7546cb384c44b073033ec313d484.png" alt="在这里插入图片描述"> ✅配置完成

<img src="https://img-blog.csdnimg.cn/75003fd226014b07a6ce08b5e0a50b4f.png" alt="在这里插入图片描述"> ✅回到解压后的文件夹里，双击打开【cn_sql_server_2017】文件夹 <img src="https://img-blog.csdnimg.cn/e91670baf26d4ce5bc1f58b1bb00b7b0.png" alt="在这里插入图片描述"> ✅选中【setup.exe】点击鼠标【右键】&gt;【以管理员身份运行】

<img src="https://img-blog.csdnimg.cn/2d41cf2ca5704637a32df48114436f53.png" alt="在这里插入图片描述"> ✅点击【安装】&gt;【全新SQL Server独立安装或向现有安装添加功能】

<img src="https://img-blog.csdnimg.cn/b67e7699e8414ee2845882d6ca069a3a.png" alt="在这里插入图片描述"> ✅选择【Express精简版】，点击【下一步】

<img src="https://img-blog.csdnimg.cn/22491f2552eb4cc1bdf7c6658238d387.gif#pic_center" alt="在这里插入图片描述"> ✅勾选【我接受许可条款】点击【下一步】

<img src="https://img-blog.csdnimg.cn/e6524e196ddb4927a831811b2d6b8f65.png" alt="在这里插入图片描述"> ✅点击【下一步】

<img src="https://img-blog.csdnimg.cn/2899d41cd1524d75bdf9ac0b71ecc2c3.png" alt="在这里插入图片描述"> ✅根据自己的需求，勾选安装的功能； 修改文件位置，可以把地址中的【C】直接改成D或E等其他盘（建议不要安装到C盘），然后点击【下一步】

<img src="https://img-blog.csdnimg.cn/9e4b792566254849b35b31c9310a9e5a.png" alt="在这里插入图片描述"> ✅点击【下一步】（可以默认实例也可以命名实例，看个人需求）

<img src="https://img-blog.csdnimg.cn/c34d48c447be49c09f31e9af556b7ad6.png" alt="在这里插入图片描述"> ✅点击【下一步】

<img src="https://img-blog.csdnimg.cn/fe9943d1fc1641519549b734839f1650.png" alt="在这里插入图片描述">

✅选择【混合模式】，设置密码（建议设置简单点，自己能记住的，）；点击【添加当前用户】，点击【下一步】

<img src="https://img-blog.csdnimg.cn/38c9e9239a8d49ccbd6ee2a83b15c5b9.png" alt="在这里插入图片描述"> ✅点击【安装】

<img src="https://img-blog.csdnimg.cn/f6fbba0c5ec942099bdc66f7f798575a.png" alt="在这里插入图片描述"> ✅安装完成，点击【关闭】

<img src="https://img-blog.csdnimg.cn/da68815d17d44776ba2414fb7d87b87c.png" alt="在这里插入图片描述">

✅选中【SSMS-Setup-CHS.exe】点击鼠标【右键】&gt;【以管理员身份运行】

<img src="https://img-blog.csdnimg.cn/c2c848a8583c45419737ac80c0aceb1a.png" alt="在这里插入图片描述"> ✅点击【安装】

<img src="https://img-blog.csdnimg.cn/c94664479f8c4a6198fc45b2084ab0a5.png" alt="在这里插入图片描述"> ✅安装完成，点击【关闭】

<img src="https://img-blog.csdnimg.cn/939edef2ab80487f999cc162214e1643.png" alt="在这里插入图片描述"> ✅打开电脑左下角【开始】菜单，找到 【Microsoft SQL Server Management Studio 17】，直接拖拽到桌面，创建桌面快捷方式

<img src="https://img-blog.csdnimg.cn/71495c47165540cd9a5d1c1cd9a75af9.gif#pic_center" alt="在这里插入图片描述"> ✅双击【Microsoft SQL Server Management Studio 17】图标，启动软件，然后点击【连接】

<img src="https://img-blog.csdnimg.cn/d3ffcd86a30f41b9872130b05f39c148.png" alt="在这里插入图片描述"> ✅安装完成

<img src="https://img-blog.csdnimg.cn/41984a0c1ae849339ddc847d2e49b9ee.png" alt="在这里插入图片描述">

## 结束语🥇

✅我的博客即将同步至腾讯云开发者社区，邀请大家一同入驻：

<img src="https://img-blog.csdnimg.cn/5b80ea7dab574ae5bb3fda934fe3f872.gif#pic_center" alt="在这里插入图片描述">
