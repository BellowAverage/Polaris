
--- 
title:  0基础学习PyFlink——水位线（watermark）触发计算 
tags: []
categories: [] 

---
在和中，我们发现如果窗口中元素个数没有把窗口填满，则不会触发计算。 <img src="https://img-blog.csdnimg.cn/c6dda301111d4c06b6f07054b10cf95d.png" alt="在这里插入图片描述">

为了解决长期不计算的问题，我们引入了在和的方案。但是这个方案引入另外一个问题，就是每次处理数据可能不尽相同。这是因为它们使用了“处理时间”（Processing Time）来作为窗口划分的参考系，而每次程序处理时间会根据当前负载情况有很大的不同。这样我们对同一批数据做处理时，可能会得出不同的Window切分方案。 <img src="https://img-blog.csdnimg.cn/056692150cc64d7a8118edaf4403d0a6.png" alt="在这里插入图片描述"> 于是我们引入方案。它可以使用源自数据本身的“事件时间”（Event Time）作为Time Window的参考系，这样在不同负载、不同时间，相同数据的时间参考系是一样的，进而可以得出一致的结果。 <img src="https://img-blog.csdnimg.cn/fc7d3da147ce4d6d9fffdd46c76825df.png" alt="在这里插入图片描述"> 但是现实中，我们没法保证上述数据是按照上面的顺序到达Flink的。 比如下面这个例子，红色部分都是乱序的，那么Flink如何处理这些数据呢？ <img src="https://img-blog.csdnimg.cn/2481b8270248490dbdc2bf73af97b94d.png" alt="在这里插入图片描述"> 只有两种可能性：
1. 直接抛弃；1. 等待一段时间统一处理，超过等待的时间直接抛弃。因为不可能一直等下去，否则什么时候处理呢？
这些即有别于Count Window，也有别于Time Window。这个时候就要引入水位线（watermark）技术来解决这个问题。 在详细讲解之前，我们需要明确一些基本知识：
1. **EventTime就是Timestamp，即我们可以通过制定Timestamp函数设定元素的EventTime。**1. EventTime从属于元素。1. **Watermark源于EventTime和max_out_of_orderness（等待无序数据的时间），即Watermark=EventTime-max_out_of_orderness。**1. Watermark从属于流。1. **Window的Start源于EventTime；End源于Start和窗口时间，即End=Start+WindowTme；这是一个左闭右开的区间，即[Start, End)。**1. Window从属于流，**只有Watermark&gt;=Window End时才会触发计算（且窗口中要有元素）。**1. **Window在单向递增前进**，比如从[0，10)变成[10，20)、[20，30)……[90，100)。1. **Wartermark单向递增前进**，它不会因为新进入的元素EventTime较小，而导致Wartermark向变小的趋势发展。 <img src="https://img-blog.csdnimg.cn/11233e73a4124300a78b68f6b7d96d9e.png" alt="在这里插入图片描述"> 上图中，第一个元素(A,1)的EventTime通过自定义公式可以得到101，于是初始的Window的Start值是该值向下取可以被Window Size整除的最大值，即100;这个进一步确认了第一个窗口是[100,105)。 watermark是通过eventtime计算出来的，上例中我们希望如果事件在窗口时间之外到来则抛弃，即不等待任何时间，即Window End+0，即Eventtime-0。 （A,0）数据来到的时候，watermark不会因为其Eventtime为100，比流中的watermark值（101）小而改变，依然维持watermark单调递增。这个在（A,2）和(A,5)到来时也是如此。 （A,8）元素的到来，会让流的watermark变成108。这个值会越过当前窗口[100,105)，于是会触发计算。计算的元素要求eventtime在上述区间内，即(A,1)、(A,0)、(A,3)和(A,4)； （A,10）元素的到来，会让流的watermark变成110。这个值会越过当前窗口[100,110)，于是会触发计算。计算的元素要求eventtime在上述区间内，即(A,8)、(A,6)、(A,7)和(A,9)；而(A,2)因为不在这个区间内，就被抛弃了。我们也可以认为（A,2）迟到而被抛弃。 为了更好讲述原理，上述例子存在一个假设：watertime更新是随着元素一个个进入而改变的。而实际元素进入个数不太确定，比如可能会两个两个进入，那么就会变成如下。主要区别就是(A,5)参与了第二次窗口计算，虽然它迟到了，而且watermark计算方法也不打算等待任何一个迟到的数据，但是它和（A,10）一起进入时间戳计算逻辑，导致触发的时机被滞后，从而“幸运”的赶上了最后一轮窗口计算。如果它稍微再晚一点到来，它也会被抛弃。 <img src="https://img-blog.csdnimg.cn/dfb8710ba24e491aace930fbc276bc5f.png" alt="在这里插入图片描述">
## 测试代码

