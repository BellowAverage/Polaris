
--- 
title:  slf4j日志框架的使用 
tags: []
categories: [] 

---
 一个完整的软件，日志是必不可少的。程序从开发、测试、维护、运行等环节，都需要向控制台或文件等位置输出大量信息。这些信息的输出，在很多时候是使用System.our.println()无法完成的。

Log4j全称为Log for java ,日志信息根据用途与记录内容不同，分为调试日志、运行日志、异常日志等。

## 一、日志的级别

日志级别由高到底，fatal(致命的)、error、warn、infor、debug、trace(堆栈)

建议使用四种：DEBUG,INFO,WARN,ERROR

为什么要对日志进行分级呢？

无论是将日志输出到控制台，还是文件，其输出都会降低程序的运行效率。但由于调试、运行维护的需要，客户的需求等原因，需要进行必要的日志输出。这时候必须要在代码中加入日志输出语句。

## 二、格式

```
%p：输出日志信息的优先级，即DEBUG，INFO，WARN，ERROR，FATAL。
%d：输出日志时间点的日期或时间，默认格式为ISO8601，也可以在其后指定格式，如：%d{yyyy/MM/dd HH:mm:ss,SSS}。
%r：输出自应用程序启动到输出该log信息耗费的毫秒数。
%t：输出产生该日志事件的线程名。
%l：输出日志事件的发生位置，相当于%c.%M(%F:%L)的组合，包括类全名、方法、文件名以及在代码中的行数。例如：test.TestLog4j.main(TestLog4j.java:10)。
%c：输出日志信息所属的类目，通常就是所在类的全名。
%M：输出产生日志信息的方法名。
%F：输出日志消息产生时所在的文件名称。
%L:：输出代码中的行号。
%m:：输出代码中指定的具体日志信息。
%n：输出一个回车换行符，Windows平台为"/r/n"，Unix平台为"/n"。
%x：输出和当前线程相关联的NDC(嵌套诊断环境)，尤其用到像java servlets这样的多客户多线程的应用中。
%%：输出一个"%"字符。
另外，还可以在%与格式字符之间加上修饰符来控制其最小长度、最大长度、和文本的对齐方式。如：
%20c：指定输出category的名称，最小的长度是20，如果category的名称长度小于20的话，默认的情况下右对齐。
%-20c："-"号表示左对齐。
%.30c：指定输出category的名称，最大的长度是30，如果category的名称长度大于30的话，就会将左边多出的字符截掉，但小于30的话也不会补空格。
```

## 三、Java工程

### 3.1添加配置文件 log4j.properties

<img alt="" class="has" height="137" src="https://img-blog.csdnimg.cn/20190717232853130.png" width="300">

```
#指定输出信息的级别--以及输出的位置
log4j.rootLogger=DEBUG,console，logFile
#表示Logger不会在父Logger的appender里输出，默认为true
log4j.additivity.org.apache=true

#控制台
log4j.appender.console=org.apache.log4j.ConsoleAppender
log4j.appender.console.layout=org.apache.log4j.PatternLayout
log4j.appender.console.ImmediateFlush=true
log4j.appender.console.Target=System.err
log4j.appender.console.layout.ConversionPattern=[%-5p] %d{yyyy-MM-dd HH:mm:ss} %c.%M(%F:%L) %m%n

#日志文件
log4j.appender.logFile=org.apache.log4j.FileAppender
log4j.appender.logFile.Threshold=DEBUG
log4j.appender.logFile.ImmediateFlush=true
log4j.appender.logFile.Append=true
log4j.appender.logFile.File=E:/logs_wmx/log.log4j
log4j.appender.logFile.layout=org.apache.log4j.PatternLayout
log4j.appender.logFile.layout.ConversionPattern=[%-5p] %d(%r) --&gt; [%t] %l: %m %x %n
```

### 3.2.添加依赖

