
--- 
title:  Go 学习笔记 
tags: []
categories: [] 

---
之前一直接触的是 Python, Ruby 之类的解释性语言，至于静态语言和动态语言的优劣，这儿就不多分析了。如果现阶段想要熟练掌握一门静态语言，感觉 Go 应该是不错的选择，如果有 C++ 、Java 的语言基础，相信上手应该也会很快。

## 安装

**GOROOT 指的是go的安装目录，go的编译器、标准库等都存放在这个目录下。**

**GOPATH 指的是项目的开发目录，存在三个目录结构，分别是src、pkg（一般下载的第三方依赖包放在这个目录下的）、bin目录。**我自己一般是把 C:\Project\Go\&lt;project-name&gt; 作为 gopath 的。

正常下载可执行的 exe 安装包安装即可，只不过有时候在 GoLand 选择GOROOT 的 SDK 的时候，会报下面的错：

```
The selected directory is not a valid home for Go SDK
```

这时候，如果是默认安装的话，需要修改 Go path 路径下 C:\Program Files\Go\src\runtime\internal\sys\zversion.go 文件，, 添加一行版本信息（根据自己实际安装的 go 的版本添加）：

```
const TheVersion = `go1.17.8`
```

然后重启 GoLand，再进行选择 SDK 即可。 

参考：

## 基本结构和数据类型

### 关键字和标识符

Go 代码中会使用到的关键字：

||||
|------
|break|default|func|interface
|case|defer|go|map
|chan|else|goto|package
|const|fallthrough|if|range
|continue|for|import|return

Go 代码中会使用到的标识符：
|append|bool|byte|cap|close|complex
|copy|false|float32|float64|imag|int
|int32|int64|iota|len|make|new
|print|println|real|recover|string|true

### 基本结构和要素 

#### 可见性规则

当标识符（包括常量、变量、类型、函数名、结构字段等等）以一个大写字母开头，如：Group1，那么使用这种形式的标识符的对象就可以被外部包的代码所使用（客户端程序需要先导入这个包），这被称为导出（像面向对象语言中的 public）；标识符如果以小写字母开头，则对包外是不可见的，但是他们在整个包的内部是可见并且可用的（像面向对象语言中的 private ）。

#### Hello World

```
package main

import "fmt"

func main() {
	fmt.Println("Hello World")
}
```

#### 注释

注释和 C++ 的一样，可以使用 // 进行单行注释，可以使用 /* ... */ 进行块注释。

#### 类型及转换

使用 var 声明的变量的值会自动初始化为该类型的零值。类型定义了某个变量的值的集合与可对其进行操作的集合。

类型可以是基本类型，如：int、float、bool、string；结构化的（复合的），如：struct、array、slice、map、channel；只描述类型的行为的，如：interface。

在必要以及可行的情况下，一个类型的值可以被转换成另一种类型的值。由于 Go 语言不存在隐式类型转换，因此所有的转换都必须显式说明，就像调用一个函数一样。

```
package main

import "fmt"

func main() {
	a := 5.0
	b := int(a)
	fmt.Println(b)
}

```

#### 一般结构
- 在完成包的 import 之后，开始对常量、变量和类型的定义或声明。- 如果存在 init 函数的话，则对该函数进行定义（这是一个特殊的函数，每个含有该函数的包都会首先执行这个函数）。- 如果当前包是 main 包，则定义 main 函数。- 然后定义其余的函数，首先是类型的方法，接着是按照 main 函数中先后调用的顺序来定义相关函数，多个函数，可以按照字母顺序来进行排序。
### 常量

**常量的值必须是能够在编译时就能够确定的。因为在编译期间自定义函数均属于未知，因此无法用于常量的赋值，但内置函数可以使用。**

#### 常量定义

语法：

```
const identifier [type] = value
```

常量使用关键字 const 定义，用于存储不会改变的数据。存储在常量中的数据类型只可以是布尔型、数字型（整数型、浮点型和复数）和字符串型。

```
const Pi = 3.14159
```

#### 隐式与显式

编译器可以根据变量的值来推断其类型。
-  显式类型定义： `const b string = "abc"` -  隐式类型定义： `const b = "abc"` 
#### 并行赋值

```
package main

import "fmt"

const beef, two = "meet", 2
const (
	Monday, Tuesday, Wednesday = 1, 2, 3
	Thursday, Friday, Saturday = 4, 5, 6
)
const (
	Unknown = 0
	Male = 1
	Female = 2
)

const (
	RED int = iota
	ORANGE
	YELLOW
	GREEN
	BLUE
	INDIGO
	VIOLET
)

func main() {
	fmt.Println(Wednesday)
	fmt.Println(Male)
	fmt.Println(YELLOW)
}

```

### 变量

#### 声明

Go声明变量时将变量的类型放在变量的名称之后，声明形式相比 C 而言更加清晰。

语法：

```
var identifier type
```

当一个变量被声明之后，系统自动赋予它该类型的零值：int 为 0，float 为 0.0，bool 为 false，string 为空字符串，指针为 nil。

```
package main

import "fmt"

var (
	a int
	b bool
	c string
)
func main() {
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
}

```

```
0
false


```

#### 赋值

一般情况下，只有类型相同的变量之间才可以相互赋值。声明与赋值（初始化）语句也可以组合起来。

```
package main

import "fmt"

var (
	a int		= 1
	b bool		= true
	c string	= "hello"
)
func main() {
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
}
```

```
1
true
hello
```

#### 简短赋值

简短赋值是使用变量的首选形式，但是它只能被用在函数体内，而不可以用于全局变量的声明与赋值。使用操作符 `:=` 可以高效地创建一个新的变量，称之为**初始化声明**。

如果在相同的代码块中，我们不可以再次对于相同名称的变量使用初始化声明。

如果声明了一个局部变量却没有在相同的代码块中使用它，同样会得到编译错误。

```
package main

import "fmt"

func main() {
	var a int = 1
	b := 2
	fmt.Println(a)
	fmt.Println(b)
}

```

#### init 函数

```
package main

import (
	"fmt"
	"math"
)

var Pi float64
func init()  {
	Pi = 4 * math.Atan(1)
}
func main() {
	fmt.Println(Pi)
}

```

### 基本类型

#### 布尔类型

布尔型的值只可以是常量 true 或者 false。两个类型相同的值可以使用相等 `==` 或者不等 `!=` 运算符来进行比较并获得一个布尔型的值。

Go 对于值之间的比较有非常严格的限制，只有两个类型相同的值才可以进行比较。像下面这种是会报错的哟。

```
package main

import "fmt"

func main() {
	a := true
	b := "hello"
	if a == b {
		fmt.Println("a equal to b")
	}
}

```

```
# command-line-arguments
.\test.go:8:7: invalid operation: a == b (mismatched types bool and string)

Compilation finished with exit code 2
```

&amp;&amp; 和 || 是具有快捷性质的运算符（大部分语言都是有这个特性的，比如 Ruby，或者 Python 的 and 和 or），当运算符左边表达式的值已经能够决定整个表达式的值的时候（&amp;&amp; 左边的值为 false，|| 左边的值为 true），运算符右边的表达式将不会被执行。利用这个性质，如果你有多个条件判断，应当将计算过程较为复杂的表达式放在运算符的右侧以减少不必要的运算。

#### 数字类型

Go 语言支持整型和浮点型数字，包括基于架构的类型。例如：int、uint 和 uintptr。

与操作系统架构无关的类型都有固定的大小，并在类型的名称中就可以看出来：

整数：
- int8（-128 -&gt; 127）- int16（-32768 -&gt; 32767）- int32（-2,147,483,648 -&gt; 2,147,483,647）- int64（-9,223,372,036,854,775,808 -&gt; 9,223,372,036,854,775,807）
无符号整数：
- uint8（0 -&gt; 255）- uint16（0 -&gt; 65,535）- uint32（0 -&gt; 4,294,967,295）- uint64（0 -&gt; 18,446,744,073,709,551,615）
浮点型（IEEE-754 标准）：
- float32（+- 1e-45 -&gt; +- 3.4 * 1e38）- float64（+- 5 * 1e-324 -&gt; 107 * 1e308）
Go 中不允许不同类型之间的混合使用（除非通过显式转换），但是对于常量的类型限制非常少，因此允许常量之间的混合使用。

```
package main

func main() {
	var a int
	var b int32
	a = 15
	b = b + a    // 编译错误
	b = b + 5    // 因为 5 是常量，所以可以通过编译
}
```

在格式化字符串里，`%t` 来表示你要输出的值为布尔型，`%d` 用于格式化整数（`%x` 和 `%X` 用于格式化 16 进制表示的数字），`%g` 用于格式化浮点型（`%f` 输出浮点数，`%e` 输出科学计数表示法），`%0d` 用于规定输出定长的整数，其中开头的数字 0 是必须的。`%n.mg` 用于表示数字 n 并精确到小数点后 m 位，除了使用 g 之外，还可以使用 e 或者 f，例如：使用格式化字符串`%5.2e` 来输出 3.4 的结果为 `3.40e+00`。

关于更多 Go 格式化输出的内容，可参考：

#### 数字值转换

当进行类似 `a32bitInt = int32(a32Float)` 转换时，小数点后的数字将被丢弃。这种情况一般发生当从取值范围较大的类型转换为取值范围较小的类型时。

#### 字符类型

在 Go 中，字符只是整数的特殊用例。`byte` 类型是 `uint8` 的别名，对于只占用 1 个字节的传统 ASCII 编码的字符来说，完全没有问题。例如：`var ch byte = 'A'`；**字符使用单引号括起来**。格式化说明符 `%c` 用于表示字符；当和字符配合使用时，`%v` 或 `%d` 会输出用于表示该字符的整数；`%U` 输出格式为 U+hhhh 的字符串。

```
var ch byte = 65 或 var ch byte = '\x41'
```

### 字符串

#### 解释字符串

该类字符串使用双引号括起来，其中的相关的转义字符将被替换，这些转义字符包括：
- `\n`：换行符- `\r`：回车符- `\t`：tab 键- `\u` 或 `\U`：Unicode 字符- `\\`：反斜杠自身
#### 非解释字符串

该类字符串使用反引号（其他解释型语言会使用单引号）括起来，例如：

```
`This is a raw string \n` 中的 `\n\` 会被原样输出。
```

```
package main

import "fmt"

func main() {
	fmt.Println("hello\nworld")
	fmt.Println(`hello\nworld`)
}
```

```
hello
world
hello\nworld

```

**`len()` 来获取字符串所占的字节长度，而不是字符串的长度！！！（字符串长度获取另有其方法）**

```
package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	str1 := "asSASA ddd dsjkdsjsこん dk"
	fmt.Println(len(str1))
	fmt.Println(utf8.RuneCountInString(str1))
}
```

```
28
24
```

#### 字符串拼接

+ 号 或者 strings.Join()

### strings

#### 前后缀

```
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.HasPrefix("hello world", "hello"))
	fmt.Println(strings.HasSuffix("hello world", "world"))
}
```

```
true
true
```

#### 包含关系

```
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Contains("hello world", "o w"))
}
```

```
true
```

#### 字符串索引

Indx、LastIndex

```
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Index("hello world", "o"))
	fmt.Println(strings.LastIndex("hello world", "o"))
}
```

```
4
7
```

#### 字符串替换

```
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Replace("hello world", "l", "x", 2))
	fmt.Println(strings.Replace("hello world", "l", "x", -1))
}
```

```
hexxo world
hexxo worxd
```

####  字符串统计

```
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Count("hello world", "l"))
}
```

```
3
```

#### 字符串重复

```
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Repeat("hello ", 3))
}
```

```
hello hello hello
```

####  字符串大小写

```
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.ToLower("Hello World"))
	fmt.Println(strings.ToUpper("Hello World"))
}
```

```
hello world
HELLO WORLD
```

####  字符串修剪

```
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.TrimSpace("  Hello World  "))
	fmt.Println(strings.TrimLeft("  Hello World  ", " "))
	fmt.Println(strings.TrimRight("  Hello World  ", " "))
	fmt.Println(strings.Trim("Hello World", "old"))
}
```

```
Hello World
Hello World  
  Hello World
Hello Wor
```

#### 字符串分割

```
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.Fields("hello world"))
	fmt.Println(strings.Fields("hello   world"))	// 类似于 Ruby 的 split
	fmt.Println(strings.Split("hello world", " "))
	fmt.Println(strings.Split("hello   world", " ")) // 类似于 Python 的 split(" ")
													 // "hello   world".split(" ")
													 // ['hello', '', '', 'world']
}
```

```
[hello world]
[hello world]
[hello world]
[hello   world]
```

#### 字符串拼接

```
package main

import (
	"fmt"
	"strings"
)

func main() {
	str1 := strings.Fields("hello world")
	fmt.Println(strings.Join(str1, "-"))
}
```

```
hello-world
```

#### 字符串读取

```
package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(strings.NewReader("hello world"))
}
```

```
&amp;{hello world 0 -1}
```

### strconv

```
package main

import (
	"fmt"
	"strconv"
)

func main() {
	var orig string = "666"
	var an int
	var newS string

	fmt.Printf("The size of ints is: %d\n", strconv.IntSize)

	an, _ = strconv.Atoi(orig)
	fmt.Printf("The integer is: %d\n", an)
	an = an + 5
	newS = strconv.Itoa(an)
	fmt.Printf("The new string is: %s\n", newS)
}
```

```
The size of ints is: 64
The integer is: 666
The new string is: 671
```

### 时间和日期

```
package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Now()
	fmt.Println(t.YearDay())
	fmt.Println(t.Year())
	fmt.Println(t.Month())
	fmt.Println(t.Day())
	fmt.Println(t.Date())
	fmt.Println(t.Unix())
	fmt.Println(t.Format(time.RFC1123))
	fmt.Println(t.Format("2006-01-02 03:04:05"))
	fmt.Println(t.Format("2006-01-02 15:04:05")) // 24小时制要将3改成15
}
```

```
171
2022
June
20
2022 June 20
1655693632
Mon, 20 Jun 2022 10:53:52 CST
2022-06-20 11:05:39
2023-01-18 15:08:26
```

### 指针

**一个指针变量可以指向任何一个值的内存地址** 它指向那个值的内存地址，在 32 位机器上占用 4 个字节，在 64 位机器上占用 8 个字节，并且与它所指向的值的大小无关。Go 语言中的指针保证了内存安全。

```
package main

import "fmt"

func main() {
	var i int = 5
	var ptr *int
	ptr = &amp;i
	fmt.Println(i, *ptr, ptr)
	*ptr = 6 // 通过 *ptr 可以修改原始对象的值
	fmt.Println(i, *ptr, ptr)
}
```

```
5 5 0xc00000a098
6 6 0xc00000a098
```

## 控制结构

关键字 if 和 else 之后的左大括号必须和 else-if 关键字在同一行。这两条规则都是被编译器强制规定的。

#### if-else

#### if

```
if condition {
    // do something 
}
```

#### if-else

```
if condition {
    // do something 
} else {
    // do something 
}
```

#### if-else if

```
if condition1 {
    // do something 
} else if condition2 {
    // do something else    
}else {
    // catch-all or default
}
```

#### if initialization; condition

这种写法具有固定的格式（在初始化语句后方必须加上分号）。

```
if initialization; condition {
    // do something
}
```

如果变量在 if 结构之前就已经存在，那么在 if 结构中，该变量原来的值会被隐藏（局部变量优先原则）。

```
package main

import (
	"fmt"
)

func main() {
	var i int = 10
	if i := 5; i == 5 {
		fmt.Println("i ==", i)
	} else {
		fmt.Println("i != 5")
	}
	fmt.Println("i ==", i)
}
```

```
i == 5
i == 10
```

### 函数返回值

Go 语言的函数经常使用两个返回值来表示执行是否成功：返回某个值以及 true 表示成功；返回零值（或 nil）和 false 表示失败。当不使用 true 或 false 的时候，也可以使用一个 error 类型的变量来代替作为第二个返回值：成功执行的话，error 的值为 nil，否则就会包含相应的错误信息（Go 语言中的错误类型为 error: `var err error`）。这样一来，就很明显需要用一个 if 语句来测试执行结果；由于其符号的原因，这样的形式又称之为 comma,ok 模式（pattern）。

#### normal

```
package main

import (
	"fmt"
	"strconv"
)

func main() {
	var orig string = "666"
	// var an int
	var newS string
	// var err error

	fmt.Printf("The size of ints is: %d\n", strconv.IntSize)
	// anInt, err = strconv.Atoi(origStr)
	an, err := strconv.Atoi(orig)
	if err != nil {
		fmt.Printf("orig %s is not an integer - exiting with error\n", orig)
		return
	}
	fmt.Printf("The integer is %d\n", an)
	an = an + 5
	newS = strconv.Itoa(an)
	fmt.Printf("The new string is: %s\n", newS)
}
```

```
The size of ints is: 64
The integer is 666
The new string is: 671
```

#### error

