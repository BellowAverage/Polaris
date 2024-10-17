
--- 
title:  Java SE总结 
tags: []
categories: [] 

---
## 一、Java概述

1.1Java产生(1991、1994、1996、1998、2009)

1.2三种技术架构(Java SE、Java EE、Java ME)

1.3配置环境变量(JDK、JRE、JAVA_HOME、path、classpath)

1.4javac、java命令

## 二、Java语法基础

2.1标识符

2.2数据类型(基本数据类型，级别、引用数据类型、自动类型转换和强制类型转换)

2.3运算符号(&amp;、&amp;&amp;、|、||)

2.4^(不需要第三方变量，进行交换)

2.5重载？如何区分？

2.6数组的表现形式

    二分法查找该数是否在该数组中(使用二分法的前提：保证该数组必须是有序数组)

```
public static int search_2(int arr[],int key){
		int low = 0;//开始的下标
		int heigh = arr.length-1;//结束 的下标
		int mid = (low + heigh)&gt;&gt;1;//二分下标
		while(arr[mid] != key){
			if(key &gt; arr[mid])	low = mid + 1;
			else if(key &lt; arr[mid])	heigh = mid - 1;
			if(low &gt; heigh)	return -1;
			mid = (heigh+low)&gt;&gt;1;
		}
		return mid;
	} 
```

2.7Java分的5片内存区

## 三、面向对象

3.1面向对象的理解

3.2局部变量和成员变量的区别(定义位置，范围，存在位置)

3.3构造函数的特点

3.4构造函数和一般函数的区别

3.5构造函数和构造代码块的区别

3.6A a = new A()，创建一个对象在内存中都做了哪些事情？

## 四、封装

4.1this

4.2static

4.3成员变量和静态变量的区别

4.4单例模式(饿汉式和懒汉式的区别？)

## 五、继承

5.1为什么不支持多继承？

5.2final的特点(类、方法、变量)

5.3抽象类abstract的特点

5.4abstract和private、final、static不能共存

5.5接口

      接口中的成员都有固定的修饰符:

      成员变量:public static final

      成员方法:public abstract

5.6抽象类和接口的区别

## 六、多态

6.1多态的好处和弊端

6.2多态在子父类中的成员上的体现的特点

    6.2.1成员变量:在多态中，子父类变量同名

      编译时期：参考的是引用型变量所属的类中是否有调用的成员变量(编译时不产生对象，只检查语法错误)

      运行时期：同样参考的是引用型变量所属的类中是否有调用的成员变量

      总结：无论编译还是运行，参考的都是引用型变量所属的类中的成员变量

      简单的一句话：成员变量-------编译运行，看  = 左边

  6.2.2成员方法:

     编译时期：参考的是引用型变量所属的类中是否有调用的方法

     运行时期：参考的是对象所属的类中是否有调用的方法

      为什么会这样?  因为在子父类中，对于一模一样的方法，有一个特性：覆盖

     简单的一句话：成员函数-------编译看 = 左边，运行看 = 右边

  6.2.3静态方法

     编译时期：参考的是引用型变量所属的类中是否有调用的方法

     运行时期：参考的也是引用型变量所属的类中是否有调用的方法

     为什么会这样？因为静态方法不属于对象，而是属于，该方法所在的类的，调用静态方法的引用是哪个类，那么就调用那个类中的静态方法

    简单的一句话：静态方法--------编译运行，看 = 左边

```
public class Persional {
	public int i = 20;
	private void priFun(){
		System.out.println("Persional private!");
	}
	public void pubFun(){
		System.out.println("Persional public!");
	}
	public static void staFun(){
		System.out.println("Persional static!");
	}
	
	public static void main(String[] args) {
		Persional p = new Stu();
		System.out.println(p.i);     //20
		p.priFun();				     //Persional private!
		p.pubFun();				     //Stu public fun
		p.staFun();				     //Persional static!
		Stu stu = (Stu) p;
		stu.stuFun();	    		 //stu!
	}
}

class Stu extends Persional{
	public int i = 10;
	public void priFun(){
		System.out.println("Stu priFun");
	}
	public void pubFun() {
		System.out.println("Stu public fun");
	}
	public static void staFun(){
		System.out.println("Stu static");
	}
	public void stuFun(){
		System.out.println("stu!");
	}
}
```

