
--- 
title:  Go 之 fmt 格式化输入输出 
tags: []
categories: [] 

---
## 向外输出

### Print

`Print`系列函数会将内容输出到系统的标准输出，区别在于`Print`函数直接输出内容，`Printf`函数支持格式化输出字符串，`Println`函数会在输出内容的结尾添加一个换行符。

```
package main

import (
	"fmt"
)

func main() {
	// Print、Printf、Println
	fmt.Print("在终端打印该信息。") // 内容输出到标准输出
	name := "Looking"
	fmt.Printf("我是：%s\n", name) // 支持格式化输出
	fmt.Println("在终端打印单独一行显示")
}
```

```
在终端打印该信息。我是：Looking
在终端打印单独一行显示
```

### Fprint

`Fprint`系列函数（Fprint、Fprintf、Fprintln）与 Print 系列函数（Print、Printf、Println）类似，只不过会将内容输出到一个`io.Writer`接口类型的变量`w`中，我们通常用这个函数往文件中写入内容。只要满足`io.Writer`接口的类型都支持写入。

```
package main

import (
	"fmt"
	"os"
)

func main() {
	// Fprint、Fprintf、Fprintln
	name := "Looking"
	fmt.Fprint(os.Stdout, "向标准输出写入内容且不换行！")
	fmt.Fprintln(os.Stdout, "向标准输出写入内容且换行！")
	fileObj, err := os.Create("./test.txt")
	if err != nil {
		fmt.Println("打开文件出错，err:", err)
		return
	}

	fmt.Fprintf(fileObj, "往文件中写如信息：%s", name) // 往文件对象输出
	// 文件: test.txt
	// 内容：往文件中写如信息：Looking
}
```

```
向标准输出写入内容且不换行！向标准输出写入内容且换行！
```

### Sprint

`Sprint`系列函数（Sprint、Sprintf、Sprintln）与 Print 系列函数（Print、Printf、Println）类似，只不过不会直接输出，而是会把传入的数据生成并返回一个字符串。

```
package main

import (
	"fmt"
)

func main() {
	// Sprint、Sprintf、Sprintln
	name := "Looking"
	s1 := fmt.Sprint(name) // 返回字符串，字符串末尾不会自动添加换行符
	fmt.Print(s1)
	s2 := fmt.Sprintln(name) // 返回字符串，字符串末尾会自动添加换行符
	fmt.Print(s2)
	age := 18
	s3 := fmt.Sprintf("name:%s, age:%d", name, age) // 返回格式化后字符串
	fmt.Print(s3)
}
```

```
LookingLooking
name:Looking, age:18
```

### Errorf

`Errorf`函数根据format参数生成格式化字符串并返回一个包含该字符串的错误。

```
package main

import (
	"errors"
	"fmt"
)

func main() {
	// Errorf
	e := errors.New("原始错误e")
	w := fmt.Errorf("Wrap了一个错误:%w", e) // Wrap了一个错误:原始错误e
	fmt.Println(w.Error())
}
```

## 获取输入

### Scan

Scan从标准输入扫描文本。

```
package main

import (
	"fmt"
)

func main() {
	var (
		name    string
		age     int
		married bool
	)
	fmt.Scan(&amp;name, &amp;age, &amp;married) // 读取由空白符分隔的值保存到传递给本函数的参数中，换行符视为空白符。
	fmt.Printf("扫描结果 name:%s age:%d married:%t \n", name, age, married)
	// 输入：Looking 29 true
	// 输出：扫描结果 name:Looking age:29 married:true
	fmt.Scanf("1:%s 2:%d 3:%t", &amp;name, &amp;age, &amp;married) // 根据format参数指定的格式去读取值保存到传递给本函数的参数中。
	fmt.Printf("扫描结果 name:%s age:%d married:%t \n", name, age, married)
	// 输入：1:Looking 2:29 3:true
	// 输出：扫描结果 name:Looking age:29 married:true
	fmt.Scanln(&amp;name, &amp;age, &amp;married) // Scanln类似Scan，它在遇到换行时才停止扫描。
	fmt.Printf("扫描结果 name:%s age:%d married:%t \n", name, age, married)
	// 输入：Looking 29 true
	// 输出：扫描结果 name:Looking age:29 married:true
}

```

