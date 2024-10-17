
--- 
title:  jsqlparser 安装和使用 
tags: []
categories: [] 

---
jsqlparser是sql语句解析工具，可以解析sql并分析语法。

## 安装

```
&lt;dependency&gt;
	&lt;groupId&gt;com.github.jsqlparser&lt;/groupId&gt;
		&lt;artifactId&gt;jsqlparser&lt;/artifactId&gt;
	&lt;version&gt;4.3&lt;/version&gt;
&lt;/dependency&gt;

```

使用

```
   String s = """
                CREATE TABLE `abc` (
                  `abc1` int NOT NULL AUTO_INCREMENT,
                  `abc2` varchar(255) DEFAULT NULL COMMENT 'comment',
                  `abc3` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'comment2',
                  UNIQUE KEY `abc1` (`abc1`),
                  KEY `abc2` (`abc2`),
                  KEY `abc3` (`abc3`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb""";

        Statement parse = CCJSqlParserUtil.parse(s);
        if (parse instanceof CreateTable t) {<!-- -->
            System.out.println(parse);
        }
    }

```

通过parse方法即可发现： <img src="https://img-blog.csdnimg.cn/74adcc978ef940b6a2757f739f78b631.png" alt="在这里插入图片描述"> 一些细节：
- 不支持 # 语法，而只支持 – 对ssql的注释。 如果使用#会提示#无法解析- 索引必须有名称，如果是没名称的索引会抛出 匹配到异常的（- 能够获取mysql数据类型，但是是会带varchar(255)的长度类型信息- 索引信息和列信息不在一个结构里面