
--- 
title:  Python 基础（二十）：sys 模块 
tags: []
categories: [] 

---


#### 目录
- - 


## 1. 简介

sys 模块主要负责与 Python 解释器进行交互，该模块提供了一系列用于控制 Python 运行环境的函数和变量。

之前我们说过 ，该模块与 sys 模块从名称上看着好像有点类似，实际上它们之间是没有什么关系的，os 模块主要负责与操作系统进行交互。

## 2. 使用

我们先整体看一下 sys 模块都包含哪些内容，如下所示：

```
&gt;&gt;&gt; import sys
&gt;&gt;&gt; dir(sys)
['__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_getframe', '_git', '_home', '_xoptions', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_wrapper', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'set_asyncgen_hooks', 'set_coroutine_wrapper', 'setcheckinterval', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 'version_info', 'warnoptions', 'winver']

```

对于一些相对常用的变量和函数，我们下面再来具体看一下。

**argv** 返回传递给 Python 脚本的命令行参数列表。看下示例：

```
import sys

if __name__ == '__main__':
    args = sys.argv
    print(args)
    print(args[1])

```

上面文件名为：test.py，我们在控制台使用命令：`python test.py 123 abc` 执行一下，执行结果如下：

```
['test.py', '123', 'abc']
123

```

**version** 返回 Python 解释器的版本信息。

**winver** 返回 Python 解释器主版号。

**platform** 返回操作系统平台名称。

**path** 返回模块的搜索路径列表。

**maxsize** 返回支持的最大整数值。

**maxunicode** 返回支持的最大 Unicode 值。

**copyright** 返回 Python 版权信息。

**modules** 以字典类型返回系统导入的模块。

**byteorder** 返回本地字节规则的指示器。

**executable** 返回 Python 解释器所在路径。

```
import sys

print(sys.version)
print(sys.winver)
print(sys.platform)
print(sys.path)
print(sys.maxsize)
print(sys.maxunicode)
print(sys.copyright)
print(sys.modules)
print(sys.byteorder)
print(sys.executable)

```

**stdout** 标准输出。看下示例：

```
import sys

# 下面两行代码等价
sys.stdout.write('Hi' + '\n')
print('Hi')

```

**stdin** 标准输入。看下示例：

```
import sys

s1 = input()
s2 = sys.stdin.readline()
print(s1)
print(s2)

```

**stderr** 错误输出。看下示例：

```
import sys

sys.stderr.write('this is a error message')

```

**exit()** 退出当前程序。看下示例：

```
import sys

print('Hi')
sys.exit()
print('Jhon')

```

**getdefaultencoding()** 返回当前默认字符串编码的名称。

**getrefcount(obj)** 返回对象的引用计数。

**getrecursionlimit()** 返回支持的递归深度。

**getsizeof(object[, default])** 以字节为单位返回对象的大小。

**setswitchinterval(interval)** 设置线程切换的时间间隔。

**getswitchinterval()** 返回线程切换时间间隔。

```
import sys

print(sys.getdefaultencoding())
print(sys.getrefcount('123456'))
print(sys.getrecursionlimit())
print(sys.getsizeof('abcde'))
sys.setswitchinterval(1)
print(sys.getswitchinterval())

```

<img src="https://img-blog.csdnimg.cn/20200127132036938.png#pic_center" alt="" width="600">
