
--- 
title:  Spring容器中的Bean是否会被GC呢？ 
tags: []
categories: [] 

---
>  
 Spring容器中的Bean是否会被GC呢？最近好几次被校招实习生问及，对于初学者来说，这应该是一个有意思的问题，鉴于此，笔者顺便写个这个文档。 


###  1.Spring容器中Bean的作用域

当通过Spring容器创建一个Bean实例时，不仅可以完成Bean的实例化，还可以为Bean指定特定的作用域。Spring支持如下5种作用域：
- singleton：单例模式，在整个Spring IoC容器中，使用singleton定义的Bean将只有一个实例；- prototype：原型模式，每次通过容器的getBean方法获取prototype定义的Bean时，都将产生一个新的Bean实例；- request：对于每次HTTP请求，使用request定义的Bean都将产生一个新实例，即每次HTTP请求将会产生不同的Bean实例。只有在Web应用中使用Spring时，该作用域才有效；- session：对于每次HTTP Session，使用session定义的Bean都将产生一个新实例。同样只有在Web应用中使用Spring时，该作用域才有效；- globalsession：每个全局的HTTP Session，使用session定义的Bean都将产生一个新实例。典型情况下，仅在使用portlet context的时候有效。同样只有在Web应用中使用Spring时，该作用域才有效；
上述作用域类型中，比较常用的是singleton和prototype两种作用域。对于singleton作用域的Bean，每次请求该Bean都将获得相同的实例，容器负责跟踪Bean实例的状态，负责维护Bean实例的生命周期行为。如果一个Bean被设置成prototype作用域，程序每次请求该id的Bean，Spring都会新建一个Bean实例，然后返回给程序。在这种情况下，Spring容器仅仅使用new 关键字创建Bean实例，一旦创建成功，容器不在跟踪实例，也不会维护Bean实例的状态。

如果不指定Bean的作用域，Spring默认使用singleton作用域。Java在创建Java实例时，需要进行内存申请；销毁实例时，需要完成垃圾回收，这些工作都会导致系统开销的增加。因此，prototype作用域Bean的创建、销毁代价比较大。而singleton作用域的Bean实例一旦创建成功，可以重复使用。因此，除非必要，否则尽量避免将Bean被设置成prototype作用域。

设置Bean的基本行为，通过scope属性指定，该属性可以接受singleton、prototype、request、session、globlesession5个值，分别代表以上5种作用域。下面的配置片段中，singleton和prototype各有一个：

```
&lt;!-- 默认的作用域：singleton --&gt;
&lt;bean id="p1" class="com.abc.Person" /&gt; 
&lt;!-- 指定的作用域：prototype --&gt;
&lt;bean id="p2" class="com.abc.Person" scope="prototype" /&gt;
```

下面是一个测试类（在Spring框架中执行）：

```
public class BeanTest {
　　public static void main(String args[]) {
　　　　//加载类路径下的beans.xml文件以初始化Spring容器
　　　　ApplicationContext context = new ClassPathXmlApplicationContext();
　　　　//分两次分别取同一个Bean，比较二者是否为同一个对象
　　　　System.out.println(context.getBean("p1") == context.getBean("p1"));
　　　　System.out.println(context.getBean("p2") == context.getBean("p2"));
　　}
}
```

执行结果：

```
true
false
```

从结果可以看出，正如上文所述：对于singleton作用域的Bean，每次请求该id的Bean，都将返回同一个实例，而prototype作用域的Bean，每次请求都将产生全新的实例。

>  
 注意：早期指定Bean的作用域也可通过singleton属性指定，该属性只接受两个属性值：true和false，分别代表singleton和prototype的作用域。使用singleton属性则无法指定其他三个作用域。实际上Spring2.X不推荐使用singleton属性指定Bean的作用域，singleton属性是Spring 1.2.X的使用方式。 




### 2.Spring容器中的Bean是否会被GC呢？

