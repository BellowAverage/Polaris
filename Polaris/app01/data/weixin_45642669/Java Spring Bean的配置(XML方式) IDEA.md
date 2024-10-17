
--- 
title:  Java Spring Bean的配置(XML方式) IDEA 
tags: []
categories: [] 

---
今天配置的吐血，三个小时搞定了bean……

## idea安装spring
- idea2021是没有Spring的！！！- 需要安装maven。- 在项目名右键–添加框架支持–Spring4。
## 新建一个类

新建一个类
- 需要实现无参构造器- 需要实现get和set方法- toString也要写，但是非必须
```
public class hello {
    public String getS() {
        return s;
    }

    public void setS(String s) {
        this.s = s;
    }

    @Override
    public String toString() {
        return "hellp{" +
                "s='" + s + '\'' +
                '}';
    }

    String s;
}


```

## XML文件
-  有N种方式，非侵入式的就是XML式。其他的都是侵入式（需要注解），新版本的支持XML，旧版本的似乎只支持注解 -  xml文件需要在resource文件夹下才能进入源代码。 
如果不存在会有这个问题： <img src="https://img-blog.csdnimg.cn/a144846e99604701b570f7aa01d882f2.png" alt="在这里插入图片描述"> 如果是非侵入式的话，需要写xml文件，默认是spring.xml。

右键：添加springXml文件，会生成：

```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd"&gt;
       
       
&lt;/beans&gt;

```

是在两个Beans 之间写入bean，不要在beans后面写，不然不会扫到，IDEA会报错。

格式是：

<img src="https://img-blog.csdnimg.cn/7cf925c91a0f418ba8a8d9fb87dab241.png" alt="在这里插入图片描述">

其余的可以去查，这个是最基础的。

## 新增一个参数

```
&lt;property name="s" value="Spring"/&gt;

```

### 初始化bean：

需要用配置文件初始化注册机。

```
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class text02 {
    public static void main(String[] args) {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("spring1.xml");
        hello hello = (hellp) context.getBean("hello");
        System.out.println(hello.toString());
    }
}


```

需要在参数里面写文件名。不然会报错。 <img src="https://img-blog.csdnimg.cn/5d0253973542460e8f3b58eb7de3f0b6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

解决方式：需要配置文件名。 <img src="https://img-blog.csdnimg.cn/83bca18ad1a34b4391cfd114a8fedc60.png" alt="在这里插入图片描述">
- 需要格式转化。 获得的类型是object，所以需要格式转化为需要的类型。 而且需要class类型，和普通的一样。 <img src="https://img-blog.csdnimg.cn/9fe6eac21c2244c3a80daf16036c25b5.png" alt="在这里插入图片描述">- 最后就是结果了：
<img src="https://img-blog.csdnimg.cn/476a470168c34175b7741868a8b450b3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">出现这个就证明：已经成功配置spring 的bean。

附加一个查找方式：

<img src="https://img-blog.csdnimg.cn/594d7ef770f34d6e8d37129402165e20.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/b4488016213a45b88615f35730025fc9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 人不是ide，所以记录一下。