6.3复写equals方法

6.4 == 和 equals 的区别

## 七、异常

7.1throw和throws的区别

7.2public、protected、private的default的范围

7.3常见异常

## 八、多线程

8.1进程？线程？

8.2创建线程的第一种方式:继承Thread类，复写run方法（步骤、线程状态）

8.3创建线程的第二种方式:实现Runable接口（步骤）

8.4同步代码块**synchronized**

8.5同步函数使用的是哪个锁？静态同步函数的锁？

8.6写一个延迟加载的单例模式？当出现多线程访问时怎么解决？带来的效率不高问题该怎么解决？

     懒汉式的单例模式，当出现多线程访问时，加同步，解决线程安全问题，这样会导致效率不高，因此可以再通过双重判断的形式来解决。

8.7wait和sleep的区别(可以从执行权和锁上来分析)

## 九、API

9.1String的特点

9.2StringBuffer字符串缓冲区的特点

9.3StringBuffer和StringBuilder的区别

9.4Object类(**equals,toString,getClass,hashCode**)

## 十、集合框架

10.1集合和数组的区别？

10.2Collection接口

      |-----List：有序(元素可以重复，有索引，元素存入的顺序和取出的顺序一致)

             |------ArrayList:底层数据结构是数组，线程不同步，替代了Vector，查询元素 的速度非常快；

             |------LinkedList:底层的数据结构是链表，线程不同步，增删元素的速度快；

             |------Vector:底层的数据结构是数组，线程同步，查询和增删都巨慢；

     【注意：在进行list列表元素迭代的时候，如果想在迭代的过程中，想要对元素进行操作的时候，比如满足条件添加新的元素。**会发生.ConcurrentModificationException并发修改异常。**

**导致的原因:**集合引用和迭代器引用在同时操作元素，通过集合获取到对应的迭代器后，在迭代中，进行集合引用的元素添加，迭代器并不知道，所以会出现此异常

**如何解决？**ListIterator 是List集合所特有的迭代器，是Iterator的一个子接口，这里边有add等方法

】

      |-----Set：无序(元素不可以重复，必须保证元素唯一性，存入顺序和取出的顺序有可能不一致)

             |-----HashSet:底层是哈希表，线程不同步，无序，高效（HashSet保证元素的唯一性，通过元素的HashCode和equals方法完成，当元素的hashcode值相同，则看equals ,如果hashcode值不同，则不判断equals从而提高对象比较速度）

                     |------LinkedHashSet：有序，hashSet的子类

             |-----TreeSet：底层是二叉树，是对集合中的元素进行指定顺序的排序，线程不同步

【

1.取出元素的方式只有一种--迭代器；

**2.哈希表原理？**

3.

**对于ArrayList集合，判断元素是否存在，或者删元素底层依据都是equals方法。**

**对于HashSet集合，判断元素是否存在，或者删除元素，底层依据的是hashCode方法和equals方法。**

】

10.3Map集合

     |-----Hashtable：底层是哈希表数据结构，是线程同步的，不可以存储null键，null值；

     |-----HashMap：底层是哈希表数据结构，线程不同步，可以存储null键，null值

     |-----TreeMap：底层是二叉树结构，对map的键值进行指定顺序的排序

10.4Map集合和Collection集合的区别

10.5取出Map中的元素

    原理：map中是没有迭代器的，collection具备迭代器，只要将map集合转成Set集合，可以使用迭代器了。之所以转成set，是因为map集合具备着键的唯一性，其实set集合就来自于map，set集合底层其实用的就是map的方法。

    方法:

           10.5.1**Set keySet();**

