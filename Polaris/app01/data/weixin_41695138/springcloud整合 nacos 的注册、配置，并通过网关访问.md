
--- 
title:  springcloud整合 nacos 的注册、配置，并通过网关访问 
tags: []
categories: [] 

---
### nacos 的启动
1. 下载安装 可以参考 1. 注意事项： springcloud 整合新版本seata、nacos，如果只整合 nacos,则只需要参考nacos 配置。有关 seata的不用管
如果没有修改 startup.cmd 的 MODE值（set MODE=“standalone”），在单机的情况下，会出现： <img src="https://img-blog.csdnimg.cn/d52342e9e1aa48e3a99e71c369f86f9b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

```

org.springframework.context.ApplicationContextException: Unable to start web server; nested exception is org.springframework.boot.web.server.WebServerException: Unable to start embedded Tomcat
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.onRefresh(ServletWebServerApplicationContext.java:156)
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:544)
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:141)
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:744)
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:391)
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:312)
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:1215)
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:1204)
        at com.alibaba.nacos.Nacos.main(Nacos.java:35)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:498)
        at org.springframework.boot.loader.MainMethodRunner.run(MainMethodRunner.java:49)
        at org.springframework.boot.loader.Launcher.launch(Launcher.java:108)
        at org.springframework.boot.loader.Launcher.launch(Launcher.java:58)
        at org.springframework.boot.loader.PropertiesLauncher.main(PropertiesLauncher.java:467)
Caused by: org.springframework.boot.web.server.WebServerException: Unable to start embedded Tomcat
        at org.springframework.boot.web.embedded.tomcat.TomcatWebServer.initialize(TomcatWebServer.java:124)
        at org.springframework.boot.web.embedded.tomcat.TomcatWebServer.&lt;init&gt;(TomcatWebServer.java:86)
        at org.springframework.boot.web.embedded.tomcat.TomcatServletWebServerFactory.getTomcatWebServer(TomcatServletWebServerFactory.java:416)
        at org.springframework.boot.web.embedded.tomcat.TomcatServletWebServerFactory.getWebServer(TomcatServletWebServerFactory.java:180)
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.createWebServer(ServletWebServerApplicationContext.java:180)
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.onRefresh(ServletWebServerApplicationContext.java:153)
        ... 16 common frames omitted
Caused by: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'distroFilterRegistration' defined in class path resource [com/alibaba/nacos/naming/web/NamingConfig.class]: Bean instantiation via factory method failed; nested exception is org.springframework.beans.BeanInstantiationException: Failed to instantiate [org.springframework.boot.web.servlet.FilterRegistrationBean]: Factory method 'distroFilterRegistration' threw exception; nested exception is org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'distroFilter': Unsatisfied dependency expressed through field 'distroMapper'; nested exception is org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'distroMapper' defined in URL [jar:file:/E:/ruoyi/code/testcode/tool/nacos/target/nacos-server.jar!/BOOT-INF/lib/nacos-naming-2.0.3.jar!/com/alibaba/nacos/naming/core/DistroMapper.class]: Unsatisfied dependency expressed through constructor parameter 0; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'serverMemberManager' defined in URL [jar:file:/E:/ruoyi/code/testcode/tool/nacos/target/nacos-server.jar!/BOOT-INF/lib/nacos-core-2.0.3.jar!/com/alibaba/nacos/core/cluster/ServerMemberManager.class]: Bean instantiation via constructor failed; nested exception is org.springframework.beans.BeanInstantiationException: Failed to instantiate [com.alibaba.nacos.core.cluster.ServerMemberManager]: Constructor threw exception; nested exception is ErrCode:500, ErrMsg:jmenv.tbsite.net
        at org.springframework.beans.factory.support.ConstructorResolver.instantiate(ConstructorResolver.java:627)
        at org.springframework.beans.factory.support.ConstructorResolver.instantiateUsingFactoryMethod(ConstructorResolver.java:456)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.instantiateUsingFactoryMethod(AbstractAutowireCapableBeanFactory.java:1318)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBeanInstance(AbstractAutowireCapableBeanFactory.java:1158)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:554)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:514)
        at org.springframework.beans.factory.support.AbstractBeanFactory.lambda$doGetBean$0(AbstractBeanFactory.java:321)
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:234)
        at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:319)
        at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:204)
        at org.springframework.boot.web.servlet.ServletContextInitializerBeans.getOrderedBeansOfType(ServletContextInitializerBeans.java:211)
        at org.springframework.boot.web.servlet.ServletContextInitializerBeans.getOrderedBeansOfType(ServletContextInitializerBeans.java:202)
        at org.springframework.boot.web.servlet.ServletContextInitializerBeans.addServletContextInitializerBeans(ServletContextInitializerBeans.java:96)
        at org.springframework.boot.web.servlet.ServletContextInitializerBeans.&lt;init&gt;(ServletContextInitializerBeans.java:85)
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.getServletContextInitializerBeans(ServletWebServerApplicationContext.java:253)
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.selfInitialize(ServletWebServerApplicationContext.java:227)
        at org.springframework.boot.web.embedded.tomcat.TomcatStarter.onStartup(TomcatStarter.java:53)
        at org.apache.catalina.core.StandardContext.startInternal(StandardContext.java:5128)
        at org.apache.catalina.util.LifecycleBase.start(LifecycleBase.java:183)
        at org.apache.catalina.core.ContainerBase$StartChild.call(ContainerBase.java:1384)
        at org.apache.catalina.core.ContainerBase$StartChild.call(ContainerBase.java:1374)
        at java.util.concurrent.FutureTask.run(FutureTask.java:266)
        at org.apache.tomcat.util.threads.InlineExecutorService.execute(InlineExecutorService.java:75)
        at java.util.concurrent.AbstractExecutorService.submit(AbstractExecutorService.java:134)
        at org.apache.catalina.core.ContainerBase.startInternal(ContainerBase.java:909)
        at org.apache.catalina.core.StandardHost.startInternal(StandardHost.java:843)
        at org.apache.catalina.util.LifecycleBase.start(LifecycleBase.java:183)
        at org.apache.catalina.core.ContainerBase$StartChild.call(ContainerBase.java:1384)
        at org.apache.catalina.core.ContainerBase$StartChild.call(ContainerBase.java:1374)
        at java.util.concurrent.FutureTask.run(FutureTask.java:266)
        at org.apache.tomcat.util.threads.InlineExecutorService.execute(InlineExecutorService.java:75)
        at java.util.concurrent.AbstractExecutorService.submit(AbstractExecutorService.java:134)
        at org.apache.catalina.core.ContainerBase.startInternal(ContainerBase.java:909)
        at org.apache.catalina.core.StandardEngine.startInternal(StandardEngine.java:262)
        at org.apache.catalina.util.LifecycleBase.start(LifecycleBase.java:183)
        at org.apache.catalina.core.StandardService.startInternal(StandardService.java:421)
        at org.apache.catalina.util.LifecycleBase.start(LifecycleBase.java:183)
        at org.apache.catalina.core.StandardServer.startInternal(StandardServer.java:930)
        at org.apache.catalina.util.LifecycleBase.start(LifecycleBase.java:183)
        at org.apache.catalina.startup.Tomcat.start(Tomcat.java:486)
        at org.springframework.boot.web.embedded.tomcat.TomcatWebServer.initialize(TomcatWebServer.java:105)
        ... 21 common frames omitted
Caused by: org.springframework.beans.BeanInstantiationException: Failed to instantiate [org.springframework.boot.web.servlet.FilterRegistrationBean]: Factory method 'distroFilterRegistration' threw exception; nested exception is org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'distroFilter': Unsatisfied dependency expressed through field 'distroMapper'; nested exception is org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'distroMapper' defined in URL [jar:file:/E:/ruoyi/code/testcode/tool/nacos/target/nacos-server.jar!/BOOT-INF/lib/nacos-naming-2.0.3.jar!/com/alibaba/nacos/naming/core/DistroMapper.class]: Unsatisfied dependency expressed through constructor parameter 0; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'serverMemberManager' defined in URL [jar:file:/E:/ruoyi/code/testcode/tool/nacos/target/nacos-server.jar!/BOOT-INF/lib/nacos-core-2.0.3.jar!/com/alibaba/nacos/core/cluster/ServerMemberManager.class]: Bean instantiation via constructor failed; nested exception is org.springframework.beans.BeanInstantiationException: Failed to instantiate [com.alibaba.nacos.core.cluster.ServerMemberManager]: Constructor threw exception; nested exception is ErrCode:500, ErrMsg:jmenv.tbsite.net
        at org.springframework.beans.factory.support.SimpleInstantiationStrategy.instantiate(SimpleInstantiationStrategy.java:185)
        at org.springframework.beans.factory.support.ConstructorResolver.instantiate(ConstructorResolver.java:622)
        ... 61 common frames omitted
Caused by: org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'distroFilter': Unsatisfied dependency expressed through field 'distroMapper'; nested exception is org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'distroMapper' defined in URL [jar:file:/E:/ruoyi/code/testcode/tool/nacos/target/nacos-server.jar!/BOOT-INF/lib/nacos-naming-2.0.3.jar!/com/alibaba/nacos/naming/core/DistroMapper.class]: Unsatisfied dependency expressed through constructor parameter 0; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'serverMemberManager' defined in URL [jar:file:/E:/ruoyi/code/testcode/tool/nacos/target/nacos-server.jar!/BOOT-INF/lib/nacos-core-2.0.3.jar!/com/alibaba/nacos/core/cluster/ServerMemberManager.class]: Bean instantiation via constructor failed; nested exception is org.springframework.beans.BeanInstantiationException: Failed to instantiate [com.alibaba.nacos.core.cluster.ServerMemberManager]: Constructor threw exception; nested exception is ErrCode:500, ErrMsg:jmenv.tbsite.net
        at org.springframework.beans.factory.annotation.AutowiredAnnotationBeanPostProcessor$AutowiredFieldElement.inject(AutowiredAnnotationBeanPostProcessor.java:598)
        at org.springframework.beans.factory.annotation.InjectionMetadata.inject(InjectionMetadata.java:90)
        at org.springframework.beans.factory.annotation.AutowiredAnnotationBeanPostProcessor.postProcessProperties(AutowiredAnnotationBeanPostProcessor.java:376)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.populateBean(AbstractAutowireCapableBeanFactory.java:1402)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:591)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:514)
        at org.springframework.beans.factory.support.AbstractBeanFactory.lambda$doGetBean$0(AbstractBeanFactory.java:321)
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:234)
        at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:319)
        at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:199)
        at org.springframework.context.annotation.ConfigurationClassEnhancer$BeanMethodInterceptor.resolveBeanReference(ConfigurationClassEnhancer.java:394)
        at org.springframework.context.annotation.ConfigurationClassEnhancer$BeanMethodInterceptor.intercept(ConfigurationClassEnhancer.java:366)
        at com.alibaba.nacos.naming.web.NamingConfig$$EnhancerBySpringCGLIB$$44e47c43.distroFilter(&lt;generated&gt;)
        at com.alibaba.nacos.naming.web.NamingConfig.distroFilterRegistration(NamingConfig.java:42)
        at com.alibaba.nacos.naming.web.NamingConfig$$EnhancerBySpringCGLIB$$44e47c43.CGLIB$distroFilterRegistration$0(&lt;generated&gt;)
        at com.alibaba.nacos.naming.web.NamingConfig$$EnhancerBySpringCGLIB$$44e47c43$$FastClassBySpringCGLIB$$80b98402.invoke(&lt;generated&gt;)
        at org.springframework.cglib.proxy.MethodProxy.invokeSuper(MethodProxy.java:244)
        at org.springframework.context.annotation.ConfigurationClassEnhancer$BeanMethodInterceptor.intercept(ConfigurationClassEnhancer.java:363)
        at com.alibaba.nacos.naming.web.NamingConfig$$EnhancerBySpringCGLIB$$44e47c43.distroFilterRegistration(&lt;generated&gt;)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:498)
        at org.springframework.beans.factory.support.SimpleInstantiationStrategy.instantiate(SimpleInstantiationStrategy.java:154)
        ... 62 common frames omitted
Caused by: org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'distroMapper' defined in URL [jar:file:/E:/ruoyi/code/testcode/tool/nacos/target/nacos-server.jar!/BOOT-INF/lib/nacos-naming-2.0.3.jar!/com/alibaba/nacos/naming/core/DistroMapper.class]: Unsatisfied dependency expressed through constructor parameter 0; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'serverMemberManager' defined in URL [jar:file:/E:/ruoyi/code/testcode/tool/nacos/target/nacos-server.jar!/BOOT-INF/lib/nacos-core-2.0.3.jar!/com/alibaba/nacos/core/cluster/ServerMemberManager.class]: Bean instantiation via constructor failed; nested exception is org.springframework.beans.BeanInstantiationException: Failed to instantiate [com.alibaba.nacos.core.cluster.ServerMemberManager]: Constructor threw exception; nested exception is ErrCode:500, ErrMsg:jmenv.tbsite.net
        at org.springframework.beans.factory.support.ConstructorResolver.createArgumentArray(ConstructorResolver.java:769)
        at org.springframework.beans.factory.support.ConstructorResolver.autowireConstructor(ConstructorResolver.java:218)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.autowireConstructor(AbstractAutowireCapableBeanFactory.java:1338)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBeanInstance(AbstractAutowireCapableBeanFactory.java:1185)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:554)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:514)
        at org.springframework.beans.factory.support.AbstractBeanFactory.lambda$doGetBean$0(AbstractBeanFactory.java:321)
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:234)
        at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:319)
        at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:199)
        at org.springframework.beans.factory.config.DependencyDescriptor.resolveCandidate(DependencyDescriptor.java:277)
        at org.springframework.beans.factory.support.DefaultListableBeanFactory.doResolveDependency(DefaultListableBeanFactory.java:1276)
        at org.springframework.beans.factory.support.DefaultListableBeanFactory.resolveDependency(DefaultListableBeanFactory.java:1196)
        at org.springframework.beans.factory.annotation.AutowiredAnnotationBeanPostProcessor$AutowiredFieldElement.inject(AutowiredAnnotationBeanPostProcessor.java:595)
        ... 85 common frames omitted
Caused by: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'serverMemberManager' defined in URL [jar:file:/E:/ruoyi/code/testcode/tool/nacos/target/nacos-server.jar!/BOOT-INF/lib/nacos-core-2.0.3.jar!/com/alibaba/nacos/core/cluster/ServerMemberManager.class]: Bean instantiation via constructor failed; nested exception is org.springframework.beans.BeanInstantiationException: Failed to instantiate [com.alibaba.nacos.core.cluster.ServerMemberManager]: Constructor threw exception; nested exception is ErrCode:500, ErrMsg:jmenv.tbsite.net
        at org.springframework.beans.factory.support.ConstructorResolver.instantiate(ConstructorResolver.java:304)
        at org.springframework.beans.factory.support.ConstructorResolver.autowireConstructor(ConstructorResolver.java:285)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.autowireConstructor(AbstractAutowireCapableBeanFactory.java:1338)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBeanInstance(AbstractAutowireCapableBeanFactory.java:1185)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:554)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:514)
        at org.springframework.beans.factory.support.AbstractBeanFactory.lambda$doGetBean$0(AbstractBeanFactory.java:321)
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:234)
        at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:319)
        at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:199)
        at org.springframework.beans.factory.config.DependencyDescriptor.resolveCandidate(DependencyDescriptor.java:277)
        at org.springframework.beans.factory.support.DefaultListableBeanFactory.doResolveDependency(DefaultListableBeanFactory.java:1276)
        at org.springframework.beans.factory.support.DefaultListableBeanFactory.resolveDependency(DefaultListableBeanFactory.java:1196)
        at org.springframework.beans.factory.support.ConstructorResolver.resolveAutowiredArgument(ConstructorResolver.java:857)
        at org.springframework.beans.factory.support.ConstructorResolver.createArgumentArray(ConstructorResolver.java:760)
        ... 98 common frames omitted
Caused by: org.springframework.beans.BeanInstantiationException: Failed to instantiate [com.alibaba.nacos.core.cluster.ServerMemberManager]: Constructor threw exception; nested exception is ErrCode:500, ErrMsg:jmenv.tbsite.net
        at org.springframework.beans.BeanUtils.instantiateClass(BeanUtils.java:187)
        at org.springframework.beans.factory.support.SimpleInstantiationStrategy.instantiate(SimpleInstantiationStrategy.java:117)
        at org.springframework.beans.factory.support.ConstructorResolver.instantiate(ConstructorResolver.java:300)
        ... 112 common frames omitted
Caused by: com.alibaba.nacos.api.exception.NacosException: java.net.UnknownHostException: jmenv.tbsite.net
        at com.alibaba.nacos.core.cluster.lookup.AddressServerMemberLookup.run(AddressServerMemberLookup.java:150)
        at com.alibaba.nacos.core.cluster.lookup.AddressServerMemberLookup.doStart(AddressServerMemberLookup.java:98)
        at com.alibaba.nacos.core.cluster.AbstractMemberLookup.start(AbstractMemberLookup.java:53)
        at com.alibaba.nacos.core.cluster.ServerMemberManager.initAndStartLookup(ServerMemberManager.java:181)
        at com.alibaba.nacos.core.cluster.ServerMemberManager.init(ServerMemberManager.java:161)
        at com.alibaba.nacos.core.cluster.ServerMemberManager.&lt;init&gt;(ServerMemberManager.java:142)
        at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
        at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)
        at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
        at java.lang.reflect.Constructor.newInstance(Constructor.java:423)
        at org.springframework.beans.BeanUtils.instantiateClass(BeanUtils.java:175)
        ... 114 common frames omitted
Caused by: java.net.UnknownHostException: jmenv.tbsite.net
        at java.net.AbstractPlainSocketImpl.connect(AbstractPlainSocketImpl.java:184)
        at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:172)
        at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:392)
        at java.net.Socket.connect(Socket.java:589)
        at sun.net.NetworkClient.doConnect(NetworkClient.java:175)
        at sun.net.www.http.HttpClient.openServer(HttpClient.java:463)
        at sun.net.www.http.HttpClient.openServer(HttpClient.java:558)
        at sun.net.www.http.HttpClient.&lt;init&gt;(HttpClient.java:242)
        at sun.net.www.http.HttpClient.New(HttpClient.java:339)
        at sun.net.www.http.HttpClient.New(HttpClient.java:357)
        at sun.net.www.protocol.http.HttpURLConnection.getNewHttpClient(HttpURLConnection.java:1220)
        at sun.net.www.protocol.http.HttpURLConnection.plainConnect0(HttpURLConnection.java:1156)
        at sun.net.www.protocol.http.HttpURLConnection.plainConnect(HttpURLConnection.java:1050)
        at sun.net.www.protocol.http.HttpURLConnection.connect(HttpURLConnection.java:984)
        at com.alibaba.nacos.common.http.client.request.JdkHttpClientRequest.execute(JdkHttpClientRequest.java:114)
        at com.alibaba.nacos.common.http.client.NacosRestTemplate.execute(NacosRestTemplate.java:482)
        at com.alibaba.nacos.common.http.client.NacosRestTemplate.get(NacosRestTemplate.java:72)
        at com.alibaba.nacos.core.cluster.lookup.AddressServerMemberLookup.syncFromAddressUrl(AddressServerMemberLookup.java:173)
        at com.alibaba.nacos.core.cluster.lookup.AddressServerMemberLookup.run(AddressServerMemberLookup.java:141)
        ... 124 common frames omitted
2021-12-28 15:24:01,971 WARN [WatchFileCenter] start close

2021-12-28 15:24:01,972 WARN [WatchFileCenter] start to shutdown this watcher which is watch : E:\ruoyi\code\testcode\tool\nacos\conf

2021-12-28 15:24:01,980 WARN [WatchFileCenter] already closed

2021-12-28 15:24:01,981 WARN [NotifyCenter] Start destroying Publisher

2021-12-28 15:24:01,983 WARN [NotifyCenter] Destruction of the end

2021-12-28 15:24:01,984 ERROR Nacos failed to start, please see E:\ruoyi\code\testcode\tool\nacos\logs\nacos.log for more details.


```

