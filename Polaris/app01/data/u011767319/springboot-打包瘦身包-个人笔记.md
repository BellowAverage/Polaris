
--- 
title:  springboot-打包瘦身包-个人笔记 
tags: []
categories: [] 

---
springboot 的打包插件默认打的是fat jar包，也就是将所有依赖包都打包到jar包里，这就导致jar包非常的大，几十甚至上百M都有，在外网部署时如果网速慢，则文件上传就要耗掉很长的时间，这在紧急更新时是很难接受的，因此为减少部署项目包的文件大小，加快部署时的网络传输速度，在开发项目中采用spring-boot-thin-launcher 打包插件进行打包，关于此插件可，它在打包时，不会将依赖包打包进JAR包里，在启动APP时采用Maven的机制实时下载依赖包，从而减少包的体积，但也因此不采用脱机模式时会导致第一次启动时非常的久（下载依赖包）！ 要启用此插件，在pom.xml文件里进行如下配置：

```
&lt;build&gt;
        &lt;plugins&gt;
            &lt;plugin&gt;
                &lt;artifactId&gt;maven-compiler-plugin&lt;/artifactId&gt;
                &lt;configuration&gt;
                    &lt;source&gt;${
   <!-- -->java.version}&lt;/source&gt;
                    &lt;target&gt;${
   <!-- -->java.version}&lt;/target&gt;
                    &lt;encoding&gt;UTF-8&lt;/encoding&gt;
                &lt;/configuration&gt;
            &lt;/plugin&gt;
            &lt;plugin&gt;
                &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
                &lt;artifactId&gt;spring-boot-maven-plugin&lt;/artifactId&gt;
                &lt;version&gt;${
   <!-- -->spring-boot.version}
```