可以将map集合中的键都取出存放到set集合中。对set集合进行迭代。迭代完成，再通过get方法对获取到的键进行值的获取。

       **Set keySet = map.keySet();**

       **Iterator it = keySet.iterator();**

**       while(it.hasNext()) {<!-- -->**

**           Object key = it.next();**

**           Object value = map.get(key);**

**           System.out.println(key+":"+value);**

**      }**

**         10.5.2entrySet()方法  **//取的是键和值的映射关系。

  Entry就是Map接口中的内部接口,entry是访问键值关系的入口，是map的入口，访问的是map中的键值对

           Set entrySet = map.entrySet();

           Iterator it = entrySet.iterator();

           while(it.hasNext()) {<!-- -->

                   **Map.Entry**  me = (Map.Entry)it.next();

                   System.out.println(me.**getKey**()+"::::"+me.**getValue**());

        }

10.6

<img alt="" class="has" height="389" src="https://img-blog.csdnimg.cn/2019081219100565.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="543">

10.7**Collection ****和 Collections的区别**

10.8**集合变数组**

## 十一、Jdk5.0新特性

11.1增强for循环

11.2可变参数(...)

      11.2.1这种和以前接收方式的区别？

11.3静态导入

11.4枚举: 关键字 enum（该特性解决了什么问题？）

11.5自动拆装箱

      11.5.1Integer x = 1; x = x + 1;  经历了什么过程？

      11.5.2 Integer池的大小？

      11.5.3 String池

11.6泛型

      11.6.1 表现形式？

      11.6.2 好处

      11.6.3 泛型技术？

      11.6.7什么时候使用泛型类？

      11.6.8泛型在程序定义中的体现（类、方法、静态方法、接口）？

      11.6.9泛型中的通配符

      11.6.10泛型限定（上限？下限？）

      11.6.11上下限什么时候使用？

      11.6.12泛型使用的细节？

## 十二、常用API

       java.lang.System  //属性和行为都是静态的。

      **java.lang.Runtime  //**类中没有构造方法，不能创建对象,使用单例模式设计的

//但是有非静态方法。说明该类中应该定义好了对象，并可以通过一个static方法获取这个对象。用这个对象来调用非静态方法。这个方法就是 static Runtime getRuntime();

      **java.util.Math   //**用于数学运算的工具类，属性和行为都是静态的。该类是final不允许继承

     ** java.util.Date  //**日期类，月份从0-11

      **java.util. Calendar //日历类**

## **十三、IO流**

     13.1字节流？字符流？

     13.2flush()和close()区别？

     13.3流的操作只有两种：读和写

     13.4

**       字节流：InputStream  OutputStream**

**       字符流：Reader  Writer**

**     13.5FileWriter**写入数据

     13.6**FileReader读文本数据（自定义缓冲区）**

**     13.7IO使用的设计模式----装饰者模式**

**     13.8**

   字节流:InputStream  OutputStream

   字符流:Reader  Writer 

   对象流:ObjectInputStream  ObjectOutputStream 

   转换流:InputStreamReader(字节转字符)  OutputStreamWriter(字符转字节)

   带缓存的流:BufferedOutputStream  BufferedInputStream  BufferedReader  BufferedWriter**   13.9输入输出重定向**

   13.10**对象的序列化：**目的：将一个具体的对象进行持久化，写入到硬盘上。

**静态数据不能被序列化**，因为静态数据不在堆内存中，是存储在静态方法区中。

**如何将非静态的数据不进行序列化？**用**transient** 关键字修饰此变量即可。

**Serializable**

## 十四、网络编程

     14.1逻辑端口

     14.2Java中的ip对象     InetAddress

     14.3Socket？DatagramSocket？DatagramPacket？

     14.4 UDP传输

     14.5UDP的发送过程？UDP的接收过程？

## 十五、反射
