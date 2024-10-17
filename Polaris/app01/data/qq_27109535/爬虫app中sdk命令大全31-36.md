
--- 
title:  爬虫app中sdk命令大全31-36 
tags: []
categories: [] 

---
### 1.查看连接设备

```
adb devices

```

直接ip时，模拟设备 设备，名称是真实设备 <img src="https://img-blog.csdnimg.cn/2aaabc0ab28d4d46b1b01aeba00ea214.png" alt="在这里插入图片描述">

### 2. 进入设备底层中

```
# 进入设备底层中
adb -s 127.0.0.1:62001 shell

ls
# 退出
exit

```

#表示root权限 $表示没root权限

<img src="https://img-blog.csdnimg.cn/837d1ebd990f42f394741899cf273378.png" alt="在这里插入图片描述">

### 3.命令行安装卸载app

```
adb -s 127.0.0.1:62001 install

```

<img src="https://img-blog.csdnimg.cn/b2257498dc764356ab140916524b3003.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/c49f8f98bdd84045a282b716a34fe79d.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/6279cf0b82ea4344a6f01b300ef0b570.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/58a5a216ff104d7aa787db982f7ba095.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/a0d31efdf9644881b3d00b8610285ebd.png" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/b2ae0a3df4a343a6a1567d2f4d95e8dc.png" alt="在这里插入图片描述">

**## 卸载**

```
adb -s 127.0.0.1:62001 shell  #  进入设备
cd /data/app  # 定位安装包路径
ls  #显示文件
exit
#adb -s 127.0.0.1:62001 uninstall 包名
adb -s 127.0.0.1:62001 uninstall com.douguo.recipe

```

<img src="https://img-blog.csdnimg.cn/5fcee840547b4d3abede7bd185d78e2f.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/241f03d76506464a8c22737faab04c4e.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/85fb5c29b5e94a5aa3032594eeff59e9.png" alt="4.">

### 4.无法连接设备

设备和adb server都是启动状态

```
adb devices
adb connect 127.0.0.1:62001
adb devices

```

<img src="https://img-blog.csdnimg.cn/0b9789b677214534bc2177bb2db650f1.png" alt="在这里插入图片描述">

### 5. 查看app名

上面有文件目录查看安装的app名

```
adb shell pm list package

```

<img src="https://img-blog.csdnimg.cn/d6dedcba909f4af1854f7efde8510d82.png" alt="在这里插入图片描述">

### 6.把pc与设备文件互传

```
adb push E:\下载内容\README.txt /sdcard

```

<img src="https://img-blog.csdnimg.cn/64a75f0cdf864883bb10dc054394a034.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/bd58e1ecd23e4f44845394aa62f4645f.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/18d20553be234591bf719ed35c598bdc.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/0c96e05a5c434dfaa76b34fc789ba425.png" alt="在这里插入图片描述">

```
#不能再磁盘根目录下，不然会报错权限问题
adb pull /sdcard/READ E:\下载内容\文件互传

```

<img src="https://img-blog.csdnimg.cn/5a92e5a10ffc45fca73d92de4ab0679e.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/bd40a469c29a476e84449e5e46268d42.png" alt="在这里插入图片描述">

### 7. 截图

```
adb shell screencap /sdcard/test.png

```

<img src="https://img-blog.csdnimg.cn/5070c626ebd44ac1acb555d974f1987e.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/074dfc123ebe4e3dac55b0544e7eaa28.png" alt="在这里插入图片描述"> 拿出来

```
adb pull /sdcard/test.png E:\下载内容\文件互传

```

<img src="https://img-blog.csdnimg.cn/55a5fd1754384092877fb98a56dafe32.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/603947f488ef4a44a2d7632dd17fe233.png" alt="在这里插入图片描述">

### 8. uiautomator

<img src="https://img-blog.csdnimg.cn/b91d3660ebd94fb88993c9dd82c31866.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/eec79bf694cd4f7f98110b3d9dc758f0.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/4c9573a389ae48a38faea25dc12cde28.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/518b4d5859c04f6ea605d4684ca6dde1.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d0ad061cc9d54bc7bee49b40eefea0db.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/70c15e321f0a47e1bc56e9231d78ee19.png" alt="在这里插入图片描述">
