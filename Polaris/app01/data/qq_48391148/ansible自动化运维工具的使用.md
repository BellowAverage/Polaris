
--- 
title:  ansible自动化运维工具的使用 
tags: []
categories: [] 

---
**目录**































































### 为什么需要ansible？ 

>  
 **linux运维人员，人肉运维不可取，效率慢，容易敲错出问题 ** 


### 什么是ansible？

>  
 **ansible是一个自动化运维工具的名称** 
 **它是基于python开发的，集合了众多运维工具的优点（puppet，fabric，slatstack），实现批量系统配置，程序的部署，批量运行命令等** 
 **        ansible依赖于paramiko，PyYaml，和jinja三个关键组件** 
 **        基于ssh协议，只要管理员通过ssh登录到一台远程主机上能做的事情，ansible都可以做** 


### ansible的组成

>  
 **ansible的组成** 
 **        1、host inventory  -- 定义客户机，可以对客户机进行分类：db类，web类。。。。** 
 **        2、playbook  --  剧本，让主机按照我给定的剧本去完成一些事情** 
 **        3、module  --  模块 实现一个个功能的程序** 
 **        4、piuging  --  插件  实现一些额外的小功能** 


############################################################################################

### ansible实验：

>  
 **        准备三台linux服务器** 
 **        a：ansible：192.168.44.170** 
 **        b：web-1：192.168.44.140** 
 **        c：web-2：192.168.44.203** 


#### 1、首先使用ansible（我设置的安装ansible软件的主机名）与其他两台linux服务器建立免密通道

** 建立免密通道：**

<img alt="" height="461" src="https://img-blog.csdnimg.cn/8ef47f667a124dceac9e39e1dd10ff7a.png" width="1200">

<img alt="" height="142" src="https://img-blog.csdnimg.cn/ac139576e5b34f33ab724f6d4b0c938a.png" width="1200">

############################################################################################ 

####  2、在ansible机器上面安装ansible工具

```
[root@ansible ~]# yum install epel-release -y
[root@ansible ~]# yum install ansible -y
```

############################################################################################ 

#### 3、配置

**ansible的配置文件存放目录：**

>  
 **        /etc/ansible/ansible.cfg** 
 **        ansible的主配置文件，此文件主要定义了roles_path的路径，主机清单路径，连接清单的主机方式等等** 
 **        /etc/hosts** 
 **        这个配置文件就是默认的主机清单配置文件，可以通过ansible.cfg重新定义** 


**先将hosts文件备份**

```
[root@ansible ansible]# ls
ansible.cfg  hosts  roles
[root@ansible ansible]# cp hosts hosts.bak
[root@ansible ansible]# ls
ansible.cfg  hosts  hosts.bak  roles

```

**清空hosts文件，添加webser组，将需要管理的主机添加到websever组里面**

```
[root@ansible ansible]# vim hosts
[root@ansible ansible]# cat hosts
[webserver]
192.168.44.140
192.168.44.203

```

**除了以上两个重要的配置文件，还有三个可执行文件分别是：**

>  
 **ansible 主执行程序，一般用于命令行下执行** 
 **ansible-playbook 执行playbook中的任务** 
 **ansible-doc获取各模块的帮助信息** 


############################################################################################ 

## 2、ansible模块的使用

>  
 **HOST-PATTERN      #匹配主机模式,如all表示所有主机 -m MOD_NAME       #模块名   如:ping -a MOD_ARGS        #模块执行的参数 -f FORKS                  #生成几个子进行程执行 -C                               #(不执行，模拟跑) -u Username             #某主机的用户名 -c  CONNection        #连接方式（default smart） ** 


### 2.1 shell模块 

####  ansible all -m shell -a "mkdir /tmp/sc"  # 指定ansible管理的所有主机都执行命令

```
[root@ansible ~]# ansible all -m shell -a "mkdir /tmp/sc"

```

<img alt="" height="205" src="https://img-blog.csdnimg.cn/ecc63bff63e2442d91520d22a99af04e.png" width="1200">

>  
 **rc  ==》 return code  --为0表示执行成功 ** 


 查看使用ansible执行命令的效果

```
[root@web-1 tmp]# ls
sc                 
```

```
[root@web-2 tmp]# ls
sc
```

############################################################################################ 

#### ansible webserver -m shell -a "mkdir /tmp/sc2"  # 指定webserver组的主机执行命令

