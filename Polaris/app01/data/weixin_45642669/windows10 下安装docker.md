
--- 
title:  windows10 下安装docker 
tags: []
categories: [] 

---
在power shell 里面使用管理员权限执行；（win10以上，以下全部都是管理员权限）

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All

```

下载docker



然后执行。

执行

```
cd "C:\Program Files\Docker\Docker"

.\DockerCli.exe -SwitchDaemon

```

下载wsl

路径位置：





```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

```

```
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

```

```
wsl --set-default-version 2

```

重启服务器即可。

## 迁移docker到D盘

https://blog.csdn.net/weixin_41166529/article/details/128597650
