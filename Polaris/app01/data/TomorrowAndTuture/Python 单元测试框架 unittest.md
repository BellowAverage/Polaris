
--- 
title:  Python 单元测试框架 unittest 
tags: []
categories: [] 

---
虽然并不是专门做测试的，但是测试方面的知识涉猎一下还是没什么坏处的。

具体细节的可以访问官网文档查看：

常用的断言方法： 

| Method | Checks that 
|------
|  | `a == b` 

`a == b`
|  | `a != b` 

`a != b`
|  | `bool(x) is True` 

`bool(x) is True`
|  | `bool(x) is False` 

`bool(x) is False`
|  | `a is b` 

`a is b`
|  | `a is not b` 

`a is not b`
|  | `x is None` 

`x is None`
|  | `x is not None` 

`x is not None`
|  | `a in b` 

`a in b`
|  | `a not in b` 

`a not in b`
|  | `isinstance(a, b)` 

`isinstance(a, b)`
|  | `not isinstance(a, b)` 

`not isinstance(a, b)`

### 基本实例

继承  就创建了一个测试样例。每个独立的测试是类的方法，这些方法的命名都以 `test` 开头。 这个命名约定告诉测试运行者类的哪些方法表示测试。如果类里边的函数不是以 test 开头，那么单元测试的时候是不会主动去执行这个函数的。

通过  和  方法，可以设置测试开始前与完成后需要执行的指令。**注意**：测试框架会自动地为**每个单独测试**调用前置方法。

```
import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()

```

在调用测试脚本时添加 `-v` 参数使  显示更为详细的信息（比如说测试的哪个类的哪个方法）：

```
[root@master ~]# python3 -m unittest test
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK

[root@master ~]# python3 -m unittest -v test
test_isupper (test.TestStringMethods) ... ok
test_split (test.TestStringMethods) ... ok
test_upper (test.TestStringMethods) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK

```

### 命令行接口

unittest 模块可以通过命令行运行模块、类和独立测试方法的测试:

```
[root@master ~]# python3 -m unittest test
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
[root@master ~]# python3 -m unittest test.TestStringMethods.test_isupper
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
[root@master ~]# python3 -m unittest -v test.TestStringMethods.test_isupper
test_isupper (test.TestStringMethods) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
[root@master ~]# python3 -m unittest -h
usage: python3 -m unittest [-h] [-v] [-q] [--locals] [-f] [-c] [-b]
                           [-k TESTNAMEPATTERNS]
                           [tests [tests ...]]

positional arguments:
  tests                a list of any number of test modules, classes and test
                       methods.

optional arguments:
  -h, --help           show this help message and exit
  -v, --verbose        Verbose output
  -q, --quiet          Quiet output
  --locals             Show local variables in tracebacks
  -f, --failfast       Stop on first fail or error
  -c, --catch          Catch Ctrl-C and display results so far
  -b, --buffer         Buffer stdout and stderr during tests
  -k TESTNAMEPATTERNS  Only run tests which match the given substring

Examples:
  python3 -m unittest test_module               - run tests from test_module
  python3 -m unittest module.TestClass          - run tests from module.TestClass
  python3 -m unittest module.Class.test_method  - run specified test method
  python3 -m unittest path/to/test_file.py      - run tests from test_file.py

...

For test discovery all test modules must be importable from the top level
directory of the project.

```

### 探索性测试

其实简单理解就是，一个目录下可能有多个单元测试的脚步，自己一个个去跑脚本显然比较麻烦，用探索性测试就可以让它自己去定位哪些脚本里边有测试样例，并且主动去进行测试。

```
[root@master ~]# python3 -m unittest discover /root
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
[root@master ~]# python3 -m unittest discover /root/test

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
[root@master ~]# mv ttt.txt test2.py
[root@master ~]# python3 -m unittest discover /root/
....F
======================================================================
FAIL: test_lower (test2.TestStringMethods)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/root/test2.py", line 7, in test_lower
    self.assertEqual('foo'.lower(), 'FOO')
AssertionError: 'foo' != 'FOO'
- foo
+ FOO


----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=1)

```

### 跳过测试和预计失败

#### 跳过测试

有时候我们可能不想去测试某个测试方法，这时候就可以 @unittest.skip() 去装饰那个要跳过的测试方法了。

```
import unittest


class TestStringMethods(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()

```

```
.s.
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK (skipped=1)
```

#### 预计失败

**@unittest.expectedFailure 这块和 @unittest.skip() 不同的是，skip 会跳过测试，但 expectedFailure 还是继续会进行测试的。**只不过如果测试失败的话，不会影响最后的测试结果（毕竟和预期失败的结果相符）；如果 **expectedFailure **预期失败，测试却反而成功的话，会得到类似如下提示：

```
FAILED (unexpected successes=1)
```

如果提前知道某个测试方法通不过测试，但是又不想让它影响最后的测试结果，就可以使用装饰器把它标注成 “预期失败”：

```
import unittest


class TestStringMethods(unittest.TestCase):

    @unittest.expectedFailure
    def test_nothing(self):
        self.fail("shouldn't happen")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()

```

```
.x.
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK (expected failures=1)
```


