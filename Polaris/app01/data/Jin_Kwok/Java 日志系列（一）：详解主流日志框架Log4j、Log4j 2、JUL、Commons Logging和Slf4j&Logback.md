
--- 
title:  Java 日志系列（一）：详解主流日志框架Log4j、Log4j 2、JUL、Commons Logging和Slf4j&Logback 
tags: []
categories: [] 

---
### 引言

随着互联网和大数据的蓬勃发展，分布式日志系统以及日志分析系统得到了广泛地应用。目前，几乎在所有应用程序中，都会用到各种各样的日志框架来记录程序的运行信息。鉴于此，作为工程师，十分有必要熟悉主流的日志记录框架。

日志的有无虽然不影响应用程序的运行结果，但是没有日志的应用程序是不完整的，甚至可以说是有缺陷的。优雅的日志系统可以记录操作轨迹，监控系统运行状况以及回溯系统故障。在工作中，部分工程师对主流的日志框架仍然是一知半解，日常应用还停留在复制粘贴的层面，因此写作本文，希望对读者有所帮助。笔者将通过 3 篇文章全面系统地介绍 Java 日志框架，主要内容如下：
- 日志的意义与价值；- Java 日志框架进化史；- 日志门面与日志系统；- 日志框架的使用选择；- 日志使用中需要遵循的规范及注意事项；- 日志使用示例及常见报错。
本文为系列文章，分 3 篇，如下：
- Java 日志系列（一）：详解主流日志框架Log4j、Log4j 2、JUL、Commons Logging和Slf4j&amp;Logback- Java 日志系列（二）：Java 日志使用中需要遵循的规范及注意事项- Java 日志系列（三）：Java 日志使用示例及常见报错
### 1.日志的意义与价值
- **在开发调试阶段**: 日志系统有助于更快的定位问题。- **在应用运维阶段**: 日志系统有助于记录大部分的异常信息，通过收集日志信息可以对系统的运行状态进行实时监控预警。- **在数据分析阶段**: 日志中通常包含大量的用户数据，包括点击行为、兴趣偏好等，基于这些数据可以对用户进行“画像”，进而助力战略决策。随着大数据技术日渐成熟，海量日志分析已经在互联网公司得到广泛应用。
### 2.Java 日志框架进化史

在开发过程中，工程师不得不面对一个很现实的问题：Java “混乱”的日志框架体系。为什么说“混乱”呢？原因在于早期 Java 日志框架没有制定统一的标准，使得很多应用程序会同时使用多种日志框架。Java 日志框架的发展历程大致可分为图 1 所示的几个阶段：

<img src="https://img-blog.csdnimg.cn/76b1464f48c642fa951d9a94766d371c.png#pic_center" alt="在这里插入图片描述" width="600" height="350">

#### 2.1 Log4j

Apache Log4j 是一种基于 Java 的日志记录工具，它是 Apache 软件基金会的一个项目。在 jdk1.3 之前，还没有现成的日志框架，Java 工程师只能使用原始的 System.out.println(), System.err.println() 或者 e.printStackTrace()。通过把 debug 日志写到 StdOut 流，错误日志写到 ErrOut 流，以此记录应用程序的运行状态。这种原始的日志记录方式缺陷明显，不仅无法实现定制化，而且日志的输出粒度不够细。鉴于此，1999 年，大牛 Ceki Gülcü 创建了 Log4j 项目，并几乎成为了 Java 日志框架的实际标准。

#### 2.2 JUL

Log4j 作为 Apache 基金会的一员，Apache 希望将 Log4j 引入 jdk，不过被 sun 公司拒绝了。随后，sun 模仿 Log4j，在 jdk1.4 中引入了 JUL（java.util.logging）。

#### 2.3 Commons Logging

为了解耦日志接口与实现，2002 年 Apache 推出了 JCL(Jakarta Commons Logging)，也就是 Commons Logging。Commons Logging 定义了一套日志接口，具体实现则由 Log4j 或 JUL 来完成。Commons Logging 基于动态绑定来实现日志的记录，在使用时只需要用它定义的接口编码即可，程序运行时会使用 ClassLoader 寻找和载入底层的日志库，因此可以自由选择由 log4j 或 JUL 来实现日志功能。

#### 2.4 Slf4j&amp;Logback

大牛 Ceki Gülcü 与 Apache 基金会关于 Commons-Logging 制定的标准存在分歧，后来，Ceki Gülcü 离开 Apache 并先后创建了 Slf4j 和 Logback 两个项目。Slf4j 是一个日志门面，只提供接口，可以支持 Logback、JUL、log4j 等日志实现，Logback 提供具体的实现，它相较于 log4j 有更快的执行速度和更完善的功能。

#### 2.5 Log4j 2

