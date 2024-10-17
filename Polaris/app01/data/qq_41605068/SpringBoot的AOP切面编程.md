
--- 
title:  SpringBoot的AOP切面编程 
tags: []
categories: [] 

---
## 一 引言

>  
 springboot是对原有项目中spring框架和springmvc的进一步封装,因此在springboot中同样支持spring框架中AOP切面编程,不过在springboot中为了快速开发仅仅提供了注解方式的切面编程. 


## 二 使用

### 2.1 引入依赖

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-aop&lt;/artifactId&gt;
&lt;/dependency&gt;

```

### 2.2 相关注解

```

    @Aspect 用来类上,代表这个类是一个切面
    @Before 用在方法上代表这个方法是一个前置通知方法 
    @After 用在方法上代表这个方法是一个后置通知方法
    @Around 用在方法上代表这个方法是一个环绕的方法


```

### 2.3 前置切面

```
@Aspect
@Component
public class MyAspect {
    @Before("execution(* com.baizhi.service.*.*(..))")
    public void before(JoinPoint joinPoint){
        System.out.println("前置通知");
        joinPoint.getTarget();//目标对象
        joinPoint.getSignature();//方法签名
        joinPoint.getArgs();//方法参数
    }
}

```

### 2.4 后置切面

```
@Aspect
@Component
public class MyAspect {
    @After("execution(* com.baizhi.service.*.*(..))")
    public void before(JoinPoint joinPoint){
        System.out.println("后置通知");
        joinPoint.getTarget();//目标对象
        joinPoint.getSignature();//方法签名
        joinPoint.getArgs();//方法参数
    }
}

```

>  
 **&gt;  注意: 前置通知和后置通知都没有返回值,方法参数都为joinpoint** 


### 2.5 环绕切面

```
@Aspect
@Component
public class MyAspect {
    @Around("execution(* com.baizhi.service.*.*(..))")
    public Object before(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
        System.out.println("进入环绕通知");
        proceedingJoinPoint.getTarget();//目标对象
        proceedingJoinPoint.getSignature();//方法签名
        proceedingJoinPoint.getArgs();//方法参数
        Object proceed = proceedingJoinPoint.proceed();//放行执行目标方法
        System.out.println("目标方法执行之后回到环绕通知");
        return proceed;//返回目标方法返回值
    }
}

```

## 三 、自定义注解

### 3.1 @Target

>  
 @Target(ElementType.TYPE)   //接口、类、枚举、注解 @Target(ElementType.FIELD) //字段、枚举的常量 @Target(ElementType.METHOD) //方法 @Target(ElementType.PARAMETER) //方法参数 @Target(ElementType.CONSTRUCTOR)  //构造函数 @Target(ElementType.LOCAL_VARIABLE)//局部变量 @Target(ElementType.ANNOTATION_TYPE)//注解 @Target(ElementType.PACKAGE) ///包    


### 3.2 @Retention

>  
 RetentionPolicy.SOURCE //只在源代码级别保留,编译时就会被忽略 
 RetentionPolicy.CLASS  //编译时被保留,在class文件中存在,但JVM将会忽略 
 RetentionPolicy.RUNTIME  //将被JVM保留,所以他们能在运行时被JVM或其他使用反射机制的代码所读取和使用. 


```
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface CheckUserPwd {

    /**
     * 是否AOP统一处理
     *
     * @return false, true
     */
    boolean value() default true;
}
```

```
@Slf4j
@Aspect
@Component
@AllArgsConstructor
public class CheckUserPwdAspect {

    @SneakyThrows
    @Around("@annotation(checkUserPwd)")
    public Object around(ProceedingJoinPoint point, CheckUserPwd checkUserPwd){
        Map&lt;String, Object&gt; params = getNameAndValue(point);
        Set&lt;String&gt; keySet = params.keySet();
        Iterator&lt;String&gt; it = keySet.iterator();
        SchemaRequest schemaRequest =null;
        while (it.hasNext()){
            Object o = params.get(it.next());
            if(o instanceof SchemaRequest){
                schemaRequest = (SchemaRequest)o;
            }
        }
        System.out.println("===&gt;&gt;"+schemaRequest.toString());

        return point.proceed();
    }
    /**
     * 获取参数Map集合
     * @param joinPoint
     * @return
     */
    Map&lt;String, Object&gt; getNameAndValue(ProceedingJoinPoint joinPoint) {
        Map&lt;String, Object&gt; param = new HashMap&lt;&gt;();
        Object[] paramValues = joinPoint.getArgs();
        String[] paramNames = ((CodeSignature)joinPoint.getSignature()).getParameterNames();
        for (int i = 0; i &lt; paramNames.length; i++) {
            param.put(paramNames[i], paramValues[i]);
        }
        return param;
    }

}
```


