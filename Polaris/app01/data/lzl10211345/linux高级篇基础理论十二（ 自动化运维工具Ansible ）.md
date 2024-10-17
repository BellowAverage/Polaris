
--- 
title:  linux高级篇基础理论十二（ 自动化运维工具Ansible ） 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
 ♥️**不能因为人生的道路坎坷,就使自己的身躯变得弯曲;不能因为生活的历程漫长,就使求索的 脚步迟缓。** 
 ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
 ♥️**感谢CSDN让你我相遇！** 


**目录**

































### **ansible是什么？**

一款开源运维自动化工具，通过Ansible可以实现运维自动化，提高运维工程师的工作效率，减少人为的失误。Asbe通过本身集成的非常丰富的模块实现各种管理任务，其自带模块超过上千个。更为重要的是，它的操作非常简单，即使新手也比较容易上手，但它提供的功能却非常丰富，在运维领域，它几乎可以做任何事情。

ansible特点：

>  
 - ansible基于python开发，对其二次开发较容易。- 有丰富的内置模块，可以满足一切需求。- 管理模式简单，一条命令可以影响上千台主机。- 无客户端模式，底层通过ssh通信 


ansible不同角色

可以分为三个部分：使用者、Ansible工具集、作用对象。

##### 使用者

Ansible使用者可以采用多种方式和Ansible交互，图中为我们展示了四种方式CDB:CMDB存储和管理着企业T架构中的各项配置信息，是构建TL项目的核心工具运维人员可以组合CMDB和Ansible,通过CDB直接下发指令调用Ansible工具集完成操作者所希望达到的目标。PUBLIC/PRIVATE方式：Ansible除了丰富的内置模块外，同时提供丰富的AP语言接口，如PHP、Python、PERL等多种流行语言，基于PUBLIC/PRIVATE,Ansible以AP调用的方式运行」Ad-Hoc命令集：Users直接通过Ad-Hoc命令集调用Ansible工具集来完成任务.laybooks:Users预先编写好Ansible Playbooks,通过执行Playbooks中预先编排好的任务集按序执行任务

工作原理：

<img alt="" height="491" src="https://img-blog.csdnimg.cn/direct/57c113066d9e48ef9b72bfad94af4e37.png" width="845">



##### Ansible工具集
- Ansible Playbooks:任务脚本，编排定义Ansible任务集的配置文件，由Ansible按序依次执行通常是JSON格式的YML文件。- Inventory:Ansible管理主机清单。- Modules:Ansible执行命令功能模块，多数为内置的核心模块，也可以自定义。- Plugins:模块功能的补充，如连接类型插件、循环插件、变量插件、过滤插件等，该功能不常用。- API:供第三方程序调用的应用程序编程接口。- Ansible:该部分图中表示得不明显，组合Inventory、APl.Modules,Plugins可以理解为是Ansible命令工具，其为核心执行工具。
##### 作用对象

Ansible的作用对象不仅仅是Linux和非Linux操作系统的主机，也可以作用于各类PUBLIC/PRIVATE 商业和非商业设备的网络设施。使用者使用Ansible或Ansible--playbooks时，在服务器终端输入Ansible的Ad-Hoc命令集或Playbooks后，Ansible会遵循预先安排的规则将Playbooks逐步拆解为Play,再将Play组织成Ansible可以识别的任务，随后调用任务涉及的所有模块和插件，根Inventory中定义的主机列表通过SSH将任务集以临时文件或命令的形式传输到远程客户端执行并返回执行结果，如果是临时文件则执行完毕后自动删除。

### Ansible初始环境

yum安装即可

```
yum -y install ansible
```

生成ssh秘钥对(三次交互全部回车即可)

```
ssh-keygen -t  rsa
```

复制公钥到服务器(192.168.1.1)

```
ssh-copy-id  root@192.168.1.1
```

#### Ansible配置

Ansible通过将设备列表以分组的方式添加到/etc/ansible/hosts文件来实现对设备的管理，所以 在正式管理之前，首先要编写hosts文件。hosts文件中，以[]包含的部分代表组名，设备列表支持 主机名和P地址，默认情况下，通过访问22端口(SSH)来管理设备。若目标主机使用了非默认的 SSH端口，还可以在主机名称之后使用冒号加端口号标明，以行为单位分隔配置。另外，hoss文件还支持通配符。

```
[web]                 #[web]为模块名称
192.168.8.136
192.168.8.139
```

只对web组中192.168.8.136主机操作。通过--|imit参数限定主机的变更

<img alt="" height="63" src="https://img-blog.csdnimg.cn/direct/1b1669b45ab84a9ea5acab9195fd3918.png" width="835">

只对192.168.8.0网段主机操作。通过通配符限定主机的变更

<img alt="" height="49" src="https://img-blog.csdnimg.cn/direct/fe01dd20ade04e73b141afe2f675e740.png" width="777">

#### ansible语法

Ansible &lt;host-pattern&gt;   [options]

