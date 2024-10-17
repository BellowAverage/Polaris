
--- 
title:  初识Maven及Maven安装与配置 
tags: []
categories: [] 

---
### 一、Maven安装与配置

        下载地址:

#### 1.1配置

         配置环境变量(和配置jdk一样)

               <img alt="" class="has" height="189" src="https://img-blog.csdnimg.cn/20190625002147381.png" width="653">

               <img alt="" class="has" height="177" src="https://img-blog.csdnimg.cn/20190625002459691.png" width="647">

#### 1.2验证

              在cmd中输入:    mvn  -v

              如出现以下信息则安装配置成功

             <img alt="" class="has" height="152" src="https://img-blog.csdnimg.cn/20190625002856629.png" width="795">

#### 1.3设置本地存储库位置(Local Repository)

               打开conf/文件下的 settings.xml，增加存储路径信息

             <img alt="" class="has" height="279" src="https://img-blog.csdnimg.cn/2019062500463832.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="801">

#### 1.4 配置阿里镜像

```
&lt;mirrors&gt;
      &lt;mirror&gt;
        &lt;id&gt;nexus-aliyun&lt;/id&gt;
        &lt;mirrorOf&gt;central&lt;/mirrorOf&gt;
        &lt;name&gt;Nexus aliyun&lt;/name&gt;
        &lt;url&gt;http://maven.aliyun.com/nexus/content/groups/public&lt;/url&gt;
      &lt;/mirror&gt;
  &lt;/mirrors&gt;
```

#### 1.5指定jdk

```
&lt;profiles&gt;
         &lt;profile&gt;
              &lt;id&gt;jdk-1.8&lt;/id&gt;
              &lt;activation&gt;
                &lt;activeByDefault&gt;true&lt;/activeByDefault&gt;
                &lt;jdk&gt;1.8&lt;/jdk&gt;
              &lt;/activation&gt;
              &lt;properties&gt;
                &lt;maven.compiler.source&gt;1.8&lt;/maven.compiler.source&gt;
                &lt;maven.compiler.target&gt;1.8&lt;/maven.compiler.target&gt;
                &lt;maven.compiler.compilerVersion&gt;1.8&lt;/maven.compiler.compilerVersion&gt;
              &lt;/properties&gt;
         &lt;/profile&gt;
  &lt;/profiles&gt;
```

#### 1.6 测试      <img alt="" class="has" height="129" src="https://img-blog.csdnimg.cn/20190625005048302.png" width="802">

              此时，你会发现 刚才设置的路径下出现很多文件，这些文件就是Maven从中央仓库下载到本地仓库的文件，只是一个   测试而已，可以删除！

#### 1.7查看所需插件版本，找到需要配置的信息

                   

### 二、初识Maven

         【官方】Maven是基于项目对象模型(POM poject object model)，可以通过小段描述信息(配置)来管理项目的构建，报告和文档的软件项目管理工具

         【通俗】Maven核心功能就是合理叙述项目间的依赖关系，通过pom.xml来获取jar包，解决了我们在开发过程中需要找各种jar包的麻烦

### 三、Maven使用

        Maven中的惯例:

                src/main/java 存放.java 文件

               src/main/resources 存放应用相关的配置文件

               src/main/webapp存放页面相关的文件，如 .jsp css js

               src/test/java 存放单元测试的.java文件

               src/test/resoures 单元测试相关的配置文件

## 四、Lifecycle—Maven生命周期

<img alt="" height="336" src="https://img-blog.csdnimg.cn/20200225115726195.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="458">

执行 Maven Project 中的生命周期的来管理项目时必须停止运行项目，否则无法对Maven项目进行生命周期的管理，同时注意一个重要的事情，Maven的生命周期在执行过程中有一个非常重要的特点，就是顺序依次自前向后执行，即如果执行compile,那么 clean 和 validate都已经自动执行了！！！  
| <h3>clean</h3> | <h3>target包被清空</h3> 

### target包被清空
| <h3>validate</h3> | <h3>验证</h3> 

### 验证
| <h3>compile</h3> | <h3>编译Java文件，生成target包</h3> 

### 编译Java文件，生成target包
| <h3>test</h3> | <h3>单元测试</h3> 

### 单元测试
| <h3>package</h3> | <h3>打包项目</h3> 

### 打包项目
| <h3>verify</h3> | <h3>对集成测试的结果执行任何检查，以确保满足质量标准</h3> 

