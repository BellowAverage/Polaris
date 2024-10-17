
--- 
title:  0基础学习PyFlink——不可以用UDTAF装饰器装饰function的原因分析 
tags: []
categories: [] 

---


#### 大纲
- - 

1. UDF：User Defined Scalar Function1. UDTF：User Defined Table Function1. UDAF：User Defined Aggregate Function1. UDTAF：User Defined Table Aggregate Function
在很多案例中，我们看到udf、udtf和udaf几个装饰器修饰function

```
@udf(result_type=DataTypes.BIGINT())
def add(i, j):
	return i + j

@udtf(result_types=[DataTypes.BIGINT(), DataTypes.BIGINT()])
def range_emit(s, e):
	for i in range(e):
		yield s, i

@udaf(result_type=DataTypes.FLOAT(), func_type="pandas")
def mean_udaf(v):
	return v.mean()

```

但是没有见到udtaf修饰function的案例，比如

```
# 错误的
@udtaf(result_type=DataTypes.ROW([DataTypes.FIELD("word", DataTypes.STRING()) , DataTypes.FIELD("count", DataTypes.BIGINT())]), accumulator_type=DataTypes.ROW([DataTypes.FIELD("word", DataTypes.STRING())]), func_type="general")
def lower(line):
	yield Row('a', 1)

```

这是因为**这儿存在一个悖论**

## udtaf要求func_type必须是general

```
def udtaf(f: Union[Callable, TableAggregateFunction, Type] = None,
          input_types: Union[List[DataType], DataType, str, List[str]] = None,
          result_type: Union[DataType, str] = None,
          accumulator_type: Union[DataType, str] = None,
          deterministic: bool = None, name: str = None,
          func_type: str = 'general') -&gt; Union[UserDefinedAggregateFunctionWrapper, Callable]:
    """
    Helper method for creating a user-defined table aggregate function.
        :param f: user-defined table aggregate function.
    :param input_types: optional, the input data types.
    :param result_type: the result data type.
    :param accumulator_type: optional, the accumulator data type.
    :param deterministic: the determinism of the function's results. True if and only if a call to
                          this function is guaranteed to always return the same result given the
                          same parameters. (default True)
    :param name: the function name.
    :param func_type: the type of the python function, available value: general
                     (default: general)
    :return: UserDefinedAggregateFunctionWrapper or function.

    .. versionadded:: 1.13.0
    """
    if func_type != 'general':
        raise ValueError("The func_type must be 'general', got %s."
                         % func_type)
    if f is None:
        return functools.partial(_create_udtaf, input_types=input_types, result_type=result_type,
                                 accumulator_type=accumulator_type, func_type=func_type,
                                 deterministic=deterministic, name=name)
    else:
        return _create_udtaf(f, input_types, result_type, accumulator_type, func_type,
                             deterministic, name)

```

如果func_type不是’general’，则会抛出错误，所以func_type="pandas"是不可以的。 udtaf修饰方法后的返回类型是UserDefinedAggregateFunctionWrapper。

```
def _create_udtaf(f, input_types, result_type, accumulator_type, func_type, deterministic, name):
    return UserDefinedAggregateFunctionWrapper(
        f, input_types, result_type, accumulator_type, func_type, deterministic, name, True)

```

## delegate function要求非func_type必须是pandas

Table API下只有这些方法接受udtaf修饰function返回的UserDefinedAggregateFunctionWrapper。
- def aggregate(self, func: Union[Expression, UserDefinedAggregateFunctionWrapper]) -&gt; ‘AggregatedTable’- def flat_aggregate(self, func: Union[Expression, UserDefinedAggregateFunctionWrapper]) -&gt; ‘FlatAggregateTable’
这些方法的在底层会调用被修饰的UserDefinedFunctionWrapper。

```
    def aggregate(self, func: Union[Expression, UserDefinedAggregateFunctionWrapper]) \
            -&gt; 'AggregatedTable':
        """
        Performs a global aggregate operation with an aggregate function. You have to close the
        aggregate with a select statement.
        .. versionadded:: 1.13.0
        """
        if isinstance(func, Expression):
            return AggregatedTable(self._j_table.aggregate(func._j_expr), self._t_env)
        else:
            func._set_takes_row_as_input()
            if hasattr(func, "_alias_names"):
                alias_names = getattr(func, "_alias_names")
                func = func(with_columns(col("*"))).alias(*alias_names)
            else:
                func = func(with_columns(col("*")))
            return AggregatedTable(self._j_table.aggregate(func._j_expr), self._t_env)

```

进而会调用到_java_user_defined_function。由于udtaf修饰的方法不是UserDefinedFunction对象，而是一个function，所以它会通过_create_delegate_function创建新的func 。

```
class UserDefinedFunctionWrapper(object):
……
    def _java_user_defined_function(self):
    ……
    if not isinstance(self._func, UserDefinedFunction):
		func = self._create_delegate_function()
    ……

```

而_create_delegate_function则要求udtaf中的function的func_type必须是pandas

```
    def _create_delegate_function(self) -&gt; UserDefinedFunction:
        assert self._func_type == 'pandas'
        return DelegatingPandasAggregateFunction(self._func)

```

这就和之前udtaf中要求func_type必须是general相背。 所以我们没看到udtaf修饰function的案例。