因为 nacos 默认是集群环境， 如果是本机开发使用的情况下，则需要更改 moded

### springcloud整合 nacos 的注册，并通过网关访问
1. 版本要求： spring-cloud-dependencies Hoxton.SR9； spring-cloud-alibaba-dependencies 2.2.6.RELEASE； spring-boot-starter-parent 2.3.2.RELEASE；整合的时间版本如果不一致，则会出现各种各样的奇怪问题1. 新建父项目： parent, pom文件：
```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd"&gt;
    &lt;modelVersion&gt;4.0.0&lt;/modelVersion&gt;
    &lt;parent&gt;
        &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
        &lt;artifactId&gt;spring-boot-starter-parent&lt;/artifactId&gt;
&lt;!--        &lt;version&gt;2.6.2&lt;/version&gt;--&gt;
        &lt;version&gt;2.3.2.RELEASE&lt;/version&gt;
        &lt;relativePath/&gt; &lt;!-- lookup parent from repository --&gt;
    &lt;/parent&gt;

    &lt;groupId&gt;com.example&lt;/groupId&gt;
    &lt;artifactId&gt;parent&lt;/artifactId&gt;
    &lt;version&gt;0.0.1&lt;/version&gt;
    &lt;name&gt;parent&lt;/name&gt;
    &lt;description&gt;父项目&lt;/description&gt;
    &lt;packaging&gt;pom&lt;/packaging&gt;

    &lt;modules&gt;
        &lt;module&gt;gateway&lt;/module&gt;
        &lt;module&gt;project&lt;/module&gt;
    &lt;/modules&gt;
    
    &lt;properties&gt;
        &lt;java.version&gt;1.8&lt;/java.version&gt;
    &lt;/properties&gt;

    &lt;dependencyManagement&gt;
        &lt;dependencies&gt;
            &lt;!-- SpringCloud 微服务 --&gt;
            &lt;dependency&gt;
                &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
                &lt;artifactId&gt;spring-cloud-dependencies&lt;/artifactId&gt;
                &lt;version&gt;Hoxton.SR9&lt;/version&gt;
                &lt;type&gt;pom&lt;/type&gt;
                &lt;scope&gt;import&lt;/scope&gt;
            &lt;/dependency&gt;

            &lt;!-- SpringCloud Alibaba 微服务 --&gt;
            &lt;dependency&gt;
                &lt;groupId&gt;com.alibaba.cloud&lt;/groupId&gt;
                &lt;artifactId&gt;spring-cloud-alibaba-dependencies&lt;/artifactId&gt;
                &lt;version&gt;2.2.6.RELEASE&lt;/version&gt;
                &lt;type&gt;pom&lt;/type&gt;
                &lt;scope&gt;import&lt;/scope&gt;
            &lt;/dependency&gt;
        &lt;/dependencies&gt;
    &lt;/dependencyManagement&gt;

    &lt;dependencies&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter&lt;/artifactId&gt;
        &lt;/dependency&gt;
    &lt;/dependencies&gt;

    &lt;build&gt;
        &lt;plugins&gt;
            &lt;plugin&gt;
                &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
                &lt;artifactId&gt;spring-boot-maven-plugin&lt;/artifactId&gt;
            &lt;/plugin&gt;
        &lt;/plugins&gt;
    &lt;/build&gt;

&lt;/project&gt;


```
1. 新建 gateway 子服务： pom文件：
```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd"&gt;
    &lt;modelVersion&gt;4.0.0&lt;/modelVersion&gt;
    &lt;parent&gt;
        &lt;groupId&gt;com.example&lt;/groupId&gt;
        &lt;artifactId&gt;parent&lt;/artifactId&gt;
        &lt;version&gt;0.0.1&lt;/version&gt;
    &lt;/parent&gt;

    &lt;groupId&gt;com.example&lt;/groupId&gt;
    &lt;artifactId&gt;gateway&lt;/artifactId&gt;
    &lt;version&gt;0.0.1&lt;/version&gt;
    &lt;name&gt;gateway&lt;/name&gt;
    &lt;description&gt;网关&lt;/description&gt;

    &lt;properties&gt;
        &lt;java.version&gt;1.8&lt;/java.version&gt;
    &lt;/properties&gt;

    &lt;dependencies&gt;
&lt;!--        &lt;dependency&gt;--&gt;
&lt;!--            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;--&gt;
&lt;!--            &lt;artifactId&gt;spring-boot-starter-web&lt;/artifactId&gt;--&gt;
&lt;!--        &lt;/dependency&gt;--&gt;

        &lt;!-- springcloud alibaba nacos discovery --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;com.alibaba.cloud&lt;/groupId&gt;
            &lt;artifactId&gt;spring-cloud-starter-alibaba-nacos-discovery&lt;/artifactId&gt;
        &lt;/dependency&gt;

        &lt;!-- spring cloud gateway 依赖 --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
            &lt;artifactId&gt;spring-cloud-starter-gateway&lt;/artifactId&gt;
        &lt;/dependency&gt;

    &lt;/dependencies&gt;

    &lt;build&gt;
        &lt;plugins&gt;
            &lt;plugin&gt;
                &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
                &lt;artifactId&gt;spring-boot-maven-plugin&lt;/artifactId&gt;
            &lt;/plugin&gt;
        &lt;/plugins&gt;
    &lt;/build&gt;

&lt;/project&gt;


```

