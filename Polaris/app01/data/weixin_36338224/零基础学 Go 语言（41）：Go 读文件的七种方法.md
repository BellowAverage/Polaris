
--- 
title:  零基础学 Go 语言（41）：Go 读文件的七种方法 
tags: []
categories: [] 

---
查看本系列教程目录，请点击 

Go 中对文件内容读写的方法，非常地多，其中大多数是基于 os 库的高级封装，不同的库，适用的场景又不太一样，为免新手在这块上裁跟头，我花了点时间把这些内容梳理了下。

这篇是上篇，先介绍读取文件的 9 种方法，过两天再介绍写文件的。

<img src="https://img-blog.csdnimg.cn/img_convert/2bff01afc6089df0c0eae6cdedf1bb09.png" alt="">

### 1. 整个文件读取入内存

直接将数据直接读取入内存，是效率最高的一种方式，但此种方式，仅适用于小文件，对于大文件，则不适合，因为比较浪费内存。

#### 1.1 直接指定文件名读取

有两种方法

**第一种：使用 os.ReadFile**

```
package main

import (
	"fmt"
	"os"
)

func main() {
	content, err := os.ReadFile("a.txt")
	if err != nil {
		panic(err)
	}
	fmt.Println(string(content))
}


```

**第二种：使用 ioutil.ReadFile**

```
package main

import (
	"io/ioutil"
	"fmt"
)

func main() {
	content, err := ioutil.ReadFile("a.txt")
	if err != nil {
		panic(err)
	}
	fmt.Println(string(content))
}


```

其实在 Go 1.16 开始，ioutil.ReadFile 就等价于 os.ReadFile，二者是完全一致的

```
// ReadFile reads the file named by filename and returns the contents.
// A successful call returns err == nil, not err == EOF. Because ReadFile
// reads the whole file, it does not treat an EOF from Read as an error
// to be reported.
//
// As of Go 1.16, this function simply calls os.ReadFile.
func ReadFile(filename string) ([]byte, error) {
	return os.ReadFile(filename)
}


```

#### 1.2 先创建句柄再读取

如果仅是读取，可以使用高级函数 os.Open

```
package main

import (
"os"
"io/ioutil"
"fmt"
)

func main() {
	file, err := os.Open("a.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()
	content, err := ioutil.ReadAll(file)
	fmt.Println(string(content))
}


```

之所以说它是高级函数，是因为它是只读模式的 os.OpenFile

```
// Open opens the named file for reading. If successful, methods on
// the returned file can be used for reading; the associated file
// descriptor has mode O_RDONLY.
// If there is an error, it will be of type *PathError.
func Open(name string) (*File, error) {
	return OpenFile(name, O_RDONLY, 0)
}


```

因此，你也可以直接使用 os.OpenFile，只是要多加两个参数

```
package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	file, err := os.OpenFile("a.txt", os.O_RDONLY, 0)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	content, err := ioutil.ReadAll(file)
	fmt.Println(string(content))
}



```

### 2. 每次只读取一行

一次性读取所有的数据，太耗费内存，因此可以指定每次只读取一行数据。方法有三种：
1. bufio.ReadLine()1. bufio.ReadBytes(’\n’)1. bufio.ReadString(’\n’)
在 bufio 的源码注释中，曾说道 bufio.ReadLine() 是低级库，不太适合普通用户使用，更推荐用户使用 bufio.ReadBytes 和 bufio.ReadString 去读取单行数据。

因此，这里不再介绍 bufio.ReadLine()

#### 2.1 使用 bufio.ReadBytes

```
package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	// 创建句柄
	fi, err := os.Open("christmas_apple.py")
	if err != nil {
		panic(err)
	}

	// 创建 Reader
	r := bufio.NewReader(fi)

	for {
		lineBytes, err := r.ReadBytes('\n')
		line := strings.TrimSpace(string(lineBytes))
		if err != nil &amp;&amp; err != io.EOF {
			panic(err)
		}
		if err == io.EOF {
			break
		}
		fmt.Println(line)
	}
}


```

#### 2.2 使用 bufio.ReadString

```
package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	// 创建句柄
	fi, err := os.Open("a.txt")
	if err != nil {
		panic(err)
	}

	// 创建 Reader
	r := bufio.NewReader(fi)

	for {
		line, err := r.ReadString('\n')
		line = strings.TrimSpace(line)
		if err != nil &amp;&amp; err != io.EOF {
			panic(err)
		}
		if err == io.EOF {
			break
		}
		fmt.Println(line)
	}
}


```

### 3. 每次只读取固定字节数

每次仅读取一行数据，可以解决内存占用过大的问题，但要注意的是，并不是所有的文件都有换行符 `\n`。

因此对于一些不换行的大文件来说，还得再想想其他办法。

通用的做法是：
- 先创建一个文件句柄，可以使用 os.Open 或者 os.OpenFile- 然后 bufio.NewReader 创建一个 Reader- 然后在 for 循环里调用 Reader 的 Read 函数，每次仅读取固定字节数量的数据。
```
package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

func main() {
	// 创建句柄
	fi, err := os.Open("a.txt")
	if err != nil {
		panic(err)
	}

	// 创建 Reader
	r := bufio.NewReader(fi)

	// 每次读取 1024 个字节
	buf := make([]byte, 1024)
	for {
		n, err := r.Read(buf)
		if err != nil &amp;&amp; err != io.EOF {
			panic(err)
		}

		if n == 0 {
			break
		}
		fmt.Println(string(buf[:n]))
	}
}


```
