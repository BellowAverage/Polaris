
--- 
title:  实战springboot+CAS单点登录系统 
tags: []
categories: [] 

---
## 一、搭建Tomcat HTTPS支持

CAS采用HTTPS协议处理用户请求，所以我们需要配置tomcat支持HTTPS协议。

### 第一步：生成密钥库

我们使用jdk自带的keytool工具生成密钥库。

>  
 keytool是Java开发工具包（JDK）中的一个命令行工具，用于管理密钥库（keystore）和证书。 
 <pre><code class="language-bash">keytool -genkey -alias &lt;alias&gt; -keyalg &lt;algorithm&gt; -keystore &lt;keystore&gt; [options]
</code></pre> 
 <ul>- `-genkey`参数用于生成密钥对并将其存储在密钥库中。-  `-alias &lt;alias&gt;`：指定生成的密钥对的别名。别名用于在后续的操作中标识密钥对。例如，`-alias mykey`将为生成的密钥对设置别名为"mykey"。 -  `-keyalg &lt;algorithm&gt;`：指定生成密钥对时使用的加密算法。常用的加密算法包括RSA、DSA和EC等。例如，`-keyalg RSA`将使用RSA算法生成密钥对。 -  `-keystore &lt;keystore&gt;`：指定要使用的密钥库文件的路径和名称。密钥库用于存储生成的密钥对和其他相关信息。例如，`-keystore mykeystore.jks`将生成的密钥对存储在名为"mykeystore.jks"的密钥库中。 -  `-v`参数用于指定详细输出（verbose mode），它可以显示更详细的信息，包括生成密钥对、导入证书等操作的详细过程和结果。 <li> `[options]`：可选参数，用于进一步配置生成密钥对的选项。一些常用的选项包括： 
   - `-keysize &lt;size&gt;`：指定密钥的长度，例如 `-keysize 2048`表示使用2048位的密钥长度。- `-validity &lt;days&gt;`：指定证书的有效期（天数），例如 `-validity 365`表示证书的有效期为365天。- `-dname &lt;distinguished_name&gt;`：指定用于生成证书的主题信息，包括国家、组织、组织单位等。- `-storepass &lt;password&gt;`：指定密钥库的密码，用于访问和管理密钥库中的密钥对。</li></ul> 
  


别名java1234；存储路径D:\CAS\keystore

```
keytool -genkey -v -alias java1234 -keyalg RSA -keystore D:\CAS\keystore\java1234.keystore
```

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/14a0ef99004747c2a4bbf83aa93f163b.png" width="1200"> 在存储路径下可查看下述文件已存在

### <img alt="" height="1005" src="https://img-blog.csdnimg.cn/16764b2bc0f24be3b87bf03f27b59063.png" width="1200">  第二步：从密钥库导出证书

```
keytool -export -trustcacerts -alias java1234 -file D:\CAS\keystore\java1234.cer -keystore D:\CAS\keystore\java1234.keystore
```

>  
 - `keytool`: 命令行工具名称，用于执行keytool命令。- `-export`: 指定要执行的操作是导出证书。- `-trustcacerts`: 导出证书时，也导出信任的根证书。- `-alias java1234`: 指定要导出的证书的别名为"java1234"。请确保该别名存在于密钥库中。- `-file D:\CAS\keystore\java1234.cer`: 指定要导出的证书文件的路径和名称。导出的证书将保存在指定的文件中。- `-keystore D:\CAS\keystore\java1234.keystore`: 指定密钥库文件的路径和名称。这是包含要导出的证书的密钥库文件。 
 该命令的目的是从密钥库中导出别名为"java1234"的证书，并将其保存在指定的文件中（D:\CAS\keystore\java1234.cer）。 
 请确保在执行该命令之前，确实存在具有指定别名的证书，并且密钥库文件路径和文件名正确。 


