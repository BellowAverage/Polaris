
--- 
title:  log4cpp封装成独立的类（单例模式） 
tags: []
categories: [] 

---
### 一、编译安装

### 二、封装使用

头文件Logger.h:

```
#ifndef DISTRIBUTED_LOGGER_H_
#define DISTRIBUTED_LOGGER_H_

#include &lt;string&gt;
#include &lt;log4cpp/Category.hh&gt;


class Logger{<!-- -->
public:
    bool init(const std::string&amp; log_conf_file);

    static Logger* instance(){<!-- -->//返回单例——全局唯一对象
        return &amp;instance_;
    }
    log4cpp::Category* get_handle(){<!-- -->
        return category_;
    }
    
protected:
    static Logger instance_;
    log4cpp::Category* category_;
};

#define LOG_INFO Logger::instance()-&gt;get_handle()-&gt;info
#define LOG_DEBUG Logger::instance()-&gt;get_handle()-&gt;debug
#define LOG_ERROR Logger::instance()-&gt;get_handle()-&gt;error
#define LOG_WARN Logger::instance()-&gt;get_handle()-&gt;warn

#endif

```

实现类Logger.cpp：

```
#include "Logger.h"

#include &lt;iostream&gt;
#include &lt;log4cpp/Category.hh&gt;
#include &lt;log4cpp/FileAppender.hh&gt;
#include &lt;log4cpp/PatternLayout.hh&gt;
#include &lt;log4cpp/OstreamAppender.hh&gt;
#include &lt;log4cpp/PropertyConfigurator.hh&gt;

Logger Logger::instance_;

bool Logger::init(const std::string&amp; log_conf_file){<!-- -->
    try{<!-- -->
        log4cpp::PropertyConfigurator::configure(log_conf_file);

    }catch(log4cpp::ConfigureFailure&amp; f){<!-- -->
        std::cerr &lt;&lt; " load log config file " &lt;&lt; log_conf_file.c_str() &lt;&lt; " failed with result : " &lt;&lt; f.what()&lt;&lt; std::endl;
        return false;
    }
    category_ = &amp;log4cpp::Category::getRoot();
    return true;
}

```
