
--- 
title:  2023Java商城毕业设计(附源码和数据库文件下载链接)Spring Boot + mysql + maven + mybatis-plus 
tags: []
categories: [] 

---


#### 2023Java商城毕业设计Spring Boot + mysql + maven + mybatis-plus
- <ul><li><ul><li>- - - - - - - <ul><li>- - - - 


>  
 资源目录如下：（源码+sql文件）  <img src="https://img-blog.csdnimg.cn/6db03934364643a98648e407923dd086.png" alt="在这里插入图片描述"> 


2000是正确码

#### 用户注册

<img src="https://img-blog.csdnimg.cn/cb2cca4f53ca4effbcfce8a0d1ec53f5.png" alt="在这里插入图片描述">

get

http://192.168.180.1/users/reg

userPhone/userMail 手机邮箱至少一个才能注册 （格式前端判断

userNickName （用户名长度前端定/判断

password 密码 6到14位前端判断

userSex 性别 0：女 1：男

userType 用户类型 0：用户，1：管理（不需要用户填写。

payPwd 支付密码（6位

返回参数为2000正确码

#### 用户登录

<img src="https://img-blog.csdnimg.cn/f2ed6c0576d34ee8aba4e18912f90b34.png" alt="在这里插入图片描述">

POST

http://192.168.180.1/users/login

userPhone/userMail 手机或邮箱登录 （格式前端判断

password 密码 （长度判断

#### 修改密码

<img src="https://img-blog.csdnimg.cn/d1ea12f973f74c028bacb09fdf590303.png" alt="在这里插入图片描述">

#### 商品列表（分类+模糊查询）

<img src="https://img-blog.csdnimg.cn/62b7e21900024d8dbc667e7628ff81af.png" alt="在这里插入图片描述">

#### 个人信息

GET

http://192.168.180.1/users/userInfo/show

用户登录就可以

其中返回的登录密码和支付密码（PayPwd）隐藏

返回参数

|data|
|------
|userNickName|用户名
|userPhone|“17707077070”
|userMail|邮箱
|payPwd|支付密码
|purchaseCount|购买商品次数
|purchaseSuccess|成功交易次数
|consumption|消费额

creditScore 信用分

#### 用户信息修改

POST

http://192.168.180.1/users/userInfo/update

以下没有的字段都不可修改，修改密码后给用户重定向登录

userPhone/userMail （格式前端判断

userNickName (长度和注册一样的规则)

oldPassword 旧密码长度判断

newPassword 密码 （新密码长度判断

oldPayPwd 旧支付密码修改（6位数修改支付密码不需要登录密码验证

newPayPwd 新支付密码（6位

返回参数为2000正确码

#### 订单信息

<img src="https://img-blog.csdnimg.cn/dfde5bd07939434486ba394f1e29d24d.png" alt="在这里插入图片描述">

POST

http://192.168.180.1/order/show

购物车与成交订单或退款订单或过期订单一个接口

请求参数（购物车查看订单未支付status传0 查看我的订单status传1（其中包括退款和过期的，前端可以区别显示订单类型

status 状态（0：未支付，1：已支付，2：已退款，3：已过期）

**记得折后价格（dealPrice)需要乘以数量(count)**

|id|订单号
|------
|userId|用户id
|productId|商品id
|shopsId|商铺id
|address|地址
|status|“1”
|discount|购入折扣
|updateBy|更新者
|updateDate|更新时间（用作购买时间
|productImg|图片
|price|原价
|dealPrice|折后价格
|productName|商品名
|shopsName|点名

count 数量

##### 添加至购物车

<img src="https://img-blog.csdnimg.cn/32913539c7d94b238839f9637c9654da.png" alt="在这里插入图片描述">

POST

http://192.168.180.1/order/add/order

请求参数

productImg 商品图片

price 原价

dealPrice 折扣价

currentDiscount 当前折扣

productName商品名

shopsName 商铺名

count 购买数量

返回参数

2000 正确码

##### 商品列表

GET

http://192.168.180.1/product/list/show

请求参数

productName 商品名搜索（模糊搜索

orderType 排序规则 0：热度排序 1：价格排序从低到高 2:价格排序从高到低

classPro 商品分类（1：服装，2：童装，2：鞋子，3：电子，4：书籍，5：宠物用品，6：生活用品，7零食

返回参数

|0|
|------
|id|商品id
|productName|商品名
|productDesc|商品简介
|shopsId|商铺id
|price|价格
|currentDiscount|当前折扣
|productImg|图片地址
|status|当前状态（0：下架，1：上架）
|dealCount|已成交数量
|type|商品类型（1：服装，2：童装，2：鞋子，3：电子，4：书籍，5：宠物用品，6：生活用品，7零食
|updateBy|更新者
|updateDate|可用作上架时间
|shopsName|店铺名
|disPrice|折后价格

##### 商铺详情

GET

http://192.168.180.1/product/list/show

复用商品列表接口

请求参数 shopsId 传入点击的商铺id（之后在店铺中的分类和排序和商品名搜索都需要携带商铺id

productName 商品名搜索（模糊搜索

orderType 排序规则 0：热度排序 1：价格排序从低到高 2:价格排序从高到低

classPro 商品分类（1：服装，2：童装，2：鞋子，3：电子，4：书籍，5：宠物用品，6：生活用品，7零食

返回参数商品列表一样

##### 商品详情

GET

http://192.168.180.1/product/details

请求参数

id 商品id

返回参数

**和商品列表的参数一样**

##### 商铺列表

GET

http://192.168.180.1/shops/list/show

请求参数

orderType 排序规则 1：热度 2：默认排序

shopsType 店铺类型（1：服装，2：童装，2：鞋子，3：电子，4：书籍，5：宠物用品，6：生活用品，7零食

shopsName 商铺名搜索(模糊搜索)

返回参数

|0|
|------
|id|商铺id
|shopsName|商铺名
|userId|用户id
|type|店铺类型（1：服装，2：童装，2：鞋子，3：电子，4：书籍，5：宠物用品，6：生活用品，7零食
|desc|“专卖玩具”
|status|店铺状态（0：正常，1：暂停运营，2：封禁）
|dealCount|成交订单数量
|createBy|创建人
|createDate|开店时间
|updateBy|更新者
|updateDate|更新时间


