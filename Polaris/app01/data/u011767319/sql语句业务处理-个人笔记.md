
--- 
title:  sql语句业务处理-个人笔记 
tags: []
categories: [] 

---
### sql -业务解决笔记

**模糊搜索更具搜索的关键字越精准排序**

```
select *
from ccb_user.ccb_user
where nick_name like concat('%',#{keyword},'%')
order by locate(#{keyword}, nick_name), char_length(nick_name);

```

### mysql 根据传入的id顺序进行排序

```
SELECT * FROM table ORDER BY FIELD(id, 1, 2, 3, 4);

```

### sql先排序后分组的例子

>  
 再业务中我们会遇到需要排序后分组的例子，但是sql的分组默认是那最小id的那一条数据，不符合我们的业务。所以参考以下例子： 


>  
 例子： 一个表有四个字段id，out_trade_no，fees_pay_id，created。其中id和out_trade_no两个字段是唯一的，根据传入的一批fees_pay_id集合，先根据created倒序排，后根据fees_pay_id分组，获取fees_pay_id的每一个out_trade_no的是created倒序的最新一条数据。sql怎么写 以下是可以用于实现所需功能的 SQL 查询语句： 


```
SELECT t1.id, t1.out_trade_no, t1.fees_pay_id, t1.created
FROM your_table_name t1
INNER JOIN (
  SELECT fees_pay_id, MAX(created) AS max_created
  FROM your_table_name
  WHERE fees_pay_id IN (your_list_of_fees_pay_ids)
  GROUP BY fees_pay_id
) t2 ON t1.fees_pay_id = t2.fees_pay_id AND t1.created = t2.max_created
GROUP BY t1.fees_pay_id, t1.out_trade_no, t1.id
ORDER BY t1.created DESC, t1.fees_pay_id

```

**解释如下：**

>  
 注意，这个查询语句假设 id 和 out_trade_no 字段都是唯一的。如果 out_trade_no 不唯一，需要对查询语句进行修改，例如使用子查询或窗口函数等方式来选取每个 fees_pay_id 中最新的 out_trade_no。 

1. your_table_name 是存储数据的表名。1. your_list_of_fees_pay_ids 是需要查询的 fees_pay_id 的集合，可以替换为具体的值或变量。1. 首先使用子查询 t2 来查找每个 fees_pay_id 中创建时间最晚的记录，并以 fees_pay_id 为分组字段。1. 然后将 t1 表与 t2 表进行内连接，以 fees_pay_id 和 created 字段匹配，从而得到 fees_pay_id 中创建时间最晚的一条记录，并选出对应的 id、out_trade_no 和 created 字段。1. 使用 GROUP BY 子句将结果按 fees_pay_id、out_trade_no 和 id 进行分组，以便保证每个 fees_pay_id 中的 out_trade_no 只选取一次，并且在 MySQL 5.7 中，对于非聚合列（即 id 和 out_trade_no），必须将其列入分组依据，否则查询会失败。1. 最后按照 created 字段的倒序和 fees_pay_id 字段进行排序，得到最终结果。
### 获取两级树名称

**表**

```
CREATE TABLE `p_product_category` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键',
  `merchant_id` bigint NOT NULL COMMENT '商家id',
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '名称',
  `description` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '描述',
  `image` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '分类图片',
  `sort` int NOT NULL DEFAULT '0' COMMENT '排序序号',
  `parent_id` bigint NOT NULL DEFAULT '0' COMMENT '父类目id，根级节点默认为0',
  `leaf` tinyint(1) NOT NULL DEFAULT '1' COMMENT '是否叶子节点',
  `hierarchy` int DEFAULT '0' COMMENT '层级',
  `created` bigint NOT NULL COMMENT '创建时间',
  `updated` bigint DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=314 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='商品类目表';

```

<img src="https://img-blog.csdnimg.cn/ee8fd0efbf7840d099957e03e7013893.png" alt="在这里插入图片描述"> **sql**

```
SELECT
	d.id,
	group_concat( c.NAME SEPARATOR ' &gt; ' ) AS NAME
FROM
	p_product_category c
	INNER JOIN (
	SELECT
		a.id,
		substring_index( substring_index( a.path, ',', b.help_topic_id + 1 ), ',', - 1 ) AS pid
	FROM
		(
		SELECT
			cat.id,
			concat( cat.parent_id, ',', cat.id ) path 
		FROM
			p_product_category cat 
		WHERE
		cat.id IN ( 65 )) a
		INNER JOIN mysql.help_topic b ON b.help_topic_id &lt; ( length( a.path ) - length( REPLACE ( a.path, ',', '' )) + 1 ) 
	ORDER BY
		pid 
	) d ON d.pid = c.id 
GROUP BY
	d.id

```

**实现效果** <img src="https://img-blog.csdnimg.cn/9b1496ecd372480dbb3b8ce3d9539281.png" alt="在这里插入图片描述">

### 获取树名字（无限级别的）

**表**

```
CREATE TABLE `category` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '类目名称',
  `path` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '类目路径',
  `parent_id` bigint DEFAULT NULL COMMENT '父类目id',
  `created` bigint NOT NULL COMMENT '创建时间',
  `filter` tinyint(1) NOT NULL COMMENT '是否筛选项',
  `sort` int NOT NULL COMMENT '排序号',
  `type` int DEFAULT NULL COMMENT '分类类型 1 = 资讯 2 = 活动',
  `editor_id` bigint DEFAULT NULL COMMENT '编辑人用户id',
  `editor_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '编辑人用户名',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3321 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

```

<img src="https://img-blog.csdnimg.cn/579b121ca9f0419caab173bb50290d40.png" alt="在这里插入图片描述"> **sql**

```
SELECT
	e.id,
	group_concat( d.NAME ) AS category_name 
FROM
	cca_basic.category d
	INNER JOIN (
	SELECT
		a.id,
		substring_index( substring_index( a.path, '/', b.help_topic_id + 1 ), '/', - 1 ) AS npath 
	FROM
		(
		SELECT
			id,
			concat( substr( c.path, 5 ), id ) AS path 
		FROM
			cca_basic.category c 
		WHERE
		id IN (3288)) a
	INNER JOIN mysql.help_topic b ON b.help_topic_id &lt; ( length( a.path ) - length( REPLACE ( a.path, '/', '' )) + 1 )) e ON e.npath = d.id 
GROUP BY
	e.id;

```

**效果** <img src="https://img-blog.csdnimg.cn/760212f091bb493091ddc1aa13f570fc.png" alt="在这里插入图片描述">

### 查询json字段的演示

**例子**

>  
 字段名是`transportUser` mysql 的json字段模糊查询[{“transportUser”: 474, “transportUserName”: “天乡”},{“transportUser”: 473, “transportUserName”: “天乡”},{“transportUser”: 475, “transportUserName”: “天乡”}]里的transportUser为474或者475的数据 


```
[{<!-- -->"transportUser": 474, "transportUserName": "天乡"},{<!-- -->"transportUser": 473, "transportUserName": "天乡"},{<!-- -->"transportUser": 475, "transportUserName": "天乡"}]

```

>  
 sql是这样写的 


```
SELECT * FROM your_table
WHERE JSON_CONTAINS(your_json_column, '{"transportUser": 474}')
   OR JSON_CONTAINS(your_json_column, '{"transportUser": 475}');

-- 或者
SELECT * FROM your_table
WHERE JSON_CONTAINS(your_json_column, '{"transportUser": 474}', '$')
   OR JSON_CONTAINS(your_json_column, '{"transportUser": 475}', '$');

```
