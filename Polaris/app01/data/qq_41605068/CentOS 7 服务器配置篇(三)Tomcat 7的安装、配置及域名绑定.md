
--- 
title:  CentOS 7 服务器配置篇(三):Tomcat 7的安装、配置及域名绑定 
tags: []
categories: [] 

---
1.下载Tomcat 7,官网地址:(jdk 6+)

  <img alt="" class="has" height="360" src="https://img-blog.csdnimg.cn/20190511090219698.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="577">

2.通过XShell上传下载好的压缩包

    新建一个放tomcat7的文件  mkdir tomcat7

    上传   rz 

      <img alt="" class="has" height="278" src="https://img-blog.csdnimg.cn/20190511091305781.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="335">

 3.解压 tar -xvf apache-tomcat-7.0.94.tar.gz

    <img alt="" class="has" height="300" src="https://img-blog.csdnimg.cn/2019051109201623.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="462">

4.Tomcat目录结构说明

    bin：脚本文件存放目录

    conf：配置文件存放目录

            catalina.policy：当时用-security选项启动Tomcat实例时会读取此配置文件来实现其安全运行策略

            catalina.properties：Java属性的定义文件，用于设定类加载器路径及一些JVM性能相关的调优策略

            context.xml：对于所有应用程序的默认配置

            logging.properties：日志相关的配置信息

            server.xml：主配置文件

                            Server：顶级组件，代表一个Tomcat实例

                            Service:将Connector关联至Engine的组件，1个Service只能包含1个Engine组件和1个或多个Connector组件

                            Connector：接受并解析用户请求，将请求映射为Engine中运行的代码，并将运行结果构建成响应报文

                            Engine：处理请求的Servlet引擎组件，即Catalina Servlet引擎，它检查每一个请求的HTTP首部信息以辨别此                                            请求应该发往哪个Host或Context，并将请求处理后的结果返回给相应的客户端

                            Host：类似http中的虚拟机

                           Context：指定web应用程序的根目录，一遍Servlet容器能够将用户请求发往正确的位置

                           Value：用来拦截请求并在将其转至目标之前进行某种处理操作，类似于Servlet规范中定义的过滤器

                           Logger：用于记录组件内的状态信息，可被用于除Context之外的任何容器中

                           Realm：用于用户的认证和授权，在配置一个应用程序时，管理员可以给每个资源或资源组定义角色及权限 而                                           这些访问控制功能的生效需要通过Realm来实现

            tomcat-users.xml：用户认证的账号密码，管理身份认证以及访问控制权限的配置文件

            web.xml：全局的web应用程序部署描述文件，可以设置Tomcat支持的文件类型，为所有的webapps提供默认部署配置

    lib：Tomcat运行依赖的jar文件存放目录

    logs：日志文件存放目录

    temp:临时文件存放目录

    webapps：应用程序默认部署根目录，每一个文件夹都是一个项目，其中ROOT是一个特殊的项目，在地址栏中没有给出项目                       名时，对应的就是ROOT项目

    work：工作目录，编译后的文件都存放在此目录，清空work目录，重启Tomcat，可以达到清除缓存的作用

5.修改Tomcat端口号为:80

  vi conf/server.xml  （vi命令详解 ）

   <img alt="" class="has" height="192" src="https://img-blog.csdnimg.cn/20190511132407524.PNG" width="423">

5.进入到bin目录，执行  sh startup.sh 开启Tomcat

    <img alt="" class="has" height="112" src="https://img-blog.csdnimg.cn/20190511125150244.PNG" width="525">

6.查看端口号    netstat -an | grep 80

<img alt="" class="has" height="74" src="https://img-blog.csdnimg.cn/20190511132451953.PNG" width="558">

7.打开浏览器 输入 ip:80

<img alt="" class="has" height="220" src="https://img-blog.csdnimg.cn/20190511132648546.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="702">

若报错，那么一定是防火墙未通过，请开启防火墙 端口规则

<img alt="" class="has" height="141" src="https://img-blog.csdnimg.cn/20190511132921357.PNG" width="1089">

    9.域名绑定

   <img alt="" class="has" height="132" src="https://img-blog.csdnimg.cn/20190511210037971.PNG" width="562">

访问:

<img alt="" class="has" height="253" src="https://img-blog.csdnimg.cn/20190511210134100.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="594">
