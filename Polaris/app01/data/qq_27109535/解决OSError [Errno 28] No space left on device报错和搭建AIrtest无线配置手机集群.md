
--- 
title:  解决OSError: [Errno 28] No space left on device报错和搭建AIrtest无线配置手机集群 
tags: []
categories: [] 

---
### OSError: [Errno 28] No space left on device和搭建AIrtest无线配置手机集群

做手机无限集群控制时，常常遇到这种错误问题。表示您的设备上没有足够的可用磁盘空间来完成某个操作。我们遇到了还得重新开端口和输入ip，如果有几百台手机是不是中午就不吃饭了，还的搞完。当然云服务哪些就不说了，出钱了用起来肯定更方便。回到这个话题，遇到这种问题了，手机有些关机了，那就重新配端口吧，开好端口。

```
#adb tcpip xxxx ( 设置现连接手机的连接端口为XXXX）
adb connect &lt;设备的IP地址&gt;:5555
adb kill-server
start-server
adb devices
adb connect &lt;设备的IP地址&gt;:5555`

```

<img src="https://img-blog.csdnimg.cn/d3fd9d40ca4644db8fe2e989b65197cb.png" alt="请添加图片描述">

主要清理两部分的缓存: pip 缓存和 conda 缓存 在cmd命令中执行

```

#1 . 清理pip 缓存

pip cache purge


# 2. 清理conda 缓存

conda clean --all



```

以后再运行时，应一个小时在cmd命令中运行一次上面两次清理缓存。写的比较广，遇到问题的小伙伴，跟着操作，避免中午或者晚上熬夜搞手机无线端口，我踩过的坑，希望帮到你。
