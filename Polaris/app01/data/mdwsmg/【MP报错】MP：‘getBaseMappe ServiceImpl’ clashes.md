
--- 
title:  【MP报错】MP：‘getBaseMappe ServiceImpl’ clashes 
tags: []
categories: [] 

---- ServiceImp报错
>  
 ‘getBaseMapper()’ in ‘com.baomidou.mybatisplus.extension.service.impl.ServiceImpl’ clashes with ‘getBaseMapper()’ in ‘com.baomidou.mybatisplus.extension.service.IService’; attempting to use incompatible return type 


在MyBatis-plus中，一般引用包为

>  
 com.baomidou.mybatisplus.core.mapper; 


略看源码可知，IService 与其实现类 ServiceImpl 对Mapper的要求都是

```
&lt;M extends BaseMapper&lt;T&gt;, T&gt;
ServiceImpl&lt;M extends BaseMapper&lt;T&gt;, T&gt; implements IService&lt;T&gt;

```

**问题解决**：查看自己定义的xxServiceI中使用的mapper是否是 BaseMapper 的子类，且

>  
 Mapper 泛型引用应该与 IService 保持一致。 

