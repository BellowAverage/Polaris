
--- 
title:  idea maven 父子项目 common模块 打包报错 
tags: []
categories: [] 

---1. common 模块
```
Failed to execute goal org.springframework.boot:spring-boot-maven-plugin:2.1.8.RELEASE:repackage (repackage) on project online-common: Execution repackage of goal org.springframework.boot:spring-boot-maven-plugin:2.1.8.RELEASE:repackage failed: Unable to find a single main class from the following candidates [com.example.onlinecommon.valatiledemo.Main, com.example.onlinecommon.valatiledemo.MainDemo, com.example.onlinecommon.valatiledemo.MyRunnable]


```

根据以上提示，我删除了类 Main、MainDemo、MyRunnable中的main方法。 2. 继续打包

```
Failed to execute goal org.springframework.boot:spring-boot-maven-plugin:2.1.8.RELEASE:repackage (repackage) on project online-common: Execution repackage of goal org.springframework.boot:spring-boot-maven-plugin:2.1.8.RELEASE:repackage failed: Unable to find main class


```

以上提示：我的common模块缺少main类，因为这是我的工具模块，因此不需要启动类。我把打包文件更改为

```
 &lt;build&gt;
        &lt;plugins&gt;
            &lt;plugin&gt;
                &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
                &lt;artifactId&gt;spring-boot-maven-plugin&lt;/artifactId&gt;
                &lt;configuration&gt;
                    &lt;skip&gt;true&lt;/skip&gt;
                &lt;/configuration&gt;
            &lt;/plugin&gt;
        &lt;/plugins&gt;
    &lt;/build&gt;

```

跳过此模块的打包即可
