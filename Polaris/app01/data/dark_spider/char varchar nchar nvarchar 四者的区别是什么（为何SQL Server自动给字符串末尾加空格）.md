
--- 
title:  char varchar nchar nvarchar 四者的区别是什么（为何SQL Server自动给字符串末尾加空格） 
tags: []
categories: [] 

---
##  

本着低碳的原则将几个变量声明为nchar，结果发现尾巴上每次都多一大串空格，C#中不得不多次Trim劳心费神易出错。上网一查原来四种字符串看似相近其实讲究很多，其中以本帖最为全面，特此转发。

原帖：

 

原帖很长排版有点散（从里到外都很欠“Trim”一下），看下面的整理吧：

 nchar(n)

 包含n个字符的固定长度Unicode字符数据。n的值必须介于1与4,000之间。存储大小为n字节的两倍。

 nchar在SQL-92中的同义词为national char和national character。

 nvarchar(n)

 包含n个字符的可变长度Unicode字符数据。

 n的值必须介于1与4,000之间。字节的存储大小是所输入字符个数的两倍。所输入的数据字符长度可以为零。

 nvarchar 在 SQL-92 中的同义词为 national char varying 和 national character varying。

 注释 如果没有在数据定义或变量声明语句中指定 n，则默认长度为 1。如果没有使用 CAST 函数指定 n，则默认长度为 30。

 如何使用nchar(n)和nvarchar(n)

 如果希望列中所有数据项的大小接近一致，则使用 nchar。如果希望列中数据项的大小差异很大，则使用 nvarchar。

 使用 nchar 或 nvarchar 的对象被赋予数据库的默认排序规则，除非使用 COLLATE 子句赋予特定的排序规则。

 SET ANSI_PADDING OFF 不适用于 nchar 或 nvarchar。SET ANSI_PADDING ON 永远适用于 nchar 和 nvarchar。 二、char 和 varchar 固定长度 (char) 或可变长度 (varchar) 字符数据类型。

 char[(n)]

 长度为 n 个字节的固定长度且非 Unicode 的字符数据。n 必须是一个介于 1 和 8,000 之间的数值。存储大小为 n 个字节。

 char 在 SQL-92 中的同义词为 character。

 varchar[(n)]

 长度为 n 个字节的可变长度且非 Unicode 的字符数据。n 必须是一个介于 1 和 8,000 之间的数值。存储大小为输入数据的字节的实际长度，而不是 n 个字节。

 所输入的数据字符长度可以为零。varchar 在 SQL-92 中的同义词为 char varying 或 character varying。

 注释 如果没有在数据定义或变量声明语句中指定 n，则默认长度为 1。如果没有使用 CAST 函数指定 n，则默认长度为 30。

 将为使用 char 或 varchar 的对象被指派数据库的默认排序规则，除非用 COLLATE 子句另外指派了特定的排序规则。该排序规则控制用于存储字符数据的代码页。

 支持多语言的站点应考虑使用 Unicode nchar 或 nvarchar 数据类型以尽量减少字符转换问题。

 如何使用 char 或 varchar

 如果希望列中的数据值大小接近一致，请使用 char。 如果希望列中的数据值大小显著不同，请使用 varchar。 如果执行 CREATE TABLE 或 ALTER TABLE 时 SET ANSI_PADDING 为 OFF，则一个定义为 NULL 的 char 列将被作为 varchar 处理。

 当排序规则代码页使用双字节字符时，存储大小仍然为 n 个字节。根据字符串的不同，n 个字节的存储大小可能小于 n 个字符。

  

理解了这些，就理解了为何SQL Server自动给字符串末尾加空格，因为他们被声明为char或nchar了。

注意即使修改成var类型，原来的空格也不会自动消失，需要手工删除。
