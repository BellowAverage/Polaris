
--- 
title:  JAVA异常 
tags: []
categories: [] 

---


#### 目录
- <ul><li><ul><li>- <ul><li>- - - 


#### 什么是异常

```
导致程序正常流程被中断的事件，就叫异常

```

##### 异常(Throwable)的种类

推荐下面的文章  分为(子类)：错误（Error）、异常（Exception）
- **错误**：系统级别的异常，不用捕捉- **异常**：分为运行时异常(RuntimeException)和非运行时异常， 也称之为不检查异常（Unchecked Exception）和检查异常（Checked Exception）。
检查异常：必须要处理的异常，不处理不能通过编译 非检查异常：不用捕捉，也不会有编码错误

<s>这里有点迷：有些资料里Error也是非检查异常，按定义来说也确实是</s>

##### 异常的处理手段

```
try||(try with resource) catch finally throws /throw

try||try(实现了AutoCloseable接口的资源){
    可处理异常||可能出现异常的代码块
    
}catch(TypeException e){
    
}finally{
    //不管是否出现异常，都会执行finally{}里的内容都会被执行
}

```

##### 当 try{ }、catch{} 和finally{}里出现return的情况

**1、当 try{ }、catch{} 和finally{}里出现return的情况** 推荐看这个 

```
public class Test {
    public static int num=1;
    public static void main(String[] args) throws ParseException {
        int result;
        result = num();
        System.out.println(result);//输出结果为1003
        System.out.println(num);//输出结果为1001
    }
    private static int num() {
        try{
            int b=4/0;
            return num = num+1000;
        }catch(Exception e){
            return num = num+1000;
        }finally {
            return num+2;
        }        
    }    
}

```

**2、throws/throw** throws与throw这两个关键字接近，不过意义不一样，有如下区别： : throws 出现在方法声明上，而throw通常都出现在方法体内。 :throws 表示出现异常的一种可能性，并不一定会发生这些异常；throw则是抛出了异常，执行throw则一定抛出了某个异常对象。

**3、自定义异常** 只要继承Exception类就可以了 xxxException extends Exception。

>  
 注：Spring对运行时异常RuntimeException才会进行事务回滚 


#### 工作中的异常处理 [update]

##### 全局异常处理

可以定义一个全局异常处理器 GlobalExceptionHandler

>  
 前置了解,到了这一步需要会框架。注解相当于一个特殊的注释标识，由动态代理类实现（是有具体实现的！） 

- @ExceptionHandler 用于方法上声明异常处理类型
```
@ExceptionHandler(ParamValidException .class)
public String ParamValidException Handler(ParamValidException ex){
	return ex.getMessage();
}
// 一般不会直接返回 ex.getMessage()，可以附加 HttpStatus 以及 日志记录操作等

```
- @ResponseBody 表示该方法的返回的结果直接写入 HTTP 响应正文中，一般在异步获取数据时使用- @ControllerAdvice 加强版@Controller- @RestControllerAdvice 全部异常处理返回json，那么可以使用 @RestControllerAdvice 代替 @ControllerAdvice ，这样在方法上就可以不需要添加 @ResponseBody
使用注解 @RestControllerAdvice 对类进行标识，使用@ExceptionHandler(XXXException.class)对各类自定义异常做异常处理 eg:

```
@RestControllerAdvice
@Slf4j
public class GlobalExceptionHandler{

	@ExceptionHandler(ParamValidException.class)
    public Result ParamValidExceptionHandler(ParamValidException ex) {
        return new Result(HttpStatus.xxx, ex.getMessage());
    }
}


```
