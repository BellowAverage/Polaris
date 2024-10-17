
--- 
title:  [oracle]Oracle数据库转换NUMBER类型 
tags: []
categories: [] 

---
没有在oracle中找到unix时间戳转换为日期类型的函数，现做一个自定义函数备份。

```
create or replace function f_long2date(v_long NUMBER) return date is
begin
return v_long / (60 * 60 * 24) +
TO_DATE('1970-01-01 08:00:00',
'YYYY-MM-DD HH24:MI:SS');
end;

```

创建oracle转换时间戳为日期函数
