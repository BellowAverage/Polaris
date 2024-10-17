
--- 
title:  Go 1.18 系列篇（四）：一文掌握 Fuzzing 模糊测试 
tags: []
categories: [] 

---
>  
 微信搜索 “写点代码的明哥”，关注更多关于 Go 与 K8S 的干货文章 


系列导读： 1、 2、 3、

### 1. 什么是模糊测试？

单元测试，大家应该都写过吧？单元测试，需要开发者根据函数逻辑，给定几组输入（入参）与输出（返回）的数据，然后 go test 根据这些数据集，调用函数，若返回值与预期相符，则说明函数的单元测试通过。

但单元测试的代码，也是由开发者写的一段一段代码，只要是代码，就会有 BUG，就会有遗漏的场景。

因此即使单元测试通过，也不代表你的程序没有问题。

可见，测试场景的数据集对于测试有多重要，而 Fuzzing 模糊测试就是一种用机器根据已知数据源，来自动生成测试数据的一种方案。

本文借用官方的一个例子来讲解。

### 2. 简单的示例

在开始之前，先初始化项目

```
go mod init github.com/iswbm/fuzz


```

然后在该项目中添加 main.go，内容如下

```
package main

import "fmt"

func Reverse(s string) string {
    b := [] byte(s)
    for i, j := 0, len(b)-1; i &lt; len(b)/2; i, j = i+1, j-1 {
        b[i], b[j] = b[j], b[i]
    }
    return string(b)
}

func main() {
    input := "The quick brown fox jumped over the lazy dog"
    rev := Reverse(input)
    doubleRev := Reverse(rev)
    fmt.Printf("original: %q\n", input)
    fmt.Printf("reversed: %q\n", rev)
    fmt.Printf("reversed again: %q\n", doubleRev)
}


```

现在我们要为 Reverse 函数编写单元测试代码，放在 reverse_test.go，Test 函数如下
- 给定了三组数据- 遍历这几组数据，将 tc.in 做为 Reverses 函数的入参执行函数，其返回值跟预期的 tc.want 做对比- 若不相等，则测试不通过～
```
package main

import (
    "testing"
)

func TestReverse(t *testing.T) {
    testcases := []struct {
        in, want string
    }{
        {"Hello, world", "dlrow ,olleH"},
        {" ", " "},
        {"!12345", "54321!"},
    }
    for _, tc := range testcases {
        rev := Reverse(tc.in)
        if rev != tc.want {
                t.Errorf("Reverse: %q, want %q", rev, tc.want)
        }
    }
}


```

现在我们执行 go test 即是普通的单元测试，输出 PASS 说明单元测试通过，到目前为止是 Go 1.18 之前的单元测试

<img src="https://img-blog.csdnimg.cn/img_convert/f32c56b9362776f64119bafbcfd009d2.png" alt="">

然后我们再往 reverse_test.go 中加入 Fuzzing 模糊测试的代码

```
// 记得前面导入 "unicode/utf8" 包

func FuzzReverse(f *testing.F) {
    testcases := []string{"Hello, world", " ", "!12345"}
    for _, tc := range testcases {
        f.Add(tc)  // Use f.Add to provide a seed corpus
    }
    f.Fuzz(func(t *testing.T, orig string) {
        rev := Reverse(orig)
        doubleRev := Reverse(rev)
        if orig != doubleRev {
            t.Errorf("Before: %q, after: %q", orig, doubleRev)
        }
        if utf8.ValidString(orig) &amp;&amp; !utf8.ValidString(rev) {
            t.Errorf("Reverse produced invalid UTF-8 string %q", rev)
        }
    })
}


```

Fuzzing 模糊测试的代码格式与单元测试很像：
- 函数名固定以 Fuzz 开头（单元测试是以 Test 开头）- 函数固定以 *testing.F 类型做为入参（单元测试是以 *testing.T）
不一样的是 Fuzzing 模糊测试，提供两个函数：
- t.Add：用于开发者输入模糊测试的种子数据，fuzzing 根据这些种子数据，自动随机生成更多测试数据- t.Fuzz：开始运行模糊测试，t.Fuzz 的入参是一个 Fuzz Target 函数（官方这么叫的），这个 Fuzz Target 函数的编写逻辑跟单元测试就一样了
在本例子中，Fuzz Target 接收 类型为 string 的入参，做为 Reverse 的输入源，然后利用两次 Reverse 的结果应与原字符串相等的原理进行测试。

