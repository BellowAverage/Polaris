
--- 
title:  [ 应急响应基础篇 ] Windows系统隐藏账户详解（Windows留后门账号） 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - <ul><li>- - - <ul><li>- - - - - - - - - - - - - 


## 一、Windows系统添加隐藏用户介绍

>  
 系统隐藏账户是一种最为简单有效的权限维持方式，其做法就是让攻击者创建一个新的具有管理员权限的隐藏账户，因为是隐藏账户，所以防守方是无法通过控制面板或命令行看到这个账户的。 


## 二、Windows系统添加隐藏用户步骤

### 1、环境介绍

>  
 前提条件: 假设在攻击的过程中通过利用各种getshell，已经拿到目标服务器administrator权限 环境：windows Server2012 IP：192.168.223.182 


### 2、创建一个隐藏账号

```
net user powershell$ w123456! /add 

```

>  
 添加powershell$隐藏用户 


```
net localgroup administrators powershell$ /add 

```

>  
 将powershell$用户添加进管理员组中 


<img src="https://img-blog.csdnimg.cn/06d7b8efef0544cdac50950065f32c0c.png" alt="在这里插入图片描述">

>  
 创建完成之后，输入net user 查看账户，发现我们创建的隐藏用户隐藏成功 


```
net user 

```

<img src="https://img-blog.csdnimg.cn/2f6f9da9a6cf458ba1abfac911842a1b.png" alt="在这里插入图片描述">

### 3、隐藏不彻底

>  
 虽然用net user 看不到，但是还有其他方式可以看到 


#### 1.管理账户查看

>  
 通过控制面板–&gt;用户账户–&gt;管理账户查看 


<img src="https://img-blog.csdnimg.cn/e2138c18f2fa4ec4b66cc075b475cb34.png" alt="在这里插入图片描述">

#### 2.管理工具查看

>  
 通过管理工具–&gt;计算机管理–&gt;本地用户和组–&gt;用户也可以看到 


<img src="https://img-blog.csdnimg.cn/1845510f85804395b987b68fa2678230.png" alt="在这里插入图片描述">

#### 3.注销登录页面查看

>  
 这里也可以看到创建的隐藏账户 


<img src="https://img-blog.csdnimg.cn/033cac26ff484e749ce8f699b6bc3d6e.png" alt="在这里插入图片描述">

### 4、修改注册表

>  
 为了更好的隐藏新建的账户，还需要进行修改注册表文件操作。 


#### 1.首先打开注册表编辑器

```
regedit

```

<img src="https://img-blog.csdnimg.cn/64e5ac5bf23448b2bea271331d3c7f4a.png" alt="在这里插入图片描述">

#### 2.确保可以看到SAM路径下的文件

>  
 找到HKEY_LOCAL_MACHINE\SAM\SAM，点击右键，选择“权限”将Administrator用户的权限，设置成“完全控制”， 


<img src="https://img-blog.csdnimg.cn/0d1e536685f84030be05f6143a30e8ae.png" alt="在这里插入图片描述">

>  
 重新打开注册表，确保可以看到SAM路径下的文件 


<img src="https://img-blog.csdnimg.cn/79b960f44e344f86ae8ec33b95a18dd0.png" alt="在这里插入图片描述">

#### 3.找到用户对应的表

>  
 其次前往SAM/Domains/Account/Users/Names处，选择Administrator用户，在右侧的键值处可以找到对应的值如0x1f4，然后从左侧的Users目录下可以找到对应的文件。 


<img src="https://img-blog.csdnimg.cn/5f7fb24716ac4f869077aa554c854f40.png" alt="在这里插入图片描述">

>  
 其次前往SAM/Domains/Account/Users/Names处，选择Administrator用户，在右侧的键值处可以找到对应的值如0x3ec，然后从左侧的Users目录下可以找到对应的文件。 


<img src="https://img-blog.csdnimg.cn/74c0b71963c84b0ab49a6f0c7c0755f0.png" alt="在这里插入图片描述">

#### 4.替换F值

>  
 <p>然后从对应的000001F4文件中将键值对F的值复制出来。然后同理找到隐藏账户powershell 
      
       
        
        
          所对应的文件，并将从 
         
        
          A 
         
        
          d 
         
        
          m 
         
        
          i 
         
        
          n 
         
        
          i 
         
        
          s 
         
        
          t 
         
        
          r 
         
        
          a 
         
        
          t 
         
        
          o 
         
        
          r 
         
        
          文件中复制出来的 
         
        
          F 
         
        
          值粘贴进 
         
        
          p 
         
        
          o 
         
        
          w 
         
        
          e 
         
        
          r 
         
        
          s 
         
        
          h 
         
        
          e 
         
        
          l 
         
        
          l 
         
        
       
         所对应的文件，并将从Administrator文件中复制出来的F值粘贴进 powershell 
        
       
     所对应的文件，并将从Administrator文件中复制出来的F值粘贴进powershell文件中。</p> 


<img src="https://img-blog.csdnimg.cn/efff400cb2314875bfca39a539cc1fc2.png" alt="在这里插入图片描述">

>  
 把之前复制的f值粘贴到0x3ec的f值中 


<img src="https://img-blog.csdnimg.cn/ef520bda508c419291f8fa3e188277f7.png" alt="在这里插入图片描述">

#### 5.导出需隐藏用户的表