```
package main

import (
	"fmt"
	"strconv"
)

func main() {
	var orig string = "ABC"
	// var an int
	var newS string
	// var err error

	fmt.Printf("The size of ints is: %d\n", strconv.IntSize)
	// anInt, err = strconv.Atoi(origStr)
	an, err := strconv.Atoi(orig)
	if err != nil {
		fmt.Printf("orig %s is not an integer - exiting with error\n", orig)
		return
	}
	fmt.Printf("The integer is %d\n", an)
	an = an + 5
	newS = strconv.Itoa(an)
	fmt.Printf("The new string is: %s\n", newS)
}
```

```
The size of ints is: 64
orig ABC is not an integer - exiting with error
```

#### 习惯用法

```
if err := file.Chmod(0664); err !=nil {
    fmt.Println(err)
    return err
}

//------------------------------------
if value, ok := readData(); ok {
…
}
//------------------------------------
func atoi (s string) (n int) {
	//1、如果返回多个值是，在接受时，希望忽略某个返回值，则使用_符号占位忽略。
	//2、如果返回值只有一个（返回值类型列表）可以不写（）
    n, _ = strconv.Atoi(s)
    return
}

```

### switch

#### 语法

```
switch var1 {
    case val1:
        ...
    case val2:
        ...
    default:
        ...
}
```

变量 var1 可以是任何类型，而 val1 和 val2 则可以是同类型的任意值。类型不被局限于常量或整数，但必须是相同的类型；或者最终结果为相同类型的表达式。前花括号 `{<!-- -->` 必须和 switch 关键字在同一行。也可以同时测试多个可能符合条件的值，使用逗号分割它们，例如：`case val1, val2, val3`。

每一个 `case` 分支都是唯一的，从上直下逐一测试，直到匹配为止。一旦成功地匹配到每个分支，在执行完相应代码后就会退出整个 switch 代码块，也就是说您不需要特别使用 `break` 语句来表示结束。程序也不会自动地去执行下一个分支的代码。如果在执行完每个分支的代码后，还希望继续执行后续分支的代码，可以使用 `fallthrough` 关键字来达到目的。

```
package main

import (
	"fmt"
)

func main() {
	var num1 int = 100
	switch num1 {
	case 98, 99:
		fmt.Println("It's equal to 98 or 99")
	case 100:
		fmt.Println("It's equal to 100")
	default:
		fmt.Println("It's not equal to 98, 99 or 100")
	}
}
```

```
It's equal to 100
```

任何支持进行相等判断的类型都可以作为测试表达式的条件，包括 int、string、指针等。

```
package main

import (
	"fmt"
)

func main() {
	var num1 int = 7

	switch {
	case num1 &lt; 0:
		fmt.Println("Number is negative")
	case num1 &gt; 0 &amp;&amp; num1 &lt; 10:
		fmt.Println("Number is between 0 and 10")
	default:
		fmt.Println("Number is 10 or greater")
	}
}

```

```
Number is between 0 and 10
```

这个时候的逻辑有点像 if - else if -else ：

```
package main

import (
	"fmt"
)

func main() {
	var num1 int = 7

	if num1 &lt; 0 {
		fmt.Println("Number is negative")
	} else if num1 &gt; 0 &amp;&amp; num1 &lt; 10 {
		fmt.Println("Number is between 0 and 10")
	} else {
		fmt.Println("Number is 10 or greater")
	}
}
```

```
Number is between 0 and 10
```

#### fallthrough

fallthrough 对应的 case 如果被执行的话，那这个 case 的下个 case 或 default 也会被执行。

```
package main

import (
	"fmt"
)

func main() {
	k := 6
	switch k {
	case 4: fmt.Println("was &lt;= 4"); fallthrough;
	case 5: fmt.Println("was &lt;= 5"); fallthrough;
	case 6: fmt.Println("was &lt;= 6"); fallthrough;
	case 7: fmt.Println("was &lt;= 7"); fallthrough;
	case 8: fmt.Println("was &lt;= 8"); fallthrough;
	default: fmt.Println("default case")
	}
}
```

```
was &lt;= 6
was &lt;= 7
was &lt;= 8
default case
```

### for

如果想要重复执行某些语句，Go 语言中您只有 for 结构可以使用。

#### 计数迭代

永远不要在循环体内修改计数器，这在任何语言中都是非常差的实践！

```
package main

import "fmt"

func main() {
	for i := 0; i &lt; 5; i++ {
		fmt.Printf("This is the %d iteration\n", i)
	}
}

```

```
This is the 0 iteration
This is the 1 iteration
This is the 2 iteration
This is the 3 iteration
This is the 4 iteration
```

```
package main

func main() {
	for i := 1; i &lt;= 5; i++ {
		for j := 1; j &lt;= i; j++ {
			print("G")
		}
		println()
	}
	println()
	str := "G"
	for i := 1; i &lt;= 5; i++ {
		println(str)
		str += "G"
	}
}
```

```
G
GG
GGG
GGGG
GGGGG

G
GG
GGG
GGGG
GGGGG
```

#### 判断迭代

```
package main

import "fmt"

func main() {
	var i int = 5
	for i &gt; 0 {
		i = i - 1
		fmt.Printf("The variable i is now: %d\n", i)
	}
}
```

```
The variable i is now: 4
The variable i is now: 3
The variable i is now: 2
The variable i is now: 1
The variable i is now: 0
```

#### 无限循环

```
package main

func main() {
	for {
		println("hello")
	}
}
```

```
hello
hello
...
```

#### for-range

```
package main

func main() {
	var arr = [5]int{1, 2, 3, 4, 5}
	for pos, char := range arr {
		println(pos, char)
	}
}
```

```
0 1
1 2
2 3
3 4
4 5
```

```
package main

func main() {
	for i, j, s := 0, 5, "a"; i &lt; 3 &amp;&amp; j &lt; 100 &amp;&amp; s != "aaaaa"; i, j,
		s = i+1, j+1, s + "a" {
		println("Value of i, j, s:", i, j, s)
	}
}
```

```
Value of i, j, s: 0 5 a
Value of i, j, s: 1 6 aa
Value of i, j, s: 2 7 aaa
```

### break 和 continue

这俩关键字在几乎所有语言里的意思都是一样的，所以就不多啰嗦了。

break 语句的作用结果是跳过整个代码块，执行后续的代码。

```
package main

import "fmt"

func main() {
	var i int = 5
	for {
		i = i - 1
		fmt.Printf("The variable i is now: %d\n", i)
		if i &lt; 1 {
			break
		}
	}
}
```

```
The variable i is now: 4
The variable i is now: 3
The variable i is now: 2
The variable i is now: 1
The variable i is now: 0
```

关键字 continue 忽略剩余的循环体而直接进入下一次循环的过程，Go 中的关键字 continue 只能被用于 for 循环中。

```
package main

func main() {
	for i := 0; i &lt; 10; i++ {
		if i == 5 {
			continue
		}
		print(i, " ")
	}
}
```

```
0 1 2 3 4 6 7 8 9 
```

### label 和 goto

for、switch 或 select 语句都可以配合标签（label）形式的标识符使用，即某一行第一个以冒号（`:`）结尾的单词。

#### label

常规 continue

```
package main

import "fmt"

func main() {
//LABEL1:
	for i := 1; i &lt;= 3; i++ {
		for j := 1; j &lt;= 3; j++ {
			if j == 2 {
				continue //LABEL1
			}
			fmt.Printf("i is: %d, and j is: %d\n", i, j)
		}
	}
}
```

```
i is: 1, and j is: 1
i is: 1, and j is: 3
i is: 2, and j is: 1
i is: 2, and j is: 3
i is: 3, and j is: 1
i is: 3, and j is: 3
```

 label continue

```
package main

import "fmt"

func main() {
LABEL1:
	for i := 1; i &lt;= 3; i++ {
		for j := 1; j &lt;= 3; j++ {
			if j == 2 {
				continue LABEL1
			}
			fmt.Printf("i is: %d, and j is: %d\n", i, j)
		}
	}
}
```

```
i is: 1, and j is: 1
i is: 2, and j is: 1
i is: 3, and j is: 1
```

如果将 continue 改为 break，则不会只退出内层循环，而是直接退出外层循环了。还可以使用 goto 语句和标签配合使用来模拟循环。

#### goto

**特别注意** 使用标签和 goto 语句是不被鼓励的：它们会很快导致非常糟糕的程序设计，而且总有更加可读的替代方案来实现相同的需求，这也是好多语言根本就不支持 goto 语法的原因之一。（目前我接触的语言里边就 汇编语言 是支持 goto 的）

```
package main

func main() {
	i := 0
	HERE:
		println(i)
		i++
		if i == 5 {
			return
		}
	goto HERE
}
```

```
0
1
2
3
4
```

## 函数

### 参数与返回值

#### 值传递和引用传递

函数接收参数副本之后，在使用变量的过程中可能对副本的值进行更改，但不会影响到原来的变量，如果你希望函数可以直接修改参数的值，而不是对参数的副本进行操作，你需要将参数的地址（变量名前面添加&amp;符号，比如 &amp;variable）传递给函数，这就是按引用传递，此时传递给函数的是一个指针。如果传递给函数的是一个指针，指针的值会被复制，但指针的值所指向的地址上的值不会被复制；我们可以通过这个指针的值来修改这个值所指向的地址上的值。

#### 命名返回值

```
package main

import "fmt"

var num int = 10
var numx2, numx3 int

func main() {
	numx2, numx3 = getX2AndX3(num)
	PrintValues()
	numx2, numx3 = getX2AndX3_2(num)
	PrintValues()
}

func PrintValues() {
	fmt.Printf("num = %d, 2x num = %d, 3x num = %d\n", num, numx2, numx3)
}

func getX2AndX3(input int) (int, int) {
	return 2 * input, 3 * input
}

func getX2AndX3_2(input int) (x2 int, x3 int) {
	x2 = 2 * input
	x3 = 3 * input
	//return x2, x3
	return
}
```

```
num = 10, 2x num = 20, 3x num = 30
num = 10, 2x num = 20, 3x num = 30
```

#### 空白符

空白符用来匹配一些不需要的值，然后丢弃掉（也叫占位符）。

```
package main

import "fmt"

var num int = 10
var numx2, numx3 int

func main() {
	var i1 int
	var f1 float32
	i1, _, f1 = ThreeValues()
	fmt.Printf("The int: %d, the float: %f \n", i1, f1)
}

func ThreeValues()(int, int, float32)  {
	return 5, 6, 7.8
}
```

```
The int: 5, the float: 7.800000
```

```
package main

import "fmt"

func main() {
	var min, max int
	min, max = MinMax(78, 65)
	fmt.Printf("Minmium is: %d, Maximum is: %d\n", min, max)
}

func MinMax(a int, b int) (min int, max int) {
	if a &lt; b {
		min = a
		max = b
	} else { // a = b or a &lt; b
		min = b
		max = a
	}
	// 会按照函数返回值定义好的顺序返回
	return
}
```

```
Minmium is: 65, Maximum is: 78
```

#### 外部变量

传递指针给函数不但可以节省内存，而且赋予了函数直接修改外部变量的能力，所以被修改的变量不再需要使用 `return` 返回。但是，传递一个指针很容易引发一些不确定的事，所以，我们要十分小心那些可以改变外部变量的函数，必要时，添加注释。

```
package main

import "fmt"

func main() {
	var n int = 0
	reply := &amp;n
	Multiply(4, 5, reply)
	fmt.Println("Multiply: ", *reply)
}

func Multiply(a int, b int, reply *int)  {
	*reply = a * b
}
```

```
Multiply:  20
```

### 变长参数

#### 相同类型

如果函数的最后一个参数是采用 `...type` 的形式，那么这个函数就可以处理一个变长的参数，这个长度可以为 0，这样的函数称为变参函数。（有点类似于 Python 函数定义中的 *args， 能够让函数支持任意数量的参数，但是 Go 中变长参数的类型需要保持一致）

```
package main

import "fmt"

func main() {
	Greeting("hello:", "Joe", "Anna", "Eileen")
}
func Greeting(prefix string, who ...string){
	fmt.Println(prefix, who)
	for _, name := range who {
		fmt.Println(prefix, name)
	}
}
```

```
hello: [Joe Anna Eileen]
hello: Joe
hello: Anna
hello: Eileen
```

#### 不同类型

定义结构体，用以存储所有可能的参数：

```
type Options struct {
    par1 type1,
    par2 type2,
    ...
}
```

#### 空接口

如果一个变长参数的类型没有被指定，则可以使用默认的空接口 `interface{}`，这样就可以接受任何类型的参数。该方案不仅可以用于长度未知的参数，还可以用于任何不确定类型的参数。一般而言我们会使用一个 for-range 循环以及 switch 结构对每个参数的类型进行判断：

```
func typecheck(..,..,values … interface{}) {
    for _, value := range values {
        switch v := value.(type) {
            case int: …
            case float: …
            case string: …
            case bool: …
            default: …
        }
    }
}
```

### defer 和 追踪

#### defer

关键字 defer 允许我们推迟到**函数返回之前**（或任意位置执行 **`return` 语句之后**）一刻才执行某个语句或函数（为什么要在返回之后才执行这些语句？因为 `return` 语句同样可以包含一些操作，而不是单纯地返回某个值）。关键字 defer 的用法类似于面向对象编程语言 Java 和 C# 的 **`finally` **语句块，它一般用于释放某些已分配的资源。当然，defer 的执行也有几个需要注意的地方：

1：**defer在defer语句处执行，defer的执行结果是把defer后的函数压入到栈，等待return或者函数panic后，再按先进后出的顺序执行被defer的函数。**

2：**defer的函数的参数是在执行defer时计算的，defer的函数中的变量的值是在函数执行时计算的。**

3：**defer的执行时机应该是return之后，且返回值返回给调用方之前（return xxx 不是一条原子语句，所以defer有机会改变最终的返回值）。**



defer及defer函数的执行顺序分2步：
1. 执行defer，计算函数的入参的值，并传递给函数，但不执行函数，而是将函数压入栈。1. 函数return语句后，或panic后，执行压入栈的函数，函数中变量的值，此时会被计算。
当有多个 defer 行为被注册时，它们会以逆序执行（类似栈，即后进先出）:

```
package main
import "fmt"

func main() {
	Function1()
}

func Function1() {
	fmt.Printf("In Function1 at the top\n")
	defer Function3()
	defer Function2()
	fmt.Printf("In Function1 at the bottom!\n")
}

func Function2() {
	fmt.Printf("Function2: Deferred until the end of the calling function!\n")
}

func Function3() {
	fmt.Printf("Function3: Deferred until the end of the calling function!\n")
}
```

```
In Function1 at the top
In Function1 at the bottom!
Function2: Deferred until the end of the calling function!
Function3: Deferred until the end of the calling function!
```

```
package main

import "fmt"


func test1() (x int) {
	defer fmt.Printf("in defer: x = %d\n", x)
	x = 7
	return 9
}

func test2() (x int) {
	x = 7
	defer fmt.Printf("in defer: x = %d\n", x)
	return 9
}

func test3() (x int) {
	defer func() {
		fmt.Printf("in defer: x = %d\n", x)
	}()

	x = 7
	return 9
}

func test4() (x int) {
	defer func(n int) {
		fmt.Printf("in defer x as parameter: x = %d\n", n)
		fmt.Printf("in defer x after return: x = %d\n", x)
	}(x)

	x = 7
	return 9
}

func main() {
	fmt.Println("test1")
	fmt.Printf("in main: x = %d\n", test1())
	fmt.Println("test2")
	fmt.Printf("in main: x = %d\n", test2())
	fmt.Println("test3")
	fmt.Printf("in main: x = %d\n", test3())
	fmt.Println("test4")
	fmt.Printf("in main: x = %d\n", test4())
}
```

```
test1
in defer: x = 0
in main: x = 9
test2
in defer: x = 7
in main: x = 9
test3
in defer: x = 9
in main: x = 9
test4
in defer x as parameter: x = 0
in defer x after return: x = 9
in main: x = 9
```

#### 追踪

**defer函数的参数是在执行defer时计算的，defer的函数中的变量的值是在函数执行时计算的。**

```
package main

import "fmt"

func trace(s string) string {
	fmt.Println("entering:", s)
	return s
}

func un(s string) {
	fmt.Println("leaving:", s)
}

func a() {
	defer un(trace("a"))  // trace("a")会在 defer 处执行，但 un() 会在函数结束后执行
	fmt.Println("in a")
}

func b() {
	defer un(trace("b"))
	fmt.Println("in b")
	a()
}

func main() {
	b()
}
```

```
entering: b
in b
entering: a
in a
leaving: a
leaving: b
```

```
package main

import (
	"io"
	"log"
)

// 匿名函数可以使用外层变量（包括入参和出参）
func func1(s string) (n int, err error) {
	defer func() {
		log.Printf("func1(%q) = %d, %v", s, n, err)
	}()
	return 7, io.EOF
}

func main() {
	func1("Go")
}
```

```
2022/07/06 17:37:32 func1("Go") = 7, EOF
```

### 内置函数

