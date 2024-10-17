
--- 
title:  打造全自动漏洞赏金扫描工具_nuclei扫描器联动xray 
tags: []
categories: [] 

---
### **0x01 说明**

本次用到的平台是：,该平台收集国外各大漏洞赏金平台，目前拥有资产规模大概在1600 0000~1800 0000，很可怕的数量 ，并且每小时都在增加或减少，对接非常多的第三方自建赏金平台，这比我们自己去收集某个平台会来的多，挖到的概率也更大。

<img src="https://img-blog.csdnimg.cn/img_convert/518671d6e7da82b08fb56844d399e76a.png" alt="">

### **0x02 自动化方案流程**
1. 使用脚本去获取projectdiscovery平台的所有资产，资产侦察与收集就交给projectdiscovery了1. 把下载的资产对比上次Master domain数据，判断当前是否有新增资产出现，如果没有就结束 ，就等待下一次循环1. 如果有，就把新增的资产提取出来，创建临时文件，并把新资产加入到Masterdomain1. 把新增资产使用naabu 进行端口扫描，把开放的端口使用httpx来验证，提取http存活资产1. 把http存活资产送往nuclei进行漏洞扫描，同时也送往Xray，默认使用Xray的基础爬虫功能扫描常见漏洞1. Xray的扫描结果保存成xray-new-$(date +%F-%T).html，也可以同时添加webhook模式推送1. nuclei漏洞扫描结果用notify实时推送、 nuclei与xray都扫描结束后 ，等待下一次循环，这一切都是自动去执行
<img src="https://img-blog.csdnimg.cn/img_convert/5e94b5f697bbebef5ab77bce90297097.png" alt="">

### 0x03 准备工作

先安装这些工具，并设置好软链接，能全局使用，这些工具安装很简单，不再阐述，github也有 安装教程
- Centos7+ 64 位 配置 4H 4G起 【服务器一台】- chaospy【资产侦查、资产下载】 - unzip 【解压】- anew 【过滤重复】 https://github.com/tomnomnom/anew- naabu【端口扫描】 https://github.com/projectdiscovery/naabu- httpx 【存活检测】 https://github.com/projectdiscovery/httpx- nuclei 【漏洞扫描】 https://nuclei.projectdiscovery.io/- Xray 【漏洞扫描】 https://download.xray.cool/- python 【微信通知】- notify 【漏洞通知】 notify比较成熟的推送方案
服务器推荐vultr，可以用我的推荐链接：

#### 0x04 关于notify通知相关配置

notify安装与配置：

配置文件(没有就创建这个文件)：/root/.config/notify/provider-config.yaml

修改通知配置 即可，比如我使用的通知是电报 和 邮件(配置任意一个即可)

<img src="https://img-blog.csdnimg.cn/img_convert/880bf015f74922b6a7ca022d28bc4579.png" alt="">

测试效果

subfinder -d hackerone.com | notify -provider telegram

我这是设置是电报通知，执行结束后，如果能收到结果，那通知这块就没问题，可以下一步了

<img src="https://img-blog.csdnimg.cn/img_convert/472af2b99d755dc28f8d1f3b8efbe00f.png" alt="">

### 0x05 部署过程

请确保上面提到的工具都已安装好，现在我们来构造一个sh脚本文件，这个脚本就把上面说的流 程都做了一遍

命名为: wadong.sh ， 添加执行权限： chmod +x wadong.sh

wadong.sh 脚本主要 完成 资产侦察资产收集、端口扫描，去重检测，存活探测，漏洞扫描，结果通知的功能

脚本：

#!/bin/bash

# 使用chaospy，只下载有赏金资产数据

#python3 chaospy.py --download-hackerone

#python3 chaospy.py --download-rewards #下载所有赏金资产

#./chaospy.py --download-bugcrowd 下载 BugCrowd 资产

#./chaospy.py --download-hackerone 下载 Hackerone 资产

#./chaospy.py --download-intigriti 下载 Intigriti 资产

