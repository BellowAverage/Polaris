
--- 
title:  hbase Caused by: java.lang.ClassNotFoundException: org.apache.commons.compress.utils.InputStreamStat 
tags: []
categories: [] 

---1. 异常信息
```
Caused by: java.lang.ClassNotFoundException: org.apache.commons.compress.utils.InputStreamStatistics
	at java.net.URLClassLoader.findClass(URLClassLoader.java:381)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:424)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:335)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:357)
	... 11 more


```

解决办法： pom.xml文件调整依赖的顺序

原来的顺

```
        &lt;!-- hadoop的通用包 --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.apache.hadoop&lt;/groupId&gt;
            &lt;artifactId&gt;hadoop-common&lt;/artifactId&gt;
            &lt;version&gt;2.7.5&lt;/version&gt;
        &lt;/dependency&gt;

        &lt;!-- 操作Office库 --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.apache.poi&lt;/groupId&gt;
            &lt;artifactId&gt;poi-ooxml&lt;/artifactId&gt;
            &lt;version&gt;4.0.1&lt;/version&gt;
        &lt;/dependency&gt;

```

调整后的顺

```
        &lt;!-- 操作Office库 --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.apache.poi&lt;/groupId&gt;
            &lt;artifactId&gt;poi-ooxml&lt;/artifactId&gt;
            &lt;version&gt;4.0.1&lt;/version&gt;
        &lt;/dependency&gt;
        &lt;!-- hadoop的通用包 --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.apache.hadoop&lt;/groupId&gt;
            &lt;artifactId&gt;hadoop-common&lt;/artifactId&gt;
            &lt;version&gt;2.7.5&lt;/version&gt;
        &lt;/dependency&gt;

```

调整后，程序执行成功，具体原因不清楚。谁知道原因的请给小编留言，小编非常感激！
