
--- 
title:  Redis持久化 RDB持久化、AOF持久化 
tags: []
categories: [] 

---
        Redis是基于内存，数据默认是在内存中操作，如果服务器重启内存的数据将会丢失，为了确保数据不丢失，Redis提供了2个不同形式的持久化方式。
-  RDB (Redis DataBase)-   AOF (Append Of File)
### 1. RDB持久化

        在指定的时间间隔内将内存中的数据快照存储到硬盘中。

#### 1.1 RDB持久化流程         <img alt="" src="https://img-blog.csdnimg.cn/59182ce1f11c4ad781ca05df5eb86723.jpeg">

         RDB持久化时会创建一个单独的fork子进程先将内存的数据进行压缩成一个临时文件中，然后再将临时文件替换上次持久化的文件。整个过程中，主进程是不进行任何IO操作的。这就确保了极高的性能。数据在写入时，父进程将原有的内存数据复制，等快照执行完成后将数据写入到原内存区域中。

#### 1.2 RDB的配置项

appendonly no //这个是aof的配置项，如果开启的话则使用aof持久化

stop-writes-on-bgsave-error  yes //默认为yes,保存数据失败，Redis是否停止接收数据

rdbcompression yes // 默认为yes 存储到磁盘中的快照，可以设置是否进行压缩存储

rdbchecksum yes //默认值是yes。在存储快照后是否使用CRC64算法来进行数据校验，这个功能会增加大约10%的性能消耗

dbfilename dump.rdb // 默认为dump.rdb 设置持久化文件的文件名

dir //设置持久化文件的存放路径

#### 1.3 RDB持久化的优劣势

优势：
- 是某个时间节点的数据集，节省磁盘空间，适合大规模的数据恢复- 在持久化时是在一个子进程中工作，主进程不需要进行任何磁盘IO操作- 恢复速度比 AOF 的恢复速度要快
劣势：
- 在持久化过程中数据被复制了一份会占有两倍的空间比较消耗性能- 它是在一定时间间隔内做持久化，所以如果在该时间间隔中出现宕机的话会有部分数据的丢失
### 2. AOF持久化

       通过日志的形式增量保存写操作的指令，只在文件后面追加，不修改原来文件。

#### 2.1 AOF持久化流程

<img alt="" src="https://img-blog.csdnimg.cn/94e5655929b64b7597c230bffd5093e4.jpeg">

        当有Redis执行命令发生时，会将执行命令追加到buffer中(AOF缓冲区)，缓冲区将执行命令同步追加到AOF文件中，当Redis服务器重启时，就会加载AOF文件进行数据恢复。由于AOF文件会越来越大，Redis也提供定期重写(rewrite)功能。

####  2.2 AOF配置项

appendonly yes //使用aof持久化

appendfilename appendonly.aof // 默认appendonly.aof 文件名称，路径跟rdb的一致

appendfsync [always、everysec、no] //缓冲区同步到AOF文件的执行策略
<td style="text-align:center;width:108px;">  always</td><td style="width:541px;">一直同步，每次写操作都会同步记录下来，这种操作比较频繁，性能较差，数据较完整</td>
<td style="text-align:center;width:108px;">everysec</td><td style="width:541px;">每秒同步一次，在同一秒内的数据可能会丢失</td>
<td style="text-align:center;width:108px;">no</td><td style="width:541px;">不主动同步，需要有操作系统或者客户端命令进行同步</td>

auto-aof-rewrite-min-size 64MB //设置文件达到最小值时重写

auto-aof-rewrite-percentage  //设置文件内容达到百分之几时重写

#### 2.3 AOF的优劣势

**优势**
- 数据丢失的概率更低- 有重写机制，有一定的容错率
**劣势**
- aof文件较大，需要占用更多的存储空间- 重启恢复时的速度较慢- 可能存在BUG
### 3. RDB和AOF如何选择
1. 官方建议两个都同时启用,不推荐单独使用AOF1. 如果数据不需要绝对的完整性可以只是用RDB1. 如果用户只做内存的缓存使用的话可以不需要持久化