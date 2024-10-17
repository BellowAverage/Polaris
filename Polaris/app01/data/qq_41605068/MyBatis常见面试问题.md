
--- 
title:  MyBatis常见面试问题 
tags: []
categories: [] 

---
#### 一、**JDBC编程有哪些不足之处，Mybatis是如何解决这些问题的？**

1） 数据库连接的创建、释放频繁造成系统资源浪费从而影响了性能，如果使用数据库连接池就可以解决这个问题。当然JDBC同样能够使用数据源。 解决：在xml中配置数据连接池，使用数据库连接池管理数据库连接。

2） SQL语句在写代码中不容易维护，事件需求中SQL变化的可能性很大，SQL变动需要改变JAVA代码。

解决：将SQL语句配置在mapper.xml文件中与java代码分离。

3） 向SQL语句传递参数麻烦，因为SQL语句的where条件不一定，可能多，也可能少，占位符需要和参数一一对应。

解决：Mybatis自动将java对象映射到sql语句。

4） 对结果集解析麻烦，sql变化导致解析代码变化，且解析前需要遍历，如果能将数据库记录封装成pojo对象解析比较方便。

解决：Mbatis自动将SQL执行结果映射到java对象。

#### 二、**Mybatis编程步骤 ？**

Step1：创建SQLSessionFactory

Step2：通过SQLSessionFactory创建SQLSession

Step3：通过SQLSession执行数据库操作

Step4：调用session.commit()提交事物

Step5：调用session.close()关闭会话

#### 三、** MyBatis与hibernate有哪些不同 ？**

1）Mybatis MyBatis 是支持定制化 SQL、存储过程以及高级映射的一种持久层框架。MyBatis 避免了几乎所有的 JDBC 代码和手动设置参数以及获取结果集。Mybatis它不完全是一个ORM(对象关系映射)框架；它需要程序员自己编写部分SQL语句。 mybatis可以通过xml或者注解的方式灵活的配置要运行的SQL语句，并将java对象和SQL语句映射生成最终的执行的SQL，最后将SQL执行的结果在映射生成java对象。

Mybatis程序员可以直接的编写原生态的SQL语句，可以控制SQL执行性能，灵活度高，适合软件需求变换频繁的企业。

缺点：Mybatis无法做到数据库无关性，如果需要实现支持多种数据库的软件，则需要自定义多套SQL映射文件，工作量大。

2）Hibernate是支持定制化 SQL、存储过程以及高级映射的一种持久层框架。 Hibernate对象-关系映射能力强，数据库的无关性好，Hirberate可以自动生成SQL语句，对于关系模型要求高的软件，如果用HIrbernate开发可以节省很多时间。

#### 四、**使用Mybatis的mapper接口调用时候有哪些要求？**

1) Mapper接口方法名和Mapper.xml中定义的每个SQL的id相同；

2) Mapper接口方法的输入参数类型和mapper.xml中定义的每个sql标签parameterType类型相同

3) Mapper接口方法的输出参数类型和mapper.xml中定义的每个sql的resultType的类型相同

4) Mapper.xml文件中的namespace，就是接口的类路径。

#### 五、**MyBatis_Config.xml中配置有哪些内容？**

properties（属性） settings（配置） typeAliases（类型别名） typeHandlers（类型处理器） objectFactory（对象工厂） plugins（插件） environments（环境集合属性对象） environment（环境子属性对象） transactionManager（事务管理） dataSource（数据源） mappers（映射器）

#### 六、** Mybatis的一级缓存和二级缓存？**

1)一级缓存。是指SQLSession，MyBatis默认开启一级缓存，一级缓存只是相对于同一个SqlSession而言，在同一个SqlSession中，执行相同的SQL查询时；第一次会去查询数据库，并写在缓存中，第二次会直接从缓存中取。 当执行SQL时候两次查询中间发生了增删改的操作，则SQLSession的缓存会被清空。 每次查询会先去缓存中找，如果找不到，再去数据库查询，然后把结果写到缓存中。 Mybatis的内部缓存使用一个HashMap，key为hashcode+statementId+sql语句。Value为查询出来的结果集映射成的java对象。 SqlSession执行insert、update、delete等操作commit后会清空该SQLSession缓存。

在一级缓存中有几个细节应该注意一下：

**一级缓存的生命周期？**

a、MyBatis在开启一个数据库会话时，会 创建一个新的SqlSession对象，SqlSession对象中会有一个新的Executor对象。Executor对象中持有一个新的PerpetualCache对象；当会话结束时，SqlSession对象及其内部的Executor对象还有PerpetualCache对象也一并释放掉。

