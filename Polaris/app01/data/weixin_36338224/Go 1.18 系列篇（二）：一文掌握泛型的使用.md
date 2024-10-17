
--- 
title:  Go 1.18 系列篇（二）：一文掌握泛型的使用 
tags: []
categories: [] 

---
>  
 微信搜索 “写点代码的明哥”，关注更多关于 Go 与 K8S 的干货文章 


系列导读： 1、

泛型，可以说是 Go 这几年来最具争议的功能，应该没人有意见吧？

其实 Go 在早前的 Beta 版本中，就提供了对泛型的支持，但还不够成熟，直到 Go 1.18 才是支持泛型的正式版本。

下面我学习了官方关于泛型的文档之后，将学习的心得总结分享给大家

### 1. 非泛型的写法

现有一个 map ，我们需要实现一个函数，来遍历该 map 然后将 value 的值全部相加并返回。

而由于这个 map 的 value 可以是任意类型的数值，比如 int64, float64

于是为了接收不同类型的 map，我们就得定义多个函数，这些函数 **除了入参类型及返回值类型不同外，没有任何不同**

```
func SumInts(m map[string]int64) int64 {
    var s int64
    for _, v := range m {
        s += v
    }
    return s
}

func SumFloats(m map[string]float64) float64 {
    var s float64
    for _, v := range m {
        s += v
    }
    return s
}


```

### 2. 用泛型的写法

若是以代码行数来定义工作量，我可不希望泛型的出现，但从另一方面来讲，这种代码横看竖看都让人非常不舒服。

同样的需求，在有了泛型之后，写法就变得简洁许多, 两个函数可以简化成一个函数

```
func SumIntsOrFloats[K comparable, V int64 | float64](m map[K]V) V {
    var s V
    for _, v := range m {
        s += v
    }
    return s
}


```

在这个函数中，它比常规的函数多了 `[K comparable, V int64 | float64]` 这么一段代码，这便是 **泛型新增的语法**，位于函数名与形参之间。

我来解释下这段 “代码”：
- K 和 V 你可以理解为类型别名，在中括号之间进行定义，作用域也只在此函数内，可以在形参、函数主体、返回值类型 里使用- comparable 是 Go 语言预声明的类型，是那些可以比较（可哈希）的类型的集合，通常用于定义 map 里的 key 类型- int64 | float64 意思是 V 可以是 int64 或 float64 中的任意一个- map[K]V 就是使用了 K 和 V 这两个别名类型的 map
有了泛型函数的定义，那如何调用该函数？

调用方式还是跟普通函数一样，只是在函数名和实参之间，可以再次使用中括号来指明上面的 K 和 V 分别是什么类型？

```
func main() {
    // Initialize a map for the integer values
    ints := map[string]int64{
        "first": 34,
        "second": 12,
    }

    // Initialize a map for the float values
    floats := map[string]float64{
        "first": 35.98,
        "second": 26.99,
    }

    fmt.Printf("Generic Sums: %v and %v\n",
        SumIntsOrFloats[string, int64](ints),
        SumIntsOrFloats[string, float64](floats),
    )
}


```

最后使用 go run 去跑一下，结果正常输出

<img src="https://img-blog.csdnimg.cn/img_convert/e8a089b3fb18ef99dd3441e9bae18164.png" alt="">

### 3. 简化泛型写法

#### 3.1 类型自动推导

在调用大部分的泛型函数时，中括号里的内容，是可以省略不写的，而这个不写的前提是，编译器有办法根据你的实参及形参来自动推导出泛型函数中 别名类型对应的类型（在上例中就是 K 和 V）。

而在上面的例子中，刚好是满足的，于是泛型函数的调用就可以简化成这样

```
    fmt.Printf("Generic Sums: %v and %v\n",
        SumIntsOrFloats(ints),
        SumIntsOrFloats(floats),
    )


```

#### 3.2 使用类型别名

上面的 V 使用 `int64 | float64` 这样的写法来表示 V 可以是其中的任意一种类型。

若这个 V 用得比较多呢？可以考虑用 type 来事先定义别名,一来方便复用，二来在泛型函数使用更加简短的别名，可以提高代码可读性

```
type Number interface {
    int64 | float64
}


```

然后泛型函数的定义就可以简化成下面这样

```
func SumNumbers[K comparable, V Number](m map[K]V) V {
    var s V
    for _, v := range m {
        s += v
    }
    return s
}


```

### 4. 写在最后

在去年，其实就通过其他人的文章中事先了解到了 Go 泛型的写法，给我的第一印象是，函数的定义变得更复杂，可读性也越来越差，一时间我也有点难以接受。

不过经过自己试用后，情况倒没有我想象的那么糟糕！新版没有改变原有函数的定义与调用，若你没有使用泛型，那么有没有泛型对你来说没有区别。

但即使你有想法需要用到泛型，我也相信这种的不适感会在时间的流逝中慢慢淡化。

由于泛型改动太大，目前 Goland 的 EAP 对泛型的支持还有很多 bug ，该检测出的语法错误没有被检测出来，正确的语法被视为错误标红之类，想用在 Goland 中使用泛型，需要有这个意识​，否则严重影响写代码的流畅度，容易被错误的提示打断了思路。

<img src="https://img-blog.csdnimg.cn/898b64e4ac064b4989f18bf8afbaba31.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5YaZ5Luj56CB55qE5piO5ZOl,size_20,color_FFFFFF,t_70,g_se,x_16" alt="">
