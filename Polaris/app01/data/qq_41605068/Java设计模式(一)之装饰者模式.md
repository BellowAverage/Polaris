
--- 
title:  Java设计模式(一)之装饰者模式 
tags: []
categories: [] 

---
## 一、概述

        装饰者模式是一种常见的设计模式，在java I/O设计中使用了大量的装饰者设计模式。装饰者设计模式是一种进行方法增强的思路，可以保证在原方法功能不变的基础上，对原方法进行功能上的增强。

## 二、原理

<img alt="" class="has" height="228" src="https://img-blog.csdnimg.cn/20190813001902576.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="551">

分析：（在装饰者模式中，明白三个对象：接口规范、待增强对象和已增强对象）

接口规范：也就是原有的基类，定义了待增强的方法，无论待增强类还是已增强类都实现了该接口；

待增强对象：待增强对象其实就是我们的装饰对象，对该对象的功能进行包装，达到增强的目的；

已增强对象：已增强对象就是包装以后的对象，由于已增强对象和待增强的对象实现了同一个接口，利用多态的原理，可以直接利用已增强对象替代待增强对象。

## 三、实现

实现场景：

 接口规范（定义一个People接口，有一个myWeek方法）

 待增强类（定义一个未婚类UnMarry，也就是单身狗类）

 已增强类（定义一个已婚类Marry，不再是单身狗）

### 3.1定义接口规范

###  

```
public interface People {
    void myWeek();//我的周末
}
```

### 3.2待增强类（UnMarry单身类）

```
public class UnMarry implements People { //单身类 = 待增强类
    @Override
    public void myWeek() {
        System.out.println("打游戏啦！！！");
    }
}
```

### 3.3已增强类（Marry已婚类）

####     3.3.1有一个属性：待增强类对象

####     3.3.2有一个有参构造，参数为待增强类类型

####     3.3.3实现对对应方法的增强功能

```
public class Marry implements People {//已婚类 = 已增强类
    private UnMarry unMarry;

    public Marry(UnMarry unMarry) {
        this.unMarry = unMarry;
    }

    @Override
    public void myWeek() {
        System.out.println("女票不让我打游戏 ^..^");
        unMarry.myWeek();
        System.out.println("最后还是打游戏 ^&lt;&gt;^");
    }
}
```

### 3.4测试

```
 public static void main(String[] args) {
        UnMarry unMarry = new UnMarry();
        System.out.println("****单身者的周末****");
        unMarry.myWeek();
        Marry marry = new Marry(unMarry);
        System.out.println("****已婚者的周末****");
        marry.myWeek();
    }
```

### 3.5结果

<img alt="" class="has" height="161" src="https://img-blog.csdnimg.cn/20190813005503853.png" width="500">

## 四、总结

**IO****中的使用到了一个设计模式：装饰设计模式。**

装饰设计模式解决：对一组类进行功能的增强。

包装：写一个类(包装类)对被包装对象进行包装；

 * 1、包装类和被包装对象要实现同样的接口；

 * 2、包装类要持有一个被包装对象；

 * 3、包装类在实现接口时，大部分方法是靠调用被包装对象来实现的，对于需要修改的方法我们自己实现；
