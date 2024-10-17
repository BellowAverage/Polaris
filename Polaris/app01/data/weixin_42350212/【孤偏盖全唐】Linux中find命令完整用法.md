
--- 
title:  【孤偏盖全唐】Linux中find命令完整用法 
tags: []
categories: [] 

---
**目录**









>  
 <h3 id="%E7%AC%AC%E4%B8%80%E9%83%A8%E5%88%86%20-%20%E6%9F%A5%E6%89%BE%E5%90%8D%E7%A7%B0%E6%9F%A5%E6%89%BE%E6%96%87%E4%BB%B6%E7%9A%84%E5%9F%BA%E6%9C%AC%E6%9F%A5%E6%89%BE%E5%91%BD%E4%BB%A4">**第一部分 - 查找名称查找文件的基本查找命令**</h3> 


1.使用当前目录中的名称查找文件

在当前工作目录中查找名称为test.c的所有文件。

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/c4674483e3c7e7fc3fc4e0ff22f7eb58.png">

 



2.在主目录下查找文件

查找/ home目录下的所有文件，名称为test。   

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/4342fb61e242efe0798071825d7776bf.png">

 





(上文中的前面两个find没有权限)

3.使用名称和忽略案例查找文件

找到名称为test的所有文件，并在/ home目录中同时包含大写和小写字母。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/561576bfcd5058c4b2819fef3b961c10.png">

 





4.使用名称查找目录

在/目录中查找名称为test的所有目录。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/43da7df6f64f654868d8e3f5720e5b83.png">

 

5.使用名称查找PHP文件

在当前工作目录中查找名为test.PHP的所有PHP文件。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/229156b4294786146e4a6ba46d974a15.png">

 



6.查找目录中的所有PHP文件

查找目录中的所有php文件。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/0973a365b1cfee24badbbaf07e582f40.png">

 

 

>  
 <h3 id="%E7%AC%AC%E4%BA%8C%E9%83%A8%E5%88%86%20-%20%E6%A0%B9%E6%8D%AE%E4%BB%96%E4%BB%AC%E7%9A%84%E6%9D%83%E9%99%90%E6%9F%A5%E6%89%BE%E6%96%87%E4%BB%B6">**第二部分 - 根据他们的权限查找文件**</h3> 


7.查找777个权限的文件

查找权限为777的所有文件 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/850c3f1771f7badf15b5309c9bc6a908.png">

 







8.查找没有777权限的文件

查找所有文件未经许可777。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/4d5ef5c16dafa40cb9ca89f220f52970.png">

 

9.查找具有644个权限的SGID文件

查找权限设置为644的所有SGID位文件。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/350ed9954d953a5a2a6d61fc572b16f8.png">

 



10.找到具有551权限的粘滞位文件

查找权限为551的所有Sticky Bit设置文件。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/8e2f97f365efc22ae3320abb489aa9bf.png">

 

11.查找SUID文件

查找所有SUID集文件。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/5b8801f9b3781d9b632eebc4689ec763.png">

 

12.查找SGID文件

查找所有SGID设置文件 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/bba19b5c7042c7cb80a1daf06ea1aacc.png">

 

13.查找只读文件

查找所有只读文件。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/6e8109dfa2d9761913ed7773ad437a27.png">

 

14.查找可执行文件

查找所有可执行文件。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/abb61ee4c44c29bcaa0a2005e27d8ae9.png">





15.找到777个权限和Chmod到644的文件

查找所有777个权限文件，并使用chmod命令将权限设置为644 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/75c87d2e1e7658a7c39a7fab483345ee.png">







16.找到具有777个权限的目录和Chmod到755

查找所有777个权限目录，并使用chmod命令将权限设置为755。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/d00542f4481a01dcd448ccb61c0d732d.png">

 

17.查找并删除单个文件

找到一个名为test.c的文件并将其删除 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/9a7b34f62c35a318770f72f8c5d92169.png">





18.查找并删除多个文件

查找和删除多个文件，如.mp3或.txt，然后使用。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/5ef3aefdd8411314d512ccc9a9e3c8ec.png">







19.查找所有空文件

在特定路径下查找所有空文件。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/be1001114cf6d3030060ae9cf3f37dd6.png">







20.查找所有空目录

将特定路径下的所有空目录归档。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/059740b58d1298549cf40d4394a6ecde.png">







21.文件所有隐藏文件

要查找所有隐藏的文件，请使用以下命令。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/f6e06ed153510050274099c7fefacf6f.png">









 

>  
 **第三部分 - 基于所有者和组的搜索文件** 


22.查找基于用户的单个文件

在所有者root的/ root目录下查找名为test.c的所有或单个文件。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/d80753b3f696f7ba93b63d7b572c2d4a.png">







23.查找基于用户的所有文件

查找~目录下属于用户neil的所有文件。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/2d72fbb1e4bbfe060a85f49077310403.png">







 

24.查找基于组的所有文件

查找/ home目录下属于Group Developer的所有文件。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/5f0ef28993c0642d23f1edd7578092a1.png">







25.查找用户的特定文件

