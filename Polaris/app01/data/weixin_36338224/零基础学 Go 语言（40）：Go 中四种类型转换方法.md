
--- 
title:  零基础学 Go 语言（40）：Go 中四种类型转换方法 
tags: []
categories: [] 

---
>  
 首发自微信公众号《Go编程时光》，如无授权请勿转载 


查看本系列教程目录，请点击 

Go 语言是静态语言，在编写代码时，就对类型有严格的要求，一旦类型不匹配，就有可能编译失败。

因此在写代码时，就要经常用到类型的转换，这些知识点，对于一个新手来说，可以说是一个不小的门槛，经常要通常搜索引擎来寻找答案。

今天我总结了四种日常开发中最经常遇到的类型转换方法，吃透后就可以自由的进行类型转换。

### 第一种：显式类型转换

使用对应的类型函数进行转换，还是以上面的例子来帮助理解，使用 int16 就可以将 int8 类型的对象转为 int16

```
package main

import "fmt"

func main() {
	var a int8 = 5
	fmt.Printf("%T \n", a)
	// output: int8

	b := int16(a)
	fmt.Printf("%T \n", b)
	// output: int16
}


```

再举个例子，先将 string 类型通过 []byte 类型函数转为 []byte （等同于 []uint8），最后又使用 string 类型函数将 []byte 转回 string

```
package main

import "fmt"

func main() {
	var s1 string = "golang"
	fmt.Printf("%T \n", s1)
	// output: string

	s2 := []byte(s1)
	fmt.Printf("%T \n", s2)
	// output: []uint8

	s3 := string(s2)
	fmt.Printf("%T \n", s3)
	// output: string
}


```

这种方法，同样适用于自己定义的结构体和接口类型，但要注意的是，**仅能用于将结构体类型转换接口类型**，而不能将接口类型转为结构体类型。

这边也举个例子

```
package main

import "fmt"

type People interface {
	Speak()
}

type Student struct {
	name string
}

func (s Student) Speak() {
	fmt.Println("hello, golang")
}

func demo2(s People) {
	s.Speak()
}

func demo1(s1 Student) {
        // 结构体类型转为接口类型
	s2 := People(s1)
	demo2(s2)
}

func main() {
	s1 := Student{name: "wangbm"}
	demo1(s1)
}


```

### 第二种：隐式类型转换

隐式转换，是编译器所为，在日常开发中，开发者并不会感觉到发生了变化。

隐式转换以下面两种情况最为常见，非常简单，我直接以截图加标注说明就行了，不再长篇大论。

#### 函数调用时转换

<img src="https://img-blog.csdnimg.cn/img_convert/2026723330cf3fe19ad458b640e944fb.png" alt="">

#### 函数返回时转换

<img src="https://img-blog.csdnimg.cn/img_convert/0c66f77bb7e4dd17bcdd6fb1255aaf0b.png" alt="">

### 第三种：类型断言

学了上面第二种方法后，我们已经知道下面这段代码，肯定是会编译失败的。

```
package main

import "fmt"

type Student struct {
	name string
}

func (s Student) Speak() {
	fmt.Println("hello, golang")
}

func demo2(s Student) {
	s.Speak()
}

func demo1(s1 interface{}) {
	demo2(s1)
}

func main() {
	s1 := Student{name: "wangbm"}
	demo1(s1)
}


```

答案当然是不能了，原因很简单，因为经过 demo1 函数后，s1 会被隐式转换成 interface{} 类型，而 demo2 函数的参数类型要求为 Student，因此类型不匹配。

<img src="https://img-blog.csdnimg.cn/img_convert/3257466882ad1f901a3704ae7e3262fd.png" alt="">

解决方法也相当的简单，只要使用类型断言一下，就能实现静态类型的转换。

<img src="https://img-blog.csdnimg.cn/img_convert/edffe2fdb751fa517510c3622f7173de.png" alt="">

为了避免有新手，还不了解类型断言（Type Assertion），我这边再简单介绍一下。

类型断言可用于判断一个对象是否是某类型。

这其中包含两种情况：

**第一种情况**：该对象是 T 类型（struct 类型），则断言该对象是 T 类型，就能断言成功。

**第二种情况**：该对象是 I 类型（接口类型），则断言对象是 T 类型，也能断言成功，并且返回一个静态类型为 T 的对象，也相当于类型转换了。

倘若类型断言失败，则会抛出 panic，使用的时候，请千万注意处理。若不想让其抛出 panic，可以使用另一种断言语法。断言不是今天的主题，这里不再展开，更多具体内容，请查看我以前的这篇文章 ，写的非常清楚。

```
s, ok := x.(T)


```

另外，有一点需要提醒的是，类型断言并不能用于两个通用类型的相互转换，只能用于将静态类型为 interface{} 类型的对象，转为具体的类型。

### 第四种：重新构造对象

在之前的教程中（），我使用图解，详细的解释了 Go 语言中的静态类型与动态类型。

其中有一个非常重要的知识点，就是如下这种定义变量的方法

```
package main

import "fmt"

func main() {
    age := (int)(25)
    // 等价于 age := 25
    fmt.Printf("type: %T, data: %v ", age, age)
    // output: type: int, data: 25
}


```

思路变通一下，这个知识点，也可以应用于类型的转换。

```
package main

import "fmt"

func main() {
	var a int8 = 5
	fmt.Printf("%T \n", a)
	// output: int8

	b := (int16)(a)
	fmt.Printf("%T \n", b)
	// output: int16
}



```

以上，就是我总结的四种类型转换方法，如果你有更多的原生类型转换方法，欢迎后台留言告诉我。