配置文件为： application.yml

```
server:
  port: 8001
spring:
  application:
    name: gateway
  cloud:
    nacos:
      discovery:
        server-addr: 127.0.0.1:8848
    gateway:
      routes:
        # 认证中心
        - id: project
          uri: lb://project
          predicates:
            - Path=/project/**
          filters:
            - StripPrefix=1

```
1. 新建 project子服务：pom文件
```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd"&gt;
    &lt;modelVersion&gt;4.0.0&lt;/modelVersion&gt;
    &lt;parent&gt;
        &lt;groupId&gt;com.example&lt;/groupId&gt;
        &lt;artifactId&gt;parent&lt;/artifactId&gt;
        &lt;version&gt;0.0.1&lt;/version&gt;
    &lt;/parent&gt;

    &lt;groupId&gt;com.example&lt;/groupId&gt;
    &lt;artifactId&gt;project&lt;/artifactId&gt;
    &lt;version&gt;0.0.1&lt;/version&gt;
    &lt;name&gt;project&lt;/name&gt;
    &lt;description&gt;商品服务&lt;/description&gt;


    &lt;properties&gt;
        &lt;java.version&gt;1.8&lt;/java.version&gt;
    &lt;/properties&gt;

    &lt;dependencies&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-web&lt;/artifactId&gt;
        &lt;/dependency&gt;

        &lt;!-- springcloud alibaba nacos discovery --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;com.alibaba.cloud&lt;/groupId&gt;
            &lt;artifactId&gt;spring-cloud-starter-alibaba-nacos-discovery&lt;/artifactId&gt;
        &lt;/dependency&gt;

        &lt;!-- lombok --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.projectlombok&lt;/groupId&gt;
            &lt;artifactId&gt;lombok&lt;/artifactId&gt;
            &lt;version&gt;1.16.22&lt;/version&gt;
        &lt;/dependency&gt;
        
    &lt;/dependencies&gt;

    &lt;build&gt;
        &lt;plugins&gt;
            &lt;plugin&gt;
                &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
                &lt;artifactId&gt;spring-boot-maven-plugin&lt;/artifactId&gt;
            &lt;/plugin&gt;
        &lt;/plugins&gt;
    &lt;/build&gt;

&lt;/project&gt;


```

