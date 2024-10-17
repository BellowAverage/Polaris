
--- 
title:  整合Druid数据源 
tags: []
categories: [] 

---
### 整合Druid数据源(druid-spring-boot-starter)
1. **导入依赖**1. **配置yml文件**1. **编写DruidConfig.java配置类**
### ------依赖

```
&lt;properties&gt;
		&lt;project.build.sourceEncoding&gt;UTF-8&lt;/project.build.sourceEncoding&gt;
		&lt;project.reporting.outputEncoding&gt;UTF-8&lt;/project.reporting.outputEncoding&gt;
		&lt;java.version&gt;1.8&lt;/java.version&gt;
		&lt;druid.version&gt;1.1.10&lt;/druid.version&gt;
	&lt;/properties&gt;

&lt;!-- mysql驱动 --&gt;
		&lt;dependency&gt;
			&lt;groupId&gt;mysql&lt;/groupId&gt;
			&lt;artifactId&gt;mysql-connector-java&lt;/artifactId&gt;
			&lt;version&gt;5.1.47&lt;/version&gt;
		&lt;/dependency&gt;

		&lt;!--druid --&gt;
		&lt;dependency&gt;
			&lt;groupId&gt;com.alibaba&lt;/groupId&gt;
			&lt;artifactId&gt;druid-spring-boot-starter&lt;/artifactId&gt;
			&lt;version&gt;${druid.version}&lt;/version&gt;
		&lt;/dependency&gt;

```

### 配置yml文件

```
spring:
	datasource:
    type: com.alibaba.druid.pool.DruidDataSource
    druid:
      driver-class-name: com.mysql.jdbc.Driver
      url: jdbc:mysql://120.79.172.69:3306/renshi?useSSL=false&amp;useUnicode=true
      username: renshi
      password: ljq123456
      initial-size: 1                     #连接池初始大小
      max-active: 20                      #连接池中最大的活跃连接数
      min-idle: 1                         #连接池中最小的活跃连接数
      max-wait: 60000                     #配置获取连接等待超时的时间
      pool-prepared-statements: true    #打开PSCache，并且指定每个连接上PSCache的大小
      max-pool-prepared-statement-per-connection-size: 20
      validation-query: SELECT 1 FROM DUAL
      validation-query-timeout: 30000
      test-on-borrow: false             #是否在获得连接后检测其可用性
      test-on-return: false             #是否在连接放回连接池后检测其可用性
      test-while-idle: true             #是否在连接空闲一段时间后检测其可用性

```

### 编写DruidConfig.java配置类

```
package com.ljq.rxrs.config;

import java.util.HashMap;
import java.util.Map;

import org.springframework.boot.web.servlet.FilterRegistrationBean;
import org.springframework.boot.web.servlet.ServletRegistrationBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.alibaba.druid.support.http.StatViewServlet;
import com.alibaba.druid.support.http.WebStatFilter;

/**
 * @email 867170960@qq.com
 * @author:刘俊秦
 * @date: 2018/10/4 0004
 * @time: 下午 8:23
 */

@Configuration
public class DruidConfig {

	// 配置Druid的监控
	@SuppressWarnings({ "rawtypes", "unchecked" })
	// 1、配置一个管理后台的Servlet
	@Bean
	public ServletRegistrationBean statViewServlet() {
		ServletRegistrationBean bean = new ServletRegistrationBean(new StatViewServlet(), "/druid/*");
		Map&lt;String, String&gt; initParams = new HashMap&lt;&gt;();

		initParams.put("loginUsername", "admin");
		initParams.put("loginPassword", "liu1101***");
		// 默认就是允许所有访问
		initParams.put("allow", "");
		initParams.put("deny", "");

		bean.setInitParameters(initParams);
		return bean;
	}

	@SuppressWarnings({ "rawtypes", "unchecked" })
	@Bean
	public FilterRegistrationBean filterRegistrationBean() {
		FilterRegistrationBean filterRegistrationBean = new FilterRegistrationBean(new WebStatFilter());
		filterRegistrationBean.addUrlPatterns("/*");
		filterRegistrationBean.addInitParameter("exclusions", "*.js,*.gif,*.jpg,*.png,*.css,*.ico,/druid/*");
		return filterRegistrationBean;
	}

}


```