|名称|说明
|------
|close|用于管道通信
|len、cap|len 用于返回某个类型的长度或数量（字符串、数组、切片、map 和管道）；cap 是容量的意思，用于返回某个类型的最大容量（只能用于切片和 map）
|new、make|new 和 make 均是用于分配内存：new 用于值类型和用户定义的类型，如自定义结构，make 用户内置引用类型（切片、map 和管道）。它们的用法就像是函数，但是将类型作为参数：new(type)、make(type)。new(T) 分配类型 T 的零值并返回其地址，也就是指向类型 T 的指针（详见第 10.1 节）。它也可以被用于基本类型：`v := new(int)`。make(T) 返回类型 T 的初始化之后的值，因此它比 new 进行更多的工作，**new() 是一个函数，不要忘记它的括号**
|copy、append|用于复制和连接切片
|panic、recover|两者均用于错误处理机制
|print、println|底层打印函数，在部署环境中建议使用 fmt 包
|complex、real imag|用于创建和操作复数

### 递归函数

```
package main

import "fmt"

func main() {
	result := 0
	for i := 0; i &lt; 10; i++ {
		result = fibonacci(i)
		fmt.Printf("fibonacci(%d) is: %d\n", i, result)
	}
}

func fibonacci(n int) (res int) {
	if n &lt;= 1 {
		res = 1
	} else {
		res = fibonacci(n-1) + fibonacci(n-2)
	}
	return res
}

```

```
fibonacci(0) is: 1
fibonacci(1) is: 1
fibonacci(2) is: 2
fibonacci(3) is: 3
fibonacci(4) is: 5
fibonacci(5) is: 8
fibonacci(6) is: 13
fibonacci(7) is: 21
fibonacci(8) is: 34
fibonacci(9) is: 55
```

### 函数作为参数

```
package main

import (
	"fmt"
)

func main() {
	callback(1, Add)
}

func Add(a, b int) {
	fmt.Printf("The sum of %d and %d is: %d\n", a, b, a+b)
}

func callback(y int, f func(int, int)) {
	f(y, 2) // this becomes Add(1, 2)
}
```

```
The sum of 1 and 2 is: 3
```

### 闭包

表示参数列表的第一对括号必须紧挨着关键字 `func`，因为匿名函数没有名称。花括号 `{}` 涵盖着函数体，最后的一对括号表示对该匿名函数的调用。匿名函数像所有函数一样可以接受或不接受参数。

匿名函数同样被称之为闭包：它们被允许调用定义在其它环境下的变量。闭包可使得某个函数捕捉到一些外部状态，例如：函数被创建时的状态。另一种表示方式为：一个闭包继承了函数所声明时的作用域。这种状态（作用域内的变量）都被共享到闭包的环境中，因此这些变量可以在闭包中被操作，直到被销毁。闭包经常被用作包装函数：它们会预先定义好一个或多个参数以用于包装（装饰）。

#### defer 语句和匿名函数

关键字 `defer` 经常配合匿名函数使用，它可以用于改变函数的命名返回值。

```
package main

import "fmt"

func f() (ret int) {
	defer func() {
		ret++
	}()
	return 1
}
func main() {
	fmt.Println(f())
}
```

```
2
```

#### 闭包调试

结合 log 和 runtime 模块，能够准确地知道哪个文件中的具体哪个函数正在执行，对于调试是十分有帮助的。

```
package main

import (
	"log"
	"runtime"
)

func main() {
	where := func() {
		_, file, line, _ := runtime.Caller(1)
		log.Printf("%s:%d", file, line)
	}
	where()
	print()
	where()
}

```

```
2022/07/07 18:43:58 E:/Project/go/src/test/test.go:13
2022/07/07 18:43:58 E:/Project/go/src/test/test.go:15
```

#### 计算执行时间

```
package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()
	time.Sleep(5 * time.Second)
	end := time.Now()
	delta := end.Sub(start)
	fmt.Printf("Sleep took this amount of time: %s\n", delta)
}
```

```
Sleep took this amount of time: 5.0028171s
```

#### 内存缓存

提升性能最直接有效的一种方式就是避免重复计算。通过在内存中缓存和重复利用相同计算的结果，称之为内存缓存。

使用递归计算

```
package main

import (
	"fmt"
	"time"
)

const LIM = 40

func main() {
	var result uint64 = 0
	start := time.Now()
	for i := 0; i &lt; LIM; i++ {
		result = fibonacci(i)
		fmt.Printf("fibonacci(%d) is: %d\n", i, result)
	}
	end := time.Now()
	delta := end.Sub(start)
	fmt.Printf("fibonacci took this amount of time: %s\n", delta)
}

func fibonacci(n int) (res uint64) {
	if n &lt;= 1 {
		res = 1
	} else {
		res = fibonacci(n-1) + fibonacci(n-2)
	}
	return res
}

```

```
fibonacci(0) is: 1
fibonacci(1) is: 1
fibonacci(2) is: 2
fibonacci(3) is: 3
fibonacci(4) is: 5
...
fibonacci took this amount of time: 672.8592ms
```

 使用内存缓存

```
package main

import (
	"fmt"
	"time"
)

const LIM = 40
var fibs [LIM]uint64

func main() {
	var result uint64 = 0
	start := time.Now()
	for i := 0; i &lt; LIM; i++ {
		result = fibonacci(i)
		fmt.Printf("fibonacci(%d) is: %d\n", i, result)
	}
	end := time.Now()
	delta := end.Sub(start)
	fmt.Printf("fibonacci took this amount of time: %s\n", delta)
}

func fibonacci(n int) (res uint64) {
	if fibs[n] != 0 { //因为数组零值是0，如果值不为0，说明已经计算过值。
		res = fibs[n]
		return
	}
	if n &lt;=1 {
		res = 1
	} else {
		res = fibonacci(n-1) + fibonacci(n-2)
	}
	fibs[n] = res
	return res
}

```

```
fibonacci(0) is: 1
fibonacci(1) is: 1
fibonacci(2) is: 2
fibonacci(3) is: 3
fibonacci(4) is: 5
...
fibonacci took this amount of time: 0s
```

## 数组与切片

### 数组声明与初始化

#### 数组概念

数组是具有相同 **唯一类型** 的一组已编号且长度固定的数据项序列（这是一种同构的数据结构）；这种类型可以是任意的原始类型例如整形、字符串或者自定义类型。数组长度必须是一个常量表达式，并且必须是一个非负整数。数组长度也是数组类型的一部分，所以[5]int和[10]int是属于不同类型的。

#### 数组声明

```
var arr1 [5]int
```

每个元素是一个整形值，当声明数组时所有的元素都会被自动初始化为默认值 0。arr1 的长度是 5，索引范围从 0 到 `len(arr1)-1`。

对索引项为 i 的数组元素赋值可以这么操作：`arr[i] = value`，所以数组是 **可变的**。只有有效的索引可以被使用，当使用等于或者大于 `len(arr1)` 的索引时：如果编译器可以检测到，会给出索引超限的提示信息（比如 GoLand）；如果检测不到的话编译会通过而运行时会 panic

```
package main

import "fmt"

func main() {
	var arr1 [5]int
	for i := 0; i &lt; len(arr1); i++ {
		arr1[i] = i * 2
	}

	for index := range arr1 {
		fmt.Printf("Array at index %d is %d\n", index, arr1[index])
	}
	fmt.Println()
	for pos, res := range arr1{
		fmt.Printf("Array at index %d is %d\n", pos, res)
	}
}

```

```
Array at index 0 is 0
Array at index 1 is 2
Array at index 2 is 4
Array at index 3 is 6
Array at index 4 is 8

Array at index 0 is 0
Array at index 1 is 2
Array at index 2 is 4
Array at index 3 is 6
Array at index 4 is 8
```

for 循环中的条件非常重要：`i &lt; len(arr1)`，如果写成 `i &lt;= len(arr1)` 的话会产生越界错误。Go 中可以通过 new 来创建数组：

`var arr1 = new([5]int)`。那么这种方式和 `var arr2 [5]int` 的区别是什么呢？arr1 的类型是 `*[5]int`，而 arr2的类型是 `[5]int`。

#### 值传递和址引用

值传递

```
package main

import "fmt"

func main() {
	var arr1 [5]int             // 赋值时属于值传递
	//var arr1 = new([5]int)	// 赋值时属于引用
	arr2 := arr1
	fmt.Printf("the first element of arr2 is %d\n", arr2[0])
	arr2[0] = 1
	fmt.Printf("the first element of arr1 is %d\n", arr1[0])
}

```

```
the first element of arr2 is 0
the first element of arr1 is 0
```

址引用

```
package main

import "fmt"

func main() {
	//var arr1 [5]int       // 赋值时属于值传递
	var arr1 = new([5]int)	// 赋值时属于引用
	arr2 := arr1
	fmt.Printf("the first element of arr2 is %d\n", arr2[0])
	arr2[0] = 1
	fmt.Printf("the first element of arr1 is %d\n", arr1[0])
}
```



```
the first element of arr2 is 0
the first element of arr1 is 1
```

#### 数组常量

```
package main

import "fmt"

func main() {
	//var arr = [5]int{18, 20, 15, 22, 16}
	//var arr = [...]int{5, 6, 7, 8, 22}
	// var arr = []int{5, 6, 7, 8, 22}
	//var arr = [5]string{3: "Chris", 4: "Ron"}
	var arr = []string{3: "Chris", 4: "Ron"}

	for i:=0; i &lt; len(arr); i++ {
		fmt.Printf("Person at %d is %s\n", i, arr[i])
	}
}
```

第一种：

```
var arrAge = [5]int{18, 20, 15, 22, 16}

```

注意 `[5]int` 可以从左边起开始忽略：`[10]int {1, 2, 3}` :这是一个有 10 个元素的数组，除了前三个元素外其他元素都为 0。

第二种：

```
var arrLazy = [...]int{5, 6, 7, 8, 22}

```

第三种变化：`key: value syntax`

```
var arrKeyValue = [5]string{3: "Chris", 4: "Ron"}

```

只有索引 3 和 4 被赋予实际的值，其他元素都被设置为空的字符串，所以输出结果为：

```
Person at 0 is
Person at 1 is
Person at 2 is
Person at 3 is Chris
Person at 4 is Ron

```

在这里数组长度同样可以写成 `...` 或者直接忽略。你可以取任意数组常量的地址来作为指向新实例的指针。

#### 多维数组

```
package main

const (
	WIDTH = 1920
	HIGHT = 1080
)

type pixel int

var screen [WIDTH][HIGHT]pixel

func main() {
	for x := 0; x &lt; WIDTH; x++ {
		for y := 0; y &lt; HIGHT; y++ {
			screen[x][y] = 1
		}
	}
}

```

#### 数组传递

```
package main

import "fmt"

func main() {
	array := [3]float64{7.0, 8.5, 9.1}
	sum := Sum(&amp;array)
	fmt.Println(sum)
}

func Sum(a *[3]float64) (sum float64) {
	for _, val := range a {
		sum += val
	}
	return sum
}

```

```
24.6
```

### 数组切片

#### 切片概念

切片（slice）是对数组一个连续片段的引用（该数组我们称之为相关数组，通常是匿名的），所以切片是一个**引用类型**（因此更类似于 C/C++ 中的数组类型，或者 Python 中的 list 类型），类似于数据库中视图的概念。其实要说切片的话，Python 算是把切片玩到极致的那种了，只不过 Python 的切片是浅拷贝，和 Go 的引用用起来还是有很大区别的。

切片是可索引的，并且可以由 `len()` 函数获取长度。给定项的切片索引可能比相关数组的相同元素的索引小。和数组不同的是，切片的长度可以在运行时修改，最小为 0 最大为相关数组的长度：切片是一个 **长度可变的数组**。

切片提供了计算容量的函数 `cap()` 可以测量切片最长可以达到多少：它等于切片的长度 + 数组除切片之外的长度。如果 s 是一个切片，`cap(s)` 就是从 `s[0]` 到数组末尾的数组长度。切片的长度永远不会超过它的容量，所以对于 切片 s 来说该不等式永远成立：`0 &lt;= len(s) &lt;= cap(s)`。

多个切片如果表示同一个数组的片段，它们可以共享数据；因此一个切片和相关数组的其他切片是共享存储的，相反，不同的数组总是代表不同的存储。数组实际上是切片的构建块。因为切片是引用，所以它们不需要使用额外的内存并且比使用数组更有效率。

**声明切片的格式是： `var identifier []type`（不需要说明长度）。初始化切片格式：`var slice1 []type = arr1[start:end]`。**

`var slice1 []type = arr1[:]` 那么 slice1 就等于完整的 arr1 数组（所以这种表示方式是`arr1[0:len(arr1)]` 的一种缩写）。等价于 `slice1 = &amp;arr1`。`arr1[2:]` 和 `arr1[2:len(arr1)]` 相同，都包含了数组从第二个到最后的所有元素。`arr1[:3]` 和 `arr1[0:3]` 相同，包含了从第一个到第三个元素（不包括第三个）。

#### 切片传递给函数

如果你有一个函数需要对数组做操作，你可能总是需要把参数声明为切片。当你调用该函数时，把数组分片，创建为一个 切片引用并传递给该函数。

```
package main

func main() {
	var arr = [5]int{0, 1, 2, 3, 4}
	print(sum(arr[:]))
}

func sum(a []int) int {
	s := 0
	for i := 0; i &lt; len(a); i++ {
		s += a[i]
	}
	return s
}

```

#### make()创建切片

当相关数组还没有定义时，我们可以使用 make() 函数来创建一个切片，同时创建好相关数组：

```
var slice1 []type = make([]type, len)
```

make 接受 2 个参数：元素的类型以及切片的元素个数。如果你想创建一个 slice1，它不占用整个数组，而只是占用以 len 为个数个项，那么只要：

```
slice1 := make([]type, len, cap)
```

make 的使用方式是：`func make([]T, len, cap)`，其中 cap 是可选参数。所以下面两种方法可以生成相同的切片:

```
make([]int, 50, 100)
new([100]int)[0:50]
```

```
package main

import "fmt"

func main() {
	var slice1 []int = make([]int, 5, 10)
	for i := 0; i &lt; len(slice1); i++ {
		slice1[i] = 5 * i
	}
	for pos, val := range slice1{
		fmt.Printf("Slice at %d is %d\n", pos, val)
	}
	fmt.Printf("\nThe length of slice1 is %d\n", len(slice1))
	fmt.Printf("The capacity of slice1 is %d\n", cap(slice1))
}

```

```
Slice at 0 is 0
Slice at 1 is 5
Slice at 2 is 10
Slice at 3 is 15
Slice at 4 is 20

The length of slice1 is 5
The capacity of slice1 is 10
```

#### new() 和 make()
- new(Type) 为每个新的类型 Type 分配一片内存，初始化为 0 并且返回类型为*Type 的内存地址：这种方法 **返回一个指向类型为 Type，值为 0 的地址的指针**，它适用于值类型如数组和结构体；它相当于 `&amp;Type{}`。- make(T) **返回一个类型为 Type 的初始值**，它只适用于3种内建的引用类型：slice、map 和 channel。
一个切片 s 可以这样扩展到它的大小上限：`s = s[:cap(s)]`，如果再扩大的话就会导致运行时错误：

```
package main

import "fmt"

func main() {
	var slice1 []byte = []byte{'p', 'o', 'e', 'm'}
	slice2 := slice1[:2]
	fmt.Printf("\nThe length of slice1 is %d\n", len(slice1))
	fmt.Printf("The capacity of slice1 is %d\n", cap(slice1))
	fmt.Printf("\nThe length of slice2 is %d\n", len(slice2))
	fmt.Printf("The capacity of slice2 is %d\n", cap(slice2))
	fmt.Println(slice2[:4])
	fmt.Println(slice2[:5]) //panic: runtime error: slice bounds out of range [:5] with capacity 4
}
```

```
The length of slice1 is 4
The capacity of slice1 is 4

The length of slice2 is 2
The capacity of slice2 is 4
[112 111 101 109]
panic: runtime error: slice bounds out of range [:5] with capacity 4
```

#### bytes

```
var buffer bytes.Buffer
for {
    if s, ok := getNextString(); ok { //method getNextString() not shown here
        buffer.WriteString(s)
    } else {
        break
    }
}
fmt.Print(buffer.String(), "\n")
```

这种实现方式比使用 += 要更节省内存和 CPU，尤其是要串联的字符串数目特别多的时候。

#### for-range

```
for ix, value := range slice1 {
    ...
}
```

第一个返回值 dx 是数组或者切片的索引，第二个是在该索引位置的值；他们都是仅在 for 循环内部可见的局部变量。value 只是 slice1 某个索引位置的值的一个拷贝，不能用来修改 slice1 该索引位置的值。

如果你只需要索引，你可以忽略第二个变量：

```
for ix := range slice1 {
    ...
}
```

如果你只需要值，你可以忽略第一个变量：

```
for _, value := range slice1 {
    ...
}
```

#### 切片重组

我们已经知道切片创建的时候通常比相关数组小，例如：

```
slice1 := make([]type, start_length, capacity)
```