配置文件为： application.yml

```
server:
  port: 8002
spring:
  application:
    name: project
  cloud:
    nacos:
      discovery:
        server-addr: 127.0.0.1:8848


```
1. 新建 TestController
```
package com.example.project.controller;

import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 *  测试控制器
 */
@RestController
@RequestMapping("/testController")
@Slf4j
public class TestController {<!-- -->


    /**
     *  该服务的测试代码
     * @return
     */
    @GetMapping("/test")
    public String test(){<!-- -->
        String str = "project 开始测试代码";
        log.info(str);
        return str;
    }


    /**
     *  该服务的测试代码
     * @return
     */
    @PostMapping("/test02")
    public String test02(){<!-- -->
        String str = "project 开始测试代码";
        log.info(str);
        return str;
    }
}


```

新建完服务之后的目录结构 <img src="https://img-blog.csdnimg.cn/7fd352488e21491594fe8773dc650a47.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_16,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
1. 启动 nacos, 和gateway project这两个服务 <img src="https://img-blog.csdnimg.cn/62cb661a40ec489fa07aaceaca92e18f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 则说明这两个服务已经注册成功1. 访问 http://localhost:8001/project/testController/test ， 测试之 <img src="https://img-blog.csdnimg.cn/260aef131c6e45b1aac40e242b6eb2ab.png" alt="在这里插入图片描述"> 出现此图，则说明测试成功
### 总结一下：
1. 引入 gateway 依赖：
```
    &lt;!-- spring cloud gateway 依赖 --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
            &lt;artifactId&gt;spring-cloud-starter-gateway&lt;/artifactId&gt;
        &lt;/dependency&gt;

```

