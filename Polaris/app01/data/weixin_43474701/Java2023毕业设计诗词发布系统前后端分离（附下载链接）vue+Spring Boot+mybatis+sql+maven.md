
--- 
title:  Java2023毕业设计诗词发布系统前后端分离（附下载链接）vue+Spring Boot+mybatis+sql+maven 
tags: []
categories: [] 

---


#### Java2023毕业设计诗词发布系统前后端分离（附资源下载链接含数据库文件）vue+Spring Boot+mybatis+sql+maven
- <ul><li><ul><li><ul><li>- - - - - - - - - - - - - 


>  
 资源目录如下：  <img src="https://img-blog.csdnimg.cn/8e6764688a0849099c329257de37bc9d.png" alt="在这里插入图片描述"> 


`项目基本功能如下：`

```
格式限制前端限制   0是成功码

```

##### 注册

```
/user/reg
post
请求
手机号 userPhone 格式限制
密码 userPwd 格式限制 6-12
用户名 userNickname 格式限制 2-6
无返回

```

##### 登录

<img src="https://img-blog.csdnimg.cn/cfad263890004776b0c4ee50a1d3e86a.png" alt="在这里插入图片描述">

```
/user/login
get
请求
手机号 userPhone 格式限制
密码 userPwd 格式限制 6-12
返回
用户id userId
用户昵称 userNickname

```

##### 查看个人信息

```
/user/show/info
post
无请求数据登录就行
返回
用户名 userNickname
手机号 userPhone 格式限制
用户简介 userDesc 限制五十字

```

##### 修改个人信息

<img src="https://img-blog.csdnimg.cn/e3eb1d85631b48dabc159e53fb7398bb.png" alt="在这里插入图片描述">

```
/user/update/info
post
请求
用户名 userNickname
手机号 userPhone 格式限制
旧密码 oldPwd 格式限制
新密码 newPwd 格式限制
简介 userDesc 限制五十字
返回
无，重定向登录，后端会删除登录信息

```

##### 诗词曲列表

```
/poetry/list
post
请求
类型 1：诗，2：词，3：曲 type
当前页 pageNumber 不给默认1
页面大小 pageSize 不给默认10
返回
是否为登录用户发布的诗词曲 poetryIsLoginUser 0不是，1是
诗词曲id id
发布用户id userId
标题 title
内容 content
发布用户昵称 releaseUserName
作者 author
类型 1：诗，2：词，3：曲 type
发布时间 createDate

```

##### 搜索

<img src="https://img-blog.csdnimg.cn/f30f6643bcfb4e159068a1f490e764fe.png" alt="在这里插入图片描述">

```
与诗词曲列表相比添加一个请求参数
标题 title

```

##### 诗词曲详情

发布 <img src="https://img-blog.csdnimg.cn/1e48b62016f640c0b9d8367841455e1e.png" alt="在这里插入图片描述">

```
/poetry/details
post
请求
诗词曲id id
返回
看上面的列表

```

##### 评论列表

```
/comment/show/list
post
请求
诗词曲id poetryId
当前页 pageNumber 不给默认1
页面大小 pageSize 不给默认10
返回
评论的用户是否为登录用户 0:不是，1:是 commentIsLoginUser
评论用户名 userNickname
评论内容 comment
评论id id
评论时间 createDate
评论的用户id userId

```

##### 点赞与取消点赞

<img src="https://img-blog.csdnimg.cn/ba131e7fc4114b919360964bc67526ad.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/179b5dd162f040a2ae08258aa98f58bd.png" alt="在这里插入图片描述">

```
/operation
post
请求
取消或添加 0：取消 1：添加 operationType
诗词曲id poetryId
点赞或收藏 1：点赞 2：收藏 type 
无返回

```

##### 收藏取消收藏

```
与点赞完全一致

```

##### 评论与删除评论

```
/comment/operation
post
请求
添加评论给 1 删除评论给 0 type 
添加评论---------诗词曲id和评论内容 poetryId和comment
删除评论---------评论id id

```

##### 发布诗词曲

<img src="https://img-blog.csdnimg.cn/39c1e40a8ede4467a31bb57b0b75cc94.png" alt="在这里插入图片描述">

```
/poetry/add
post
请求
作者 author
标题 title
内容 content
类型 1：诗，2：词，3：曲 type
无返回

```

##### 删除诗词曲

```
/poetry/delete
post
请求
诗词曲id id
无返回

```

##### 查看用户点赞或收藏

```
/operation/show
post
请求
type传1看点赞列表，传2看收藏列表

```