其中 `start_length` 作为切片初始长度而 `capacity` 作为相关数组的长度。这么做的好处是我们的切片在达到容量上限后可以扩容（其实是扩展长度，容量并没有修改）。改变切片长度的过程称之为切片重组 **reslicing**，做法如下：`slice1 = slice1[0:end]`，其中 end 是新的末尾索引（即长度）。

将切片扩展 1 位可以这么做：

```
sl = sl[0:len(sl)+1]
```

#### 切片复制

```
package main
import "fmt"

func main() {
	sl_from := []int{1, 2, 3}
	sl_to := make([]int, 10)

	n := copy(sl_to, sl_from)
	fmt.Println(sl_to)
	fmt.Printf("Copied %d elements\n", n) // n == 3
}
```

```
[1 2 3 0 0 0 0 0 0 0]
Copied 3 elements
```

```
func AppendByte(slice []byte, data ...byte) []byte {
    m := len(slice)
    n := m + len(data)
    if n &gt; cap(slice) { // if necessary, reallocate
        // allocate double what's needed, for future growth.
        newSlice := make([]byte, (n+1)*2)
        copy(newSlice, slice)
        slice = newSlice
    }
    slice = slice[0:n] // resize the real length
    copy(slice[m:n], data)  // copy data to slice
    return slice
}

```

`func copy(dst, src []T) int` copy 方法将类型为 T 的切片从源地址 src 拷贝到目标地址 dst，覆盖 dst 的相关元素，并且返回拷贝的元素个数。源地址和目标地址可能会有重叠。拷贝个数是 src 和 dst 的长度最小值。如果 src 是字符串那么元素类型就是 byte。如果你还想继续使用 src，在拷贝后执行 `src = dst`。

#### 切片追加

```
package main
import "fmt"

func main() {
	sl3 := []int{1, 2, 3}  // 如果是 [3]int{1, 2, 3} 或者 [...]int{1, 2, 3} 形式的数组，则不可以往自身追加
	sl3 = append(sl3, 4, 5, 6)
	fmt.Println(sl3)
}
```

```
[1 2 3 4 5 6]
```

`func append(s[]T, x ...T) []T` 其中 append 方法将 0 个或多个具有相同类型 s 的元素追加到切片后面并且返回新的切片；追加的元素必须和原切片的元素同类型。如果 s 的容量不足以存储新增元素，append 会分配新的切片来保证已有切片元素和新增元素的存储。因此，**返回的切片可能已经指向一个不同的相关数组了。**

#### **切片应用**

修改字符串某个字符

```
package main

func main() {
	s := "hello"
	c := []byte(s)
	c[0] = 'c'
	println(string(c))
}
```

```
cello
```

字节数组对比函数

```
func Compare(a, b[]byte) int {
    for i:=0; i &lt; len(a) &amp;&amp; i &lt; len(b); i++ {
        switch {
        case a[i] &gt; b[i]:
            return 1
        case a[i] &lt; b[i]:
            return -1
        }
    }
    // 数组的长度可能不同
    switch {
    case len(a) &lt; len(b):
        return -1
    case len(a) &gt; len(b):
        return 1
    }
    return 0 // 数组相等
}
```

切片和数组排序

```
package main

import (
	"fmt"
	"sort"
)

func main() {
	var arr1 = []int{1, 3, 2, 4, 5}
	if !sort.IntsAreSorted(arr1) {
		println("arr1 are not sorted!")
		sort.Ints(arr1)
	}
	fmt.Println(arr1)
}
```

```
arr1 are not sorted!
[1 2 3 4 5]
```

append 常见操作
1.  将切片 b 的元素追加到切片 a 之后：`a = append(a, b...)` <li> 复制切片 a 的元素到新的切片 b 上： <pre><code class="language-Go">b = make([]T, len(a))
copy(b, a)
</code></pre> </li>1.  删除位于索引 i 的元素：`a = append(a[:i], a[i+1:]...)` 1.  切除切片 a 中从索引 i 至 j 位置的元素：`a = append(a[:i], a[j:]...)` 1.  为切片 a 扩展 j 个元素长度：`a = append(a, make([]T, j)...)` 1.  在索引 i 的位置插入元素 x：`a = append(a[:i], append([]T{x}, a[i:]...)...)` 1.  在索引 i 的位置插入长度为 j 的新切片：`a = append(a[:i], append(make([]T, j), a[i:]...)...)` 1.  在索引 i 的位置插入切片 b 的所有元素：`a = append(a[:i], append(b, a[i:]...)...)` 1.  取出位于切片 a 最末尾的元素 x：`x, a = a[len(a)-1], a[:len(a)-1]` 1.  将元素 x 追加到切片 a：`a = append(a, x)` 
切片和数组排序

切片的底层指向一个数组，该数组的实际体积可能要大于切片所定义的体积。只有在没有任何切片指向的时候，底层的数组内层才会被释放，这种特性有时会导致程序占用多余的内存。

**示例** 函数 `FindDigits` 将一个文件加载到内存，然后搜索其中所有的数字并返回一个切片。

```
var digitRegexp = regexp.MustCompile("[0-9]+")

func FindDigits(filename string) []byte {
    b, _ := ioutil.ReadFile(filename)
    return digitRegexp.Find(b)
}

```

这段代码可以顺利运行，但返回的 `[]byte` 指向的底层是整个文件的数据。只要该返回的切片不被释放，垃圾回收器就不能释放整个文件所占用的内存。换句话说，一点点有用的数据却占用了整个文件的内存。

想要避免这个问题，可以通过拷贝我们需要的部分到一个新的切片中：

```
func FindDigits(filename string) []byte {
   b, _ := ioutil.ReadFile(filename)
   b = digitRegexp.Find(b)
   c := make([]byte, len(b))
   copy(c, b)
   return c
}
```

## Map

### 声明和初始化

#### 概念

map 这种类型在不用语言有不同叫法，静态类语言大多叫它 map，也有叫字典（dict），哈希（Hash）的。

**map 是引用类型**， 内存用 make 方法来分配，可以使用如下声明：

```
var map1 map[keytype]valuetype
```

在声明的时候不需要知道 map 的长度，map 是可以动态增长的。未初始化的 map 的值是 nil。key 可以是任意可以用 == 或者 != 操作符比较的类型，比如 string、int、float。所以数组、切片和结构体不能作为 key，但是指针和接口类型可以。如果要用结构体作为 key 可以提供 `Key()` 和 `Hash()` 方法，这样可以通过结构体的域计算出唯一的数字或者字符串的 key。value 可以是任意类型的。**（数组可以视为一种简单形式的 map，key 是从 0 开始的整数）。**

```
package main

import "fmt"

func main() {
	var mapLit map[string]int
	var mapAssigned map[string]int

	mapLit = map[string]int{"one": 1, "two": 2}
	mapCreated := make(map[string]float32)
	mapAssigned = mapLit

	mapCreated["key1"] = 4.5
	mapCreated["key2"] = 3.14159
	mapAssigned["two"] = 3

	fmt.Printf("Map literal at \"one\" is: %d\n", mapLit["one"])
	fmt.Printf("Map created at \"key2\" is: %f\n", mapCreated["key2"])
	fmt.Printf("Map assigned at \"two\" is: %d\n", mapLit["two"])
	fmt.Printf("Map literal at \"ten\" is: %d\n", mapLit["ten"])
}

```

常用的 `len(map1)` 方法可以获得 map 中的 pair 数目，这个数目是可以伸缩的，因为 map-pairs 在运行时可以动态添加和删除。

**不要使用 new，永远用 make 来构造 map**

#### map容量

和数组不同，map 可以根据新增的 key-value 对动态的伸缩，因此它不存在固定长度或者最大限制。但是你也可以选择标明 map 的初始容量 `capacity`，就像这样：`make(map[keytype]valuetype, cap)`。例如：

```
map1 := make(map[string]float, 100)

```

当 map 增长到容量上限的时候，如果再增加新的 key-value 对，map 的大小会自动加 1。所以出于性能的考虑，对于大的 map 或者会快速扩张的 map，即使只是大概知道容量，也最好先标明。这里有一个 map 的具体例子，即将音阶和对应的音频映射起来：

```
noteFrequency := map[string]float32 {
    "C0": 16.35, "D0": 18.35, "E0": 20.60, "F0": 21.83,
    "G0": 24.50, "A0": 27.50, "B0": 30.87, "A4": 440}
```

#### 切片作为map的value

既然一个 key 只能对应一个 value，而 value 又是一个原始类型，那么如果一个 key 要对应多个值怎么办？例如，当我们要处理unix机器上的所有进程，以父进程（pid 为整形）作为 key，所有的子进程（以所有子进程的 pid 组成的切片）作为 value。通过将 value 定义为 `[]int` 类型或者其他类型的切片，就可以解决这个问题。

```
map1 := make(map[int][]int)
map2 := make(map[int]*[]int)
```

### 键值存在性测试和删除

```
package main

import "fmt"

func main() {
	map1 := map[string]int{"a": 1, "b": 2}
	fmt.Println(map1)
	_, ok := map1["a"]
	if ok {
		fmt.Println("hello")
	}
	val, ok := map1["b"]
	if ok {
		fmt.Printf("the value is %d\n", val)
	}
	delete(map1, "a")
	fmt.Println(map1)
}
```

```
map[a:1 b:2]
hello
the value is 2
map[b:2]
```

### map 的 for 循环

```
for key, value := range map1 {
    ...
}

或者
for _, value := range map1 {
    ...
}

或者
for key := range map1 {
    ...
}
```

**注意： **map 不是按照 key 的顺序排列的，也不是按照 value 的序排列的。和其他语言里的一样，可以认为 map 是无序的。

map 和 slice 有个特点，只声明的话是没法直接使用的（数组会有初始零值，所以它可以直接使用）。

### map 的切片

假设我们想获取一个 map 类型的切片，我们必须使用两次 `make()` 函数，第一次分配切片，第二次分配 切片中每个 map 元素。

```
package main
import "fmt"

func main() {
	// Version A:
	items := make([]map[int]int, 5)
	for i:= range items {
		items[i] = make(map[int]int)
		items[i][1] = 1
	}
	fmt.Printf("Version A: Value of items: %v\n", items)

	// Version B: NOT GOOD!
	items2 := make([]map[int]int, 5)
	for _, item := range items2 {
		item = make(map[int]int) // item is only a copy of the slice element.
		item[1] = 2 // This 'item' will be lost on the next iteration.
	}
	fmt.Printf("Version B: Value of items: %v\n", items2)
}
```

```
Version A: Value of items: [map[1:1] map[1:1] map[1:1] map[1:1] map[1:1]]
Version B: Value of items: [map[] map[] map[] map[] map[]]
```

### map的排序

map本身是无序的，如果你想为 map 排序，需要将 key（或者 value）拷贝到一个切片，再对切片排序。

```
package main
import (
	"fmt"
	"sort"
)

var (
	barVal = map[string]int{"alpha": 34, "bravo": 56, "charlie": 23,
		"delta": 87, "echo": 56, "foxtrot": 12,
		"golf": 34, "hotel": 16, "indio": 87,
		"juliet": 65, "kili": 43, "lima": 98}
)

func main() {
	fmt.Println("unsorted:")
	for k, v := range barVal {
		fmt.Printf("Key: %v, Value: %v \n", k, v)
	}
	keys := make([]string, len(barVal))
	i := 0
	for k, _ := range barVal {
		keys[i] = k
		i++
	}
	sort.Strings(keys)
	fmt.Println()
	fmt.Println("sorted:")
	for _, k := range keys {
		fmt.Printf("Key: %v, Value: %v \n", k, barVal[k])
	}
}
```

```
unsorted:
Key: bravo, Value: 56 
Key: delta, Value: 87 
Key: echo, Value: 56 
Key: golf, Value: 34 
Key: hotel, Value: 16 
Key: indio, Value: 87 
Key: kili, Value: 43 
Key: lima, Value: 98 
Key: alpha, Value: 34 
Key: charlie, Value: 23 
Key: foxtrot, Value: 12 
Key: juliet, Value: 65 

sorted:
Key: alpha, Value: 34 
Key: bravo, Value: 56 
Key: charlie, Value: 23 
Key: delta, Value: 87 
Key: echo, Value: 56 
Key: foxtrot, Value: 12 
Key: golf, Value: 34 
Key: hotel, Value: 16 
Key: indio, Value: 87 
Key: juliet, Value: 65 
Key: kili, Value: 43 
Key: lima, Value: 98 
```

### map的键值对掉

```
package main

import (
	"fmt"
)

var (
	barVal = map[string]int{"alpha": 34, "bravo": 56, "charlie": 23,
		"delta": 87, "echo": 56, "foxtrot": 12,
		"golf": 34, "hotel": 16, "indio": 87,
		"juliet": 65, "kili": 43, "lima": 98}
)

func main() {
	invMap := make(map[int]string, len(barVal))
	fmt.Println("raw:")
	for k, v := range barVal {
		invMap[v] = k
		fmt.Printf("Key: %v, Value: %v \n", k, v)
	}

	fmt.Println()
	fmt.Println("inv:")
	for k, v := range invMap {
		fmt.Printf("Key: %v, Value: %v \n", k, v)
	}
}
```

```
raw:
Key: alpha, Value: 34 
Key: bravo, Value: 56 
Key: delta, Value: 87 
Key: hotel, Value: 16 
Key: kili, Value: 43 
Key: lima, Value: 98 
Key: charlie, Value: 23 
Key: echo, Value: 56 
Key: foxtrot, Value: 12 
Key: golf, Value: 34 
Key: indio, Value: 87 
Key: juliet, Value: 65 

inv:
Key: 34, Value: golf 
Key: 56, Value: echo 
Key: 87, Value: indio 
Key: 65, Value: juliet 
Key: 16, Value: hotel 
Key: 43, Value: kili 
Key: 98, Value: lima 
Key: 23, Value: charlie 
Key: 12, Value: foxtrot 
```

如果原始 value 值不唯一那么这么做肯定会出错；为了保证不出错，当遇到不唯一的 key 时应当立刻停止，这样可能会导致没有包含原 map 的所有键值对！一种解决方法就是仔细检查唯一性并且使用多值 map，比如使用 `map[int][]string`类型。 

```
package main

import (
	"fmt"
)

var (
	barVal = map[string]int{"alpha": 34, "bravo": 56, "charlie": 23,
		"delta": 87, "echo": 56, "foxtrot": 12,
		"golf": 34, "hotel": 16, "indio": 87,
		"juliet": 65, "kili": 43, "lima": 98}
)

func main() {
	invMap := make(map[int][]string, len(barVal))
	fmt.Println("raw:")
	for k, v := range barVal {
		_, ok := invMap[v]
		if ok {
			invMap[v] = append(invMap[v], k)
		}else {
			invMap[v] = []string{k}
		}
		fmt.Printf("Key: %v, Value: %v \n", k, v)
	}

	fmt.Println()
	fmt.Println("inv:")
	for k, v := range invMap {
		fmt.Printf("Key: %v, Value: %v \n", k, v)
	}
}
```

```
raw:
Key: golf, Value: 34 
Key: juliet, Value: 65 
Key: kili, Value: 43 
Key: lima, Value: 98 
Key: foxtrot, Value: 12 
Key: hotel, Value: 16 
Key: indio, Value: 87 
Key: alpha, Value: 34 
Key: bravo, Value: 56 
Key: charlie, Value: 23 
Key: delta, Value: 87 
Key: echo, Value: 56 

inv:
Key: 12, Value: [foxtrot] 
Key: 16, Value: [hotel] 
Key: 34, Value: [golf alpha] 
Key: 65, Value: [juliet] 
Key: 43, Value: [kili] 
Key: 23, Value: [charlie] 
Key: 98, Value: [lima] 
Key: 87, Value: [indio delta] 
Key: 56, Value: [bravo echo]
```

## 包

### 标准库
-  `unsafe`: 包含了一些打破 Go 语言“类型安全”的命令，一般的程序中不会被使用，可用在 C/C++ 程序的调用中。 <li> `syscall`-`os`-`os/exec`: 
  <ul>-  `os`: 提供给我们一个平台无关性的操作系统功能接口，采用类Unix设计，隐藏了不同操作系统间差异，让不同的文件系统和操作系统对象表现一致。 -  `os/exec`: 提供我们运行外部操作系统命令和程序的方式。 -  `syscall`: 底层的外部包，提供了操作系统底层调用的基本接口。 -  `archive/tar` 和 `/zip-compress`：压缩(解压缩)文件功能。 <li> `fmt`-`io`-`bufio`-`path/filepath`-`flag`: 
  <ul>-  `fmt`: 提供了格式化输入输出功能。 -  `io`: 提供了基本输入输出功能，大多数是围绕系统功能的封装。 -  `bufio`: 缓冲输入输出功能的封装。 -  `path/filepath`: 用来操作在当前系统中的目标文件名路径。 -  `flag`: 对命令行参数的操作。 
