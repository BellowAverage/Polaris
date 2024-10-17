
--- 
title:  JAVA栈、堆、方法区 
tags: []
categories: [] 

---
## 一、什么是JAVA栈、堆、方法区

      我们java程序的运行首先会先将.java的文件编译成.class文件，然后由JVM虚拟机的类加载器加载各个类的字节码文件到内存中进行执行，JVM虚拟机将这些数据加载到内存时会对内存进行划分为几个区域分别为栈、堆和方法区，那它们各自的作用是什么呢？

### JAVA方法区

        方法区是JVM堆的一个逻辑部分，它主要分为：         类信息池：它主要存储类每个类的信息（包括类的名称、方法信息、字段信息）以及编译器编译后的类的字节码；         静态池：存储被static修饰的静态变量和静态方法，当加载类时会扫描将该类的static属性优先存储在静态池中，而且这个操作是在创建对象之前操作的这也就是为什么静态方法不能包含有非静态变量，同一个进程下多个线程是共享这个静态属性，从jdk8开始静态变量的移到了堆区中。

        字符串常量池：存储字符串常量当我们使用String定义一个字符串时，会先将字符串常量存储到字符串常量池中，然后将该地址返回给到变量;

### JAVA堆

        堆区存储的是所有创建的对象，对象中不存放基本类型和对象引用，只存放对象本身，每个对象都包含一个对应的class信息。它同样也是被同一进程下的所有子线程共享。一旦这些对象没有被栈帧里的变量所使用时,则java里的垃圾收集器会自动清理这些对象信息。

### JAVA栈

        每个方法在运行时都会创建一个栈帧，栈帧里存放的是方法的参数、局部变量和返回值等信息。每个线程有自己独立的栈区，它并不会被其他子线程共享。         栈分为3个部分：基本类型变量区、执行环境上下文、操作指令区(存放操作指令）。

## 二、JAVA实例

        这里我们通过一个简单的实例来模拟一下JVM的内存分配的过程。

Person类：

>  
 <pre>public class Person {
    int age;
    String name;
    double weight;
    double height;
    /**
     * 空构造器
     */
    public Person(){}

    /**
     * 构造器的重载
     * @param name
     * @param age
     * @param height
     * @param weight
     */
    public Person(String name,int age,double height,double weight){
        this.name = name;
        this.age = age;
        this.height = height;
        this.weight = weight;
    }
    public  void addAge(int age){
        this.age +=age;
    }
}
</pre> 


main入口：

>  
 <pre>public static void main(String[] args) {
    Person p = new Person("张三",18,175.5,173);
    System.out.println("名字为："+p.name);
    p.addAge(2);
}</pre> 


代码执行过程：<img alt="" height="326" src="https://img-blog.csdnimg.cn/b59824a33441401eac1113fa19c6e9ba.jpeg" width="658">

这段代码执行的过程主要有9步： 1. main入口函数开始，在栈区给main分配了一个main函数栈帧。

2. 在实例化Person类之前需要先将Person的字节码信息加载到方法区，我们这里没有静态变量，如果有静态变量也会将静态变量先加载到静态变量池中。

3. new一个对象后会在堆区中给这个对象开辟一个对象空间。

4. 创建对象后进行对象的初始化操作，这时我们需要初始化一个name字符串常量，因此需要先将字符串常量"张三"存储到方法区里的字符串常量池中。

5. 这时给堆中的对象属性进行赋值，name赋值的是字符串常量的地址。

6. 创建完对象后，回到main方法里，将这个对象的地址给到了一个的局部变量p中，p存储到main的函数栈帧里。

7. 当我们调用addAge方法时，也需要先在栈区中为它创建一个栈帧。

8. addAge方法有个传参，变量为age，age变量放在addAge的栈帧中。

9. 执行addAge方法里的内容。

## 总结

        这里通过一个简单的例子介绍了java程序在执行时的过程，针对类的加载、对象的创建，属性赋值和执行方法这些操作时JVM对内存的分配情况，这也让我们更好的理解了java的执行过程，在我们现实开发过程中，如果有遇到变量是否有权限访问，以及变量赋值时是否会影响其他对象这些问题时能有一个更好的了解。
