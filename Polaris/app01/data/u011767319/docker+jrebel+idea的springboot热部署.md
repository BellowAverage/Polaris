
--- 
title:  docker+jrebel+idea的springboot热部署 
tags: []
categories: [] 

---
### 简介

>  
 解放稍微更新代码就打包重启的烦恼，本人已经受够的小改动就要打包上传重启全部代码的方式 


### 照顾我的粉丝，关注我可以直接看

>  
 绝对是精华 


### idea安装jrebel

>  
 本人的另外一篇文章有详细介绍，请移步，在这就不多做解释了 




### 测试项目的结构

>  
 这个是测试的demo 


<img src="https://img-blog.csdnimg.cn/20210707114516429.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### 配置pom文件的打包定义

>  
 打包很关键，为了方便项目打包的线上 spring-boot-thin-layout打包成精简包也就几百k，上传后再现在下载依赖，减少上传文件的痛苦 docker-maven-plugin 这是docker打包工具 maven-antrun-plugin 这是maven打包工具 可以重新定义打包位置 其他的就不多做描述了 


```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd"&gt;
    &lt;modelVersion&gt;4.0.0&lt;/modelVersion&gt;
    &lt;parent&gt;
        &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
        &lt;artifactId&gt;spring-boot-starter-parent&lt;/artifactId&gt;
        &lt;version&gt;2.4.5&lt;/version&gt;
        &lt;relativePath/&gt; &lt;!-- lookup parent from repository --&gt;
    &lt;/parent&gt;
    &lt;groupId&gt;com.ljq&lt;/groupId&gt;
    &lt;artifactId&gt;docker_pack_demo&lt;/artifactId&gt;
    &lt;version&gt;0.0.1-SNAPSHOT&lt;/version&gt;
    &lt;name&gt;docker_pack_demo&lt;/name&gt;
    &lt;description&gt;docker打包测试&lt;/description&gt;
    &lt;properties&gt;
        &lt;java.version&gt;1.8&lt;/java.version&gt;
    &lt;/properties&gt;
    &lt;dependencies&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-web&lt;/artifactId&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;org.projectlombok&lt;/groupId&gt;
            &lt;artifactId&gt;lombok&lt;/artifactId&gt;
            &lt;optional&gt;true&lt;/optional&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;
            &lt;scope&gt;test&lt;/scope&gt;
        &lt;/dependency&gt;
    &lt;/dependencies&gt;

    &lt;build&gt;
        &lt;plugins&gt;
            &lt;plugin&gt;
                &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
                &lt;artifactId&gt;spring-boot-maven-plugin&lt;/artifactId&gt;
                &lt;dependencies&gt;
                    &lt;dependency&gt;
                        &lt;groupId&gt;org.springframework.boot.experimental&lt;/groupId&gt;
                        &lt;artifactId&gt;spring-boot-thin-layout&lt;/artifactId&gt;
                        &lt;version&gt;1.0.26.RELEASE&lt;/version&gt;
                    &lt;/dependency&gt;
                &lt;/dependencies&gt;
                &lt;configuration&gt;
                    &lt;excludes&gt;
                        &lt;exclude&gt;
                            &lt;groupId&gt;org.projectlombok&lt;/groupId&gt;
                            &lt;artifactId&gt;lombok&lt;/artifactId&gt;
                        &lt;/exclude&gt;
                    &lt;/excludes&gt;
                &lt;/configuration&gt;
            &lt;/plugin&gt;
            &lt;!-- docker构建插件 --&gt;
            &lt;plugin&gt;
                &lt;groupId&gt;com.spotify&lt;/groupId&gt;
                &lt;artifactId&gt;docker-maven-plugin&lt;/artifactId&gt;
                &lt;version&gt;1.0.0&lt;/version&gt;
                &lt;configuration&gt;
                    &lt;!-- 生成的docker镜像名称  --&gt;
                    &lt;imageName&gt;${<!-- -->docker.image.prefix}/${<!-- -->project.artifactId}&lt;/imageName&gt;
                    &lt;dockerDirectory&gt;${<!-- -->project.basedir}/src/main/docker&lt;/dockerDirectory&gt;
                    &lt;resources&gt;
                        &lt;resource&gt;
                            &lt;targetPath&gt;/&lt;/targetPath&gt;
                            &lt;directory&gt;${<!-- -->project.build.directory}&lt;/directory&gt;
                            &lt;include&gt;${<!-- -->project.build.finalName}.jar&lt;/include&gt;
                        &lt;/resource&gt;
                    &lt;/resources&gt;
                &lt;/configuration&gt;
            &lt;/plugin&gt;
            &lt;!-- 复制jar包到指定目录 --&gt;
            &lt;plugin&gt;
                &lt;artifactId&gt;maven-antrun-plugin&lt;/artifactId&gt;
                &lt;executions&gt;
                    &lt;execution&gt;
                        &lt;phase&gt;package&lt;/phase&gt;
                        &lt;configuration&gt;
                            &lt;tasks&gt;
                                &lt;copy todir="src/main/docker" file="target/${project.artifactId}-${project.version}.${project.packaging}"&gt;&lt;/copy&gt;
                            &lt;/tasks&gt;
                        &lt;/configuration&gt;
                        &lt;goals&gt;
                            &lt;goal&gt;run&lt;/goal&gt;
                        &lt;/goals&gt;
                    &lt;/execution&gt;
                &lt;/executions&gt;
            &lt;/plugin&gt;
        &lt;/plugins&gt;
    &lt;/build&gt;

&lt;/project&gt;


```