`strings`-`strconv`-`unicode`-`regexp`-`bytes`:
-  `strings`: 提供对字符串的操作。 -  `strconv`: 提供将字符串转换为基础类型的功能。 -  `unicode`: 为 unicode 型的字符串提供特殊的功能。 -  `regexp`: 正则表达式功能。 -  `bytes`: 提供对字符型分片的操作。 -  `index/suffixarray`: 子字符串快速查询。 
`math`-`math/cmath`-`math/big`-`math/rand`-`sort`:
-  `math`: 基本的数学函数。 -  `math/cmath`: 对复数的操作。 -  `math/rand`: 伪随机数生成。 -  `sort`: 为数组排序和自定义集合。 -  `math/big`: 大数的实现和计算。 
`container`-`/list-ring-heap`: 实现对集合的操作。
- `list`: 双链表。<li> `time`-`log`: 
  <ul>-  `time`: 日期和时间的基本操作。 -  `log`: 记录程序运行时产生的日志,我们将在后面的章节使用它。 
`encoding/json`-`encoding/xml`-`text/template`:
-  `encoding/json`: 读取并解码和写入并编码 JSON 数据。 -  `encoding/xml`:简单的 XML1.0 解析器,有关 JSON 和 XML 的实例请查阅第 12.9/10 章节。 -  `text/template`:生成像 HTML 一样的数据与文本混合的数据驱动模板（参见第 15.7 节）。 
`net`-`net/http`-`html`:（参见第 15 章）
-  `net`: 网络数据的基本操作。 -  `http`: 提供了一个可扩展的 HTTP 服务器和基础客户端，解析 HTTP 请求和回复。 -  `html`: HTML5 解析器。 
`runtime`: Go 程序运行时的交互操作，例如垃圾回收和协程创建。

`reflect`: 实现通过程序运行时反射，让程序操作任意类型的变量。

### regexp包

如果是简单模式，使用 `Match` 方法便可：

```
ok, _ := regexp.Match(pat, []byte(searchIn))

```

变量 ok 将返回 true 或者 false,我们也可以使用 `MatchString`：

```
ok, _ := regexp.MatchString(pat, searchIn)
```

```
package main
import (
	"fmt"
	"regexp"
	"strconv"
)
func main() {
	//目标字符串
	searchIn := "John: 2578.34 William: 4567.23 Steve: 5632.18"
	pat := "[0-9]+.[0-9]+" //正则

	f := func(s string) string{
		v, _ := strconv.ParseFloat(s, 32)
		return strconv.FormatFloat(v * 2, 'f', 2, 32)
	}

	if ok, _ := regexp.Match(pat, []byte(searchIn)); ok {
		fmt.Println("Match Found!")
	}

	re, _ := regexp.Compile(pat)
	//将匹配到的部分替换为"##.#"
	str := re.ReplaceAllString(searchIn, "##.#")
	fmt.Println(str)
	//参数为函数时
	str2 := re.ReplaceAllStringFunc(searchIn, f)
	fmt.Println(str2)
}
```

```
Match Found!
John: ##.# William: ##.# Steve: ##.#
John: 5156.68 William: 9134.46 Steve: 11264.36
```

### 锁和 sync 包

通常通过不同线程执行不同应用来实现程序的并发。当不同线程要使用同一个变量时，经常会出现一个问题：无法预知变量被不同线程修改的顺序！经典的做法是一次只能让一个线程对共享变量进行操作。当变量被一个线程改变时(临界区)，我们为它上锁，直到这个线程执行完成并解锁后，其他线程才能访问它。 map 类型是不存在锁的机制来实现这种效果(出于对性能的考虑)，所以 map 类型是非线程安全的。

`sync.Mutex` 是一个互斥锁，它的作用是守护在临界区入口来确保同一时间只能有一个线程进入临界区。假设 info 是一个需要上锁的放在共享内存中的变量。通过包含 `Mutex` 来实现的一个典型例子如下：

```
import  “sync”

type Info struct {
    mu sync.Mutex
    // ... other fields, e.g.: Str string
}
```

如果一个函数想要改变这个变量可以这样写:

```
func Update(info *Info) {
    info.mu.Lock()
    // critical section:
    info.Str = // new value
    // end critical section
    info.mu.Unlock()
}
```

还有一个很有用的例子是通过 Mutex 来实现一个可以上锁的共享缓冲器:

```
type SyncedBuffer struct {
    lock    sync.Mutex
    buffer  bytes.Buffer
}

```

在 sync 包中还有一个 `RWMutex` 锁：他能通过 `RLock()` 来允许同一时间多个线程对变量进行读操作，但是只能一个线程进行写操作。如果使用 `Lock()` 将和普通的 `Mutex` 作用相同。包中还有一个方便的 `Once` 类型变量的方法`once.Do(call)`，这个方法确保被调用函数只能被调用一次。相对简单的情况下，通过使用 sync 包可以解决同一时间只能一个线程访问变量或 map 类型数据的问题。如果这种方式导致程序明显变慢或者引起其他问题，我们要重新思考来通过 goroutines 和 channels 来解决问题，这是在 Go 语言中所提倡用来实现并发的技术。

### 自定义包

当写自己包的时候，要使用短小的不含有 `_ `的小写单词来为文件命名。这里有个简单例子来说明包是如何相互调用以及可见性是如何实现的。

```
package main

import (
	"test/pack1"
	"fmt"
)

func main() {
	var test1 string
	test1 = pack1.ReturnStr()
	fmt.Println(test1)
}
```

```
└── src
    └── test
        ├── go.mod
        ├── mymath
        │   ├── myMath1.go
        │   └── myMath2.go
        ├── pack1
        │   └── pack1.go
        ├── test.go
        └── test.txt

```

## 结构体与方法

Go 通过类型别名（alias types）和结构体的形式支持用户自定义类型，或者叫定制类型。一个带属性的结构体试图表示一个现实世界中的实体。结构体是复合类型（composite types），当需要定义一个类型，它由一系列属性组成，每个属性都有自己的类型和值的时候，就应该使用结构体，它把数据聚集在一起。然后可以访问这些数据，就好像它是一个独立实体的一部分。结构体也是值类型，因此可以通过 **new** 函数来创建。

组成结构体类型的那些数据称为 **字段（fields）**。每个字段都有一个类型和一个名字；在一个结构体中，字段名字必须是唯一的。结构体的概念在软件工程上旧的术语叫 ADT（抽象数据类型：Abstract Data Type），在一些老的编程语言中叫 **记录（Record）**，比如 Cobol，在 C 家族的编程语言中它也存在，并且名字也是 **struct**，在面向对象的编程语言中，跟一个无方法的轻量级类一样。不过因为 Go 语言中没有类的概念，因此在 Go 中结构体有着更为重要的地位。

### 结构体定义

#### 常规结构体

结构体定义的一般方式如下：

```
type identifier struct {
    field1 type1
    field2 type2
    ...
}
```

简单示例：

```
package main
import "fmt"

type struct1 struct {
	i1  int
	f1  float32
	str string
}

func main() {
	//ms := &amp;struct1{10, 15.5, "Chris"}

	ms := new(struct1)
	ms.i1 = 10
	ms.f1 = 15.5
	ms.str= "Chris"

	fmt.Printf("The int is: %d\n", ms.i1)
	fmt.Printf("The float is: %f\n", ms.f1)
	fmt.Printf("The string is: %s\n", ms.str)
	fmt.Printf("The struct is: %v\n", ms)
}
```

```
The int is: 10
The float is: 15.500000
The string is: Chris
The struct is: &amp;{10 15.5 Chris}
```

初始化一个结构体实例(一个结构体字面量：struct-literal)的更简短和惯用的方式如下：

```
    ms := &amp;struct1{10, 15.5, "Chris"}
    // 此时ms的类型是 *struct1

```

或者：

```
    var mt struct1
    ms := struct1{10, 15.5, "Chris"}
```

混合字面量语法 `&amp;struct1{a, b, c}` 是一种简写，底层仍然会调用 `new ()`，这里值的顺序必须按照字段顺序来写。在下面的例子中能看到可以通过在值的前面放上字段名来初始化字段的方式。表达式 `new(Type)`和 `&amp;Type{}` 是等价的。 

```
package main

import "fmt"

type Interval struct {
	start int
	end   int
}

func main() {
	intr1 := Interval{0, 3}
	intr2 := Interval{end: 3, start: 0}
	intr3 := Interval{end: 3}
	fmt.Printf("intr1: %v, intr2: %v, intr3: %v\n", intr1, intr2, intr3)
}
```

```
intr1: {0 3}, intr2: {0 3}, intr3: {0 3}
```

可以使用点号符给字段赋值：`structname.fieldname = value`。同样的，使用点号符可以获取结构体字段的值：`structname.fieldname`。在 Go 语言中这叫 **选择器（selector）**。

初始化一个结构体实例(一个结构体字面量：struct-literal)的更简短和惯用的方式如下：

```
    ms := &amp;struct1{10, 15.5, "Chris"}
    // 此时ms的类型是 *struct1

```

或者：

```
    var mt struct1
    ms := struct1{10, 15.5, "Chris"}
```

混合字面量语法（composite literal syntax）`&amp;struct1{a, b, c}` 是一种简写，底层仍然会调用 `new ()`，这里值的顺序必须按照字段顺序来写。在下面的例子中能看到可以通过在值的前面放上字段名来初始化字段的方式。表达式 `new(Type)`和 `&amp;Type{}` 是等价的。 

```
package main
import (
	"fmt"
	"strings"
)

type Person struct {
	firstName   string
	lastName    string
}

func upPerson(p *Person) {
	p.firstName = strings.ToUpper(p.firstName)
	p.lastName = strings.ToUpper(p.lastName)
}

func main() {
	// 1-struct as a value type:
	var pers1 Person
	pers1.firstName = "Chris"
	pers1.lastName = "Woodward"
	upPerson(&amp;pers1)
	fmt.Printf("The name of the person is %s %s\n", pers1.firstName, pers1.lastName)

	// 2—struct as a pointer:
	pers2 := new(Person)
	pers2.firstName = "Chris"
	pers2.lastName = "Woodward"
	(*pers2).lastName = "Woodward"  // 这是合法的
	upPerson(pers2)
	fmt.Printf("The name of the person is %s %s\n", pers2.firstName, pers2.lastName)

	// 3—struct as a literal:
	pers3 := &amp;Person{"Chris","Woodward"}
	upPerson(pers3)
	fmt.Printf("The name of the person is %s %s\n", pers3.firstName, pers3.lastName)
}
```

```
The name of the person is CHRIS WOODWARD
The name of the person is CHRIS WOODWARD
The name of the person is CHRIS WOODWARD
```

#### 结构体内存布局

Go 语言中，结构体和它所包含的数据在内存中是以连续块的形式存在的，即使结构体中嵌套有其他的结构体，这在性能上带来了很大的优势。不像 Java 中的引用类型，一个对象和它里面包含的对象可能会在不同的内存空间中，这点和 Go 语言中的指针很像。下面的例子清晰地说明了这些情况：

```
type Rect1 struct {Min, Max Point }
type Rect2 struct {Min, Max *Point }
```

#### 递归结构体

结构体类型可以通过引用自身来定义。这在定义链表或二叉树的元素（通常叫节点）时特别有用，此时节点包含指向临近节点的链接（地址）。如下所示，链表中的 `su`，树中的 `ri` 和 `le` 分别是指向别的节点的指针。

链表：

```
type Node struct {
    data    float64
    su      *Node
}
```

树： 

```
type Tree strcut {
    le      *Tree
    data    float64
    ri      *Tree
}
```

#### 结构体转换

```
package main
import "fmt"

type number struct {
	f float32
}

type nr number   // alias type

func main() {
	a := number{5.0}
	b := nr{5.0}
	// var i float32 = b   // compile-error: cannot use b (type nr) as type float32 in assignment
	// var i = float32(b)  // compile-error: cannot convert b (type nr) to type float32
	// var c number = b    // compile-error: cannot use b (type nr) as type number in assignment
	// needs a conversion:
	var c = number(b)
	fmt.Println(a, b, c)
}
```

```
{5} {5} {5}
```

### 结构体工厂 

Go 语言不支持面向对象编程语言中那样的构造子方法，了方便通常会为类型定义一个工厂，按惯例，工厂的名字以 new 或 New 开头。假设定义了如下的 File 结构体类型：

```
type File struct {
    fd      int     // 文件描述符
    name    string  // 文件名
}

```

下面是这个结构体类型对应的工厂方法，它返回一个指向结构体实例的指针：

```
func NewFile(fd int, name string) *File {
    if fd &lt; 0 {
        return nil
    }

    return &amp;File(fd, name)
}

```

然后这样调用它：

```
f := NewFile(10, "./test.txt")
```

如果 `File` 是一个结构体类型，那么表达式 `new(File)` 和 `&amp;File{}` 是等价的。这可以和大多数面向对象编程语言中笨拙的初始化方式做个比较：`File f = new File(...)`。我们可以说是工厂实例化了类型的一个对象，就像在基于类的面向对象编程语言中那样。

#### 强制使用工厂

通过应用可见性规则就可以禁止使用 new 函数，强制用户使用工厂方法，从而使类型变成私有的（比如小写结构体名），就像在面向对象语言中那样。

```
type matrix struct {
    ...
}

func NewMatrix(params) *matrix {
    m := new(matrix) // 初始化 m
    return m
}

```

在其他包里使用工厂方法：

```
package main
import "matrix"
...
wrong := new(matrix.matrix)     // 编译失败（matrix 是私有的）
right := matrix.NewMatrix(...)  // 实例化 matrix 的唯一方式
```

#### new 和 make 的区别

```
package main

type Foo map[string]string
type Bar struct {
    thingOne string
    thingTwo int
}

func main() {
    // OK
    y := new(Bar)
    (*y).thingOne = "hello"
    (*y).thingTwo = 1

    // NOT OK
    z := make(Bar) // 编译错误：cannot make type Bar
    (*y).thingOne = "hello"
    (*y).thingTwo = 1

    // OK
    x := make(Foo)
    x["x"] = "goodbye"
    x["y"] = "world"

    // NOT OK
    u := new(Foo)
    (*u)["x"] = "goodbye" // 运行时错误!! panic: assignment to entry in nil map
    (*u)["y"] = "world"
}
```

试图 `make()` 一个结构体变量，会引发一个编译错误，但是 `new()` 一个映射并试图使用数据填充它，将会引发运行时错误！ 因为 `new(Foo)` 返回的是一个指向 `nil` 的指针，它尚未被分配内存。所以在使用 `map` 时要特别谨慎。

### 自定义包的结构体

structPack/structPack.go （注意里边的  ExpStruct 是大写字母开头的）

```
package structPack

type ExpStruct struct {
	Mi1 int
	Mf1 float32
}
```

main.go

```
package main
import (
	"fmt"
	"test/structPack"
)

func main() {
	struct1 := new(structPack.ExpStruct)
	struct1.Mi1 = 10
	struct1.Mf1 = 16.

	fmt.Printf("Mi1 = %d\n", struct1.Mi1)
	fmt.Printf("Mf1 = %f\n", struct1.Mf1)
}
```

### 带标签的结构体

结构体中的字段除了有名字和类型外，还可以有一个可选的标签（tag）：它是一个附属于字段的字符串，可以是文档或其他的重要标记(比如重要说明或注释)。标签的内容不可以在一般的编程中使用，只有包 `reflect` 能获取它。在一个变量上调用 `reflect.TypeOf()` 可以获取变量的正确类型，如果变量是一个结构体类型，就可以通过 Field 来索引结构体的字段，然后就可以使用 Tag 属性。

```
package main

import (
	"fmt"
	"reflect"
)

type TagType struct {
	field1 bool		"An important answer"
	field2 string	"The name of the thing"
	field3 int		"How much there are"
}
func main() {
	tt := TagType{true, "looking", 1}
	for i := 0; i &lt; 3; i++ {
		refTag(tt, i)
	}
}

func refTag(tt TagType, ix int) {
	ttType := reflect.TypeOf(tt)
	ixField := ttType.Field(ix)
	fmt.Printf("%v:%v\n", ttType, ixField.Tag)
}
```

```
main.TagType:An important answer
main.TagType:The name of the thing
main.TagType:How much there are
```

### 匿名字段和内嵌结构体

结构体可以包含一个或多个 **匿名（或内嵌）字段**，即这些字段没有显式的名字，只有字段的类型是必须的，**此时类型也就是字段的名字**。匿名字段本身可以是一个结构体类型，即 **结构体可以包含内嵌结构体**。

#### 匿名字段

```
package main

import "fmt"

type innerS struct {
	in1 int
	in2 int
}

type outerS struct {
	b    int
	c    float32
	int  			// anonymous field
	innerS 			// anonymous field
}

func main() {
	outer := new(outerS)
	outer.b = 6
	outer.c = 7.5
	outer.int = 60
	outer.in1 = 5
	outer.in2 = 10

	fmt.Printf("outer.b is: %d\n", outer.b)
	fmt.Printf("outer.c is: %f\n", outer.c)
	fmt.Printf("outer.int is: %d\n", outer.int)
	fmt.Printf("outer.in1 is: %d\n", outer.in1)
	fmt.Printf("outer.in2 is: %d\n", outer.in2)

	// 使用结构体字面量
	outer2 := outerS{6, 7.5, 60, innerS{5, 10}}
	fmt.Printf("outer2 is: %v\n", outer2)
}
```