### 对集成测试的结果执行任何检查，以确保满足质量标准
| <h3>install</h3> | <h3>将打包过的jar包安装到本地Maven仓库，覆盖原来Maven本地仓库中的jar包，用作本地其他项目的依赖项</h3> 

### 将打包过的jar包安装到本地Maven仓库，覆盖原来Maven本地仓库中的jar包，用作本地其他项目的依赖项
| <h3>Deploy</h3> | <h3>在构建环境中完成，将最终的包复制到远程存储库以与其他开发人员和项目共享。</h3> 

### 在构建环境中完成，将最终的包复制到远程存储库以与其他开发人员和项目共享。

### 具体生命周期作用如下：

```
1.清洁Clean：清空项目中的target目录，
  target是用来存放项目构建后的文件和目录、jar包、war包、编译的class文件，
  所有都是Maven构建时生成的。
2.验证Validate:验证项目是否正确，所有必要的信息可用
3.编译Compile:编译Java文件
4.测试Test:测试的，走单元测试的，报错信息处理，报错信息在target里面，console里不会报错
5.打包Package:会将项目打包
6.验证verify: 对集成测试的结果执行任何检查，以确保满足质量标准
7.安装install: 将打包过的jar包安装到本地Maven仓库，覆盖原来Maven本地仓库中的jar包，用作本地其他项目的依赖项
8.部署Deploy：在构建环境中完成，将最终的包复制到远程存储库以与其他开发人员和项目共享。

```

## 五、其它标签

### &lt;scope&gt;:是用来限制 dependency 的作用范围的，影响 maven 项目在各个生命周期时导入的 package 的状态，主要管理依赖的部署。
|compile|默认值，适用于所有阶段（表明该 jar 包在编译、运行以及测试中路径均可见），并且会随着项目一起发布。
|test|只在测试时使用，用于编译和运行测试代码，不会随项目发布。
|runtime| 无需参与项目的编译，不过后期的测试和运行周期需要其参与，与 compile 相比，跳过了编译。如 JDBC 驱动，适用运行和测试阶段。  
|provided|编译和测试时有效，但是该依赖在运行时由服务器提供，并且打包时也不会被包含进去。如 servlet-api。
|system|类似 provided，需要显式提供包含依赖的jar，不会从 maven 仓库下载，而是从本地文件系统获取，需要添加 systemPath 的属性来定义路径。

### &lt;optional&gt;:B项目依赖引用了A项目，那么A项目中的test-artifactId因为 true 所以，再根据，B项目中将不会有A项目的test-artifactId依赖传递过来。

注意

如果A项目打包的时候没有将自己所需的test-artifactId一同打包，在这种情况下使用 true标注；那么在B项目中使用A项目的时候，B项目不能拉取A项目中所需要的test-artifactId，并且A项目中需要的依赖test-artifactId也不能获取。这时候使用的过程中会发生NotClassFound！！！

## 六、Maven打包时出错

```
mvn install:install-file  -DgroupId=com.alipay   -DartifactId=obdriver   -Dversion=1.0.0   
-Dpackaging=jar  -Dfile=E:\Jar\obdriver-1.0.0-SNAPSHOT.jar
```

<img alt="" height="180" src="https://img-blog.csdnimg.cn/20210104150804826.png" width="1200">

解决方法：

```
            &lt;plugin&gt;
                &lt;groupId&gt;org.apache.maven.plugins&lt;/groupId&gt;
                &lt;artifactId&gt;maven-resources-plugin&lt;/artifactId&gt;
                &lt;!--修改版本--&gt;
                &lt;version&gt;3.1.0&lt;/version&gt;
            &lt;/plugin&gt;
```

## 六、将jar推到本地仓库

### 6.1**添加system范围的直接引用**

```
&lt;dependency&gt;
	&lt;groupId&gt;com.roufid.tutorials&lt;/groupId&gt;
	&lt;artifactId&gt;example-app&lt;/artifactId&gt;
	&lt;version&gt;1.0&lt;/version&gt;
	&lt;scope&gt;system&lt;/scope&gt;
	&lt;systemPath&gt;${basedir}/lib/yourJar.jar&lt;/systemPath&gt;
&lt;/dependency&gt;
```

>  
 ****${basedir}** ****表示包含 pom.xml的目录** 


###  6.2JAR包发布到新的本地仓库中

>  
 mvn install:install-file  -Dfile=\**\xxx.jar -DgroupId=上面的groupId  -DartifactId=上面的artifactId  -Dversion=上面的version  -Dpackaging=jar 


<img alt="" height="476" src="https://img-blog.csdnimg.cn/ff1663184ce94b54b0413e31bc5d5657.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">