### Fscan

这几个函数功能分别类似于`fmt.Scan`、`fmt.Scanf`、`fmt.Scanln`三个函数，只不过它们不是从标准输入中读取数据而是从`io.Reader`中读取数据。

```
package main

import (
	"fmt"
	"os"
)

func main() {
	var (
		name    string
		age     int
		married bool
	)
	fileObj, err := os.OpenFile("./test.txt", os.O_RDONLY, 0644)
	if err != nil {
		fmt.Println("打开文件出错，err:", err)
		return
	}
	fmt.Fscan(fileObj, &amp;name, &amp;age, &amp;married)
	fmt.Printf("扫描结果 name:%s age:%d married:%t \n", name, age, married)
	// test.txt：Looking 29 true
	// 输出：扫描结果 name:Looking age:29 married:true
	fmt.Fscanf(fileObj, "1:%s 2:%d 3:%t", &amp;name, &amp;age, &amp;married)
	fmt.Printf("扫描结果 name:%s age:%d married:%t \n", name, age, married)
	// test.txt：1:Looking 2:29 3:true
	// 输出：扫描结果 name:Looking age:29 married:true
	fmt.Fscanln(fileObj, &amp;name, &amp;age, &amp;married)
	fmt.Printf("扫描结果 name:%s age:%d married:%t \n", name, age, married)
	// test.txt：Looking 29 true
	// 输出：扫描结果 name:Looking age:29 married:true
}

```

### Sscan

这几个函数功能分别类似于`fmt.Scan`、`fmt.Scanf`、`fmt.Scanln`三个函数，只不过它们不是从标准输入中读取数据而是从指定字符串中读取数据。

```
package main

import (
	"fmt"
)

func main() {
	var (
		name    string
		age     int
		married bool
	)

	fmt.Sscan("Looking 29 true", &amp;name, &amp;age, &amp;married)
	fmt.Printf("扫描结果 name:%s age:%d married:%t \n", name, age, married)
	// 输入：Looking 29 true
	// 输出：扫描结果 name:Looking age:29 married:true
	fmt.Sscanf("1:Looking 2:29 3:true", "1:%s 2:%d 3:%t", &amp;name, &amp;age, &amp;married)
	fmt.Printf("扫描结果 name:%s age:%d married:%t \n", name, age, married)
	// 输入：1:Looking 2:29 3:true
	// 输出：扫描结果 name:Looking age:29 married:true
	fmt.Sscanln("Looking 29 true", &amp;name, &amp;age, &amp;married)
	fmt.Printf("扫描结果 name:%s age:%d married:%t \n", name, age, married)
	// 输入：Looking 29 true
	// 输出：扫描结果 name:Looking age:29 married:true
}

```

### NewReader

完整获取输入的内容并裁剪首尾空格

```
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin) // 从标准输入生成读对象
	fmt.Print("请输入内容：")
	text, _ := reader.ReadString('\n') // 读到换行，分隔符后面的内容被忽略
	text = strings.TrimSpace(text) // 字符串头尾的空格会被移除
	fmt.Printf("%#v\n", text)
}

```

```
请输入内容：  hello world   
"hello world"
```

## 格式化输出

### 常用占位符

 常用格式化字符转义表

