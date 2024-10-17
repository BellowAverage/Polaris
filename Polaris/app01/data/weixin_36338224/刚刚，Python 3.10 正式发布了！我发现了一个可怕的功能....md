
--- 
title:  刚刚，Python 3.10 正式发布了！我发现了一个可怕的功能... 
tags: []
categories: [] 

---
就在前几天( 2021年10月4日) Python 终于正式发布了 3.10 版本，看了下这个版本的一些特性，最受关注的应该就是 **结构模式匹配** 了吧？也就是大家所熟悉的 ~~switch-case~~ ，写错了不好意思，是 match-case。

<img src="https://img-blog.csdnimg.cn/20211010220006939.png" alt="">

下边是最简单的一个 match-case 的例子，看起来是不是非常的直观简洁？

```
def http_error(status):
    match status:
        case 400:
            print("Bad request")
        case 404:
            print("Not found")
        case 418:
            print("I'm a teapot")
        case _:
            print("Something's wrong with the internet")
```

对这个功能满怀期待的我，赶紧就下载升级了 3.10 的 Python 赶紧试用，可没想到在我深入的体验过后，我从最开始的期待，变成了敬畏。

**敬畏**，是因为这样一个看似简单的新功能，却有着不少的学习成本，并且对 **结构模式匹配** 半知半解的人来说，会增大代码出错的概率，并不是大数人都能轻松驾驭的。

我为什么会这么说呢？我会在文章最后来简述我的观点。

鉴于大多数人，都没有实际用过这种 **结构模式匹配**，我会从 升级 3.10 开始教大家如何尝鲜这个新功能，然后我会详细的介绍 match-case 的使用方法。

#### 1. 升级 3.10 新版本

我本机的电脑上目前的 Python 版本是 3.9.1 的

```
$ /usr/local/bin/python3 --version
Python 3.9.1
```

由于这边我使用的是 mac，因此我从官网上下载的是 Python 3.10 的 pkg 文件，如果是 win 的用户，可以下载相应的 msi 或者 exe 文件。

下载链接我贴在下边，可以直接访问下载

```
mac: https://www.python.org/ftp/python/3.10.0/python-3.10.0-macos11.pkg
win: https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe
```

我下载好安装文件后，双击安装，之后就双击下载的 pkg 文件，进入安装流程

<img src="https://img-blog.csdnimg.cn/20211010220007386.png" alt="">

一路点击继续，该同意的同意一下，出现如下提示表示安装成功。

<img src="https://img-blog.csdnimg.cn/20211010220007825.png" alt="">

再次在终端上确认下是否升级成功

<img src="https://img-blog.csdnimg.cn/20211010220008145.png" alt="">

#### 2. or 模式的使用

在上面我已经贴出一个 match-case 的最简单示例，这边就直接跳过简单示例，来说说那些比较特殊的用法。

在 Python 3.10 中其实有新增一个 联合类型操作符 `|` ，但这个只能用于类型，具体的用法，我会在下一篇文章中做详细的介绍，本篇文章还是集中于 match-case 的使用。

在学习match-case 的时候，你会发现，也有一个类似于联合类型操作符的用法，但请你要注意区别，它并不是联合类型操作，而是在 match-case 下独有的 **or模式操作符** `|` ，它可以将多个具体相同逻辑的 case 语句简写成同一个

```
match status:
    case 401 | 403 | 404:
        print("Not allowed")
    case _:
        print("Something's wrong with the internet")
```

#### 3. 通配符匹配任意对象

match-case 的出现有利于提高代码的可读性，让你的代码更加优雅，但同时要使用好它，也是有一些门槛的，特别是通配符的使用。

下边我举一些例子来进行讲解

在如下代码中，使用了通配符 `_` 和 可变参数中的 `*` 符号

```
import sys

match sys.argv[1:]:
    case ["quit"]:
        print("exit")
    case ["create", user]:     # 创建单个用户
        print("create", user)
    case ["create", *users]:  # 批量创建多个用户
        for user in users:
            print("create", user)
    case _:
        print("Sorry, I couldn't understand the argv")
```

最后一个 case 中的 `_` 并不作为变量名，而表示一种特殊的模式，在前面的 case 中都未命中的情况下，该 case 会是最后的保障，能确保命中，它相当于 Go 语言中的 `default` 分支。

```
import "fmt"

func main() {
    education := "本科"

    switch education {
    case "博士":
        fmt.Println("我是博士")
    case "研究生":
        fmt.Println("我是研究生")
    case "本科":
        fmt.Println("我是本科生")
    case "大专":
        fmt.Println("我是大专生")
    default:
        fmt.Println("学历未达标..")
    }
}
```