引入nacos依赖注册：

```
 &lt;dependency&gt;
            &lt;groupId&gt;com.alibaba.cloud&lt;/groupId&gt;
            &lt;artifactId&gt;spring-cloud-starter-alibaba-nacos-discovery&lt;/artifactId&gt;
        &lt;/dependency&gt;

```
1. 在gateway 服务中，如果依赖中有spring-boot-starter-web，则会出现一下异常
```
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-web&lt;/artifactId&gt;
        &lt;/dependency&gt;

```

<img src="https://img-blog.csdnimg.cn/4196b24c99894759af6983444d534461.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

```
Spring MVC found on classpath, which is incompatible with Spring Cloud Gateway at this time. Please remove spring-boot-starter-web dependency.

**********************************************************


2021-12-28 15:48:51.222  INFO 4136 --- [           main] o.s.cloud.commons.util.InetUtils         : Cannot determine local hostname
2021-12-28 15:48:52.751  INFO 4136 --- [           main] o.s.cloud.commons.util.InetUtils         : Cannot determine local hostname
2021-12-28 15:48:53.472  WARN 4136 --- [           main] ConfigServletWebServerApplicationContext : Exception encountered during context initialization - cancelling refresh attempt: org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'routeDefinitionRouteLocator' defined in class path resource [org/springframework/cloud/gateway/config/GatewayAutoConfiguration.class]: Unsatisfied dependency expressed through method 'routeDefinitionRouteLocator' parameter 1; nested exception is org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'modifyRequestBodyGatewayFilterFactory' defined in class path resource [org/springframework/cloud/gateway/config/GatewayAutoConfiguration.class]: Unsatisfied dependency expressed through method 'modifyRequestBodyGatewayFilterFactory' parameter 0; nested exception is org.springframework.beans.factory.NoSuchBeanDefinitionException: No qualifying bean of type 'org.springframework.http.codec.ServerCodecConfigurer' available: expected at least 1 bean which qualifies as autowire candidate. Dependency annotations: {<!-- -->}
2021-12-28 15:48:53.475  INFO 4136 --- [           main] o.apache.catalina.core.StandardService   : Stopping service [Tomcat]
2021-12-28 15:48:53.487  INFO 4136 --- [           main] ConditionEvaluationReportLoggingListener : 

Error starting ApplicationContext. To display the conditions report re-run your application with 'debug' enabled.
2021-12-28 15:48:53.813 ERROR 4136 --- [           main] o.s.b.d.LoggingFailureAnalysisReporter   : 

***************************
APPLICATION FAILED TO START
***************************

Description:

Parameter 0 of method modifyRequestBodyGatewayFilterFactory in org.springframework.cloud.gateway.config.GatewayAutoConfiguration required a bean of type 'org.springframework.http.codec.ServerCodecConfigurer' that could not be found.


Action:

Consider defining a bean of type 'org.springframework.http.codec.ServerCodecConfigurer' in your configuration.

Disconnected from the target VM, address: '127.0.0.1:50609', transport: 'socket'

Process finished with exit code 1


```

