
--- 
title:  Python 优雅地 dumps 非标准类型 
tags: []
categories: [] 

---
在 Python 很经常做的一件事就是 Python 数据类型和 JSON 数据类型的转换。

但是存在一个明显的问题，JSON 作为一种数据交换格式有固定的数据类型，但是 Python 作为编程语言除了内置的数据类型以为还能编写自定义的数据类型。

>  
 墙裂推荐：去看看 JSON 官网对 JSON 的介绍： 


比如你肯定遇到过类似的问题:

```
&gt;&gt;&gt; import json
&gt;&gt;&gt; import decimal
&gt;&gt;&gt; 
&gt;&gt;&gt; data = {'key1': 'string', 'key2': 10, 'key3': decimal.Decimal('1.45')}
&gt;&gt;&gt; json.dumps(data)
Traceback (most recent call last):
  File "&lt;input&gt;", line 1, in &lt;module&gt;
    json.dumps(data)
  File "/usr/lib/python3.6/json/__init__.py", line 231, in dumps
    return _default_encoder.encode(obj)
  File "/usr/lib/python3.6/json/encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "/usr/lib/python3.6/json/encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "/usr/lib/python3.6/json/encoder.py", line 180, in default
    o.__class__.__name__)
TypeError: Object of type 'Decimal' is not JSON serializable复制代码
```

那么问题就来了，如何把各种各样的 Python 数据类型转化成 JSON 数据类型。 一种很不 pythonic 的做法就是，先转换成某种能和 JSON 数据类型直接转换的值，然后在 dump，这么做很直接很暴力，但是在各种花式数据类型面前就很无力。

Google 是解决问题的重要方式之一，当你一顿搜索过后，你就会发现其实可以在 dumps 时 encode 这个阶段对数据进行转化。

所以你肯定是那么做的，完美地解决了问题。

```
&gt;&gt;&gt; class DecimalEncoder(json.JSONEncoder):
...     def default(self, obj):
...         if isinstance(obj, decimal.Decimal):
...             return float(obj)
...         return super(DecimalEncoder, self).default(obj)
...     
... 
&gt;&gt;&gt; 
&gt;&gt;&gt; json.dumps(data, cls=DecimalEncoder)
'{"key1": "string", "key2": 10, "key3": 1.45}'复制代码
```

### JSON 的 Encode 过程

>  
 文中代码摘自  
 删除了几乎所有的 docstring，由于代码太长，直接截取了重要片段。可以在片段最上方的链接查看完整的代码。 


熟悉 json 这个库的都知道基本只有4个常用的 API，分别是 dump、dumps 和 load、loads。

>  
 源码位于 cpython/Lib/json 中 


```
# https://github.com/python/cpython/blob/master/Lib/json/__init__.py#L183-L238

def dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kw):

     # cached encoder
    if (not skipkeys and ensure_ascii and
        check_circular and allow_nan and
        cls is None and indent is None and separators is None and
        default is None and not sort_keys and not kw):
        return _default_encoder.encode(obj)

    if cls is None:
        cls = JSONEncoder

    # 重点
    return cls(
        skipkeys=skipkeys, ensure_ascii=ensure_ascii,
        check_circular=check_circular, allow_nan=allow_nan, indent=indent,
        separators=separators, default=default, sort_keys=sort_keys,
        **kw).encode(obj)复制代码
```

直接看到最后的 return。可以发现如果不提供 cls 默认就使用 JSONEncoder，然后调用该类的实例方法 encode。

encode 方法也十分简单：

```
# https://github.com/python/cpython/blob/191e993365ac3206f46132dcf46236471ec54bfa/Lib/json/encoder.py#L182-L202
def encode(self, o):
    # str 类型直接 encode 后返回
    if isinstance(o, str):
        if self.ensure_ascii:
            return encode_basestring_ascii(o)
        else:
            return encode_basestring(o)

    # chunks 是数据中的各个部分
    chunks = self.iterencode(o, _one_shot=True)
    if not isinstance(chunks, (list, tuple)):
        chunks = list(chunks)
    return ''.join(chunks)复制代码
```

可以看出最后的我们得到 JSON 都是 chunks 拼接得到的，chunks 是调用 self.iterencode 方法得到的。

