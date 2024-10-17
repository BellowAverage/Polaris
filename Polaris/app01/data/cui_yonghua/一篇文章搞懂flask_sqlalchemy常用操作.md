
--- 
title:  一篇文章搞懂flask_sqlalchemy常用操作 
tags: []
categories: [] 

---
### 一.查询：

#### 1.1 查询所有

`模型类.query.all() 等价于 select * from user` 如果有条件的查询： `模型类.query.filter_by(字段名=值) --&gt; select * from user where 字段名=值` `模型类.query.filter_by(字段名=值).first() --&gt; select * from user where 字段=值 limit=1`

如：

```
select * from user where age&gt;17 and gender ='男'
select * from user username like 'zhang%'
select * from user where rdatetime &gt; xxx rdatetime &lt;xxx;

```

注意： 模型类.query.filter() 里边**是布尔的条件**模型类.query.filter(模型名.字段名==值) 模型类.query.filter_by() 里边**是一个等值**模型类.query.filter_by(字段名=值)

#### 1.2 模型类.query.filter()

1.模型类.query.filter().all()------------------&gt;列表 2.模型类.query.filter().first()--------------&gt;对象 如：

```
User.query.filter(User.username.endwith('z')).all() like '%z'
User.query.filter(User.username.startwith('z')).all() like 'z%'
User.query.filter(User.username.contains('z')).all() like '%z%'
User.query.filter(User.username.like('%z%')).all()

```

#### 1.3 多条件：

或者：or_ 并且：and_ 非：not_

```
User.query.filter(or_(User.username.like('z%'),User.username.contains('i'))).all()
select * from user where username like 'z%' or username like '%z%'

User.query.filter(and_(User.username.like('z%'),User.rdatetime &gt; '2020-10-22 23:58:23')).all()
select * from user where username like 'z%' and rdatetime &gt; '2020-10-22 23:58:23'

```

#### 1.4 若过滤时间和整型：&gt; ,&lt; ,&gt;=, &lt;=，!=

age:17,18,19,20,22,23,25…

```
select * from user where age in [17,18,22]

```

#### 1.5 排序：order_by

`user_list=User.query.filter(User.username.contains('z')).order_by(-User.rdatetime).all()` `user_list=User.query.order_by(-User.id).order_by(-User.rdatetime).all()`

对所有得进行排序，注意order_by()的参数： 1.直接是字符串：‘字段名’ 这样不能排序 2.模型.字段名：模型.字段 order_by(-模型.字段) 倒叙 还可以使用desc()函数

#### 1.6 限制：limit

limit的使用 + offset user_list=User.query.limit(2).all() 默认获取两条数据 user_list=User.query.offset(2).limit(2).all() 跳过两条记录再获取两条记录

Jquery CDN:引用网上的jQuery资源，加快速度，减少项目的复杂度和空间，更加方便与用户快速获取js效果。

查询小总结： 1.User.query.all() 所有 2.User.query.get(pk) 一个 3.User.query.filter() * ??? 如果要检索的字段是字符串（varchar,db.String） User.username.startwith(‘’) User.username.endwitd(‘’) User.username.contains(‘’) User.username.like(‘’) 传入的参数需要加% User.username.in_([‘’,‘’,‘’,‘’]) User.username== 如果要检索的字段是整型或日期类型： User.age.**lt**(18) 双下划线 User.rdatetime.**gt**(‘…’) User.age.**le**(18) User.age.**ge**(18) User.age.between(18,25) 多个条件一起检索：and_ or_ 非得条件：or_

排序：order_by() 获取指定数量：limit（） offset（） 4.User.query.filter_by(username=‘xxx’) User.query.filter(username== ‘xxx’)

### 二. 删除

#### 2.1 逻辑删除

其实就是更新（定义数据库中的表的时候，添加一个字段名为isdelete,通过此字段控制是否删除） id=request.args.get(id) 用于接收get请求中的参数 user=User.query.get(id) user.isdelete=True db.session.commit()

#### 2.2 物理删除

（彻底从数据库中删除） id=request.args.get(id) 用于接收get请求中的参数，若为post就把args替换成form user=User.query.get(id) db.session.delete(user) db.session.commit()

### 三. 更新

id=request.args.get(id) user=User.query.get(id) #修改对象的属性 user.username=xxx user.phone=xxx #提交修改 db.session.commit()

需要提交： 添加 user=User() user.xxx=xxx db.session.add(user) db.session.commit()

删除 user=User.query.get(id) db.session.delete(user) db.session.commit()

更新 user=User.query.get(id) #获取数据库中的对象 #修改对象的属性 user.username=xxx user.phone=xxx #提交修改 db.session.commit()