```
import time
from pyflink.common import Duration, WatermarkStrategy, Time, Types
from pyflink.datastream.window import TumblingEventTimeWindows, TimeWindow, TumblingProcessingTimeWindows
from pyflink.common.watermark_strategy import TimestampAssigner
from pyflink.datastream import StreamExecutionEnvironment,RuntimeExecutionMode, TimeCharacteristic
from pyflink.table import StreamTableEnvironment, TableDescriptor, Schema, DataTypes
from pyflink.datastream.functions import AllWindowFunction, ProcessFunction, ProcessAllWindowFunction, KeyedProcessFunction
from pyflink.table.expressions import lit, col
from pyflink.table.window import Tumble
from pyflink.common.time import Instant
from pyflink.table.udf import udf
from pyflink.common import Row

            
class WindowFunc(AllWindowFunction[tuple, tuple, TimeWindow]):
    def apply(self, window, inputs):
        out = "**************************WindowFunc**************************" \
                "\nwindow: start:{} end:{} \ninputs: {}" \
                "\n**************************WindowFunc**************************" \
                    .format(Instant.of_epoch_milli(window.start), Instant.of_epoch_milli(window.end), inputs)
        print(out)
      
        for value in inputs:
            yield (value, Instant.of_epoch_milli(window.start), Instant.of_epoch_milli(window.end))

class TimestampAssignerAdapter(TimestampAssigner):
    def extract_timestamp(self, value, record_timestamp: int):
        return value[1] * 1000
    
class TimestampAssignerProcessFunctionAdapter(ProcessFunction):
    def process_element(self, value, ctx: 'ProcessFunction.Context'):
        out_put = "-----------------------TimestampAssignerProcessFunctionAdapter {}-----------------------" \
                    "\nvalue: {} \ttimestamp: {} \tcurrent_processing_time: {} \tcurrent_watermark: {}" \
                    "\n-----------------------TimestampAssignerProcessFunctionAdapter-----------------------" \
                        .format(int(time.time()), value, Instant.of_epoch_milli(ctx.timestamp()),
                                Instant.of_epoch_milli(ctx.timer_service().current_processing_time()),
                                Instant.of_epoch_milli(ctx.timer_service().current_watermark()))
                        
        print(out_put)
        
        yield (value, Instant.of_epoch_milli(ctx.timestamp()), 
               Instant.of_epoch_milli(ctx.timer_service().current_processing_time()),
               Instant.of_epoch_milli(ctx.timer_service().current_watermark()))

def gen_random_int_and_timestamp():
    stream_execute_env = StreamExecutionEnvironment.get_execution_environment()
    # stream_execute_env.set_runtime_mode(RuntimeExecutionMode.STREAMING)
    stream_execute_env.set_stream_time_characteristic(TimeCharacteristic.EventTime)
    stream_execute_env.set_parallelism(1)
    stream_execute_env.get_config().set_auto_watermark_interval(2)
    
    stream_table_env = StreamTableEnvironment.create(stream_execution_environment=stream_execute_env)
    ordinal_num_start = 0
    ordinal_num_end = 10
    rows_per_second = 1
    
    schame = Schema.new_builder().column('in_ord', DataTypes.INT()) \
                                .build()
                                
    table_descriptor = TableDescriptor.for_connector('datagen') \
                        .schema(schame) \
                        .option('fields.in_ord.kind', 'sequence') \
                        .option('fields.in_ord.start', str(ordinal_num_start)) \
                        .option('fields.in_ord.end', str(ordinal_num_end)) \
                        .option('rows-per-second', str(rows_per_second)) \
                        .build()
          
    stream_table_env.create_temporary_table('source', table_descriptor)
    
    table = stream_table_env.from_path('source')
    
    @udf(result_type=DataTypes.ROW([DataTypes.FIELD("in_ord", DataTypes.INT()), DataTypes.FIELD("calc_order", DataTypes.INT())]), input_types=[DataTypes.INT()])
    def colFunc(oneCol):
        ordinal_num_data_map = {<!-- -->0: 1, 1: 0, 2: 3, 3: 4, 4: 8, 5: 6, 6: 7, 7: 2, 8: 9, 9: 10, 10: 5}
        # ordinal_num_data_map = {0: 16, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
        #                       10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15, 16: 0, 17: 17, 18: 18, 19: 19,
        #                       20: 20, 21: 121, 22: 122, 23: 123, 24: 124, 25: 125, 26: 126, 27: 127, 28: 128, 29: 129,}
        data = ordinal_num_data_map[oneCol] + 100
        return Row(oneCol, data)
    
    input_table=table.map(colFunc(col('in_ord')))
    
    datastream = stream_table_env.to_data_stream(input_table)
    
    ###############################################################################################    
    # datastream.window_all(TumblingProcessingTimeWindows.of(Time.milliseconds(10))) \
    #                     .apply(WindowFunc())
    ###############################################################################################
    # watermark_strategy = WatermarkStrategy.no_watermarks().with_timestamp_assigner(TimestampAssignerAdapter())
    # datastream_with_watermark=datastream.assign_timestamps_and_watermarks(watermark_strategy)
    # datastream_with_watermark.process(TimestampAssignerProcessFunctionAdapter())
    
    # datastream_with_watermark.window_all(TumblingEventTimeWindows.of(Time.milliseconds(10))) \
    #                     .apply(WindowFunc())        
    ###############################################################################################
    # watermark_strategy = WatermarkStrategy.for_monotonous_timestamps().with_timestamp_assigner(TimestampAssignerAdapter())
    watermark_strategy = WatermarkStrategy.for_bounded_out_of_orderness(Duration.of_seconds(0)).with_timestamp_assigner(TimestampAssignerAdapter())
    datastream_with_watermark=datastream.assign_timestamps_and_watermarks(watermark_strategy)
    
    datastream_with_watermark.process(TimestampAssignerProcessFunctionAdapter())
    
    
    datastream_with_watermark.window_all(TumblingEventTimeWindows.of(Time.seconds(5))) \
                        .apply(WindowFunc())
    ###############################################################################################

    stream_execute_env.execute()
    
if __name__ == '__main__':
    gen_random_int_and_timestamp()

```

