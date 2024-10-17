
--- 
title:  [SpringBoot Server]SpringBoot tomcat max-connections与threads-max测试 
tags: []
categories: [] 

---
在配置tomcat时，发现有两个配置项max-connections、threads-max均为线程数配置，下面对两个选项进行测试。



#### 目录
- - - <ul><li>


## 1、SpringBoot tomcat max-connections与threads-max测试结论

先说**结论**:当最大请求连接数max-connections小于最大线程数threads-max时，tomcat处理（最大并发）以最大连接数为准。

## 2、测试代码

### 2.1、 controller

在测试中，最大连接数为190，有190个线程休眠等待。

```

@RestController
public class DemoController {<!-- -->
	@PostMapping("/test")
    public String test() {<!-- -->
        try {<!-- -->
            // 线程休眠3000ms,一个请求正常响应为3000+几十ms，程序预热后更快
            Thread.sleep(3000);
        } catch (InterruptedException e) {<!-- -->
            throw new RuntimeException(e);
        }
        return "ok";
    }
}

```

## 3、 application.yaml配置

```
server:
  port: 8080
  #  可以在 tomcat类中看到配置
  tomcat:
   #队列等待数没测出来 TODO 这个不用管
    accept-count: 10
    max-connections: 190
    threads:
      max: 200

```

启动后使用jmeter进行测试，设置并发线程为200 <img src="https://img-blog.csdnimg.cn/327091ea32e641ddbe1ab9a2cdd544a9.png" alt="在这里插入图片描述">

发现有请求进入等待队列，因为设置的最大请求数为190
