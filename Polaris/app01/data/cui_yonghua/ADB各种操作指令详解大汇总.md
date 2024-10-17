
--- 
title:  ADB各种操作指令详解大汇总 
tags: []
categories: [] 

---
### 一. ADB概述

**1. ADB**：ADB，即 Android Debug Bridge，它是 Android 开发/测试人员不可替代的强大工具，也是 Android 设备玩家的好玩具。可用于执行各种设备操作（例如安装和调试应用），并提供对 Unix shell（可用来在设备上运行各种命令）的访问权限。它是一种客户端-服务器程序，包括以下三个组件：
- `客户端`：用于发送命令。客户端在开发计算机上运行。您可以通过发出 ADB命令来从命令行终端调用客户端。- `守护进程`：在设备上运行命令。守护进程在每个设备上作为后台进程运行。- `服务器`：管理客户端和守护进程之间的通信。服务器在开发机器上作为后台进程运行。 通过这个命令行工具我们可以使用它来操作手机上的资源，而且不需要借助Android SDK就可以轻松操控手机里的应用。
安卓调试桥 (Android Debug Bridge, adb)，是一种可以用来操作手机设备或模拟器的命令行工具。它存在于 sdk/platform-tools 目录下。虽然现在 Android Studio 已经将大部分 ADB 命令以图形化的形式实现了，但是了解一下还是有必要的。

**2. 工作原理**：启动某个ADB客户端时，客户端会先检查是否有 ADB服务器进程正在运行。如果没有，它将启动服务器进程。服务器在启动后会与本地 TCP 端口 5037 绑定，并监听 ADB 客户端发出的命令 - 所有 ADB客户端均通过端口 5037 与 ADB 服务器通信。 然后，服务器会与所有正在运行的设备建立连接。它通过扫描 5555 到 5585 之间（该范围供前 16 个模拟器使用）的奇数号端口查找模拟器。服务器一旦发现ADB守护进程 (ADBD)，便会与相应的端口建立连接。请注意，每个模拟器都使用一对按顺序排列的端口 - 用于控制台连接的偶数号端口和用于ADB 连接的奇数号端口。

**3. 为什么要用 ADB?**

ADB 可以直接操作管理手机模拟器或者真实的手机设备(如华为手机)。它的主要功能有：
- 运行设备的 shell(命令行)- 管理模拟器或设备的端口映射- 计算机和设备之间上传/下载文件- 可以对设备的应用进行卸载安装等- 在 App 遇到 ANR/Crash 等 bug 时，可以通过 ADB 来抓取日志
简而言之，ADB 就是连接 Android 手机与 PC 端的桥梁，可以让用户在电脑上对手机进行全面的操作！

### 二. 基本指令操作

#### 2.1 设备的启动关闭操作

这里我选择连接模拟器，看看连接有什么区别。

1).连接设备

```
adb connect 127.0.0.1:62001#连接一个模拟器

```

2).启动服务

```
adb start-server#开启服务

# 启动服务
adb shell am startservice "com.zhy.aaa/com.zhy.aaa.MyService"

```

3).查看设备

```
adb devices #查看设备信息
adb version #设备版本
adb help #帮助文档 
adb get-state #查看设备状态 device(正常连接),offline(连接异常),unknown(没有连接)
adb get-serialno #获取序列号
adb get-devpath #获取设备路径
adb shell cat /system/build.prop #获取设备名称

```

4).操作多个设备

```
adb —a 监听所有网络接口,而不仅仅是localhost
　　-d 使用USB设备(如果多个设备连接错误)
　　-e 使用TCP / IP设备(如果可用多个TCP / IP设备错误)
　　-s 使用给定的序列号(覆盖ANDROID_SERIAL)
　　-t 使用给定设备ID
　　-h adb服务器主机名称(默认= localhost)
　　-p adb服务器的端口(默认= 5037)
　　-l 监听来自套接字的adb服务器(默认= tcp: localhost: 5037)
　　例如：adb -s 127.0.0.1:62001 shell

```

这样就进入了模拟器的Shell界面了。

5).关闭服务

```
adb kill-server

```

6).设置监听TCP/IP的端口

```
adb tcpip 5555

```

7).断开连接

```
adb disconnect 127.0.0.1:62001

```

8).关机与重启

```
adb reboot #设备重启
adb shutdown #设备关机

```

9).Root权限

```
adb root   # 正常输出：restarting adbd as root
adb unroot # 取消root权限

```

10).刷机模式

```
adb reboot bootloader #重启到bootloader，即刷机模式
adb reboot recovery #重启到recovery，即恢复模式
adb sideload &lt;path-to-update.zip&gt;#更新系统

```

11).命令转载

```
adb wait-for-device # 在模拟器/设备连接之前把命令转载在adb的命令器中

```

#### 2.2 设备的应用操作

1).查看应用

```
adb shell pm list packages #所有应用， 显示所有包名
adb shell pm list package -f #
adb shell pm list packages -s #系统应用， 显示系统应用包名
adb shell pm list packages -3 #三方应用， 显示第三方应用包名
adb shell pm list packages | findstr bluetooth #过滤应用  管道符进行搜索，Linux下使用grep

```