>  
 -----------------------TimestampAssignerProcessFunctionAdapter 1699856800----------------------- value: Row(in_ord=0, calc_order=101) timestamp: Instant&lt;101, 0&gt; current_processing_time: Instant&lt;1699856800, 705000000&gt; current_watermark: Instant&lt;-9223372036854776, 192000000&gt; -----------------------TimestampAssignerProcessFunctionAdapter----------------------- -----------------------TimestampAssignerProcessFunctionAdapter 1699856802----------------------- value: Row(in_ord=1, calc_order=100) timestamp: Instant&lt;100, 0&gt; current_processing_time: Instant&lt;1699856802, 700000000&gt; current_watermark: Instant&lt;100, 999000000&gt; -----------------------TimestampAssignerProcessFunctionAdapter----------------------- -----------------------TimestampAssignerProcessFunctionAdapter 1699856802----------------------- value: Row(in_ord=2, calc_order=103) timestamp: Instant&lt;103, 0&gt; current_processing_time: Instant&lt;1699856802, 702000000&gt; current_watermark: Instant&lt;100, 999000000&gt; -----------------------TimestampAssignerProcessFunctionAdapter----------------------- -----------------------TimestampAssignerProcessFunctionAdapter 1699856804----------------------- value: Row(in_ord=3, calc_order=104) timestamp: Instant&lt;104, 0&gt; current_processing_time: Instant&lt;1699856804, 700000000&gt; current_watermark: Instant&lt;102, 999000000&gt; -----------------------TimestampAssignerProcessFunctionAdapter----------------------- -----------------------TimestampAssignerProcessFunctionAdapter 1699856804----------------------- value: Row(in_ord=4, calc_order=108) timestamp: Instant&lt;108, 0&gt; current_processing_time: Instant&lt;1699856804, 709000000&gt; current_watermark: Instant&lt;102, 999000000&gt; -----------------------TimestampAssignerProcessFunctionAdapter----------------------- **<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>WindowFunc**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> window: start:Instant&lt;100, 0&gt; end:Instant&lt;105, 0&gt; inputs: [Row(in_ord=0, calc_order=101), Row(in_ord=1, calc_order=100), Row(in_ord=2, calc_order=103), Row(in_ord=3, calc_order=104)] **<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>WindowFunc**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> -----------------------TimestampAssignerProcessFunctionAdapter 1699856806----------------------- value: Row(in_ord=5, calc_order=106) timestamp: Instant&lt;106, 0&gt; current_processing_time: Instant&lt;1699856806, 701000000&gt; current_watermark: Instant&lt;107, 999000000&gt; -----------------------TimestampAssignerProcessFunctionAdapter----------------------- -----------------------TimestampAssignerProcessFunctionAdapter 1699856806----------------------- value: Row(in_ord=6, calc_order=107) timestamp: Instant&lt;107, 0&gt; current_processing_time: Instant&lt;1699856806, 705000000&gt; current_watermark: Instant&lt;107, 999000000&gt; -----------------------TimestampAssignerProcessFunctionAdapter----------------------- -----------------------TimestampAssignerProcessFunctionAdapter 1699856808----------------------- value: Row(in_ord=7, calc_order=102) timestamp: Instant&lt;102, 0&gt; current_processing_time: Instant&lt;1699856808, 700000000&gt; current_watermark: Instant&lt;107, 999000000&gt; -----------------------TimestampAssignerProcessFunctionAdapter----------------------- -----------------------TimestampAssignerProcessFunctionAdapter 1699856808----------------------- value: Row(in_ord=8, calc_order=109) timestamp: Instant&lt;109, 0&gt; current_processing_time: Instant&lt;1699856808, 701000000&gt; current_watermark: Instant&lt;107, 999000000&gt; -----------------------TimestampAssignerProcessFunctionAdapter----------------------- -----------------------TimestampAssignerProcessFunctionAdapter 1699856809----------------------- value: Row(in_ord=9, calc_order=110) timestamp: Instant&lt;110, 0&gt; current_processing_time: Instant&lt;1699856809, 440000000&gt; current_watermark: Instant&lt;108, 999000000&gt; -----------------------TimestampAssignerProcessFunctionAdapter----------------------- -----------------------TimestampAssignerProcessFunctionAdapter 1699856809----------------------- value: Row(in_ord=10, calc_order=105) timestamp: Instant&lt;105, 0&gt; current_processing_time: Instant&lt;1699856809, 441000000&gt; current_watermark: Instant&lt;108, 999000000&gt; -----------------------TimestampAssignerProcessFunctionAdapter----------------------- **<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>WindowFunc**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> window: start:Instant&lt;105, 0&gt; end:Instant&lt;110, 0&gt; inputs: [Row(in_ord=4, calc_order=108), Row(in_ord=5, calc_order=106), Row(in_ord=6, calc_order=107), Row(in_ord=8, calc_order=109), Row(in_ord=10, calc_order=105)] **<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>WindowFunc**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> **<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>WindowFunc**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> window: start:Instant&lt;110, 0&gt; end:Instant&lt;115, 0&gt; inputs: [Row(in_ord=9, calc_order=110)] 


## 参考资料
- 