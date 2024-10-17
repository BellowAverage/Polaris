
--- 
title:  管理Python虚拟环境的脚本 
tags: []
categories: [] 

---


#### 大纲
- - <ul><li>- - - - <ul><li>- - - - - - - - <ul><li>- - - - <ul><li>- - <ul><li>- - - - - 


Python提供了很多代码库以方便开发人员使用。但是在多个项目同步开发中，不同项目所依赖的代码库的版本可能不一样。如果我们在同一个环境中维护着这些项目，将导致依赖库的版本错乱。为了解决这个问题，我们引入虚拟环境来做项目隔离。 本文介绍的脚本，提供了下列方法：
- init：初始化并创建环境。包括安装python-venv，以及创建虚拟环境（放在目录.env文件夹下）- del：删除虚拟环境。如果当前在虚拟环境中，则需要再传递force命令，以退出虚拟环境后再删除虚拟环境（.env文件夹）。- enter：进入虚拟环境。- quit：退出虚拟环境。- import：从当前目录下的requirements.txt中，导入依赖的代码库。- export：将当前虚拟环境的代码库导出到requirements.txt。如果requirements.txt文件存在，则需要额外传递force参数以强制覆盖。- install：通过pip3安装代码库。- uninstall：通过pip3删除代码库。- help：提供帮助信息。
## init

```
source env.sh init

```

### 未安装Python-venv

>  
 python version number: Python3.10 Reading package lists… Done Building dependency tree… Done Reading state information… Done Note, selecting ‘python3.10-venv’ for glob ‘Python3.10-venv’ The following NEW packages will be installed: python3.10-venv 0 upgraded, 1 newly installed, 0 to remove and 6 not upgraded. Need to get 0 B/5,716 B of archives. After this operation, 28.7 kB of additional disk space will be used. Selecting previously unselected package python3.10-venv. (Reading database … 81266 files and directories currently installed.) Preparing to unpack …/python3.10-venv_3.10.12-1~22.04.3_amd64.deb … Unpacking python3.10-venv (3.10.12-1~22.04.3) … Setting up python3.10-venv (3.10.12-1~22.04.3) … Scanning processes… Scanning candidates… Scanning linux images… Running kernel seems to be up-to-date. Restarting services… Service restarts being deferred: /etc/needrestart/restart.d/dbus.service systemctl restart networkd-dispatcher.service systemctl restart systemd-logind.service systemctl restart unattended-upgrades.service systemctl restart user@1000.service No containers need to be restarted. No user sessions are running outdated binaries. No VM guests are running outdated hypervisor (qemu) binaries on this host. Create virtual environment 


### 已安装Python-venv

>  
 python version number: Python3.10 Reading package lists… Done Building dependency tree… Done Reading state information… Done Note, selecting ‘python3.10-venv’ for glob ‘Python3.10-venv’ python3.10-venv is already the newest version (3.10.12-1~22.04.3). 0 upgraded, 0 newly installed, 0 to remove and 6 not upgraded. The virtual environment already exists. If you need to create a new virtual environment, please execute the source env.sh del command to delete the virtual environment. 


## del

```
source env.sh del

```

### 未进入虚拟环境

>  
 Delete virtual environment 


### 已进入虚拟环境

#### 非强制

>  
 Currently in the virtual environment. Failed to delete the virtual environment. if you need to delete the virtual environment, please exit the virtual environment and then execute the source env.sh del command to delete the virtual environment. Or execute the source env.sh del force command to force delete the virtual environment. 


#### 强制

```
source env.sh del force

```

>  
 Quit the virtual environment Delete virtual environment 


## enter

```
source env.sh enter

```

### 未进入虚拟环境

>  
 Enter the virtual environment 


### 已进入虚拟环境

>  
 Currently in the virtual environment. 


## quit

```
source env.sh quit

```

### 未进入虚拟环境

>  
 Currently not in the virtual environment. 


### 已进入虚拟环境

