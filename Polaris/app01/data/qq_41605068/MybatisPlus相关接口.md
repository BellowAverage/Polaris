
--- 
title:  MybatisPlus相关接口 
tags: []
categories: [] 

---
```
&lt;!--mybatis--&gt;
		&lt;dependency&gt;
			&lt;groupId&gt;com.baomidou&lt;/groupId&gt;
			&lt;artifactId&gt;mybatis-plus-boot-starter&lt;/artifactId&gt;
			&lt;version&gt;3.1.2&lt;/version&gt;
		&lt;/dependency&gt;
```



```
 /**
     * 分页插件
     */
    @Bean
    public PaginationInterceptor paginationInterceptor() {
        return new PaginationInterceptor();
    }
```

一、MybatisPlus

AUTO(0), // 数据库id自增

NONE(1), // 未设置主键

INPUT(2), // 手动输入

ID_WORKER(3), // 默认的方式,全局唯一id

UUID(4), // 全局唯一id uuid

ID_WORKER_STR(5); //ID_WORKER 字符串表示法



* AUTO：自动增长 *

ID_WORKER：mp自带策略，生成19位值，主键是数字类型时，使用这种策略 *

ID_WORKER_STR：mp自带策略，生成19位值，主键是String类型时，使用这种策略 *

INPUT：自己手动设置id *

NONE：手动设置 *

UUID：使用uuid随机生成唯一值

二、参数

<img alt="" src="https://img-blog.csdnimg.cn/20200715091728928.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxMjA3OTE3,size_16,color_FFFFFF,t_70">

>  
 原符号       &lt;        &lt;=      &gt;       &gt;=       &amp;        '        " 替换符号    &amp;lt;    &amp;lt;=   &amp;gt;    &amp;gt;=   &amp;amp;   &amp;apos;  &amp;quot; 


四、

QueryWrapper&lt;User&gt; wrapper = new QueryWrapper&lt;&gt;();

五、模糊查询

```
Wrappers.&lt;KnowType&gt;lambdaQuery().like(KnowType::getName,name)
```

六、IN查询

```
UpdateWrapper&lt;KnowType&gt; wrapper = Wrappers.update();
wrapper.in(KnowType.COL_PARENT_ID,ids);
```

七配置

```
spring.datasource.type=com.zaxxer.hikari.HikariDataSource
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url= jdbc:mysql://ip:3306/数据库名?allowMultiQueries=true&amp;characterEncoding=utf8&amp;characterEncoding=utf8&amp;zeroDateTimeBehavior=convertToNull&amp;useSSL=false&amp;useJDBCCompliantTimezoneShift=true&amp;useLegacyDatetimeCode=false&amp;serverTimezone=Asia/Shanghai
spring.datasource.username=账号
spring.datasource.password=密码
spring.datasource.hikari.maximum-pool-size=12
spring.datasource.hikari.connection-timeout=200000
spring.datasource.hikari.minimum-idle=10
spring.datasource.hikari.idle-timeout=500000
spring.datasource.hikari.max-lifetime=540000

swagger.title=知识库管理服务接口文档
swagger.description=知识库服务接口文档
swagger.base-package=com.shiyou.kbm.controller

#对以下URL进行放行，不拦截



spring.main.allow-bean-definition-overriding=true
security.oauth2.client.client-id=development
security.oauth2.client.client-secret=development
security.oauth2.client.scope=server


#热部署
spring.devtools.restart.enabled= true  
# 配置mapper的扫描，找到所有的mapper.xml映射文件
mybatis-plus.mapper-locations= classpath*:mapper/*Mapper.xml 
mybatis-plus.global-config.banner= false


# 全局映射器启用缓存
mybatis-plus.configuration.cache-enabled=true
# 查询时，关闭关联对象即时加载以提高性能
mybatis-plus.configuration.lazy-loading-enabled=false
#对于未知的SQL查询，允许返回不同的结果集以达到通用的效果
mybatis-plus.configuration.multiple-result-sets-enabled=true
#许使用列标签代替列名
mybatis-plus.configuration.use-column-label=true
#不允许使用自定义的主键值(比如由程序生成的UUID 32位编码作为键值)，数据表的PK生成策略将被覆盖
mybatis-plus.configuration.use-generated-keys=false
#给予被嵌套的resultMap以字段-属性的映射支持 FULL,PARTIAL
mybatis-plus.configuration.auto-mapping-behavior=PARTIAL
#配置默认的执行器。SIMPLE 执行器没有什么特别之处。REUSE 执行器重用预处理语句。BATCH 执行器重用语句和批量更新
mybatis-plus.configuration.default-executor-type=REUSE
#不更新值为null
mybatis-plus.global-config.db-config.field-strategy=not_null
#全局唯一ID
mybatis-plus.global-config.db-config.id-type=NONE
#Allows using RowBounds on nested statements
mybatis-plus.configuration.safe-row-bounds-enabled=false
#Enables automatic mapping from classic database column names A_COLUMN 
#			to camel case classic Java property names aColumn. 
mybatis-plus.configuration.map-underscore-to-camel-case=true
#MyBatis uses local cache to prevent circular references and speed 
#			up repeated nested queries. By default (SESSION) all queries executed during 
#			a session are cached. If localCacheScope=STATEMENT local session will be 
#			used just for statement execution, no data will be shared between two different 
#			calls to the same SqlSession.
mybatis-plus.configuration.local-cache-scope=SESSION
#Specifies the JDBC type for null values when no specific JDBC type 
#			was provided for the parameter. Some drivers require specifying the column 
#			JDBC type but others work with generic values like NULL, VARCHAR or OTHER.
mybatis-plus.configuration.jdbc-type-for-null=OTHER
#Specifies which Object's methods trigger a lazy load 
mybatis-plus.configuration.lazy-load-trigger-methods=equals,clone,hashCode,toString
#设置关联对象加载的形态，此处为按需加载字段(加载字段由SQL指 定)，不会加载关联表的所有字段，以提高性能 
mybatis-plus.configuration.aggressive-lazy-loading=true
mybatis-plus.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl
#mybatis分页查询
pagehelper.helper-dialect=mysql
```

