
--- 
title:  父类对象的属性直接赋值给子类对象(使用copyProperties中的方法copyProperties） 
tags: []
categories: [] 

---
BeanUtils.copyProperties() 是 Apache Commons BeanUtils 包中提供的一个方法，用于将一个 JavaBean 对象的属性值赋值到另一个 JavaBean 对象中。该方法可以简化 JavaBean 之间的属性复制过程，避免手动编写大量的赋值代码。

以下是 BeanUtils.copyProperties() 方法的基本用法：

```
public class SourceBean {<!-- -->
    private String name;
    private int age;
    // getter and setter methods
}

public class TargetBean {<!-- -->
    private String name;
    private int age;
    // getter and setter methods
}

SourceBean source = new SourceBean();
source.setName("Alice");
source.setAge(20);

TargetBean target = new TargetBean();
BeanUtils.copyProperties(source, target);

```

在上面的例子中，首先创建了一个名为 source 的 SourceBean 对象，并为其设置了 name 和 age 属性。然后创建了一个名为 target 的 TargetBean 对象，并使用 BeanUtils.copyProperties() 方法将 source 对象的属性值赋值给 target 对象。这样就可以将一个 JavaBean 对象的属性值赋值到另一个 JavaBean 对象中，从而实现了属性复制的功能。

>  
 通过上述例子可以了解到，是将第一个属性赋值给第二个属性。 通常用于父类对象赋值个子类 


需要注意的是，BeanUtils.copyProperties() 方法会将两个 JavaBean 对象中名称相同、类型相同、可读可写的属性进行映射赋值。如果属性名称不同或者类型不同，则会导致赋值失败。此外，在进行属性复制时，如果源对象可能为 null 值，则需要进行非空判断和处理，以避免出现空指针异常。

除了复制单个属性外，BeanUtils 还提供了其他的一些操作方法，例如复制多个属性、复制集合和数组等。具体可以参考 Apache Commons BeanUtils 的官方文档进行了解。
