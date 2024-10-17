
--- 
title:  [备忘]在用IDEA插件备忘 
tags: []
categories: [] 

---
要618了，万一我能换得起电脑，IDEA怎么说也得梳理增强一下吧？ 

#### 目录
- <ul><li>- <ul><li><ul><li>- <ul><li>- - - - - - - 


### 0、《初始Plugins》【本文必看】

##### IDE快速了解、学习—— IDE Features Trainer

安装后侧边栏会出现 learn 。如果idea不熟，一定要试试这个。 可以在操作中快速熟悉IDEA。

### 1、《项目中的Plugins》

##### 启动不了之——依赖分析：maven helper

可以检测依赖的版本冲突的插件 <img src="https://img-blog.csdnimg.cn/20210617151513285.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="使用后"> 使用后，打开pom.xml文件，界面下方会有Dependency Analyzer
- Conflicts（查看冲突）- All Dependencies as List（列表形式查看所有依赖）- All Dependencies as Tree（树形式查看所有依赖） <img src="https://img-blog.csdnimg.cn/202106171524267.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 可查看冲突、依赖（用这个不算明显）
##### 看不懂——中文翻译：Translation

相对于词典\百度翻译，Translation插件翻译出来的更加专业一丢丢。右键不了的地方直接快捷键Ctrl+Shift+Y，只要能选中的都可以翻译。 <img src="https://img-blog.csdnimg.cn/20210617153025408.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210617153151733.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

##### 更熟悉快捷键：Key Promoter X

当你点击的功能有快捷键时，Key Promoter 会告诉你快捷键是哪个（看起来就是很专业） <img src="https://img-blog.csdnimg.cn/20210617153455497.png" alt="在这里插入图片描述">

##### 写的更快：Codota

代码提示工具，扫描你的代码后，根据你的敲击进行概率提示。 <img src="https://img-blog.csdnimg.cn/20210623103427111.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

##### Bug分析与代码优化：Spotbugs\SonarLint

都会帮你分析代码——查找可能出现的bug、代码质量优化点。
-  **Spotbugs** 右键项目——&gt;Spotbugs ——&gt;analyze project files…… <img src="https://img-blog.csdnimg.cn/20210617155143883.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 先分析一波，打开IDEA界面下方Spotbugs，以**bad practice**（坏习惯）为例 <img src="https://img-blog.csdnimg.cn/2021061715532668.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> Spotbugs提示我说 Enum field is public and mutable A mutable public field is defined inside a public enum, thus can be changed by malicious code or by accident from another package. Though mutable enum fields may be used for lazy initialization, it’s a bad practice to expose them to the outer world. Consider declaring this field final and/or package-private. （Enum 字段是公共且可变的 可变公共字段定义在公共枚举中，因此可以被恶意代码或意外从另一个包更改。尽管可变枚举字段可用于延迟初始化，但将它们暴露给外部世界是一种不好的做法。考虑将此字段声明为 final 和/或 package-private。） -  **SonarLint** 不用右键分析，安装后点击SonarLint窗口，会有当前打开并选中的文件的分析 <img src="https://img-blog.csdnimg.cn/20210617161154369.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 建议你说，类实现了 Cloneable 但没有定义或使用 clone 方法。建议XXX。 
##### 热部署：JRebel

以插件形式实现热部署也是很好用的，反正，不用计算一个1+1都要rebuild，那就是好用。安装后要在Help——&gt;Jrebel，激活。很好用，有条件请支持正版。

激活后，在setting中jrebel设置work offline 这里偷偷放一个我搭建的activatehttp://121.4.107.87:8081/3f0c3e3d-5a51-484a-976c-1dbcdf15f2db

##### 看下这个接口出问题了：RestfulToolkit

安装后可以直接快捷键 ctrl+\，根据链接查找到接口 <img src="https://img-blog.csdnimg.cn/20210617163116153.png" alt="在这里插入图片描述"> 配合ctrl + shift + n查找文件使用，当无情的接盘侠

##### 我的表单不可能出问题：Json Parser

用于校验json字符串 <img src="https://img-blog.csdnimg.cn/20210623103141515.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 场景：校验数据库表单、检查flyway的SQL中的JSON

### 2、《备忘Plugins》

代码注解插件： Lombok 仓库：Git lni文件支持：lni 构建工具：Maven、Maven Extension\Gradle 、Gradle Extension 数据库：DataBase Tools and SQL …… 阿里代码规约检测：Alibaba Java Coding Guidelines 代码生成工具：CodeMaker 单元测试测试生成工具：JUnitGenerator Mybatis 工具：Free Mybatis plugin JSON转领域对象工具：GsonFormat 字符串工具：String Manipulation 生成对象set方法：GenerateAllSetter Redis可视化：Iedis K8s工具：Kubernetes 中英文翻译工具：Translation

等……

**感觉只要有想用的框架、工具、中间件，都很容易找到对应的插件。** 先用着，等到后面有其他需求，用到了别的再来补充。