出现则情况，移除spring-boot-starter-web依赖即可

### springcloud整合 nacos 的配置
1. 引入依赖
```
&lt;!-- springcloud alibaba nacos config --&gt;
&lt;dependency&gt;
	&lt;groupId&gt;com.alibaba.cloud&lt;/groupId&gt;
	&lt;artifactId&gt;spring-cloud-starter-alibaba-nacos-config&lt;/artifactId&gt;
&lt;/dependency&gt;

```
1. 在 discovery 后面追加nacos的配置
```
# Spring
spring:
  application:
    # 应用名称
    name: project
  profiles:
    # 环境配置
    active: dev
  cloud:
    nacos:
      discovery:
        # 服务注册地址
        server-addr: 127.0.0.1:8848
      config:
        # 配置中心地址
        server-addr: 127.0.0.1:8848
        # 配置文件格式
        file-extension: yml
        # 共享配置
        shared-configs:
          - application-${<!-- -->spring.profiles.active}.${<!-- -->spring.cloud.nacos.config.file-extension}

```

<img src="https://img-blog.csdnimg.cn/c32cc506cbeb46f5882ae6486aac19cd.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
1. 在nacos中 新建一个配置文件 project-dev.yml <img src="https://img-blog.csdnimg.cn/20cf63b665494c76a9ec4cb43b8e884d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">1. 新建 TestControllerDemo
```

import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
//@RefreshScope //动态刷新配置  需要的时候 可以打开注释
public class TestControllerDemo {<!-- -->

    @Value("${test.name}")
    private String name;

    @Value("${test.version}")
    private String version;

    @GetMapping("info")
    public String get() {<!-- -->
        return name + version;
    }




```
1. 访问请求测试之 http://localhost:8001/info <img src="https://img-blog.csdnimg.cn/b112e407d43f430eaddd1bb56c202a67.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">