
--- 
title:  Java 日志系列（二）：Java 日志使用中需要遵循的规范及注意事项 
tags: []
categories: [] 

---
在上一篇文章——中，笔者介绍了常用的日志框架，本文作为日志话题的延续，将结合具体案例介绍日志的使用。

### 1.日志的格式和级别

在使用日志框架的时候，可以根据应用的诉求在日志配置文件中去自定义日志打印格式和日志级别等信息。如下所示，为 logback.xml 配置样例，其中对配置文件中的关键信息做了解释，其它日志框架的使用示例将在下一部分介绍。

```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;configuration debug="false"&gt;
&lt;!--定义日志文件的存储地址 勿在 LogBack 的配置中使用相对路径--&gt;
&lt;property name="LOG_HOME" value="/home" /&gt;
&lt;!-- 控制台输出 --&gt;
&lt;appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender"&gt;
&lt;encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder"&gt;
&lt;!--格式化输出：%d 表示日期，%thread 表示线程名，%-5level：级别从左显示 5 个字符宽度，%msg：日志消息，%n 是换行符--&gt;
&lt;pattern&gt;%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{50} - %msg%n&lt;/pattern&gt;
&lt;/encoder&gt;
&lt;/appender&gt;
&lt;!-- 按照每天生成日志文件 --&gt;
&lt;appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender"&gt;
&lt;rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy"&gt;
&lt;!--日志文件输出的文件名--&gt;
&lt;FileNamePattern&gt;${LOG_HOME}/TestWeb.log.%d{yyyy-MM-dd}.log&lt;/FileNamePattern&gt;
&lt;!--日志文件保留天数--&gt;
&lt;MaxHistory&gt;30&lt;/MaxHistory&gt;
&lt;/rollingPolicy&gt;
&lt;encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder"&gt;
&lt;!-- 日志输出格式：%d 表示日期时间，%thread 表示线程名，%-5level：级别从左显示 5 个字符宽度 %logger{50} 表示 logger 名字最长 50 个字符，否则按照句点分割。 %msg：日志消息，%n 是换行符 --&gt;
&lt;pattern&gt;%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{50} - %msg%n&lt;/pattern&gt;
&lt;/encoder&gt;
&lt;!--日志文件最大的大小--&gt;
&lt;triggeringPolicy class="ch.qos.logback.core.rolling.SizeBasedTriggeringPolicy"&gt;
&lt;MaxFileSize&gt;10MB&lt;/MaxFileSize&gt;
&lt;/triggeringPolicy&gt;
&lt;/appender&gt;

&lt;!-- 日志输出级别 --&gt;
&lt;root level="INFO"&gt;
&lt;appender-ref ref="STDOUT" /&gt;
&lt;/root&gt;
&lt;/configuration&gt;

```

#### 1.1 日志命名和保持期限

在公开的阿里巴巴 java 开发手册中对日志规范也有相关介绍，在此，笔者介绍其中两条规范，即日志命名方式和日志保存期限。
- **日志命名方式：**
```
appName_logType_logName.log。

```

其中 appName 表示应用名；logType 表示日志类型，推荐分类有 stats，monitor，visit 等；logName 为日志描述，这种命名好处是可以快速清晰地了解日志文件类型和目的，便于归类查找。
- **日志保持期限：**
如何确定日志保持期限是个比较棘手的问题，如果日志存放时间过长，会消耗大量存储资源，甚至会导致磁盘压力过大影响系统稳定性；如果日志存放时间过短，可能导致日志数据“丢失”，出现问题时无法追溯。阿里 java 开发手册中对日志文件保存期限的建议是至少保存 15 天。在实际应用中，可以根据日志文件的重要程度、文件大小以及磁盘空间自行调整，此外，还可以对日志进行监控，定期转储。

#### 1.2 日志等级

通常，日志记录的优先级分为 OFF、FATAL、ERROR、WARN、INFO、DEBUG、ALL 或自定义的级别。Log4j 建议只使用四个级别，优先级从高到低分别是 ERROR、WARN、INFO、DEBUG。通过在日志框架的配置文件中设置日志级别，可以控制应用程序中相应级别的日志信息开关。比如配置为 INFO 级别，那么只有等于及高于这个级别的日志才进行处理，应用程序中所有 DEBUG 级别的日志信息不会被打印出来。需要说明的是，日志等级不仅关乎“详细程度”，还关系到适用场景、服务对象等。常见日志等级的说明如下：
- **ALL**：打印所有的日志。- **OFF**：关闭所有的日志输出。- **ERROR**：错误信息，包括错误的类型，错误的内容，位置和场景，是否可恢复等。只有当错误会影响到系统的正常运行时，才作为信息输出。- **WARN**：起到提醒作用，虽然应用程序目前运行正常，但存在隐含的风险。- **INFO**：记录系统的基本运行过程、运行状态、关键信息。- **DEBUG**：系统运行过程与状态的细节信息，可用于调试。- **TRACE**：系统结构与内容的细节信息，比如一些关键对象的内容，函数调用参数、结果等。
#### 1.3 日志格式