### 开始编写dockerFile文件

>  
 FROM java:latest 到时候docker 会去下载openjdk 8 ENV 定义参数 


**jrebel.jar和libjrebel64.so 热部署必须的**

>  
 这个是为了简单起见的，不想用这个的话可以去官网下载文件 这个两个文件需要从哪里找的 64位操作系统就选择64结尾的，32位操作系统就选择32结尾的；Linux选择.so后缀的，Mac选择.dylib结尾的，windows选择.dll结尾的 jrebel.jar和libjrebel64.so建议放到可以用http下载的地方 本人电脑用的是win11，不要在意细节哈 看下面例子 <img src="https://img-blog.csdnimg.cn/20210707120236244.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210707120444732.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210707120608421.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 


**热启动必须的**

```
-Xdebug","-Xrunjdwp:server=y,transport=dt_socket,address=${<!-- -->DBUG_SERVER_PORT},suspend=n","-agentpath:/libjrebel64.so"

```

```
# 指定基础镜像 这里springboot项目运行只需要java jdk环境即可
FROM java:latest
#端口号
ENV SERVER_PORT=8080
#Dbug
ENV DBUG_SERVER_PORT=8081
#指定使用utf-8编码运行
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
# 维护者信息
MAINTAINER ljq
# 重命名
ADD *.jar app.jar
#添加jrebel的包
ADD http://192.168.1.50/file/jrebel.jar /jrebel.jar
ADD http://192.168.1.50/file/libjrebel64.so /libjrebel64.so
# 对外暴漏的端口号
EXPOSE $SERVER_PORT
# 运行
ENTRYPOINT ["java", "-jar","-Xdebug","-Xrunjdwp:server=y,transport=dt_socket,address=${DBUG_SERVER_PORT},suspend=n","-agentpath:/libjrebel64.so","-Drebel.remoting_plugin=true","-Djava.security.egd=file:/dev/./urandom", "app.jar","--server.port=${SERVER_PORT}"]

```

### idea配置好docker打包的链接

>  
 选好dockerfile 位置 指定好绑定窗口 打包是跳过测试过程，-Dmaven.test.skip=true 完整 `clean package install -Dmaven.test.skip=true` 


<img src="https://img-blog.csdnimg.cn/20210707115533517.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### 配置jrebel的部署方式

<img src="https://img-blog.csdnimg.cn/20210707115758886.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210707115821446.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/20210707115845726.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### 项目中也要配置好部署地址

<img src="https://img-blog.csdnimg.cn/20210707115931437.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### 运行发现的问题

>  
 打包运行时，发现docker容器里的时区不对 需要在运行选项上指定好，项目运行的时区 `-e TZ="Asia/Shanghai"` 中国的时区 


<img src="https://img-blog.csdnimg.cn/8f62c484498c45878f0057d1ba9198a6.png" alt="在这里插入图片描述">

**docker 容器默认是使用0时区的** <img src="https://img-blog.csdnimg.cn/a91f3faa14974a4e992c6fa56dfac454.png" alt="在这里插入图片描述"> **添加完参数后，显示中国时区** <img src="https://img-blog.csdnimg.cn/ab3a505b7c684518b3b296641aec9888.png" alt="在这里插入图片描述">

**idea 的docker 控制台输出**

>  
 控制台输出-编码格式默认是GBK的 所有输出中文乱码了 需要将idea的指定一下编码格式 


**英文版的** IDEA工具栏 → HELP → Edit Custom VM Options… **中文版的** <img src="https://img-blog.csdnimg.cn/f00505b4de314bd9b5ebcb2dcce39368.png" alt="在这里插入图片描述"> **添加配置**

```
-Dfile.encoding=utf-8

```

添加完重启一下idea，控制台就显示正常了