查找~目录下的用户neil的所有.txt文件 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/d28501ae1effa6f7e717e79a212a46d5.png">









 

>  
 <h3 id="%E7%AC%AC%E5%9B%9B%E9%83%A8%E5%88%86%20-%20%E6%A0%B9%E6%8D%AE%E6%97%A5%E6%9C%9F%E5%92%8C%E6%97%B6%E9%97%B4%E6%9F%A5%E6%89%BE%E6%96%87%E4%BB%B6%E5%92%8C%E7%9B%AE%E5%BD%95">**第四部分 - 根据日期和时间查找文件和目录**</h3> 


26.查找最近50天修改的文件

查找50天后修改的所有文件。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/3820287dd94223fa121b58cf0787e4ed.png">







27.查找最近50天访问的文件

查找50天后访问的所有文件。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/8a43c009ee5c425ca1740d1df7608f70.png">







28.查找最后50-100天修改的文件

查找所有被修改超过50天以及少于100天的文件。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/491515e6bebf5e6a255f06df46f1ca31.png">







 

29.在过去1小时内查找更改的文件

查找最近1小时内更改的所有文件 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/6997f912d6c192c37736968c9a6ab1f4.png">







 

30.在最近1小时内查找修改的文件

查找最近1小时内修改的所有文件。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/0fe1aa6bf34a809b00ed26db1c286a6f.png">

 







31.查找最近1小时内访问的文件

查找最近1小时内访问的所有文件。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/f06d61bacc9f18685902ec7bbbadf3cc.png">

  

>  
 <h3 id="%E7%AC%AC%E4%BA%94%E9%83%A8%E5%88%86%20-%20%E6%A0%B9%E6%8D%AE%E5%A4%A7%E5%B0%8F%E6%9F%A5%E6%89%BE%E6%96%87%E4%BB%B6%E5%92%8C%E7%9B%AE%E5%BD%95">**第五部分 - 根据大小查找文件和目录**</h3> 


32.找到50MB的文件

要找到所有50MB的文件，请使用。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/53e169b837a9289f9cb34e83e3236c1e.png">







33.查找大小在50MB到100MB之间

找到大于50MB且小于100MB的所有文件。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/94d0678c77c39ffb185cf43cad07ce78.png">







 

34.查找并删除100MB的文件

查找所有100MB文件并使用一个命令删除它们。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/523ae9f0b0ba37f3bb05eecd035ed1ac.png">







35.查找特定文件并删除

查找超过10MB的所有.mp3文件，并使用一个命令删除它们 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/cd8f5407b7efaf552e028b37483e7f61.png">

 

###  推荐阅读

#### 【资源推荐】
-  <h4 id="%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%93%E7%94%A8%E7%B3%BB%E7%BB%9F">**渗透测试专用系统**</h4> - kali-linux-e17-2019.1a-amd64.iso系统镜像- - kali-linux-2018.4-amd64 操作系统- - manjaro-xfce-17.1.7-stable-x86_64.iso系统镜像- - WiFi专用渗透系统 nst-32-11992.x86_64.iso操作系统镜像- - Parrot-security-4.1_amd64.iso 操作系统镜像- - manjaro-xfce-17.1.7-stable-x86_64 操作系统- - cyborg-hawk-linux-v-1.1 操作系统- - <li> <h4 id="%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E7%9B%B8%E5%85%B3%E5%B7%A5%E5%85%B7">渗透测试相关工具</h4> - **<strong>**</strong>- 【kali常用工具】上网行为监控工具       - - 【kali常用工具】抓包工具Charles Windows64位 免费版- - 【kali常用工具】图印工具stamp.zip- - 【kali常用工具】brutecrack工具[WIFIPR中文版]及wpa/wpa2字典- - 【kali常用工具】EWSA 5.1.282-破包工具- - 【kali常用工具】Realtek 8812AU KALI网卡驱动及安装教程- - 【kali常用工具】无线信号搜索工具_kali更新- - 【kali常用工具】inssider信号测试软件_kali常用工具- - 【kali常用工具】MAC地址修改工具 保护终端不暴露- - 【kali常用工具】脚本管理工具 php和jsp页面 接收命令参数 在服务器端执行- 
#### 渗透测试相关工具


- **Java实现照片GPS定位【完整脚本】**- - **Python实现照片GPS定位【完整脚本】**- - **女神忘记相册密码 python20行代码打开【完整脚本】**- - **<strong>**</strong>- 
**python实战**
- **<strong>******</strong>- **<strong>**</strong>- **<strong>**...</strong>- **<strong>**</strong>- **<strong>**</strong>- **<strong>**********</strong>
**【pygame开发实战开发30例 完整源码】**
- 
**【pygame游戏开发专栏，获取完整源码+教程】**
- **<strong>**</strong>- **<strong>**</strong>- **<strong>**</strong>- **<strong>**</strong>- **<strong>** </strong>- **<strong>**</strong>
#### CSDN官方学习推荐 ↓ ↓ ↓
- **CSDN出的Python全栈知识图谱，太强了，推荐给大家！**
<img alt="" height="625" src="https://img-blog.csdnimg.cn/20210607120133619.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="351">