```
[root@ansible ~]# ansible webserver -m shell -a "mkdir /tmp/sc2"

```

<img alt="" height="188" src="https://img-blog.csdnimg.cn/1a63fb14884f4784bde694a3528ee541.png" width="1200">

执行效果：

```
[root@web-1 tmp]# ls
sc           
sc2
```

```
[root@web-2 tmp]# ls
sc
sc2
```

############################################################################################ 

### 2.2  copy模块 

#### ansible webserver -m copy -a "src=/etc/passwd dest=/tmp mode=666"  # 指定webserver，将/etc/passwd复制到主机/tmp目录下，指定权限666

#### ansible参数说明

>  
 ** 1、copy  -- 配置管理     从本地copy文件分发到目录主机路径      参数说明:     src= 源文件路径     dest= 目标路径      注意src= 路径后面带/ 表示带里面的所有内容复制到目标目录下，不带/是目录递归复制过去     content= 自行填充的文件内容     owner 属主     group 属组     mode权限** 


```
[root@ansible ~]# ansible webserver -m copy -a "src=/etc/passwd dest=/tmp mode=666"

```

<img alt="" height="567" src="https://img-blog.csdnimg.cn/8e448314f5a541edafcc6a5ad4c64312.png" width="1046">

############################################################################################ 

###  2.3  fetch模块  从远程主机拉取文件到本地

#### ansible webserver -m fetch -a "src=/etc/hostname dest=/lianxi mode=644  # 从远程主机拉取文件到本地

```
[root@ansible lianxi]# ansible webserver -m fetch -a "src=/etc/hostname dest=/lianxi mode=644"
192.168.44.140 | CHANGED =&gt; {
    "changed": true, 
    "checksum": "1846cb4df90d9aaa490a6dfd7870e76f3a5860c4", 
    "dest": "/lianxi/192.168.44.140/etc/hostname", 
    "md5sum": "c60f6e095eff21f568d9ed5d31a5fee3", 
    "remote_checksum": "1846cb4df90d9aaa490a6dfd7870e76f3a5860c4", 
    "remote_md5sum": null
}
192.168.44.203 | CHANGED =&gt; {
    "changed": true, 
    "checksum": "5ea6f5e3c054c592dc4797377cf154a18b1b0c6a", 
    "dest": "/lianxi/192.168.44.203/etc/hostname", 
    "md5sum": "9874bffccf99f644bb486d1aa16d9a71", 
    "remote_checksum": "5ea6f5e3c054c592dc4797377cf154a18b1b0c6a", 
    "remote_md5sum": null
}
[root@ansible lianxi]# ls
192.168.44.140  192.168.44.203  python_flask  test  truncate_tables.sh
[root@ansible lianxi]# cd 192.168.44.140/
[root@ansible 192.168.44.140]# ls
etc
[root@ansible 192.168.44.140]# cd etc/
[root@ansible etc]# ls
hostname

```

############################################################################################ 

### 2.4  command模块

>  
 **从远程主机上执行命令，属于裸执行，非键值对显示，不进行shell解析** 


```
[root@ansible ~]# ansible all -m command -a "ip a"
192.168.44.140 | CHANGED | rc=0 &gt;&gt;
1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:37:b5:82 brd ff:ff:ff:ff:ff:ff
    inet 192.168.44.140/24 brd 192.168.44.255 scope global noprefixroute ens33
       valid_lft forever preferred_lft forever
    inet6 fe80::20c:29ff:fe37:b582/64 scope link 
       valid_lft forever preferred_lft forever
192.168.44.203 | CHANGED | rc=0 &gt;&gt;
1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:09:24:e9 brd ff:ff:ff:ff:ff:ff
    inet 192.168.44.203/24 brd 192.168.44.255 scope global noprefixroute ens33
       valid_lft forever preferred_lft forever
    inet6 fe80::20c:29ff:fe09:24e9/64 scope link 
       valid_lft forever preferred_lft forever
[root@ansible ~]# 

```

############################################################################################ 

### 2.5  file模块

>  
 **    设置文件属性(创建文件)     常用参数:     path目标路径     state directory为目录,link为软链接     group 目录属组     owner 属主         mode  权限     等,其他参数通过ansible-doc -s file 获取** 


####  ansible all -m file -a "path=/tmp/sanchuang  state=directory"  # 创建文件目录