>  
 Quit the virtual environment 


## import

```
source env.sh import

```

### 未进入虚拟环境

>  
 Currently not in the virtual environment. 


### 已进入虚拟环境

#### 不存在requirements.txt文件

>  
 The requirements.txt file does not exist. If you need to import the requirements.txt file, please execute the source env.sh export command to export the requirements.txt file from other virtual environment. 


#### 已存在requirements.txt文件

以requirements.txt中内容是numpy==1.26.3为例

>  
 Collecting numpy==1.26.3 Using cached numpy-1.26.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (18.2 MB) Installing collected packages: numpy Successfully installed numpy-1.26.3 Import virtual environment 


## export

### 未进入虚拟环境

>  
 Currently not in the virtual environment. 


### 已进入虚拟环境

#### 不存在requirements.txt文件

>  
 Export virtual environment 


#### 已存在requirements.txt文件

##### 非强制覆盖

>  
 The requirements.txt file already exists. If you need to update the requirements.txt file, remove requirements.txt and then execute the source env.sh export command to update the requirements.txt file. 


##### 强制覆盖

```
source env.sh export force

```

>  
 Export virtual environment 


## install

```
source env.sh install numpy scipy

```

### 未进入虚拟环境

>  
 source env.sh install numpy scipy 


### 已进入虚拟环境

>  
 Collecting numpy Using cached numpy-1.26.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (18.2 MB) Collecting scipy Using cached scipy-1.11.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (36.4 MB) Installing collected packages: numpy, scipy Successfully installed numpy-1.26.3 scipy-1.11.4 Install libraries numpy scipy 


## uninstall

```
source env.sh install numpy scipy

```

### 未进入虚拟环境

>  
 Currently not in the virtual environment. 


### 已进入虚拟环境

>  
 Found existing installation: numpy 1.26.3 Uninstalling numpy-1.26.3: Would remove: /home/fangliang/numpy-example/.env/bin/f2py /home/fangliang/numpy-example/.env/lib/python3.10/site-packages/numpy-1.26.3.dist-info/* /home/fangliang/numpy-example/.env/lib/python3.10/site-packages/numpy.libs/libgfortran-040039e1.so.5.0.0 /home/fangliang/numpy-example/.env/lib/python3.10/site-packages/numpy.libs/libopenblas64_p-r0-0cf96a72.3.23.dev.so /home/fangliang/numpy-example/.env/lib/python3.10/site-packages/numpy.libs/libquadmath-96973f99.so.0.0.0 /home/fangliang/numpy-example/.env/lib/python3.10/site-packages/numpy/* Proceed (Y/n)? Y Successfully uninstalled numpy-1.26.3 Found existing installation: scipy 1.11.4 Uninstalling scipy-1.11.4: Would remove: /home/fangliang/numpy-example/.env/lib/python3.10/site-packages/scipy-1.11.4.dist-info/* /home/fangliang/numpy-example/.env/lib/python3.10/site-packages/scipy.libs/libgfortran-040039e1.so.5.0.0 /home/fangliang/numpy-example/.env/lib/python3.10/site-packages/scipy.libs/libopenblasp-r0-23e5df77.3.21.dev.so /home/fangliang/numpy-example/.env/lib/python3.10/site-packages/scipy.libs/libquadmath-96973f99.so.0.0.0 /home/fangliang/numpy-example/.env/lib/python3.10/site-packages/scipy/* Proceed (Y/n)? Y Successfully uninstalled scipy-1.11.4 Uninstall libraries numpy scipy 


## help

```
source env.sh help

```

>  
 init: create virtual environment enter: enter virtual environment quit: quit virtual environment del (force): delete virtual environment. If the force parameter is added, the virtual environment will be deleted forcibly export (force): export virtual environment. If the force parameter is added, the requirements.txt file will be overwritten import: import virtual environment install: install libraries uninstall : uninstall libraries help: view help 


## 代码库