```
outer.b is: 6
outer.c is: 7.500000
outer.int is: 60
outer.in1 is: 5
outer.in2 is: 10
outer2 is: {6 7.5 60 {5 10}}
```

通过类型 `outer.int` 的名字来获取存储在匿名字段中的数据，于是可以得出一个结论：**在一个结构体中对于每一种数据类型只能有一个匿名字段（显而易见，不然取值时会出现字段冲突）。**

#### 内嵌结构体

同样地结构体也是一种数据类型，所以它也可以作为一个匿名字段来使用，如同上面例子中那样。外层结构体通过`outer.in1` 直接进入内层结构体的字段。

```
package main

import "fmt"

type A struct {
	ax int
	ay int
}

type B struct {
	A
	bx, by float32
}

func main() {
	b := B{A{1, 2}, 3.0, 4.0}
	fmt.Printf("b: %v\n", b)
	fmt.Println("b.A: ", b.A)
	fmt.Println(b.ax, b.ay, b.bx, b.by)
}
```

```
b: {<!-- -->{1 2} 3 4}
b.A:  {1 2}
1 2 3 4
```

#### 命名冲突
1. 外层名字会覆盖内层名字（几乎所有语言都是这样），这提供了一种重载字段或方法的方式。1. 如果相同的名字在同一级别出现了两次，如果这个名字被程序使用了，将会引发一个错误（不使用没关系）。没有办法来解决这种问题引起的二义性，必须由程序员自己修正。
```
package main

import "fmt"

type A struct {
	a int
}
type B struct {
	a, b int
}

type C struct {
	A
	B
}

func main() {
	c := C{A{1}, B{2, 3}}
	//fmt.Println(c.a)	// ambiguous selector c.a
	fmt.Println(c.A.a)
	fmt.Println(c.B.a)
}
```

```
1
2
```

```
package main

import "fmt"

type A struct {
	a int
}
type B struct {
	a, b int
}

type C struct {
	A
	B
	a int
}

func main() {
	c := C{A{1}, B{2, 3}, 4}
	fmt.Println(c.a)
	fmt.Println(c.A.a)
	fmt.Println(c.B.a)
}

```

```
4
1
2
```

### 方法

#### 方法定义

Go 方法是作用在接收者（receiver）上的一个函数，接收者是某种类型的变量。因此方法是一种特殊类型的函数。一个类型加上它的方法等价于面向对象中的一个类。一个重要的区别是：在 Go 中，类型的代码和绑定在它上面的方法的代码可以不放置在一起，它们可以存在在不同的源文件，唯一的要求是：它们必须是同一个包的。

定义方法的一般格式如下：

```
func (recv receiver_type) methodName(parameter_list) (return_value_list) { ... }
```

如果方法不需要使用 `recv` 的值，可以用 **_** 替换它，比如：

```
func (_ receiver_type) methodName(parameter_list) (return_value_list) { ... }
```



```
package main

import "fmt"

type TwoInts struct {
	a int
	b int
}

func main() {
	two1 := new(TwoInts)
	two1.a = 1
	two1.b = 2

	fmt.Printf("The sum is: %d\n", two1.Add1())

	two2 := TwoInts{3, 4}
	fmt.Printf("The sum is: %d\n", Add2(&amp;two2))
}

func (tn *TwoInts) Add1() int {  // 方法
	return tn.a + tn.b
}

func Add2(tn *TwoInts) int {     // 函数
	return tn.a + tn.b
}
```

```
The sum is: 3
The sum is: 7
```

```
package main

import "fmt"

type IntVector []int

func (v IntVector) Sum() (s int) {
	for _, x := range v {
		s += x
	}
	return
}

func main() {
	fmt.Println(IntVector{1, 2, 3}.Sum()) // 输出是6
}
```

类型和作用在它上面定义的方法必须在同一个包里定义，这就是为什么不能在 int、float 或类似这些的类型上定义方法。类型在其他的，或是非本地的包里定义，在它上面定义方法都会得到和上面同样的错误。但是有一个绕点的方式：可以先定义该类型（比如：int 或 float）的别名类型，然后再为别名类型定义方法。或者像下面这样将它作为匿名类型嵌入在一个新的结构体中。当然方法只在这个别名类型上有效。

```
package main

import (
	"fmt"
	"time"
)

type myTime struct {
	time.Time //anonymous field
}

func (t myTime) first3Chars() string {
	return t.Time.String()[0:3]
}
func main() {
	m := myTime{time.Now()}
	// 调用匿名Time上的String方法
	fmt.Println("Full time now:", m.String())
	// 调用myTime.first3Chars
	fmt.Println("First 3 chars:", m.first3Chars())
}

/* Output:
Full time now: 2022-08-11 09:05:22.4214735 +0800 CST m=+0.005682701
First 3 chars: 202
 */
```

#### 函数和方法的区别

函数将变量作为参数：**Function1(recv)**，方法在变量上被调用：**recv.Method1()。**接收者必须有一个显式的名字，这个名字必须在方法中被使用。**receiver_type** 叫做 **（接收者）基本类型**，这个类型必须在和方法同样的包中被声明。在 Go 中，（接收者）类型关联的方法不写在类型结构里面，就像类那样；耦合更加宽松；类型和方法之间的关联由接收者来建立。**方法没有和数据定义（结构体）混在一起：它们是正交的类型；表示（数据）和行为（方法）是独立的。**

#### 指针或值作为接收者

`change()`接受一个指向 B 的指针，并改变它内部的成员；`write()` 接受通过拷贝接受 B 的值并只输出B的内容。注意 Go 为我们做了探测工作，我们自己并没有指出是是否在指针上调用方法，Go 替我们做了这些事情。b1 是值而 b2 是指针，方法都支持运行了。

```
package main

import (
    "fmt"
)

type B struct {
    thing int
}

func (b *B) change() { b.thing = 1 }

func (b B) write() string { return fmt.Sprint(b) }

func main() {
    var b1 B // b1是值
    b1.change()
    fmt.Println(b1.write())

    b2 := new(B) // b2是指针
    b2.change()
    fmt.Println(b2.write())
}

/* Output：
{1}
{1}
*/
```

我们知道方法不需要指针作为接收者，**指针方法和值方法都可以在指针或非指针上被调用**：

```
package main

import (
	"fmt"
	"math"
)

type Point3 struct {
	x, y, z float64
}

func main() {
	p3 := Point3{0, 3, 4}
	fmt.Println(p3.Abs())
}

func (p Point3) Abs() float64{
	return math.Sqrt(p.x*p.x + p.y*p.y + p.z*p.z)
}
```

```
package main

import (
	"fmt"
	"math"
)

type Point3 struct {
	x, y, z float64
}

func main() {
	p3 := &amp;Point3{0, 3, 4}
	fmt.Println(p3.Abs())
}

func (p *Point3) Abs() float64{
	return math.Sqrt(p.x*p.x + p.y*p.y + p.z*p.z)
}
```

#### 方法和未导出字段

通过方法实现 getter 和 setter：

```
package main

import "fmt"

type Person struct {
	firstName string
	lastName  string
}

func (p *Person) FirstName() string {
	return p.firstName
}

func (p *Person) SetFirstName(newName string) {
	p.firstName = newName
}

func main()  {
	p := new(Person)
	p.SetFirstName("Eric")
	fmt.Println(p.firstName)
}

/* Output
Eric
*/
```

#### 并发访问对象

对象的字段（属性）不应该由 2 个或 2 个以上的不同线程在同一时间去改变。如果在程序发生这种情况，为了安全并发访问，可以使用包 `sync `中的方法。在后续章节我们会通过 goroutines 和 channels 探索另一种方式。

#### 内嵌类型的方法和继承

下面示例展示了内嵌结构体上的方法可以直接在外层类型的实例上调用：

```
package main

import (
	"fmt"
	"math"
)

type Point struct {
	x, y float64
}

func (p *Point) Abs() float64 {
	return math.Sqrt(p.x*p.x + p.y*p.y)
}

type NamedPoint struct {
	Point
	Name string
}

func main() {
	np := &amp;NamedPoint{Point{3, 4}, "Looking"}
	fmt.Println(np.Abs())
}

/* Output
5
*/

```

内嵌将一个已存在类型的字段和方法注入到了另一个类型里：匿名字段上的方法“晋升”成为了外层类型的方法。当然类型可以有只作用于本身实例而不作用于内嵌“父”类型上的方法，可以覆写方法（像字段一样）：和内嵌类型方法具有同样名字的外层类型的方法会覆写内嵌类型对应的方法（从其它语言的角度简单来理解的话，可以认为 NamedPoint 是 Point 的子类，当有同名方法时，子类的方法会屏蔽掉父类的同名方法）。

```
package main

import (
	"fmt"
	"math"
)

type Point struct {
	x, y float64
}

func (p *Point) Abs() float64 {
	return math.Sqrt(p.x*p.x + p.y*p.y)
}

type NamedPoint struct {
	Point
	Name string
}

func (np *NamedPoint) Abs() float64 {
	return np.Point.Abs() * 100
}

func main() {
	np := &amp;NamedPoint{Point{3, 4}, "Looking"}
	fmt.Println(np.Abs())
}

/* Output
500
*/

```

因为一个结构体可以嵌入多个匿名类型，所以实际上我们可以有一个简单版本的多重继承，就像：`type Child struct { Father; Mother}`。结构体内嵌和自己在同一个包中的结构体时，可以彼此访问对方所有的字段和方法。

#### 在类型中嵌入功能

主要有两种方法来实现在类型中嵌入功能：

A：聚合（或组合）：包含一个所需功能类型的具名字段。 B：内嵌：内嵌（匿名地）所需功能类型，像前一节所演示的那样。

为了使这些概念具体化，假设有一个 `Customer` 类型，我们想让它通过 `Log` 类型来包含日志功能，`Log` 类型只是简单地包含一个累积的消息（当然它可以是复杂的）。如果想让特定类型都具备日志功能，你可以实现一个这样的 `Log` 类型，然后将它作为特定类型的一个字段，并提供 `Log()`，它返回这个日志的引用。

聚合示例：

```
package main

import "fmt"

type Log struct{
	msg string
}

type Customer struct {
	Name string
	log *Log
}

func main() {
	c1 := new(Customer)
	c1.Name = "Looking1"
	c1.log = new(Log)
	c1.log.msg = "1 - Hello"
	c2 := &amp;Customer{"Looking2", &amp;Log{"2 - World"}}
	c1.Log().Add(c2.log.String())
	fmt.Println(c1.Log())
}

func (l *Log) Add(s string) {
	l.msg += "\n" + s
}

func (l *Log) String() string {
	return l.msg
}

func (c *Customer) Log() *Log {
	return c.log
}

```

```
1 - Hello
2 - World
```

内嵌示例：

```
package main

import "fmt"

type Log struct{
	msg string
}

type Customer struct {
	Name string
	Log
}

func main() {
	c := &amp;Customer{"Looking", Log{"Hello"}}
	c.Add("World")
	fmt.Println(c)
}

func (l *Log) Add(s string) {
	l.msg += "&lt;Log&gt;" + s
}

//func (c *Customer) Add(s string)  {
//	c.msg += "&lt;Customer&gt;" + s
//}

func (l *Log) String() string {
	return l.msg
}

func (c *Customer) String() string {
	return c.Name + "\nLog: " + fmt.Sprintln(c.Log)
}

```

```
Looking
Log: {Hello&lt;Log&gt;World}
```

还可以通过例子了解内嵌方法调用顺序：

```
package main

import "fmt"

type Log struct{
	msg string
}

type Customer struct {
	Name string
	Log
}

func main() {
	c := &amp;Customer{"Looking", Log{"Hello"}}
	c.Add("World")
	fmt.Println(c)
}

func (l *Log) Add(s string) {
	l.msg += "&lt;Log&gt;" + s
}

func (c *Customer) Add(s string)  {
	c.msg += "&lt;Customer&gt;" + s
}

func (l *Log) String() string {
	return l.msg
}

func (c *Customer) String() string {
	return c.Name + "\nLog: " + fmt.Sprintln(c.Log)
}

```

```
Looking
Log: {Hello&lt;Customer&gt;World}
```

内嵌的类型不需要指针，`Customer` 也不需要 `Add` 方法，它使用 `Log` 的 `Add` 方法，`Customer` 有自己的 `String` 方法，并且在它里面调用了 `Log` 的 `String` 方法。如果内嵌类型嵌入了其他类型，也是可以的，那些类型的方法可以直接在外层类型中使用。

#### 多重继承

```
package main

import "fmt"

type Camera struct {}

func (c *Camera) TakePicture() string {
	return "Click"
}

type Phone struct {}

func (p *Phone) Call() string {
	return "Ring"
}

type CameraPhone struct {
	Camera
	Phone
}

func main() {
	cp := new(CameraPhone)
	fmt.Println(cp.TakePicture())
	fmt.Println(cp.Call())
}
```

```
Click
Ring
```

#### 通用方法及命名

在编程中一些基本操作会一遍又一遍的出现，比如打开（Open）、关闭（Close）、读（Read）、写（Write）、排序（Sort）等等，并且它们都有一个大致的意思：打开（Open）可以作用于一个文件、一个网络连接、一个数据库连接等等。具体的实现可能千差万别，但是基本的概念是一致的。在 Go 语言中，通过使用接口，标准库广泛的应用了这些规则，在标准库中这些通用方法都有一致的名字，比如 `Open()`、`Read()`、`Write()`等。想写规范的 Go 程序，就应该遵守这些约定，给方法合适的名字和签名，就像那些通用方法那样。这样做会使 Go 开发的软件更加具有一致性和可读性。比如：如果需要一个 convert-to-string 方法，应该命名为 `String()`，而不是 `ToString()`。在如 C++、Java、C# 和 Ruby 这样的面向对象语言中，方法在类的上下文中被定义和继承：在一个对象上调用方法时，运行时会检测类以及它的超类中是否有此方法的定义，如果没有会导致异常发生。在 Go 语言中，这样的继承层次是完全没必要的：如果方法在此类型定义了，就可以调用它，和其他类型上是否存在这个方法没有关系。在这个意义上，Go 具有更大的灵活性。

比如：我们想定义自己的 `Integer` 类型，并添加一些类似转换成字符串的方法，在 Go 中可以如下定义：

```
type Integer int
func (i *Integer) String() string {
    return strconv.Itoa(i)
}

```

在 Java 或 C# 中，这个方法需要和类 `Integer` 的定义放在一起，在 Ruby 中可以直接在基本类型 int 上定义这个方法。

## 接口与反射

### 接口

Go 语言不是一种 **“传统”** 的面向对象编程语言：它里面没有类和继承的概念。但是 Go 语言里有非常灵活的 **接口** 概念，通过它可以实现很多面向对象的特性。接口提供了一种方式来 **说明** 对象的行为：如果谁能搞定这件事，它就可以用在这儿。

接口定义了一组方法（方法集），但是这些方法不包含（实现）代码：它们没有被实现（它们是抽象的）。接口里也不能包含变量。

通过如下格式定义接口：

```
type Namer interface {
    Method1(param_list) return_type
    Method2(param_list) return_type
    ...
}

```

上面的 `Namer` 是一个 **接口类型**。

按照约定，只包含一个方法的接口的名字由方法名加 `[e]r` 后缀组成，例如`Printer`、`Reader`、`Writer`、`Logger`、`Converter` 等等。还有一些不常用的方式（当后缀 `er` 不合适时），比如`Recoverable`，此时接口名以 `able` 结尾，或者以 `I` 开头（像 `.NET` 或 `Java` 中那样）。

Go 语言中的接口都很简短，**通常它们会包含 0 个、最多 3 个方法**。不像大多数面向对象编程语言，在 Go 语言中接口可以有值，一个接口类型的变量或一个 **接口值** ：`var ai Namer`，`ai`是一个多字（multiword）数据结构，它的值是 `nil`。它本质上是一个指针，虽然不完全是一回事。**指向接口值的指针是非法的，它们不仅一点用也没有，还会导致代码错误。**

此处的方法指针表是通过运行时反射能力构建的。类型（比如结构体）实现接口方法集中的方法，每一个方法的实现说明了此方法是如何作用于该类型的：**即实现接口**，同时方法集也构成了该类型的接口。实现了 `Namer` 接口类型的变量可以赋值给 `ai` （接收者值），此时方法表中的指针会指向被实现的接口方法。当然如果另一个类型（也实现了该接口）的变量被赋值给 `ai`，这二者（译者注：指针和方法实现）也会随之改变。

**类型不需要显式声明它实现了某个接口：接口被隐式地实现。多个类型可以实现同一个接口**。**实现某个接口的类型（除了实现接口方法外）可以有其他的方法**。**一个类型可以实现多个接口**。**接口类型可以包含一个实例的引用， 该实例的类型实现了此接口（接口是动态类型）**。

