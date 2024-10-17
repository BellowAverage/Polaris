
--- 
title:  基于java web SSM框架的仓库管理系统源码+数据库，可做毕业设计，含项目部署视频教程 
tags: []
categories: [] 

---
## 基于SSM框架的仓库管理系统

### 视频-IDEA导入+运行项目演示

>  
 「基于SSM框架的仓库管理系统演示.mp4」https://www.aliyundrive.com/s/EyvLAHvJsfK 提取码: zf19 


### 功能
- 系统操作权限管理。系统提供基本的登入登出功能，同时系统包含两个角色：系统超级管理员和普通管理员，超级管理员具有最高的操作权限，而普通管理员仅具有最基本的操作权限，而且仅能操作自己被指派的仓库。- 请求URL鉴权。对于系统使用者登陆后进行操作发送请求的URL，后台会根据当前用户的角色判断是否拥有请求该URL的权限。- 基础数据信息管理。对包括：货物信息、供应商信息、客户信息、仓库信息在内的基础数据信息进行管理，提供的操作有：添加、删除、修改、条件查询、导出为Excel和到从Excel导入。- 仓库管理员管理。对仓库管理员信息CRUD操作，或者为指定的仓库管理员指派所管理的仓库。上述中的仓库管理员可以以普通管理员身份登陆到系统。- 库存信息管理。对库存信息的CRUD操作，导入导出操作，同时查询的时候可以根据仓库以及商品ID等信息进行多条件查询。- 基本仓库事务操作。执行货物的入库与出库操作。- 系统登陆日志查询。超级管理员可以查询某一用户在特定时间段内的系统登陆日志。- 系统操作日志查询。超级管理员可以查询某一用户在特定时间段内对系统进行操作的操作记录。、- 密码修改。
### 使用到的框架和库
- Apache POI- MyBatis- Spring Framework- Spring MVC- Apache Shiro- Ehcache- Apache Commons- Log4j- Slf4j- Jackson- C3P0- Junit- MySQL-Connector- jQuery- Bootstrap
### 登陆系统方式

用户ID : 1001 密码 ：123456 <img src="https://img-blog.csdnimg.cn/1a493e51b58647e5b229999099e411e6.png" alt="在这里插入图片描述">

加密代码

```
// 用户密码（wms_user.USER_PASSWORD）加密规则
String tempStr = MD5Util.MD5("123456");// 第一次对密码进行加密
String encryptPassword = MD5Util.MD5(tempStr + "1001");// 第二次对密码进行加密
//存入数据库的加密密码
System.out.println(encryptPassword);

```

新增用户默认密码为用户ID（比如新增一个用户ID为1012，密码也为1012）

### 数据库版本

#### **5.7（不要一味求新，企业开发大多用的5.7左右版本，稳定）**

### 数据库关系图

<img src="https://img-blog.csdnimg.cn/d247395a9336478b82aaa97bfc4d1c10.png" alt="在这里插入图片描述">

### 部分截图

<img src="https://img-blog.csdnimg.cn/c363f0d00c1a40f4ad3f343553fd9838.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/473019cd853147e0b39d3cc3b5fbee16.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/5dcff7c3b43f470286b4137258e84e57.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b051479ddd654e6faf5f9f4d69aa96d2.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/df12128491404b668caf1d664708fe53.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/aa8701c3823a475b89062bcebe7f417f.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/0cf778d941534cdf905cb2a7642cdf7b.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/88819d051aa64acc96e547927bb7fd6b.png" alt="在这里插入图片描述"> 完整代码下载地址：