有了上一节内容的铺垫，这个问题实际上已经很清楚了——是否会被GC取决于两点：1.Bean的作用域；2.Spring容器的状态。这里先给出结论：
- singleton 类型的Bean不会被GC，当然，前提是Spring容器处于运行中，如果Spring容器被关闭，那么相关Bean也会被回收；- prototype 类型的Bean会被GC，这种类型的Bean与程序中new关键字生成的对象类似，每次使用都new一个，使用完就回被回收；- new 关键字生成的对象，在程序中会通过new关键字生成对象，这些对象与Spring容器没有直接关系，本质上就是一个普通的Java对象，当这个对象没有引用时即被JVM回收。
 

#### 2.1 单例模式-singleton

在Spring IoC容器中，使用singleton定义的Bean将只有一个实例。实际上，在大多数场景下，我们通过XML文件实例化的Bean的作用域都是singleton。

```
&lt;!-- 默认的作用域：singleton --&gt;
&lt;bean id="person1" class="com.abc.Person" /&gt; 
```

一个Spring bean默认初始化为单例-singleton对象，长期会被spring容器保持（在Spring上下文的map中），容器寄存在servlet的成员变量的servetcontext中，即应用服务器不关闭，引用将一直存在。如开始的成员变量，注入的对象，内存空间一直被引用着，jvm不会回收它们的空间。

那么，为什么要保存在map中保存起来？默认情况下我spring中的bean都是单例，其他地方用都是同一个对象可以复用。所以要做缓存，而不是用完回收，下次再用再创建。



#### 2.2 Spring容器中的Bean存放在何处？

Spring 在初始化时，解析xml文件，将bean信息放在位于beanFactory的beanDefinitionMap中。之后，spring会开始依赖注入，若设置了lazy-init，需要在调用getBean时，实时完成依赖注入过程。DefaultListableBeanFactory 这个类是一个真正可以使用的beanfactory实现， DefaultSingletonBeanRegistry类里的singletonObjects哈希表保存了单例-singleton对象；而prototype类型的对象是不会保存在这个map中的，使用的时候通过new关键字生成。

为了更直观，这里贴一段Spring的代码：

```
public class DefaultSingletonBeanRegistry extends SimpleAliasRegistry implements SingletonBeanRegistry {
 
    /**
     * Internal marker for a null singleton object:
     * used as marker value for concurrent Maps (which don't support null values).
     */
    protected static final Object NULL_OBJECT = new Object();
 
    /** Logger available to subclasses */
    protected final Log logger = LogFactory.getLog(getClass());
 
    /** Cache of singleton objects: bean name --&gt; bean instance */
    // 生成的bean的名称和实例，Spring中会依靠这个beaName进行查找bean
    private final Map&lt;String, Object&gt; 'singletonObjects' = new ConcurrentHashMap&lt;String, Object&gt;(64);
 
    /** Cache of singleton factories: bean name --&gt; ObjectFactory */
    // bean名称和产生的工厂
    private final Map&lt;String, ObjectFactory&lt;?&gt;&gt; singletonFactories = new HashMap&lt;String, ObjectFactory&lt;?&gt;&gt;(16);
 
    /** Cache of early singleton objects: bean name --&gt; bean instance */
    //省略其它代码.......
}
```

可以看到代码中的singletonObjects就是存放单例Bean的容器，就是一个ConcurrentHashMap。暂且不管Spring是怎么把XML配置Bean配置文件还是@bean相关的注解怎么转换成Bean的。反正最终生成的单例Bean是被存放到这个map中了，之后的获取也不管多复杂，多少场景，最后也是从map中获取Bean。



#### 2.3 Spring容器中单例Bean的典型生命周期