2).查看应用的Activity信息

```
adb shell dumpsys package com.android.bluetooth #查看系统应用蓝牙的包名信息
adb shell dumpsys activity activities #查看所有的活动程序包名
adb shell dumpsys activity | findstr mFocusedActivity #查看当前重启的是哪个包
adb shell dumpsys activity top | findstr activity #查找设备活动程序的父窗口

```

3).清除应用数据和缓存

```
adb shell pm clear

```

4).安装卸载应用

```
adb install D:/aa.apk #安装在电脑上的apk， adb install &lt;apk 文件路径 &gt;
adb install -r D:/aa.apk#覆盖安装 保留数据和缓存文件 -g 授予所有运行时权限
adb shell pm install /scard/picture#安装在手机上的apk
adb uninstall -k 包名，在模拟器或者真机中需要使用 -s来指定

```

#### 2.3 日志

```
adb logcat#查看日志
adb logcat -v time #打印详情日志，会记录当前的所有操作行为以及产生的结果,默认持续监听，按下Ctrl+c即可结束
adb logcat -v time &gt;D:\log.txt #保存日志到电脑
adb logcat -f /sdcard/1.txt    #保存日志到手机
adb logcat | findstr com.android.bluetooth #保存指定包名的日志
adb logcat -c  #清除之前的日志输出
adb logcat | findstr ActivityManager  #查看当前正在运行的Activity
adb logcat | findstr Displayed        #查看当前正在运行的Activity
adb bugreport #查看bug报告
adb logcat -b radio #无线通讯的日志
adb shell dmesg #内核日志

```

#### 2.4 设备文件操作

```
#把电脑上的文件传到手机储存卡中
# adb push &lt; 本地路径 &gt; &lt; 手机端路径 &gt;
adb push C:\Users\Administrator\Desktop\1.gif /sdcard/

#把手机存储卡里的文件传到电脑
# adb pull &lt; 手机端文件 &gt; &lt; 本地路径 &gt;
adb pull /sdcard/1.gif C:\Users\Administrator\Desktop\

```

#### 2.5 截屏，录屏

```
adb shell screencap /sdcard/1.png #当前窗口截屏保存到手机
adb shell /system/bin/screencap -p /sdcard/2.png
adb exec-out screencap -p &gt;1.png #截图保存到电脑
adb shell screenrecord &gt;1.mp4  #屏幕录像，Ctrl+c停止录制
--size #视频大小
--bit-rate #比特率
--time-limit #持续时间
--verbose #命令行显示log信息
注：模拟器和安卓4.4以下版本不支持录屏

```

#### 2.6 Shell

Shell里有很多命令，简单列举下：

```
cat	显示文件内容
cd	切换目录
chmod	改变文件的存取模式/访问权限
df	查看磁盘空间使用情况
grep	过滤输出
kill	杀死指定 PID 的进程
ls	列举目录内容
mount	挂载目录的查看和管理
mv	移动或重命名文件
ps	查看正在运行的进程
rm	删除文件
top	查看进程的资源占用情况

```

1).进入退出

```
# 将登录设备的 shell(内核)，登录 shell 后可以使用 cd、ls、rm 等 Linux 命令
adb shell #进入shell 返回$ 则没有root权限  #有root权限
exit #退出shell

```

2).设备的相关信息

```
adb shell getprop ro.build.version.release #安卓系统版本
adb get-serialno #获取设备的序列号（设备号）
adb shell getprop ro.product.model # 查看设备型号
adb shell cat /sys/class/net/wlan0/address #查看MAC地址
adb shell wm size #设备屏幕分辨率
adb shell wm size 400X654 #设置屏幕分辨率
adb shell wm size reset #恢复原屏幕分辨率
adb shell wm density #设备屏幕密度
adb shell wm density 100 #修改屏幕密度为100dpi
adb shell wm density reset #恢复原屏幕密度
adb shell wm overscan 10,20,30,100 #显示区域
adb shell wm overscan reset #恢复原显示区域
adb shell dumpsys window displays #显示屏参数
adb shell service list  #查看后台services信息
adb shell settings put global adb_enabled 0 #关闭 USB 调试模式
adb shell uiautomator dump   #获取当前界面的控件信息
adb shell ime list -s  #设备上的输入法

```

3).进程

```
adb shell ps #查看手机正在运行的进程 adb shell ps | findstr bluetooth 
adb shell ps -x pid #查看指定pid的进程状态信息
adb shell kill pid #根据进程号杀进程
adb shell procrank #杀进程 
adb shell start adbd #启动守护进程
adb shell stop adbd  #关闭守护进程

```

4).性能分析

```
adb shell cat /proc/cpuinfo #获取CPU序列号
adb shell cat /proc/meminfo #查看当前内存占用
adb shell cat /proc/iomem #查看IO内存分区
adb remount #将system分区重新挂载为可读写分区
adb shell dumpsys meminfo bluetooth #查看蓝牙占用的内存
adb shell dumpsys cpuinfo | findstr bluetooth #获取CPU
adb shell top #查看实时资源占用情况
adb shell top -n 1 | findstr bluetooth #刷新一次内存信息，然后返回蓝牙内存占用
adb shell top #查看设备cpu和内存占用情况
adb shell top -m 6 #查看占用内存前6的app
adb shell dumpsys gfxinfo bluetooth #获取流畅度相关
adb shell netcfg #查看设备的网络连接情况
adb shell ifconfig wlan0 #获取wlan0的IP地址和子网掩码

```

