
--- 
title:  springboot集成xxl-job个人笔记 
tags: []
categories: [] 

---
### 配置springboot配置文件application.yml

```
xxl:
  job:
    accessToken:
    admin:
      addresses: http://127.0.0.1:9998/xxl-job-admin
    executor:
      appname: ${<!-- -->spring.application.name}
      ip:
      port: 5000
      logpath: /data/applogs/xxl-job/jobhandler
      logretentiondays: 30

```

### 创建一个XxlJobConfig配置

```
package com.hgj.face.config.xxljob;

import com.hgj.common.util.LogPrintUtil;
import com.xxl.job.core.executor.impl.XxlJobSpringExecutor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;

@Component
public class XxlJobConfig {<!-- -->

    @Value("${xxl.job.admin.addresses}")
    private String adminAddresses;
    @Value("${xxl.job.executor.appname}")
    private String appname;
    @Value("${xxl.job.executor.ip}")
    private String ip;
    @Value("${xxl.job.executor.port}")
    private Integer port;
    @Value("${xxl.job.accessToken}")
    private String accessToken;
    @Value("${xxl.job.executor.logpath}")
    private String logPath;
    @Value("${xxl.job.executor.logretentiondays}")
    private Integer logRetentionDays;

    @Bean
    public XxlJobSpringExecutor xxlJobExecutor() {<!-- -->
        LogPrintUtil.logRes("&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt; xxl-job配置开始启动");
        XxlJobSpringExecutor xxlJobSpringExecutor = new XxlJobSpringExecutor();
        xxlJobSpringExecutor.setAdminAddresses(adminAddresses);
        xxlJobSpringExecutor.setAppname(appname);
        xxlJobSpringExecutor.setIp(ip);
        xxlJobSpringExecutor.setPort(port);
        xxlJobSpringExecutor.setAccessToken(accessToken);
        xxlJobSpringExecutor.setLogPath(logPath);
        xxlJobSpringExecutor.setLogRetentionDays(logRetentionDays);
        return xxlJobSpringExecutor;
    }

}


```

**logpath官方说是选填**

>  
 到时再xxl-job调用的过程中，springboot 会在这个目录创建文件。所有必须在所在的服务器中创建自己定义的logpath目录。不然代码就会一直报错 例子：no such file or directory 


```
#创建文件目录
mkdir -p /data/applogs/xxl-job/jobhandler
#赋予权限
chmod 777 /data/applogs/xxl-job/jobhandler

```
