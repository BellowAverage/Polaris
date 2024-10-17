
--- 
title:  MyBatis的xml中日期的使用 
tags: []
categories: [] 

---
日期常用函数：DATE_FORMAT(date,format)，date 参数是合法的日期，format 规定日期/时间的输出格式。

相关格式：
|格式|描述
|%a|缩写星期名
|%b|缩写月名
|%c|月，数值
|%D|带有英文前缀的月中的天
|%d|月的天，数值(00-31)
|%e|月的天，数值(0-31)
|%f|微秒
|%H|小时 (00-23)
|%h|小时 (01-12)
|%I|小时 (01-12)
|%i|分钟，数值(00-59)
|%j|年的天 (001-366)
|%k|小时 (0-23)
|%l|小时 (1-12)
|%M|月名
|%m|月，数值(00-12)
|%p|AM 或 PM
|%r|时间，12-小时（hh:mm:ss AM 或 PM）
|%S|秒(00-59)
|%s|秒(00-59)
|%T|时间, 24-小时 (hh:mm:ss)
|%U|周 (00-53) 星期日是一周的第一天
|%u|周 (00-53) 星期一是一周的第一天
|%V|周 (01-53) 星期日是一周的第一天，与 %X 使用
|%v|周 (01-53) 星期一是一周的第一天，与 %x 使用
|%W|星期名
|%w|周的天 （0=星期日, 6=星期六）
|%X|年，其中的星期日是周的第一天，4 位，与 %V 使用
|%x|年，其中的星期一是周的第一天，4 位，与 %v 使用
|%Y|年，4 位
|%y|年，2 位

示例：

```
&lt;if test="start_time != null AND start_time != ''"&gt;
	&lt;![CDATA[ AND DATE_FORMAT(stime, '%Y-%m-%d %H:%i:%S') &gt;= DATE_FORMAT(#{<!-- -->start_time}, '%Y-%m-%d %H:%i:%S') ]]&gt;
&lt;/if&gt;
&lt;![CDATA[ AND DATE_FORMAT(etime, '%Y-%m-%d %H:%i:%S') &gt;= DATE_FORMAT(NOW(), '%Y-%m-%d %H:%i:%S') ]]&gt;

```