```
&lt;resultMap id="userMap" type="xxx.entity.User"&gt;
        &lt;id column="id" property="id"/&gt;
        &lt;result column="username" property="username"/&gt;
        &lt;result column="password" property="password"/&gt;
        &lt;result column="nick_name" property="nickName"/&gt;
        &lt;result column="real_name" property="realName"/&gt;
        &lt;result column="avatar" property="avatar"/&gt;
        &lt;result column="sex" property="sex"/&gt;
        &lt;result column="phone" property="phone"/&gt;
        &lt;result column="email" property="email"/&gt;
        &lt;result column="state" property="state"/&gt;
        &lt;result column="create_date" property="createDate"/&gt;
        &lt;result column="update_date" property="updateDate"/&gt;
        &lt;result column="company_id" property="companyId"/&gt;
        &lt;result column="company_name" property="companyName"/&gt;
        &lt;result column="office_id" property="officeId"/&gt;
        &lt;result column="office_name" property="officeName"/&gt;

        &lt;collection property="roles" ofType="xxx.entity.Role"
                    javaType="java.util.List" select="getRoleInfo" column="id"&gt;
&lt;!-- {cityId=city_id,adr=addressCol, dis=districtCol}--&gt;
        &lt;/collection&gt;
    &lt;/resultMap&gt;

    &lt;resultMap id="roles" type="xxx.entity.Role"&gt;
        &lt;id column="role_id" property="id"/&gt;
        &lt;result column="role_name" property="roleName"/&gt;
    &lt;/resultMap&gt;

&lt;select id="getRoleInfo" parameterType="java.lang.String" resultMap="roles"&gt;
        select b.role_id, c.role_name
        from user_role b
        join role c on (b.role_id = c.id)
        where b.user_id = #{id}
&lt;/select&gt;
    
&lt;select id="listByPage" resultMap="userMap" parameterType="xxx.ReqParam"&gt;
        select a.*
        from user a
        &lt;trim prefix="WHERE" prefixOverrides="AND|OR"&gt;
            &lt;if test="searchKey != null and searchKey != '' and searchValue != null and searchValue != ''"&gt;
                AND a.${searchKey} like concat('%',#{searchValue},'%')
            &lt;/if&gt;
        &lt;/trim&gt;
        order by a.create_date
&lt;/select&gt;

```






