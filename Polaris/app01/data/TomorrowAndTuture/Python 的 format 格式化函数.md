
--- 
title:  Python 的 format 格式化函数 
tags: []
categories: [] 

---
### 参数传递方式

基本语法是通过 {} 和 : 来代替以前的 % 。

```
&gt;&gt;&gt; "output {:.2f}".format(3.1415926)
'output 3.14'
&gt;&gt;&gt; "output %.2f" % 3.1415926
'output 3.14'

```

format 函数可以接受不限个参数，位置可以不按顺序。

```
&gt;&gt;&gt; "{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
'hello world'
&gt;&gt;&gt; "{0} {1}".format("hello", "world")  # 设置指定位置
'hello world'
&gt;&gt;&gt; "{1} {0} {1}".format("hello", "world")  # 设置指定位置
'world hello world'
```

也可以设置参数。

```
&gt;&gt;&gt; "name: {name}, address: {address}".format(name="Looking", address="somewhere")
'name: Looking, address: somewhere'

&gt;&gt;&gt; my_dict = {"name": "Looking", "address": "somewhere"}
&gt;&gt;&gt; "name: {name}, address: {address}".format(**my_dict)
'name: Looking, address: somewhere'

&gt;&gt;&gt; my_list = ["Looking", "somewhere"]
&gt;&gt;&gt; "name: {0[0]}, address: {0[1]}".format(my_list)
'name: Looking, address: somewhere'

&gt;&gt;&gt; my_list = ["Looking", "somewhere"]
&gt;&gt;&gt; "name: {0}, address: {1}".format(*my_list)
'name: Looking, address: somewhere'
```

其实，Python3.6 以后新出来的 f-string 也是很受欢迎的，用起来也很方便，大家可以多多尝试一下。

```
&gt;&gt;&gt; name = "Looking"
&gt;&gt;&gt; address = "somewhere"
&gt;&gt;&gt; "name: {name}, address: {address}"
'name: {name}, address: {address}'
&gt;&gt;&gt; f"name: {name}, address: {address}"
'name: Looking, address: somewhere'

&gt;&gt;&gt; my_dict = {"name": "Looking", "address": "somewhere"}
&gt;&gt;&gt; f"name: {my_dict['name']}, address: {my_dict['address']}"
'name: Looking, address: somewhere'

&gt;&gt;&gt; my_list = ["Looking", "somewhere"]
&gt;&gt;&gt; f"name: {my_list[0]}, address: {my_list[1]}"
'name: Looking, address: somewhere'

```

### 数字格式化

^, &lt;, &gt; 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。

+ 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格

b、d、o、x 分别是二进制、十进制、八进制、十六进制。

#### 默认保留六位小数

```
&gt;&gt;&gt; "output {:f}".format(3.1415926)
'output 3.141593'

```

#### 保留两位小数

```
&gt;&gt;&gt; "output {:.2f}".format(3.1415926)
'output 3.14'

```

#### 带符号保留两位小数

```
&gt;&gt;&gt; "output {:+.2f}".format(3.1415926)
'output +3.14'
&gt;&gt;&gt; "output {:+.2f}".format(-3.1415926)
'output -3.14'

```

#### 不带小数（可以理解为四舍五入）

```
&gt;&gt;&gt; "output {:.0f}".format(3.1415926)
'output 3'
&gt;&gt;&gt; "output {:.0f}".format(-3.1415926)
'output -3'
&gt;&gt;&gt; "output {:.0f}".format(2.71828)
'output 3'
&gt;&gt;&gt; "output {:.0f}".format(-2.71828)
'output -3'

```

#### 数字补零 (右对齐，填充左边, 宽度为3)

```
&gt;&gt;&gt; "output {:0&gt;3d}".format(3)
'output 003'

```

#### 空格填充 (右对齐，填充左边, 宽度为3) 

```
&gt;&gt;&gt; "output {: &gt;3d}".format(3)
'output   3'

```

#### 数字补零 (左对齐，填充右边, 宽度为3)

```
&gt;&gt;&gt; "output {:0&lt;3d}".format(3)
'output 300'
```

#### 空格填充 (左对齐，填充右边, 宽度为3) 

```
&gt;&gt;&gt; "output {: &lt;3d}".format(3)
'output 3  '

```