```
verb            描述
 
%+v    添加字段名(如结构体)
%#v　  相应值的Go语法表示 
%T     相应值的类型的Go语法表示 
%%     字面上的百分号，并非值的占位符　
%t     true 或 false
%b     二进制表示 
%c     相应Unicode码点所表示的字符 
%d     十进制表示 
%o     八进制表示 
%x     十六进制表示，字母形式为小写 a-f 
%X     十六进制表示，字母形式为大写 A-F 
%U     Unicode格式：U+1234，等同于 "U+%04X"
%b     无小数部分的，指数为二的幂的科学计数法
%e     科学计数法，例如 -1234.456e+78 
%E     科学计数法，例如 -1234.456E+78 
%f     有小数点而无指数，例如 123.456 
%g     根据情况选择 %e 或 %f 以产生更紧凑的（无末尾的0）输出 
%G     根据情况选择 %E 或 %f 以产生更紧凑的（无末尾的0）输出
%s     字符串或切片的无解译字节 
%q     双引号围绕的字符串，由Go语法安全地转义 
%p     十六进制表示，前缀 0x (用于指针)
```

### 通用占位符

简单理解，占位符 %v，% 和 v 中间的 + 越多，输出的结果越详细。

<th style="width:124px;">占位符</th><th style="width:564px;">说明</th>
|------
<td style="width:124px;">%v</td><td style="width:564px;">值的默认格式表示</td>
<td style="width:124px;">%+v</td><td style="width:564px;">类似%v，但输出结构体时会添加字段名（详细一些）</td>
<td style="width:124px;">%#v</td><td style="width:564px;">值的Go语法表示（更详细一些）</td>
<td style="width:124px;">%T</td><td style="width:564px;">打印值的类型</td>
<td style="width:124px;">%%</td><td style="width:564px;">百分号</td>

```
package main

import (
	"fmt"
)

func main() {
	fmt.Printf("%v\n", 100)   // 100
	fmt.Printf("%v\n", false) // false
	o := struct {
		name string
	}{"Looking"}
	fmt.Printf("%v\n", o)  // 打印值，{Looking}
	fmt.Printf("%#v\n", o) // 打印值，struct { name string }{name:"Looking"}
	fmt.Printf("%+v\n", o) // 打印值，输出结构体会添加字段名称 {name:Looking}
	fmt.Printf("%T\n", o)  // 打印值的类型，struct { name string }
	fmt.Printf("100%%\n")  // 100%
}

```

### 布尔型占位符

|占位符|说明
|------
|%t|true或false

```
package main

import "fmt"

func main() {
	b := true
	fmt.Printf("%t\n", b) // true
}

```

### 浮点数与复数

|占位符|说明
|------
|%b|无小数部分、二进制指数的科学计数法，如-123456p-78
|%e|科学计数法，如-1234.456e+78
|%E|科学计数法，如-1234.456E+78
|%f|有小数部分但无指数部分，如123.456
|%F|等价于%f
|%g|根据实际情况采用%e或%f格式（以获得更简洁、准确的输出）
|%G|根据实际情况采用%E或%F格式（以获得更简洁、准确的输出）

```
package main

import "fmt"

func main() {
	f := 12.34
	fmt.Printf("%b\n", f) // 6946802425218990p-49
	fmt.Printf("%e\n", f) // 1.234000e+01
	fmt.Printf("%E\n", f) // 1.234000E+01
	fmt.Printf("%f\n", f) // 12.340000
	fmt.Printf("%g\n", f) // 12.34
	fmt.Printf("%G\n", f) // 12.34
}

```

###  字符串和[]byte

|占位符|说明
|------
|%s|直接输出字符串或者[]byte
|%q|该值对应的双引号括起来的go语法字符串字面值，必要时会采用安全的转义表示
|%x|每个字节用两字符十六进制数表示（使用a-f ）
|%X|每个字节用两字符十六进制数表示（使用A-F）

```
package main

import "fmt"

func main() {
	s := "Looking"
	fmt.Printf("%s\n", s) // Looking
	fmt.Printf("%q\n", s) // "Looking"
	fmt.Printf("%x\n", s) // 4c6f6f6b696e67
	fmt.Printf("%X\n", s) // 4C6F6F6B696E67
}

```

### 指针占位符

