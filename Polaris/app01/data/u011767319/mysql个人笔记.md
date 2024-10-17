
--- 
title:  mysql个人笔记 
tags: []
categories: [] 

---
### 表的text 用的过多，单行插入数据过多报8126错误，解决办法

在MySQL的配置文件 mysqld

```
innodb_file_per_table
innodb_file_format = Barracuda

```

在修改表 <img src="https://img-blog.csdnimg.cn/20190907092505944.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 就解决了

### 关于全文索引的使用（mysql版本起码要5.7以上，不然全文索引不生效）

查看全文索引参数

```
SHOW VARIABLES  LIKE 'ft%';

```

**ngram全文解析器** ngram就是一段文字里面连续的n个字的序列。ngram全文解析器能够对文本进行分词，每个单词是连续的n个字的序列。例如，用ngram全文解析器对“生日快乐”进行分词:

```
n=1: '生', '日', '快', '乐' 
n=2: '生日', '日快', '快乐' 
n=3: '生日快', '日快乐' 
n=4: '生日快乐'

```

MySQL 中使用全局变量ngram_token_size来配置ngram中n的大小，它的取值范围是1到10，默认值是2。通常ngram_token_size设置为要查询的单词的最小字数。如果需要搜索单字，就要把ngram_token_size设置为1。在默认值是2的情况下，搜索单字是得不到任何结果的。因为中文单词最少是两个汉字，推荐使用默认值2。 1、启动mysqld命令时

```
mysqld --ngram_token_size=2

```

2、修改MySQL配置文件

```
[mysqld] 
ngram_token_size=2

```

>  
 配置一下mysql的配置文件 win mysql的配置文件是 my.ini linux mysql 配置文件是 my.cnf 宝塔就不需要解释了，直接设置里面设置就行 


配置文件（宝塔）：

```
[mysqld]
# 全文检索分词数
ft_min_word_len=1 #最小索引数
ngram_token_size=1 #解析器最小索引数

```

切记配置完需要重新启动mysql ，重新建立全文索引。否则不生效

使用navicat 工具： <img src="https://img-blog.csdnimg.cn/20200505210725893.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 解析器：ngram 必须添加，不然全文索引不生效

全文索引使用的sql 语句和模糊搜索不一样，它有专属语句： MATCH （表字段：与索引吻合） AGAINST(‘检索的字符串’)

```
SELECT * FROM cs_text where MATCH(title) AGAINST('广东');

```

全文检索模式 常用的全文检索模式有两种：

1、自然语言模式(NATURAL LANGUAGE MODE) ， 自然语言模式是MySQL 默认的全文检索模式。自然语言模式不能使用操作符，不能指定关键词必须出现或者必须不能出现等复杂查询。

2、BOOLEAN模式(BOOLEAN MODE) BOOLEAN模式可以使用操作符，可以支持指定关键词必须出现或者必须不能出现或者关键词的权重高还是低等复杂查询。

示例

```
SELECT * FROM articles
WHERE MATCH (title,body)
AGAINST ('一路 一带' IN NATURAL LANGUAGE MODE);

// 不指定模式，默认使用自然语言模式
SELECT * FROM articles
WHERE MATCH (title,body)
AGAINST ('一路 一带');

```

上面的示例返回结果会自动按照相关性排序，相关性高的在前面。相关性的值是一个非负浮点数，0表示无相关性。

```
// 获取相关性的值
SELECT id,title,
MATCH (title,body) AGAINST ('手机' IN NATURAL LANGUAGE MODE) AS score
FROM articles
ORDER BY score DESC;

```

<img src="https://img-blog.csdnimg.cn/2019042909220512.png" alt="在这里插入图片描述">

```
// 获取匹配结果记录数
SELECT COUNT(*) FROM articles
WHERE MATCH (title,body)
AGAINST ('一路 一带' IN NATURAL LANGUAGE MODE);

```

