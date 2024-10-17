
--- 
title:  Redis事务 
tags: []
categories: [] 

---
## Redis事务

#### 基本事务指令

Redis提供了一定的事务支持，可以保证一组操作原子执行不被打断，但是如果执行中出现错误，事务不能回滚，Redis未提供回滚支持。
- `multi`开启事务- `exec`执行事务
```
127.0.0.1:6379&gt; multi
OK
127.0.0.1:6379&gt; set a 100
QUEUED
127.0.0.1:6379&gt; set b 200
QUEUED
127.0.0.1:6379&gt; get a
QUEUED
127.0.0.1:6379&gt; get b
QUEUED
127.0.0.1:6379&gt; exec
1) OK
2) OK
3) "100"
4) "200"

```

使用multi开启事务后，操作的指令并未立即执行，而是被redis记录在队列中，等待一起执行。当执行exec命令后，开始执行事务指令，最终得到每条指令的结果。

```
127.0.0.1:6379&gt; multi
OK
127.0.0.1:6379&gt; set c 300
QUEUED
127.0.0.1:6379&gt; hgetall a
QUEUED
127.0.0.1:6379&gt; set d 400
QUEUED
127.0.0.1:6379&gt; get d
QUEUED
127.0.0.1:6379&gt; exec
1) OK
2) (error) WRONGTYPE Operation against a key holding the wrong kind of value
3) OK
4) "400"
127.0.0.1:6379&gt;

```

如果事务中出现了错误，事务并不会终止执行，而是只会记录下这条错误的信息，并继续执行后面的指令。所以事务中出错不会影响后续指令的执行。

#### Python客户端操作

在Redis的Python 客户端库redis-py中，提供了pipeline (称为流水线 或 管道)，该工具的作用是：
- 在客户端统一收集操作指令- 补充上multi和exec指令，当作一个事务发送到redis服务器执行
```
from redis import StrictRedis
r = StrictRedis.from_url('redis://127.0.0.1:6381/0')
pl = r.pipeline()
pl.set('a', 100)
pl.set('b', 200)
pl.get('a')
pl.get('b')
ret = pl.execute()
print(ret) #  [True, True, b'100', b'200']

```

#### watch监视

若在构建的redis事务在执行时依赖某些值，可以使用watch对数据值进行监视。

```
127.0.0.1:6379&gt; set stock 100
OK
127.0.0.1:6379&gt; watch stock
OK
127.0.0.1:6379&gt; multi
OK
127.0.0.1:6379&gt; incrby stock -1
QUEUED
127.0.0.1:6379&gt; incr sales
QUEUED
127.0.0.1:6379&gt; exec
1) (integer) 99
2) (integer) 1

```

事务exec执行前被监视的stock值未变化，事务正确执行。

```
127.0.0.1:6379&gt; set stock 100
OK
127.0.0.1:6379&gt; watch stock
OK
127.0.0.1:6379&gt; multi
OK
127.0.0.1:6379&gt; incrby stock -1
QUEUED
127.0.0.1:6379&gt; incr sales
QUEUED

```

此时在另一个客户端修改stock的值，执行

```
127.0.0.1:6379&gt; incrby stock -2
(integer) 98

```

当第一个客户端再执行exec时

```
127.0.0.1:6379&gt; exec
(nil)

```

表明事务需要监视的stock值发生了变化，事务不能执行了。

**注意：Redis Cluster 集群不支持事务**
