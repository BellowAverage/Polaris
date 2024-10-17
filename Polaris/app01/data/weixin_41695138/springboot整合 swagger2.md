
--- 
title:  springboot整合 swagger2 
tags: []
categories: [] 

---
### springboot整合 swagger2
1. 引入依赖
```
 &lt;!-- swagger  --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;io.springfox&lt;/groupId&gt;
            &lt;artifactId&gt;springfox-swagger2&lt;/artifactId&gt;
            &lt;version&gt;2.9.2&lt;/version&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;io.springfox&lt;/groupId&gt;
            &lt;artifactId&gt;springfox-swagger-ui&lt;/artifactId&gt;
            &lt;version&gt;2.9.2&lt;/version&gt;
        &lt;/dependency&gt;

```
1. 配置文件中添加配置项
```
# swagger2
swagger.enabled = true

```
1. 新建 swagger 配置类
```

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.service.Contact;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;


/**
 *  http://127.0.0.1:5555/scan/swagger-ui.html
 */
@EnableSwagger2
@Configuration
@Profile({<!-- -->"dev", "test"})
public class SwaggerConfig {<!-- -->

    /**
     * 是否开启 swagger
     */
    @Value(value = "${swagger.enabled}")
    Boolean swaggerEnabled;

    @Bean
    public Docket createRestApi() {<!-- -->
        return new Docket(DocumentationType.SWAGGER_2).apiInfo(apiInfo())
                // 是否开启
                .enable(swaggerEnabled).select()
                // 扫描的路径包（controller所在的包）
                .apis(RequestHandlerSelectors.basePackage("com.csjbot.scan.module"))
                // 指定路径处理PathSelectors.any()代表所有的路径
                .paths(PathSelectors.any()).build().pathMapping("/");
    }

    private ApiInfo apiInfo() {<!-- -->
        return new ApiInfoBuilder()
                .title("springboot整合swagger2")
                .description("springboot整合swagger2的详细描述")
                // 作者信息
                .contact(new Contact("qinenqi", "xxx", "xxx"))
                .version("1.0.0")
                .build();
    }
}

```

新建一个测试类

```

import com.csjbot.scan.common.AjaxResult;
import com.csjbot.scan.module.test.entry.Test;
import com.csjbot.scan.module.test.service.TestService;
import com.csjbot.scan.module.websocket.entry.WebsocketThreadTest;
import com.csjbot.scan.util.newutil.ThreadExecutorUtil;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

/**
 *  测试程序
 */
@Api(value = "测试程序_value", tags = "测试程序")
@RestController
@RequestMapping("/testController")
public class TestController {<!-- -->

    @Autowired
    private TestService testService;

    /**
     *  测试基础程序
     */
    @GetMapping("/test")
    public AjaxResult test(){<!-- -->
        System.out.println("测试程序");
//        int number = 1/0;
        return AjaxResult.success("success");
    }

    /**
     *  测试 新增
     */
    @PostMapping("/insert")
    public void insert(){<!-- -->
        Test test = new Test();
        test.setName("测试01");
        testService.insert01(test);
    }

    /**
     *  测试 查询
     */
    @GetMapping("/select")
    public AjaxResult select(){<!-- -->
        List&lt;Test&gt; select = testService.select();
        AjaxResult success = AjaxResult.success(select);
        return success;
    }

    /**
     *  测试开启线程并查询线程池状态
     * @return
     */
    @GetMapping("/getRunState")
    public AjaxResult getRunState(){<!-- -->
        ThreadExecutorUtil instance = ThreadExecutorUtil.getInstance();
        instance.getThreadState();

        WebsocketThreadTest websocketThreadTest = new WebsocketThreadTest();
        instance.execute(websocketThreadTest);

        try {<!-- -->
            Thread.sleep(100);
        } catch (InterruptedException e) {<!-- -->
            e.printStackTrace();
        }
        instance.getThreadState();

        return AjaxResult.success();
    }

    /**
     *  测试 swagger 的 get 方法
     *  @ApiOperation 注解： value:接口的描述    notes：接口的详细描述
     * @param name
     */
    @ApiOperation(value = "测试 swagger 的 get 方法", notes = "这是 测试swagger的get方法 的详细描述")
    @GetMapping("/testSwaggerGet")
    public AjaxResult testSwaggerGet(@RequestParam String name){<!-- -->
        return AjaxResult.success("get 接收的参数为：" + name);
    }

    /**
     *  测试 swagger 的 post 方法
     *   @ApiOperation 注解： value:接口的描述    notes：接口的详细描述
     */
    @ApiOperation(value = "测试 swagger 的 post 方法", notes = "这是 测试swagger的post方法 的详细描述")
    @PostMapping("/testSwaggerPost")
    public AjaxResult testSwaggerPost(@RequestBody Test test){<!-- -->
        return AjaxResult.success("post 接收的参数为：" + test);
    }


}


```

请根据自己的实际情况处理
1. 启动项目，报错 <img src="https://img-blog.csdnimg.cn/36c962927fc74ae59f252554aa49142f.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
```
The method's class, com.google.common.collect.FluentIterable, is available from the following locations:

    jar:file:/D:/tool/maven/apache-maven-3.6.1-src/repository/com/google/guava/guava/18.0/guava-18.0.jar!/com/google/common/collect/FluentIterable.class


```

这是上面截图的一部分，因为guavar依赖的问题，我添加依赖

```
 &lt;!--   不加入此依赖，会报guava异常     --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;com.google.guava&lt;/groupId&gt;
            &lt;artifactId&gt;guava&lt;/artifactId&gt;
            &lt;version&gt;26.0-jre&lt;/version&gt;
        &lt;/dependency&gt;

```
1. 运行项目，访问swagger2的地址：
```
http://127.0.0.1:5555/scan/swagger-ui.html#/

```

<img src="https://img-blog.csdnimg.cn/21f53d6020844e83bd55af3fdc1e3ece.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### swagger2 区分开发环境与生产环境
1. Springboot中多环境配置文件名需要满足的条件是：application-{profile}.properties，其中{profile}相当于环境标志。 <img src="https://img-blog.csdnimg.cn/71f1a0ed86434aa6a109b0991893ae14.png" alt="在这里插入图片描述">1. 在 application.properties 进行配置
```
#spring.profiles.active=prod
spring.profiles.active=dev


```
1. 在 SwaggerConfig 类中添加注解
```
// 表示 dev test这两个环境可用，其余的环境swagger不可用
@Profile({<!-- -->"dev", "test"})

```
1. 切换到 pord 环境下，swagger2不可用 <img src="https://img-blog.csdnimg.cn/8ada5cc92ec547abb2926bb7d6e86081.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">