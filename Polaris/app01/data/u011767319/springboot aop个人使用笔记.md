
--- 
title:  springboot aop个人使用笔记 
tags: []
categories: [] 

---
### spring boot 框架配置 aop

**依赖注入**

```
	&lt;!-- aop --&gt;
	&lt;dependency&gt;
	    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
	    &lt;artifactId&gt;spring-boot-starter-aop&lt;/artifactId&gt;
	&lt;/dependency&gt;

```

**execution表达式-解析**

|符号|含义
|------
|execution( * com.ljq.demo_java14.controller.**.**(…))|例子：表达式
|执行（）|表达式的主体
|第一个 “*” 符号|表示返回值的类型任意
|com.sample.service.impl|AOP所切的服务的包名，即，我们的业务部分
|包名后面的". ."|表示当前包及子包
|第二个"*"|表示类名，*即所有类
|. *（. .）|表示任何方法名，括号表示参数，两个点表示任何参数类型

**代码演示-个人写的全部控制器拦截打印日志**

```
package com.ljq.demo_java14.aop;


import com.alibaba.fastjson.JSON;
import lombok.extern.slf4j.Slf4j;
import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.*;
import org.springframework.stereotype.Component;

import javax.annotation.Resource;
import javax.servlet.http.HttpServletRequest;
import java.util.Arrays;

/**
 * @email 867170960@qq.com
 * @author:刘俊秦
 * @date: 2019/5/11 0011
 * @time: 上午 9:44
 * 打印日志
 */
@Component
@Aspect
@Slf4j
public class PrintLog {<!-- -->

    @Resource
    private HttpServletRequest request;

    @Pointcut("execution( * com.ljq.demo_java14.controller.*.*(..))")
    public void webLog() {<!-- -->
    }

    @Before("webLog()")
    public void before(JoinPoint point) {<!-- -->
        printLog_common(point, "请求开始");
    }

    @After("webLog()")
    public void after(JoinPoint point) {<!-- -->
        printLog_common(point, "请求结束");
    }

    @AfterReturning(returning = "res", pointcut = "webLog()")
    public void doAfterReturning(Object res) {<!-- -->
        // 处理完请求，返回内容
        log.info("&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; { 响应 } &gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;");
        String zhi = null != res ? JSON.toJSONString(res) : "没有返回值";
        log.info("响应参数 : " + zhi);
        log.info("===================================================================");
    }


    public void printLog_common(JoinPoint point, String title) {<!-- -->
        // 记录下请求内容
        log.info("&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; {" + title + "} &gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;");
        log.info("&lt;&lt;&lt; { 目标为：" + point.getSignature().getDeclaringTypeName() + "} &gt;&gt;&gt;");
        log.info("请求地址 : " + request.getRequestURL().toString());
        log.info("请求IP : " + request.getRemoteAddr());
        log.info("请求类型为：" + request.getMethod());
        log.info("方法为：" + point.getSignature().getName());
        log.info("参数为：" + Arrays.toString(point.getArgs()));
        log.info("===================================================================");
    }

}


```

### spring 框架的配置aop（本人已经不使用）------------------------

aop 的依赖

```
		&lt;dependency&gt;
			&lt;groupId&gt;org.aspectj&lt;/groupId&gt;
			&lt;artifactId&gt;aspectjrt&lt;/artifactId&gt;
			&lt;version&gt;1.8.4&lt;/version&gt;
		&lt;/dependency&gt;
		&lt;dependency&gt;
			&lt;groupId&gt;org.aspectj&lt;/groupId&gt;
			&lt;artifactId&gt;aspectjtools&lt;/artifactId&gt;
			&lt;version&gt;1.8.4&lt;/version&gt;
		&lt;/dependency&gt;
		&lt;dependency&gt;
			&lt;groupId&gt;org.aspectj&lt;/groupId&gt;
			&lt;artifactId&gt;aspectjweaver&lt;/artifactId&gt;
			&lt;version&gt;1.8.4&lt;/version&gt;
		&lt;/dependency&gt;

```

============================================

配置spring-config.xm

```
&lt;!-- 开启注解式的aop --&gt;
	&lt;aop:aspectj-autoproxy&gt;&lt;/aop:aspectj-autoproxy&gt;

```

## – 简单切入所有类所有方法

### 编写 UserService.java 类（业务类）

```
package com.bjpowernode.user.service;

import org.springframework.stereotype.Service;

@Service

public class UserService {

	public void insert() {
		System.out.println("insert");
	}
	
	public void update() {
		System.out.println("update");
	}

	public void delete() {
		System.out.println("delete");
	}
}

```

### 编写 TestSpring.java 类（测试类 JUnit的类）