```
[root@ansible ~]# ansible all -m file -a "path=/tmp/sanchuang  state=directory"
192.168.44.203 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "gid": 0, 
    "group": "root", 
    "mode": "0755", 
    "owner": "root", 
    "path": "/tmp/sanchuang", 
    "secontext": "unconfined_u:object_r:user_tmp_t:s0", 
    "size": 6, 
    "state": "directory", 
    "uid": 0
}
192.168.44.140 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "gid": 0, 
    "group": "root", 
    "mode": "0755", 
    "owner": "root", 
    "path": "/tmp/sanchuang", 
    "secontext": "unconfined_u:object_r:user_tmp_t:s0", 
    "size": 6, 
    "state": "directory", 
    "uid": 0
}
[root@ansible ~]# 

```

#### ansible all -m file -a "path=/tmp/sanchuang owner=liming"  # 设置修改文件属性

```
[root@ansible ~]# ansible all -m file -a "path=/tmp/sanchuang owner=liming"
192.168.44.203 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "gid": 0, 
    "group": "root", 
    "mode": "0755", 
    "owner": "liming", 
    "path": "/tmp/sanchuang", 
    "secontext": "unconfined_u:object_r:user_tmp_t:s0", 
    "size": 6, 
    "state": "directory", 
    "uid": 1000
}
192.168.44.140 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "gid": 0, 
    "group": "root", 
    "mode": "0755", 
    "owner": "liming", 
    "path": "/tmp/sanchuang", 
    "secontext": "unconfined_u:object_r:user_tmp_t:s0", 
    "size": 6, 
    "state": "directory", 
    "uid": 1000
}

```

############################################################################################ 

### 2.6  cron模块 计划任务

>  
 **    通过cron模块对目标主机生成计划任务     常用参数:     除了分(minute)时(hour)日(day)月(month)周(week)外     name: 本次计划任务的名称     state: present 生成(默认) |absent 删除 (基于name)** 
 **    ntp服务，是一个时间管理服务器     在 centos 8 中， ntp 已经被 chrony 代替。     之前的版本：yum install -y ntp     centos8：yum install chrony** 


#### ansible all -m cron -a "minute=*/3 job='date &gt;&gt;time.txt' name=date_test state=present"   # 每三分钟输出当前时间，到/tmp/time.txt文件

```
[root@ansible ~]# ansible all -m cron -a "minute=*/3 job='date &gt;&gt;time.txt' name=date_test state=present"
192.168.44.203 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "envs": [], 
    "jobs": [
        "date_test"
    ]
}
192.168.44.140 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "envs": [], 
    "jobs": [
        "date_test"
    ]
}

[root@web-1 tmp]# crontab -l
#Ansible: date_test
*/3 * * * * date &gt;&gt;time.txt
[root@web-2 tmp]# crontab -l
#Ansible: date_test
*/3 * * * * date &gt;&gt;time.txt
[root@web-2 tmp]# 

```

####  ansible 192.168.44.140 -m cron -a "name=date_test state=absent"   删除名字为date_test 的计划任务

```
[root@ansible ~]# ansible 192.168.44.140 -m cron -a "name=date_test state=absent"
192.168.44.140 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "envs": [], 
    "jobs": []
}

```

#### 2.7  yum模块

