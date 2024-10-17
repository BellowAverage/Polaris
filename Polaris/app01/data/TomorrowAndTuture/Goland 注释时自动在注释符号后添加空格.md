
--- 
title:  Goland 注释时自动在注释符号后添加空格 
tags: []
categories: [] 

---
不得不说 JetBrains 旗下的 IDE 都好用，而且对于注释这块，使用 Ctrl + / 进行注释的时候，大多会在每个注释符号后统一添加一个空格，比如 PyCharm 和 RubeMine 等。

```
# PyCharm
# print("hello world")
```

```
# RubyMine
# require 'yaml'
#
# puts "hello world"

```

但最近终于碰到了一个例外，那就是 GoLand，你进行行注释的时候，它默认是不会加空格的，就像下边这种（至于它为什么默认设置成不加我也不想多探究）：

```
//package main
//
//import (
//	"fmt"
//)
//
//func main() {
//	fmt.Println("hello world")
//}

```

看起来很难看，对于强迫症患者绝对是忍不了的。那么，怎么设置成注释后会自动添加空格呢？

重点来了，行注释后自动添加空格：
- **`Preference -&gt; Editor -&gt; Code Style -&gt; Go`**- **`Add leading space to comments` 前打勾勾**
<img alt="" height="920" src="https://img-blog.csdnimg.cn/14d81fa8ea154c208a507ea045bd0dfd.png" width="1200">

 再进行多行注释，看起来就舒服多了。

```
// package main
// 
// import (
// 	"fmt"
// )
// 
// func main() {
// 	fmt.Println("hello world")
// }

```
