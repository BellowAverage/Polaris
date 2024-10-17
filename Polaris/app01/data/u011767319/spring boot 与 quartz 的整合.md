
--- 
title:  spring boot 与 quartz 的整合 
tags: []
categories: [] 

---
### 引入jar包

```
&lt;!-- quartz --&gt;
&lt;dependency&gt;
	&lt;groupId&gt;org.quartz-scheduler&lt;/groupId&gt;
	&lt;artifactId&gt;quartz&lt;/artifactId&gt;
	&lt;version&gt;2.2.1&lt;/version&gt;
	&lt;exclusions&gt;
		&lt;exclusion&gt;
			&lt;artifactId&gt;slf4j-api&lt;/artifactId&gt;
			&lt;groupId&gt;org.slf4j&lt;/groupId&gt;
		&lt;/exclusion&gt;
	&lt;/exclusions&gt;
&lt;/dependency&gt;
&lt;!-- 该依赖必加，里面有sping对schedule的支持 --&gt;
&lt;dependency&gt;
	&lt;groupId&gt;org.springframework&lt;/groupId&gt;
	&lt;artifactId&gt;spring-context-support&lt;/artifactId&gt;
	&lt;version&gt;4.3.10.RELEASE&lt;/version&gt;
&lt;/dependency&gt;

```

### 在资源文件下创建quarzt的配置文件

>  
 **文件名：** quartz.properties 


****文件内容（整合druid的结果）：****

```
org.quartz.scheduler.instanceName = MyScheduler
org.quartz.threadPool.threadCount = 5
org.quartz.jobStore.class = org.quartz.impl.jdbcjobstore.JobStoreTX
org.quartz.jobStore.driverDelegateClass = org.quartz.impl.jdbcjobstore.StdJDBCDelegate
org.quartz.jobStore.tablePrefix = QRTZ_
org.quartz.jobStore.dataSource = myDS

//整合druid
org.quartz.dataSource.myDS.connectionProvider.class:com.ljq.rxrs.config.DruidConnectionProvider

org.quartz.dataSource.myDS.driver = com.mysql.jdbc.Driver
org.quartz.dataSource.myDS.URL = jdbc:mysql://120.79.172.69:3306/renshi?characterEncoding=utf-8
org.quartz.dataSource.myDS.user = renshi
org.quartz.dataSource.myDS.password = ljq123456
org.quartz.dataSource.myDS.maxConnection = 5

```

### 编写SchedulerConfig配置

```
package com.ljq.rxrs.quartz.config;

import java.io.IOException;
import java.util.Properties;

import org.quartz.Scheduler;
import org.quartz.ee.servlet.QuartzInitializerListener;
import org.springframework.beans.factory.config.PropertiesFactoryBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;
import org.springframework.scheduling.quartz.SchedulerFactoryBean;

/**
 * @email 867170960@qq.com
 * @author:刘俊秦
 * @date: 2018/11/17 0017
 * @time: 下午 12:15
 */
@Configuration
public class SchedulerConfig {

	@Bean(name = "SchedulerFactory")
	public SchedulerFactoryBean schedulerFactoryBean() throws IOException {
		SchedulerFactoryBean factory = new SchedulerFactoryBean();
		factory.setQuartzProperties(quartzProperties());
		return factory;
	}

	@Bean
	public Properties quartzProperties() throws IOException {
		PropertiesFactoryBean propertiesFactoryBean = new PropertiesFactoryBean();
		propertiesFactoryBean.setLocation(new ClassPathResource("/quartz.properties"));
		// 在quartz.properties中的属性被读取并注入后再初始化对象
		propertiesFactoryBean.afterPropertiesSet();
		Properties object = propertiesFactoryBean.getObject();
		System.out.println(object);
		return propertiesFactoryBean.getObject();
	}

	/*
	 * quartz初始化监听器
	 */
	@Bean
	public QuartzInitializerListener executorListener() {
		return new QuartzInitializerListener();
	}

	/*
	 * 通过SchedulerFactoryBean获取Scheduler的实例
	 */
	@Bean(name = "Scheduler")
	public Scheduler scheduler() throws IOException {
		return schedulerFactoryBean().getScheduler();
	}

}


```

1.Quartz各版本数据库连接池技术更新情况

Quartz 2.0 以前 DBCP

Quartz 2.0 以后 C3P0（包含2.0）

**原因Quartz 2.0默认连接池是 C3P0，而博主用的连接池是druid。所有得更改连接池**

### 配置quartz扩展druid连接池