#### 以逗号分隔的数字格式

符合西方国家千分位的风格

```
&gt;&gt;&gt; "output {:,}".format(300000000000)
'output 300,000,000,000'

```

#### 百分比格式

```
&gt;&gt;&gt; "output {:.2%}".format(0.25)
'output 25.00%'
&gt;&gt;&gt; "output {:.3%}".format(0.25)
'output 25.000%'

```

#### 指数格式化

```
&gt;&gt;&gt; "output {:.2e}".format(2500000)
'output 2.50e+06'
```

#### 对齐方式（左对齐，居中，右对齐）

```
&gt;&gt;&gt; "output {: &lt;9d}".format(3)
'output 3        '
&gt;&gt;&gt; "output {: ^9d}".format(3)
'output     3    '
&gt;&gt;&gt; "output {: &gt;9d}".format(3)
'output         3'

```

#### 进制转换

python 进制的转换主要是利用十进制作为转换的过渡

带前缀

```
# 十进制转换为其他进制
&gt;&gt;&gt; bin(11)            # 二进制
'0b1011'
&gt;&gt;&gt; oct(11)            # 八进制
'0o13'
&gt;&gt;&gt; int(11)            # 十进制
11
&gt;&gt;&gt; hex(11)            # 十六进制
'0xb'


# 其他进制转换为十进制
&gt;&gt;&gt; int('0b1011', 2)   # 二进制
11
&gt;&gt;&gt; int('0o13', 8)     # 八进制
11
&gt;&gt;&gt; int('11', 10)      # 十进制
11
&gt;&gt;&gt; int('0xb', 16)     # 十六进制
11
```

不带前缀 

```
# 十进制转换为其他进制
&gt;&gt;&gt; "{:b}".format(11)  # 二进制
'1011'
&gt;&gt;&gt; "{:o}".format(11)  # 八进制
'13'
&gt;&gt;&gt; "{:d}".format(11)  # 十进制
'11'
&gt;&gt;&gt; "{:x}".format(11)  # 十六进制（小写）
'b'
&gt;&gt;&gt; "{:X}".format(11)  # 十六进制（大写）
'B'

irb(main):001:0&gt; 11.to_s(2)
=&gt; "1011"
irb(main):002:0&gt; 11.to_s(8)
=&gt; "13"
irb(main):003:0&gt; 11.to_s(10)
=&gt; "11"
irb(main):004:0&gt; 11.to_s(16)
=&gt; "b"

# 其他进制转换为十进制
&gt;&gt;&gt; int('1011', 2)     # 二进制
11
&gt;&gt;&gt; int('13', 8)       # 八进制
11
&gt;&gt;&gt; int('11', 10)      # 十进制
11
&gt;&gt;&gt; int('b', 16)       # 十六进制（小写）
11
&gt;&gt;&gt; int('B', 16)       # 十六进制（大写）
11
```



```
irb(main):001:0&gt; "%b" % 11
=&gt; "1011"
irb(main):002:0&gt; "%o" % 11
=&gt; "13"
irb(main):003:0&gt; "%d" % 11
=&gt; "11"
irb(main):004:0&gt; "%x" % 11
=&gt; "b"
irb(main):005:0&gt; "%X" % 11
=&gt; "B"


# 其他进制转换为十进制
irb(main):008:0&gt; '1011'.to_i(2)
=&gt; 11
irb(main):009:0&gt; '13'.to_i(8)
=&gt; 11
irb(main):010:0&gt; '11'.to_i(10)
=&gt; 11
irb(main):011:0&gt; 'b'.to_i(16)
=&gt; 11
irb(main):011:0&gt; 'B'.to_i(16)
=&gt; 11
```

哈哈，最后来个 Python 写的进度条 ^_^。

```
import sys
import time

bar_length = 100
for i in range(bar_length + 1):
    s="\r%3d%%[%s&gt;%s]"%(i,"="*i, ' '*(bar_length - i))   #\r表示回车但是不换行，利用这个原理进行百分比的刷新
    sys.stdout.write(s)       #向标准输出终端写内容
    sys.stdout.flush()        #立即将缓存的内容刷新到标准输出
    time.sleep(0.1)           #设置延迟查看效果
print()

```

```
[root@master python3_learning]# python3 test.py
100%[====================================================================================================&gt;]
```


