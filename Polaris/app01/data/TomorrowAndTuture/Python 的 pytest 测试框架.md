
--- 
title:  Python 的 pytest 测试框架 
tags: []
categories: [] 

---
说到 pytest，大家总不免要拿来和 unittest 来比一下，但是 unittest 毕竟是标准库，兼容性方面肯定没得说，但要论简洁和方便的话，pytest 也是不落下风的。

### 简单测试示例

```
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5

```

```
Testing started at 15:57 ...
Launching pytest with arguments test.py::test_answer --no-header --no-summary -q in D:\Projects\insight-tools-rest

============================= test session starts =============================
collecting ... collected 1 item

test.py::test_answer FAILED                                              [100%]
test.py:4 (test_answer)
4 != 5

Expected :5
Actual   :4
&lt;Click to see difference&gt;

def test_answer():
&gt;       assert func(3) == 5
E       assert 4 == 5

test.py:6: AssertionError


============================== 1 failed in 0.13s ==============================

Process finished with exit code 1
```

### 断言某类异常

```
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()

```

```
[root@master ~]# pytest test.py
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.6.8, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /root
collected 1 item                                                                                                                                                               

test.py .                                                                                                                                                                [100%]

============================================================================== 1 passed in 0.01s ===============================================================================

[root@master ~]# pytest -q test.py
.                                                                                                                                                                        [100%]
1 passed in 0.00s

```

### 将多个测试分组到类

```
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
```

```
[root@master ~]# pytest -q test.py
.F                                                                                                                                                                       [100%]
=================================================================================== FAILURES ===================================================================================
______________________________________________________________________________ TestClass.test_two ______________________________________________________________________________

self = &lt;test.TestClass object at 0x7ff2dec24390&gt;

    def test_two(self):
        x = "hello"
&gt;       assert hasattr(x, "check")
E       AssertionError: assert False
E        +  where False = hasattr('hello', 'check')

test.py:8: AssertionError
=========================================================================== short test summary info ============================================================================
FAILED test.py::TestClass::test_two - AssertionError: assert False
1 failed, 1 passed in 0.02s

```

在类中对测试分组时需要注意的是，每个测试都有一个唯一的类实例。让每个测试共享同一个类实例将非常不利于测试隔离（添加到类层级的属性会被所有 test 共享）。

```

class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1

```

```
[root@master ~]# pytest -q test.py
.F                                                                                                                                                                       [100%]
=================================================================================== FAILURES ===================================================================================
________________________________________________________________________ TestClassDemoInstance.test_two ________________________________________________________________________

self = &lt;test.TestClassDemoInstance object at 0x7f22110f44e0&gt;

    def test_two(self):
&gt;       assert self.value == 1
E       assert 0 == 1
E        +  where 0 = &lt;test.TestClassDemoInstance object at 0x7f22110f44e0&gt;.value

test.py:9: AssertionError
=========================================================================== short test summary info ============================================================================
FAILED test.py::TestClassDemoInstance::test_two - assert 0 == 1
1 failed, 1 passed in 0.02s

```

### 指定测试

#### **在模块中运行测试**

```
pytest test.py
```

```
[root@master ~]# pytest -q test.py
.F                                                                                                                                                                       [100%]
=================================================================================== FAILURES ===================================================================================
________________________________________________________________________ TestClassDemoInstance.test_two ________________________________________________________________________

self = &lt;test.TestClassDemoInstance object at 0x7f3395b78470&gt;

    def test_two(self):
&gt;       assert self.value == 1
E       assert 0 == 1
E        +  where 0 = &lt;test.TestClassDemoInstance object at 0x7f3395b78470&gt;.value

test.py:9: AssertionError
=========================================================================== short test summary info ============================================================================
FAILED test.py::TestClassDemoInstance::test_two - assert 0 == 1
1 failed, 1 passed in 0.02s

```

#### 在模块中运行特定测试

```
pytest test.py::TestClassDemoInstance::test_one

```

```
[root@master ~]# pytest -q test.py::TestClassDemoInstance::test_one
.                                                                                                                                                                        [100%]
1 passed in 0.01s
```

#### **在目录中运行测试**

```
pytest testing/
```

#### **按关键字表达式运行测试**

```
pytest -k "MyClass and not method"
```

```
[root@master ~]# pytest -q test.py -k 'one'
.                                                                                                                                                                        [100%]
1 passed, 1 deselected in 0.01s

[root@master ~]# pytest -q test.py -k 'two'
F                                                                                                                                                                        [100%]
=================================================================================== FAILURES ===================================================================================
________________________________________________________________________ TestClassDemoInstance.test_two ________________________________________________________________________

self = &lt;test.TestClassDemoInstance object at 0x7fbbe853e908&gt;

    def test_two(self):
&gt;       assert self.value == 1
E       assert 0 == 1
E        +  where 0 = &lt;test.TestClassDemoInstance object at 0x7fbbe853e908&gt;.value

test.py:9: AssertionError
=========================================================================== short test summary info ============================================================================
FAILED test.py::TestClassDemoInstance::test_two - assert 0 == 1
1 failed, 1 deselected in 0.02s

```

### 关于预期异常的断言