为了维护在 Java 日志江湖的地位，防止 JCL、Log4j 被 Slf4j、Logback 组合取代 ，2014 年 Apache 推出了 Log4j 2。Log4j 2 与 log4j 不兼容，经过大量深度优化，其性能显著提升。

### 3.日志门面与日志系统

在上文中已经提及，目前常用的日志框架有 Log4j，Log4j 2，Commons Logging，Slf4j，Logback，JUL。这些日志框架可以分为两种类型：门面日志和日志系统。
- **日志门面**：只提供日志相关的接口定义，即相应的 API，而不提供具体的接口实现。日志门面在使用时，可以动态或者静态地指定具体的日志框架实现，解除了接口和实现的耦合，使用户可以灵活地选择日志的具体实现框架。- **日志系统**：与日志门面相对，它提供了具体的日志接口实现，应用程序通过它执行日志打印的功能。 <img src="https://img-blog.csdnimg.cn/b81da74a80224d828ce9087d9e74b7c8.png#pic_center" alt="在这里插入图片描述" width="600" height="300">
如图 2 所示，Commons-Logging 和 Slf4j 属于日志门面框架，Log4j、Logback、和 JUL 则属于具体的日志系统框架。阅读至此，想必读者一定疑惑——**为何如此设计？为何不简单一点？为何分成了门面和实现？**

在回答上述问题之前，我们先一起简单回顾一下门面模式（软件设计模式的一种，也称外观模式、正面模式）。门面模式的核心为：外部客户端与一个子系统的通信，必须通过一个统一的外观对象进行，使得子系统更易于使用，其本质就是为子系统中的一组接口提供一个统一的高层接口，如图 3 所示：

<img src="https://img-blog.csdnimg.cn/d752086f45434a699d3fe58e4f8208ba.png#pic_center" alt="在这里插入图片描述" width="600" height="300">

门面模式的核心是门面对象 Facade，它有如下几个特点：
- **知道所有子模块的责任和功能。**- **将客户端发来的请求委派到子系统中，本身没有具体业务逻辑。**- **不参与子系统内业务逻辑的实现。**
了解过门面模式的基本信息，再回到最初的问题——为什么日志框架要使用门面模式呢？其实答案很简单，在工程开发中常遇到这样的场景：
1. 我们自己的系统中使用了 Logback 这个日志系统；1. 我们的系统使用了 A.jar，A.jar 中使用的日志系统为 Log4j；1. 我们的系统又使用了 B.jar，而 B.jar 中使用的日志系统为 JUL。
在上述场景中，我们的系统需要同时支持并维护 Logback、Log4j、JUL 三种日志框架，其繁琐程度不言而喻。为了解决这个问题，可以引入一个适配层，由适配层决定具体使用哪一种日志系统，应用程序中的调用者只管打印日志，而不必关心日志是如何被打印出来的，如此，问题迎刃而解。显然，Slf4j 和 Commons-Logging 就是这种适配层，而 JUL、Log4j 和 Logback 等就是打印日志的具体实现。换言之，日志门面（适配层）只需要提供日志的接口，日志系统的具体实现则交由其它日志框架，这样就避免了需要维护复杂日志系统的问题。

### 4.避免环形依赖

Slf4j 的作者 Ceki Gülcü 当年因为觉得 Commons-Logging 的 API 设计的不好，性能也不够高，因而设计了 Slf4j。而他为了 Slf4j 能够兼容各种类型的日志系统实现，还设计了相当多的 adapter 和 bridge 来连接，如图 4 所示： <img src="https://img-blog.csdnimg.cn/b3d696fbf89e474caf8665e2d0119527.png#pic_center" alt="在这里插入图片描述" width="800" height="400">

这些 adapter 和 bridge 在此就不做详细介绍，读者需要时可自行查阅上图找到对应的 jar 包。这里只想引出一个由此产生的问题，那就是日志框架的循环依赖问题。具体而言，如果在应用中使用 Slf4j 作为日志门面，就需要引入 slf4j-api-xx.jar，如果同时又引入了 slf4j-log4j12-xx.jar，log4j-xx.jar，log4j-over-slf4j-xx.jar 这几个包，在这种情况下，调用 slf4j-api 就会出现死循环（如图 5 所示）。

<img src="https://img-blog.csdnimg.cn/ce1bf41470254b05902a14a1cbe1117a.png#pic_center" alt="在这里插入图片描述" width="600" height="300">

**鉴于此，在引入日志框架依赖的时候要尽力避免，比如以下组合就不能同时出现：**
- jcl-over-slf4j 和 slf4j-jcl- log4j-over-slf4j 和 slf4j-log4j12- jul-to-slf4j 和 slf4j-jdk14
### 5.日志框架的使用选择

#### 5.1 日志框架之间的关系