5).文件操作

```
adb shell ls #列出目录下的文件和文件夹
adb shell cd sys #切换当前目录为sys
adb shell rename 旧文件名 新文件名 #重命名文件名
adb shell rm /sys/1.apk #删除指定目录下的文件
adb shell rm -r #删除指定目录下的文件夹及其子目录
adb shell mv 旧文件名 新文件名 #移动文件
adb shell chmod 777 1.jpg #设置文件权限
adb shell mkdir 文件夹名 #新建文件夹
adb shell cat 文件 #查看文件内容
adb shell cat /data/misc/wifi/*.conf #查看WiFi密码

```

6).按键

```
adb shell input keyevent 3 # HOME 键
adb shell input keyevent 4 # 返回键
adb shell input keyevent 5 # 拨号
adb shell input keyevent 6 # 挂断
adb shell input keyevent 24 # 音量+
adb shell input keyevent 25 # 音量-
adb shell input keyevent 26 # 电源键
adb shell input keyevent 27 # 拍照
adb shell input keyevent 64 # 打开浏览器
adb shell input keyevent 82 # 菜单键
adb shell input keyevent 85 # 播放/暂停
adb shell input keyevent 86 # 停止播放
adb shell input keyevent 87 # 播放下一首
adb shell input keyevent 88 # 播放上一首
adb shell input keyevent 122 #移动光标到行首或列表顶部 
adb shell input keyevent 123 #移动光标到行尾或列表底部
adb shell input keyevent 126 # 恢复播放
adb shell input keyevent 127 # 暂停播放
adb shell input keyevent 164 # 静音 
adb shell input keyevent 176 # 打开系统设置 
adb shell input keyevent 187 # 切换应用
adb shell input keyevent 207 # 打开联系人 
adb shell input keyevent 208 # 打开日历
adb shell input keyevent 209 # 打开音乐
adb shell input keyevent 210 # 打开计算器 
adb shell input keyevent 220 # 降低屏幕亮度
adb shell input keyevent 221 # 提高屏幕亮度
adb shell input keyevent 223 # 休眠
adb shell input keyevent 224 # 点亮屏幕
adb shell input keyevent 231 # 打开语音助手
adb shell input keyevent 276 # 如果没有 wakelock 则让系统休眠

```

7).点击，滑动屏幕

```
adb shell input tap 100 300 #在(100,300)处点击
adb shell input swipe 100 1200 100 200 #上滑
adb shell input swipe 100 200 100 1200  #下滑

```

8).输入

```
adb shell input text hello  #输入hello

```

9).电池

```
adb shell dumpsys battery

```

10).设备ID

```
adb shell settings get secure android_id

```

11).无线网络 在操作前必须获得Root权限。

```
adb shell svc wifi enable  #开启WiFi
adb shell svc wifi disable #关闭WiFi

```

#### 2.7 端口转发

```
adb forward tcp:60 tcp:70 #将60端口转到70端口
adb forward tcp:60 local:logd # 将60端口转到local:logd的转发

```

#### 2.8 Activity 管理器

```
adb shell am start -n activity路径 #启动某一个activity
adb shell am start -a android.intent.action.VIEW -d www.baidu.com#启动默认浏览器打开一个网页
adb shell am start -n com.android.camera/.Camera #启动相机
adb shell am start -a android.intent.action.CALL -d tel:10086#启动拨号10086
adb shell am startservice -n 服务 #开启服务
adb shell am stopservice  服务 #停止服务
adb shell am force-stop bluetooth #杀死蓝牙进程
adb shell am kill 进程号  #杀掉进程
adb shell am broadcast -a android.intent.action.BOOT_COMPLETED #向所有组件广播设备启动完毕

```

#### 2.9 调用软件包管理器

```
adb shell pm list permissions #查看权限
adb shell pm list permission-groups #输出所有已知的权限组
adb shell pm list permissions -d -g -f #查看系统危险权限并按组输出所有信息
adb shell pm list instrumentation#列出所有测试软件包,-f列出测试软件包的APK文件
adb shell pm path com.android.bluetooth #查看软件安装路径
adb shell pm list features  #输出系统的所有功能
adb shell pm list libraries #输出当前设备支持的所有库
adb shell pm list users #输出系统中的所有用户
adb shell pm enable ** #启用给定的软件包或组件（写为“package/class”）
adb shell pm disable ** #停用给定的软件包或组件（写为“package/class”）
adb shell pm get-max-users #输出设备支持的最大用户数

```

#### 2.10 备份

```
adb backup -all #备份所有数据

```

#### 2.11 压力测试，Monkey格式：

```
adb shell monkey -v -p your.package.name 500
adb shell monkey -v -p com.tencent.weishi 500

```
