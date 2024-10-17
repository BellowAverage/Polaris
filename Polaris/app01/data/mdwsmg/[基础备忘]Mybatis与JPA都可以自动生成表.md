
--- 
title:  [基础备忘]Mybatis与JPA都可以自动生成表 
tags: []
categories: [] 

---
使用Mybatis与JPA都可以自动生成表。<s>不过Mybatis-plus可以生成一套代码</s>

两者都可以通过注解定义实体类属性对应的数据表策略，下面对两者在实体类不同注解做备份。

### 1、Mybatis

常作用在BaseEntity上的字段注解。

|注解|属性
|------
|@TableId(value = “id”, type = IdType.AUTO)|value说明字段名，相同名称可以不写；type
|@TableField(fill = FieldFill.INSERT)|表字段标识,exist = false表示该属性不为数据库表字段，但又是必须使用的。fill = FieldFill.INSERT注解填充字段 ，生成器策略部分也可以配置
|@TableLogic|表逻辑处理注解（逻辑删除）

### 2、JPA

|注解|属性
|------
|@GeneratedValue|指定如何标识属性可以被初始化，如@GeneratedValue()。strategy = GenerationType.SEQUENCE：表示主键生成策略是sequence，还有Auto、ldentity、 Native等。generator = "repair_seq"声明了主键生成器的名称
|@GenericGenerator|自定义主键生成策略，由@GenericGenerator实现。name属性指定生成器名称。与@GeneratorValue中 generator 的值对应。strategy属性指定具体生成器的类名。parameters得到strategy指定的具体生成器所用到的参数
|@Column(name = “create_time”)|说明字段
|@ld|指定的类的属性，一个表中的主键。
|@Transient|标注的属性会被JPA所忽略，不会映射到数据库中，即程序运行后数据库中将不会有该字段。
|@Table|用来标识实体类与数据表的对应关系。
|@Entity|表明这个class是实体类，并且使用默认的orm规则，即class名即数据库表中表名，class字段名即表中的字段名。

### 3、自动建表的注意事项
- @MappedSuperclass **在创建实体类的父类时，使用JPA的BaseEntity需要添加@MappedSuperclass注解以适应多继承**，而Mybatis自动生成表所继承的BaseEntity不用这个注解。 @MappedSuperclass 用在父类上面。当这个类肯定是父类时，加此标注。如果改成@Entity，则继承后，多个类继承，只会生成一个表，而不是多个继承，生成多个表 对应报错:
>  
 No identifier specified for entity 

- @Temporal(TemporalType.TIMESTAMP) 当实体类的父类有**创建时间、更新时间等字段**时，可能会需要@Temproal()注解向数据库映射日期（Date）属性时用来调整映射的精度（实体类会封装成完整的时间“yyyy-MM-dd hh:MM:ss”）。 这里要注意的是，@Temproal注解与LocalDateTime类会发生冲突。应该使用Date类型 对应报错：
>  
 Caused by: org.hibernate.AnnotationException: @Temporal should only be set on a java.util.Date or java.util.Calendar property: 


使用@CreatedDate 配合 @DateTimeFormat(pattern=“yyyy-MM-dd HH:mm:ss”)其实也是一个很好的选择，而且很香。对应的类为Date，更新字段为@LastModifiedDate。这些注解都在org.springframework.data.annotation;包下。

但是**LocalDateTime类**也很香，继承了Temporal, TemporalAdjuster, ChronoLocalDateTime