通过配置日志输出格式可以控制输出日志信息的内容和样式。以上面日志配置文件 logback.xml 为例，其中 pattern 标签定义了日志的输出格式，默认参数如下表格所示。

|参数|含义
|------
|%d|输出日志时间点的日期或时间，如：%d{yyyy-MM-dd HH:mm:ss.SSS}
|%thread|输出产生该日志事件的线程名
|%-5level|日志级别，从左显示 5 个字符宽度
|%msg|输出日志消息，即输出代码中指定的消息
|%n|输出一个回车换行符，Windows 平台为“\r\n”，Unix 平台为“\n”

除了上述默认的日志格式参数，Logback 还支持日志格式自定义配置，比如，希望每条日志能打印 ip 地址，实现方式如下：
- **step1：新建一个类 IPLogConfig，重写 convert 方法，实现 ip 获取。**
```
public class IPLogConfig extends ClassicConverter {<!-- -->
    @Override
    public String convert(ILoggingEvent event) {<!-- -->
        try {<!-- -->
            return InetAddress.getLocalHost().getHostAddress();
        } catch (UnknownHostException e) {<!-- -->
            e.printStackTrace();
        }
        return null;
    }
}

```
- **step2: 修改 logback.xml 配置。**
```
&lt;!--配置规则类的位置--&gt;
&lt;conversionRule conversionWord="ip" converterClass="com.test.conf.IPLogConfig" /&gt;
&lt;appender name="Console" class="ch.qos.logback.core.ConsoleAppender"&gt;
   &lt;layout&gt;
        &lt;pattern&gt;[ip=%ip] %d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{50} - %msg%n&lt;/pattern&gt;
   &lt;/layout&gt;
&lt;/appender&gt;

```

与 Logback 的日志输出格式配置相比，log4j 的输出格式配置有所不同，主要参数配置如下所示：

|参数|含义
|------
|%m|输出代码中指定的消息
|%p|输出优先级，即 DEBUG，INFO，WARN，ERROR，FATAL
|%r|输出自应用启动到输出该日志信息耗费的毫秒数
|%c|输出所属的类目，通常就是所在类的全名
|%t|输出产生该日志事件的线程名
|%n|输出一个回车换行符，Windows 平台为“\r\n”，Unix 平台为“\n”
|%d|输出日志时间点的日期或时间，默认格式为 ISO8601，也可以在其后指定格式，比如：%d{yy MMMM dd HH:mm:ss,SSS}
|%l|输出日志事件的发生位置，包括类目名、发生的线程，以及在代码中的行数
|%F|输出日志消息产生时所在的文件名称

### 2.日志使用注意事项

本节将结合例子介绍日志应用中需要注意的基础事项，如异常记录、对象实例记录、日志监控、日志分类等。

#### 2.1 异常日志如何记录

记录异常时一定要输出异常堆栈信息。如果没有完整的堆栈信息，那么一旦应用程序出现异常，维护人员将很难定位问题。示例：某应用对处理链路进行功能点的拆分，每个功能点的失败都会抛异常。在服务入口处对异常日志进行分类记录。

```
try {<!-- -->
        this.startOrderProcess(request, result, processName);
} catch (ProductBizException e) {<!-- -->
        if (CollectionUtils.isNotEmpty(e.getErrorMessages())) {<!-- -->
                e.getErrorMessages().forEach(errorMessage -&gt; {<!-- -->
                    log.error("biz process error" + e.getMessage(), e);
                });
        }
} catch (ProductSystemException ex) {<!-- -->
        log.error("system error" + ex.getMessage(), ex);
} catch (TMFRuntimeException e) {<!-- -->
        ErrorMessage errorMessage = e.getErrorMessage();
        if (null != errorMessage) {<!-- -->
                log.error("tmf runtime error" + e.getMessage(), e);
        }
}

```

#### 2.2 对象实例如何记录

日志中如果输出对象实例，要确保实例类重写了 toString 方法，否则只会输出对象的 hashCode 值，毫无意义。此外，也可以通过 java 反射来获取对应的属性。主要好处是当增加或修改属性的时候，不需要修改 toString 方法，通常采用 fastjson 将对象转换成 json 对象。

示例：在某项目中，有一处 debug 级别的日志信息需要记录服务调用方的请求参数，因此，对 ProductQueryRequest 对象实例重写了 toString 方法，以获取完整的对象信息。

```
// 采用 slf4j 中占位符输出形式记录 debug 信息
logger.debug("query request: {}", productQueryRequest);

// 其中 ProductQueryRequest 对象重写了 toString 方法
@Override
public String toString() {<!-- -->
        return "ProductQueryRequest{" +
            "queryOption=" + queryOption +
            ", productIds=" + productIds +
            ", MemberId=" + MemberId +
        '}';
}

```

