
--- 
title:  [踩坑]fastjson踩坑，转换对象多出来属性 
tags: []
categories: [] 

---
fastjson转换对象多出来属性怎么解决？



#### 目录
- - - 


## 1、结论与解决方法

使用fastjson转换对象出现多的属性，可能是含有is开头的方法导致。可以改用其他json工具类，或者去掉isxx()中的“is”。 目前仅发现alibaba的json中会出现这样的问题。

## 2、示例

需要转换成JsonStr的对象的具体属性如下： <img src="https://img-blog.csdnimg.cn/b67830e6d6704eaab0391702ab16891b.png" alt="在这里插入图片描述"> 在实践中使用JSON.toJSONString();**方法进行转换后，会多出 failed属性与 succ属性**。 对方法进行debug，阅读源码后发现，dubug发现出现的地方是 **JSONSerializer**。

<img src="https://img-blog.csdnimg.cn/c4cd9df599ca45f7b2d64bc4522e23d6.png" alt="在这里插入图片描述"> 最后在方法发现有两个 is 开头的方法，isFailed()与isSucc()。 <img src="https://img-blog.csdnimg.cn/a08e3ae1c4bb4dab9b46b6d0db8e87b3.png" alt="在这里插入图片描述"> 修改方法名，或者改用其他JSON工具类，破案。

**顺带一提，使用hutool的JSONUtil不会出现这种问题，难怪阿里规范要强调不用is开头，就你们是吧！！！**

## 3、Hutool工具类JSON示例

hutool的json工具名为 JSONUtil,官网示例如下

```
SortedMap&lt;Object, Object&gt; sortedMap = new TreeMap&lt;Object, Object&gt;() {<!-- -->
    private static final long serialVersionUID = 1L;
    {<!-- -->
    put("attributes", "a");
    put("b", "b");
    put("c", "c");
}};

JSONUtil.toJsonStr(sortedMap);

```
