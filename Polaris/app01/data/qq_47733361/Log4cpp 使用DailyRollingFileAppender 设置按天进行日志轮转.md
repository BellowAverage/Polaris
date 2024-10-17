
--- 
title:  Log4cpp 使用DailyRollingFileAppender 设置按天进行日志轮转 
tags: []
categories: [] 

---
#### 一、需求

使用Log4cpp日志框架，设置按天进行日志轮转，每天生成一个日志，日志最大保留天数为7天。

#### 二、实现

按天进行日志轮转，我们选择Log4cpp中的 DailyRollingFileAppender 类，实现代码如下： 首先在头文件中定义一个成员变量来存储 根 Category

```
protected:
    log4cpp::Category* category_;

```

下面为Log4cpp初始化方法：

```
void TransmissionServiceLog::initLog(std::string logFilename){<!-- -->
    // 获取根 Category
    category_ = &amp;log4cpp::Category::getRoot();
    // 定义Appender，指定日志输出位置
    log4cpp::DailyRollingFileAppender* fileAppender = new log4cpp::DailyRollingFileAppender("DailyAppender1", logFilename, 2, true);

    // 设置日志布局
    log4cpp::PatternLayout* layout = new log4cpp::PatternLayout();
    layout-&gt;setConversionPattern("%m");

    fileAppender-&gt;setLayout(layout);
    category_-&gt;setAppender(fileAppender);
    category_-&gt;setPriority(log4cpp::Priority::DEBUG);
	category_-&gt;info("TransmissionServiceLog::initLog successful! the logFilename = %s", logFilename);
}

```

#### 三、源代码分析

查看DailyRollingFileAppender 的源代码，我们可以看到它的构造函数：

```
DailyRollingFileAppender(const std::string&amp; name,
                            const std::string&amp; fileName,
                            unsigned int maxDaysToKeep = maxDaysToKeepDefault,
                            bool append = true,
                            mode_t mode = 00644);

```
- const std::string&amp; name：表示当前这个Appender的名字；- const std::string&amp; fileName：表示要记录的日志文件的名字；- unsigned int maxDaysToKeep = maxDaysToKeepDefault：表示设置最大保留天数，默认为maxDaysToKeepDefault；- bool append = true：表示如果设置为 true，则在打开日志文件时将日志追加到末尾，设置为 false 则会清空原有内容；- mode_t mode = 00644：设置文件权限的模式，默认值为 00644。