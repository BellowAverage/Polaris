
--- 
title:  centos7编译 C++ 使用log4cpp框架——/usr/local/lib/liblog4cpp.so：对‘pthread_key_create’未定义的引用（已解决） 
tags: []
categories: [] 

---
### 错误如下：

```
[root@node2 test]# g++ -o Log4cppTest Log4cppTest.cpp -llog4cpp
/usr/local/lib/liblog4cpp.so：对‘pthread_key_create’未定义的引用
/usr/local/lib/liblog4cpp.so：对‘pthread_getspecific’未定义的引用
/usr/local/lib/liblog4cpp.so：对‘pthread_key_delete’未定义的引用
/usr/local/lib/liblog4cpp.so：对‘pthread_setspecific’未定义的引用

```

### 问题及解决：

出现上述问题的原因是因为编译时没有链接 **lpthread** 库的原因，因此将编译命令改为如下：

```
g++ -o Log4cppTest Log4cppTest.cpp -llog4cpp -lpthread

```

编译成功！