|占位符|说明
|------
|%p|表示为十六进制，并加上前导的0x

```
package main

import "fmt"

func main() {
	a := 10
	fmt.Printf("%p\n", &amp;a)  // 0xc0000aa058
	fmt.Printf("%#p\n", &amp;a) // c0000aa058
}

```

### 宽度标识符

宽度通过一个紧跟在百分号后面的十进制数指定，如果未指定宽度，则表示值时除必需之外不作填充。精度通过（可选的）宽度后跟点号后跟的十进制数指定。如果未指定精度，会使用默认精度；如果点号后没有跟数字，表示精度为0。举例如下：

|占位符|说明
|------
|%f|默认宽度，默认精度
|%9f|宽度9，默认精度
|%.2f|默认宽度，精度2
|%9.2f|宽度9，精度2
|%9.f|宽度9，精度0

```
package main

import "fmt"

func main() {
	n := 12.34
	fmt.Printf("%f\n", n)    // 12.340000
	fmt.Printf("%9f\n", n)   // 12.340000
	fmt.Printf("%.2f\n", n)  // 12.34
	fmt.Printf("%9.2f\n", n) //     12.34
	fmt.Printf("%9.f\n", n)  //        12
}

```

### 其他占位符

<th style="width:68px;">占位符</th><th style="width:620px;">说明</th>
|------
<td style="width:68px;">'+'</td><td style="width:620px;">总是输出数值的正负号；对%q（%+q）会生成全部是ASCII字符的输出（通过转义）；</td>
<td style="width:68px;">' '</td><td style="width:620px;">对数值，正数前加空格而负数前加负号；对字符串采用%x或%X时（% x或% X）会给各打印的字节之间加空格</td>
<td style="width:68px;">'-'</td><td style="width:620px;">在输出右边填充空白而不是默认的左边（即从默认的右对齐切换为左对齐）；</td>
<td style="width:68px;">'#'</td><td style="width:620px;">八进制数前加0（%#o），十六进制数前加0x（%#x）或0X（%#X），指针去掉前面的0x（%#p）对%q（%#q），对%U（%#U）会输出空格和单引号括起来的go字面值；</td>
<td style="width:68px;">'0'</td><td style="width:620px;">使用0而不是空格填充，对于数值类型会把填充的0放在正负号后面；</td>

```
package main

import "fmt"

func main() {
	s := "Looking"
	fmt.Printf("%s\n", s)      // 字符串输出
	fmt.Printf("%10s\n", s)    // 宽度10，右对齐
	fmt.Printf("%-10s\n", s)   // 宽度10，左对齐
	fmt.Printf("%10.5s\n", s)  // 宽度10，右对齐，截取前5位
	fmt.Printf("%-10.5s\n", s) // 宽度10，左对齐，截取前5位
	fmt.Printf("%10.2s\n", s)  // 宽度10，右对齐，截取前2位
	fmt.Printf("%010s\n", s)   // 宽度10，右对齐，左边使用0填充
}

```

```
Looking
   Looking
Looking   
     Looki
Looki     
        Lo
000Looking
```

## 基本数据类型与字符串转换 

### Atoi/Itoa

```
package main

import (
	"fmt"
	"strconv"
)

func main() {
	i := 123
	s := strconv.Itoa(i)
	fmt.Printf("type:%T value:%#v\n", s, s) // type:string value:"123"

	a, _ := strconv.Atoi("1234")
	fmt.Printf("type:%T value:%#v\n", a, a) // type:int value:1234
}

```

### 字符串解析（Parse系列函数）

