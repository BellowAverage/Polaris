
--- 
title:  C++ 模版类和模板函数介绍及使用 
tags: []
categories: [] 

---
### 1. 简介
- 模板是C++支持参数化多态的工具，使用模板可以使用户为类或者函数声明一种一般模式，使得类中的某些数据成员或者成员函数的参数、返回值取得任意类型。- 模板是泛型编程的基础，泛型编程即以一种独立于任何特定类型的方式编写代码。- 模板是创建泛型类或函数的蓝图或公式。库容器，比如迭代器和算法，都是泛型编程的例子，它们都使用了模板的概念。- 每个容器都有一个单一的定义，比如 向量，我们可以定义许多不同类型的向量，比如 vector 或 vector 。
#### 1.1 说明
- 模板是一种对类型进行参数化的工具；- 通常有两种形式：函数模板和类模板；- 函数模板针对仅参数类型不同的函数；- 类模板针对仅数据成员和成员函数类型不同的类。
#### 1.2 使用模版目的

能够让我们编写与类型无关的代码。比如编写了一个交换两个整型int 类型的swap函数，这个函数就只能实现int 型，对double，字符这些类型无法实现，要实现这些类型的交换就要重新编写另一个swap函数。使用模板的目的就是要让这程序的实现与类型无关，比如一个swap模板函数，即可以实现int 型，又可以实现double型的交换。模板可以应用于函数和类。

#### 1.3 使用注意

模板的声明或定义只能在全局，命名空间或类范围内进行。即不能在局部范围，函数内进行，比如不能在main函数中声明或定义一个模板。

### 2. 函数模版

#### 2.1 函数模板的格式：

```
template &lt;typename type&gt; ret-type func-name(parameter list)
{<!-- -->
   // 函数的主体
}

```

其中template和class是关见字，class可以用typename 关见字代替，在这里typename 和class没区别，&lt;&gt;括号中的参数叫模板形参，模板形参和函数形参很相像，模板形参不能为空。一但声明了模板函数就可以用模板函数的形参名声明类中的成员变量和成员函数，即可以在该函数中使用内置类型的地方都可以使用模板形参名。模板形参需要调用该模板函数时提供的模板实参来初始化模板形参，一旦编译器确定了实际的模板实参类型就称他实例化了函数模板的一个实例。比如swap的模板函数形式为:

```
template &lt;class T&gt; void swap(T&amp; a, T&amp; b){<!-- -->}

```

当调用这样的模板函数时类型T就会被被调用时的类型所代替，比如swap(a,b)其中a和b是int 型，这时模板函数swap中的形参T就会被int 所代替，模板函数就变为swap(int &amp;a, int &amp;b)。而当swap(c,d)其中c和d是double类型时，模板函数会被替换为swap(double &amp;a, double &amp;b)，这样就实现了函数的实现与类型无关的代码。

```
#include &lt;iostream&gt;
#include &lt;string&gt;
 
using namespace std;
 
template &lt;typename T&gt;
inline T const&amp; Max (T const&amp; a, T const&amp; b) 
{<!-- --> 
    return a &lt; b ? b:a; 
} 
int main ()
{<!-- -->
 
    int i = 39;
    int j = 20;
    cout &lt;&lt; "Max(i, j): " &lt;&lt; Max(i, j) &lt;&lt; endl; 
 
    double f1 = 13.5; 
    double f2 = 20.7; 
    cout &lt;&lt; "Max(f1, f2): " &lt;&lt; Max(f1, f2) &lt;&lt; endl; 
 
    string s1 = "Hello"; 
    string s2 = "World"; 
    cout &lt;&lt; "Max(s1, s2): " &lt;&lt; Max(s1, s2) &lt;&lt; endl; 
 
    return 0;
}

```

结果：

```
Max(i, j): 39
Max(f1, f2): 20.7
Max(s1, s2): World

```

#### 2.2 注意

对于函数模板而言不存在 h(int,int) 这样的调用，不能在函数调用的参数中指定模板形参的类型，对函数模板的调用应使用实参推演来进行，即只能进行 h(2,3) 这样的调用，或者int a, b; h(a,b)。

### 3. 类模版

#### 3.1 类模板的格式为：

```
template&lt;class  形参名，class 形参名，…&gt;   class 类名
{<!-- --> ... };

```

类模板和函数模板都是以template开始后接模板形参列表组成，模板形参不能为空，一但声明了类模板就可以用类模板的形参名声明类中的成员变量和成员函数，即可以在类中使用内置类型的地方都可以使用模板形参名来声明。比如

```
template&lt;class T&gt; class A{<!-- -->public: T a; T b; T hy(T c, T &amp;d);};

```

在类A中声明了两个类型为T的成员变量a和b，还声明了一个返回类型为T带两个参数类型为T的函数hy。