可以使用BOOLEAN模式执行高级查询。

```
// 必须包含"腾讯"
SELECT * FROM articles
WHERE MATCH (title,body)
AGAINST ('+腾讯' IN BOOLEAN MODE);

```

<img src="https://img-blog.csdnimg.cn/201904290922505.png" alt="在这里插入图片描述">

```
// 必须包含"腾讯"，但是不能包含"通讯工具"
SELECT * FROM articles
WHERE MATCH (title,body)
AGAINST ('+腾讯 -通讯工具' IN BOOLEAN MODE);

```

<img src="https://img-blog.csdnimg.cn/20190429092318706.png" alt="在这里插入图片描述"> 下面的例子演示了BOOLEAN模式下运算符的使用方式：

```
'apple banana' 
无操作符，表示或，要么包含apple，要么包含banana

'+apple +juice'
必须同时包含两个词

'+apple macintosh'
必须包含apple，但是如果也包含macintosh的话，相关性会更高。

'+apple -macintosh'
必须包含apple，同时不能包含macintosh。

'+apple ~macintosh'
必须包含apple，但是如果也包含macintosh的话，相关性要比不包含macintosh的记录低。

'+apple +(&gt;juice &lt;pie)'
查询必须包含apple和juice或者apple和pie的记录，但是apple juice的相关性要比apple pie高。

'apple*'
查询包含以apple开头的单词的记录，如apple、apples、applet。

'"some words"'
使用双引号把要搜素的词括起来，效果类似于like '%some words%'，
例如“some words of wisdom”会被匹配到，而“some noise words”就不会被匹配。

```

注意
- 只能在类型为CHAR、VARCHAR或者TEXT的字段上创建全文索引。- 全文索引只支持InnoDB和MyISAM引擎。- MATCH (columnName) AGAINST (‘keywords’)。MATCH()函数使用的字段名，必须要与创建全文索引时指定的字段名一致。如上面的示例，MATCH (title,body)使用的字段名与全文索引ft_articles(title,body)定义的字段名一致。如果要对title或者body字段分别进行查询，就需要在title和body字段上分别创建新的全文索引。- MATCH()函数使用的字段名只能是同一个表的字段，因为全文索引不能够跨多个表进行检索。- 如果要导入大数据集，使用先导入数据再在表上创建全文索引的方式要比先在表上创建全文索引再导入数据的方式快很多，所以全文索引是很影响TPS的。
### win 安装 mysql 8.*版本



### Navicat for MySQL 设置定时任务（事件）

>  
 比如平时我需要定时恢复一些签到数据或者恢复一些心跳包数据，就可以利用mysql来定时处理数据库数据 


**检查mysql是否开启定时任务**
1. 查询界面输入命令，查看定时任务是否开启，未开始时OFF： `show variables like '%event_scheduler%';`1. 查询界面输入命令，开启定时任务： `set global event_scheduler =1`（再使用`show variables like '%sche%';` 可查看到为on）
**Navicat 建立定时任务** 新建一个函数 ，取名为update_qiandao ,内容为 UPDATE week7_user SET isqiandao = 0 <img src="https://img-blog.csdnimg.cn/20201112102046816.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 参照上图，新建一个事件 ，在定义里写 call update_qiandao() --也就是之前定义的函数 <img src="https://img-blog.csdnimg.cn/20201112102059720.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 在“计划”选项卡中设置 执行时间，这里我选择的是每天。 <img src="https://img-blog.csdnimg.cn/202011121021130.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

### 查询数据库-对应表的信息

```
SELECT
COLUMN_NAME 列名,
COLUMN_TYPE 数据类型,
COLUMN_KEY 主键,
COLUMN_COMMENT 注释
FROM
information_schema.`COLUMNS`
WHERE
TABLE_SCHEMA='face_recognition_test' #数据库名
AND
table_name='masses_face_database' #表

```

### 截断表数据

```
truncate table 表;

```
