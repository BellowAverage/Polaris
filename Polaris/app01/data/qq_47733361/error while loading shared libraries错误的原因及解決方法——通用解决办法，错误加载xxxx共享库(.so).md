
--- 
title:  error while loading shared libraries错误的原因及解決方法——通用解决办法，错误加载xxxx共享库(.so) 
tags: []
categories: [] 

---
在linux下整合log4cpp日志框架时，出现了下面的错误：当加载共享库时出错，找不到共享库 XXXX

```
[root@hecs-207177 cworkspace]# ./Log4cppTest 
./Log4cppTest: error while loading shared libraries: liblog4cpp.so.5: cannot open shared object file: No such file or directory

```

### 通用解决办法：

#### 1、首先使用find命令，查找报错中的共享库路径

此处我以上面报错为例：

```
find / -name 共享库

```

```
[root@hecs-207177 cworkspace]# find / -name liblog4cpp.so.5
/usr/local/lib/liblog4cpp.so.5
/usr/src/log4cpp/src/.libs/liblog4cpp.so.5

```

#### 2、将上面路径加入到 /etc/ld.so.conf 中

```
[root@hecs-207177 cworkspace]# vim /etc/ld.so.conf

```

注意，此处只需要将 lib 目录加入即可，如下图： <img src="https://img-blog.csdnimg.cn/6335e3744c9346088e3a675a6b710994.png" alt="在这里插入图片描述">

#### 3、使用 ldconfig 命令加载刚刚加入的共享库

```
ldconfig

```