>  
 <p>最后将powershell$ 和000003EC从注册表中右键导出，并删除powershell 
      
       
        
        
          用户，然后将刚刚导出的两个文件重新导入进注册表中即可实现 
         
        
          p 
         
        
          o 
         
        
          w 
         
        
          e 
         
        
          r 
         
        
          s 
         
        
          h 
         
        
          e 
         
        
          l 
         
        
          l 
         
        
       
         用户，然后将刚刚导出的两个文件重新导入进注册表中即可实现powershell 
        
       
     用户，然后将刚刚导出的两个文件重新导入进注册表中即可实现powershell用户的隐藏。 导出powershell$表</p> 


<img src="https://img-blog.csdnimg.cn/d0dd8bcd77e9400ea964355e54309834.png" alt="在这里插入图片描述">

>  
 导出000003EC表 


<img src="https://img-blog.csdnimg.cn/4129eb5e3a93420297236af4ead038c9.png" alt="在这里插入图片描述">

>  
 导出来的表如下 


<img src="https://img-blog.csdnimg.cn/4b363b48885f432c999ea09dc5d868b5.png" alt="在这里插入图片描述">

#### 6.删除需要隐藏的用户

```
net user powershell$ /del 

```

<img src="https://img-blog.csdnimg.cn/e6944139a1d5474181b508b0b1574adc.png" alt="在这里插入图片描述">

>  
 此时注册表 


<img src="https://img-blog.csdnimg.cn/149830fe97084a0baf800cda19a57373.png" alt="在这里插入图片描述">

#### 7.导入需隐藏用户的表

>  
 导入000003EC表 


<img src="https://img-blog.csdnimg.cn/d61c39ecc03542f6b2b455e568c8115c.png" alt="在这里插入图片描述">

>  
 导入powershell$表 


<img src="https://img-blog.csdnimg.cn/295bc0e6833940dd8a1106ec16f5cc5d.png" alt="在这里插入图片描述">

>  
 此时注册表 


<img src="https://img-blog.csdnimg.cn/856499e9fbb64f88bf2f96309d8d92e2.png" alt="在这里插入图片描述">

#### 8.隐藏状态

>  
 管理账户下看不到隐藏用户 


<img src="https://img-blog.csdnimg.cn/0d1eeafb747348d6b52934660b027821.png" alt="在这里插入图片描述">

>  
 计算机管理用户下看不到隐藏用户 


<img src="https://img-blog.csdnimg.cn/6ea74efeccee43909c4986238c3d9541.png" alt="在这里插入图片描述">

>  
 注销登录页面查看任然可以看到创建的隐藏账户 <img src="https://img-blog.csdnimg.cn/15a6c8bf021548ab8e20b20602e912ae.png" alt="在这里插入图片描述"> 


### 5、登陆界面隐藏账户

>  
 在注册表中进行设置，使用户不在登录界面显示。 终端中输入： regedit 回车打开注册表编辑器。 


```
regedit 

```

<img src="https://img-blog.csdnimg.cn/da2048bf6d2d49c892f6e85cd83007a5.png" alt="在这里插入图片描述">

>  
 依次定位到：进入注册表HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\ 右键新建项SpecialAccounts 


<img src="https://img-blog.csdnimg.cn/7d24dc4d636b415885e146be64a263ad.png" alt="在这里插入图片描述">

>  
 右键新建项UserList 


<img src="https://img-blog.csdnimg.cn/0a39779842174c878487cc10daa080cd.png" alt="在这里插入图片描述">

>  
 右键新建项DWORD32值 


<img src="https://img-blog.csdnimg.cn/bbc8f821e51b41b8bd0ece096b7d34c1.png" alt="在这里插入图片描述">

>  
 名称为需要隐藏的账户，值为0 值为0表示隐藏，值为1表示显示 


<img src="https://img-blog.csdnimg.cn/d8cc10fbde9d4eb1a767dd3c49ffda57.png" alt="在这里插入图片描述">

>  
 最终如下 


<img src="https://img-blog.csdnimg.cn/4d8f31bf5612449f879027427c0dcb97.png" alt="在这里插入图片描述">

### 6、用户被完全隐藏

>  
 登录界面也看不到了 


<img src="https://img-blog.csdnimg.cn/0bd9c8730bbd4fada0734f0350ea686c.png" alt="在这里插入图片描述">

### 7、用户正常登录

>  
 采用powershell$登录，成功登录 


<img src="https://img-blog.csdnimg.cn/99c8488cd3964eb8b488dc51880f898e.png" alt="在这里插入图片描述">

>  
 登陆进来用的是administrator的身份 


<img src="https://img-blog.csdnimg.cn/c2028dd5ef184b38ad03300cbc677809.png" alt="在这里插入图片描述">

## 三、应急响应发现隐藏账户

>  
 对比以下三张表数量及名称，发现powershell$隐藏用户 


### 1、注册表中用户

>  
 查看注册表中HKEY_LOCAL_MACHINE\SAM\SAM\Domains\Account\Users\Names 位置的用户名 


<img src="https://img-blog.csdnimg.cn/b1b4a4848ff341d18c4d10ac23c6e9a7.png" alt="在这里插入图片描述">

### 2、管理账户中用户

>  
 控制面板–&gt;用户账户–&gt;管理账户 


<img src="https://img-blog.csdnimg.cn/278063a0a7914cc29f32af0e374aeac4.png" alt="在这里插入图片描述">

### 3、管理工具中用户

>  
 管理工具–&gt;计算机管理–&gt;本地用户和组–&gt;用户 


<img src="https://img-blog.csdnimg.cn/11de629ad8a94cfa8b71b7d515b33dba.png" alt="在这里插入图片描述">
