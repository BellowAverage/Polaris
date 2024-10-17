
--- 
title:  JAVA个人健康信息管理系统源码+数据库，基于spring+springmvc+mybatis+mysql 
tags: []
categories: [] 

---
## health-manager

##### 介绍

个人健康信息管理系统 完整代码下载地址：

##### 软件架构

spring+springmvc+mybatis+mysql+jsp+bootstrap

##### 安装教程
1. 数据库导入sql文件1. eclipse导入maven项目1. 设置项目project facets，配置版本Dynamic Web Model为[3.0,)1. 配置web容器，导入项目到容器中，启动容器
##### 使用说明
1. 访问地址：(http://localhost:{web容器端口}/{项目名称}/)
##### 项目效果

<img src="https://img-blog.csdnimg.cn/c8c7941a71534830811485d92f478303.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/5a57cb95277940d0bf17f92be1300e3e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/00fab846db80488a8631c8674f6d0ff2.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/a1608185a8ae418f9163094b49e190b1.png" alt="在这里插入图片描述">

##### 附录

###### Mybatis字段类型映射

```
JDBCType      |     JavaType
----------------------------
CHAR                String
VARCHAR             String
LONGVARCHAR         String
NUMERIC             java.math.BigDecimal
DECIMAL             java.math.BigDecimal
BIT                 boolean
BOOLEAN             boolean
TINYINT             byte
SMALLINT            short
INTEGER             int
BIGINT              long
REAL                float
FLOAT               double
DOUBLE              double
BINARY              byte[]
VARBINARY           byte[]
LONGVARBINARY       byte[]
DATE                java.sql.Date
TIME                java.sql.Time
TIMESTAMP           java.sql.Timestamp
CLOB                Clob
BLOB                Blob
ARRAY               Array
DISTINCT            mapping of underlying type
STRUCT              Struct
REF                 Ref
DATALINK            java.net.URL[color=red][/color]

```

###### SpringMVC 入参校验注解

```
校验注解                     可校验类型                                                                        具体类型
@AssertTrue  Boolean、boolean                 属性必须是true
@AssertFalse Boolean、boolean                 属性必须是false
@Null        基本类型除外                       属性必须为null
@NotNull     基本类型除外                       属性必须不能为null
@NotEmpty    CharSequence、Collection、Map     属性不能为null，字符串和集合长度不能为0（无法校验空字符串）
@NotBlank    CharSequence                    属性不能为null，并不能为空字符串
@Size        CharSequence、Collection、Map    属性长度必须在指定范围
@Length      CharSequence                    属性长度必须在指定范围
@Min         Number                          属性必须大于指定最小值
@Max         Number                          属性必须小于指定最大值
@Range       Number                          属性在指定返回内
@Past        Date、Calender                   属性时间必须大于当前时间
@Future      Date、Calender                   属性时间必须小于当前时间
@Email       CharSequence                    属性必须是合法邮件格式
@Pattern     CharSequence                    属性必须匹配正则表达式

```
