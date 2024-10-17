
--- 
title:  MySQL MVCC工作原理 
tags: []
categories: [] 

---
        之前的文章中我们讲到，MySQL事务的隔离级别有四种分别是：read uncommitted、read committed、repeatable read和serializable。现在InnoDB下默认的存储引擎是repeatable read，之前也提过在repeatable read下MySQL是通过MVCC来实现可重复读。本文就介绍一下MVCC的原理。

###       MVCC定义

         MVCC(Multi-Version Concurrency Control),叫多版本并发控制，它是一个抽象概念而非具体实现，它通过给每行数据维护了一个版本链条控制，从而实现非阻塞的并发读。

###       MVCC原理

        要了解MVCC原理需要先了解当前读快照读的区别，还有undolog的作用，以及了解readview的结构。MVCC实现原理主要是依赖每行数据中记录了 3个隐式字段(DB_ROW_ID、DB_TRX_ID、DB_ROLL_PTR)，undo日志 ，Read View 来实现的。

####        当前读和快照读

        当前读：事务在修改该数据或对该数据加锁时这时的读就是当前读，它读取的是最新的版本数据，同时在读取时会对该记录加锁防止其他事务进行修改。因此对update、delete、select for update、select lock in share mode 这些操作都是当前读。

        快照读：它是一种不加锁的非阻塞读，它的前提不能是串行的隔离级别。它在读取时不会进行加锁操作，其他事务可能会对该记录进行修改，所以它读取的数据不一定是最新的版本数据。这种做法是为了提高并发读的性能。

####         undolog

        记录了当前事务修改记录的反操作记录，在事务中用于做回滚操作，它记录了不同事务对同一行记录修改的版本链条。

       <img alt="" height="955" src="https://img-blog.csdnimg.cn/0097a22a690e49dd981bf8a7ea65dafd.jpeg" width="919">

        undolog 分为insert undolog和update undolog。

        insert undo log是指在insert操作中产生的undo log。由于insert操作的记录，只是对本事务可见，其他事务不可见，所以undo log可以在事务提交后直接删除，而不需要purge操作。

        update undo log是指在delete和update操作中产生的undo log。该undo log会被后续用于MVCC当中，因此不能提交的时候删除。提交后会放入undo log的链表，等待purge线程进行最后的删除

####         3个隐式字段

        DB_ROW_ID：隐藏的主键如果没有设置主键则会自动生成。目前我们基本都会自己设置主键就不用这个字段。

        DB_TRX_ID：这是一个事务的全局变量，记录了该数据最新修改的事务ID。

        DB_ROLL_PTR：回滚指针，指向该行记录的上一个版本的地址，其指向的就是undo log的位置。

####         Read View

        Read View 就是事务进行快照读操作的时候生产的读视图 (Read View)。事务中对其他事务操作的可见性就是Read View来做的可见性判断。         Read View的记录了以下几个值：trx_list (当前活跃事务列表)、min_trx_id(活跃事务中最小事务ID)、max_trx_id(当前未分配的下一个事务ID)、creator_trx_id（快照读的当前事务ID）。

####         事务ID生成规则

        当一个事务开启的时候,并不会立刻生成事务id ,而是执行增删改的时候才会生成 id ,事务id=最大事务ID+1，同一个事务内的所有修改事务ID一致。

        当开启一个事务它的第一次执行动作时快照读时会给该事务生成一个很大的数，这个数的生成算法是把当前事务的 trx变量的指针地址转成整数再加上 2，这个事务ID是一个临时的事务ID，不会被记录在全局的trx_id中。

####         可见性判断算法

        1. DB_TRX_ID = creator_trx_id 如果成立则证明该事务修改在本事务中所以是可见的。

        2.DB_TRX_ID&lt;min_trx_id如果成立则能证明是在快照读时已经提交的事务是可以看到DB_TRX_ID的记录，不成立则进入下一步判断。

        3. DB_TRX_ID&gt;=max_trx_id如果成立则代表DB_TRX_ID的记录是在快照读生成后才出现,所以是看不到该事务记录，如果小于则进入下一步判断。

        4. 判断DB_TRX_ID in (trx_list) 如果在则说明快照读时该事务还在活跃中还未提交，因此是不可见的，如果不在则说明该事务已经提交了，那么对当前事务是可见的。

        当前DB_TRX_ID如果是不可见的则会根据undolog版本链条中找到前一条事务ID进行判断直到找到可见的那个版本数据。