>  
 **    故名思义就是yum安装软件包的模块;     常用参数说明:     enablerepo,disablerepo表示启用与禁用某repo库     name 安装包名     state (present' or installed', latest')表示安装, (absent' or `removed') 表示删除** 


#### 示例：通过yum模块安装vsftpd文件传输服务

** ansible all -m yum -a "name=vsftpd state=installed"**

```
[root@ansible ~]# ansible all -m yum -a "name=vsftpd state=installed"
192.168.44.203 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "changes": {
        "installed": [
            "vsftpd"
        ]
    }, 
    "msg": "", 
    "rc": 0, 
    "results": [
        "Loaded plugins: fastestmirror\nLoading mirror speeds from cached hostfile\n * base: mirrors.ustc.edu.cn\n * extras: mirrors.nju.edu.cn\n * updates: mirrors.ustc.edu.cn\nResolving Dependencies\n--&gt; Running transaction check\n---&gt; Package vsftpd.x86_64 0:3.0.2-29.el7_9 will be installed\n--&gt; Finished Dependency Resolution\n\nDependencies Resolved\n\n================================================================================\n Package         Arch            Version                 Repository        Size\n================================================================================\nInstalling:\n vsftpd          x86_64          3.0.2-29.el7_9          updates          173 k\n\nTransaction Summary\n================================================================================\nInstall  1 Package\n\nTotal download size: 173 k\nInstalled size: 353 k\nDownloading packages:\nRunning transaction check\nRunning transaction test\nTransaction test succeeded\nRunning transaction\n  Installing : vsftpd-3.0.2-29.el7_9.x86_64                                 1/1 \n  Verifying  : vsftpd-3.0.2-29.el7_9.x86_64                                 1/1 \n\nInstalled:\n  vsftpd.x86_64 0:3.0.2-29.el7_9                                                \n\nComplete!\n"
    ]
}
192.168.44.140 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "changes": {
        "installed": [
            "vsftpd"
        ]
    }, 
    "msg": "", 
    "rc": 0, 
    "results": [
        "Loaded plugins: fastestmirror\nLoading mirror speeds from cached hostfile\n * base: mirrors.ustc.edu.cn\n * extras: mirrors.bupt.edu.cn\n * updates: mirrors.ustc.edu.cn\nResolving Dependencies\n--&gt; Running transaction check\n---&gt; Package vsftpd.x86_64 0:3.0.2-29.el7_9 will be installed\n--&gt; Finished Dependency Resolution\n\nDependencies Resolved\n\n================================================================================\n Package         Arch            Version                 Repository        Size\n================================================================================\nInstalling:\n vsftpd          x86_64          3.0.2-29.el7_9          updates          173 k\n\nTransaction Summary\n================================================================================\nInstall  1 Package\n\nTotal download size: 173 k\nInstalled size: 353 k\nDownloading packages:\nRunning transaction check\nRunning transaction test\nTransaction test succeeded\nRunning transaction\n  Installing : vsftpd-3.0.2-29.el7_9.x86_64                                 1/1 \n  Verifying  : vsftpd-3.0.2-29.el7_9.x86_64                                 1/1 \n\nInstalled:\n  vsftpd.x86_64 0:3.0.2-29.el7_9                                                \n\nComplete!\n"
    ]
}

```

安装成功： 

```
[root@web-1 ~]# ps aux | grep "ftp"
root      23115  0.0  0.0  53292   576 ?        Ss   10:56   0:00 /usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf
root      23117  0.0  0.0 112824   976 pts/1    R+   10:56   0:00 grep --color=auto ftp

```

```
[root@web-2 ~]# ps aux | grep ftp
root       1566  0.0  0.0  53292   576 ?        Ss   10:56   0:00 /usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf
root       1574  0.0  0.0 112824   976 pts/0    S+   10:57   0:00 grep --color=auto ftp

```

 示例：卸载vsftpd

```
[root@ansible ~]# ansible all -m yum -a "name=vsftpd state=absent"
192.168.44.203 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "changes": {
        "removed": [
            "vsftpd"
        ]
    }, 
    "msg": "", 
    "rc": 0, 
    "results": [
        "已加载插件：fastestmirror\n正在解决依赖关系\n--&gt; 正在检查事务\n---&gt; 软件包 vsftpd.x86_64.0.3.0.2-29.el7_9 将被 删除\n--&gt; 解决依赖关系完成\n\n依赖关系解决\n\n================================================================================\n Package        架构           版本                      源                大小\n================================================================================\n正在删除:\n vsftpd         x86_64         3.0.2-29.el7_9            @updates         353 k\n\n事务概要\n================================================================================\n移除  1 软件包\n\n安装大小：353 k\nDownloading packages:\nRunning transaction check\nRunning transaction test\nTransaction test succeeded\nRunning transaction\n  正在删除    : vsftpd-3.0.2-29.el7_9.x86_64                                1/1 \n  验证中      : vsftpd-3.0.2-29.el7_9.x86_64                                1/1 \n\n删除:\n  vsftpd.x86_64 0:3.0.2-29.el7_9                                                \n\n完毕！\n"
    ]
}
192.168.44.140 | CHANGED =&gt; {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": true, 
    "changes": {
        "removed": [
            "vsftpd"
        ]
    }, 
    "msg": "", 
    "rc": 0, 
    "results": [
        "已加载插件：fastestmirror\n正在解决依赖关系\n--&gt; 正在检查事务\n---&gt; 软件包 vsftpd.x86_64.0.3.0.2-29.el7_9 将被 删除\n--&gt; 解决依赖关系完成\n\n依赖关系解决\n\n================================================================================\n Package        架构           版本                      源                大小\n================================================================================\n正在删除:\n vsftpd         x86_64         3.0.2-29.el7_9            @updates         353 k\n\n事务概要\n================================================================================\n移除  1 软件包\n\n安装大小：353 k\nDownloading packages:\nRunning transaction check\nRunning transaction test\nTransaction test succeeded\nRunning transaction\n  正在删除    : vsftpd-3.0.2-29.el7_9.x86_64                                1/1 \n  验证中      : vsftpd-3.0.2-29.el7_9.x86_64                                1/1 \n\n删除:\n  vsftpd.x86_64 0:3.0.2-29.el7_9                                                \n\n完毕！\n"
    ]
}