#### 2.3 日志记录如何分类

日志分类建议从功能上分为监控日志、统计日志、访问日志。
- **监控日志**：这里的监控日志不包括统计信息，当然统计信息和访问信息均可以配置为监控信息。监控日志是开发人员需要重点关注的，因为监控日志直接关系到系统的稳定性和运维难度。典型的监控日志有请求入口和出口；外部服务调用和返回；资源消耗操作: 如读写文件等；容错行为: 如云硬盘的副本修复操作; 程序异常: 如数据库无法连接；后台操作: 定期执行删除的线程；启动、关闭、配置加载等。- **统计日志**：用户访问统计，如用户 IP，上传下载的数据量，请求 qps 情况，请求 rt 等。统计日志对格式需要严格要求，以便统计。实践中，应针对具体的日志分析平台来设计日志格式，便于对数据进行统计分析。- **访问日志**：该类日志一般在 nginx 层直接记录，如应用的 access.log，数据格式也基本统一。也可以使用相关日志分析平台来对访问日志进行统计分析。
#### 2.4 日志级别如何判断

在实践中，常用的日志级别有 debug、info、warn、error 四个级别，那么应如何具体判断日志的归属级别呢？
- **error**：记录较重要的错误信息(注：参数检查不通过这种不是 error)。通常情况下，exception 的出现均可以认为是 error 级别的。比如查询用户信息服务获取用户信息失败的，读取文件信息返回 IOException 的，功能模块执行异常的等。- **warn**：记录较重要的提示信息，如请求参数校验不通过、部分不重要的异常、非正常的条件分支(业务流程预期不符)、请求服务获取的结果为空的(潜在的风险)等。- **info**：记录可用于业务数据统计、监控、定位一般问题的信息，如系统状态变化日志，业务流程的核心处理、关键动作，业务流程的状态变化。- **debug**：记录调试信息，如 request/response。通常，在开发中和上线前期 debug 日志才会打开，随着系统稳定会关闭 debug 开关，只有当出现棘手的问题时才会根据需要开启。
#### 2.5 日志数据如何监控

通过对日志中的关键字进行监控，可以及时发现系统故障并报警，对系统运维至关重要。服务的监控和报警是一个很大的话题，本节只介绍日志监控报警需要注意的一些问题：
- **非必要，不报警**，只有需要运维马上处理的错误才需要发送报警。这样做的原因是避免长期的报警骚扰让运维人员对报警不再敏感，最后变成“狼来了”的故事；- **明确报警关键字**，例如用 ERROR 作为报警的关键字，而不是各种各样的复杂规则。这样做的原因是日志监控本质上是不断地进行字符串匹配操作，如果规则太多太复杂，就可能对线上服务产生影响；- **对于一些预警操作**，例如某个服务需要重试多次才能成功，或者某个用户的配额快用完等，可以通过每天一封报警邮件的方式来反馈；- **每一次系统出现故障**，都需要及时检查日志报警是否灵敏，日志报警的描述是否准确等，不断优化日志报警；
**监控配置规范**

|项目|规范
|------
|覆盖率|重大问题故障类、财务资损类、用户投诉类，监控通常须 100% 覆盖
|分层监控|监控内容要涵盖系统监控、JVM 监控、关键中间件监控、集群链路监控、依赖上下游业务监控、自身业务监控
|多维度分析|监控形式包括：线下和预发环境可以自动化跑全量业务监控、线上重要功能短周期定时单机监控、线上全量功能周期自动化执行监控、线上流量错误率等大盘分析指标实时监控、离线分析业务指标大盘监控
|误报率|监控配置后，要跟进数据结果合理设置预警，预警配置后要持续优化直到不再出现误报

#### 2.6 日志文件的大小

日志文件不宜过大，过大的日志文件会降低日志监控、问题定位的效率。因此需要进行日志文件的切分，具体而言，按天来分割还是按照小时分割，可以根据日志量来决定，原则就是方便开发或运维人员能快速查找日志。如下配置所示，日志文件大小定义为 20M，按天来做文件分割，并保留最近 15 天的数据。

```
&lt;rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy"&gt;
       &lt;fileNamePattern&gt;${LOG_FILE}.%d{yyyy-MM-dd}.%i.log&lt;/fileNamePattern&gt;
       &lt;maxHistory&gt;15&lt;/maxHistory&gt;
       &lt;maxFileSize&gt;20MB&lt;/maxFileSize&gt;
       &lt;totalSizeCap&gt;20GB&lt;/totalSizeCap&gt;
&lt;/rollingPolicy&gt;

```

为了防止日志文件将整个磁盘空间占满，需要定期对日志文件进行删除。例如，在收到磁盘报警时，可以将一周以前的日志文件删除或者转储。在实践中，日志转储/删除应实现自动化，当系统监控发现磁盘空间使用率超过设定的阈值时，便根据日志文件名标注的日期进行转储/删除。