#./chaospy.py --download-external 下载自托管资产

#./chaospy.py --download-swags 下载程序 Swags 资产

#./chaospy.py --download-rewards 下载有奖励的资产

#./chaospy.py --download-norewards 下载没有奖励的资产

#对下载的进行解压，使用awk把结果与上次的做对比，检测是否有新增

if ls | grep “.zip” &amp;&gt; /dev/null; then

unzip ‘*.zip’ &amp;&gt; /dev/null

cat *.txt &gt;&gt; newdomains.md

rm -f *.txt

awk ‘NR==FNR{lines[$0];next} !($0 in lines)’ alltargets.txtls newdomains.md &gt;&gt; domains.txtls

rm -f newdomains.md

################################################################################## 发送新增资产手机通知

echo “资产侦察结束 $(date +%F-%T)” | notify -silent -provider telegram

echo “找到新域 $(wc -l &lt; domains.txtls) 个” | notify -silent -provider telegram

################################################################################## 更新nuclei漏洞扫描模板

nuclei -silent -update

nuclei -silent -ut

rm -f *.zip

else

echo “没有找到新程序” | notify -silent -provider telegram

fi

if [ -s domains.txtls ];then

echo “开始使用 naabu 对新增资产端口扫描” | notify -silent -provider telegram

fine_line=$(cat domains.txtls | wc -l )

num=1

K=10000

j=true

F=0

while $j

do

echo $fine_line

if [ $num -lt $fine_line ];then

