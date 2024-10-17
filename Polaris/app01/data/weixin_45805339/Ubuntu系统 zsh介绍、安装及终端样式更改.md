
--- 
title:  Ubuntu系统 zsh介绍、安装及终端样式更改 
tags: []
categories: [] 

---
### 1. 安装zsh

```
sudo apt install zsh

```

### 2. download or copy oh-my-zsh to ~/

```

sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
or

sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# 如果网络不通我们可以按照下面的方法安装
# 下载 ohmyzsh 的 zip压缩包. https://github.com/ohmyzsh/ohmyzsh
# 解压后重命名文件夹为~/.oh-my-zsh：mv ohmyzsh-master ~/.oh-my-zsh
# 创建zsh配置文件：cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc

```

### 3. chsh -s $(which zsh)

### 4. 重新开启一个终端就可以了

### 5. 更改显示样式

#### 5.1修改自带主题

```
vim ~/.zshrc
#修改
ZSH_THEME="adben"

```

#### 5.2 自带主题展示

简单的列举两个样式，其实有很多，也可以自定义样式，就不一一列举了

```
# 1 ZSH_THEME="adben"
&lt;&lt; root@41b810c41ed9~/xxx
ll&gt;                                                                                                                ‹git:master ✔› 20:29.37 Thu Nov 10 2022 &gt;&gt;&gt; 
total 24K
-rw-r--r-- 1 root root    0 Nov 10 18:57 README.md
drwxr-xr-x 1 root root 4.0K Nov 10 19:14 bin
drwxr-xr-x 2 root root 4.0K Nov 10 18:57 client
drwxr-xr-x 2 root root 4.0K Nov 10 18:57 config
drwxr-xr-x 3 root root 4.0K Nov 10 18:57 script
drwxr-xr-x 1 root root 4.0K Nov 10 19:11 src
&lt;&lt;&lt; 
&lt;&lt;&lt; root@41b810c41ed9~/xxx
&gt;&gt;&gt; 
# 2 ZSH_THEME="af-magic"
~/workdir/xxx (master) » ll                                                                                                                                                         xxx@xxxdeMacBook-Pro
total 24
-rw-r--r--   1 xxx  staff   1.3K Jul  5 15:00 Makefile
-rw-r--r--   1 xxx  staff   453B Jul  5 15:00 README.md
drwxr-xr-x   5 xxx  staff   160B Nov  2 14:15 bin
-rw-r--r--   1 xxx  staff   568B Jul  5 15:00 build.sh
drwxr-xr-x   8 xxx  staff   256B Jul  5 15:00 config
drwxr-xr-x   3 xxx  staff    96B Jul  5 15:00 doc
drwxr-xr-x   4 xxx  staff   128B Jul  5 15:02 pkg
drwxr-xr-x   5 xxx  staff   160B Nov  1 15:21 scripts
drwxr-xr-x  15 xxx  staff   480B Nov  8 12:03 src
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
~/workdir/xxx (master) »


```