#### 4. 使用可变参数 *args

第二个 case 和 第三个 case 非常的像，区别在于第三个 case中 `users` 前加了个 `*`，他跟原 Python 函数中的可变参数是一个用法，会匹配列表的多个值。

在该中表示可以从命令行参数中批量创建用户。

<img src="https://img-blog.csdnimg.cn/20211010220008420.png" alt="">

在 match-case 中相应的 case 若有运行到，对应的变量是会被创建的。比如

<img src="https://img-blog.csdnimg.cn/20211010220008724.png" alt="">

#### 5. 使用可变参数 **kv

在如下代码中，`**rest` 会匹配到所有的 args 中的 key 和 value

<img src="https://img-blog.csdnimg.cn/20211010220008985.png" alt="">

#### 6. 长度的匹配方式

若你希望使用 case 仅对对象的长度做一些匹配，可以使用下面这样的方式
- `[*_]` 匹配任意长度的 `list`;- `(_, _, *_)` 匹配长度至少为 2 的 `tuple`。
#### 7. 类对象的匹配

对于类对象的匹配，下边这个例子足够简单，不再讲解。

<img src="https://img-blog.csdnimg.cn/20211010220009315.png" alt="">

#### 8. 匹配要注意顺序

在上边基本介绍完了 match-case 的使用方法，如需更详细的内容，不如去通读下  的内容。

在文章最开始的时候，我说过开发者应该对这些新特性 **心存敬畏**，match-case 这样一个看似简单的新功能，却有着不少的学习成本，如果对 **结构模式匹配** 半知半解的人来说，可能会增大代码出错的概率，并不是大数人都能轻松驾驭的。

之所以会这么说，是因为 match-case 在面对不同的对象，它的匹配的规则也有所不同。
- 当 match 的对象是一个 list 或者 tuple 的时候，需要长度和元素值都能匹配，才能命中，这就是为什么下面这个例子走的是第三个 case 而不是第二个 case。
<img src="https://img-blog.csdnimg.cn/20211010220009620.png" alt="">
- 当 match 的对象是一个 dict 的时候，规则却有所不同，只要 case 表达式中的 key 在所 match 的对象中有存在，即可命中。
<img src="https://img-blog.csdnimg.cn/2021101022001034.png" alt="">
- 而当 match 的对象是类对象时，匹配的规则是，跟 dict 有点类似，只要对象类型和对象的属性有满足 case 的条件，就能命中。
<img src="https://img-blog.csdnimg.cn/20211010220010462.png" alt="">

因此在写 match-case 的时候，最大的难点可能就是如何把握这个顺序，才能确保你写的代码不会翻车。

我个人总结一些规律，仅供大家参考：
- list 或者 tuple：应该从不格式到严格- dict 或者 object：应该从严格到不严格
在经过半天时间的尝鲜后，我有了一些自己的理解，分享给大家，不知道我的理解有没有问题，但我依然建议大家在 **充分了解 match-case 的匹配规则** 后，再去使用它。

另外，这个功能一出，有许多人表示 **终于来了**，也有一些人表示 **太鸡肋了**。

我对于此事的看法是，match-case 必然有一定的适用场景，但这不意味着 match-case 是必要的，所有的 match-case 都可以换成 if 表达式，但反过来却不然，if 可以结合 and 和 or 承接 n 个多复杂的组合判断，但 match-case 却不行，它只能用于单个对象进行匹配判断。

但是从一定程度上来说，它有点多余，而且有一定的上手成本。

**那么对于这样的一个 新特性，你会用它吗？**

文章最后给大家介绍三个我自己写的在线文档：

**第一个文档**：

花了两个多月的时间，整理了 100 个 PyCharm 的使用技巧，为了让新手能够直接上手，我花了很多的时间录制了上百张 GIF 动图，有兴趣的前往在线文档阅读。

<img src="https://img-blog.csdnimg.cn/20211010220016476.png" alt="">

**第二个文档**：

系统收录各种 Python 冷门知识，Python Shell 的多样玩法，令人疯狂的 Python 炫技操作，Python 的超详细进阶知识解读，非常实用的 Python 开发技巧等。

<img src="https://img-blog.csdnimg.cn/20211010220017421.png" alt="">

**第三个文档**：

花了三个月时间写的一本 适合零基础入门 Python 的全中文教程，搭配大量的代码案例，让初学者对 代码的运作效果有一个直观感受，教程既有深度又有广度，每篇文章都会标内容的难度，是基础还是进阶的，可供读者进行选择，是一本难得的 Python 中文电子教程。

<img src="https://img-blog.csdnimg.cn/20211010220018418.png" alt="">