```
&lt;!-- https://mvnrepository.com/artifact/org.slf4j/slf4j-api --&gt;
    &lt;dependency&gt;
      &lt;groupId&gt;org.slf4j&lt;/groupId&gt;
      &lt;artifactId&gt;slf4j-api&lt;/artifactId&gt;
      &lt;version&gt;1.7.25&lt;/version&gt;
    &lt;/dependency&gt;
&lt;!-- https://mvnrepository.com/artifact/org.slf4j/slf4j-log4j12 --&gt;
    &lt;dependency&gt;
      &lt;groupId&gt;org.slf4j&lt;/groupId&gt;
      &lt;artifactId&gt;slf4j-log4j12&lt;/artifactId&gt;
      &lt;version&gt;1.7.25&lt;/version&gt;
      &lt;!--&lt;scope&gt;test&lt;/scope&gt;--&gt;
    &lt;/dependency&gt;
&lt;!--
执行时出现报错信息:
    SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
    SLF4J: Defaulting to no-operation (NOP) logger implementation
    SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
解决方法:
    1.将类型&lt;scope&gt;test去掉
    2.将类型改为&lt;scope&gt;compile
    3.依赖的版本号要匹配
--&gt;


   
```

### 3.3日志记录

```
public class App 
{
    public static void main( String[] args ) {
        Logger logger = LoggerFactory.getLogger(App.class);
        logger.debug("This is debug!");
        logger.info("This is info");
        logger.warn("This is warn!");
        logger.error("This is error!");
    }
}
```

### 3.4执行结果

<img alt="" class="has" height="140" src="https://img-blog.csdnimg.cn/20190717232949768.png" width="786">

## 四、SSM框架使用slf4j

Mybatis内置的日志工厂提供日志功能，具体的日志实现有以下几种工具：

    SLF4J     Apache Commons Logging     Log4j 2     Log4j    JDK logging

具体选择哪个日志实现工具由MyBatis的内置日志工厂确定。它会使用最先找到的（按上文列举的顺序查找）。 如果一个都未找到，日志功能就会被禁用。当然，我们可以通过设置来确定使用哪个日志工具，具体配置如下：

### 1.mybatis-config.xml配置

```
&lt;configuration&gt;
    &lt;!-- 用于输出日志 SLF4J --&gt;
    &lt;settings&gt;  
        &lt;setting name="logImpl" value="SLF4J"/&gt;  
    &lt;/settings&gt;  
&lt;!-- 
logImpl可选的值有：SLF4J、LOG4J、LOG4J2、JDK_LOGGING、COMMONS_LOGGING、STDOUT_LOGGING、NO_LOGGING 或者是实现了接口org.apache.ibatis.logging.Log的类的完全限定类名， 并且这个类的构造函数需要是以一个字符串（String类型）为参数的。比如这个类为：
org.apache.ibatis.logging.LogFactory，那么在所有MyBatis方法之前调用以下方法：
org.apache.ibatis.logging.LogFactory.useSlf4jLogging();
org.apache.ibatis.logging.LogFactory.useLog4JLogging();
org.apache.ibatis.logging.LogFactory.useJdkLogging();
org.apache.ibatis.logging.LogFactory.useCommonsLogging();
org.apache.ibatis.logging.LogFactory.useStdOutLogging();
--&gt;
&lt;!-- configuration在配置文件中的位置必须符合要求，否则会报错，顺序如下:
        properties, 
        settings, 
        typeAliases, 
        typeHandlers, 
        objectFactory,
        objectWrapperFactory,
        plugins, 
        environments, 
        databaseIdProvider,
        mappers
 --&gt;
&lt;/configuration&gt;
```

### 2.web.xml配置

```
&lt;!-- 加载log4j --&gt;
    &lt;context-param&gt;
        &lt;param-name&gt;log4jConfigLocation&lt;/param-name&gt;
        &lt;param-value&gt;classpath:log4j.properties&lt;/param-value&gt;
    &lt;/context-param&gt;
    &lt;listener&gt;
        &lt;listener-class&gt;org.springframework.web.util.Log4jConfigListener&lt;/listener-class&gt;
    &lt;/listener&gt;


```

