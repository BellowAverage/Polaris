
--- 
title:  spring bean的生命周期 
tags: []
categories: [] 

---
### bean的生命周期

Spring上下文中的Bean生命周期也类似，如下： （1）实例化Bean： 对于BeanFactory容器，当客户向容器请求一个尚未初始化的bean时，或初始化bean的时候需要注入另一个尚未初始化的依赖时，容器就会调用createBean进行实例化。对于ApplicationContext容器，当容器启动结束后，通过获取BeanDefinition对象中的信息，实例化所有的bean。(当向BeanFactory容器请求一个尚未初始化的bean时，调用createBean进行实例化)

（2）设置对象属性（依赖注入）： 实例化后的对象被封装在BeanWrapper对象中，紧接着，Spring根据BeanDefinition中的信息 以及 通过BeanWrapper提供的设置属性的接口完成依赖注入。（完成依赖注入）

（3）处理Aware接口： Spring会检测该对象是否实现了xxxAware接口，并将相关的xxxAware实例注入给Bean： ①如果这个Bean已经实现了BeanNameAware接口，会调用它实现的setBeanName(String beanId)方法，此处传递的就是Spring配置文件中Bean的id值； ②如果这个Bean已经实现了BeanFactoryAware接口，会调用它实现的setBeanFactory()方法，传递的是Spring工厂自身。 ③如果这个Bean已经实现了ApplicationContextAware接口，会调用setApplicationContext(ApplicationContext)方法，传入Spring上下文； （Spring会检测该对象是否实现了xxxAware接口，并将相关的xxxAware实例注入给Bean）

（4）BeanPostProcessor： 如果想对Bean进行一些自定义的处理，那么可以让Bean实现了BeanPostProcessor接口，那将会调用postProcessBeforeInitialization(Object obj, String s)方法。

（5）InitializingBean 与 init-method： 如果Bean在Spring配置文件中配置了 init-method 属性，则会自动调用其配置的初始化方法。

（6）如果这个Bean实现了BeanPostProcessor接口，将会调用postProcessAfterInitialization(Object obj, String s)方法；由于这个方法是在Bean初始化结束时调用的，所以可以被应用于内存或缓存技术；

以上几个步骤完成后，Bean就已经被正确创建了，之后就可以使用这个Bean了。 （7）DisposableBean： 当Bean不再需要时，会经过清理阶段，如果Bean实现了DisposableBean这个接口，会调用其实现的destroy()方法；

（8）destroy-method： 最后，如果这个Bean的Spring配置中配置了destroy-method属性，会自动调用其配置的销毁方法。

参考 ，整理一下，方便后期的复习： 1.bean的生命周期 通过构造函数（不管是有参还是无参）来实例化bean

2.为bean的属性设置值 和对其他的bean引用（调用set方法）

3.在初始化之前执行的方法 postProcessBeforeInitialization

4.调用bean的初始化的方法（需要进行配置） xml文件中加上init -method

5.在初始化之后执行的方法 postProcessAfterInitialization

6.获取创建bean实例对象

7.执行销毁方法
