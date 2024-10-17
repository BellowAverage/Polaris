
--- 
title:  使用记事本编写第一个GO程序 
tags: []
categories: [] 

---
### 开发环境：

>  
         go1.18.3 
         记事本 


先来看一下要编写的第一个hello,world Go程序

```
package main 

import "fmt"

func main() {
	/* this is my first Go program*/
	fmt.Println("hello,world")
}
```

>  
  第一行代码 package main定义了域名，你必须在源文件中非注释的第一行指明这个文件属于哪个包，如package main。package main表示一个可独立执行的程序，每个Go应用程序都包含一个名为main的包 
  
 下一行 import "fmt"是搞事Go编译器这个程序需要使用fmt包（的函数，或其他元素），fmt包实现了格式化IO（输入/输出）的函数。 
  
 下一行func main() 是程序开始执行的函数，main函数是每个可执行程序所必须包含的，一般来说都是在被启动后执行的第一个函数（如果有init()函数则会先执行该函数）。 
  
 下一行/*    */ 是注释，在程序执行时将被忽略，单行注释是最常见的注释形式，你可以在任何地方使用以//开头的单行注释，多行注释也叫块注释，均以/*  开头，并以*/结尾，且不可以嵌套使用，多行注释一般用于包的文档描述或注释成块的代码片段 
  
 下一行 fmt.Println("hello,world")可以将字符串输出至控制台，并在最后自动增加换行符\n 
 使用fmt.Print("hello,world\n")可以达到相同的结果 
 Println和Print这两个函数也支持使用变量，如：fmt.Println(a),如果没有特别指定，它们会以默认的打印格式将变量a输出到控制台。 
  
 当标识符（包括常量、变量、类型、函数名、结构字段等等）以一个大写字母开头，如：Group1，那么使用这种形式的标识符的对象就可以被外部包的代码所使用（客户端程序需要先导入这个包），这被称为导出（像面向对象语言中的 public）；标识符如果以小写字母开头，则对包外是不可见的，但是他们在整个包的内部是可见并且可用的（像面向对象语言中的 protected ）。 


### 执行Go程序

>  
 打开hello.go文件的命令行窗口。 
 使用go run hello.go执行go程序 


<img alt="" height="519" src="https://img-blog.csdnimg.cn/ba8fe923a6b049c398b1d6c1bd06258f.png" width="993">

###  将Go程序变成二进制文件

使用 go build 命令来生成二进制文件，二进制文件是可以直接执行的。

<img alt="" height="519" src="https://img-blog.csdnimg.cn/9065d1d5a04e46baa9282fc27963c755.png" width="993">

 

<img alt="" height="88" src="https://img-blog.csdnimg.cn/964598764f624168ac4f8bf890cbba3f.png" width="648">

 




