
--- 
title:  jeecgboot安装部署教程 
tags: []
categories: [] 

---
## 一、需要环境

### 安装jdk1.8

### <img alt="" height="172" src="https://img-blog.csdnimg.cn/da184867847d4f58827332bd30d4d2d7.png" width="1200">

### 安装idea、maven

官方下载地址

相关配置参考：

### 安装MySql、navicat

mysql安装参考：

navicat安装包：链接： 提取码：0lnd 

### 安装redis

<img alt="" height="1186" src="https://img-blog.csdnimg.cn/d304e88cfd924f4796b065ff4846510e.png" width="1200">

### 安装node Js

下载链接： 

安装教程：

 <img alt="" height="221" src="https://img-blog.csdnimg.cn/da73541679bf4fee8ca2f0293637d2dc.png" width="487">

**在nodejs文件夹下新建文件夹`node_global`和`node_cache`，在`node_global`下新建`node_modules`文件夹。**

cmd下输入两行命令设置全局文件和缓存文件。

```
npm config set prefix "D:\Node.js\node_global"
npm config set cache "D:\Node.js\node_cache"
```

<img alt="" height="140" src="https://img-blog.csdnimg.cn/15f6d4c8c63442aebf2cb8ae20fddedb.png" width="1200">

创建系统环境变量NODE_PATH--&gt;D:\Node.js

path下添加环境变量--&gt;%NODE_PATH%和%NODE_PATH%\node_global

安装cnpm、yarn cnpm安装：npm install -g cnpm --registry=https://registry.npm.taobao.org yarn安装：npm install -g yarn --registry=https://registry.npm.taobao.org

报错：

<img alt="" height="131" src="https://img-blog.csdnimg.cn/c616fa33b6fe4350a8748d56a8b07bbe.png" width="1200"> 解决方法：

若还是无法解决，则以管理员身份运行cmd命令行即可。

使用npm安装yarn,cnpm,pnpm成功后，可在D:\Node.js\node_global\node_modules路径下找到：

<img alt="" height="416" src="https://img-blog.csdnimg.cn/06e4c2e221cb4123b713d66da765012f.png" width="612">

###  安装yarn

下载链接：

### <img alt="" height="449" src="https://img-blog.csdnimg.cn/a3d020d78d4a481589fac5b3164bbda3.png" width="1200"> 安装pnpm、serve

<img alt="" height="186" src="https://img-blog.csdnimg.cn/47f23a56e8ae4a73aba4845220a1d352.png" width="820">

<img alt="" height="127" src="https://img-blog.csdnimg.cn/18f36a0831a0468d9c0ef3a41cf5cc73.png" width="784">

##   二、拉取代码

```
后端：git clone https://gitee.com/jeecg/jeecg-boot.git
前端：git clone https://gitee.com/jeecg/jeecgboot-vue3.git
```

<img alt="" height="276" src="https://img-blog.csdnimg.cn/b1c105a8ffb947c79da2fdfa85706a98.png" width="1095">

<img alt="" height="276" src="https://img-blog.csdnimg.cn/666f75102e1c43d3b0bdc0f7de0cfd35.png" width="1031">

## 三、启动后端

### 初始化数据库 (要求 mysql5.7+)

>  
 执行Sql脚本： jeecg-boot/db/jeecgboot-mysql-5.7.sql 脚本作用：会自动创建库`jeecg-boot`, 并初始化数据 。 


<img alt="" height="675" src="https://img-blog.csdnimg.cn/be5733b6ce204a24a8bcb18a1602943f.png" width="773"> <img alt="" height="1200" src="https://img-blog.csdnimg.cn/287ba7bda63b4327baa68a19554c73b6.png" width="1200">

### 修改项目配置 (数据库、redis等)

`配置文件： jeecg-module-system/jeecg-system-start/src/main/resources/application-dev.yml`
-  a. 数据库配置(连接和账号密码) 
<img alt="" height="1200" src="https://img-blog.csdnimg.cn/dceb4d72af7e4ae6b45cab9e0be05028.png" width="1200">
-  b. Redis配置（配置redis的host和port） 
<img alt="" height="1200" src="https://img-blog.csdnimg.cn/ed453e92230c43858fe636eeb6b12909.png" width="1200">

### 启动项目&amp;访问

>  
 以上配置完成后，找到类  
 `jeecg-system-start/src/main/java/org/jeecg/JeecgSystemApplication.java` 
 右键执行启动； 
 通过 `http://localhost:8080/jeecg-boot/doc.html ` 访问后台的swagger地址。 


<img alt="" height="1200" src="https://img-blog.csdnimg.cn/96555744a2d3434aa8f2c17bd8315fc1.png" width="1200">

##  四、启动前端



### 执行命令下载依赖

执行命令`pnpm i` 或者 执行命令`yarn install`

<img alt="" height="374" src="https://img-blog.csdnimg.cn/f0924d492f1c4e6188102ad48200d3ee.png" width="1200">

### 启动前端项目

执行命令pnpm `serve` 启动项目 看到如下日志 则启动成功

 <img alt="" height="265" src="https://img-blog.csdnimg.cn/b90d69eec1f24b85b7e91458d9ccdae0.png" width="671">

通过 `http://localhost:3100` 访问前端项目 默认账号密码： `admin/123456`

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/1d96211178c0466d9ba4a2dbfaab1684.png" width="1200"> 
