
--- 
title:  0基础学习PyFlink——时间滑动窗口（Sliding Time Windows） 
tags: []
categories: [] 

---
在我们介绍了不会有重复数据的时间滚动窗口。本节我们将介绍存在重复计算数据的时间滑动窗口。 关于滑动窗口，可以先看下。下图就是个数滑动窗口示意图。 <img src="https://img-blog.csdnimg.cn/69e2302af3fe43efa4add7100acf487a.png" alt="在这里插入图片描述"> 我们看到个数滑动窗口也会因为窗口内数据不够而不被触发。但是时间滑动窗口则可以解决这个问题，我们只要把窗口改成时间类型即可。 相应的代码我们参考，只要把TumblingProcessingTimeWindows改成SlidingProcessingTimeWindows，并增加一个偏移参数（Time.milliseconds(1)）即可。这意味着我们将运行一个时间长度为2毫秒，每次递进1毫秒的窗口。

## 完整代码

```
from typing import Iterable
import time
from pyflink.common import Types, Time
from pyflink.datastream import StreamExecutionEnvironment, RuntimeExecutionMode, WindowFunction
from pyflink.datastream.window import  TimeWindow, SlidingProcessingTimeWindows
   
class SumWindowFunction(WindowFunction[tuple, tuple, str, TimeWindow]):
    def apply(self, key: str, window: TimeWindow, inputs: Iterable[tuple]):
        print(*inputs, window)
        return [(key,  len([e for e in inputs]))]


word_count_data = [("A",2),("A",1),("A",4),("A",3),("A",6),("A",5),("A",7),("A",8),("A",9),("A",10),
                   ("A",11),("A",12),("A",13),("A",14),("A",15),("A",16),("A",17),("A",18),("A",19),("A",20)]

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
    reduced=keyed.window(SlidingProcessingTimeWindows.of(Time.milliseconds(2), Time.milliseconds(1))) \
                    .apply(SumWindowFunction(),
                        Types.TUPLE([Types.STRING(), Types.INT()]))
        
    # # define the sink
    reduced.print()

    # submit for execution
    env.execute()

if __name__ == '__main__':
    word_count()

```

## 运行结果

运行两次上述代码，我们发现每次都不同，而且有重叠计算的元素。

>  
 (‘A’, 2) (‘A’, 1) (‘A’, 4) TimeWindow(start=1698773292650, end=1698773292652) (‘A’, 2) (‘A’, 1) (‘A’, 4) (‘A’, 3) (‘A’, 6) (‘A’, 5) (‘A’, 7) (‘A’, 8) (‘A’, 9) (‘A’, 10) (‘A’, 11) TimeWindow(start=1698773292651, end=1698773292653) (A,3) (A,11) (‘A’, 3) (‘A’, 6) (‘A’, 5) (‘A’, 7) (‘A’, 8) (‘A’, 9) (‘A’, 10) (‘A’, 11) (‘A’, 12) (‘A’, 13) (‘A’, 14) (‘A’, 15) (‘A’, 16) (‘A’, 17) (‘A’, 18) (‘A’, 19) (‘A’, 20) TimeWindow(start=1698773292652, end=1698773292654) (A,17) 


<img src="https://img-blog.csdnimg.cn/765ce722649a4e499046a7187d5b7774.png" alt="在这里插入图片描述">

>  
 (‘A’, 2) (‘A’, 1) (‘A’, 4) TimeWindow(start=1698773319933, end=1698773319935) (‘A’, 2) (‘A’, 1) (‘A’, 4) (‘A’, 3) (‘A’, 6) (‘A’, 5) (‘A’, 7) (‘A’, 8) (‘A’, 9) (‘A’, 10) (‘A’, 11) (‘A’, 12) TimeWindow(start=1698773319934, end=1698773319936) (A,3) (A,12) (‘A’, 3) (‘A’, 6) (‘A’, 5) (‘A’, 7) (‘A’, 8) (‘A’, 9) (‘A’, 10) (‘A’, 11) (‘A’, 12) (‘A’, 13) (‘A’, 14) (‘A’, 15) (‘A’, 16) (‘A’, 17) (‘A’, 18) (‘A’, 19) (‘A’, 20) TimeWindow(start=1698773319935, end=1698773319937) (A,17) 


<img src="https://img-blog.csdnimg.cn/ec7e161240ba4d5581c0ee9b93379d32.png" alt="在这里插入图片描述">

## 参考资料
- 