```
# https://github.com/python/cpython/blob/191e993365ac3206f46132dcf46236471ec54bfa/Lib/json/encoder.py#L204-257
    if (_one_shot and c_make_encoder is not None
            and self.indent is None):
        _iterencode = c_make_encoder(
            markers, self.default, _encoder, self.indent,
            self.key_separator, self.item_separator, self.sort_keys,
            self.skipkeys, self.allow_nan)
    else:
        _iterencode = _make_iterencode(
            markers, self.default, _encoder, self.indent, floatstr,
            self.key_separator, self.item_separator, self.sort_keys,
            self.skipkeys, _one_shot)
return _iterencode(o, 0)复制代码
```

iterencode 方法比较长，我们只关心最后几行。

返回值 `_iterencode`，是函数中 `c_make_encoder` 或者 `_make_iterencode` 这两个高阶函数的返回值。

`c_make_encoder` 是来自 `_json` 这个 module ，这个 module 是一个 c 模块，我们不去关心这个模块怎么实现的。 转去研究同等作用的 `_make_iterencode` 方法。

```
# https://github.com/python/cpython/blob/191e993365ac3206f46132dcf46236471ec54bfa/Lib/json/encoder.py#L259-441
def _iterencode(o, _current_indent_level):
    if isinstance(o, str):
        yield _encoder(o)
    elif o is None:
        yield 'null'
    elif o is True:
        yield 'true'
    elif o is False:
        yield 'false'
    elif isinstance(o, int):
        # see comment for int/float in _make_iterencode
        yield _intstr(o)
    elif isinstance(o, float):
        # see comment for int/float in _make_iterencode
        yield _floatstr(o)
    elif isinstance(o, (list, tuple)):
        yield from _iterencode_list(o, _current_indent_level)
    elif isinstance(o, dict):
        yield from _iterencode_dict(o, _current_indent_level)
    else:
        if markers is not None:
            markerid = id(o)
            if markerid in markers:
                raise ValueError("Circular reference detected")
            markers[markerid] = o
        o = _default(o)
        yield from _iterencode(o, _current_indent_level)
        if markers is not None:
            del markers[markerid]
return _iterencode复制代码
```

同样需要关心的只有返回的这个函数，代码里各种 if-elif-else 逐一把内置类型转换成 JSON 类型。 在对面无法识别的类型时候就使用了 `_default()` 这个方法，然后递归调用解析各个值。

`_default` 就是最前面那个被覆盖的 `default`。

到这里就可以完全了解 Python 是如何 encode 成 JSON 数据。

总结一下流程，`json.dumps()` 调用 JSONEncoder 的实例方法 `encode()`，随后使用 `iterencode()` 递归转化各种类型，最后把 chunks 拼接成字符串后返回。

### 优雅的解决方案

通过前面的流程分析之后，知道为什么继承 JSONEncoder 然后覆盖 default 方法就可以完成自定义类型解析了。

也许你以后需要解析 datetime 类型数据，你可定会那么做：

```
class ExtendJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)

        if isinstance(obj, datetime.datetime):
            return obj.strftime(DATETIME_FORMAT) 

        return super(ExtendJSONEncoder, self).default(obj)复制代码
```

最后调用父类是 `default()` 方法纯粹是为了触发异常。

Python 可以使用 singledispatch 来解决这种单泛型问题。

```
import json

from datetime import datetime
from decimal import Decimal
from functools import singledispatch

class MyClass:
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

# 创建三个非内置类型的实例
mc = MyClass('i am class MyClass ')
dm = Decimal('11.11')
dt = datetime.now()

@singledispatch
def convert(o):
    raise TypeError('can not convert type')

@convert.register(datetime)
def _(o):
    return o.strftime('%b %d %Y %H:%M:%S') 

@convert.register(Decimal)
def _(o):
    return float(o)

@convert.register(MyClass)
def _(o):
    return o.get_value()

class ExtendJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return convert(obj)
        except TypeError:
            return super(ExtendJSONEncoder, self).default(obj)

data = {
    'mc': mc,
    'dm': dm,
    'dt': dt
}

json.dumps(data, cls=ExtendJSONEncoder)

# {"mc": "i am class MyClass ", "dm": 11.11, "dt": "Nov 10 2017 17:31:25"}复制代码
```

这种写法比较符合设计模式的规范。假如以后有了新的类型，不用再修改 `ExtendJSONEncoder` 类，只需要添加适当的 singledispatch 方法就可以了， 比较 pythonic 。

如果你执意的想在类中添加 singledispatch 可以参考:  ，当然我仍然觉得还是不要写在类中比较好。