```
package main

import (
	"fmt"
	"strconv"
)

func main() {
	b, _ := strconv.ParseBool("1")
	fmt.Printf("type:%T value:%#v\n", b, b) // type:string value:"123"

	i, _ := strconv.ParseInt("1A", 16, 32)   // base: 将字符串按照 base 进制进行解析
	fmt.Printf("type:%T value:%#v\n", i, i)  // type:int64 value:26
	fmt.Println(strconv.FormatInt(26, 2))    // 11010
	i2, _ := strconv.ParseInt("1A", 16, 4)   // bitSize: 若超过最大位数，显示能表示的最大值，有符号整形的符号位额外占一位。
	fmt.Printf("type:%T value:%v\n", i2, i2) // type:int64 value:7   解析结果为26，二进制形式长度加符号位限定为4位，结果显示为7（符号位额外占一位）

	i3, _ := strconv.ParseUint("1A", 16, 4)  // bitSize: 若超过最大位数，显示能表示的最大值。
	fmt.Printf("type:%T value:%v\n", i3, i3) // type:uint64 value:15 解析结果为26，二进制形式长度为5位，超过限定的4，结果显示为15

	f, _ := strconv.ParseFloat("3.1415926", 32) // bitSize 指定精度的浮点数，可以为 32 或 64.
	f2, _ := strconv.ParseFloat("3.1415926", 64)
	fmt.Printf("type:%T value:%#v\n", f, f)   // type:float64 value:3.141592502593994
	fmt.Printf("type:%T value:%#v\n", f2, f2) // type:float64 value:3.1415926
}

```

### 字符串转换（Format系列函数）

```
package main

import (
	"fmt"
	"strconv"
)

func main() {
	s1 := strconv.FormatBool(true)
	fmt.Printf("type:%T value:%#v\n", s1, s1) // type:string value:"true"
	s2 := strconv.FormatFloat(3.1415, 'E', -1, 64)
	fmt.Printf("type:%T value:%#v\n", s2, s2) // type:string value:"3.1415E+00"
	s3 := strconv.FormatInt(-123, 16)
	fmt.Printf("type:%T value:%#v\n", s3, s3) // type:string value:"-7b"
	s4 := strconv.FormatUint(123, 2)
	fmt.Printf("type:%T value:%#v\n", s4, s4) // type:string value:"1111011"
	s5 := strconv.FormatUint(123, 8)
	fmt.Printf("type:%T value:%#v\n", s5, s5) // type:string value:"173"
	s6 := strconv.FormatUint(123, 10)
	fmt.Printf("type:%T value:%#v\n", s6, s6) // type:string value:"123"
	s7 := strconv.FormatUint(123, 16)
	fmt.Printf("type:%T value:%#v\n", s7, s7) // type:string value:"7b"
	fmt.Println(strconv.IsPrint('好'))         // true
}

```

### 字符串追加（Append系列函数）

```
package main

import (
	"fmt"
	"strconv"
)

func main() {
	a := []byte("hello:")
	fmt.Println(string(a)) // hello:
	a = strconv.AppendBool(a, true)
	fmt.Println(string(a)) // hello:true
	a = strconv.AppendFloat(a, 3.14159, 'f', 4, 32) // f:以浮点数形式 e:科学记数法表示数字 g:自适应展示
	fmt.Println(string(a)) // hello:true3.1416
	a = strconv.AppendInt(a, 26, 2) // 将整形转换成2进制字符串追加
	fmt.Println(string(a)) // hello:true3.141611010
	a = strconv.AppendUint(a, 26, 16) // 将无符号整形转换成16进制字符串追加
	fmt.Println(string(a)) // hello:true3.1416110101a
	a = strconv.AppendQuote(a, "你") // 带引号的字符串追加
	fmt.Println(string(a)) // hello:true3.1416110101a"你"
	a = strconv.AppendQuoteRune(a, '好') // 带引号的字符追加
	fmt.Println(string(a)) // hello:true3.1416110101a"你"'好'
}

```

### 字符串和字节数组相互转换

```
package main

import (
	"fmt"
)

func main() {
	a := "hello "
	b := []byte{' ', 'w', 'o', 'r', 'l', 'd'}
	fmt.Println([]byte(a)) // [104 101 108 108 111 32]
	fmt.Println(string(b)) //  world
}
```
