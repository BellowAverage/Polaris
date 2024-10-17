
--- 
title:  【C++/Python】Windows用Swig实现C++调用Python（史上最简单详细，80岁看了都会操作） 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h3>#【C++/Python】Swig实现C++调用Python（史上最简单详细，80岁看了都会操作）</h3> 
  
  
  <h4>目录</h4> 
  - <ul><li> 
   </li>- - - - - - - - </ul> 
  
  


#### 目录

## 1. 下载SWIG安装包

官网下载SWIG并解压。官网

<img src="https://img-blog.csdnimg.cn/3f59aca44e124036a623c837d9ff095e.png" alt="在这里插入图片描述">

## 2. 添加环境变量

将SWIG路径 `D:\swigwin-4.1.1` 添加到环境变量中。

<img src="https://img-blog.csdnimg.cn/f25ef6326ba54da4adc2e261eeca5460.png" alt="在这里插入图片描述">

## 3. 测试安装成功

打开`cmd`，输入 `swig --help` 显示如下，证明安装成功。

<img src="https://img-blog.csdnimg.cn/7ffa55f2fcd44a00b6d5aaf7323eb18e.png" alt="在这里插入图片描述">

## 4. 编写C++代码

编写要转换为python的C++代码

>  
 testSwig.h： 


```
class SumTest{<!-- -->
public:
    void printNum();

};


int add_num(int a, int b);


std::string add_string(std::string a, std::string b);

```

>  
 testSwig.cpp： 


```
#include &lt;iostream&gt;
#include "testSwig.h"

int add_num(int a, int b){<!-- -->
    return a + b;
}

std::string add_string(std::string a, std::string b){<!-- -->

    return a + b;
}


void SumTest::printNum(){<!-- -->
    std::cout &lt;&lt; "I love You" &lt;&lt; std::endl;
}

```

## 5. 编写接口文件

为了使用swig，你需要增加一个接口文件。 接口文件一般以`.i` 为文件的后缀。接口文件的作用是，提取c/c++源文件中的接口函数或类型，以及定义一些特殊的功能

>  
 testSwig.i： 


```
%module testSwig

%{<!-- -->
#include &lt;iostream&gt;
#include "testSwig.h"
%}

%include "std_string.i"

int add_num(int a, int b);
std::string add_string(std::string a, std::string b);

class SumTest {<!-- -->
public:
    void printNum();
};

```

可以把接口文件看做三个部分：
1. 第一部分是定义要生成的模块名，就是上面的第一行。1. 第二部分就是包含的头文件信息。1. 第三部分就是指定导出的函数。
由于接口文件的存在，c/c++源文件中一般不需要像导出dll一样需要声明导出函数，只需要保持原样就可以了。

## 6. 执行i文件

根据写好的接口文件，用swig进行编译，打开`cmd`，切换至包含`.i` 文件的路径下：

```
swig -python -c++ testSwig.i

```

编译生成两个文件，一个后缀名为.cxx的c++文件，一个后缀名为.py的python文件，各自从c++和python的角度声明导出信息。

## 7. 使用visual studio生成DLL

1） 创建空项目

<img src="https://img-blog.csdnimg.cn/25bc82fe2a494801a4e92670077e0b68.png" alt="在这里插入图片描述">

2）将 `testSwig.cpp` 、`testSwig.cxx`、`testSwig.i` 放在同一个目录下。

<img src="https://img-blog.csdnimg.cn/fc041a683c684d1ca6a28048864768c5.png" alt="在这里插入图片描述">

3）打开属性，将平台设置为`X64` ，`VC++目录` 中的 `包含目录` 设置为python的`include` 路径。

<img src="https://img-blog.csdnimg.cn/d951e66021b64b83844e5a6da5c3cfeb.png" alt="在这里插入图片描述">

4）选择 `链接器` 将 `附加库目录` 设置为python的 libs路径。

<img src="https://img-blog.csdnimg.cn/1039a7e375404eefb9c8845bd2eab769.png" alt="在这里插入图片描述">

5）将 `常规` 属性中的配置类型，设置为 `动态库.dll`.

<img src="https://img-blog.csdnimg.cn/a312d541cff449b695f4c98b52353387.png" alt="在这里插入图片描述">

6）点击生成，编译出DLL文件。

<img src="https://img-blog.csdnimg.cn/35ff8a241a0a45f8910082ab14f5fa65.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/ddcb038025e44ff494baeea349f40b4d.png" alt="在这里插入图片描述">

7）将dll文件名字修改为下划线开头加模块名，后缀为.pyd，如：_testSwig.pyd

<img src="https://img-blog.csdnimg.cn/9b1b2e48c80f4b01b69b96a009b9bd24.png" alt="在这里插入图片描述">

## 8. 使用pyd文件

将重命名后的 `_testSwig.pyd`文件和 `testSwig.py` 文件放在一起。

<img src="https://img-blog.csdnimg.cn/26beeae2d22f4c84be1529abe78b7db7.png" alt="在这里插入图片描述">

新建一个`test.py` 文件用于测试C++转python是否转换成功：

>  
 test.py： 


```
import testSwig

a = testSwig.add_num(1, 2)
print(a)

b = testSwig.add_string("a", "b")
print(b)

c = testSwig.SumTest()
c.printNum()

```

测试结果： <img src="https://img-blog.csdnimg.cn/70893322c49945eb985a334be3fe40a2.png" alt="在这里插入图片描述">