### 3.log4j.properties配置

```
#1.配置根logger,
##语法为:log4j.rootLogger=[level],appenderName,appenderName2,...
  ##level是日志记录的优先级低到高，分为OFF,TRACE,DEBUG,INFO,WARN,ERROR,FATAL,ALL  
  ##appenderName就是指定日志信息输出到哪个地方,可同时指定多个输出目的
##Log4j提供的appender有以下几种：
  ##--1)org.apache.log4j.ConsoleAppender(输出到控制台)
  ##--2)org.apache.log4j.FileAppender(输出到文件)
  ##--3)org.apache.log4j.DailyRollingFileAppender(每天产生一个日志文件)
  ##--4)org.apache.log4j.RollingFileAppender(文件大小到达指定尺寸的时候产生一个新的文件)
  ##--5)org.apache.log4j.WriterAppender(将日志信息以流格式发送到任意指定的地方)
##Log4j提供的layout有以下几种：
  ##--1)org.apache.log4j.HTMLLayout(以HTML表格形式布局)
       #属性：
       #LocationInfo=TRUE:默认值false,输出java文件名称和行号
       #Title=StrutsLogMessage:默认值Log4JLogMessages
  ##--2)org.apache.log4j.PatternLayout(可以灵活地指定布局模式)
       #属性:ConversionPattern=%m%n:格式化指定的消息(参数参考格式二)
  ##--3)org.apache.log4j.SimpleLayout(包含日志信息的级别和信息字符串)
  ##--4)org.apache.log4j.TTCCLayout(包含日志产生的时间、线程、类别等等信息)
  ##--5)org.apache.log4j.xml.XMLLayout(以XML形式布局)
       #属性:LocationInfo=TRUE:默认值false,输出java文件名称和行号

log4j.rootLogger=INFO,console,DB,logMail,logDailyFile,logFile,logRollingFile
##########    console(demo1),(输出到控制台)                      ##########
##########    DB(demo2),(登录到sql)                              ##########
##########    logMail(demo3),((发送email)                        ##########
##########    logDailyFile(demo4),(每天产生一个日志文件)           ##########
##########    logFile(demo5),(输出到文件)                         ##########
##########    logRollingFile(demo6),(到达指定文件大小生一个新的文件) ##########

#2.输出到控制台(demo1)--------------
  ##配置日志信息输出目的地Appender
log4j.appender.console=org.apache.log4j.ConsoleAppender
  ##默认值是true,所有的消息都会被立即输出
log4j.appender.console.ImmediateFlush=true
  ##默认值System.out,输出到控制台(err为红色,out为黑色)
log4j.appender.console.Target=System.err
  ##配置日志信息的格式(布局)PatternLayout
log4j.appender.console.layout=org.apache.log4j.PatternLayout
  ##参数格式
log4j.appender.console.layout.ConversionPattern=[%-5p] %d{yyyy-MM-dd HH:mm:ss} %c.%M(%F:%L) %m%n
  ##指定特定包的输出特定的级别
log4j.logger.org.springframework=DEBUG
    ##--mybatis显示SQL语句日志配置
log4j.logger.org.mybatis=DEBUG
log4j.logger.com.tchuhu.mapper=DEBUG
#3.显示sql语句配置--------------
log4j.logger.com.ibatis=DEBUG
#log4j.logger.com.ibatis.common.jdbc.SimpleDataSource=DEBUG
#log4j.logger.com.ibatis.common.jdbc.ScriptRunner=DEBUG
#log4j.logger.com.ibatis.sqlmap.engine.impl.SqlMapClientDelegate=DEBUG
#log4j.logger.java.sql.Connection=DEBUG
#log4j.logger.java.sql.Statement=DEBUG
#log4j.logger.java.sql.PreparedStatement=DEBUG
#4.将日志登录到MySQL数据库(demo2)------------
log4j.appender.DB=org.apache.log4j.jdbc.JDBCAppender
log4j.appender.DB.layout=org.apache.log4j.PatternLayout
log4j.appender.DB.Driver=com.mysql.jdbc.Driver
log4j.appender.DB.Threshold=DEBUG
    # 定义字符集防止中文乱码
log4j.appender.DB.encoding=UTF-8 
    #url
log4j.appender.DB.URL=jdbc:mysql://localhost:3306/ms
    #账户
log4j.appender.DB.User=root
    #密码
log4j.appender.DB.Password=root
log4j.appender.DB.Sql=INSERT INTO  ...........
     ##sql参数
      #  %p   输出优先级，即DEBUG，INFO，WARN，ERROR，FATAL
      #  %r   输出自应用启动到输出该log信息耗费的毫秒数
      #  %c   输出所属的类目，通常就是所在类的全名
      #  %t   输出产生该日志事件的线程名
      #  %n   输出一个回车换行符，Windows平台为“rn”，Unix平台为“n”
      #  %d   输出日志时间点的日期或时间，默认格式为ISO8601，也可以在其后指定格式，比如：%d{yyyMMMddHH:mm:ss,SSS}，输出类似：2002年10月18日22：10：28，921
      #  %l   输出日志事件的发生位置，包括类目名、发生的线程，以及在代码中的行数。举例：Testlog4.main(TestLog4.java:10)
     ##Table
    #DROP TABLE IF EXISTS `t_log4j`;
    #CREATE TABLE `t_log4j` (
            #  `log_id` int(11) NOT NULL AUTO_INCREMENT,
            #  `project_name` varchar(255) DEFAULT NULL COMMENT '目项名',
            #  `create_date` varchar(255) DEFAULT NULL COMMENT '创建时间',
            #  `level` varchar(255) DEFAULT NULL COMMENT '优先级',
            #  `category` varchar(255) DEFAULT NULL COMMENT '所在类的全名',
            #  `file_name` varchar(255) DEFAULT NULL COMMENT '输出日志消息产生时所在的文件名称 ',
            #  `thread_name` varchar(255) DEFAULT NULL COMMENT '日志事件的线程名',
            #  `line` varchar(255) DEFAULT NULL COMMENT '号行',
            #  `all_category` varchar(255) DEFAULT NULL COMMENT '日志事件的发生位置',
            #  `message` varchar(4000) DEFAULT NULL COMMENT '输出代码中指定的消息',
            #  PRIMARY KEY (`log_id`)
            #) ENGINE=InnoDB AUTO_INCREMENT=170 DEFAULT CHARSET=utf8;
#5.用Email发送日志(demo3)-----------------
log4j.appender.logMail=org.apache.log4j.net.SMTPAppender
log4j.appender.logMail.layout=org.apache.log4j.HTMLLayout
log4j.appender.logMail.layout.LocationInfo=TRUE
log4j.appender.logMail.layout.Title=MSMailLogFile
log4j.appender.logMail.Threshold=DEBUG
log4j.appender.logMail.SMTPDebug=FALSE
log4j.appender.logMail.SMTPHost=SMTP.163.com
log4j.appender.logMail.From=yaosiyuanmail@163.com
log4j.appender.logMail.To=yaosiyuanmail@gmail.com
log4j.appender.logMail.SMTPUsername=yaosiyuan
log4j.appender.logMail.SMTPPassword=1234567
log4j.appender.logMail.Subject=Log4jLogMessages
#log4j.appender.logMail.BufferSize=1024
#log4j.appender.logMail.SMTPAuth=TRUE
#6.每天产生一个日志文件(demo4)---------------------
log4j.appender.logDailyFile=org.apache.log4j.DailyRollingFileAppender
    #属性：
        #-- Threshold=WARN:指定日志消息的输出最低层次
        #-- ImmediateFlush=TRUE:默认值是true,所有的消息都会被立即输出
        #-- File=C:\log4j.log:指定消息输出到C:\log4j.log文件
        #-- Append=FALSE:默认值true,将消息追加到指定文件中，false指将消息覆盖指定的文件内容
        #-- DatePattern='.'yyyy-ww:每周滚动一次文件,即每周产生一个新的文件。还可以按用以下参数:
            #-- '.'yyyy-MM:每月
            #-- '.'yyyy-ww:每周
            #-- '.'yyyy-MM-dd:每天
            #-- '.'yyyy-MM-dd-a:每天两次
            #-- '.'yyyy-MM-dd-HH:每小时
            #-- '.'yyyy-MM-dd-HH-mm:每分钟
        #-Encoding=UTF-8:可以指定文件编码格式
log4j.appender.logDailyFile.layout=org.apache.log4j.PatternLayout
log4j.appender.logDailyFile.layout.ConversionPattern=[%-5p][%-22d{yyyy/MM/ddHH:mm:ssS}][%l]%n%m%n
log4j.appender.logDailyFile.Threshold=DEBUG
log4j.appender.logDailyFile.ImmediateFlush=TRUE
log4j.appender.logDailyFile.Append=TRUE
log4j.appender.logDailyFile.File=../WebRoot/log/DailyFile/Struts
log4j.appender.logDailyFile.DatePattern='.'yyyy-MM-dd-HH-mm'.log'
log4j.appender.logDailyFile.Encoding=UTF-8
#7.输出到文件(demo5)-------------
log4j.appender.logFile=org.apache.log4j.FileAppender
    ##属性
        #-- Threshold=INFO:指定日志消息的输出最低层次
        #-- ImmediateFlush=TRUE:默认值是true,所有的消息都会被立即输出
        #-- File=C:\log4j.log:指定消息输出到C:\log4j.log文件
        #-- Append=FALSE:默认值true,将消息追加到指定文件中，false指将消息覆盖指定的文件内容
        #-- Encoding=UTF-8:可以指定文件编码格式
log4j.appender.logFile.layout=org.apache.log4j.PatternLayout
log4j.appender.logFile.layout.ConversionPattern=[%-5p][%-22d{yyyy/MM/ddHH:mm:ssS}][%l]%n%m%n
log4j.appender.logFile.Threshold=DEBUG
log4j.appender.logFile.ImmediateFlush=TRUE
log4j.appender.logFile.Append=TRUE
log4j.appender.logFile.File=../WebRoot/log/File/log4j.log
log4j.appender.logFile.Encoding=UTF-8
#8.文件大小到达指定尺寸的时候产生一个新的文件(demo6)-------------
log4j.appender.logRollingFile=org.apache.log4j.RollingFileAppender
    #属性:
     #-- Threshold=ERROR:指定日志消息的输出最低层次
     #-- ImmediateFlush=TRUE:默认值是true,所有的消息都会被立即输出
     #-- File=C:/log4j.log:指定消息输出到C:/log4j.log文件
     #-- Append=FALSE:默认值true,将消息追加到指定文件中，false指将消息覆盖指定的文件内容
     #-- MaxFileSize=100KB:后缀可以是KB,MB,GB.在日志文件到达该大小时,将会自动滚动
     #-- MaxBackupIndex=2:指定可以产生的滚动文件的最大数
     #-- Encoding=UTF-8:可以指定文件编码格式
log4j.appender.logRollingFile.layout=org.apache.log4j.PatternLayout
log4j.appender.logRollingFile.layout.ConversionPattern=[%-5p][%-22d{yyyy/MM/ddHH:mm:ssS}][%l]%n%m%n
log4j.appender.logRollingFile.Threshold=DEBUG
log4j.appender.logRollingFile.ImmediateFlush=TRUE
log4j.appender.logRollingFile.Append=TRUE
log4j.appender.logRollingFile.File=../Struts2/WebRoot/log/RollingFile/log4j_Struts.log
log4j.appender.logRollingFile.MaxFileSize=1MB
log4j.appender.logRollingFile.MaxBackupIndex=10
log4j.appender.logRollingFile.Encoding=UTF-8
```

 
