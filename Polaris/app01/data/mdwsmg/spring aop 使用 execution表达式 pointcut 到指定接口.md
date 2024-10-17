
--- 
title:  spring aop 使用 execution表达式 pointcut 到指定接口 
tags: []
categories: [] 

---
对需要处理的方法，使用@Pointcut做切入点，通过其他方法对切入点做处理。

```
    @Pointcut("execution(* pers.crayon.april.demo.forum.controller.ArticleController.details*(..))")
    public void yourExcutionName() {<!-- -->
    }

```

编辑excution表达式定位切入点。 推荐，可以看到详解，**本文做使用摘要，不求甚解**。 https://blog.csdn.net/likun557/article/details/107096539

### 1、execution——表达式摘要说明

切点**使用execution(方法表达式)匹配方法执行**。
- execution格式如下: execution(modifiers-pattern? ret-type-pattern declaring-type-pattern? name-pattern(param-pattern) throws-pattern?)
```
execution(* pers.crayon.april.demo.forum.controller.ArticleController.details*(..))"

```

**在表达式中**

带 ?号的部分是**可选项**，如: modifiers-pattern?，declaring-type-pattern?，hrows-pattern?

|表达式中的可选项|可选项解释
|------
|modifier-pattern|修饰符匹配，如public 表示匹配公有方法
|declaring-type-pattern|类路径匹配
|throws-pattern|异常类型匹配

其余是**必选项**

|表达式中的必选项|必选项解释
|------
|ret-type-pattern|返回值匹配，* 表示任何返回值，全路径的类名等
|name-pattern|方法名匹配，* 代表所有，set*，代表以set开头的所有方法
|param-pattern|参数匹配，指定方法参数(声明的类型)，(…)代表所有参数，(*,String)代表第一个参数为任何值,第二个为String类型，(…,String)代表最后一个参数是String类型

### 2、举例说明

例如开头的表达式

```
"execution(* pers.crayon.april.demo.forum.controller.ArticleController.details*(..))"
↓表达式如下↓
* pers.crayon.april.demo.forum.controller.ArticleController.details*(..)

```

```
↓对公式进行匹配↓
modifiers-pattern? ret-type-pattern declaring-type-pattern? name-pattern(param-pattern) throws-pattern?

```

只用了必选项，其中
- ‘*’ 表示匹配所有类型返回值- ‘pers.crayon.april.demo.forum.controller.ArticleController.details*’ 表示匹配 pers.crayon.april.demo.forum.controller**包下** ArticleController **类中**，details**为方法名开头**的**方法**- ‘(…)’ 表示匹配所有入参
所以，表达式的意思合起来就是——“匹配 pers.crayon.april.demo.forum.controller**包下** ArticleController **类中**，details**为方法名开头**的**且入参与返回值为所有类型的方法**”

>  
 很多地方会按照类型的匹配，再来说一下类型匹配的语法。 


AspectJ类型匹配的通配符：

|通配符|含义
|------
|*|匹配任何数量字符
|…|匹配任何数量字符的重复，如在类型模式中匹配任何数量子包；而在方法参数模式中匹配任何数量参数（0个或者多个参数）
|+|匹配指定类型及其子类型；仅能作为后缀放在类型模式后边