<img alt="" height="180" src="https://img-blog.csdnimg.cn/59aff404e7cf454e812e0925bb24bae1.png" width="1200">

 <img alt="" height="1005" src="https://img-blog.csdnimg.cn/770a62e35a364a1eb98af0e250a30747.png" width="1200">

### 第三步：将证书导入到jdk证书库

```
keytool -import -trustcacerts -alias java1234 -file ‪D:\CAS\keystore\java1234.cer -keystore ‪D:\java\jdk1.8.0_91\jre\lib\security\cacerts
```

>  
 以上命令使用keytool工具来导入证书到信任的根证书库中。下面是命令中各个参数的解释： 
 - `keytool`: 命令行工具名称，用于执行keytool命令。 - `-import`: 指定要执行的操作是导入证书。 - `-trustcacerts`: 表示将证书导入到信任的根证书库中。 - `-alias java1234`: 指定要导入的证书的别名为"java1234"。 - `-file D:\CAS\keystore\java1234.cer`: 指定要导入的证书文件的路径和名称。该证书文件是要导入的证书的内容。 - `-keystore D:\java\jdk1.8.0_91\jre\lib\security\cacerts`: 指定信任的根证书库的路径和名称。该证书库是Java安装目录下的cacerts文件，用于存储信任的根证书。 
 该命令的目的是将指定路径下的证书文件（D:\CAS\keystore\java1234.cer）导入到Java安装目录下的信任的根证书库（cacerts文件）中，并使用别名"java1234"进行标识。 
 请确保在执行该命令之前，证书文件路径和文件名正确，以及信任的根证书库的路径和文件名正确。另外，请确保有足够的权限执行该操作。 


### <img alt="" height="1200" src="https://img-blog.csdnimg.cn/6dde38beeceb45eb9ea235ead72da031.png" width="1200">

###  第四步：

tomcat下载地址：

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/f83b9ff47dca48809516a18ebea37616.png" width="1200">

 下载完成后解压至CAS目录下，进入D:\CAS\apache-tomcat-9.0.76-windows-x64\apache-tomcat-9.0.76\conf目录下找到server.xml文件

在该文件中添加下述代码

```
&lt;Connector port="8443" protocol="org.apache.coyote.http11.Http11AprProtocol"
               maxThreads="150" SSLEnabled="true" scheme="https" secure="true"
               clientAuth="false" sslProtocol="TLS"
               keystoreFile="D:\CAS\keystore\java1234.keystore"
               keystorePass="666666" /&gt;
```

如图所示

<img alt="" height="641" src="https://img-blog.csdnimg.cn/6bffea2da0be42179ce14092ed0b0337.png" width="1200">

保存后退出，进入D:\CAS\apache-tomcat-9.0.76-windows-x64\apache-tomcat-9.0.76\bin目录下找到startup.bat文件，双击打开运行

<img alt="" height="1005" src="https://img-blog.csdnimg.cn/7b2e8ee2be2f4b3fb022631ef98dc341.png" width="1200"> 运行结果如下，出现乱码问题：

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/f4e0bc2bbbdd45c0876b40de61d3cdee.png" width="1200"> 进入conf目录，打开下述文件

<img alt="" height="1005" src="https://img-blog.csdnimg.cn/1effb3a8899a44568adba160a3767a44.png" width="1200">

 将文件中java.util.logging.ConsoleHandler.encoding = UTF-8代码修正为java.util.logging.ConsoleHandler.encoding = GBK

<img alt="" height="180" src="https://img-blog.csdnimg.cn/175d61f1b4334fe58e026e9b70e93d9e.png" width="1200">

 再进入bin目录，启动startup.bat文件，运行乱码问题解决：

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/b6795cea8a3d4f889e40055b2442f154.png" width="1200">

###  测试

访问

能够成功访问tomcat即证明配置成功。

<img alt="" height="1162" src="https://img-blog.csdnimg.cn/2f9e8d1616484e5cbacfa69576b4c182.png" width="1200">

##  二、CAS Server war下载

下载地址：