在介绍日志框架的使用之前，简要回顾一下前面四节的内容。Commons Logging 和 Slf4j 是日志门面。Log4j 和 Logback 则是具体的日志实现方案。可以简单的理解为接口与接口的实现，调用者只需要关注接口而无需关注具体的实现，从而做到解耦。在整个日志框架中主要包括日志门面、日志适配器、日志库三个部分，它们之间的关系如图 6 所示： <img src="https://img-blog.csdnimg.cn/33618ba4c7e34a2abc54ad2d4d78024a.png#pic_center" alt="在这里插入图片描述" width="600" height="300">

#### 5.2 日志框架的使用选择

比较常用的组合使用方式是 Slf4j 与 Logback 组合使用，Commons Logging 与 Log4j 组合使用，Logback 必须配合 Slf4j 使用。由于 Logback 和 Slf4j 是同一个作者，其兼容性不言而喻。

这里顺便介绍一个小故事：Apache 曾试图说服 Log4j 以及其它的日志来按照 Commons-Logging 的标准编写，但是由于 Commons-Logging 的类加载机制在实际应用中存在问题（它使用 ClassLoader 寻找和载入底层的日志库），实现起来也不友好，因此 Log4j 的作者便开发了 Slf4j，与 Commons-Logging 两分天下。

关于如何选择日志框架，如果是新的项目 (没有历史包袱，无需切换日志框架)，建议使用 Slf4j 与 Logback 组合，这样有如下的几个优点：
- **Slf4j 实现机制决定 Slf4j 限制较少，使用范围更广**。相较于 Commons-Logging，Slf4j 在编译期间便静态绑定本地的 Log 库，其通用性要好得多。- **Logback 拥有更好的性能**。Logback 声称：某些关键操作，比如判定是否记录一条日志语句的操作，其性能得到了显著的提高，这个操作在 Logback 中只需 3 纳秒，而在 Log4j 则需要 30 纳秒。- **Slf4j 支持参数化，使用占位符号，代码更为简洁**，如下例子。
```
// 在使用 Commons-Logging 时，通常的做法是
if(log.isDebugEnabled()){<!-- -->
  log.debug("User name： " + user.getName() + " buy goods id ：" + good.getId());
}
// 在 Slf4j 阵营，你只需这么做：
log.debug("User name：{} ,buy goods id ：{}", user.getName(),good.getId());  

```
- **Logback 的所有文档是免费提供的，Log4j 只提供部分免费文档而需要用户去购买付费文档**。- **MDC (Mapped Diagnostic Contexts) 用 Filter，将当前用户名等业务信息放入 MDC 中，在日志 format 定义中即可使用该变量**。具体而言，在诊断问题时，通常需要打出日志。如果使用 Log4j，则只能降低日志级别，但是这样会打出大量的日志，影响应用性能；如果使用 Logback，保持原定日志级别而过滤某种特殊情况，如 Alice 这个用户登录，日志将打在 DEBUG 级别而其它用户可以继续打在 WARN 级别。实现这个功能只需加 4 行 XML 配置。- **自动压缩日志**。RollingFileAppender 在产生新文件的时候，会自动压缩已经打出来的日志文件。压缩过程是异步的，因此在压缩过程中应用几乎不会受影响。 举例说明：如果直接使用 Slf4j 和 Logback 组合，可通过如下配置进行集成：
```
&lt;dependency&gt;
    &lt;groupId&gt;org.slf4j&lt;/groupId&gt;
    &lt;artifactId&gt;slf4j-api&lt;/artifactId&gt;
    &lt;version&gt;${slf4j-api.version}&lt;/version&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
    &lt;groupId&gt;ch.qos.logback&lt;/groupId&gt;
    &lt;artifactId&gt;logback-classic&lt;/artifactId&gt;
    &lt;version&gt;${logback.version}&lt;/version&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
   	&lt;groupId&gt;ch.qos.logback&lt;/groupId&gt;
    &lt;artifactId&gt;logback-core&lt;/artifactId&gt;
    &lt;version&gt;${logback.version}&lt;/version&gt;
&lt;/dependency&gt;

```

对于已有工程，需要根据所使用的日志库来确定门面适配器从而使用 Slf4j。Slf4j 的设计思想比较简洁，使用了 Facade 设计模式，Slf4j 本身只提供了一个 slf4j-api-version.jar 包，这个 jar 中主要是日志的抽象接口，jar 包中本身并没有对抽象出来的接口做实现。对于不同的日志实现方案（例如 Logback，Log4j 等），封装出不同的桥接组件(例如 logback-classic-version.jar，slf4j-log4j12-version.jar)，这样使用过程中可以灵活地选取自己项目里的日志实现。

举例说明，如果已有工程中使用了 Log4j 日志库，可通过如下配置进行集成：