b、如果SqlSession调用了close()方法，会释放掉一级缓存PerpetualCache对象，一级缓存将不可用。

c、如果SqlSession调用了clearCache()，会清空PerpetualCache对象中的数据，但是该对象仍可使用。

d、SqlSession中执行了任何一个修改操作(update()、delete()、insert()) ，都会清空PerpetualCache对象的数据，但是该对象可以继续使用。

**怎么判断某两次查询是完全相同的查询？**

statementId、sql语句

2）二级缓存。是mapper级别的，开启二级缓存是需要手动配置的。 第一次调用mapper下的SQL去查询用户的信息，查询到的信息会存放代该mapper对应的二级缓存区域。 当第二次调用namespace下的mapper映射文件时，用相同的sql去查询用户信息时，会去对应的二级缓存内取结果。 如果调用相同namespace下的mapepr映射文件中增删改sql，并执行了commit操作，都会清空该mapper下的二级缓存区域。

实现二级缓存的时候，MyBatis要求返回的POJO必须是可序列化的。 也就是要求实现Serializable接口，配置方法很简单，只需要在映射XML文件配置就可以开启缓存了&lt;cache/&gt;，如果我们配置了二级缓存就意味着：
- 映射语句文件中的所有select语句将会被缓存。- 映射语句文件中的所欲insert、update和delete语句会刷新缓存。- 缓存会使用默认的Least Recently Used（LRU，最近最少使用的）算法来收回。- 根据时间表，比如No Flush Interval,（CNFI没有刷新间隔），缓存不会以任何时间顺序来刷新。- 缓存会存储列表集合或对象(无论查询方法返回什么)的1024个引用- 缓存会被视为是read/write(可读/可写)的缓存，意味着对象检索不是共享的，而且可以安全的被调用者修改，不干扰其他调用者或线程所做的潜在修改。
#### 七、**Mybatis的映射文件 ？**

Mybatis 真正强大的在于它的映射文件，它和JDBC代码进行比较，可以省掉95%的代码，Mybatis就是针对SQL进行构建。 SQL映射文件中几个顶级的元素：

• cache – 给定命名空间的缓存配置。

• cache-ref – 其他命名空间缓存配置的引用。

• resultMap – 是最复杂也是最强大的元素，用来描述如何从数据库结果集中来加载对象。

• sql – 可被其他语句引用的可重用语句块。

• insert – 映射插入语句

• update – 映射更新语句

• delete – 映射删除语句

• select – 映射查询语句

#### 八、** Mybatis动态SQL？**

1) 传统的JDBC的方法，在组合SQL语句的时候需要去拼接，稍微不注意就会少少了一个空格，标点符号，都会导致系统错误。Mybatis的动态SQL就是为了解决这种问题而产生的；Mybatis的动态SQL语句值基于OGNL表达式的，方便在SQL语句中实现某些逻辑；可以使用标签组合成灵活的sql语句，提供开发的效率。

2) Mybatis的动态SQL标签主要由以下几类： If语句（简单的条件判断） Choose(when/otherwise),相当于java语言中的switch，与jstl中choose类似 Trim(对包含的内容加上prefix，或者suffix) Where(主要是用来简化SQL语句中where条件判断，能智能的处理and/or 不用担心多余的语法导致的错误) Set(主要用于更新时候) Foreach(一般使用在mybatis in语句查询时特别有用)

#### 九、**Mybatis 分页查询？**

Mybatis本身有分页查询，但是并不是正真的分页查询，它是把数据查出来放在内存里面，你想要什么就给你什么。

我们使用Mybatis实现分页查询的时候，是要实现真分页查询，就是要用sql语句来实现分页查询。

MySQL和Oracle两种数据库的实现方法是不一样的。

Mysql：select * from table limit N , M; 其中：N表示从第几页开始，M表示每页显示的条数。

比如：数据库中有30条数据，要求每页显示10条，显示第2页的所有数据。 SQL语句就可以写成：Limit 10 , 20;

Oracle实现分页查询：采用伪列ROWNUM

#### 十、**Mybais 常用注解 ？**

@Insert ： 插入sql , 和xml insert sql语法完全一样

@Select ： 查询sql, 和xml select sql语法完全一样

@Update ： 更新sql, 和xml update sql语法完全一样

@Delete ： 删除sql, 和xml delete sql语法完全一样

@Param ： 入参

@Results ：结果集合

@Result ： 结果