<img alt="" height="1090" src="https://img-blog.csdnimg.cn/54292db6a832483192e828e1720584a6.png" width="1200"> 若需要修改后端代码，则需要将github上源码进行下载，修改后进行打包，发布war包。

## 三、CAS Server发布到tomcat

将下载的war包放进D:\CAS\apache-tomcat-9.0.76-windows-x64\apache-tomcat-9.0.76\webapps目录下

<img alt="" height="1005" src="https://img-blog.csdnimg.cn/6ee5d74f05534ba6921fedee90163599.png" width="1200">

 复制到该目录后，此war包会自动解压，将解压后的文件重命名为cas，并删除war包

<img alt="" height="1005" src="https://img-blog.csdnimg.cn/93d57b370fd843c9a81f1985a5d77020.png" width="1200">

 回到bin目录下，运行startup.bat文件

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/e90400fc49854d2fa9e7435b7d82e05a.png" width="1200">

启动成功后，我们访问 

若启动无问题，则成功访问到上述网址

<img alt="" height="1074" src="https://img-blog.csdnimg.cn/79ba6ef5f0724c9d8353f80f5dc39b24.png" width="1200"> 进入D:\CAS\apache-tomcat-9.0.76-windows-x64\apache-tomcat-9.0.76\webapps\cas\WEB-INF\classes目录下，打开application.properties文件

<img alt="" height="210" src="https://img-blog.csdnimg.cn/b58e77815bf048efbc2f4d5a406b31ef.png" width="877">

即cas接收的用户为casuser,密码为Mellon；将其输入至登陆页面，显示登录成功。

<img alt="" height="1025" src="https://img-blog.csdnimg.cn/8fe1e11cebf645d0bbbc75c33a8b7af9.png" width="1200">

 若输入的用户名和密码与上述不符，则认证失败

<img alt="" height="891" src="https://img-blog.csdnimg.cn/a4a5eeaf719742da9fd4fc1181b002cb.png" width="983">

 继续在D:\CAS\apache-tomcat-9.0.76-windows-x64\apache-tomcat-9.0.76\webapps\cas\WEB-INF\classes目录下，打开log4j2.xml文件

<img alt="" height="168" src="https://img-blog.csdnimg.cn/c6ce6f6cf9ab49bc9563308b4b8a73d6.png" width="1200">

将上述日志的基础路径换为D:\CAS\log

<img alt="" height="354" src="https://img-blog.csdnimg.cn/96088646d58c413daa86b18efee50591.png" width="1200"> 配置域名：C:\Windows\System32\drivers\etc\hosts

<img alt="" height="196" src="https://img-blog.csdnimg.cn/87b30bae5e79438193deccb19c493fd4.png" width="964">

保存文件的时候，出现下述错误：

<img alt="" height="368" src="https://img-blog.csdnimg.cn/c108a269c122497c8165195a2f50cb93.png" width="730">

 提供解决方案的文章链接：

经尝试，已成功解决。

 域名配置成功后，可以利用https://java1234.com:8443/cas访问。

## 四、CAS配置数据源、数据库用户认证

上述登录使用的用户名密码是在application.properties文件中写死的，但实际开发中，需要配置数据源、进行数据库用户认证。

**a.新建数据和表**

启动mysql服务

<img alt="" height="1186" src="https://img-blog.csdnimg.cn/51a958c47979470abbc36c0a6678c702.png" width="1200">

输入mysql -u root -p

之后输入密码即可进入mysql shell

<img alt="" height="612" src="https://img-blog.csdnimg.cn/250573c735b94d72bb152082f82b99bf.png" width="1200">

在mysql shell界面依次执行下述命令：

```
CREATE DATABASE db_sso;

USE db_sso;

CREATE TABLE t_cas (
  id int(11) NOT NULL AUTO_INCREMENT,
  username varchar(30) DEFAULT NULL,
  password varchar(100) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

insert into t_cas(id,username,password) values(1,'java1234','123456');
```

<img alt="" height="248" src="https://img-blog.csdnimg.cn/a7010a335e494d79a0d5917da4fd0745.png" width="802">