```
#include &lt;iostream&gt;
#include &lt;vector&gt;
#include &lt;cstdlib&gt;
#include &lt;string&gt;
#include &lt;stdexcept&gt;
 
using namespace std;
 
template &lt;class T&gt;
class Stack {<!-- --> 
  private: 
    vector&lt;T&gt; elems;     // 元素 
 
  public: 
    void push(T const&amp;);  // 入栈
    void pop();               // 出栈
    T top() const;            // 返回栈顶元素
    bool empty() const{<!-- -->       // 如果为空则返回真。
        return elems.empty(); 
    } 
}; 
 
template &lt;class T&gt;
void Stack&lt;T&gt;::push (T const&amp; elem) 
{<!-- --> 
    // 追加传入元素的副本
    elems.push_back(elem);    
} 
 
template &lt;class T&gt;
void Stack&lt;T&gt;::pop () 
{<!-- --> 
    if (elems.empty()) {<!-- --> 
        throw out_of_range("Stack&lt;&gt;::pop(): empty stack"); 
    }
    // 删除最后一个元素
    elems.pop_back();         
} 
 
template &lt;class T&gt;
T Stack&lt;T&gt;::top () const 
{<!-- --> 
    if (elems.empty()) {<!-- --> 
        throw out_of_range("Stack&lt;&gt;::top(): empty stack"); 
    }
    // 返回最后一个元素的副本 
    return elems.back();      
} 
 
int main() 
{<!-- --> 
    try {<!-- --> 
        Stack&lt;int&gt;         intStack;  // int 类型的栈 
        Stack&lt;string&gt; stringStack;    // string 类型的栈 
 
        // 操作 int 类型的栈 
        intStack.push(7); 
        cout &lt;&lt; intStack.top() &lt;&lt;endl; 
 
        // 操作 string 类型的栈 
        stringStack.push("hello"); 
        cout &lt;&lt; stringStack.top() &lt;&lt; std::endl; 
        stringStack.pop(); 
        stringStack.pop(); 
    } 
    catch (exception const&amp; ex) {<!-- --> 
        cerr &lt;&lt; "Exception: " &lt;&lt; ex.what() &lt;&lt;endl; 
        return -1;
    } 
}

```

结果：

```
7
hello
Exception: Stack&lt;&gt;::pop(): empty stack

```

#### 3.2 类模板对象的创建

比如一个模板类A，则使用类模板创建对象的方法为A m;在类A后面跟上一个&lt;&gt;尖括号并在里面填上相应的类型，这样的话类A中凡是用到模板形参的地方都会被int 所代替。当类模板有两个模板形参时创建对象的方法为A&lt;int, double&gt; m;类型之间用逗号隔开。

#### 3.3 对于类模板，模板形参的类型必须在类名后的尖括号中明确指定。

比如A&lt;2&gt; m;用这种方法把模板形参设置为int是错误的（编译错误：error C2079: ‘a’ uses undefined class ‘A’），类模板形参不存在实参推演的问题。也就是说不能把整型值2推演为int 型传递给模板形参。要把类模板形参调置为int 型必须这样指定A m。

#### 3.4 在类模板外部定义成员函数的方法为：

template&lt;模板形参列表&gt; 函数返回类型 类名&lt;模板形参名&gt;::函数名(参数列表){函数体}， 比如有两个模板形参T1，T2的类A中含有一个void h()函数，则定义该函数的语法为：

template&lt;class T1,class T2&gt; void A&lt;T1,T2&gt;::h(){}。 注意：当在类外面定义类的成员时template后面的模板形参应与要定义的类的模板形参一致。

#### 3.5 再次提醒注意

模板的声明或定义只能在全局，命名空间或类范围内进行。即不能在局部范围，函数内进行，比如不能在main函数中声明或定义一个模板。

### 4 模板的形参

有三种类型的模板形参：类型形参，非类型形参和模板形参。

#### 4.1 类型形参
- 类型形参由关见字class或typename后接说明符构成，如template void h(T a){};其中T就是一个类型形参，类型形参的名字由用户自已确定。模板形参表示的是一个未知的类型。模板类型形参可作为类型说明符用在模板中的任何地方，与内置类型说明符或类类型说明符的使用方式完全相同，即可以用于指定返回类型，变量声明等。- 不能为同一个模板类型形参指定两种不同的类型，比如templatevoid h(T a, T b){}，语句调用h(2, 3.2)将出错，因为该语句给同一模板形参T指定了两种类型，第一个实参2把模板形参T指定为int，而第二个实参3.2把模板形参指定为double，两种类型的形参不一致，会出错。（针对函数模板）- 当我们声明类对象为：A a，比如templateT g(T a, T b){}，语句调用a.g(2, 3.2)在编译时不会出错，但会有警告，因为在声明类对象的时候已经将T转换为int类型，而第二个实参3.2把模板形参指定为double，在运行时，会对3.2进行强制类型转换为3。当我们声明类的对象为：A a,此时就不会有上述的警告，因为从int到double是自动类型转换。
```
#ifndef TEMPLATE_DEMO_HXX
#define TEMPLATE_DEMO_HXX
 
template&lt;class T&gt; class A{<!-- -->
    public:
        T g(T a,T b);
        A();
};
 
#endif
 
　　TemplateDemo.cpp
 
#include&lt;iostream.h&gt;
#include "TemplateDemo.h"
 
template&lt;class T&gt; A&lt;T&gt;::A(){<!-- -->}
 
template&lt;class T&gt; T A&lt;T&gt;::g(T a,T b){<!-- -->
    return a+b;
}
 
void main(){<!-- -->
    A&lt;int&gt; a;
    cout&lt;&lt;a.g(2,3.2)&lt;&lt;endl;
}

```
