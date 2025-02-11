
--- 
title:  PHP设计模式之单例模式 
tags: []
categories: [] 

---
####   单例模式的定义

        单例模式是一种对象创建模式，单例顾名思义就是只有一个实例，因此单例类不能被外部多次创建以及克隆。单例模式主要应用于对资源消耗较多的场景中，为了防止随意创建浪费了资源。

####  单例模式的特点

        单例模式由于不能被外部实例化只能通过自身实例化，因此需要将构造函数进行私有化，同时需要提供一个公共的实例化入口。

它的结构值需要记住一句三私一公：

1. 私有的构造方法    //防止多次创建和防止继承，防止外部实例化

2. 私有的静态属性    //用于存放唯一的自身实例

3. 私有的克隆方法  //防止克隆

4. 公共静态创建方法  //开放公共的静态创建方法给外部调用，自身进行实例化。

#### 代码实现

代码的实现如下：

>  
 <pre>class sigle {
   //私有静态属性
    private static $instance = null;
   //私有的构造函数
    private function __construct(){
    }
    //公共的静态创建方法
    public static function getInstance(){
       if(!(self::$instance instanceof self)){
          self::$instance = new self();
       }
       return self::$instance;
    }
    //私有化的克隆方法
    private function __clone(){
       
    }
}</pre> 


#### 单例模式的优缺点

##### 优点

1. 降低内存占用，只能实例化一次，不能重复实例化减少内存的占用。

2.  提升系统性能，由于只能生成一个实例，且实例常驻在内存中，因此可以减少内存的申请和释放所带来的性能消耗。

3. 避免资源多重占用，在一个实例中操作文件的读写操作，可以避免同一个资源被多个实例进行多重的读写操作。

##### 缺点

1. 扩展难度高，如果有需要扩展或者修改只能修改单例下的代码。

2. 容易引发内存泄漏，如果单例对象有Context，那么很容易引发内存泄漏，所以需要注意传递给单例对象的Context最好是Application Context。

#### 适用场景

1. 设计数据库连接池，由于数据库连接是数据库的一种资源，降低数据库资源的使用可以提高数据库的性能。因此使用单例模式来设计数据库的数据库连接池，可以大大降低数据库资源多次开启关闭带来的资源损耗。

2. 设计多线程线程池，这个和数据库一样，线程是操作系统的资源，使用单例可以更方便线程池中的线程进行管理。

3. 文件系统，对于操作系统而言文件系统主要的还是在IO的读写上，如果重复IO读写操作对操作系统的压力也很大，使用单例模式的话，操作系统上只有一个文件系统进行操作，可减低操作系统的压力。

#### 总结

        单例模式就是集中管理权，将一些耗性能、耗资源的操作集中在一个类里操作，不允许其他人篡权管理，这样就可以更好的对资源进行管控，不至于被人随意拿去使用。单例模式也是所有程序员必须掌握的一种设计模式，在面试中也是必问，我之前在面试时就遇到过，问单例模式讲不出来的，直接就pass了。