<img alt="" height="306" src="https://img-blog.csdnimg.cn/669d9ab327b74a4496529671b7884268.png" width="1188">

<img alt="" height="410" src="https://img-blog.csdnimg.cn/a2404b32bcc94547b8773a7fde04bf4d.png" width="1200">

 在  中，可以使用 **CREATE DATABASE** 语句创建数据库，语法格式如下：

```
CREATE DATABASE [IF NOT EXISTS] &lt;数据库名&gt;
[[DEFAULT] CHARACTER SET &lt;字符集名&gt;] 
[[DEFAULT] COLLATE &lt;校对规则名&gt;];
```

>  
 `[ ]`中的内容是可选的。语法说明如下： 
 - &lt;数据库名&gt;：创建数据库的名称。MySQL 的数据存储区将以目录方式表示 MySQL 数据库，因此数据库名称必须符合操作系统的文件夹命名规则，不能以数字开头，尽量要有实际意义。注意在 MySQL 中不区分大小写。- IF NOT EXISTS：在创建数据库之前进行判断，只有该数据库目前尚不存在时才能执行操作。此选项可以用来避免数据库已经存在而重复创建的错误。- [DEFAULT] CHARACTER SET：指定数据库的字符集。指定字符集的目的是为了避免在数据库中存储的数据出现乱码的情况。如果在创建数据库时不指定字符集，那么就使用系统的默认字符集。- [DEFAULT] COLLATE：指定字符集的默认校对规则。 
 MySQL 的字符集（CHARACTER）和校对规则（COLLATION）是两个不同的概念。字符集是用来定义 MySQL 存储字符串的方式，校对规则定义了比较字符串的方式。后面我们会单独讲解 MySQL 的字符集和校对规则。 




```
cas.authn.jdbc.query[0].url=jdbc:mysql://localhost:3306/db_sso?serverTimezone=GMT

cas.authn.jdbc.query[0].user=root

cas.authn.jdbc.query[0].password=123456

cas.authn.jdbc.query[0].sql=select * from t_cas where username=?

cas.authn.jdbc.query[0].fieldPassword=password

cas.authn.jdbc.query[0].driverClass=com.mysql.jdbc.Driver
```

** c.加上jdbc驱动包以及支持jar**

将事先下载好的jar包复制进D:\CAS\apache-tomcat-9.0.76-windows-x64\apache-tomcat-9.0.76\webapps\cas\WEB-INF\lib目录下<img alt="" height="1005" src="https://img-blog.csdnimg.cn/3527af65eba541e5bc44715662a5e72d.png" width="1200">

 **d.测试**

进入bin目录下启动startup.bat

进入登陆页面登录，发现认证失败，可能是数据库连接出现问题，还不知道怎么解决。

## 五、CAS client+SpringBoot客户端整合搭建

<img alt="" height="1028" src="https://img-blog.csdnimg.cn/cfde3ecedb3d4c21956203dfd29b13a2.png" width="603">

 注意：crm_sys模块下java目录下需要创建包com.java1234，即与步骤三最后所配置的域名需要保持一致。

由于cas默认支持https服务，不支持http服务，现在运行项目，访问http://localhost:9999会出现未认证服务的报错。

现在配置一下http服务，进入D:\CAS\apache-tomcat-9.0.76-windows-x64\apache-tomcat-9.0.76\webapps\cas\WEB-INF\classes\services目录，打开HTTPSandIMAPS-10000001.json文件，如下图所示，加入|http

<img alt="" height="306" src="https://img-blog.csdnimg.cn/49267b40efd846ccac753249b8331002.png" width="1200">

之后回退到上一路径D:\CAS\apache-tomcat-9.0.76-windows-x64\apache-tomcat-9.0.76\webapps\cas\WEB-INF\classes，打开application.properties文件，在该文件末尾添加下述代码：