```
package main

import "fmt"

type Shaper interface {
	Area() float32
	Perimeter() float32
}

type Square struct {
	side float32
}

func (sq *Square) Area() float32{
	return sq.side * sq.side
}

func (sq *Square) Perimeter() float32{
	return sq.side * 4
}

func main() {
	sq1 := new(Square)
	sq1.side = 5
	var shaper Shaper
	shaper = Shaper(sq1) // 如果 sq1 没有实现 Shaper 所要求的所有方法，则不可以进行这种转换

	fmt.Println("Area:\t\t", shaper.Area())
	fmt.Println("Perimeter:\t", shaper.Perimeter())
}

```

```
Area:		 25
Perimeter:	 20
```

#### 接口多态

```
package main

import (
	"fmt"
)

type Shaper interface {
	Name() string
	Area() float32
}

type Square struct {
	name string
	side float32
}

func (sq *Square) Name() string{
	return sq.name
}

func (sq *Square) Area() float32{
	return sq.side * sq.side
}

type Rectangle struct {
	name string
	length, width float32
}

func (r Rectangle) Area() float32{
	return r.length * r.width
}

func (r Rectangle) Name() string{
	return r.name
}

func main() {
	s := &amp;Square{"Square", 5}
	r := Rectangle{"Rectangle", 3, 4}
	shapes := []Shaper{s, r}
	for _, ele := range shapes{
		fmt.Println("Shape details: ", ele)
		fmt.Printf("Area of the %s is: %v\n", ele.Name(), ele.Area())
	}
}

```

```
Shape details:  &amp;{Square 5}
Area of the Square is: 25
Shape details:  {Rectangle 3 4}
Area of the Rectangle is: 12
```

在调用 `ele.Area()` 这个时，只知道 `ele` 是一个 `Shaper` 对象，最后它摇身一变成为了一个 `Square` 或`Rectangle` 对象，并且表现出了相对应的行为。

```
package main

import "fmt"

type stockPosition struct {
	ticker		string
	sharePrice	float32
	count		float32
}

func (s stockPosition) getValue() float32{
	return s.sharePrice * s.count
}

type car struct{
	make	string
	model	string
	price	float32
}

func (c car) getValue() float32{
	return c.price
}

type valuable interface {
	getValue() float32
}

func showValue(assert valuable){
	fmt.Printf("Value of the asset is %f\n", assert.getValue())
}

func main() {
	var o valuable = stockPosition{"GOOG", 577.2, 4}
	showValue(o)
	o = car{"BMW", "M3", 66500}
	showValue(o)
}

```

```
Value of the asset is 2308.800049
Value of the asset is 66500.000000
```

#### 嵌套接口

一个接口可以包含一个或多个其他的接口，这相当于直接将这些内嵌接口的方法列举在外层接口中一样。比如接口 `File` 包含了 `ReadWrite` 和 `Lock` 的所有方法，它还额外有一个 `Close()` 方法。

```
type ReadWrite interface {
    Read(b Buffer) bool
    Write(b Buffer) bool
}

type Lock interface {
    Lock()
    Unlock()
}

type File interface {
    ReadWrite
    Lock
    Close()
}
```

#### 接口转换

```
package main

import "fmt"

type USB interface {
	Name() string
	Connector
}

type Connector interface {
	Connect()
}

type PhoneConnector struct {
	name string
}

func (pc PhoneConnector) Name() string {
	return pc.name
}

func (pc PhoneConnector) Connect() {
	fmt.Println("Connected:", pc.name)
}

type TVConnector struct {
	name string
}

func (tv TVConnector) Connect() {
	fmt.Println("Connected:", tv.name)
}

func main() {
	pc := PhoneConnector{"PhoneConnector"}
	var a USB
	a = USB(pc)
	a.Name()
	a.Connect() // Connected: PhoneConnector

	var b Connector
	b = Connector(pc) // 可以转换，因为 pc 也实现了 Connector 所需要的 Connect() 方法
	pc.name = "pc"    // 此处修改不影响 b.Connect() 的输出，说明对象赋值给接口时，会发生拷贝
	b.Connect()       // Connected: PhoneConnector
	//b.Name()  // 不能调用，因为 Connector 没有实现 Name() 方法

	tv := TVConnector{"TVConnector"}
	tv.Connect() // Connected: TVConnector
	//a = USB(tv) // 不能转换，因为 tv 没有实现 USB 所需的 Name() 方法
	//a.Name()

	var c interface{}
	fmt.Println(c == nil) // true
	var p *int = nil
	c = p
	fmt.Println(c == nil) // false
}

```

#### 类型断言与判断

#### 类型断言 

一个接口类型的变量 `varI` 中可以包含任何类型的值，必须有一种方式来检测它的 **动态** 类型，即运行时在变量中存储的值的实际类型。在执行过程中动态类型可能会有所不同，但是它总是可以分配给接口变量本身的类型。通常我们可以使用**类型断言** 来测试在某个时刻 `varI` 是否包含类型 `T` 的值：

```
v := varI.(T)       // unchecked type assertion

```

**varI 必须是一个接口变量**，否则编译器会报错：`invalid type assertion: varI.(T) (non-interface type (type of varI) on left)` 。

接口是一种契约，实现类型必须满足它，它描述了类型的行为，规定类型可以做什么。接口彻底将类型能做什么，以及如何做分离开来，使得相同接口的变量在不同的时刻表现出不同的行为，这就是多态的本质。编写参数是接口变量的函数，这使得它们更具有一般性。**使用接口使代码更具有普适性。**标准库里到处都使用了这个原则，如果对接口概念没有良好的把握，是不可能理解它是如何构建的。

```
package main

import (
	"fmt"
	"math"
)

type Square struct {
	side float32
}

type Circle struct {
	radius float32
}

type Shaper interface {
	Area() float32
}

func main() {
	s := Square{5}
	c := Circle{5}
	areaIntfs := []Shaper{s, c}
	for _, areaIntf := range areaIntfs {
		if t, ok := areaIntf.(Square); ok{
			fmt.Printf("The type of areaIntf is: %T\n", t)
		}

		if t, ok := areaIntf.(Circle); ok{
			fmt.Printf("The type of areaIntf is: %T\n", t)
		}
	}
}

func (s Square) Area() float32{
	return s.side * s.side
}

func (c Circle) Area() float32{
	return c.radius * c.radius * math.Pi
}
```

```
The type of areaIntf is: main.Square
The type of areaIntf is: main.Circle
```

#### 类型判断

```
package main

import (
	"fmt"
	"math"
)

type Square struct {
	side float32
}

type Circle struct {
	radius float32
}

type Shaper interface {
	Area() float32
}

func main() {
	s := Square{5}
	c := Circle{5}
	areaIntfs := []Shaper{s, c}
	for _, areaIntf := range areaIntfs {
		switch t := areaIntf.(type) {
		case Square:
			fmt.Printf("The type of areaIntf is: %T\n", t)
		case Circle:
			fmt.Printf("The type of areaIntf is: %T\n", t)
		case nil:
			fmt.Printf("nil value: nothing to check?\n")
		default:
			fmt.Printf("Unexpected type %T\n", t)
		}
	}
}

func (s Square) Area() float32{
	return s.side * s.side
}

func (c Circle) Area() float32{
	return c.radius * c.radius * math.Pi
}
```

```
The type of areaIntf is: main.Square
The type of areaIntf is: main.Circle
```

下面的代码片段展示了一个类型分类函数，它有一个可变长度参数，可以是任意类型的数组，它会根据数组元素的实际类型执行不同的动作：

```
func classifier(items ...interface{}) {
    for i, x := range items {
        switch x.(type) {
        case bool:
            fmt.Printf("Param #%d is a bool\n", i)
        case float64:
            fmt.Printf("Param #%d is a float64\n", i)
        case int, int64:
            fmt.Printf("Param #%d is a int\n", i)
        case nil:
            fmt.Printf("Param #%d is a nil\n", i)
        case string:
            fmt.Printf("Param #%d is a string\n", i)
        default:
            fmt.Printf("Param #%d is unknown\n", i)
        }
    }
}

```

可以这样调用此方法：`classifier(13, -14.3, "BELGIUM", complex(1, 2), nil, false)` 。

```
Param #0 is a int
Param #1 is a float64
Param #2 is a string
Param #3 is unknown
Param #4 is a nil
Param #5 is a bool
```

在处理来自于外部的、类型未知的数据时，比如解析诸如 JSON 或 XML 编码的数据，类型测试和转换会非常有用。

### 方法集与接口

作用于变量上的方法实际上是不区分变量到底是指针还是值的。当碰到接口类型值时，这会变得有点复杂，原因是接口变量中存储的具体值是不可寻址的，幸运的是，如果使用不当编译器会给出错误。

```
package main

import "fmt"

type List []int

func (l List) Len() int {
	return len(l)
}

func (l *List) Append(val int) {
	*l = append(*l, val)
}

type Appender interface {
	Append(int)
}

func CountInto(a Appender, start, end int) {
	for i := start; i &lt;= end; i++ {
		a.Append(i)
	}
}

type Lener interface {
	Len() int
}

func LongEnough(l Lener) bool {
	return l.Len() * 10 &gt; 42
}
func main() {
	var lst List
	// compiler error:
	// cannot use lst (type List) as type Appender in argument to CountInto:
	//       List does not implement Appender (Append method has pointer receiver)
	// CountInto(lst, 1, 10)
	if LongEnough(lst) { // VALID:Identical receiver type
		fmt.Printf("- lst is long enough\n")
	}

	plst := new(List)
	CountInto(plst, 1, 10)
	if LongEnough(plst) {
		// VALID: a *List can be dereferenced for the receiver
		fmt.Printf("- plst is long enough\n")
	}
}

```

```
- plst is long enough
```

**讨论**

在 `lst` 上调用 `CountInto` 时会导致一个编译器错误，因为 `CountInto` 需要一个 `Appender`，而它的方法 `Append` 只定义在指针上。 在 `lst` 上调用 `LongEnough` 是可以的因为 'Len' 定义在值上。

在 `plst` 上调用 `CountInto` 是可以的，因为 `CountInto` 需要一个 `Appender`，并且它的方法 `Append` 定义在指针上。 在 `plst` 上调用 `LongEnough` 也是可以的，因为指针会被自动解引用。

**总结**

在接口上调用方法时，必须有和方法定义时相同的接收者类型或者是可以从具体类型 `P` 直接可以辨识的：
- 指针方法可以通过指针调用- 值方法可以通过值调用- 接收者是值的方法可以通过指针调用，因为指针会首先被解引用- 接收者是指针的方法不可以通过值调用，因为存储在接口中的值没有地址
将一个值赋值给一个接口赋值时，编译器会确保所有可能的接口方法都可以在此值上被调用，因此不正确的赋值在编译期就会失败。

**译注**

Go 语言规范定义了接口方法集的调用规则：
- 类型 *T 的可调用方法集包含接受者为 *T 或 T 的所有方法集- 类型 T 的可调用方法集包含接受者为 T 的所有方法，不包含接受者为 *T 的方法
### 接口示例

#### 排序

```
package main

import (
	"fmt"
)

func Sort(data Sorter) {
	for pass := 1; pass &lt; data.Len(); pass++ {
		for i := 0; i &lt; data.Len()-pass; i++ {
			if data.Less(i+1, i) {
				data.Swap(i, i+1)
			}
		}
	}
}

type Sorter interface {
	Len() int
	Less(i, j int) bool
	Swap(i, j int)
}

type IntArray []int

func (p IntArray) Len() int {
	return len(p)
}

func (p IntArray) Less(i, j int) bool {
	return p[i] &lt; p[j]
}

func (p IntArray) Swap(i, j int) {
	p[i], p[j] = p[j], p[i]
}

func main() {
	data := IntArray{74, 59, 238, -784, 9845, 959, 905, 0, 0, 42, 7586, -5467984, 7586}
	a := Sorter(data)
	Sort(a)
	fmt.Println(a)
}

```

```
[-5467984 -784 0 0 42 59 74 238 905 959 7586 7586 9845]
```

sort.go

```
package sort

type Sorter interface {
	Len() int
	Less(i, j int) bool
	Swap(i, j int)
}

func Sort(data Sorter) {
	for pass := 1; pass &lt; data.Len(); pass++ {
		for i := 0; i &lt; data.Len()-pass; i++ {
			if data.Less(i+1, i) {
				data.Swap(i, i+1)
			}
		}
	}
}

func IsSorted(data Sorter) bool {
	n := data.Len()
	for i := n - 1; i &gt; 0; i-- {
		if data.Less(i, i-1) {
			return false
		}
	}
	return true
}

// Convenience types for common cases
type IntArray []int

func (p IntArray) Len() int           { return len(p) }
func (p IntArray) Less(i, j int) bool { return p[i] &lt; p[j] }
func (p IntArray) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }

type StringArray []string

func (p StringArray) Len() int           { return len(p) }
func (p StringArray) Less(i, j int) bool { return p[i] &lt; p[j] }
func (p StringArray) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }

// Convenience wrappers for common cases
func SortInts(a []int)       { Sort(IntArray(a)) }
func SortStrings(a []string) { Sort(StringArray(a)) }

func IntsAreSorted(a []int) bool       { return IsSorted(IntArray(a)) }
func StringsAreSorted(a []string) bool { return IsSorted(StringArray(a)) }
```

main.go

```
package main

import (
	"test/sort"
	"fmt"
)

func ints() {
	data := []int{74, 59, 238, -784, 9845, 959, 905, 0, 0, 42, 7586, -5467984, 7586}
	//a := sort.IntArray(data) //conversion to type IntArray
	//sort.Sort(a)
	sort.SortInts(data)
	//if !sort.IsSorted(a) {
	if !sort.IntsAreSorted(data) {
		panic("fails")
	}
	//fmt.Printf("The sorted array is: %v\n", a)
	fmt.Printf("The sorted array is: %v\n", data)
}

func strings() {
	data := []string{"monday", "friday", "tuesday", "wednesday", "sunday", "thursday", "", "saturday"}
	//a := sort.StringArray(data)
	//sort.Sort(a)
	sort.SortStrings(data)
	//if !sort.IsSorted(a) {
	if !sort.StringsAreSorted(data) {
		panic("fail")
	}
	//fmt.Printf("The sorted array is: %v\n", a)
	fmt.Printf("The sorted array is: %v\n", data)
}

type day struct {
	num       int
	shortName string
	longName  string
}

type dayArray struct {
	data []*day
}

func (p *dayArray) Len() int           { return len(p.data) }
func (p *dayArray) Less(i, j int) bool { return p.data[i].num &lt; p.data[j].num }
func (p *dayArray) Swap(i, j int)      { p.data[i], p.data[j] = p.data[j], p.data[i] }

func days() {
	Sunday    := day{0, "SUN", "Sunday"}
	Monday    := day{1, "MON", "Monday"}
	Tuesday   := day{2, "TUE", "Tuesday"}
	Wednesday := day{3, "WED", "Wednesday"}
	Thursday  := day{4, "THU", "Thursday"}
	Friday    := day{5, "FRI", "Friday"}
	Saturday  := day{6, "SAT", "Saturday"}
	data := []*day{&amp;Tuesday, &amp;Thursday, &amp;Wednesday, &amp;Sunday, &amp;Monday, &amp;Friday, &amp;Saturday}
	a := dayArray{data}
	sort.Sort(&amp;a)
	if !sort.IsSorted(&amp;a) {
		panic("fail")
	}
	for _, d := range data {
		fmt.Printf("%s ", d.longName)
	}
	fmt.Printf("\n")
}

func main() {
	ints()
	strings()
	days()
}
```

```
The sorted array is: [-5467984 -784 0 0 42 59 74 238 905 959 7586 7586 9845]
The sorted array is: [ friday monday saturday sunday thursday tuesday wednesday]
Sunday Monday Tuesday Wednesday Thursday Friday Saturday
```

`panic("fail")` 用于停止处于在非正常情况下的程序，当然也可以先打印一条信息，然后调用`os.Exit(1)` 来停止程序。

上面的例子帮助我们进一步了解了接口的意义和使用方式。对于基本类型的排序，标准库已经提供了相关的排序函数，所以不需要我们再重复造轮子了。对于一般性的排序，`sort` 包定义了一个接口：

```
type Interface interface {
    Len() int
    Less(i, j int) bool
    Swap(i, j int)
}

```

这个接口总结了需要用于排序的抽象方法，函数 `Sort(data Interface)` 用来对此类对象进行排序，可以用它们来实现对其他数据（非基本类型）进行排序。在上面的例子中，我们也是这么做的，不仅可以对 `int` 和 `string` 序列进行排序，也可以对用户自定义类型 `dayArray` 进行排序。

#### 读写

读和写是软件中很普遍的行为，提起它们会立即想到读写文件、缓存（比如字节或字符串切片）、标准输入输出、标准错误以及网络连接、管道等等，或者读写我们的自定义类型。为了使代码尽可能通用，Go 采取了一致的方式来读写数据。`io` 包提供了用于读和写的接口 `io.Reader` 和 `io.Writer`：

```
type Reader interface {
    Read(p []byte) (n int, err error)
}

type Writer interface {
    Write(p []byte) (n int, err error)
}

```

