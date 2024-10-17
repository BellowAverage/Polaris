
--- 
title:  SpringBoot中使用Mybatis逆向工程（实体类含数据库注释） 
tags: []
categories: [] 

---
>  
 Mybatis逆向工程：根据创建好的数据库表，生成对应的实体类、DAO、映射文件 




#### 文章目录
- - - - 


## 开发环境
- 开发工具：IntelliJ IDEA 2021.3.3 (Ultimate Edition)- SpringBoot版本：2.5.12- mysql驱动依赖版本：5.1.47- mybatis逆向工程插件版本：1.3.5- 通用mapper依赖版本：4.1.5- JDK版本：1.8
 

## 1.新建SpringBoot应用
- 新建项目参考链接：
## 2.添加逆向工程插件依赖
- **添加Mybatis的maven插件，引入其他两个所需的依赖**
```
&lt;!-- 添加mybatis逆向工程插件 --&gt;
&lt;plugin&gt;
    &lt;groupId&gt;org.mybatis.generator&lt;/groupId&gt;
    &lt;artifactId&gt;mybatis-generator-maven-plugin&lt;/artifactId&gt;
    &lt;version&gt;1.3.5&lt;/version&gt;

    &lt;configuration&gt;
        &lt;!-- 获取配置文件路径 --&gt;
        &lt;configurationFile&gt;${basedir}/src/main/resources/generatorConfig.xml&lt;/configurationFile&gt;
        &lt;!-- 当生成的类已经存在时，是否覆盖 --&gt;
        &lt;overwrite&gt;true&lt;/overwrite&gt;
    &lt;/configuration&gt;

    &lt;!-- 添加mybatis逆向工程所需的依赖 --&gt;
    &lt;dependencies&gt;
        &lt;!-- 添加通用mysql驱动依赖 --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;mysql&lt;/groupId&gt;
            &lt;artifactId&gt;mysql-connector-java&lt;/artifactId&gt;
            &lt;version&gt;5.1.47&lt;/version&gt;
        &lt;/dependency&gt;

        &lt;!-- 添加通用Mapper依赖 --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;tk.mybatis&lt;/groupId&gt;
            &lt;artifactId&gt;mapper&lt;/artifactId&gt;
            &lt;version&gt;4.1.5&lt;/version&gt;
        &lt;/dependency&gt;
    &lt;/dependencies&gt;
&lt;/plugin&gt;

```
<li> **逆向工程配置文件** 
  <ul>- 在SpringBoot项目的`src/main/resources`文件夹下新建`generatorConfig.xml`配置文件(路径可改）
```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;!DOCTYPE generatorConfiguration PUBLIC
        "-//mybatis.org//DTD MyBatis Generator Configuration 1.0//EN"
        "http://mybatis.org/dtd/mybatis-generator-config_1_0.dtd"&gt;
&lt;generatorConfiguration&gt;
    &lt;context id="DB2Tables" targetRuntime="MyBatis3Simple" defaultModelType="flat"&gt;

        &lt;!-- 通用 Mapper 继承的接口 --&gt;
        &lt;plugin type="tk.mybatis.mapper.generator.MapperPlugin"&gt;
            &lt;property name="mappers" value="tk.mybatis.mapper.common.Mapper"/&gt;
        &lt;/plugin&gt;

        &lt;commentGenerator&gt;
            &lt;!-- 不生成时间戳 --&gt;
            &lt;property name="suppressDate" value="true"/&gt;
            &lt;!-- 生成注解 --&gt;
            &lt;property name="suppressAllComments" value="false"/&gt;
            &lt;!-- 注解采用数据库的标注，suppressAllComments 必须设置为 false 才会生效 --&gt;
            &lt;property name="addRemarkComments" value="true"/&gt;
        &lt;/commentGenerator&gt;

        &lt;!-- 数据库连接信息 --&gt;
        &lt;jdbcConnection driverClass="com.mysql.jdbc.Driver"
                        connectionURL="jdbc:mysql://localhost:3306/数据库名称?characterEncoding=utf8"
                        userId="数据库用户名"
                        password="数据库密码"&gt;
            &lt;!-- oracle 获取数据库注解的方式，想要获取数据库注解必须添加 --&gt;
            &lt;!-- &lt;property name="remarksReporting" value="true"/&gt; --&gt;
            &lt;!-- mysql 获取数据库注解的方式，想要获取数据库注解必须添加 --&gt;
            &lt;property name="useInformationSchema" value="true"/&gt;
            &lt;!-- 其它类型数据库暂不支持 --&gt;
        &lt;/jdbcConnection&gt;

        &lt;!-- 生成实体类位置 --&gt;
        &lt;javaModelGenerator targetPackage="com.example.tkmapper.demo.entity" targetProject="src/main/java"&gt;
            &lt;property name="enableSubPackages" value="true"/&gt;
            &lt;property name="trimStrings" value="true"/&gt;
        &lt;/javaModelGenerator&gt;

        &lt;!-- 生成的 xml 映射文件位置 --&gt;
        &lt;sqlMapGenerator targetPackage="/" targetProject="src/main/resources/mapper"&gt;
            &lt;property name="enableSubPackages" value="true"/&gt;
        &lt;/sqlMapGenerator&gt;

        &lt;!-- 生成 mapper 接口的位置 --&gt;
        &lt;javaClientGenerator type="XMLMAPPER" targetPackage="com.example.tkmapper.demo.dao" targetProject="src/main/java"&gt;
            &lt;property name="enableSubPackages" value="true"/&gt;
        &lt;/javaClientGenerator&gt;

        &lt;!-- 数据表 和 JAVA 实体的映射，tableName 表名，domainObjectName 实体名 --&gt;
        &lt;table tableName="users" domainObjectName="User" enableCountByExample="false" enableUpdateByExample="false"
               enableDeleteByExample="false" enableSelectByExample="false" selectByExampleQueryId="false"&gt;
        &lt;/table&gt;

        &lt;!-- 如果想要一次性生成所有表，可以把 tableName 配置为 %，一般不推荐这么干，开发项目的时候最好是要用到哪些表，才去生成 --&gt;
        &lt;!-- &lt;table tableName="%"/&gt; --&gt;
    &lt;/context&gt;
&lt;/generatorConfiguration&gt;

```

## 3.执行逆向生成

<img src="https://img-blog.csdnimg.cn/439b222ddbfc4f8da24ff04435e8df05.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">
