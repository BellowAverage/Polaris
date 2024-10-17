
--- 
title:  基于JAVA的个人信息管理系统源码，含基于VUE的PC前端及移动端，用于管理个人消费、锻炼、音乐、阅读、健康、饮食等衣食住行信息 
tags: []
categories: [] 

---
### 项目介绍

完整代码下载地址： 用于管理个人消费、锻炼、音乐、阅读、健康、饮食、人生经历等各个衣食住行信息的系统，通过提醒、计划模块利用调度系统来统计分析执行情况。 并通过积分和评分体系来综合评估个人的总体状态。

系统可以说是一个个人助理系统，它主要解决三个问题：
- 我的计划(期望)是什么？- 我要做什么？- 我做了什么？
该系统是前后端分离的项目，当前项目mulanbay-server为后端API项目，只提供系统的api接口，整个系统必须要同时运行前端才能完整访问。

木兰湾前端项目：

VUE版本
- 基于Vue的前端(PC端)[mulanbay-ui-vue]- 基于Vue的前端(移动端)[mulanbay-mobile-vue]


#### 功能简介
- 基于RBAC的用户权限管理- 支持分布式运行的调度功能- 基于AHANLP的自然语言学习服务- 提供消费、锻炼、音乐、阅读、健康、饮食、人生经历等常用模块- 统一的日志管理及日志流分析- 提供基于模板化的提醒、计划、图表、行为配置及分析- 统一的日历管理，提供日历自动新增、完成功能- 提供磁盘、CPU、内存的监控及报警，并可以自动恢复- 数据库数据、备份文件自动清理- 统一及强大的图表统计分析功能- 基于微信公众号消息、邮件的消息提醒服务- 基于错误代码的消息发送可配置化- 基于Hibernate的配置化的查询便捷封装- 提供可配置的个人积分和评分体系- 提供多角度的用户行为分析- 提供词云、相似度、智能问答等分析功能
#### 文档地址

木兰湾文档

#### 所用技术
- 前端：Vue、Jquery、Element UI、Echarts- 后端：Spring Boot、Hibernate、Quartz、NLP、Redis &amp; Jwt
|核心依赖|版本
|------
|Spring Boot|2.3.4.RELEASE
|Hibernate|5.4.21.Final
|Quartz|2.3.2

#### 项目结构

```
mulanbay-server
├── mulanbay-business    -- 通用业务类
├── mulanbay-common      -- 公共模块
├── mulanbay-persistent  -- 持久层基于hibernate的封装
├── mulanbay-pms         -- 木兰湾API接口层
├── mulanbay-schedule    -- 调度模块封装
├── mulanbay-web         -- 基于SpringMVC的一些封装


```

#### 项目运行与部署

```
# Step 1：初始化数据库

1. 下载源代码
2. 在mysql中创建数据库，比如:mulanbay_db
3. 初始化数据库,执行mulanbay-pms工程docs目录下的sql文件：mulanbay_init.sql

(mulanbay_init.sql里面的数据只有原始的空数据，如果想看模拟的数据，可以选择导入mulanbay_init_data.sql(同时包含表结构和初始化数据))

# Step 2：修改配置文件

1. 在mulanbay-pms/src/main/resources/目录下复制application-local-template.properties文件并重命名为application-local.properties，设置本地配置。
   其中Mysql数据库配置、Redis配置为必须配置，如果需要使用微信公众号的消息发送功能，需要配置.
2. 智能客服、词云、商品重复度、饮食重复度等需要用到AHANLP的自然语言处理，需要配置hanlp.properties，ahanlp.properties
  * hanlp.properties文件中需要设置根路径，如：root=D:/ws/AHANLP_base-1.3
  * ahanlp.properties文件中需要设置里面的各个配置项
  * 词云模块需要使用Python的wordcloud插件（3.0版本及以后不需要，词云修改为echarts实现），安装命令：
    pip3 install wordcloud -i https://pypi.tuna.tsinghua.edu.cn/simple
  * NLP所需要的ahanlpData文件包，请到百度网盘下载：（链接：https://pan.baidu.com/share/init?surl=zECO4re43orEOwdZrO7rUg 提取码：w86y ）
    或者直接去原作者项目处下载：https://github.com/jsksxs360/AHANLP/blob/master/github/w2v.md

# Step 3：打包&amp;运行

1. 开发环境
  运行mulanbay-pms子工程下的cn.mulanbay.pms.web.Application

2. 正式环境
  * 进入到mulanbay-server目录，运行mvn clean package
  * 运行mulanbay-pms/target下的mulanbay-pms-3.0.jar文件

后端项目默认的端口是：8080，项目路径为api，完整的路径地址：http://localhost:8080/api/

# Step 4：用户数据初始化

系统默认包含两个用户admin和mulanbay，密码都是123456.admin用户主要是维护使用，一般以mulanbay用户登录。

mulanbay用户默认情况下是没有任何业务数据的，可以在"权限管理/用户管理"里对mulanbay用户进行"初始化数据"，系统可以显示mulanbay用户基础的配置数据。


```

#### 软件要求

|软件|版本
|------
|JDK|1.8+
|Nginx|1.17+
|Redis|6.0+
|Mysql|8.0+

#### 硬件要求

内存4G+

### 系统架构

#### 系统模块

<img src="https://img-blog.csdnimg.cn/475d5e689d2f4839ab4cdb09a808ebe0.png" alt="在这里插入图片描述">

#### 系统结构

<img src="https://img-blog.csdnimg.cn/331ca558312d4a8ba3d751a93f7caa6f.png" alt="在这里插入图片描述">

#### 业务流程

<img src="https://img-blog.csdnimg.cn/909c8351353f4758bc7940bf08aac109.png" alt="在这里插入图片描述">

#### 图表分类

<img src="https://img-blog.csdnimg.cn/bb335b1111b4471eba949cfe99414940.png" alt="在这里插入图片描述">

### 参考/集成项目

木兰湾参考、集成了一些项目，有些功能自己也只是一个搬运工，先感谢大家的开源。
- Jquery版本前端(移动)UI组件：- Jquery版本前端(移动)Tag方案：- 前端(PC)日历组件：- 自然语言学习：- Vue版本前端(PC)：，- Vue版本前端(PC)自动表单生成：- 智能客服UI组件：
### Q&amp;A
-  Q：用户计划的时间线统计图没有数据？ A: 计划的时间线数据需要日终调度程序来统计的，第二天凌晨后才会有当天的数据。 -  Q：我的日历里面没有数据？ A: 自动生成的日历也是需要日终调度程序来统计的，第二天凌晨后才会有数据。 不过日历也可以手动创建，但是手动日历无法自动关闭。 
### 项目展望

### 项目截图

#### 基于Vue的PC端

<img src="https://img-blog.csdnimg.cn/0c269b9128214ea28948ce2b3a2c996e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/1b0d3526a2d244ed97889d99d450d545.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/1e1012f6226b48b08bd2fa40e4d8fc56.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/92db5e48d9f24a9f97a8a9e2205de1ee.png" alt="在这里插入图片描述">

#### 基于Vue的移动端

<img src="https://img-blog.csdnimg.cn/30efeddca0274102b8ae1dc54407a0f7.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/9cbf13ad7dd24e8a8faa3444ffb91c8c.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b040cd980e214f7fa7701a9b9e57507c.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/c6e7b6376e084557a49a675f11d62ab4.png" alt="在这里插入图片描述">

#### 微信公众号消息推送

<img src="https://img-blog.csdnimg.cn/a17dc4205ac44c9787ba3c4d37d766bf.png" alt="在这里插入图片描述">

完整代码下载地址：