```
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

```

```
root@master ~# pytest test.py
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.6.8, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /root
collected 1 item                                                                                                                                                               

test.py .                                                                                                                                                                [100%]

============================================================================== 1 passed in 0.02s ===============================================================================
```

通过 `match` 上下文管理器的关键字参数，用于测试正则表达式是否匹配异常的字符串表示形式（如果能正常匹配，则可以通过测试）：

```
import pytest


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    #with pytest.raises(ValueError, match=r".* 123 .*"):
    with pytest.raises(ValueError, match=r".* 124 .*"):
        myfunc()
```

```
root@master ~# pytest -q test.py
F                                                                                                                                                                        [100%]
=================================================================================== FAILURES ===================================================================================
__________________________________________________________________________________ test_match __________________________________________________________________________________

    def test_match():
        #with pytest.raises(ValueError, match=r".* 123 .*"):
        with pytest.raises(ValueError, match=r".* 124 .*"):
&gt;           myfunc()

test.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def myfunc():
&gt;       raise ValueError("Exception 123 raised")
E       ValueError: Exception 123 raised

test.py:5: ValueError

During handling of the above exception, another exception occurred:

    def test_match():
        #with pytest.raises(ValueError, match=r".* 123 .*"):
        with pytest.raises(ValueError, match=r".* 124 .*"):
&gt;           myfunc()
E           AssertionError: Regex pattern '.* 124 .*' does not match 'Exception 123 raised'.

test.py:11: AssertionError
=========================================================================== short test summary info ============================================================================
FAILED test.py::test_match - AssertionError: Regex pattern '.* 124 .*' does not match 'Exception 123 raised'.
1 failed in 0.02s

```

```
def test_set_comparison():
    set1 = set("1308")
    set2 = set("8035")
    assert set1 == set2

```

```
root@master ~# pytest -q test.py
F                                                                                                                                                                        [100%]
=================================================================================== FAILURES ===================================================================================
_____________________________________________________________________________ test_set_comparison ______________________________________________________________________________

    def test_set_comparison():
        set1 = set("1308")
        set2 = set("8035")
&gt;       assert set1 == set2
E       AssertionError: assert {'0', '1', '3', '8'} == {'0', '3', '5', '8'}
E         Extra items in the left set:
E         '1'
E         Extra items in the right set:
E         '5'
E         Full diff:
E         - {'3', '8', '0', '5'}
E         + {'8', '3', '1', '0'}

test.py:4: AssertionError
=========================================================================== short test summary info ============================================================================
FAILED test.py::test_set_comparison - AssertionError: assert {'0', '1', '3', '8'} == {'0', '3', '5', '8'}
1 failed in 0.02s

```

使用 pytest.raises 断言给定的异常

```
import pytest

@pytest.mark.xfail(raises=IndexError)
def test_f():
    a = [1, 2]
    print(a[0])

```

```
root@master ~# pytest -q test.py
X                                                                                                                                                                        [100%]
1 xpassed in 0.01s

```

```
import pytest

@pytest.mark.xfail(raises=IndexError)
def test_f():
    a = [1, 2]
    print(a[2])

```

```
root@master ~# pytest -q test.py
x                                                                                                                                                                        [100%]
1 xfailed in 0.02s

```

也可以使用 pytest.warns 检查代码是否引发了特定的警告

### 固定装置 @pytest.fixture

fixture 是 pytest 的特色，这个我就不多说了。不过，要怎么理解这个 @pytest.fixture 装饰的函数呢？

**正常来说，像下面的例子，如果函数 test_string 直接把输入 order 当成一个普通的参数的话，肯定是会报错的（毕竟，谁也不知道你这个 order 是什么东东）。但使用了 @pytest.fixture 装饰 order 以后，就完全不一样了，这时候，test_string 的输入参数 order 其实是可以看成函数 order 执行返回后的结果重新赋值给了 order 参数（这也很符合装饰器的特点）。因此，@pytest.fixture 装饰的测试函数的参数相当于是一个已定义函数执行后的结果。**

```
import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]

```

```

def first_entry():
    return "a"


def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]


entry = first_entry()
the_list = order(first_entry=entry)
test_string(order=the_list)

```

固定装置有很多特点，比如装置和使用其他装置，也可以重复使用，测试函数和装置也可以请求一次安装多个装置。

固定装置也可以在同一测试期间多次执行，pytest不会为该测试再次执行它们（而是使用第一次执行后的缓存结果），比如下面的例子：

```
import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order():
    return []


# Act
@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string1(append_first, order, first_entry):
    # Assert
    assert order == [first_entry]

def test_string2(order, first_entry):
    # Assert
    assert order == []

```

test_string1 和 test_string2 哪个会通过测试呢？答案是：两个都会通过测试。

```
root@master ~# pytest -q test.py
..                                                                                                                                                                       [100%]
2 passed in 0.01s

```

但是为什么呢？因为对于 test_string1 而言，append_first 使用了固定装置 order 后， order 已经不再是空列表了，即使 test_string1 也有使用 order，但是这个 order 只是第一次 order 被执行后的结果的引用，而不会真正去执行一遍 order 固定装置。test_string2 的话就好理解一些了。