相比于普通的Java对象（new关键字生成的对象），Spring中的Bean的生命周期就复杂得多，以下是Bean装载到Spring应用上下文的典型生命周期：
1. Spring对Bean进行实例化；1. Spring将值和Bean的引用注入Bean对应的属性中；1. 如果Bean实现了BeanNameAware接口，Spring将Bean的ID传递给setBeanName()接口方法；1.  如果Bean实现了BeanFactoryAware接口，Spring将调用setBeanFactory()接口方法，将BeanFactory容器实例传入；1. 如果Bean实现了ApplicationContextAware接口，Spring将调用setApplicationContext()接口方法，将应用上下文的引用传入；1.  如果Bean实现了BeanPostProcessor接口，Spring将调用postProcessorBeforeInitialization()接口方法；1.  如果Bean实现了InitializingBean接口，Spring将调用afterPropertiesSet()接口方法。如果Bean使用init-method声明了初始化方法，afterPropertiesSet()接口方法也会被调用；1. 如果Bean实现了BeanPostProcessor接口，Spring将调用postProcessorAfterInitialization接口方法；1. 到此时，Bean的初始化已经完成，可以被应用程序使用，并且Bean将一直驻留在应用上下文中，直到该应用上下文被销毁；1. 如果Bean实现了DisposableBean接口，Spring将调用它的的destory()接口方法。如果Bean使用destory-method声明了销毁方法，destory()接口方法也会被调用；
 

###  3.Spring 的设计思想

IOC容器（Inversion of Control，缩写为IoC）也称为控制反转。这个词大家都很熟悉，但是真正要理解好并不是一件容易的事情。控制反转是代表一种思想，依赖注入是一种实现控制反转的设计模式。控制反转是在以解耦为目标驱动而产生的一种思想，终极目标就是通过IOC容器提供中间商的作用，让对象之间的依赖不靠对象自身控制。



#### 3.1 IOC-控制反转

汽车发动机里面的齿轮大小不一，相互咬合着转动，协同工作。这个非常复杂的一套机械系统，其中任何一个齿轮发生故障都有可能导致发动机抛锚。对比我们软件设计过程遇到的就是深耦合的问题，随着软件复杂度的日益增加，我们迫切需要解决对象之间耦合过高的情形。

<img alt="" src="https://img-blog.csdnimg.cn/20210806230326911.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0ppbl9Ld29r,size_16,color_FFFFFF,t_70">

软件专家Michael Mattson提出了IOC理论，也就是控制反转，它是一种面向对象编程中的一种设计原则，用来减低计算机代码之间的耦合度。其核心思想是：借助“第三方平台”实现具有依赖关系的对象之间的解耦。

引入第三方平台后，对象的主动控制被剥夺，不再自主显式创建（即通过 new 产生对象）所要依赖的对象，而是被动的由第三方平台来控制，当执行到需要其他对象的时候，第三方平台会自动返回所需对象。这样的一种由主动创建到被动分配对象的方式，就叫做控制反转。这个第三方平台就是IOC容器，在它的眼里各个对象之间都是独立的存在，他们之间的依赖关系也只是被写到注册表里面，运行的时候回去检查依赖所需，按需分配，把对象“粘合”到容器里面。

控制反转是一种思想，不止应用在软件设计中，现实生活中其实也是可以用得到的。比如电影院提供卖票服务，每增加一个渠道电影院就得新增人员与其对接，这样如果渠道多的话电影院就忙不过来，而且很容易出错。与其这样每次新增人员对接，电影院索性制定了对接标准，你们谁要来我这里拿电影票，就得按我的标准来。电影院不再需要每次都主动对接渠道，而是把控制权拿过来，自己制定标准，渠道商按照标准来，这也是控制反转的一种实践。



####  3.2 DI-依赖注入

依赖注入就是将实例变量传入到一个对象中去(Dependency injection means giving an object its instance variables)。思想的实现需要具体的步骤，依赖注入就是实现控制反转的方法论。

最后容我举一个粗浅的例子，如果说spring容器的context是舞台，那么bean就是演员，spring的core就是剧本，让bean在舞台上享受了她们的人生（生命周期）。

  