```
package com.bjpowernode;
//包
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import com.bjpowernode.user.service.UserService;

@RunWith(SpringJUnit4ClassRunner.class) //@RunWith 翻译成中文就是 测试运行器，JUnit所有的测试方法都是由测试运行器负责执行
@ContextConfiguration(locations = { "classpath:spring-config.xml" }) //@ContextConfiguration Spring整合JUnit4测试时，使用注解引入多个配置文件

public class TestSpring {
	@Autowired //自动注入
	private UserService service;

	@Test //标记测试
	public void run() {
		
		service.insert();
		
		service.update();
		
		service.delete();
	}

}

```

### 编写 UserServiceInterceptor.java 类（aop切入类）

```
package com.bjpowernode;

import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;

import com.bjpowernode.user.InitParam;

@Component // 把本类声明spring组件
@Aspect // 在本类上开启切面技术(把这个类声明成切面)

public class UserServiceInterceptor {

	@After("within(com.bjpowernode.user.service..*)") //表示方法执行后切入
	public void run() {
		System.out.println("切入成功！！！！");
	}

}

```

>  
 运行结果:  insert 切入成功！！！！  update 切入成功！！！！  delete 切入成功！！！！ 


## ------ 注解方式 针对某个方法 切入

### 创建Annotation -&gt; InitParam 注解类

```
package com.bjpowernode.user;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target({ ElementType.METHOD }) //元注解 定义作用域 ElementType.METHOD作用到方法上
@Retention(RetentionPolicy.RUNTIME)  //生命周期  RetentionPolicy.RUNTIME运行时有效

//定义一个标记
public @interface InitParam {

}

```

### 创建业务类 UserService

```
package com.bjpowernode.user.service;

import org.springframework.stereotype.Service;

import com.bjpowernode.user.InitParam;

@Service

public class UserService {

	public void insert() {
		System.out.println("insert");
	}

	@InitParam
	// 在作过标记的方法上切入程序
	public void update() {
		System.out.println("update");
	}

	public void delete() {
		System.out.println("delete");
	}
}

```

### 编写 UserServiceInterceptor.java 类（aop切入类）

```
package com.bjpowernode;

import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;

import com.bjpowernode.user.InitParam;

@Component // 把本类声明spring组件
@Aspect // 在本类上开启切面技术(把这个类声明成切面)

public class UserServiceInterceptor {

	//	annotation(initParam) 括号放的是注解类型变量
	//  @Before("within(com.bjpowernode.user.service..*)")
	//	@Before("within(com.bjpowernode.user.service..*) &amp;&amp; @annotation(initParam)") //表示方法执行之前切入
	@After("within(com.bjpowernode.user.service..*) &amp;&amp; @annotation(initParam)") //表示方法执行之后切入
	public void run(InitParam initParam) {
		System.out.println("切入成功！！！！");
	}

}

```

### 编写 TestSpring.java 类（测试类 JUnit的类）

```
package com.bjpowernode;
//包
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import com.bjpowernode.user.service.UserService;

@RunWith(SpringJUnit4ClassRunner.class) //@RunWith 翻译成中文就是 测试运行器，JUnit所有的测试方法都是由测试运行器负责执行
@ContextConfiguration(locations = { "classpath:spring-config.xml" }) //@ContextConfiguration Spring整合JUnit4测试时，使用注解引入多个配置文件

public class TestSpring {
	@Autowired //自动注入
	private UserService service;

	@Test //标记测试
	public void run() {
		
		service.insert();
		
		service.update();
		
		service.delete();
	}

}

```

### aop普通是使用方式

```
@Component
@Aspect
@Slf4j
public class PrintLog {
	//定义切入点
    @Pointcut("execution(* com.ljq.assets.controller.*.*(..))")
    public void pointcut() {
    }

    @Before("pointcut()")
    public void before(JoinPoint point) {
        log.info("=================================================================");
        log.info("@Before：目标为：" + point.getSignature().getDeclaringTypeName());
        log.info("@Before：方法为：" + point.getSignature().getName());
        log.info("@Before：参数为：" + Arrays.toString(point.getArgs()));
        log.info("=================================================================");
    }

}

```

### aop获取HttpServletRequest信息

```
HttpServletRequest request = ((ServletRequestAttributes) RequestContextHolder.getRequestAttributes()).getRequest();

```

### aop输出日志

```
@Before("pointcut()")
    public void before(JoinPoint point) {
        log.info("=================================================================");
        log.info("@Before：目标为：" + point.getSignature().getDeclaringTypeName());
        log.info("@Before：方法为：" + point.getSignature().getName());
        log.info("@Before：参数为：" + Arrays.toString(point.getArgs()));
        log.info("=================================================================");
    }

```
