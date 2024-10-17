
--- 
title:  Linux命令之jar命令 
tags: []
categories: [] 

---
## 一、jar命令简介

  jar命令是Java开发中常用的命令行工具，用于创建、查看和操作Java归档文件（也称为JAR文件）。一般情况下我们很少直接使用此命令创建jar包，都是内嵌在开发工具中。主要使用场景如下：
- 1、开发环境jar包或者war包部署到测试环境；- 2、某演示系统war程序复制部署到客户环境，给客户提供试用；- 3、通用前置机jar包程序部署到不同客户环境，只需要修改客户购买的账户及数据库连接信息即可。
  这些情况下开发人员将系统打包成jar包或者war包，我们只需要部署前根据实际环境修改配置文件相关参数，然后启动程序即可完成系统部署。这个时候我们就可以使用jar命令解压软件包，如果是war包部署的WEB程序，实际上解压完成后修改参数启动即可；如果是jar包程序则需要重新打包后运行。

## 二、jar命令使用示例

### 1、解压war包

  解压后我们就可以进入配置文件目录编辑或者替换配置文件。

>  
 (base) [wuhs@s142 webapps]$ jar xvf test.war … (base) [wuhs@s142 webapps]$ ll total 52244 drwxrwxr-x. 7 wuhs wuhs 84 May 6 13:39 html drwxrwxr-x. 3 wuhs wuhs 38 May 6 16:21 META-INF -rw-r–r–. 1 wuhs wuhs 53497846 May 6 14:08 test.war drwxrwxr-x. 4 wuhs wuhs 47 May 6 13:39 WEB-INF (base) [wuhs@s142 webapps]$ vim WEB-INF/classes/config.properties 


### 2、解压jar包

  解压jar包和war包方式是一样的。

>  
 (base) [wuhs@s142 test]$ jar xvf test.jar … (base) [wuhs@s142 test]$ ll total 132 drwxrwxr-x. 3 wuhs wuhs 23 Jul 30 2020 com drwxrwxr-x. 3 wuhs wuhs 38 Aug 3 2020 META-INF -rw-r–r–. 1 wuhs wuhs 134472 May 6 16:23 test.jar 


### 3、创建jar包

>  
 (base) [wuhs@s142 test]$ tar -cvf test1.jar com META-INF/ … (base) [wuhs@s142 test]$ ll total 264 drwxrwxr-x. 3 wuhs wuhs 23 Jul 30 2020 com drwxrwxr-x. 3 wuhs wuhs 38 May 6 16:28 META-INF -rw-rw-r–. 1 wuhs wuhs 135165 May 6 16:28 test1.jar -rw-r–r–. 1 wuhs wuhs 134472 May 6 16:23 test.jar 


### 4、查看jar包文件列表

>  
 (base) [wuhs@s142 test]$ jar -tvf abcd.jar <img src="https://img-blog.csdnimg.cn/bc6e963cf6c34ae5b5aac876ea4e0c85.png" alt="在这里插入图片描述"> 


>  
 #查看jar包内容，如果文件较多我们可以结合grep命令过滤 (base) [wuhs@s142 webapps]$ jar tvf test.war |grep config.properties 3802 Sat May 06 09:31:20 CST 2023 WEB-INF/classes/config.properties 


### 5、更新文件到jar包

  使用u参数可以将文件更新到jar包中，文件增加到了jar包根目录下。

>  
 (base) [wuhs@s142 test]$ jar -uvf test.jar config_uat.properties adding: config_uat.properties(in = 3802) (out= 1073)(deflated 71%) 


### 6、创建带MANIFEST.MF文件的jar包

  使用m参数创建带MANIFEST.MF文件的jar包，要求MANIFEST.MF该文件存在，生成jar包的时候会自动创建META-INF目录，并将该MANIFEST.MF文件放置到该目录下。

>  
 (base) [wuhs@s142 test]$ jar -cvfm abcd.jar MANIFEST.MF com … (base) [wuhs@s142 test]$ jar -xvf abcd.jar created: META-INF/ inflated: META-INF/MANIFEST.MF … 


### 7、不创建MANIFEST.MF文件的jar包

  默认是自动创建MANIFEST.MF文件，如果不需要创建则使用-M参数，如果使用-m参数指定MANIFEST.MF文件则需要提前创建好该文件，通过MANIFEST.MF文件可以对jar包进行一些设置。

>  
 (base) [wuhs@s142 test]$ jar -cvfM abcd.jar com 


### 8、切换到指定目录执行jar命令

  注意-C dir后面的点哦。

>  
 (base) [wuhs@s142 test]$ jar -cvf abcd.jar -C abc/ . 


## 三、jar命令使用语法及参数说明

### 1、使用语法

>  
 #jar {ctxui}[vfmn0PMe] [jar-file] [manifest-file] [entry-point] [-C dir] files … #jar 参数 jar包名称 文件或目录 


### 2、参数说明

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-c</td><td align="left">创建新的存档</td>
<td align="left">-t</td><td align="left">存档目录列表</td>
<td align="left">-x</td><td align="left">从存档中提取命名（或所有）文件</td>
<td align="left">-u</td><td align="left">更新现有存档</td>
<td align="left">-v</td><td align="left">在标准输出上生成详细输出</td>
<td align="left">-f</td><td align="left">指定存档文件名</td>
<td align="left">-m</td><td align="left">包括指定清单文件中的清单信息</td>
<td align="left">-n</td><td align="left">在创建新存档后执行Pack200规范化</td>
<td align="left">-e</td><td align="left">为绑定到可执行jar文件中的独立应用程序指定应用程序入口点</td>
<td align="left">-0</td><td align="left">不使用ZIP压缩</td>
<td align="left">-P</td><td align="left">保留文件名中的前导’/'（绝对路径）和“…”（父目录）组件</td>
<td align="left">-M</td><td align="left">不为条目创建清单文件</td>
<td align="left">-i</td><td align="left">为指定的jar文件生成索引信息</td>
<td align="left">-C</td><td align="left">更改到指定的目录并包含以下文件</td>

## 四、War包和Jar包区别

  War包和Jar包都是Java开发中的归档文件，但它们有一些区别：
1. 用途不同：War包主要用于Web应用程序的部署，而Jar包则用于Java应用程序的打包和部署。1. 包含内容不同：War包通常包含Web应用程序的所有文件，包括JSP、HTML、CSS、JavaScript、Servlet、JavaBean等，而Jar包则包含Java类、资源文件和库文件等。1. 目录结构不同：War包通常包含WEB-INF目录和META-INF目录，其中WEB-INF目录包含web.xml、classes目录和lib目录，META-INF目录包含MANIFEST.MF文件；而Jar包则通常只包含META-INF目录和Java类文件。1. 部署方式不同：War包一般需要部署到Web服务器中，例如Tomcat、WebLogic等，而Jar包可以作为Java应用程序的独立运行文件，也可以作为库文件被其他Java应用程序调用。
  总的来说，War包和Jar包有不同的用途和适用场景，开发人员需要根据实际情况选择适合的归档文件类型。
