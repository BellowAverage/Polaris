
--- 
title:  BeanFactory和FactoryBean的区别 
tags: []
categories: [] 

---
### BeanFactory和FactoryBean的区别

参考 

BeanFactory是个Factory，也就是IOC容器或对象⼯⼚，FactoryBean是个Bean。在Spring中，所有的Bean都是由BeanFactory(也就是IOC容器)来进⾏管理的。但对FactoryBean⽽⾔，这个Bean不是简单的Bean，⽽是⼀个能⽣产或者修饰对象⽣成的⼯⼚Bean,它的实现与设计模式中的⼯⼚模式和修饰器模式类似
