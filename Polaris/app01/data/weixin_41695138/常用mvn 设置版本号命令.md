
--- 
title:  常用mvn 设置版本号命令 
tags: []
categories: [] 

---
转载  再次记录一下，方便后期查看 对于多module项目，可以使用versions-maven-plugin的mvn versions：set命令升级版本号 统一修改pom的版本号，及子模块依赖的版本号：mvn versions:set -DnewVersion=xxx 如：升级版本： mvn versions:set -DnewVersion=0.0.12 如果有问题，可以回退：mvn versions:revert 如果没问题，然后执行如下命令：mvn versions:commit