有了 FuzzReverse 函数后，就可以使用如下命令进行模糊测试

```
go18 test -fuzz=Fuzz


```

通过输出发现测试并不顺利，Go 1.18 的 Fuzzing 会将导致测试异常的数据文件记录下来，使用 cat 可以查看该测试数据

<img src="https://img-blog.csdnimg.cn/img_convert/8ed7f952dda6478c0a632beef7ed39e2.png" alt="">

记录下来后，该数据就可做为普通单元测试的数据，此时我们再执行 go test 就会引用该数据，当然了，在问题解决之前， go test 会一直报错

<img src="https://img-blog.csdnimg.cn/img_convert/0d07be4885fa0282c8401ede225add4c.png" alt="">

### 3. 问题排查与解决

模糊测试帮我们发现了一个出乎意料的 Bug 场景：在中文里的字符 `泃`其实是由3个字节组成的，如果按照字节反转，反转后得到的就是一个无效的字符串。

因此为了保证字符串反转后得到的仍然是一个有效的UTF-8编码的字符串，我们要按照`rune`进行字符串反转。

为了更好地方便大家理解中文里的字符 `泃`按照`rune`为维度有多少个`rune`，以及按照byte反转后得到的结果长什么样，我们对代码做一些修改。

<img src="https://img-blog.csdnimg.cn/img_convert/3d82cc52a31a919cd7f793ccbec8ddeb.png" alt="">

改完之后，再次执行 go test 就会提示测试成功，说明我们已经修复上面的那个场景的 BUG

<img src="https://img-blog.csdnimg.cn/img_convert/45de4c9c1cd24e924f77267c0957974d.png" alt="">

当下我们已经发现并修复了一个 BUG，程序肯定还有更多 BUG 存在，要继续寻找可以再次进行模糊测试，重复上面的步骤即可，这里不再赘述。

### 4. 更多参数介绍

在支持了 Fuzzing 模糊测试后，go test 工具也有了一些新的命令，在这里一并记录下

**进行模糊测试**

```
go test -fuzz=Fuzz


```

**只对某个函数进行模糊测试**：使用 -run=Fuzzxxx 或者 -fuzz=Fuzzxxx 指定模糊测试函数，避免执行到其他测试函数

```
go18 test -run=FuzzReverse
go18 test -fuzz=FuzzReverse


```

**测试某个失败数据**：使用 -run=file 指定数据文件

```
go test -run=FuzzReverse/1fdd0160e6b3dd8f1e6b7a4179b4787e0c014cf9c46c67a863d71e3a0277c213


```

**指定模糊测试的时间**：使用 -fuzztime 指定模糊测试时间或者迭代次数（默认无限期），避免一直在跑测试无法退出

还有一个 -fuzzminimizetime 参数，看官方文档的介绍，我没明白其作用，有知道的还请评论区分享下

```
go test -fuzz=Fuzz -fuzztime 30s


```

**设置模糊测试进程数据**：默认值是 $GOMAXPROCS，可根据实际情况进行设置，避免太占用机器的资源

```
go test -fuzz=Fuzz -parallel 4


```

### 5. 写在最后

模糊测试的存在，并不是为了替代原单元测试，而是为单元测试提供更好的保障，是一个补充方案，而非替代方案。

单元测试的局限性在于，你只能用预期的输入进行测试；模糊测试在发现暴露出奇怪行为的意外输入方面非常出色。一个好的模糊测试系统也会对被测试的代码进行分析，因此它可以有效地产生输入，从而扩大代码覆盖面。

同时模糊测试的适用场景也比较有限，如果函数的入参并不是像本例中的那样的简单（字符串），而是各种对象呢？可能它就无能为力了吧。 <img src="https://img-blog.csdnimg.cn/898b64e4ac064b4989f18bf8afbaba31.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5YaZ5Luj56CB55qE5piO5ZOl,size_20,color_FFFFFF,t_70,g_se,x_16" alt="">
