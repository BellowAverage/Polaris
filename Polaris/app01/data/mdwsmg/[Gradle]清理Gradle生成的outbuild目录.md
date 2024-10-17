
--- 
title:  [Gradle]清理Gradle生成的out\build目录 
tags: []
categories: [] 

---
不懂gradle，遇到一个问题： SpringBoot 应用中，在修改了一个service后，bean的名称与引用也发生了变化，但是运行时还是使用的原来的bean。

gradle不知道是设置了什么，缓存没有更新。

### 在build.gradle文件添加

在build.gradle文件添加下列脚本后，在gralde选项卡，other下选择cleanBuildDir即可。
- 多模块项目，所有模块清理
```
allprojects {
    task cleanBuildDir(type: Delete) {
        delete "${projectDir}/build"
        delete "${projectDir}/out"
    }
}


```
- 当个模块项目清理
```
task cleanBuildDir(type: Delete) {
    delete "${projectDir}/build"
    delete "${projectDir}/out"
}

```

>  
 手动删除是一样的 