m= 
     
      
       
       
         ( 
        
       
         ( 
        
       
      
        (( 
       
      
    ((num+$K))

sed -n '‘ 
     
      
       
       
         n 
        
       
         u 
        
        
        
          m 
         
        
          ′ 
         
        
        
        
          , 
         
        
          ′ 
         
        
       
      
        num',' 
       
      
    num′,′m’p’ domains.txtls &gt;&gt; domaint.txtls

((num=num+$m))

naabu -stats -l domaint.txtls -p 80,443,8080,2053,2087,2096,8443,2083,2086,2095,8880,2052,2082,3443,8791,8887,8888,444,9443,2443,10000,10001,8082,8444,20000,8081,8445,8446,8447 -silent -o open-domain.txtls &amp;&gt; /dev/null | echo “端口扫描”

echo “端口扫描结束，开始使用httpx探测存活” | notify -silent -provider telegram

httpx -silent -stats -l open-domain.txtls -fl 0 -mc 200,302,403,404,204,303,400,401 -o newurls.txtls &amp;&gt; /dev/null

echo “httpx共找到存活资产 $(wc -l &lt; newurls.txtls) 个” | notify -silent -provider telegram

cat newurls.txtls &gt;new-active-$(date +%F-%T).txt #保存新增资产记录

cat domaint.txtls &gt;&gt; alltargets.txtls

echo “已将存活资产存在加入到历史缓存 $(date +%F-%T)” | notify -silent -provider telegram

echo “开始使用 nuclei 对新增资产进行漏洞扫描” | notify -silent -provider telegram

cat newurls.txtls | nuclei -rl 300 -bs 35 -c 30 -mhe 10 -ni -o res-all-vulnerability-results.txt -stats -silent -severity critical,medium,high,low | notify -silent -provider telegram

echo “nuclei 漏洞扫描结束” | notify -silent -provider telegram

#使用xray扫描，记得配好webhook，不配就删掉这项，保存成文件也可以

#echo “开始使用 xray 对新增资产进行漏洞扫描” | notify -silent -provider telegram

#xray_linux_amd64 webscan --url-file newurls.txtls --webhook-output http://www.qq.com/webhook --html-output xray-new-$(date +%F-%T).html

#echo “xray 漏洞扫描结束，xray漏洞报告请上服务器查看” | notify -silent -provider telegram

rm -f open-domain.txtls

rm -f domaint.txtls

rm -f newurls.txtls

else

echo “ssss”

j = false

sed -n '‘ 
     
      
       
       
         n 
        
       
         u 
        
        
        
          m 
         
        
          ′ 
         
        
        
        
          , 
         
        
          ′ 
         
        
       
      
        num',' 
       
      
    num′,′find_line’p’ domains.txtls domaint.txtls

naabu -stats -l domaint.txtls -p 80,443,8080,2053,2087,2096,8443,2083,2086,2095,8880,2052,2082,3443,8791,8887,8888,444,9443,2443,10000,10001,8082,8444,20000,8081,8445,8446,8447 -silent -o open-domain.txtls &amp;&gt; /dev/null | echo “端口扫描”

echo “端口扫描结束，开始使用httpx探测存活” | notify -silent -provider telegram

httpx -silent -stats -l open-domain.txtls -fl 0 -mc 200,302,403,404,204,303,400,401 -o newurls.txtls &amp;&gt; /dev/null

echo “httpx共找到存活资产 $(wc -l &lt; newurls.txtls) 个” | notify -silent -provider telegram

cat newurls.txtls &gt;new-active-$(date +%F-%T).txt #保存新增资产记录

cat domaint.txtls &gt;&gt; alltargets.txtls

echo “已将存活资产存在加入到历史缓存 $(date +%F-%T)” | notify -silent -provider telegram

echo “开始使用 nuclei 对新增资产进行漏洞扫描” | notify -silent -provider telegram

cat newurls.txtls | nuclei -rl 300 -bs 35 -c 30 -mhe 10 -ni -o res-all-vulnerability-results.txt -stats -silent -severity critical,medium,high,low | notify -silent -provider telegram

echo “nuclei 漏洞扫描结束” | notify -silent -provider telegram

#使用xray扫描，记得配好webhook，不配就删掉这项，保存成文件也可以

#echo “开始使用 xray 对新增资产进行漏洞扫描” | notify -silent -provider telegram

#xray_linux_amd64 webscan --url-file newurls.txtls --webhook-output http://www.qq.com/webhook --html-output xray-new-$(date +%F-%T).html

#echo “xray 漏洞扫描结束，xray漏洞报告请上服务器查看” | notify -silent -provider telegram

rm -f open-domain.txtls

rm -f domaint.txtls

rm -f newurls.txtls

fi

done

rm -f domains.txtls

else

################################################################################## Send result to notify if no new domains found

echo “没有新域 $(date +%F-%T)” | notify -silent -provider telegram

fi

再构建一个first.sh文件，这个脚本只执行一次就行，后续也就用不到了， 主要用于第一次产生历 史缓存域，标记为旧资产

添加执行权限： chmod +x first.sh

#!/bin/bash # 使用chaospy，只下载有赏金资产数据 ./chaospy.py --download-new ./chaospy.py --download-rewards #对下载的进行解压， if ls | grep “.zip” &amp;&gt; /dev/null; then unzip ‘*.zip’ &amp;&gt; /dev/null rm -f alltargets.txtls cat *.txt &gt;&gt; alltargets.txtls rm -f *.txt rm -f *.zip echo “找到域 $(wc -l &lt; alltargets.txtls) 个，已保存成缓存文件alltargets.txt” fi

### 0x06 开始赏金自动化

在确保以上工具都安装好的情况下

1、执行 first.sh 脚本，让本地产生足够多的缓存域名，标记为旧资产

./first.sh

2、循环执行bbautomation.sh脚本，sleep 3600秒 就是每小时一次,也就是脚本

xunhuan.sh:

#!/bin/bash

while true; do ./wadong.sh;sleep 3600; done

3.chaospy脚本已做了大概修改，优化延迟扫描时间和报错

#!/usr/bin/python3

import requests

import time,os,argparse

#Colors

Black = “\033[30m”

Red = “\033[31m”

Green = “\033[32m”

Yellow = “\033[33m”

Blue = “\033[34m”

Magenta = “\033[35m”

Cyan = “\033[36m”

LightGray = “\033[37m”

DarkGray = “\033[90m”

LightRed = “\033[91m”

LightGreen = “\033[92m”

LightYellow = “\033[93m”

LightBlue = “\033[94m”

LightMagenta = “\033[95m”

LightCyan = “\033[96m”

White = “\033[97m”

Default = ‘\033[0m’

banner= “”"

```
      %s             \_\_\_\_\_\_\_\_                     \_\_\_\_

                  / \_\_\_\_/ /\_  \_\_\_\_ \_\_\_\_\_  \_\_\_\_\_/ \_\_ \\\_\_  \_\_

                 / /   / \_\_ \\/ \_\_ \`/ \_\_ \\/ \_\_\_/ /\_/ / / / /

                / /\_\_\_/ / / / /\_/ / /\_/ (\_\_  ) \_\_\_\_/ /\_/ /

                \\\_\_\_\_/\_/ /\_/\\\_\_,\_/\\\_\_\_\_/\_\_\_\_/\_/    \\\_\_, /

                                                  /\_\_\_\_/

      %s  Small Tool written based on chaos from projectdiscovery.io

      %s          https://chaos.projectdiscovery.io/

      %s    \*Author -&gt; Moaaz (https://twitter.com/photonbo1t)\*

```

%s \n “”"%(LightGreen,Yellow,DarkGray,DarkGray,Default)

parser = argparse.ArgumentParser(description=‘ChaosPY Tool’)

parser.add_argument(‘-list’,dest=‘list’,help=‘List all programs’,action=‘store_true’)

parser.add_argument(‘–list-bugcrowd’,dest=‘list_bugcrowd’,help=‘List BugCrowd programs’,action=‘store_true’)

parser.add_argument(‘–list-hackerone’,dest=‘list_hackerone’,help=‘List Hackerone programs’,action=‘store_true’)

parser.add_argument(‘–list-intigriti’,dest=‘list_intigriti’,help=‘List Intigriti programs’,action=‘store_true’)

parser.add_argument(‘–list-external’,dest=‘list_external’,help=‘List Self Hosted programs’,action=‘store_true’)

parser.add_argument(‘–list-swags’,dest=‘list_swags’,help=‘List programs Swags Offers’,action=‘store_true’)

parser.add_argument(‘–list-rewards’,dest=‘list_rewards’,help=‘List programs with rewards’,action=‘store_true’)

parser.add_argument(‘–list-norewards’,dest=‘list_norewards’,help=‘List programs with no rewards’,action=‘store_true’)

parser.add_argument(‘–list-new’,dest=‘list_new’,help=‘List new programs’,action=‘store_true’)

parser.add_argument(‘–list-updated’,dest=‘list_updated’,help=‘List updated programs’,action=‘store_true’)

parser.add_argument(‘-download’,dest=‘download’,help=‘Download Specific Program’)

parser.add_argument(‘–download-all’,dest=‘download_all’,help=‘Download all programs’,action=‘store_true’)

parser.add_argument(‘–download-bugcrowd’,dest=‘download_bugcrowd’,help=‘Download BugCrowd programs’,action=‘store_true’)

parser.add_argument(‘–download-hackerone’,dest=‘download_hackerone’,help=‘Download Hackerone programs’,action=‘store_true’)

parser.add_argument(‘–download-intigriti’,dest=‘download_intigriti’,help=‘Download intigriti programs’,action=‘store_true’)

parser.add_argument(‘–download-external’,dest=‘download_external’,help=‘Download external programs’,action=‘store_true’)

parser.add_argument(‘–download-swags’,dest=‘download_swags’,help=‘Download programs Swags Offers’,action=‘store_true’)

parser.add_argument(‘–download-rewards’,dest=‘download_rewards’,help=‘Download programs with rewards’,action=‘store_true’)

parser.add_argument(‘–download-norewards’,dest=‘download_norewards’,help=‘Download programs with no rewards’,action=‘store_true’)

parser.add_argument(‘–download-new’,dest=‘download_new’,help=‘Download new programs’,action=‘store_true’)

parser.add_argument(‘–download-updated’,dest=‘download_updated’,help=‘Download updated programs’,action=‘store_true’)

args = parser.parse_args()

os.system(‘clear’)

ls = args.list

list_bugcrowd = args.list_bugcrowd

list_hackerone=args.list_hackerone

list_intigriti=args.list_intigriti

list_external=args.list_external

list_swags=args.list_swags

list_rewards=args.list_rewards

list_norewards=args.list_norewards

list_new=args.list_new

list_updated=args.list_updated

download = args.download

download_all= args.download_all

download_bugcrowd = args.download_bugcrowd

download_hackerone=args.download_hackerone

download_intigriti=args.download_intigriti

download_external=args.download_external

download_swags=args.download_swags

download_rewards=args.download_rewards

download_norewards=args.download_norewards

download_new=args.download_new

download_updated=args.download_updated

print (banner)

def getdata():

```
url = "https://chaos-data.projectdiscovery.io/index.json"

insuer = True

while insuer:

    try:

        source= requests.get(url)

        print("爬取完毕!")

        insuer = False

    except:

        print("存在延迟!")

        time.sleep(10)

return source.json()

```

def info():

```
new = 0

hackerone = 0

bugcrowd= 0

intigriti = 0

external = 0

changed = 0

subdomains = 0

rewards= 0

norewards= 0

swags= 0

for item in getdata():

    if item\['is\_new'\] is True:

        new += 1

    if item\['platform'\] == "hackerone":

        hackerone +=1

    if item\['platform'\] == "bugcrowd":

        bugcrowd += 1

    if item\['platform'\] == "intigriti":

        intigriti += 1

    else:

        external += 1

    if item\['change'\] != 0:

        changed +=1

    subdomains = subdomains +item\['count'\]

    if item\['bounty'\] is True:

        rewards += 1

    else:

        norewards += 1

    if 'swag' in item:

        swags +=1

print(White+"\[!\] Programs Last Updated {}".format(item\['last\_updated'\]\[:10\]))

print(LightGreen+"\[!\] {} Subdomains.".format(subdomains))

print(Green+"\[!\] {} Programs.".format(len(getdata()))+Default)

print(LightCyan+"\[!\] {} Programs changed.".format(changed)+Default)

print(Blue+"\[!\] {} New programs.".format(new)+Default)

print(LightGray+"\[!\] {} HackerOne programs.".format(hackerone)+Default)

print(Magenta+"\[!\] {} Intigriti programs.".format(intigriti)+Default)

print(Yellow+"\[!\] {} BugCrowd programs.".format(bugcrowd)+Default)

print(LightGreen+"\[!\] {} Self hosted programs.".format(external)+Default)

print(Cyan+"\[!\] {} Programs With Rewards.".format(rewards)+Default)

print(Yellow+"\[!\] {} Programs Offers Swags.".format(swags)+Default)

print(LightRed+"\[!\] {} No Rewards programs.".format(norewards)+Default)

```

def down():

```
print(download)

for item in getdata():

    if item\['name'\] == download:

        print(LightGreen+"\[!\] Program Found."+Default)

        print(Cyan+"\[!\] Downloading",download, "..."+Default)

        url = item\['URL'\]

        resp = requests.get(url)

        zname= download+".zip"

        zfile = open(zname, 'wb')

        zfile.write(resp.content)

        zfile.close()

        print(LightGreen+"\[!\] {} File successfully downloaded.".format(zname)+Default)

```

def list_all():

```
print(White+"\[!\] Listing all Programs. \\n"+Default)

for item in getdata():

    print (Blue+item\['name'\]+Default)

```

def bugcrowd():

```
print(Yellow+"\[!\] Listing Bugcrowd Programs."+Default)

for item in getdata():

    if item\['platform'\] == "bugcrowd":

        print (Yellow+item\['name'\]+Default)

```

def hackerone():

```
print(White+"\[!\] Listing HackerOne Programs."+Default)

for item in getdata():

    if item\['platform'\] == "hackerone":

        print (White+item\['name'\]+Default)

```

def intigriti():

```
print(Magenta+"\[!\] Listing intigriti Programs."+Default)

for item in getdata():

    if item\['platform'\] == "hackerone":

        print (Magenta+item\['name'\]+Default)

```

def external():

```
print(Cyan+"\[!\] Listing External Programs."+Default)

for item in getdata():

    if item\['platform'\] == "":

        print (Cyan+item\['name'\]+Default)

```

def swags():

```
print(LightGreen+"\[!\] Listing Swag Programs."+Default)

for item in getdata():

    if 'swag' in item:

        print (LightGreen+item\['name'\]+Default)

```

def rewards():

```
print(Cyan+"\[!\] Listing Rewards Programs."+Default)

for item in getdata():

    if item\['bounty'\] == True:

        print (Cyan+item\['name'\]+Default)

```

def norewards():

```
print(Red+"\[!\] Listing NORewards Programs."+Default)

for item in getdata():

    if item\['bounty'\] == False:

        print (Red+item\['name'\]+Default)

```

def new():

```
print(LightGreen+"\[!\] Listing New Programs."+Default)

for item in getdata():

    if item\['is\_new'\] == True:

        print (LightGreen+item\['name'\]+Default)

```

def changed():

```
print(Cyan+"\[!\] Listing Updated Programs."+Default)

for item in getdata():

    if item\['change'\] != 0:

        print (Cyan+item\['name'\]+Default)

```

def all_down():

```
for item in getdata():

    print(Blue+"\[!\] Downloading {}                   ".format(item\['name'\]),end="\\r"+Default)

    resp = requests.get(item\['URL'\])

    zname= item\['name'\]+".zip"

    zfile = open(zname, 'wb')

    zfile.write(resp.content)

    zfile.close()

print(LightGreen+"\[!\] All Programs successfully downloaded."+Default)

```

def bc_down():

```
for item in getdata():

    if item\['platform'\] == "bugcrowd":

        print(Yellow+"\[!\] Downloading {}                   ".format(item\['name'\]),end="\\r"+Default)

        resp = requests.get(item\['URL'\])

        zname= item\['name'\]+".zip"

        zfile = open(zname, 'wb')

        zfile.write(resp.content)

        zfile.close()

print(LightGreen+"\[!\] All BugCrowd programs successfully downloaded."+Default)

```

def h1_down():

```
for item in getdata():

    if item\['platform'\] == "hackerone":

        print(White+"\[!\] Downloading {}                   ".format(item\['name'\]),end="\\r"+Default)

        resp = requests.get(item\['URL'\])

        zname= item\['name'\]+".zip"

        zfile = open(zname, 'wb')

        zfile.write(resp.content)

        zfile.close()

print(LightGreen+"\[!\] All HackerOne programs successfully downloaded."+Default)

```

def intigriti_down():

```
for item in getdata():

    if item\['platform'\] == "intigriti":

        print(Magenta+"\[!\] Downloading {}                   ".format(item\['name'\]),end="\\r"+Default)

        resp = requests.get(item\['URL'\])

        zname= item\['name'\]+".zip"

        zfile = open(zname, 'wb')

        zfile.write(resp.content)

        zfile.close()

print(LightGreen+"\[!\] All intigriti programs successfully downloaded."+Default)

```

def external_down():

```
for item in getdata():

    if item\['platform'\] == "":

        print(White+"\[!\] Downloading {}                   ".format(item\['name'\]),end="\\r"+Default)

        resp = requests.get(item\['URL'\])

        zname= item\['name'\]+".zip"

        zfile = open(zname, 'wb')

        zfile.write(resp.content)

        zfile.close()

print(LightGreen+"\[!\] All External programs successfully downloaded."+Default)

```

def new_down():

```
for item in getdata():

    if item\['is\_new'\] is True:

        print(Cyan+"\[!\] Downloading {}                   ".format(item\['name'\]),end="\\r"+Default)

        insuer = True

        while insuer:

            try:

                resp = requests.get(item\['URL'\])

                print("爬取完毕")

                insuer = False

            except:

                print("存在延时！")

                time.sleep(5)

        zname= item\['name'\]+".zip"

        zfile = open(zname, 'wb')

        zfile.write(resp.content)

        zfile.close()

print(LightGreen+"\[!\] All New programs successfully downloaded."+Default)

```

def updated_down():

```
for item in getdata():

    if item\['change'\] != 0:

        print(Blue+"\[!\] Downloading {}                   ".format(item\['name'\]),end="\\r"+Default)

        resp = requests.get(item\['URL'\])

        zname= item\['name'\]+".zip"

        zfile = open(zname, 'wb')

        zfile.write(resp.content)

        zfile.close()

print(LightGreen+"\[!\] All Updated programs successfully downloaded."+Default)

```

def swags_down():

```
for item in getdata():

    if 'swag' in item:

        print(LightYellow+"\[!\] Downloading {}                   ".format(item\['name'\]),end="\\r"+Default)

        resp = requests.get(item\['URL'\])

        zname= item\['name'\]+".zip"

        zfile = open(zname, 'wb')

        zfile.write(resp.content)

        zfile.close()

print(LightGreen+"\[!\] All Swags programs successfully downloaded."+Default)

```

def rewards_down():

```
for item in getdata():

    if item\['bounty'\] is True:

        print(Cyan+"\[!\] Downloading {}                   ".format(item\['name'\]),end="\\r"+Default)

        insuer = True

        while insuer:

            try:

                resp = requests.get(item\['URL'\])

                print("爬取完毕")

                insuer = False

            except:

                print("存在延时！")

                time.sleep(5)

        zname= item\['name'\]+".zip"

        zfile = open(zname, 'wb')

        zfile.write(resp.content)

        zfile.close()

print(LightGreen+"\[!\] All Bounty programs successfully downloaded."+Default)

```

def norewards_down():

```
for item in getdata():

    if item\['bounty'\] is False:

        print(LightRed+"\[!\] Downloading {}                   ".format(item\['name'\]),end="\\r"+Default)

        resp = requests.get(item\['URL'\])

        zname= item\['name'\]+".zip"

        zfile = open(zname, 'wb')

        zfile.write(resp.content)

        zfile.close()

print(LightGreen+"\[!\] All Norewards programs successfully downloaded."+Default)

```

def main():

```
info()

if download is not None:

    down()

if download\_all :

    all\_down()

if ls :

    list\_all()

if list\_bugcrowd:

    bugcrowd()

if list\_hackerone:

    hackerone()

if list\_external:

    external()

if list\_swags:

    swags()

if list\_rewards:

    rewards()

if list\_norewards:

    norewards()

if list\_new:

    new()

if list\_updated:

    changed()

if download\_bugcrowd:

    bc\_down()

if download\_hackerone:

    h1\_down()

if download\_intigriti:

    intigriti\_down()

if download\_external:

    external\_down()

if download\_swags:

    swags\_down()

if download\_rewards:

    rewards\_down()

if download\_norewards:

    norewards\_down()

if download\_new:

    new\_down()

if download\_updated:

    updated\_down()

```

if __name__ == ‘__main__’:

```
main()

```

### 0x07 最后

建议在 Digital Ocean 或 vultr 等 VPS 系统上运行这些程序，启一个后台线程即可，建议使用tmux的后台功能

这样扫描到重复漏洞会非常少的，也会更加容易获取赏金，将更多的关注新资产漏洞

资产侦察 资产收集、端口扫描，去重检测，存活探测，漏洞扫描，全自动化，结果通知，全部自动化了，即使睡觉也在挖洞

<img src="https://img-blog.csdnimg.cn/img_convert/d6a37b6734718cff03881243df7455e0.png" alt="">

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