只要类型实现了读写接口，提供 `Read()` 和 `Write` 方法，就可以从它读取数据，或向它写入数据。一个对象要是可读的，它必须实现 `io.Reader` 接口，这个接口只有一个签名是 `Read(p []byte) (n int, err error)` 的方法，它从调用它的对象上读取数据，并把读到的数据放入参数中的字节切片中，然后返回读取的字节数和一个 `error` 对象，如果没有错误发生返回 'nil'，如果已经到达输入的尾端，会返回 `io.EOF("EOF")`，如果读取的过程中发生了错误，就会返回具体的错误信息。类似地，一个对象要是可写的，它必须实现 `io.Writer` 接口，这个接口也只有一个签名是 `Write(p []byte) (n int, err error)` 的方法，它将指定字节切片中的数据写入调用它的对象里，然后返回实际写入的字节数一个 `error` 对象（如果没有错误发生就是 `nil`）。`io` 包里的 `Readers` 和 `Writers` 都是不带缓冲的，`bufio` 包里提供了对应的带缓冲的操作，在读写 `UTF-8` 编码的文本文件时它们尤其有用。在后边我们会看到在实战使用它们的很多例子。实际编程中尽可能的使用这些接口，会使程序变得更通用，可以在任何实现了这些接口的类型上使用读写方法。

### 空接口

#### 概念

**空接口或者最小接口** 不包含任何方法，它对实现不做任何要求：

```
type Any interface {}

```

任何其他类型都实现了空接口，`any` 或 `Any` 是空接口一个很好的别名或缩写。空接口类似 `Java/C#` 中所有类的基类： `Object` 类，二者的目标也很相近。可以给一个空接口类型的变量 `var val interface {}` 赋任何类型的值（空接口变量就有点像 ruby 或 Python 这种解释性语言中的变量了）。

```
package main

import "fmt"

var i = 5
var str = "ABC"

type Person struct {
	name string
	age  int
}

type Any interface {}

func main() {
	var val Any
	val = 5
	fmt.Printf("val has the value: %v\n", val)
	val = str
	fmt.Printf("val has the value: %v\n", val)
	pers1 := new(Person)
	pers1.name = "Looking"
	pers1.age = 29
	val = pers1
	fmt.Printf("val has the value: %v\n", val)
	switch t := val.(type) {
	case int:
		fmt.Printf("Type int %T\n", t)
	case string:
		fmt.Printf("Type string %T\n", t)
	case bool:
		fmt.Printf("Type bool %T\n", t)
	case *Person:
		fmt.Printf("Type pointer to Person %T\n", t)
	default:
		fmt.Printf("Type default %T\n", t)
	}

}
```

```
val has the value: 5
val has the value: ABC
val has the value: &amp;{Looking 29}
Type pointer to Person *main.Person
```

在上面的例子中，接口变量 `val` 被依次赋予一个 `int`，`string` 和 `Person` 实例的值，然后使用 `type-swtich` 来测试它的实际类型。每个 `interface {}` 变量在内存中占据两个字长：一个用来存储它包含的类型，另一个用来存储它包含的数据或者指向数据的指针。

```
package main

import "fmt"

type specialString string

var whatIsThis specialString = "hello"

func TypeSwitch() {
	testFunc := func(any interface{}) {
		switch v := any.(type) {
		case bool:
			fmt.Printf("any %v is a bool type", v)
		case int:
			fmt.Printf("any %v is an int type", v)
		case float32:
			fmt.Printf("any %v is a float32 type", v)
		case string:
			fmt.Printf("any %v is a string type", v)
		case specialString:
			fmt.Printf("any %v is a special String!", v)
		default:
			fmt.Println("unknown type!")
		}
	}
	testFunc(whatIsThis)
}

func main() {
	TypeSwitch()
}
```

```
any hello is a special String!
```

#### 构建通用类型数组

让我们给空接口定一个别名类型 `Element`：`type Element interface{}`，然后定义一个容器类型的结构体 `Vector`，它包含一个 `Element` 类型元素的切片：

```
type Vector struct {
    a []Element
}

```

`Vector` 里能放任何类型的变量，因为任何类型都实现了空接口，实际上 `Vector` 里放的每个元素可以是不同类型的变量。我们为它定义一个 `At()` 方法用于返回第 `i` 个元素：

```
func (p *Vector) At(i int) Element {
    return p.a[i]
}

```

再定一个 `Set()` 方法用于设置第 `i` 个元素的值：

```
func (p *Vector) Set(i int, e Element) {
    p.a[i] = e
}
```

`Vector` 中存储的所有元素都是 `Element` 类型，要得到它们的原始类型（unboxing：拆箱），需要用到类型断言。 

完整示例：

```
package main

import "fmt"

type Element interface {
}

type Vector struct {
	a [3]Element
}

func (p *Vector) At(i int) Element {
	return p.a[i]
}

func (p *Vector) Set(i int, e Element) {
	p.a[i] = e
}
func main() {
	v := new(Vector)
	v.Set(0, "Hello")
	v.Set(1, 2)
	v.Set(2, 3.14)
	fmt.Printf("the value of v is %v\n", v.a)
}

```

```
the value of v is [Hello 2 3.14]
```

#### 复制数据切片到空接口切片

假设你有一个 `myType` 类型的数据切片，你想将切片中的数据复制到一个空接口切片中，类似：

```
var dataSlice []myType = FuncReturnSlice()
var interfaceSlice []interface{} = dataSlice

```

可惜不能这么做，编译时会出错：

```
cannot use dataSlice (type []myType) as type []interface { } in assignment
```

原因是它们俩在内存中的布局是不一样的，必须使用 `for-range` 语句来一个一个显式地复制：

```
var dataSlice []myType = FuncReturnSlice()
var interfaceSlice []interface{} = make([]interface{}, len(dataSlice))
for ix, d := range dataSlice {
    interfaceSlice[i] = d
}
```

#### 通用类型的节点数据结构

```
package main

import "fmt"

type Node struct {
	le   *Node
	data interface{}
	ri   *Node
}

func NewNode(left, right *Node) *Node {
	return &amp;Node{left, nil, right}
}

func (n *Node) SetData(data interface{}) {
	n.data = data
}

func main() {
	root := NewNode(nil, nil)
	root.SetData("root node")
	// make child (leaf) nodes:
	a := NewNode(nil, nil)
	a.SetData("left node")
	b := NewNode(nil, nil)
	b.SetData("right node")
	root.le = a
	root.ri = b
	fmt.Printf("%v\n", root) // Output: &amp;{0x125275f0 root node 0x125275e0}
}
```

### 反射包

#### 方法和类型的反射

我们看到可以通过反射来分析一个结构体。本节我们进一步探讨强大的反射功能。反射是用程序检查其所拥有的结构，尤其是类型的一种能力；这是元编程的一种形式。反射可以在运行时检查类型和变量，例如它的大小、方法和`动态`的调用这些方法。这对于没有源代码的包尤其有用。这是一个强大的工具，除非真得有必要，否则应当避免使用或小心使用。

变量的最基本信息就是类型和值：反射包的`Type`用来表示一个Go类型，反射包的`Value`为Go值提供了反射接口。

两个简单的函数,`reflect.TypeOf`和`reflect.ValueOf`，返回被检查对象的类型和值。例如，x被定义为：`var x float64 = 3.4`,那么`reflect.TypeOf(x)`返回`float64`，`reflect.ValueOf(x)`返回`&lt;float64 Value&gt;`

实际上，反射是通过检查一个接口的值，变量首先被转换成空接口。这从下面两个函数签名能够很明显的看出来：

```
    func TypeOf(i interface{}) Type
    func ValueOf(i interface{}) Value
```

接口的值包含一个type和value。反射可以从接口值反射到对象，也可以从对象反射回接口值。reflect.Type 和 reflect.Value 都有许多方法用于检查和操作它们。一个重要的例子是 Value 有一个 Type 方法返回 reflect.Value 的 Type。另一个是 Type 和 Value 都有 Kind 方法返回一个常量来表示类型：Uint、Float64、Slice 等等。同样 Value 有叫做 Int 和 Float 的方法可以获取存储在内部的值。

```
const (
    Invalid Kind = iota
    Bool
    Int
    Int8
    Int16
    Int32
    Int64
    Uint
    Uint8
    Uint16
    Uint32
    Uint64
    Uintptr
    Float32
    Float64
    Complex64
    Complex128
    Array
    Chan
    Func
    Interface
    Map
    Ptr
    Slice
    String
    Struct
    UnsafePointer
)
```

```
package main

import (
    "fmt"
    "reflect"
)

func main() {
    var x float64 = 3.4
    fmt.Println("type:", reflect.TypeOf(x))
    v := reflect.ValueOf(x)
    fmt.Println("value:", v)
    fmt.Println("type:", v.Type())
    fmt.Println("kind:", v.Kind())
    fmt.Println("value:", v.Float())
    fmt.Println(v.Interface())
    fmt.Printf("value is %5.2e\n", v.Interface())
    y := v.Interface().(float64)
    fmt.Println(y)
}

/* output:
type: float64
value: &lt;float64 Value&gt;
type: float64
kind: float64
value: 3.4
3.4
value is 3.40e+00
3.4
*/
```

知道x是一个float64类型的值，`reflect.ValueOf(x).float()`返回这个float64类型的实际值；同样的适用于`Int(), Bool(), Complex() ,String()`

#### 通过反射修改值

```
package main

import (
	"fmt"
	"reflect"
)

type User struct {
	Id   int
	Name string
	Age  int
}

func (u User) Hello(name string)  {
	fmt.Println("Hello", name, ", my name is ", u.Name)
}

func Set(o interface{}) {
	v := reflect.ValueOf(o)

	// 判断是否是预期类型以及是否可修改
	if v.Kind() == reflect.Ptr &amp;&amp; !v.Elem().CanSet() {
		fmt.Println("Not support")
		return
	} else {
		v = v.Elem()
	}
	// 判断是否有相应名称的字段
	f := v.FieldByName("Name")
	if !f.IsValid() {
		fmt.Println("Not valid")
	}
	// 重新修改值
	if f.Kind() == reflect.String {
		f.SetString("Bye")
	}
	// 判断是否有相应名称的方法并调用
	m := v.MethodByName("Hello")
	args := []reflect.Value{reflect.ValueOf("Joe")}
	m.Call(args) // Hello Joe , my name is  Bye
}

func main() {
	u := User{1, "OK", 12}
	Set(&amp;u)
	fmt.Println(u) // {1 Bye 12}
}

```

反射中有些内容是需要用地址去改变它的状态的。

#### 反射结构

有些时候需要反射一个结构类型。NumField() 方法返回结构内的字段数量；可以通过一个 for 循环通过索引取得每个字段的值`Field(i)`。我们同样能够调用签名在结构上的方法，例如，使用索引 n 来调用:`Method(n).Call(nil)。`

```
package main

import (
	"fmt"
	"reflect"
)

type User struct {
	Id   int
	Name string
	Age  int
}

func (u User) Hello() {
	fmt.Println("Hello world.")
}

func Info(o interface{}) {
	t := reflect.TypeOf(o)
	fmt.Println("Type:", t.Name())

	// 判断是否是预期的数据类型
	if k := t.Kind(); k != reflect.Struct {
		fmt.Println("Not support kind!")
		return
	}

	// 获取字段的 Name，Type 和 val
	v := reflect.ValueOf(o)
	fmt.Println("Fields:")
	for i := 0; i &lt; t.NumField(); i++ {
		f := t.Field(i)
		val := v.Field(i)
		fmt.Printf("%6s: %v = %v\n", f.Name, f.Type, val)
	}

	// 获取方法的 Name，Type
	for i := 0; i &lt; t.NumMethod(); i++ {
		m := t.Method(i)
		fmt.Printf("%6s: %v\n", m.Name, m.Type)
	}
}
func main() {
	u := User{1, "OK", 12}
	Info(u)
}

/* Output:
Type: User
Fields:
    Id: int = 1
  Name: string = OK
   Age: int = 12
 Hello: func(main.User)
*/

```

但是如果尝试更改一个值，会得到一个错：

```
    panic: reflect.Value.SetString using value obtained using unexported field

```

这是因为结构中只有被导出字段(首字母大写)才是可设置的。

```
// reflect_struct2.go
package main

import (
    "fmt"
    "reflect"
)

type T struct {
    A int
    B string
}

func main() {
    t := T{23, "skidoo"}
    s := reflect.ValueOf(&amp;t).Elem()
    typeOfT := s.Type()
    for i := 0; i &lt; s.NumField(); i++ {
        f := s.Field(i)
        fmt.Printf("%d: %s %s = %v\n", i,
            typeOfT.Field(i).Name, f.Type(), f.Interface())
    }
    s.Field(0).SetInt(77)
    s.Field(1).SetString("Sunset Strip")
    fmt.Println("t is now", t)
}

/* Output:
0: A int = 23
1: B string = skidoo
t is now {77 Sunset Strip}
*/
```

#### 嵌套反射

```
package main

import (
	"fmt"
	"reflect"
)

type User struct {
	Id   int
	Name string
	Age  int
}

type Manager struct {
	User
	title string
}

func (u User) Hello() {
	fmt.Println("Hello world.")
}


func main() {
	m := Manager{User{1, "OK", 12}, "test"}
	t := reflect.TypeOf(m)
	fmt.Println("Type:", t.Name())
	for i := 0; i &lt; t.NumField(); i++ {
		fmt.Printf("%#v\n", t.Field(i))
	}
	fmt.Printf("%#v\n", t.FieldByIndex([]int{0, 1}))
}

/* Output:
Type: Manager
reflect.StructField{Name:"User", PkgPath:"", Type:(*reflect.rtype)(0x490160), Tag:"", Offset:0x0, Index:[]int{0}, Anonymous:true}
reflect.StructField{Name:"title", PkgPath:"main", Type:(*reflect.rtype)(0x486b80), Tag:"", Offset:0x20, Index:[]int{1}, Anonymous:false}
reflect.StructField{Name:"Name", PkgPath:"", Type:(*reflect.rtype)(0x486b80), Tag:"", Offset:0x8, Index:[]int{1}, Anonymous:false}
*/

```

## 协程与通道

同步

```
package main

import (
	"fmt"
)

func main() {
	c := make(chan bool) // 通过 make 来创建，默认双向通道
	go func() {
		fmt.Println("Go Go Go!!!")
		c &lt;- true
		close(c) // 通过 close 来关闭
	}()
	for v := range c { // 使用 for range 来迭代不断操作 channel
		fmt.Println(v) // true
	}
}

```

```
package main

import (
	"fmt"
)

func main() {
	//c := make(chan bool) // 无缓存同步阻塞
	c := make(chan bool, 1) // 有缓存异步
	go func() {
		fmt.Println("Go Go Go!!!")
		&lt;- c
	}()
	c &lt;- true
}

```

```
package main

import (
	"fmt"
	"runtime"
	"sync"
)

func Go(wg *sync.WaitGroup, index int) {
	a := 1
	for i := 0; i &lt; 1000; i++ {
		a += i
	}

	fmt.Println(index, a)
	wg.Done() // 标记待完成任务数
}

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())
	wg := sync.WaitGroup{}
	wg.Add(10)
	//c := make(chan bool)
	for i := 0; i &lt; 10; i++ {
		go Go(&amp;wg, i)
	}
	wg.Wait() // 等待任务组任务都完成再退出
}
```

超时

```
package main

import (
	"fmt"
	"time"
)

func main() {
	c := make(chan int)

	select {
	case v := &lt;-c:
		fmt.Println(v)
	case &lt;- time.After(3 * time.Second):
		fmt.Println("Timeout!") // 3秒后打印退出
	}
}

```

通信

```
package main

import (
	"fmt"
	"time"
)

var c = make(chan int)

func Ping() {
	for {
		v1 := &lt;-c
		fmt.Printf("Ping: %d\n", v1)
		c &lt;- v1 + 1
		time.Sleep(time.Second)
	}
}

func Pang()  {
	for {
		v2 := &lt;-c
		fmt.Printf("Pang: %d\n", v2)
		c &lt;- v2 + 10
		time.Sleep(time.Second)
	}
}
func main() {
	go Ping()
	c &lt;- 0
	Pang()
}

```

## 日志

```
package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	logFile, err := os.OpenFile("./test.log", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0644)
	if err != nil {
		fmt.Println("open log file failed, err:", err)
		return
	}
	log.SetOutput(logFile)                       // 设置日志输出目的地，默认标准输出。
	log.SetFlags(log.LstdFlags | log.Lshortfile) // 设置日志输出选项
	log.SetPrefix("[Looking]")            // 设置日志前缀
	log.Println("这是一条很普通的日志。")      // [Looking]2023/10/09 19:17:09 main.go:17: 这是一条很普通的日志。
	v := "很普通的"
	log.Printf("这是一条%s日志。\n", v)
	log.Fatalln("这是一条会触发fatal的日志。")
	log.Panicln("这是一条会触发panic的日志。")

	logger := log.New(os.Stdout, "[prefix]", log.Lshortfile|log.Ldate|log.Ltime)
	logger.Println("这是自定义的logger记录的日志。")
}

```


