
--- 
title:  Mybatis Plus的使用个人笔记 
tags: []
categories: [] 

---
### 导包

```
&lt;!--mybatis-plus start--&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;com.baomidou&lt;/groupId&gt;
            &lt;artifactId&gt;mybatis-plus-boot-starter&lt;/artifactId&gt;
            &lt;version&gt;3.1.0&lt;/version&gt;
        &lt;/dependency&gt;

        &lt;!-- mybatis-plus自动模板引擎依赖 --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;com.baomidou&lt;/groupId&gt;
            &lt;artifactId&gt;mybatis-plus-generator&lt;/artifactId&gt;
            &lt;version&gt;3.1.0&lt;/version&gt;
        &lt;/dependency&gt;

        &lt;!-- mybatis-plus需要的模板引擎freemarker --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.freemarker&lt;/groupId&gt;
            &lt;artifactId&gt;freemarker&lt;/artifactId&gt;
        &lt;/dependency&gt;
        &lt;!--mybatis-plus end--&gt;

```

### yml配置

```
mybatis-plus:
  configuration:
    #配置返回数据库(column下划线命名&amp;&amp;返回java实体是驼峰命名)，自动匹配无需as（没开启这个，SQL需要写as： select user_id as userId）
    map-underscore-to-camel-case: true
    cache-enabled: false
    log-impl: org.apache.ibatis.logging.stdout.StdOutImpl #打印sql语句,调试用

```

### bean 配置

```
	/**
     * 分页插件
     */
    @Bean
    public PaginationInterceptor paginationInterceptor() {
        return new PaginationInterceptor();
    }
	/**
     * 格式化打印 sql
     */
    @Bean
    public PerformanceInterceptor performanceInterceptor() {
        PerformanceInterceptor performanceInterceptor = new PerformanceInterceptor();
        //格式化sql语句
        Properties properties = new Properties();
        properties.setProperty("format", "true");
        performanceInterceptor.setProperties(properties);
        return performanceInterceptor;
    }

```

### xml 编写大于等于，小于等于，出现报错的解决办法

>  
 由于在mybatis框架的xml中&lt;= , &gt;=解析会出现问题,编译报错,所以需要转译 


**第一种写法：** 原符号 `&lt; &lt;= &gt; &gt;= &amp; ’ "` 替换符号 `&amp;lt; &amp;lt;= &amp;gt; &amp;gt;= &amp;amp; &amp;apos; &amp;quot;`

**详细表：**

|原符号|替换符号
|------
|&lt;|`&amp;lt;`
|&lt;=|`&amp;lt;=`
|&gt;=|`&amp;gt;=`
|&amp;|`&amp;amp;`
|’|`&amp;apos;`
|"|`&amp;quot;`

例如：sql如下：

```
unix_timestamp(target.mc_end_date)&amp;lt;= unix_timestamp(#{<!-- -->MonthEndTime})；unix_timestamp(target.mc_start_date) &amp;gt;= unix_timestamp(#{<!-- -->MonthBeginTime})


```

**第二种写法：** 大于等于

```
&lt;![CDATA[ &gt;= ]]&gt;

```

小于等于

```
&lt;![CDATA[ &lt;= ]]&gt;

```

**例如：sql如下：**

```
mc_end_date &lt;![CDATA[ &gt;= ]]&gt; #{<!-- -->endTime} and  mc_start_date &lt;![CDATA[ &lt;= ]]&gt; #{<!-- -->startTime}


```

### 更新时，实体传空，如何让字段不被过滤，而直接更新为空呢

>  
 可以使用以下注解，使其跳过空校验，让其传入什么参数就更新为什么参数 


```
@TableField(strategy = FieldStrategy.IGNORED)
private Long approvalTime;

```
