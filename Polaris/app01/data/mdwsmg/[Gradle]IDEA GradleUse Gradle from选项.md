
--- 
title:  [Gradle]IDEA GradleUse Gradle from选项 
tags: []
categories: [] 

---
<s>不知道是百度的方式不对，还是我心态不好，最近总是搜不到想要的。烦闷</s> 关于idea gradle的 use gradle from 选项。gradle太久不用，做个备忘

官网文档链接点

### Use Gradle from

官方解释如下
- **gradle-wrapper.properties file**： 这是一个推荐的默认选项，使用Gradle包装器。 在这种情况下，你将Gradle版本的更新委托给Gradle，并在构建时获得Gradle的自动下载。这个选项还可以让你用精确的Gradle版本进行构建。Gradle版本被保存在你项目的gradle目录下的gradle-wrapper.properties文件中，并帮助你消除任何Gradle版本问题。
gradle-wrapper.properties 属性说明如下:

|属性|说明
|------
|distributionUrl|指定版本的gradle的下载地址
|zipStoreBase|下载的gradle-version-bin.zip所存放的位置
|zipStorePath|zipStoreBase指定的目录下的子目录
|distributionBase|gradle-version-bin.zip解压后文件存放的位置
|distributionPath|distributionBase指定的目录下的子目录

**zipStoreBase**和**distributionBase**有两种取值：**GRADLE_USER_HOME和PROJECT。** 其中，GRADLE_USER_HOME表示用户目录。 在**windows**下是%USERPROFILE%/.gradle，例如C:\Users&lt;user_name&gt;.gradle\。 在**linux**下是$HOME/.gradle，例如~/.gradle。

**PROJECT**表示工程的当前目录，即gradlew所在的目录。
-  **‘wrapper’ task in Gradle build script:** 选择这个选项可以根据wrapper任务的配置来配置Gradle包装器。如果你喜欢控制在项目中使用哪个Gradle版本，这可能很方便。 如果你使用了默认的Gradle包装器选项，然后切换到Gradle包装器任务配置，你在任务中所做的改变会在项目导入时自动更新。 -  **Specified location**: 如果你想手动下载并使用一个特定的Gradle版本，请选择这个选项。指定你的Gradle安装位置和JVM，当你导入指定的Gradle项目和执行其任务时，IntelliJ IDEA将在该位置运行Gradle。 