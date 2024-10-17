
--- 
title:  Qt 程序异常结束 并且crashed——解决方法 （动态链接库） 
tags: []
categories: [] 

---
出现这个问题，依据网上的案例，基本上确定为动态链接库有问题，事实上确实是这个问题。 <img src="https://img-blog.csdnimg.cn/20190507213134863." alt="在这里插入图片描述">

解决方法： **第一步** 在添加库时 <img src="https://img-blog.csdnimg.cn/20190507213450187.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190507213633957.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190507213653539.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 将代码添加到.pro文件中

```
win32: LIBS += -L$$PWD/../../../install/x64/mingw/lib/ -llibopencv_calib3d344.dll
win32: LIBS += -L$$PWD/../../../install/x64/mingw/lib/ -llibopencv_core344.dll
win32: LIBS += -L$$PWD/../../../install/x64/mingw/lib/ -llibopencv_dnn344.dll
win32: LIBS += -L$$PWD/../../../install/x64/mingw/lib/ -llibopencv_features2d344.dll
win32: LIBS += -L$$PWD/../../../install/x64/mingw/lib/ -llibopencv_flann344.dll
win32: LIBS += -L$$PWD/../../../install/x64/mingw/lib/ -llibopencv_highgui344.dll
win32: LIBS += -L$$PWD/../../../install/x64/mingw/lib/ -llibopencv_imgcodecs344.dll
win32: LIBS += -L$$PWD/../../../install/x64/mingw/lib/ -llibopencv_imgproc344.dll
win32: LIBS += -L$$PWD/../../../install/x64/mingw/lib/ -llibopencv_ml344.dll
win32: LIBS += -L$$PWD/../../../install/x64/mingw/lib/ -llibopencv_objdetect344.dll
win32: LIBS += -L$$PWD/../../../install/x64/mingw/lib/ -llibopencv_photo344.dll
win32: LIBS += -L$$PWD/../../../install/x64/mingw/lib/ -llibopencv_shape344.dll
win32: LIBS += -L$$PWD/../../../install/x64/mingw/lib/ -llibopencv_stitching344.dll
win32: LIBS += -L$$PWD/../../../install/x64/mingw/lib/ -llibopencv_superres344.dll
win32: LIBS += -L$$PWD/../../../install/x64/mingw/lib/ -llibopencv_video344.dll
win32: LIBS += -L$$PWD/../../../install/x64/mingw/lib/ -llibopencv_videoio344.dll
win32: LIBS += -L$$PWD/../../../install/x64/mingw/lib/ -llibopencv_videostab344.dll
INCLUDEPATH += $$PWD/../../../install/include
DEPENDPATH += $$PWD/../../../install/include

```

这样可以确保链接库的路径没有错 但是错误还是出现。

**第二步** 在环境变量中添加动态库的路径。 注意，一定要在**系统变量的path**中加（在用户变量的path中之前已经加了，但是还是会报错） <img src="https://img-blog.csdnimg.cn/20190507214145780.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20190507214104797.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

**第三步** 构建-&gt;执行qmake

然后再次运行 一般就没有错误啦~
