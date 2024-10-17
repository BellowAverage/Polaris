
--- 
title:  c与c++的struct区别 
tags: []
categories: [] 

---
看了一些文章，总结了大概这四点，实际上是三点，两外一点说的是C++中的struct和class的区别
- **1.** C++中struct是抽象数据类型(ADT)，可以将struct当成类来处理，可以包含类的所有东西，比如构造函数、析构函数、友元等，可以继承也可以实现多态，只是因为有了class一般不用。C语言中：struct是用户自定义数据类型(UDT)，C语言struct不是类，不可以有函数，没有权限设置也不能使用类的特征例如public等关键字，是一些变量的集合体，可以封装数据却不可以隐藏数据。- **2.** C++ struct里面成员初始化的形式和类是相同的，不可以直接初始化，就是不可以定义成员的时候同时初始化。C语言中struct中的某个类型（例如int）不可以直接初始化。- **3.** C++中struct和class的区别 （1）class中的成员默认是private，而struct的成员默认为public。 （2）class默认的继承方式是private，而struct的默认继承方式是public。 （3）class还可以用于表示模板类型，struct则不行。在用模版的时候只能写template 或template不能写template 。- **4.** struct作为类的一种特例是用来自定义数据结构的。一个结构标记声明后，在C中必须在结构标记前加上struct，才能做结构类型名