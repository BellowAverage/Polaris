
--- 
title:  Java 面试官：说说 final、finally、finalize 的区别 
tags: []
categories: [] 

---


#### 目录
- <ul><li>- - 


### final

final 用于修饰变量、方法和类。
-  final 变量：被修饰的变量不可变，不可变分为`引用不可变`和`对象不可变`，final 指的是`引用不可变`，final 修饰的变量必须初始化，通常称被修饰的变量为`常量`。 -  final 方法：被修饰的方法不允许任何子类重写，子类可以使用该方法。 -  final 类：被修饰的类不能被继承，所有方法不能被重写。 
### finally

finally 作为异常处理的一部分，它只能在 `try/catch` 语句中，并且附带一个语句块表示这段语句最终一定被执行（无论是否抛出异常），经常被用在需要释放资源的情况下，`System.exit (0)` 可以阻断 finally 执行。

### finalize

finalize 是在 `java.lang.Object` 里定义的方法，也就是说每一个对象都有这么个方法，这个方法在 `gc` 启动，该对象被回收的时候被调用。

一个对象的 finalize 方法只会被调用一次，finalize 被调用不一定会立即回收该对象，所以有可能调用 finalize 后，该对象又不需要被回收了，然后到了真正要被回收的时候，因为前面调用过一次，所以不会再次调用 finalize 了，进而产生问题，因此不推荐使用 finalize 方法。

<img src="https://img-blog.csdnimg.cn/20191007101439261.JPG#pic_center" alt="在这里插入图片描述" width="600" height="350">
