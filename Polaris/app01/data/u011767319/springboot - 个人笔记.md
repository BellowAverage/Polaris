
--- 
title:  springboot - 个人笔记 
tags: []
categories: [] 

---
### 如何发生事件呢

>  
 首先创建一个事件 例子：用户数据更新 


```
package app.woya.service.app.event;

import org.springframework.context.ApplicationEvent;

public class UserUpdateEvent extends ApplicationEvent {<!-- -->

    private Long userId;

    public UserUpdateEvent(Long userId) {<!-- -->
        super(userId);
        this.userId = userId;
    }

    public Long getUserId() {<!-- -->
        return userId;
    }

    public void setUserId(Long userId) {<!-- -->
        this.userId = userId;
    }
}


```

发生事件

```
@Resource
private ApplicationEventPublisher applicationEventPublisher;

//发起用户更新事件
applicationEventPublisher.publishEvent(new UserUpdateEvent(userProfile.getUserId()));

```

监听事件

```
package app.woya.service.app.event.listener;

import app.woya.lib.user.api.v1.ChatWithApiService;
import app.woya.service.app.event.UserUpdateEvent;
import lombok.extern.slf4j.Slf4j;
import org.springframework.context.event.EventListener;
import org.springframework.stereotype.Component;

import javax.annotation.Resource;

@Component
@Slf4j
public class UserUpdateListener {<!-- -->

    @Resource
    private ChatWithApiService chatWithApiService;

    @EventListener
    public void updateUserDate(UserUpdateEvent userUpdateEvent) {<!-- -->
        //用户数据更新，更新用户的陪聊设置
        chatWithApiService.updateEnable(userUpdateEvent.getUserId());
    }

}

```

### 获取当前服务使用得是什么环境

```
	@Resource
    private ApplicationContext applicationContext;

    public void operationDiamond(UserDiamondOperationDTO operationDTO) {<!-- -->
        String activeProfile = applicationContext.getEnvironment().getActiveProfiles()[0];
        //activeProfile的值，例子：test prod dev
    }

```

### 发送自定义格式的邮件



**首先我们需要确认邮件服务的环境是否已经搭建成功，简单回顾一下邮件服务配置流程：**
1. 项目中引入&gt;spring-boot-starter-mail依赖1. 配置文件中配置邮箱账户、账户密码或授权密码、邮箱服务器地址等信息1. 定义发送邮件类MailService，注入官方提供的JavaMailSender工具，注入配置的邮箱账户，完成邮箱发送逻辑1. 定义单元测试类，测试邮件发送功能
**自定义邮件格式**

>  
 定义sendHTMLStyleMail()方法来发送HTML格式邮件 


```
/**
 * 发送HTML格式邮件
 */
public void sendHTMLStyleMail(String to, String subject, String content){<!-- -->
    log.info("发送HTML格式邮件，收件人：{}，主题：{}，内容：{}",to,subject,content);
    //使用MimeMessage发送复杂邮件
    MimeMessage mimeMessage = javaMailSender.createMimeMessage();
    try {<!-- -->
        //设置开启multiparty email
        MimeMessageHelper messageHelper = new MimeMessageHelper(mimeMessage,true);
        messageHelper.setFrom(fromEmail);
        messageHelper.setTo(to);
        messageHelper.setSubject(subject);
        //设置解析为html
        messageHelper.setText(content,true);
        javaMailSender.send(mimeMessage);
        log.info("邮件发送完成！");
    } catch (MessagingException e) {<!-- -->
        log.info("邮件发送失败，错误信息：{}",e);
    }
}

```
- 发送HTML格式内容时，使用org.springframework.mail.javamail包的MimeMessageHelper类 创建MimeMessageHelper时传入true参数，代表开启Multipart email，此时邮件中允许添加附件和内嵌资源。- setText()方法设置内容时第二个参数true代表内容解析为HTML **在单元测试中定义测试方法，并调用发送HTML格式邮件**
```
@Test
public void testSendHTMLStyleMail(){<!-- -->
    log.info("测试HTML格式邮件发送功能 =&gt; ");
    String to = "104123456@qq.com";
    String subject = "发送HTML格式邮件";
    StringBuilder content = new StringBuilder();
    content.append("&lt;html&gt;");
    content.append("&lt;body style="background-color:PowderBlue;"&gt;");
    content.append("&lt;h1&gt;标题：SpringBoot发送HTML邮件&lt;/h1&gt;");
    content.append("&lt;p style="font-size:30px;color:red"&gt; 这里是正文：字体大小20px，红色 &lt;/p&gt;");
    content.append("&lt;/html&gt;");
    emailService.sendHTMLStyleMail(to,subject,content.toString());
}

```

