
--- 
title:  0基础学习PyFlink——个数滑动窗口（Sliding Count Windows） 
tags: []
categories: [] 

---


#### 大纲
- - - <ul><li>- - - 


## 滑动（Sliding）和滚动（Tumbling）的区别

正如其名，“滑动”是指这个窗口沿着一定的方向，按着一定的速度“滑行”。 <img src="https://img-blog.csdnimg.cn/9c68ce3d77cd443f82402958b3b202a5.png" alt="在这里插入图片描述"> 而滚动窗口，则是一个个“衔接着”，而不是像上面那样交错着。 <img src="https://img-blog.csdnimg.cn/6dbecb8ee4694d0ebd119fce2effd73a.png" alt="在这里插入图片描述"> 它们的相同之处就是：只有窗口内的事件数量到达窗口要求的数值时，这些窗口才会触发计算。

## 样例

我们只要对中的代码做轻微的改动即可。为了简化样例，我们只看Key为E的元素的滑动。

```
word_count_data = [("E",3),("E",1),("E",4),("E",2),("E",6),("E",5)]

def word_count():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    # write all the data to one file
    env.set_parallelism(1)

    source_type_info = Types.TUPLE([Types.STRING(), Types.INT()])
    # define the source
    # mappging
    source = env.from_collection(word_count_data, source_type_info)
    # source.print()

    # keying
    keyed=source.key_by(lambda i: i[0]) 

```

### 窗口为2，滑动距离为1

count_window会根据传入的第二参数决定是构建滚动（CountTumblingWindowAssigner）窗口还是滑动（CountSlidingWindowAssigner）窗口。

```
    def count_window(self, size: int, slide: int = 0):
        """
        Windows this KeyedStream into tumbling or sliding count windows.

        :param size: The size of the windows in number of elements.
        :param slide: The slide interval in number of elements.

        .. versionadded:: 1.16.0
        """
        if slide == 0:
            return WindowedStream(self, CountTumblingWindowAssigner(size))
        else:
            return WindowedStream(self, CountSlidingWindowAssigner(size, slide))

```

我们只要给count_window第二个参数传递一个不为0的值，即可达到滑动效果。

```
    # reducing
    windows_size = 2
    sliding_size = 1
    reduced=keyed.count_window(windows_size, sliding_size) \
                .apply(SumWindowFunction(),
                       Types.TUPLE([Types.STRING(), Types.INT()]))

    # # define the sink
    reduced.print()

    # submit for execution
    env.execute()

```

>  
 (E,2) (E,2) (E,2) (E,2) (E,2) 


<img src="https://img-blog.csdnimg.cn/ddd819a5eb7a4156ac9b1e93af749a72.png" alt="在这里插入图片描述">

### 窗口为3，滑动距离为1

```
    # reducing
    windows_size = 3
    sliding_size = 1
    reduced=keyed.count_window(windows_size, sliding_size) \
                .apply(SumWindowFunction(),
                       Types.TUPLE([Types.STRING(), Types.INT()]))

```

>  
 (E,3) (E,3) (E,3) (E,3) 


<img src="https://img-blog.csdnimg.cn/c17d6e734aaf4d969e2c2d988be26feb.png" alt="在这里插入图片描述">

### 窗口为3，滑动距离为2

```
    # reducing
    windows_size = 3
    sliding_size = 2
    reduced=keyed.count_window(windows_size, sliding_size) \
                .apply(SumWindowFunction(),
                       Types.TUPLE([Types.STRING(), Types.INT()]))

```

>  
 (E,3) (E,3) 


<img src="https://img-blog.csdnimg.cn/0feb017432f3454d9227f04f3c6846a7.png" alt="在这里插入图片描述">

### 窗口为3，滑动距离为3

这个就等效于滚动窗口了，因为“滑”过了窗口大小。

```
    # reducing
    windows_size = 3
    sliding_size = 3
    reduced=keyed.count_window(windows_size, sliding_size) \
                .apply(SumWindowFunction(),
                       Types.TUPLE([Types.STRING(), Types.INT()]))

```

>  
 (E,3) (E,3) 


<img src="https://img-blog.csdnimg.cn/1f9fbfc0922e49d8949a3ad0f8b92680.png" alt="在这里插入图片描述">

## 完整代码

```
from typing import Iterable

from pyflink.common import Types
from pyflink.datastream import StreamExecutionEnvironment, RuntimeExecutionMode, WindowFunction
from pyflink.datastream.window import CountWindow

class SumWindowFunction(WindowFunction[tuple, tuple, str, CountWindow]):
    def apply(self, key: str, window: CountWindow, inputs: Iterable[tuple]):
        return [(key,  len([e for e in inputs]))]


word_count_data = [("E",3),("E",1),("E",4),("E",2),("E",6),("E",5)]

def word_count():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    # write all the data to one file
    env.set_parallelism(1)

    source_type_info = Types.TUPLE([Types.STRING(), Types.INT()])
    # define the source
    # mappging
    source = env.from_collection(word_count_data, source_type_info)
    # source.print()

    # keying
    keyed=source.key_by(lambda i: i[0]) 
    
    # reducing
    windows_size = 3
    sliding_size = 1
    reduced=keyed.count_window(windows_size, sliding_size) \
                .apply(SumWindowFunction(),
                       Types.TUPLE([Types.STRING(), Types.INT()]))

    # # define the sink
    reduced.print()

    # submit for execution
    env.execute()

if __name__ == '__main__':
    word_count()

```

## 参考资料
- 