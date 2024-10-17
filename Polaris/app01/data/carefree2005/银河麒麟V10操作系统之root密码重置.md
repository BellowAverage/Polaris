
--- 
title:  银河麒麟V10操作系统之root密码重置 
tags: []
categories: [] 

---
## 一、需求说明

  从kingbase工程师那拷贝了一个已经安装了kingbase数据库环境的虚拟机，只有一个kingbase普通账户，root密码位置，且该账户未加入到sudo组中，无法执行新软件等的安装和部署。为了满足需要，我们需要重置root密码。

## 二、服务器版root密码重置步骤

### 1、重启后按e

  重启操作系统，按ESC键，进入此界面后按e键，进入grub模式。 <img src="https://img-blog.csdnimg.cn/a9827637d74f46c1adae6a6556ccd59e.png" alt="在这里插入图片描述">

### 2、输入grub账户密码

  银行麒麟V10服务器版操作系统需要输入grub账户密码才可以进入grub模式。默认账户密码为：root/Kylin123123。 <img src="https://img-blog.csdnimg.cn/0f827acf2dbf41d489442eb702a710cd.png" alt="在这里插入图片描述">

### 3、修改启动参数

  输入账户密码后进入编辑模式，找到linux开头的行，在行末尾加入rw init=/bin/bash。 <img src="https://img-blog.csdnimg.cn/9f6ce86eb2cc48d18a92c5832de941f9.png" alt="在这里插入图片描述">

### 4、进入单用户模式

  修改好启动参数后按照最下方提示输入Ctl+x启动系统就可以进入单用户模式。

### 5、修改root密码

  进入单用户模式后使用passwd命令就可以修改root账户密码，此时不需要输入原密码，直接输入两遍你需要设置的root新密码即可。 <img src="https://img-blog.csdnimg.cn/3f2349e98fc54e6c940b6dc3998a2d92.png" alt="在这里插入图片描述">

### 6、重启系统

  修改完密码我们重启操作系统，此时reboot命令是无法直接使用的，我们需要指定完成路径/usr/sbin/reboot，虚拟机环境建议加上-f参数。 <img src="https://img-blog.csdnimg.cn/2c6ab96462e640a8a86c864de005da57.png" alt="在这里插入图片描述">

### 7、验证root密码

  使用kingbase账户登录后使用su 切换到root账户下，输入密码后切换成功。 <img src="https://img-blog.csdnimg.cn/ee59e5365890429488c8e8e38bd555b3.png" alt="在这里插入图片描述">

### 3、桌面版系统账户密码重置

  修复模式下账户密码重置主要是针对在没有配置root密码情况下用于修复普通账户密码的，也可以用于初次设置root密码。但是在初次设置了root密码情况下进入修复模式要求输入root密码方可，如果忘记了root密码我们则需要通过第二章节的方式重置root密码。

### 1、启动的时候选择Kylin V10 高级选项

  开机系统启动后，在启动选项中选择——Kylin V10 高级选项。 <img src="https://img-blog.csdnimg.cn/20bcfa53ecdb4db7873b25eca84c83b1.png" alt="在这里插入图片描述">

### 2、选择“recovery mode”

  进入如下界面中选择——Kylin v10.1，（recovery mode）。 <img src="https://img-blog.csdnimg.cn/ed4ba00c17ea49fd891761c694bc0c04.png" alt="在这里插入图片描述">

### 3、进入修复模式

  如下图所示，按照提示输入回车进入修复模式。如果选择的安装的语言进入修复模式中文显示乱码，我们直接回车即可，银河麒麟既然作为国产操作系统主流品牌，这些地方还是要改进哦。 <img src="https://img-blog.csdnimg.cn/8ddad33efdf64617a55b5472ef1620c9.png" alt="在这里插入图片描述">

### 4、修改账户密码

  启动后进入修复模式，使用passwd命令设置root账户密码。当然我们也可以使用passwd命令修改其他账户的密码。如果曾经设置了root密码，进入修复模式会要求输入root密码，如果我们又忘记了root密码，那么我们只能通过第二章节的方式修改root密码。 <img src="https://img-blog.csdnimg.cn/0289f526b0d445c1b27afc52780e32d9.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b371a66328544f529c9042227469d558.png" alt="在这里插入图片描述">

### 5、重启系统

  修改完密码后使用reboot命令重启系统。如版本提示，银河麒麟桌面版V10是基于debian系统的，这个跟服务器版是不一样的哦。

>  
 wuhs@wuhs-pc:~$ cat /etc/os-release NAME=“Kylin” VERSION=“V10.1 (juniper)” ID=kylin ID_LIKE=debian PRETTY_NAME=“Kylin V10.1” VERSION_ID=“v10.1” HOME_URL=“http://www.kylinos.cn/” SUPPORT_URL=“http://www.kylinos.cn/service.aspx” BUG_REPORT_URL=“http://www.kylinos.cn/” PRIVACY_POLICY_URL=“http://www.kylinos.cn” VERSION_CODENAME=juniper UBUNTU_CODENAME=juniper 

