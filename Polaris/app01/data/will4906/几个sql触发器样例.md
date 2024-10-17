
--- 
title:  几个sql触发器样例 
tags: []
categories: [] 

---
触发器虽然在sql标准中有支持，但是几个数据库仍然还是具有特殊的语法。笔者试着写了几个比较常用的触发器作为记录。

### DEMO

使用一下两个表作为触发器的使用示例
- test1(<u>a</u>, b, c, d)- test2(<u>a</u>, c, d)
#### Mysql
- insert
```
DROP TRIGGER IF EXISTS after_insert_trigger;
DELIMITER $
CREATE TRIGGER after_insert_trigger
AFTER INSERT ON test1
FOR EACH ROW
BEGIN
    INSERT INTO test2 VALUES(NEW.a, NEW.c, NEW.d);
END$
DELIMITER ;
```
- update
```
DROP TRIGGER IF EXISTS after_update_trigger;
DELIMITER $
CREATE TRIGGER after_update_trigger
AFTER UPDATE ON test1
FOR EACH ROW
BEGIN
    UPDATE test2 SET c = NEW.c, d = NEW.d WHERE test2.a = NEW.a;
END$
DELIMITER ;
```
- delete
```
DROP TRIGGER IF EXISTS after_delete_trigger;
DELIMITER $
CREATE TRIGGER after_delete_trigger
AFTER DELETE ON test1 
FOR EACH ROW 
BEGIN 
DELETE FROM test2 WHERE test2.a = OLD.a;
END$
DELIMITER ;
```


<li> 
 </li>- 这里AFTER 指在事件发生后执行，我们也可以使用BEFORE在事件发生之前执行触发器的动作。 


>  
 在事件之前被执行的触发器可以作为避免非法更新、插入或删除的额外约束。为了避免执行非法动作而产生错误，触发器可以采取措施来纠正问题，使更新、插入或删除合法化。[1]  


```
DROP TRIGGER IF EXISTS before_insert_trigger;
DELIMITER $
CREATE TRIGGER before_insert_trigger
BEFORE INSERT ON test1
FOR EACH ROW
BEGIN
  SET NEW.b = NEW.b + 1;
END$
DELIMITER ;
```
- DELIMITER  DELIMITER是用来定义分隔符的，由于BEGIN和END之中的多行执行语句需要’ ; ‘作为结尾，导致命令行提前以为语句书写结束，导致报错，需要使用DELIMITER定义临时分隔符，如’$’保证语句的正常执行。
#### Postgresql

postgresql对触发器的语法是比较特殊的，需要先定义执行函数，然后在出发器中使用`EXECUTE PROCEDURE`来处理执行的行为。

```
CREATE OR REPLACE FUNCTION after_insert_trigger()
RETURNS TRIGGER AS $$
BEGIN
INSERT INTO test2 VALUES(NEW.a, NEW.c, NEW.d);
RETURN NULL;
END;
$$
LANGUAGE plpgsql;
DROP TRIGGER IF EXISTS after_insert_trigger ON test1;
CREATE TRIGGER after_insert_trigger
    AFTER INSERT ON test1
    FOR EACH ROW EXECUTE PROCEDURE after_insert_trigger();
```

其他行为语法均与上面例子相似，笔者便不再赘述。

### 参考文献

[1] Abraham Silberschatz, Henry F.Korth S.Sudarshan. 数据库系统概念.杨冬青, 李红燕, 唐世渭等译. 北京. 机械工业出版社.2012.103-103.
<td align="center" colspan="2">赞赏</td>
<td align="center"> <img src="https://img-blog.csdn.net/20170521121423299?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" width="200px" alt="微信支付"> </td><td align="center"> <img src="https://img-blog.csdn.net/20170521131930503?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" width="200px" alt="支付宝"> </td>
<td align="center">微信</td><td align="center">支付宝</td>
