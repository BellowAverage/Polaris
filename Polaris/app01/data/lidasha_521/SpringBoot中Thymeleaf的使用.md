
--- 
title:  SpringBoot中Thymeleaf的使用 
tags: []
categories: [] 

---


#### Thymeleaf的使用
- - - - - 


## 1.Thymeleaf简介
- JSP必须依赖Tomcat运行，不能直接运行在浏览器中- HTML可以直接运行在浏览器中，但是不能接收控制器传递的数据- Thymeleaf既保留了HTML的后缀能够直接在浏览器运行，又实现了JSP显示动态数据的功能
## 2.Thymeleaf的使用

>  
 SpringBoot对Thymeleaf提供了良好的支持 

- 2.1.SpringBoot项目添加Thymeleaf依赖
```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-thymeleaf&lt;/artifactId&gt;
&lt;/dependency&gt;

```
<li> 2.2.创建Thymeleaf模板 
  <blockquote> 
   Thymeleaf模板就是HTML页面 
  </blockquote> 
  <ul>- 2.2.1.SpringBoot项目中 resources/templates目录就是用来存放页面模板的
💡 static目录下的资源被定义为静态资源，SpringBoot默认不拦截；如果将HTML页面创建在static目录是可以直接访问的

举个例子：

<img src="https://img-blog.csdnimg.cn/509495dbbbb748c28dfa4033b1105c22.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 💡 templates目录下的文件被定义为动态网页模板，SpringBoot会拦截templates中定义的资源；如果将HTML页面创建在templates目录，必须通过控制器跳转访问

举个例子：

<img src="https://img-blog.csdnimg.cn/1421d18bcc694eada64561d6bffd5596.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

那么如何访问呢？？？
- 2.2.1.通常我们需要创建一个PageController类，用于转发页面请求
<img src="https://img-blog.csdnimg.cn/bee9f4e762824e468a2303684a1b22c8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

```
@Controller
public class PapeController {<!-- -->
    @RequestMapping("/index.html")
    public String test(Model model){<!-- -->
        return "index";
    }
}

```

## 3.Thymeleaf取值
- 3.1.在Thymeleaf模板页面进入th标签的命名空间
```
&lt;!DOCTYPEhtml&gt;
&lt;html lang="en" xmlns:th="http://www.thymeleaf.org"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;Title&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;

&lt;/body&gt;
&lt;/html&gt;

```
<li> 3.2.标签 
  <ul>- 3.2.1. `th:text`
```
// 几乎所有的HTML标签都可以使用th:text属性，将接收到的数据显示在标签的内容中
&lt;label th:text="${name}"&gt;&lt;/label&gt;
&lt;p th:text="${user.userName}"&gt;&lt;/p&gt;
&lt;div th:text="${user.userName}"&gt;&lt;/div&gt;

```
<li> 3.2.2.`th:inline` 内联标签 
    <ul>- HTML内联
```
&lt;p th:inline="text"&gt;年龄：[[${user.age}]]&lt;/p&gt;

```
- CSS内联
```
&lt;style type="text/css" th:inline="css"&gt;
	.test{<!-- -->
			color:[[${<!-- -->color}]]
    }
&lt;/style&gt;

```
- JavaScript内联
```
&lt;script type="text/css" th:text="javascript"&gt;

&lt;/script&gt;

```

3.2.3.`th:each`循环控制

```
&lt;table border="1"&gt;
    &lt;caption&gt;水果集合&lt;/caption&gt;
    &lt;thead&gt;
        &lt;tr&gt;
            &lt;th&gt;水果名称&lt;/th&gt;
        &lt;/tr&gt;
    &lt;/thead&gt;
    &lt;tbody&gt;
        &lt;tr th:each="s:${strs}"&gt;
            &lt;td th:text="${s}" class="test"&gt;&lt;/td&gt;
        &lt;/tr&gt;
    &lt;/tbody&gt;
&lt;/table&gt;

```

## 4.主要代码

`PapeController类`

```
@Controller
public class PapeController{<!-- -->

	@RequestMapping("/index.html")
	public String test(Model model){<!-- -->
		// 字符串
        model.addAttribute("name","张三");
		// CSS内联
        model.addAttribute("color","red");

        // 自定义对象
        User user = new User("李四",25);
        model.addAttribute("user",user);

        //集合
        List&lt;String&gt;strs = new ArrayList&lt;&gt;();
        strs.add("苹果");
        strs.add("香蕉");
        strs.add("西红柿");
        model.addAttribute("strs",strs);

        return "index";
	}
}

```

`User类`

```
@Data
@AllArgsConstructor
public class User{<!-- -->
private String userName;
    private int age;
}

```

`index.html页面`

```
&lt;!DOCTYPEhtml&gt;
&lt;html lang="en" xmlns:th="http://www.thymeleaf.org"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;Title&lt;/title&gt;
	&lt;!-- CSS内联 --&gt;
	&lt;style type="text/css" th:inline="css"&gt;
		.test{<!-- -->
			color:[[${<!-- -->color}]]
       	}
   	&lt;/style&gt;
	&lt;!-- javaScript内联 --&gt;
    &lt;script type="text/css" th:text="javascript"&gt;

	&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
姓名：&lt;label th:text="${name}" class="test"&gt;&lt;/label&gt;
     &lt;hr&gt;
姓名：&lt;label th:text="${user.userName}"&gt;无&lt;/label&gt;
&lt;!-- HTML内联 --&gt;
&lt;p th:inline="text"&gt;年龄：[[${user.age}]]&lt;/p&gt;
    &lt;hr&gt;
&lt;!-- 集合  th:each --&gt;
&lt;table border="1"&gt;
      &lt;caption&gt;水果集合&lt;/caption&gt;
      &lt;thead&gt;
          &lt;tr&gt;
              &lt;th&gt;水果名称&lt;/th&gt;
          &lt;/tr&gt;
      &lt;/thead&gt;
      &lt;tbody&gt;
          &lt;tr th:each="s:${strs}"&gt;
              &lt;td th:text="${s}" class="test"&gt;&lt;/td&gt;
          &lt;/tr&gt;
      &lt;/tbody&gt;
  &lt;/table&gt;
&lt;/body&gt;
&lt;/html&gt;

```

## 5.运行结果展示

<img src="https://img-blog.csdnimg.cn/f184abd759f649d0b5df588aa5709e05.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_18,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">
