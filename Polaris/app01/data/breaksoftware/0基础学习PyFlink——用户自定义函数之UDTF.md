
--- 
title:  0基础学习PyFlink——用户自定义函数之UDTF 
tags: []
categories: [] 

---


#### 大纲
- - 


在中，我们讲解了UDF。本节我们将讲解表值函数——UDTF <img src="https://img-blog.csdnimg.cn/7965fc6b06a84bb8bc97b9b37b33a2db.png" alt="在这里插入图片描述">

## 表值函数

我们对比下UDF和UDTF

```
def udf(f: Union[Callable, ScalarFunction, Type] = None,
        input_types: Union[List[DataType], DataType, str, List[str]] = None,
        result_type: Union[DataType, str] = None,
        deterministic: bool = None, 
        name: str = None, 
        func_type: str = "general",
        udf_type: str = None
        ) -&gt; Union[UserDefinedScalarFunctionWrapper, Callable]:

```

```
def udtf(f: Union[Callable, TableFunction, Type] = None,
         input_types: Union[List[DataType], DataType, str, List[str]] = None,
         result_types: Union[List[DataType], DataType, str, List[str]] = None,
         deterministic: bool = None,
         name: str = None
         ) -&gt; Union[UserDefinedTableFunctionWrapper, Callable]:

```

可以发现：
- UDF比UDTF多了func_type和udf_type参数；- UDTF的返回类型比UDF的丰富，多了两个List类型：List[DataType]和List[str]；
特别是最后一点，可以认为是UDF和UDTF在应用上的主要区别。 换种更容易理解的说法是：**UDTF可以返回任意数量的行作为输出而不是像UDF那样返回单个值（行）。** 举一个例子：

```
word_count_data = ["A", "B", "C", "a", "C"] 

```

我们希望统计上面这些字符的个数，以及小写后字符的个数。这样A的个数是1，a的个数是2（因为a算一个，A小写后又算一个）。C的个数是2，g的个数是2。 这就要求统计算法在遇到大写字母时，需要统计大小写两种字母；而遇到小写字母时，只需要统计小写字母。

```
    @udtf(result_types=[DataTypes.STRING()], input_types=row_type_tab_source)
    def rowFunc(row):
        if row[0].isupper():
            yield row[0]
            yield row[0].lower()
        else:
            yield row[0]

```

yield关键字返回的是generator生成器。Table API对rowFunc的调用最终会生成[“A”,“a”,“B”,“b”,“C”,“c”,“a”,“C”,“c”]。 和调用UDF不同的是，需要使用flat_map来调用UDTF。flat即为“打平”，可以生动的理解为将多维降为一维。

```
    tab_trans=tab_source.flat_map(rowFunc)
    tab_trans.execute().print()

```

```
+--------------------------------+
|                             f0 |
+--------------------------------+
|                              A |
|                              a |
|                              B |
|                              b |
|                              C |
|                              c |
|                              a |
|                              C |
|                              c |
+--------------------------------+
9 rows in set

```

由于我们没有指定经过处理的值所属的字段名称，于是会使用默认的f0作为字段名。我们可以使用alias来给它别名下。

```
    tab_trans_alias=tab_trans.alias('trans_word')
    tab_trans_alias.execute().print()

```

```
+--------------------------------+
|                     trans_word |
+--------------------------------+
|                              A |
|                              a |
|                              B |
|                              b |
|                              C |
|                              c |
|                              a |
|                              C |
|                              c |
+--------------------------------+
9 rows in set

```

最后我们就可以用这个新的表做字数统计计算

```
    tab_trans_alias.group_by(col('trans_word')) \
        .select(col('trans_word'), lit(1).count) \
        .execute_insert("WordsCountTableSink") \
        .wait()

```

```
+I[A, 1]
+I[a, 2]
+I[B, 1]
+I[b, 1]
+I[C, 2]
+I[c, 2]

```

## 完整代码

```
from pyflink.common import Configuration
from pyflink.table import (EnvironmentSettings, TableEnvironment, Schema)
from pyflink.table.types import DataTypes
from pyflink.table.table_descriptor import TableDescriptor
from pyflink.table.expressions import lit, col
from pyflink.common import Row
from pyflink.table.udf import udf,udtf,udaf,udtaf
import pandas as pd
from pyflink.table.udf import UserDefinedFunction

word_count_data = ["A", "B", "C", "a", "C"]  
    
def word_count():
    config = Configuration()
    # write all the data to one file
    config.set_string('parallelism.default', '1')
    env_settings = EnvironmentSettings \
        .new_instance() \
        .in_batch_mode() \
        .with_configuration(config) \
        .build()
    
    t_env = TableEnvironment.create(env_settings)
    
    row_type_tab_source = DataTypes.ROW([DataTypes.FIELD('word', DataTypes.STRING())])
    tab_source = t_env.from_elements(map(lambda i: Row(i), word_count_data), row_type_tab_source)

    # define the sink schema
    sink_schema = Schema.new_builder() \
        .column("word", DataTypes.STRING().not_null()) \
        .column("count", DataTypes.BIGINT()) \
        .primary_key("word") \
        .build()
        
    # Create a sink descriptor
    sink_descriptor = TableDescriptor.for_connector('print')\
        .schema(sink_schema) \
        .build()
    
    t_env.create_temporary_table("WordsCountTableSink", sink_descriptor)
    
    @udtf(result_types=[DataTypes.STRING()], input_types=row_type_tab_source)
    def rowFunc(row):
        if row[0].isupper():
            yield row[0]
            yield row[0].lower()
        else:
            yield row[0]

    tab_trans=tab_source.flat_map(rowFunc)
    tab_trans.execute().print()
    tab_trans_alias=tab_trans.alias('trans_word')
    tab_trans_alias.execute().print()
    tab_trans_alias.group_by(col('trans_word')) \
        .select(col('trans_word'), lit(1).count) \
        .execute_insert("WordsCountTableSink") \
        .wait()

if __name__ == '__main__':
    word_count()

```
