
--- 
title:  [Maven] maven lifecycle/maven 生命周期（执行阶段） 
tags: []
categories: [] 

---
>  
 狠狠地补Maven 


maven中，当给定一个阶段时，Maven 将执行序列中的每个阶段，直到并包括定义的那个阶段。例如，如果你执行编译阶段compile，实际执行的阶段是:

```
validate 验证
generate-sources 生成源
process-sources 过程源
generate-resources 生成资源
process-resources 过程资源
compile 编译

```

## Maven执行阶段顺序（生命周期）

### 一、默认的生命周期列表

1.validate 验证项目是否提供所有必要信息 2.compile 编译项目的源代码，一般是编译scr/main/java或是scr/test/java里面的文件 3.test 使用合适的单元测试框架测试已编译的源代码。这些测试不应要求打包或部署代码 4.package 获取已编译的代码并将其打包为其可分发的格式，例如 JAR 5.vertify 进行任何检查，以验证包是否有效，是否符合质量标准 6.install 将将软件包安装到本地存储库中，用作本地其他项目的依赖项 7.deploy 复制最终的包至远程仓库 共享给其它开发人员和项目

### 二、另外的两个生命周期

1.clean clean用于清除之前构建生成的所有文件（target目录及目录内容） 2.site 为该项目生成站点文档

需要注意的一件有趣的事情是，阶段和目标可以按顺序执行。

```
mvn clean dependency:copy-dependencies package

```

参考文档:https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html
