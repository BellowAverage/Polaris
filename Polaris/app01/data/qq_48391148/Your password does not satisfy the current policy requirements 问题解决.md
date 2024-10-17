
--- 
title:  Your password does not satisfy the current policy requirements 问题解决 
tags: []
categories: [] 

---
最近新入了一台云服务器，安装了mysql，新建用户的时候总是提示密码不符合规范

示例：

```
mysql&gt; create user zabbix@'%' identified by '123456';
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements
```

解决方法：

修改mysql里面关于密码复杂度的bianli变量

```
mysql&gt; show variables like 'validate_password%';
+--------------------------------------+--------+
| Variable_name                        | Value  |
+--------------------------------------+--------+
| validate_password_check_user_name    | OFF    |
| validate_password_dictionary_file    |        |
| validate_password_length             | 8      |
| validate_password_mixed_case_count   | 1      |
| validate_password_number_count       | 1      |
| validate_password_policy             | MEDIUM |
| validate_password_special_char_count | 1      |
+--------------------------------------+--------+
7 rows in set (0.01 sec)
```

将密码验证强度等级设置为低

```
mysql&gt; set global validate_password_policy=LOW;
Query OK, 0 rows affected (0.00 sec)
```

设置密码长度为6

```
mysql&gt; set global validate_password_length=6;
Query OK, 0 rows affected (0.00 sec)

mysql&gt; create user 'zabbix'@'%' identified by '123456';
Query OK, 0 rows affected (0.00 sec)
```

这样新建用户的时候，密码长度只要符合6位长度就ok
