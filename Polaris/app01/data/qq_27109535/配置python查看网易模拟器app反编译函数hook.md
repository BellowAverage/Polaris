
--- 
title:  配置python查看网易模拟器app反编译函数hook 
tags: []
categories: [] 

---
## 配置python查看网易模拟器app反编译函数hook

### 一、电脑终端安装：frida

```
# 方法一
pip install frida
pip install frida-tools
## 方法一 镜像安装
pip install frida -i https://pypi.mirrors.ustc.edu.cn/simple/ 
pip install frida-tools -i https://pypi.mirrors.ustc.edu.cn/simple/

#查看frida版本
frida --version

# 启动
adb start-server
adb kill-server


#连接设备
adb connect 127.0.0.1:7555
#查看连接设备
adb devices

```

### 二、手机安装：frida（root权限）

```
1. 确定手机的CPU架构（多少位）
 
adb -s emulator-5554 shell getprop ro.product.cpu.abi   模拟器：x86_64
2. 下载frida-server 包（模拟器的位数下载）
    https://github.com/frida/frida/releases
    https://github.com/frida/frida/releases

4. 解压，改名 frida-server，将 frida-server 上传到手机上。
adb -s 设备 push  xx/xxx/xxx/frida-server  /sdcard

5.通过adb shell 进入手机​
adb root
adb shell       进入手机
su -            获得root权限

6.给frida-server赋可执行权限
chmod 777 frida-server

```

### 三、pycharm连接mu模拟器准备工作

```
1.终端运行
# 电脑通过adb进行端口的转发
adb forward tcp:27042 tcp:27042
adb forward tcp:27043 tcp:27043

2.adb的shell进入手机并运行起来frida

adb shell       进入手机
su -            获得root权限
cd /sdcard      模拟器路径
./frida-server  启动frida-server

```

### 四、pycharm查看mu模拟器app信息

```
# -*- coding: utf-8 -*-
import frida
# 获取设备信息
rdev = frida.get_remote_device()
print(rdev)
# 枚举所有的进程
processes = rdev.enumerate_processes()
for process in processes:
    print (process)

```