**测试成功后，邮箱接收到邮件内容，解析HTML内容为：** <img src="https://img-blog.csdnimg.cn/b7d1804d3155460280fc51b406ccaf8e.png" alt="在这里插入图片描述">

### 自定义注解

例子：

>  
 Target :指明了修饰的这个注解的使用范围，即被描述的注解可以用在哪里 Retention: 指明修饰的注解的生存周期，即会保留到哪个阶段。 Documented：指明修饰的注解，可以被例如javadoc此类的工具文档化，只负责标记，没有成员取值。 


**Target**

```
TYPE:类，接口或者枚举
FIELD:域，包含枚举常量
METHOD:方法
PARAMETER:参数
CONSTRUCTOR:构造方法
LOCAL_VARIABLE:局部变量
ANNOTATION_TYPE:注解类型
PACKAGE:包

```

**RetentionPolicy**

```
SOURCE：源码级别保留，编译后即丢弃
CLASS:编译级别保留，编译后的class文件中存在，在jvm运行时丢弃，这是默认值
RUNTIME： 运行级别保留，编译后的class文件中存在，在jvm运行时保留，可以被反射调用

```

```
@Target({<!-- -->ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface EnableSseRocketMQMode {<!-- -->

}

```

**使用一下注解标记实现类**

```
@ConditionalOnBean(annotation = EnableSseRocketMQMode.class)

```

**使用自定义注解**

```
@EnableSseRocketMQMode

```

### springboot 如何使用异步

**创建异步配置**

```
package com.ushangxie.cca.service.wechat.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.AsyncConfigurer;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

import java.util.concurrent.Executor;
import java.util.concurrent.ThreadPoolExecutor;

/**
 * @author ljq
 * @date 2021/2/6
 */
@EnableAsync(proxyTargetClass = true)
@Configuration
public class AsyncTaskConfiguration implements AsyncConfigurer {<!-- -->

    @Override
    public Executor getAsyncExecutor() {<!-- -->
        return taskExecutor();
    }

    /**
     * 任务线程池
     *
     * @return
     */
    @Bean
    public Executor taskExecutor() {<!-- -->
        ThreadPoolTaskExecutor taskExecutor = new ThreadPoolTaskExecutor();     //定义线程池
        taskExecutor.setCorePoolSize(50);                                       //核心线程数
        taskExecutor.setMaxPoolSize(200);                                       //线程池最大线程数
        taskExecutor.setKeepAliveSeconds(30);                                   //30s保活
        taskExecutor.setQueueCapacity(Integer.MAX_VALUE);                       //线程队列最大队列数量
        taskExecutor.setRejectedExecutionHandler(new ThreadPoolExecutor.AbortPolicy());
        taskExecutor.initialize();                                              //初始化
        return taskExecutor;
    }
}


```

**创建调用工具类**

```
package com.ushangxie.cca.common.lib.util;

import org.springframework.beans.BeansException;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.stereotype.Component;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * @author ljq
 * @date 2020/7/15
 */

@Component
public class SpringUtils implements ApplicationContextAware {<!-- -->

    private static ApplicationContext context;


    @Override
    public void setApplicationContext(ApplicationContext context) throws BeansException {<!-- -->
        setContext(context);
    }

    private synchronized static void setContext(ApplicationContext context) {<!-- -->
        SpringUtils.context = context;
    }

    public static Object getBean(String beanName) {<!-- -->
        return context.getBean(beanName);
    }

    public static &lt;T&gt; T getBean(Class&lt;T&gt; requiredType) {<!-- -->
        return context.getBean(requiredType);
    }

    public static HttpServletRequest getRequest() {<!-- -->
        ServletRequestAttributes servletRequestAttributes = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();
        return servletRequestAttributes == null ? null : servletRequestAttributes.getRequest();
    }

    public static HttpServletResponse getResponse() {<!-- -->
        ServletRequestAttributes servletRequestAttributes = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();
        return servletRequestAttributes == null ? null : servletRequestAttributes.getResponse();
    }
    


}


```

