
--- 
title:  Springboot写单元测试 
tags: []
categories: [] 

---
## 导入依赖

```
		&lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;
            &lt;exclusions&gt;
                &lt;exclusion&gt;
                    &lt;groupId&gt;org.junit.vintage&lt;/groupId&gt;
                    &lt;artifactId&gt;junit-vintage-engine&lt;/artifactId&gt;
                &lt;/exclusion&gt;
            &lt;/exclusions&gt;
            &lt;scope&gt;test&lt;/scope&gt;
        &lt;/dependency&gt;

```

当然，正常的Springboot也要导入

问题：不要引入

```
&lt;dependency&gt;
    &lt;groupId&gt;org.junit.jupiter&lt;/groupId&gt;
    &lt;artifactId&gt;junit-jupiter-api&lt;/artifactId&gt;
    &lt;version&gt;5.5.0&lt;/version&gt;
    &lt;scope&gt;test&lt;/scope&gt;
&lt;/dependency&gt;

```

这样会出现依赖冲突，删除只保留Test

## 点击生成

<img src="https://img-blog.csdnimg.cn/05ed78cc70224ca195d540a40babd726.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/41637e974c9a439192c5e0897a6efcc7.png" alt="在这里插入图片描述"> 即可生成测试类

## 添加注解

在类上添加@@SpringBootTest注解 如果想打印内容需要再加上@Slf4j注解

在启动类的时候，会调用BeforeEach

然后遍历整个@Test

最后调用@AfterEach方法来收尾

## 点击测试

<img src="https://img-blog.csdnimg.cn/c76353a263ae423dab4b718aba2f239e.png" alt="在这里插入图片描述">
