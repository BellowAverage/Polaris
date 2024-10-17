
--- 
title:  Pythonmock基本使用 
tags: []
categories: [] 

---
什么是mock?

 

mock在翻译过来有模拟的意思。这里要介绍的mock是辅助单元测试的一个模块。它允许您用模拟对象替换您的系统的部分，并对它们已使用的方式进行断言。

 

在Python2.x 中 mock是一个单独模块，需要单独安装。

 

&gt; pip install -U mock

 

在Python3.x中，mock已经被集成到了unittest单元测试框架中，所以，可以直接使用。

 

　　可能你和我初次接触这个概念的时候会有这样的疑问：把要测的东西都模拟掉了还测试什么呢？

 

　　但在，实际生产中的项目是非常复杂的，对其进行单元测试的时候，会遇到以下问题：

 

接口的依赖

外部接口调用

测试环境非常复杂

　　单元测试应该只针对当前单元进行测试, 所有的内部或外部的依赖应该是稳定的, 已经在别处进行测试过的.使用mock 就可以对外部依赖组件实现进行模拟并且替换掉, 从而使得单元测试将焦点只放在当前的单元功能。

 

简单的例子                                                        

 

我们先从最简单例子开始。

 

modular.py

 

#modular.py

 

class Count():

 

    def add(self):

        pass

这里要实现一个Count计算类，add() 方法要实现两数相加。但，这个功能我还没有完成。这时就可以借助mock对其进行测试。

 

mock_demo01.py

 

from unittest import mock

import unittest

 

from modular import Count

 

# test Count class

class TestCount(unittest.TestCase):

 

    def test_add(self):

        count = Count()

        count.add = mock.Mock(return_value=13)

        result = count.add(8,5)

        self.assertEqual(result,13)

 

 

if __name__ == '__main__':

    unittest.main()

　　count = Count()

 

　　首先，调用被测试类Count() 。

 

　　count.add = mock.Mock(return_value=7)

 

　　通过Mock类模拟被调用的方法add()方法，return_value 定义add()方法的返回值。

 

　　result = count.add(2,5)

 

　　接下来，相当于在正常的调用add()方法，传两个参数2和5，然后会得到相加的结果7。然后，7的结果是我们在上一步就预先设定好的。

 

　　self.assertEqual(result,7)

 

　　最后，通过assertEqual()方法断言，返回的结果是否是预期的结果7。

 

 　 运行测试结果：

 

&gt; python3 mock_demo01.py

.

----------------------------------------------------------------------

Ran 1 test in 0.000s

 

OK

这样一个用例就在mock的帮助下编写完成，并且测试通过了。

 

完成功能测试                                                     

 

 　　再接下来完成module.py文件中add()方法。

 

#module.py

 

class Count():

 

    def add(self, a, b):

        return a + b

　　然后，修改测试用例：

 

from unittest import mock

import unittest

from module import Count

 

 

class MockDemo(unittest.TestCase):

 

    def test_add(self):

        count = Count()

        count.add = mock.Mock(return_value=13, side_effect=count.add)

        result = count.add(8, 8)

        print(result)

        count.add.assert_called_with(8, 8)

        self.assertEqual(result, 16)

 

if __name__ == '__main__':

    unittest.main()

  　count.add = mock.Mock(return_value=13, side_effect=count.add)

 

　　side_effect参数和return_value是相反的。它给mock分配了可替换的结果，覆盖了return_value。简单的说，一个模拟工厂调用将返回side_effect值，而不是return_value。

 

　　所以，设置side_effect参数为Count类add()方法，那么return_value的作用失效。

 

　　result = count.add(8, 8)

 

　　print(result)

 

　　这次将会真正的调用add()方法，得到的返回值为16（8+8）。通过print打印结果。

 

　　assert_called_with(8,8)

 

　　检查mock方法是否获得了正确的参数。

 

解决测试依赖                                                     

 

 　 前面的例子，只为了让大家对mock有个初步的印象。再接来，我们看看如何mock方法的依赖。

 

　　例如，我们要测试A模块，然后A模块依赖于B模块的调用。但是，由于B模块的改变，导致了A模块返回结果的改变，从而使A模块的测试用例失败。其实，对于A模块，以及A模块的用例来说，并没有变化，不应该失败才对。

 

　　这个时候就是mock发挥作用的时候了。通过mock模拟掉影响A模块的部分（B模块）。至于mock掉的部分（B模块）应该由其它用例来测试。

 

# function.py

def add_and_multiply(x, y):

    addition = x + y

    multiple = multiply(x, y)

    return (addition, multiple)

 

 

def multiply(x, y):

    return x * y

  　　然后，针对 add_and_multiply()函数编写测试用例。func_test.py

 

import unittest

import function

 

 

class MyTestCase(unittest.TestCase):

 

    def test_add_and_multiply(self):

        x = 3

        y = 5

        addition, multiple = function.add_and_multiply(x, y)

        self.assertEqual(8, addition)

        self.assertEqual(15, multiple)

 

 

if __name__ == "__main__":

    unittest.main()

 运行结果：

 

&gt; python3 func_test.py

.

----------------------------------------------------------------------

Ran 1 test in 0.000s

 

OK

　　目前运行一切正确常，然而，add_and_multiply()函数依赖了multiply()函数的返回值。如果这个时候修改multiply()函数的代码。

 

……

def multiply(x, y):

    return x * y + 3

　　这个时候，multiply()函数返回的结果变成了x*y加3。

 

　　再次运行测试：

 

&gt; python3 func_test.py                                                   

F                                                                       

======================================================================  

FAIL: test_add_and_multiply (__main__.MyTestCase)                       

----------------------------------------------------------------------  

Traceback (most recent call last):                                      

  File "fun_test.py", line 19, in test_add_and_multiply                 

    self.assertEqual(15, multiple)                                      

AssertionError: 15 != 18                                                

                                                                        

----------------------------------------------------------------------  

Ran 1 test in 0.000s                                                    

                                                                        

FAILED (failures=1)   

　　测试用例运行失败了，然而，add_and_multiply()函数以及它的测试用例并没有做任何修改，罪魁祸首是multiply()函数引起的，我们应该把 multiply()函数mock掉。

 

import unittest

from unittest.mock import patch

import function

 

 

class MyTestCase(unittest.TestCase):

 

    @patch("function.multiply")

    def test_add_and_multiply2(self, mock_multiply):

        x = 3

        y = 5

        mock_multiply.return_value = 15

        addition, multiple = function.add_and_multiply(x, y)

        mock_multiply.assert_called_once_with(3, 5)

 

        self.assertEqual(8, addition)

        self.assertEqual(15, multiple)

 

 

if __name__ == "__main__":

    unittest.main()

　　@patch("function.multiply")

 

　　patch()装饰/上下文管理器可以很容易地模拟类或对象在模块测试。在测试过程中，您指定的对象将被替换为一个模拟（或其他对象），并在测试结束时还原。

 

　　这里模拟function.py文件中multiply()函数。

 

　　def test_add_and_multiply2(self, mock_multiply):

 

　　在定义测试用例中，将mock的multiply()函数（对象）重命名为 mock_multiply对象。

 

　　mock_multiply.return_value = 15

 

　　设定mock_multiply对象的返回值为固定的15。

 

　　ock_multiply.assert_called_once_with(3, 5)

 

　　检查ock_multiply方法的参数是否正确。

 

　　再次，运行测试用例，通过！