```

############################################################################################

### 2.8  service模块

>  
 **    服务管理模块     常用参数:     name:服务名     state:服务状态  started（启动） stopped(关闭) restarted（重启） reloaded（重新加载）     enabled: 是否开机启动 true|false     runlevel: 启动级别 (systemed方式忽略)** 


 示例：关闭vsftpd服务

```
ansible all -m service -a "name=vsftpd state=stopped"

```

 开启vsftpd服务

```
ansible all -m service -a "name=vsftpd state=started"

```

############################################################################################

### 2.9  script模块

>  
 **把本地的脚本传到远端执行;前提是到远端可以执行,不要把Linux下的脚本同步到windows下执行; 只在远程服务器执行脚本，不上传脚本到远程服务器** 


```
[root@b ~]# cat test.sh
#!/bin/bash
echo "test ansible" &gt;&gt; /tmp/ansible.txt
[root@b ~]# ansible all -m script -a "/root/test.sh"
192.168.0.48 | CHANGED =&gt; {
    "changed": true, 
    "rc": 0, 
    "stderr": "Shared connection to 192.168.0.48 closed.\r\n", 
    "stderr_lines": [
        "Shared connection to 192.168.0.48 closed."
    ], 
    "stdout": "", 
    "stdout_lines": []
}
```

############################################################################################

## 3、 playbook的使用 

>  
 **如果ansible的各模块(能实现各种功能)是车间里的各工具;playbook就是指导手册,目标远程主机就是库存和原料对象** 


#### **语法 yaml 格式配置** 

>  
 **语法 yaml 格式配置** 
 **1、playbook的核心元素 hosts : playbook配置文件作用的主机 tasks: 任务列表 variables: 变量  templates:包含模板语法的文本文件 handlers :由特定条件触发的任务 roles :用于层次性、结构化地组织playbook。roles 能够根据层次型结构自动装载变量文件、tasks以及handlers等** 


#### playbook运行方式 

>  
 **ansible-playbook --check 只检测可能会发生的改变,但不真执行操作 ansible-playbook --list-hosts 列出运行任务的主机 ansible-playbook --syntax-check playbook.yaml 语法检测 ansible-playbook -t TAGS_NAME playbook.yaml 只执行TAGS_NAME任务 ansible-playbook playbook.yaml 运行** 


####  示例：使用playbook剧本，首先要编辑一个yml文件

>  
 **- hosts：所有主机** 
 **        remote_user:指定远程连接用户为root** 
 **        tasks：任务** 
 **        -name：任务名为 up file** 
 **                copy：将/etc/passwd 文件拷贝到 /tmp/passwd_tmp** 
 **        -name：任务名：下载redis** 
 **                yum：name=redie state=installed** 
 **- hosts：对于webserver组** 
 **        tasks：任务** 
 **        -name：删除文件 remove file** 
 **                shell：** 


```
[root@ansible ~]# cat ansible_playbook_sc.yaml 
- hosts: all
  remote_user: root
  tasks:
  - name: up file
    copy: src=/etc/passwd dest=/tmp/passwd_tmp
  - name: download redis
    yum: name=redis state=installed
- hosts: webser
  tasks:
  - name: remove file
    shell: rm -rf /tmp/passwd_tmp
```

 #执行playbook

```
[root@b ~]# ansible-playbook ansible_playbook_sc.yaml 
```

 
