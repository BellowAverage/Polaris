
--- 
title:  [ 系统安全篇 ] window 命令禁用用户及解禁方法 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - <ul><li>- - - - - - 


## 一、注意需要用管理员身份进行

>  
 管理员身份才有权限，否则会报错 


<img src="https://img-blog.csdnimg.cn/847494474b69452ea4ada0bf9705754f.png" alt="在这里插入图片描述">

## 二、禁用及解禁用户

### 1、查看用户

```
net user

```

<img src="https://img-blog.csdnimg.cn/9c3324ea4b9b4b9caabdcb962e58926c.png" alt="在这里插入图片描述">

### 2、禁用用户

```
net user 用户名 /active:no

```

<img src="https://img-blog.csdnimg.cn/11ff308406834d5f9cb524bcaec5ec01.png" alt="在这里插入图片描述">

### 3、查看用户状态

```
net user 用户名

```

>  
 发现用户被禁用了 


<img src="https://img-blog.csdnimg.cn/e0d26c765ffc4818bf1320188978b1a3.png" alt="在这里插入图片描述">

### 4、解禁用户

```
net user 用户名 /active:yes

```

<img src="https://img-blog.csdnimg.cn/e4c8285a77844e1099034376ca663913.png" alt="在这里插入图片描述">

### 5、查看用户状态

```
net user 用户名

```

>  
 发现用户解除禁用了 


<img src="https://img-blog.csdnimg.cn/eb42914f7d8e4100a7dc1ebadd5f3814.png" alt="在这里插入图片描述">

## 三、管理员被禁用解禁方式

### 1、先禁用管理员账户

>  
 我们用命令行吧管理员用户禁用 


```
net user 用户名 /active:no

```

<img src="https://img-blog.csdnimg.cn/6440431402fe449e93b537207923f1c8.png" alt="在这里插入图片描述">

>  
 然后重启一下，采用管理员账号密码登录 


<img src="https://img-blog.csdnimg.cn/95217592e1cd4e23ab64a5ba5ad90004.png" alt="在这里插入图片描述">

>  
 点击登录按钮后报错 


<img src="https://img-blog.csdnimg.cn/9dced3589cac4f57ba564fe495557643.png" alt="在这里插入图片描述">

### 2、解禁管理员账户

>  
 首先我们按住shift重启电脑，悬着疑难杂症 


<img src="https://img-blog.csdnimg.cn/8a8e36fc53a24bedbbb8ce0db93f16e6.png" alt="在这里插入图片描述">

>  
 选择高级选项 


<img src="https://img-blog.csdnimg.cn/39bc85d506984809b2e30e608e0de2c3.png" alt="在这里插入图片描述">

>  
 选择启动设置 


<img src="https://img-blog.csdnimg.cn/591064835ba14b248f23ed577a4936a5.png" alt="在这里插入图片描述">

>  
 重启 


<img src="https://img-blog.csdnimg.cn/8e24b009e82e436c96155d693828370d.png" alt="在这里插入图片描述">

>  
 启动设置，键入F4进入安全模式 


<img src="https://img-blog.csdnimg.cn/d536452110f549f98408cbeec734bae1.png" alt="在这里插入图片描述">

>  
 选中其中的安全模式，在安全模式中，管理员用户是默认开启的 


<img src="https://img-blog.csdnimg.cn/5607b6ba6de6494590be806745e87441.png" alt="在这里插入图片描述">

>  
 等了一会儿之后进入了安全模式 


<img src="https://img-blog.csdnimg.cn/1b7488c9fdbf45feae792fd669668866.png" alt="在这里插入图片描述">

>  
 以管理员身份打开cmd 执行命令 


```
net user 用户名 /active:yes

```

<img src="https://img-blog.csdnimg.cn/671678ab703148bc969bdeea0476247c.png" alt="在这里插入图片描述">

>  
 成功解除禁用 


<img src="https://img-blog.csdnimg.cn/7814fabc1ef64031ab0902367dd88174.png" alt="在这里插入图片描述">

>  
 重启退出安全模式 使用admin账号进行登录，可以正常登录 


<img src="https://img-blog.csdnimg.cn/7d5fe34448bb4dbe8ca9a672e307b0e3.png" alt="在这里插入图片描述">