<img alt="" height="430" src="https://img-blog.csdnimg.cn/direct/06e878de227f4c89b3258c6147360a03.png" width="910">

检查所有主机是否存活。具体执行命令如下。

<img alt="" height="157" src="https://img-blog.csdnimg.cn/direct/d1b4c3df6d054409ac676ad95dcef8b9.png" width="649">

其中，192.168.8.139是执行的主机，SUCCESS表示命令执行成功，”=&gt;{}表示返回的结果。”changed”:false表示没有对主机做出更改，”ping”:”pong”表示执行了ping命令的返回结果。命令中all关键字是系统默认存在的，代表了/etc/ansible/hosts中的所有主机，不需要在hosts文件中定义all关键字。

列出wb组所有的主机列表。执行命令如下。

<img alt="" height="129" src="https://img-blog.csdnimg.cn/direct/609b1efe07ff4013a18f27fd363110f3.png" width="360">

批量显示web组中的磁盘使用空间，执行命令如下。

<img alt="" height="588" src="https://img-blog.csdnimg.cn/direct/e8adc912f67b47e194527c97e9043110.png" width="862">

#### Ansible返回结果

Ansible的返回结果非常友好，一般会用三种颜色来表示执行结果：红色、绿色和橘黄色。其中红色表示执行过程有异常，橘黄色表示命令执行后目标有状态变化，绿色表示执行成功且没有对目 标机器做修改

### Ansible模块

##### 1、shell模块

Shell模块在远程主机执行命令，相当于调用远程主机的Shell进程，然后在该Shell下打开一个 子Shell运行命令。和command模块的区别是它支持Shell特性，如管道、重定向等。

<img alt="" height="56" src="https://img-blog.csdnimg.cn/direct/7ad9a67c58304ea4bf9715099c5306fd.png" width="765">

##### 2、copy模块
- dest:指出复制文件的目标目录位置，使用绝对路径。如果源是目录，则目标也要是目录如果目标文件已存在，会覆盖原有内容。- src：指出源文件的路径，可以使用相对路径和绝对路径，支持直接指定目录。如果源是目录，则目标也要是目录。- mode:指出复制时，目标文件的权限，可选。- owner：指出复制时，目标文件的属主，可选。- group指出复制时，目标文件的属组，可选。- content:指出复制到目标主机上的内容，不能与src一起使用，相当于复制content指明的数据到目标文件中。
<img alt="" height="66" src="https://img-blog.csdnimg.cn/direct/837b23f152324dcc870e53770544eb37.png" width="876">

##### 3、hostname模块

hostname模块用于管理远程主机上的主机名，常用参数如下。

<img alt="" height="86" src="https://img-blog.csdnimg.cn/direct/79447e8a12c1415d9f0a633571e8528f.png" width="999">

##### 4、yum模块
- yum模块基于yum机制，对远程主机管理程序包，常用参数如下。- name:程序包的名称，可以带上版本号。若不指明版本，则默认为最新版本。- state=present\latest\absent:指明对程序包执行的操作，present表示安装程序包，latest表示安装最新版本的程序包，absent表示卸载程序包。- disablerepo:在用yum安装时，临时禁用某个仓库的ID。- enablerepo:在用yum安装时，临时启用某个仓库的ID,- conf_file:yum运行时的配置文件，而不是使用默认的配置文件。- diable_gpg_check=yes/no:是否启用完整性校验功能。
<img alt="" height="71" src="https://img-blog.csdnimg.cn/direct/3ccc864445874f828accd0d2cfddd7c5.png" width="1029">

##### 5、service模块
- service模块为用来管理远程主机上的服务的模块，常见参数如下。- name:被管理的服务名称。- state-=started stopped restarted：动作包含启动，关闭或重启- enabled=yes no:表示是否设置该服务开机自启动。- runlevel:如果设定了enabled开机自启动，则要定义在哪些运行目标下自动启动
<img alt="" height="53" src="https://img-blog.csdnimg.cn/direct/b5f005b15cfb4ccabfeb0edc568df6d7.png" width="849">

##### 6、user模块

user模块用于管理远程主机上的用户账号，常见参数如下。 name:必选参数，账号名称。 state=present\absent:创建账号或者删除账号，present表示创建，absent表示删除。 system=yes\no:是否为系统账号。， uid:用户UID。 group:用户的基本组。 groups:用户的附加组。 shell:默认使用的shell。

home:用户的家目录 move_home=yes/no:如果设置的家目录已经存在，是否将已存在的家目录进行移动. password:用户的密码，建议使用加密后的字符串。 comment:用户的注释信息。 remove=yes/no:当state=absent时，是否要删除用户的家目录。

创建用户示例如下：

<img alt="" height="91" src="https://img-blog.csdnimg.cn/direct/933814660c8e46b58260510ae6fceaa7.png" width="846">

>  
 人生要尽全力度过每一关,不管遇到什么困难不可轻言放弃！！！ 