```
cas.tgc.secure=false

cas.serviceRegistry.initFromJson=true
```

 之后进入bin目录下启动startup.bat，访问http://localhost:9999，发现已可以自动跳转到登陆页面。

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/138c2a65b11f4fbc934a7added5b31f4.png" width="1200">

输入用户名和密码即可进入相应系统界面。

<img alt="" height="194" src="https://img-blog.csdnimg.cn/f7f907dc3d5845eabc29a9aeaa833ea4.png" width="600">

为更好的验证单点登录，可以多创建几个模块。

<img alt="" height="560" src="https://img-blog.csdnimg.cn/7f680f68d2d844a39927b494ae76dc28.png" width="606">

 测试页面代码如下：

```
&lt;!DOCTYPE html&gt;
&lt;html xmlns:th="http://www.thymeleaf.org"&gt;
&lt;head&gt;
    &lt;meta http-equiv="Content-Type" content="text/html; charset=UTF-8"&gt;
    &lt;meta http-equiv="Pragma" content="no-cache"&gt;
    &lt;meta http-equiv="Cache-Control" content="no-cache"&gt;
    &lt;meta http-equiv="Expires" content="0"&gt;
    &lt;title&gt;SSO单点登录系统 Powered by java1234.vip&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
SSO单点登录系统 Powered by java1234.vip&lt;br/&gt;
&lt;a href="http://java1234.com:6666/crm" target="_blank"&gt;crm客户关系管理系统&lt;/a&gt;&lt;br/&gt;
&lt;a href="http://java1234.com:8888/fd" target="_blank"&gt;fd财务管理系统系统&lt;/a&gt;&lt;br/&gt;
&lt;a href="http://java1234.com:9999/hr" target="_blank"&gt;hr人力资源管理系统&lt;/a&gt;&lt;br/&gt;
&lt;/body&gt;
```

测试页面如图：

<img alt="" height="272" src="https://img-blog.csdnimg.cn/fd099f742fec4d62b0aa3d52c1585664.png" width="1200">

经测试，单点登入登出正常。

当未登录时，点击进入任意系统，都会跳转到cas单点登录界面，进行登录验证；成功后，进入其余系统也无需进行验证。登出后，其余系统也同步登出。

##  六、CAS Server界面修改

进入D:\CAS\apache-tomcat-9.0.76-windows-x64\apache-tomcat-9.0.76\webapps\cas\WEB-INF\classes目录，打开layout.html文件，将header和footer注释掉。

<img alt="" height="642" src="https://img-blog.csdnimg.cn/b6c2ba8beb0643f2800bbbd6b59c9f8a.png" width="1200">

 之后重新启动bin目录下的startup.bat文件，运行效果如图，header和footer已删除：

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/ada5c3c50cfa48f19339913dfa03a994.png" width="1200">

之后将casLoginView.html文件中如图所示部分进行注释：

<img alt="" height="1041" src="https://img-blog.csdnimg.cn/a958bc97346442a6b4527edde7972e5f.png" width="1200"> 运行结果如下：

<img alt="" height="1189" src="https://img-blog.csdnimg.cn/794a685a57bf46cd8372bb6dbd61d099.png" width="1200">

 在D:\CAS\apache-tomcat-9.0.76-windows-x64\apache-tomcat-9.0.76\webapps\cas\WEB-INF\classes\static\css\cas.css文件添加下述代码

```
#notices .rightimg{
  width: 500px;
  height: 440px;
  background-image: url(D:\CAS\apache-tomcat-9.0.76-windows-x64\apache-tomcat-9.0.76\webapps\cas\WEB-INF\classes\static\images\login-img.png);
}
```

在casLoginView.html文件图示位置增加下述一行代码：

<img alt="" height="914" src="https://img-blog.csdnimg.cn/decb33142ade48f89ded2dc4e83e9662.png" width="1200">

启动startup.bat运行效果如图示：

<img alt="" height="1059" src="https://img-blog.csdnimg.cn/224ecf51a1bd405a9c4d7e63cbeded73.png" width="1200">

 


