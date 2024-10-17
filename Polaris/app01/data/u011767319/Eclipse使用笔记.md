
--- 
title:  Eclipse使用笔记 
tags: []
categories: [] 

---
### Eclipse编辑YAML插件-YEdit

官网：

离线版本：（链接:  密码: wyyb）

安装方法：直接复制JAR包到Plugins文件夹即可。

### Eclipse使用Maven打包spring boot项目
<li> spring boot 加了不是Maven仓库里的jar包，怎么打jar。方法如下： <pre><code>```
&lt;!--e应用 --&gt;
&lt;dependency&gt;
	&lt;groupId&gt;com.taobao.top&lt;/groupId&gt;
	&lt;artifactId&gt;top-api-sdk-dev&lt;/artifactId&gt;
	&lt;version&gt;ding-open-mc-SNAPSHOT&lt;/version&gt;
	&lt;scope&gt;system&lt;/scope&gt; 	//------这个很重要，system表示打包时会加上
	&lt;systemPath&gt;${pom.basedir}/lib/taobao-sdk-java-auto_1479188381469-20180926.jar&lt;/systemPath&gt;
&lt;/dependency&gt;

&lt;dependency&gt;
	&lt;groupId&gt;com.taobao.top&lt;/groupId&gt;
	&lt;artifactId&gt;lippi-oapi-encrpt&lt;/artifactId&gt;
	&lt;version&gt;dingtalk-SNAPSHOT&lt;/version&gt;
	&lt;scope&gt;system&lt;/scope&gt;
	&lt;systemPath&gt;${pom.basedir}/lib/taobao-sdk-java-auto_1479188381469-20180926-source.jar&lt;/systemPath&gt;
&lt;/dependency&gt;

&lt;!--maven 的配置如下 --&gt;
&lt;build&gt;
&lt;plugins&gt;
	&lt;plugin&gt;
		&lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
		&lt;artifactId&gt;spring-boot-maven-plugin&lt;/artifactId&gt;
		&lt;configuration&gt; 
			&lt;includeSystemScope&gt;true&lt;/includeSystemScope&gt; //----这里就是表示把本地jar，也一起打包
		&lt;/configuration&gt;
	&lt;/plugin&gt;
&lt;/plugins&gt;
</code></pre> ``` </li>
### Eclipse下的项目文件更新后，自动刷新目录方法

**Window-&gt;Preferences-&gt;General-&gt;Workspace-&gt;** **勾选Refresh using native hocks or polling** **勾选Refresh on access**