```
&lt;dependency&gt;
    &lt;groupId&gt;org.slf4j&lt;/groupId&gt;
    &lt;artifactId&gt;slf4j-api&lt;/artifactId&gt;
    &lt;version&gt;${slf4j-api.version}&lt;/version&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
   	&lt;groupId&gt;org.slf4j&lt;/groupId&gt;
    &lt;artifactId&gt;slf4j-log4j12&lt;/artifactId&gt;
    &lt;version&gt;${slf4j-log4j12.version}&lt;/version&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
    &lt;groupId&gt;log4j&lt;/groupId&gt;
    &lt;artifactId&gt;log4j&lt;/artifactId&gt;
    &lt;version&gt;${log4j.version}&lt;/version&gt;
&lt;/dependency&gt;

```

下面是 Slf4j 与其它日志组件调用关系图： <img src="https://img-blog.csdnimg.cn/2eecba34c4a44b3683d79010adb5b2ec.png#pic_center" alt="在这里插入图片描述" width="600" height="400">

如果老代码中直接使用非 Slf4j 日志库提供的接口打印日志，需要引入日志库适配器来桥接遗留的 api。在实际环境中我们经常会遇到不同的组件使用的日志框架不同的情况，例如 Spring Framework 使用的是日志组件是 Commons Logging，XSocket 依赖的则是 Java Util Logging。

如果在同一项目中使用不同的组件时，如何解决不同组件依赖的日志组件不一致的情况呢？这就需要统一日志方案，统一使用 Slf4j，把他们的日志输出重定向到 Slf4j，然后 Slf4j 又会根据绑定器把日志交给具体的日志实现工具。Slf4j 带有几个桥接模块，可以重定向 Log4j，JCL 和 java.util.logging 中的 Api 到 Slf4j。

举例说明：如果老代码中直接使用了 Log4j 日志库接口打印日志，需引入如下配置：

```
&lt;dependency&gt;
    &lt;groupId&gt;org.slf4j&lt;/groupId&gt;
    &lt;artifactId&gt;log4j-over-slf4j&lt;/artifactId&gt;
    &lt;version&gt;${log4j-over-slf4j.version}&lt;/version&gt;
&lt;/dependency&gt;

```

桥接方式参考下图： <img src="https://img-blog.csdnimg.cn/32a3b4296c7e4381b067074a71df31a1.png#pic_center" alt="在这里插入图片描述" width="800" height="500">

#### 5.3 排除项目中依赖的第三方包的日志依赖

在实际使用过程中，项目会根据需要引入一些第三方组件，例如常用的 Spring，而 Spring 本身的日志实现使用了 Commons Logging，如果想使用 Slf4j+Logback 组合，这时候需要在项目中将 Commons Logging 排除掉，通常会用到以下 3 种方案，各有利弊，可以根据项目的实际情况选择最适合自己项目的解决方案。
- **方案一：采用 maven 的 exclusion 方案**
```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework&lt;/groupId&gt;
    &lt;artifactId&gt;spring-core&lt;/artifactId&gt;
    &lt;exclusions&gt;
        &lt;exclusion&gt;
            &lt;groupId&gt;commons-logging&lt;/groupId&gt;
            &lt;artifactId&gt;commons-logging&lt;/artifactId&gt;
        &lt;/exclusion&gt;
    &lt;/exclusions&gt;
    &lt;version&gt;${springframework.version}&lt;/version&gt;
&lt;/dependency&gt;

```

这种方案优点是 exclusion 是 maven 原生提供的，不足之处是如果有多个组件都依赖了 commons-logging，则需要在很多处增加 exclusion，比较繁琐。
- **方案二：在 maven 声明 commons-logging 的 scope 为 provided**
```
&lt;dependency&gt;
    &lt;groupId&gt;commons-logging&lt;/groupId&gt;
    &lt;artifactId&gt;commons-logging&lt;/artifactId&gt;
    &lt;version&gt;1.1.1&lt;/version&gt;
    &lt;scope&gt;provided&lt;/scope&gt;
&lt;/dependency&gt;

```

这种方案虽然简洁，但也有缺点，在调试代码时有可能导致 IDE 将 commons-logging 放置在 classpath 下，从而导致程序运行时出现异常。
- **方案三：在 maven 私服中增加类似于 99.0-does-not-exist 这种虚拟的版本号**
```
&lt;dependency&gt;    
    &lt;groupId&gt;commons-logging&lt;/groupId&gt;    
    &lt;artifactId&gt;commons-logging&lt;/artifactId&gt;    
    &lt;version&gt;99.0-does-not-exist&lt;/version&gt;    
&lt;/dependency&gt; 

```

这种方案好处在于声明方式比较简单，用 IDE 调试代码时也不会出现问题，不足之处是 99.0-does-not-exist 这种版本是 maven 中央仓库中可能不存在，需要发布到自己的 maven 私服中。
