
--- 
title:  自定义类加载器加载E盘上的.class文件 
tags: []
categories: [] 

---
两年前做项目时，需要加载硬盘上的class文件，而类与类之间有依赖关系，当时自定义类加载器加载类class文件时，经常会出现依赖类的异常ClassNotFoundExecution（idea环境不会出现，而服务器部署项目后会出现），当时的解决方案是通过第三方依赖解决 方式一：引入JarClassLoader 类， 方式二： 自定义类加载器
1. 新建 User
```
package com.example.demo.reflex;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.io.Serializable;

/**
 * @author qinenqi
 * @desc
 * @date 2022-09-06 18:43
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class User implements Serializable {

    private int id;
    private String name;

    private Student student;

    public void test() {
        System.out.println("反射调用 test 方法");
        student = new Student();
        student.test();
    }
}

```

新建 Student

```
package com.example.demo.reflex;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.io.Serializable;

/**
 * @author qinenqi
 * @desc
 * @date 2022-09-06 18:01
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Student implements Serializable {

    private Long id;

    private String name;

    private String sex;
    
    public void test(){
        System.out.println("student 的 test 方法");
    }
}


```

这两个是测试类，没有业务逻辑 2. 新建 MyClassLoader 自定义类加载器

```
package com.example.demo.reflex;

import java.io.FileInputStream;

/**
 * @author qinenqi
 * @desc 自定义类加载器
 *  类加载器几个重要的方法：
 *      loadclass:判断是否已加载，使用双亲委派模型，请求父加载器，都为空，使用findclass
 *      findclass:根据名称或位置加载.class字节码,然后使用defineClass
 *      defineclass：解析定义.class字节流，返回class对象
 * @date 2022-09-06 18:42
 */
public class MyClassLoader extends ClassLoader {

   // 类的位置
    private String classPath;

    public MyClassLoader(String classPath) {
        this.classPath = classPath;
    }

    /**
     * @description: 文件加载的方法，也可以不用一次性加载完成，每次1024字节进行读取
     * @author: qinenqi
     * @date: 2022/9/7 14:05
     * @param: [name: 类的全限定名]
     * @return: byte[]：
     **/
    private byte[] loadByte(String name) throws Exception {
        name = name.replaceAll("\\.", "/");
        FileInputStream fis = new FileInputStream(classPath + "/" + name + ".class");
        int len = fis.available();
        byte[] data = new byte[len];
        fis.read(data);
        fis.close();
        return data;
    }

    /**
     * @description:
     * @author: qinenqi
     * @date: 2022/9/7 14:04
     * @param: [name: 类的全限定名]
     * @return: java.lang.Class&lt;?&gt;
     **/
    @Override
    protected Class&lt;?&gt; findClass(String name) throws ClassNotFoundException {
        try {
            byte[] data = loadByte(name);
            return defineClass(name, data, 0, data.length);
        } catch (Exception e) {
            e.printStackTrace();
            throw new ClassNotFoundException();
        }
    }
}


```
1. 新建 controller (方便进行http测试)
```
package com.example.demo.reflex.controller;

import com.example.demo.reflex.MyClassLoader;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.lang.reflect.Method;

/**
 * @author qinenqi
 * @desc 设计相关的控制器
 * @date 2022-09-06 18:00
 */
@RestController
@RequestMapping("/reflexController")
public class ReflexController {

    /**
     * @description: 通过http请求进行接口的测试
     * @author: qinenqi
     * @date: 2022/9/7 14:09
     * @param: []
     * @return: java.lang.String
     **/
    @GetMapping("/reflex")
    public String reflex() throws Exception{
        // 测试的类class，请提前放入到 E:\classes 目录下
        MyClassLoader classLoader = new MyClassLoader ("E:\\classes");
        Class clazz = classLoader.loadClass("com.example.demo.reflex.User");
        Object obj = clazz.newInstance();
        Method method = clazz.getDeclaredMethod("test", null);
        method.invoke(obj, null);
        System.out.println(clazz.getClassLoader().getClass().getName());
        return "SUCCESS";
    }

}

```
1. 目录结构 <img src="https://img-blog.csdnimg.cn/c15124d3bf624e448aa2024187a10511.png" alt="在这里插入图片描述">1. 硬盘上的位置 <img src="https://img-blog.csdnimg.cn/b3f41df8230e494c90c5d474312ecfb2.png" alt="在这里插入图片描述">1. 测试效果 测试请求：get方式 localhost:9999/reflexController/reflex <img src="https://img-blog.csdnimg.cn/d706c44a9c52486b9af610d45784d09a.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/792d02b3ee9c439b89ba148630e158b4.png" alt="在这里插入图片描述">