
--- 
title:  RESTful风格学习笔记【包含示例】 
tags: []
categories: [] 

---


#### RESTful风格快速开发
- <ul><li>- <ul><li>- - 


### 1、REST、RESTful、传统风格

>  
 - **REST**全称是Representational State Transfer，中文为表述性状态转移，REST指的是一组架构约束条件和原则- RESTful表述的是资源的状态性转移，在Web中资源就是URI(Uniform Resource Identifier)- 如果一个架构符合REST的约束条件和原则，我们就称它为RESTful架构，HTTP是目前与REST相关的唯一实例- RESTful架构应该遵循统一的接口原则，应该使用标准的HTTP方法如GET和POST，并且遵循这些方法的语义 


#### 1.1REST简介

REST（Representational State Transfer），表现形式状态转换 **传统风格资源描述形式** http://localhost/user/getById?id=1 http://localhost/user/saveUser **REST风格描述形式** http://localhost/user/1 http://localhost/user **优点：** 隐藏资源的访问行为，无法通过地址得知对资源是何种操作 书写简化

#### 1.2 REST风格简介

按照REST风格访问资源时使用行为动作区分对资源进行了何种操作 http://localhost/users 查询全部用户信息  http://localhost/users/1 查询指定用户信息 http://localhost/users 添加用户信息 http://localhost/users 修改用户信息 http://localhost/users/1 删除用户信息 根据REST风格对资源进行访问称为RESTful

>  
 上述行为是约定方式，约定不是规范，可以打破，所以称REST风格，而不是REST规范 描述模块的名称通常使用复数，也就是加s的格式描述，表示此类资源，而非单个资源，例如：users、books、accounts…… 


### 2、HTTP方法的语义

|方法|语义
|------
|GET|获取指定的资源
|DELETE|删除指定的资源
|POST|发送数据给服务器，依据HTTP 1.1规范中的描述，结合实际项目开发经验，POST经常为了以统一的方法来涵盖以下功能：1.在公告板，新闻组，邮件列表或类似的文章组中发布消息 2 .通过注册新增用户3. 向数据处理程序提供一批数据，例如提交一个表单
|PUT|使用请求中的负载创建或者替换目标资源。PUT和POST的区别在于PUT是幂等的，而POST不是。幂等的含义可以理解为调用一次与连续调用多次是等价的（没有副作用或副作用不变）

#### 2.1 POST和PUT的区别
- POST和PUT的区别容易被简单地误认为“POST表示创建资源，PUT表示更新资源”- 而实际上，二者均可用于创建资源，更为本质的差别是在幂等性方面 <img src="https://img-blog.csdnimg.cn/d0646d5dc5834f4193249cbecf2f18a2.png" alt="在这里插入图片描述">
### 3、RESTful接口URL命名原则
- 命名原则1：HTTP方法后跟的URL必须是名词且统一成名词复数形式- 命名原则2：URL中不采用大小写混合的驼峰命名，尽量采用全小写单词，如果需要连接多个单词，则采用“-”连接- 示例：/users、/users-fans；反例：/getUsers、/getUsersFans
### 4、RESTful接口URL分级原则
- 分级原则1：一级用来定位资源分类，如/users即表示需要定位到用户相关资源- 分级原则2：二级仍用来定位具体某个资源，如/users/20即表示id为20的用户，再如/users/20/fans/1即表示id为20的用户的id为1的粉丝
>  
 一条小建议：原则是为了让我们的开发更加规范，但是不能成为束缚我们开发的枷锁！ 


### 5、RESTful接口命名示例
1. GET、POST、PUT、DELETE接口命名示例 <img src="https://img-blog.csdnimg.cn/106013c3381a4d29ac40519363d2c80a.png" alt="在这里插入图片描述">1. 复杂GET查询请求接口命名示例 <img src="https://img-blog.csdnimg.cn/139b9bbf2be042a294559dae040bcfdc.png" alt="在这里插入图片描述">
### 7、RESTful入门案例

**步骤**
1. 设定http请求动作（动词）
<img src="https://img-blog.csdnimg.cn/dc408979046345e8a3bdbb560319c1ba.png" alt="在这里插入图片描述">
1. 设定请求参数（路径变量） <img src="https://img-blog.csdnimg.cn/411ad455efcc4355a466edae9b3ae54c.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/f4d3e21eb8e142f99665f466667bf4d3.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d624c6785a4543fc9930bc041d3aedc3.png" alt="在这里插入图片描述">
### 8、@RequestBody @RequestParam @PathVariable

**区别** @RequestParam用于接收url地址传参或表单传参 @RequestBody用于接收json数据 @PathVariable用于接收路径参数，使用{参数名称}描述路径参数

**应用** 后期开发中，发送请求参数超过1个时，以json格式为主，@RequestBody应用较广 如果发送非json格式数据，选用@RequestParam接收请求参数 采用RESTful进行开发，当参数数量较少时，例如1个，可以采用@PathVariable接收请求路径变量，通常用于传递id值

### 9、RESTful快速开发

<img src="https://img-blog.csdnimg.cn/f7ae93edde9046c1b8e13c23dfbf817a.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/e2167eed8f2d4a05b32262f9585c8a27.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ce53e340d3bd4cb2a1d25dca82664a6e.png" alt="在这里插入图片描述">

### 10、基于RESTful页面数据交互

<img src="https://img-blog.csdnimg.cn/9ef36a1fb0634d19af26e67052272a60.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b0937ec2747a4409ae6c52624dbea509.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/c253a87e64fd49ce9a6c46a9829653ed.png" alt="在这里插入图片描述">

>  
 基于RESTful页面数据交互 先做后台功能，开发接口并调通接口 再做页面异步调用，确认功能可以正常访问 最后完成页面数据展示 补充：放行静态资源访问 