**在要使用的异步方法上添加异步注解**

```
@Async
public void sendNeedPayWxSubscribeMsgNotice(CcaCcFeesPayCollectPO po) {<!-- -->
//...内容
}

```

**调用异步方法**

```
SpringUtils.getBean(FeesOperationService.class).sendNeedPayWxSubscribeMsgNotice(rs);

```

### 走异步，但是事务没有提交，异步方法执行任务查询事务数据失败的解决办法

>  
 在需要执行异步方法外加上事务监听(TransactionSynchronizationManager.registerSynchronization())，等事务提交完成后在执行异步方法 


**参考代码如下：**

```
/**
 * 事务测试
 *
 * @return
 */
@Transactional(rollbackFor = Exception.class)
public boolean testTransactional1() {<!-- -->
 
 
    Warehouse warehouse = warehouseService.getById(1);
    warehouse.setUpdateTime(LocalDateTime.now());
    warehouseService.updateById(warehouse);
 
    TransactionSynchronizationManager.registerSynchronization(new TransactionSynchronization() {<!-- -->
        @Override
        public void afterCommit() {<!-- -->
            sendMsg();
        }
    });
 
    warehouseService.save(warehouse);
 
    return Boolean.TRUE;
}

```

### 配置线程池

```
@Bean
public ExecutorService getThreadPool() {<!-- -->
    return new ThreadPoolExecutor(
            50,
            200,
            30,
            TimeUnit.SECONDS,
            new ArrayBlockingQueue&lt;&gt;(50),
            r -&gt; new Thread(r) {<!-- -->
                @Override
                public void run() {<!-- -->
                    try {<!-- -->
                        r.run();
                    } catch (Exception e) {<!-- -->
                        log.error("异步错误消息：", e);
                    }
                }
            }
    );
}

```

### 拷贝 空值不拷贝

```
package com.ljq.cca.common.lib.util;

import org.springframework.beans.BeanUtils;
import org.springframework.beans.BeanWrapper;
import org.springframework.beans.BeanWrapperImpl;
import org.springframework.beans.BeansException;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.stereotype.Component;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.HashSet;
import java.util.Set;

@Component
public class SpringUtils implements ApplicationContextAware {<!-- -->

    private static ApplicationContext context;


    @Override
    public void setApplicationContext(ApplicationContext context) throws BeansException {<!-- -->
        setContext(context);
    }

    private synchronized static void setContext(ApplicationContext context) {<!-- -->
        SpringUtils.context = context;
    }

    public static Object getBean(String beanName) {<!-- -->
        return context.getBean(beanName);
    }

    public static &lt;T&gt; T getBean(Class&lt;T&gt; requiredType) {<!-- -->
        return context.getBean(requiredType);
    }

    public static HttpServletRequest getRequest() {<!-- -->
        ServletRequestAttributes servletRequestAttributes = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();
        return servletRequestAttributes == null ? null : servletRequestAttributes.getRequest();
    }

    public static HttpServletResponse getResponse() {<!-- -->
        ServletRequestAttributes servletRequestAttributes = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();
        return servletRequestAttributes == null ? null : servletRequestAttributes.getResponse();
    }

    public static String[] getNullPropertyNames(Object source) {<!-- -->
        final BeanWrapper src = new BeanWrapperImpl(source);
        java.beans.PropertyDescriptor[] pds = src.getPropertyDescriptors();

        Set&lt;String&gt; emptyNames = new HashSet&lt;String&gt;();
        for (java.beans.PropertyDescriptor pd : pds) {<!-- -->
            Object srcValue = src.getPropertyValue(pd.getName());
            if (srcValue == null) emptyNames.add(pd.getName());
        }
        String[] result = new String[emptyNames.size()];
        return emptyNames.toArray(result);
    }

    public static void copyPropertiesIgnoreNull(Object src, Object target) {<!-- -->
        BeanUtils.copyProperties(src, target, getNullPropertyNames(src));
    }


}


```

**如何使用**

```
SpringUtils.copyPropertiesIgnoreNull(olbArticle, articlePO);

```
