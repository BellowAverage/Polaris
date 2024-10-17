
--- 
title:  使用navicat连接postgresql报错问题解决 
tags: []
categories: [] 

---
## 使用navicat连接postgresql报错问题解决

### 一、问题现象：

最近使用Navicat来连接postgreSQL数据库，发现连接不上，报错信息如下：

<img src="https://img-blog.csdnimg.cn/4da692c8b9cb4e458089cbf76ff0df37.png#pic_center" alt="在这里插入图片描述">

自己百度了一下，发现pgsql 15版本以后，有些系统表的列名改了，pg_database表里的这一个列被删除了导致的。

<img src="https://img-blog.csdnimg.cn/7d7363adc28d4b78a2f3825c104115ee.png#pic_center" alt="在这里插入图片描述">

### 二、解决方法：

#### 1、升级Navicat版本：

将navicat升级到16.2以上版本；

<img src="https://img-blog.csdnimg.cn/047515a1440445519d1ad35fee856fb4.png#pic_center" alt="在这里插入图片描述">

#### 2、使用低版本的postgreSQL：

降级pgsql、老版本仍然可用。

#### 3、修改Navicat的dll文件：

找到navicat安装目录，有一个libcc.dll文件。

<img src="https://img-blog.csdnimg.cn/071a3d8cdc594228ae5a6954aba8f330.png#pic_center" alt="在这里插入图片描述">
- 备份这个文件；- 进入网站 https://hexed.it/ 打开本地的libcc.dll 文件；- 右侧点击搜索，关键词 SELECT DISTINCT datlastsysoid ；- 找到之后，把 datlastsysoid 这几个字，改成 dattablespace ；- 然后把文件下载回来，放回原处。
<img src="https://img-blog.csdnimg.cn/9119bb892c4a49c8a2753da11c26a199.png#pic_center" alt="在这里插入图片描述">

最后，重启Navicat，可以发现无论老和新版本的pgsql都可以正常访问了。

<img src="https://img-blog.csdnimg.cn/574d81ae2a1d468c918e6cdc4323e9ff.png#pic_center" alt="在这里插入图片描述">
