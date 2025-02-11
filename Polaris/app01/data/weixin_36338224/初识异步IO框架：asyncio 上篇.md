
--- 
title:  初识异步IO框架：asyncio 上篇 
tags: []
categories: [] 

---
通过前两节的铺垫（关于协程的使用），今天我们终于可以来介绍我们整个系列的重点 -- `asyncio`。

`asyncio`是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。

有些同学，可能很疑惑，既然有了以生成器为基础的协程，我们直接使用`yield` 和 `yield from` 不就可以手动实现对IO的调度了吗？ 为何Python吃饱了没事干，老重复造轮子。

这个问题很好回答，就跟为什么会有`Django`，为什么会有`Scrapy`，是一个道理。

他们都是框架，将很多很重复性高，复杂度高的工作，提前给你做好，这样你就可以专注于业务代码的研发。

跟着小明学完了协程的那些个难点，你是不是也发现了，协程的知识点我已经掌握了，但是我还是不知道怎么用，如何使用，都说它可以实现并发，但是我还是不知道如何入手？

那是因为，我们现在还缺少一个成熟的框架，帮助你完成那些复杂的动作。这个时候，`ayncio`就这么应运而生了。

### 1. 如何定义/创建协程

还记得在前两章节的时候，我们创建了生成器，是如何去检验我们创建的是不是生成器对象吗？

我们是借助了`isinstance()`函数，来判断是否是`collections.abc` 里的`Generator`类的子类实现的。

同样的方法，我们也可以用在这里。

只要在一个函数前面加上 `async` 关键字，这个函数对象是一个协程，通过`isinstance`函数，它确实是`Coroutine`类型。

```
from collections.abc import Coroutine

async def hello(name):
    print('Hello,', name)

if __name__ == '__main__':
    # 生成协程对象，并不会运行函数内的代码
    coroutine = hello("World")

    # 检查是否是协程 Coroutine 类型
    print(isinstance(coroutine, Coroutine))  # True
```

前两节，我们说，生成器是协程的基础，那我们是不是有办法，将一个生成器，直接变成协程使用呢。答案是有的。

```
import asyncio
from collections.abc import Generator, Coroutine

'''
只要在一个生成器函数头部用上 @asyncio.coroutine 装饰器
就能将这个函数对象，【标记】为协程对象。注意这里是【标记】，划重点。
实际上，它的本质还是一个生成器。
标记后，它实际上已经可以当成协程使用。后面会介绍。
'''


@asyncio.coroutine
def hello():
    # 异步调用asyncio.sleep(1):
    yield from asyncio.sleep(1)


if __name__ == '__main__':
    coroutine = hello()
    print(isinstance(coroutine, Generator))  # True
    print(isinstance(coroutine, Coroutine))  # False
```

### 2. asyncio的几个概念

在了解`asyncio`的使用方法前，首先有必要先介绍一下，这几个贯穿始终的概念。
- `event_loop 事件循环`：程序开启一个无限的循环，程序员会把一些函数（协程）注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。- `coroutine 协程`：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。- `future 对象`： 代表将来执行或没有执行的任务的结果。它和task上没有本质的区别- `task 任务`：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。Task 对象是 Future 的子类，它将 coroutine 和 Future 联系在一起，将 coroutine 封装成一个 Future 对象。- `async/await 关键字`：python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。其作用在一定程度上类似于yield。
这几个概念，干看可能很难以理解，没事，往下看实例，然后再回来，我相信你一定能够理解。

### 3. 学习协程是如何工作的

协程完整的工作流程是这样的
- 定义/创建协程对象- 将协程转为task任务- 定义事件循环对象容器- 将task任务扔进事件循环对象中触发
光说不练假把戏，一起来看下

```
import asyncio

async def hello(name):
    print('Hello,', name)

# 定义协程对象
coroutine = hello("World")

# 定义事件循环对象容器
loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)

# 将协程转为task任务
task = loop.create_task(coroutine)

# 将task任务扔进事件循环对象中并触发
loop.run_until_complete(task)
```

输出结果，当然显而易见

```
Hello, World
```

### 4. await与yield对比

前面我们说，`await`用于挂起阻塞的异步调用接口。其作用在`一定程度上`类似于yield。

注意这里是，一定程度上，意思是效果上一样（都能实现暂停的效果），但是功能上却不兼容。就是你不能在生成器中使用`await`，也不能在async 定义的协程中使用`yield from`。

小明不是胡说八道的。有实锤。 <img src="https://img-blog.csdnimg.cn/20201026081611385.png" alt="普通函数中 不能使用 await"> 再来一锤。 <img src="https://img-blog.csdnimg.cn/20201026081611913.png" alt="async 中 不能使用yield">

除此之外呢，还有一点很重要的。
- `yield from` 后面可接 `可迭代对象`，也可接`future对象`/协程对象；- `await` 后面必须要接 `future对象`/`协程对象`
如何验证呢？

`yield from` 后面可接 `可迭代对象`，这个前两章已经说过了，这里不再赘述。 接下来，就只要验证，`yield from`和`await`都可以接`future对象`/`协程对象`就可以了。

验证之前呢，要先介绍一下这个函数： `asyncio.sleep(n)`，这货是asyncio自带的工具函数，他可以模拟IO阻塞，他返回的是一个协程对象。

```
func = asyncio.sleep(2)
print(isinstance(func, Future))      # False
print(isinstance(func, Coroutine))   # True
```

还有，要学习如何创建`Future对象`，不然怎么验证。 前面概念里说过，Task是Future的子类，这么说，我们只要创建一个task对象即可。

```
import asyncio
from asyncio.futures import Future

async def hello(name):
    await asyncio.sleep(2)
    print('Hello, ', name)

coroutine = hello("World")

# 将协程转为task对象
task = asyncio.ensure_future(coroutine)

print(isinstance(task, Future))   # True
```

好了，接下来，开始验证。 <img src="https://img-blog.csdnimg.cn/20201026081612975.png" alt="验证通过">

### 5. 绑定回调函数

异步IO的实现原理，就是在IO高的地方挂起，等IO结束后，再继续执行。在绝大部分时候，我们后续的代码的执行是需要依赖IO的返回值的，这就要用到回调了。

回调的实现，有两种，一种是绝大部分程序员喜欢的，利用的同步编程实现的回调。 这就要求我们要能够有办法取得协程的await的返回值。

```
import asyncio
import time

async def _sleep(x):
    time.sleep(2)
    return '暂停了{}秒！'.format(x)


coroutine = _sleep(2)
loop = asyncio.get_event_loop()

task = asyncio.ensure_future(coroutine)
loop.run_until_complete(task)

# task.result() 可以取得返回结果
print('返回结果：{}'.format(task.result()))
```

输出

```
返回结果：暂停了2秒！
```

还有一种是通过asyncio自带的添加回调函数功能来实现。

```
import time
import asyncio


async def _sleep(x):
    time.sleep(2)
    return '暂停了{}秒！'.format(x)

def callback(future):
    print('这里是回调函数，获取返回结果是：', future.result())

coroutine = _sleep(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)

# 添加回调函数
task.add_done_callback(callback)

loop.run_until_complete(task)
```

输出

```
这里是回调函数，获取返回结果是： 暂停了2秒！
```

emmm，和上面的结果是一样的。nice
