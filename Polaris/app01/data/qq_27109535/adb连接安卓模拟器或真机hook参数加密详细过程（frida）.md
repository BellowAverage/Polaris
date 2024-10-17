
--- 
title:  adb连接安卓模拟器或真机hook参数加密详细过程（frida） 
tags: []
categories: [] 

---
app逆向时，参数与函数的确定很关键，找到可疑的函数，不确定是否由该函数生成，该怎么解决？hook就应允而生了，首先是要求本地电脑和安卓模拟器（网易mumu模拟器支持多系统，该模拟器作为主流）或真机的连接，无论是网易mumu模拟器还是真机都要取得超级权限（root），用两者的区别在于是否java函数中调用c，java函数中调用c就用真机。 adb连接安卓模拟器或真机hook参数加密详细过程（frida）

### 一、终端安装frida第三方包

```
pip install frida==14.2.18
pip install frida-tools==9.2.5

```

### 二、adb连接安卓模拟器与真机的详细过程

```
&gt;&gt;&gt;adb kill-server
​
&gt;&gt;&gt;adb start-server

模拟机的连接/真机自动连接
&gt;&gt;&gt;adb connect 127.0.0.1:7555

&gt;&gt;&gt;adb devices
List of devices attached
emulator-5554   device
1a9f22350107    device
​

电脑上的apk安装
&gt;&gt;&gt;adb -s emulator-5554  install F:xxx/xxx/xxx/x.apk



cpu架构
&gt;&gt;&gt;adb -s bmus5t7dvkofmvgu shell getprop ro.product.cpu.abi  
arm64-v8a  表示模拟器CPU是arm -&gt; 64位
​
&gt;&gt;&gt;adb -s 1a9f22350107 shell getprop ro.product.cpu.abi
x86_64        表示模拟器CPU是x86 -&gt; 64位

&gt;&gt;&gt;adb -s 1a9f22350107 shell getprop ro.product.cpu.abi
armeabi-v7a   表示模拟器CPU是arm -&gt; 32位
​
&gt;&gt;&gt;adb -s 1a9f22350107 shell        # 登录设备
&gt;&gt;&gt;adb -s emulator-5554 shell       # 登录设备
&gt;&gt;&gt;adb shell  一个设备
cezanne:/ $ su -  相当于root最高权限
​
本地电脑文件迁移到设备上    移动文件
&gt;&gt;&gt;adb push D:\xxxx\xxxxxx\xxxxxxx /sdcard/


```

### 三、安装frida

下载：https://github.com/frida/frida/releases<img src="https://img-blog.csdnimg.cn/1b070b1e4ac54020bb84ef84a6322ffb.png" alt="在这里插入图片描述">

```
安装：
    - 【电脑】解压
    - 【电脑】文件上传到设备
        adb push C:\2345Downloads\... /sdcard
    - 【手机】将frida-server..文件移动到手机的 /data/local/tmp 目录
        &gt;&gt;&gt;adb shell
        &gt;&gt;&gt;su -
        &gt;&gt;&gt;cd sdcard
                &gt;&gt;&gt;ls
        &gt;&gt;&gt;mv frida-server-14.2.18-android-x86_64  /data/local/tmp
    - 【进入】
        &gt;&gt;&gt;cd /data/local/tmp
    - 【授权】授予可执行的权限
        &gt;&gt;&gt;chmod 777 frida-server-14.2.18-android-x86_64
       # chmod 777 frida-server-14.2.18-android-arm64

```

### 四、 启动和Hook

```
&gt;&gt;&gt;adb shell
&gt;&gt;&gt;su -
&gt;&gt;&gt;cd /data/local/tmp/
&gt;&gt;&gt;./frida-server-14.2.18-android-x86_64


```

端口的转发

```
&gt;&gt;&gt;adb forward tcp:27042 tcp:27042
&gt;&gt;&gt;adb forward tcp:27043 tcp:27043

```

查看包名

```
# 枚举手机上的所有进程 &amp; 前台进程
import frida

# 获取设备信息
rdev = frida.get_remote_device()
print(rdev)

# 枚举所有的进程
processes = rdev.enumerate_processes()
for process in processes:
    print(process)

# 获取在前台运行的APP
front_app = rdev.get_frontmost_application()
print(front_app)

```

搜索url或关键词 找到可疑之处查看包、类、方法名 <img src="https://img-blog.csdnimg.cn/8145ef97db6d44479fb52866ed119971.png" alt="在这里插入图片描述">

```
import frida
import sys

# 连接手机设备
rdev = frida.get_remote_device()

# Hook手机上的那个APP（app的包名字）
# 注意事项：在运行这个代码之前，一定要先在手机上启动app
session = rdev.attach("app的包名字")  

scr = """
Java.perform(function () {

    // 包.类
    var AHAPIHelper = Java.use("包.类");


    // Hook，替换  implementation实现 
    类.方法名.implementation = function(context,map){
        console.log(123);
        
        // 执行原来的方法
        this.方法名(context,map);
        // 执行原来的方法（如果有返回值）
        // var x =   this.方法名(context,map);
        // retrun x;
                    
        console.log(666);

    }
    
});
""" 
// 读取脚本
script = session.create_script(scr)

// 回调函数
def on_message(message, data):
    print(message, data)


script.on("message", on_message)

// 加载
script.load()
// 等待
sys.stdin.read()


```
