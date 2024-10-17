
--- 
title:  [ 攻防演练演示篇 ] 利用谷歌 0day 漏洞上线靶机 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - <ul><li>- - - <ul><li>- - - - - - - 


## 一、前言

>  
 本次使用于搭建一个演示环境，用于演示，这里我利用了一个Google的0ady 需要注意的是： 


```
1.靶机环境win10、win7均可，sever不行
2.chrome客户端需64位（Google Chrome &lt; = 89.0.4389.128）
3.浏览器需要关闭沙箱模式--no-sandbox
4.攻击机需要有java和python环境
5.攻击机我这里利用的Cobaltsrike，当然想使用msf，大灰狼等等工具都是可以的

```

## 二、演示环境搭建

### 1、靶机安装低版本谷歌

>  
 低版本谷歌下载链接在文末给出 创建快捷方式到桌面，右键编辑快捷方式，在目标后面添加-no-sandbox参数 增加 -no-sandbox 参数的目的是关闭沙箱 


<img src="https://img-blog.csdnimg.cn/471f423d60b7458ab38e53c546a5d83a.png" alt="在这里插入图片描述">

### 2、攻击机安装CS神器

>  
 Cobaltsrike CS神器下载链接： 


```
https://download.csdn.net/download/qq_51577576/87379235

```

>  
 资源有可能会被下架，如果被下架了，自行下载 


## 三、红方操作

### 1、POC制作

#### 1.启动CS服务端

>  
 启动CS，以管理员身份进入teamserver.bat所在目录 打开运行框，启动cs 


```
./teamserver.bat 10.10.12.143 123456

```

<img src="https://img-blog.csdnimg.cn/37168129b3d3441995ad6debe47f6d92.png" alt="在这里插入图片描述">

#### 2.打开CS客户端

>  
 打开cs客户端 cobaltsrike 


<img src="https://img-blog.csdnimg.cn/9bc819fd69964c77a7f6acf47d7ec117.png" alt="在这里插入图片描述">

#### 3.客户端连接CS服务端

>  
 输入ip、端口和密码等信息 


<img src="https://img-blog.csdnimg.cn/98452d9eb2f0449bbc3e50ef0af8522d.png" alt="在这里插入图片描述">

#### 4.添加监听器

>  
 添加监听器 


<img src="https://img-blog.csdnimg.cn/04ea539414e54f6e8232df7082964a76.png" alt="在这里插入图片描述">

#### 5.生成payload

>  
 生成后门 攻击–&gt;生成后门–&gt;payload Generator 


<img src="https://img-blog.csdnimg.cn/1e373d1a71b64354a51133cc79f12533.png" alt="在这里插入图片描述">

>  
 选择我们前面创建的监听器，使用X64payload，点击Generate 


<img src="https://img-blog.csdnimg.cn/6cc7344c027841cb8ef2063b87fb32cf.png" alt="在这里插入图片描述">

>  
 选择生成路径，随便放哪里都行，我就放在了桌面，桌面就会多一个payload.c文件这个就是CS生成的后门文件 


#### 6.制作POC

>  
 1、打开payload.c文件，并将payload.c中的”\”全部替换为“,0”，如下 


<img src="https://img-blog.csdnimg.cn/af7c56f3ba4749b9b7138862efcfaf50.png" alt="在这里插入图片描述">

>  
 2、替换完成之后我们赋值所有的十六进制编码，并替换到POC.txt的shellcode参数中，如下就是替换完成的 POC.txt下载链接再文末给出 


<img src="https://img-blog.csdnimg.cn/c9f2b7f2fb1341819f83aa714b9e8754.png" alt="在这里插入图片描述">

>  
 3、将txt后缀改为html 


<img src="https://img-blog.csdnimg.cn/da997326baa34704a183244199c36e3c.png" alt="在这里插入图片描述">

### 2、准备恶意网页

>  
 进入POC.html目录启一个python服务，目的是把我们制作的POC.html公开，让靶机能够访问得到 启动网页命令 


```
python -m http.server 8080

```

<img src="https://img-blog.csdnimg.cn/06157dcdce464c53a2beef4d032de061.png" alt="在这里插入图片描述">

## 四、蓝方操作

>  
 访问（红方人员诱导蓝方人员点击） 


```
http://攻击机IP:8080/POC.html

```

<img src="https://img-blog.csdnimg.cn/581964be53d5446186957770d3ff8d2d.png" alt="在这里插入图片描述">

## 五、红方操作

### 1、蓝方人员上线

>  
 发现蓝方人员成功上线，我们截它桌面的图 


<img src="https://img-blog.csdnimg.cn/143b9bf1cda14267a7bb04dfab2a8d8b.png" alt="在这里插入图片描述">

### 2、截蓝方机器桌面的图

>  
 1、使用cs工具操作桌面截图 右键上线机器 --&gt; Explore --&gt; Screenshots 


<img src="https://img-blog.csdnimg.cn/9846b605906d49dbaac07f5c05777cb6.png" alt="在这里插入图片描述">

>  
 2、成功截取到图片 执行完上面那一步我们已经截到图了，我们打开工具栏的图片图标，查看截取到的图片 


<img src="https://img-blog.csdnimg.cn/66e590b543704bc1a03be2b72a90276c.png" alt="在这里插入图片描述">

## 六、相关资源

    