####         可见性判断的模拟
<td style="background-color:#d9d9d9;border-color:#000000;text-align:center;vertical-align:middle;width:66pt;">时间</td><td style="background-color:#d9d9d9;border-color:#000000;text-align:center;vertical-align:middle;width:77.25pt;">事务A</td><td style="background-color:#d9d9d9;border-color:#000000;text-align:center;vertical-align:middle;width:77.25pt;">事务B</td><td style="background-color:#d9d9d9;border-color:#000000;text-align:center;vertical-align:middle;width:77.25pt;">事务C</td><td style="background-color:#d9d9d9;border-color:#000000;text-align:center;vertical-align:middle;width:77.25pt;">事务D</td><td style="background-color:#d9d9d9;border-color:#000000;text-align:center;vertical-align:middle;width:77.25pt;">事务E</td>
<td style="border-color:#000000;text-align:center;vertical-align:middle;">T1</td><td style="border-color:#000000;text-align:center;vertical-align:middle;">begin</td><td style="border-color:#000000;text-align:center;vertical-align:middle;">begin</td><td style="border-color:#000000;text-align:center;vertical-align:middle;">begin</td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td>
<td style="border-color:#000000;text-align:center;vertical-align:middle;">T2</td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td><td style="border-color:#000000;text-align:center;vertical-align:middle;width:77.25pt;">update trx_id = 1 commit</td><td style="border-color:#000000;text-align:center;vertical-align:middle;width:77.25pt;">update trx_id=2</td><td style="border-color:#000000;text-align:center;vertical-align:middle;">begin</td><td style="border-color:#000000;text-align:center;vertical-align:middle;">begin</td>
<td style="border-color:#000000;text-align:center;vertical-align:middle;">T3</td><td style="border-color:#000000;text-align:center;vertical-align:middle;">select1</td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td><td style="border-color:#000000;text-align:center;vertical-align:middle;width:77.25pt;">update trx_id=3</td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td>
<td style="border-color:#000000;text-align:center;vertical-align:middle;">T4</td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td><td style="border-color:#000000;text-align:center;vertical-align:middle;">commit</td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td><td style="border-color:#000000;text-align:center;vertical-align:middle;">select2</td>
<td style="border-color:#000000;text-align:center;vertical-align:middle;">T5</td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td><td style="border-color:#000000;text-align:center;vertical-align:middle;">commit</td><td style="border-color:#000000;text-align:center;vertical-align:middle;width:77.25pt;">update trx_id=4</td>
<td style="border-color:#000000;text-align:center;vertical-align:middle;">T6</td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td><td style="border-color:#000000;text-align:center;vertical-align:middle;">select3</td>
<td style="border-color:#000000;text-align:center;vertical-align:middle;">T7</td><td style="border-color:#000000;text-align:center;vertical-align:middle;">select4</td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td><td style="border-color:#000000;text-align:center;vertical-align:middle;"></td><td style="border-color:#000000;text-align:center;vertical-align:middle;">commit</td>

        上图中有5个事务在进行中，在7个时间节点里进行了不同的操作，这里记录下了每次快照读时的事务变化。

<img alt="" height="265" src="https://img-blog.csdnimg.cn/33c5248529b04b9b87d9748e9bff0bab.png" width="929">

**T3时间节点select1进行可见性判断：**

此时DB_TRX_ID=3

1. 判断creator_trx_id = DB_TRX_ID,发现不相等，证明该记录修改并非本事务的修改。进入下一步判断。

2. DB_TRX_ID&lt;min_trx_id, 3&lt;2不成立，证明该快照读产生时事务还未提交，所以不可见，进入下一步判断。

3. DB_TRX_ID&gt;=max_trx_id，3&gt;=4不成立 ，所以进入下一步判断。 4. 判断DB_TRX_ID in (trx_list) ,3 in (2,3) 说明生成快照读时该事务还在活跃中还未提交，因此是不可见的。

所以判断事务ID=3的记录对当前快照读不可见。

这时需要从undo log中去找下一个事务ID也就是 DB_TRX_ID=2,同样进行以上4个判断，发现也不可见。

再次继续找DB_TRX_ID=1进行判断，发现DB_TRX_ID=1,命中了条件2所以对1是可见的。因此查询出来的结果就是事务ID=1时修改结果。

**T4时间节点select2进行可见性判断：**

此时DB_TRX_ID=3

1. 判断creator_trx_id = DB_TRX_ID,发现不相等，证明该记录修改并非本事务的修改。进入下一步判断。

2. DB_TRX_ID&lt;min_trx_id, 3&lt;3不成立，证明该快照读产生时事务还未提交，所以不可见，进入下一步判断。

3. DB_TRX_ID&gt;=max_trx_id，3&gt;=4不成立 ，所以进入下一步判断。 4. 判断DB_TRX_ID in (trx_list) ,3 in (3) 说明生成快照读时该事务还在活跃中还未提交，因此是不可见的。

这时需要从undo log中去找下一个事务ID也就是 DB_TRX_ID=2,同样进行以上4个判断，发现命中了条件2，因此该快照读对DB_TRX_ID=2的记录时可见的。

**T6时间节点select3进行可见性判断：**

此时DB_TRX_ID=4，由于RR级别下readview 在第一次快照读就生成了所以下一次快照读时复制原readview 因此该快照读时的 tax_list、min_trx_id、max_trx_id这几个信息和T4是一致的。

1. 判断creator_trx_id = DB_TRX_ID, 4=4 成立则说明该记录是本事务修改的，因此是可见的。

**T7时间节点select4进行可见性判断：**

        此时DB_TRX_ID=4，由于RR级别下readview 在第一次快照读就生成了所以下一次快照读时复制原readview，因此该快照读时的 tax_list、min_trx_id、max_trx_id 这几个信息和T3是一致的。 最后进行判断发现其可见性和T3时刻的可见性也是一致的。

###         总结        

        MySQL MVCC的工作原理是依靠快照读生成Read View记录下当前活跃的事务ID,同时在本事务修改时也会将本事务的creator_trx_id记录在Read View中。最后通过和全局变量中的DB_TRX_ID进行比较判断其可见，如果当前事务ID不可见就从undo log中找到其上一次修改的记录再次进行判断直到找到满足条件的记录。

        RC隔离级别每次都读取最新的数据，因此它在同一事务中是可以读到其他事务修改并提交的记录。RR隔离级别在同一事务中只会在第一次快照读时生成Read View，第二次的快照读都是复制了第一次的Read View数据进行判断，因此它在两次读取的结果时一致的。

        MVCC也并不能解决幻读的问题，解决幻读的话需要借助锁机制来实现。
