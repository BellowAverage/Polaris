
--- 
title:  【C++】C++基础查漏补缺 
tags: []
categories: [] 

---
## **内存**

C/C++程序编译时内存分为5大存储区：堆区、栈区、全局区、文字常量区、程序代码区
- 从静态存储区域分配：内存在程序编译时就已经分配好，这块内存在程序的整个运行期间都存在。速度快、不容易出错，因为有系统会善后。例如全局变量，static变量等。- 在栈上分配：在执行函数时，函数内局部变量的存储单元都在栈上创建，函数执行结束时这些存储单元自动被释放。栈内存分配运算内置于处理器的指令集中，效率很高，但是分配的内存容量有限。- 从堆上分配：动态内存分配。程序在运行的时候用malloc或new申请任意大小的内存，程序员自己负责在何时用free或delete释放内存。动态内存的生存期由程序员决定，使用非常灵活。如果在堆上分配了空间，就有责任回收它，否则运行的程序会出现内存泄漏，另外频繁地分配和释放不同大小的堆空间将会产生堆内碎块。
C++ 程序中的内存分为两个部分：
- **栈：**在函数内部声明的所有变量都将占用栈内存。- **堆：**这是程序中未使用的内存，在程序运行时可用于动态分配内存。
递归函数需要栈空间，而栈空间取决于递归的深度



### 堆和栈的区别

<th style="text-align:center;width:118px;"></th><th style="text-align:center;width:214px;">堆</th><th style="text-align:center;">栈</th>
|------
<th style="text-align:center;width:118px;">申请方式</th><td style="width:214px;">程序员申请和释放</td>|系统自动分配
<th style="text-align:center;width:118px;">分配方式</th><td style="width:214px;">动态分配</td>|静态分配、动态分配
<th style="text-align:center;width:118px;">空间特点</th><td style="width:214px;"> 不连续内存区域 堆大小受限于系统中有效的虚拟内存大小 向高地址方向扩充 </td>| 连续内存区域 大小由OS预设好 向低地址方向扩充 

堆大小受限于系统中有效的虚拟内存大小

连续内存区域

向低地址方向扩充
<th style="text-align:center;width:118px;">内存管理</th><td style="width:214px;"> 系统维护一个**记录空闲内存地址的链表** （当系统收到程序申请时，遍历该链表，寻找第一个空间大于申请空间的堆结点，将该结点空间分配给程序，并删除链表中结点。大多数系统还会在这块内存空间的首地址记录本次分配的大小，同时将多余部分重新放入空闲链表中。） </td>|只要栈的剩余空间大于所申请空间，系统为程序提供内存，否则报异常提示栈溢出

（当系统收到程序申请时，遍历该链表，寻找第一个空间大于申请空间的堆结点，将该结点空间分配给程序，并删除链表中结点。大多数系统还会在这块内存空间的首地址记录本次分配的大小，同时将多余部分重新放入空闲链表中。）
<th style="text-align:center;width:118px;">分配效率</th><td style="width:214px;"> 速度慢，会有碎片 （操作是由C/C++函数库提供，分配堆内存的时候需要算法寻找合适大小的内存，获取堆的内容需要两次访问，第一次访问指针，第二次根据指针保存的地址访问内存） </td>| 高 （栈是系统提供的数据结构，计算机在底层对栈提供支持，分配专门 寄存器存放栈地址，栈操作有专门指令，出入栈操作也很简单） 

（操作是由C/C++函数库提供，分配堆内存的时候需要算法寻找合适大小的内存，获取堆的内容需要两次访问，第一次访问指针，第二次根据指针保存的地址访问内存）

（栈是系统提供的数据结构，计算机在底层对栈提供支持，分配专门 寄存器存放栈地址，栈操作有专门指令，出入栈操作也很简单）

**思路【源自网络】**

栈就像去饭馆里吃饭，只管点菜（发出申请）、付钱、和吃（使用）。吃饱了就走，不必理会切菜、洗菜等准备工作和洗碗、刷锅等扫尾工作。快捷，但是自由度小。

堆就像是自己动手做喜欢吃的菜肴，比较麻烦，但是符合自己的口味，而且自由度大。

## **内存泄漏**

堆内存泄露

**避免方式**：
1. 计数法1. 将基类的析构函数声明为虚函数：当派生类对象指针被赋值给基类对象指针时，如果基类的析构函数不是虚函数，那么在删除这个基类指针时，只会调用基类的析构函数，而不会调用派生类的析构函数。这会导致派生类中可能存在的资源没有被释放，从而引起内存泄漏等问题1. new/delete、malloc/free成对出现1. 对数组的释放使用delete[]
## **对象复用**

在程序中重复使用已有的对象，避免频繁地创建新对象，提高程序的运行效率，减少内存分配和回收的开销，避免产生内存碎片
1. **对象池**（内存池）：将多个需要重复使用的对象预先创建好并保存在一个对象池中，程序需要时从对象池中获取对象进行使用，使用完成后再将对象返还到对象池中。1. **单例模式**：将类设计成只能创建一个实例，通过在程序运行期间反复使用同一对象来达到对象复用的目的1. **享元模式**：对象被分为内部状态和外部状态，内部状态是共享的，外部状态是不共享的，因此可以通过调整外部状态来复用对象




## **new / delete 与 malloc / free**

都可用于内存的动态申请和释放

<th style="text-align:center;width:236px;">new / delete</th><th style="text-align:center;width:263px;">malloc / free</th>
|------
<td style="width:236px;"> C++关键字（编译器） 支持重载 </td><td style="width:263px;"> C/C++语言标准库函数（头文件） 支持覆盖 </td>

支持重载

支持覆盖
<td style="width:236px;">自动计算要分配的空间的大小</td><td style="width:263px;"> 手工计算 </td>
<td style="width:236px;"> 类型安全 返回与构造对象类型相同的指针 </td><td style="width:263px;"> 不支持 分配成功返回void*指针，后续需要进行强制类型转换 </td>

返回与构造对象类型相同的指针

分配成功返回void*指针，后续需要进行强制类型转换
<td style="width:236px;"> **new：**     - 调用名为**operator new**的标准库函数，分配内存，保存指定类型的对象- 调用构造函数，初始化构造对象- 返回指向构造对象的指针**delete：** 简单类型调用free函数 复杂类型：     - 运行析构函数- 调用名为**operator delete**的标准库函数释放该对象所用内存 </td><td style="width:263px;"> **malloc**：仅分配内存空间 **free**：仅回收内存空间 不能执行构造函数和析构函数 操作对象必须是明确大小的 （被free回收的内存会首先被ptmalloc使用双链表保存起来，当用户下一次申请内存的时候，会尝试从这些内存中寻找合适的返回。这样就避免了频繁的系统调用，占用过多的系统资源。同时ptmalloc也会尝试对小块内存进行合并，避免过多的内存碎片。） </td>

**delete：**

复杂类型：
1. 运行析构函数1. 调用名为**operator delete**的标准库函数释放该对象所用内存
**malloc**：仅分配内存空间

不能执行构造函数和析构函数

（被free回收的内存会首先被ptmalloc使用双链表保存起来，当用户下一次申请内存的时候，会尝试从这些内存中寻找合适的返回。这样就避免了频繁的系统调用，占用过多的系统资源。同时ptmalloc也会尝试对小块内存进行合并，避免过多的内存碎片。）
<td style="width:236px;">分配失败抛出bac_alloc异常</td><td style="width:263px;">分配失败返回NULL</td>

### allocator

申请内存，但不初始化对象，当需要的时候才进行初始化操作

### calloc

malloc申请的空间的值随机初始化，calloc申请的空间的值初始化为0

### 

### realloc

给动态分配的空间分配额外的空间，用于扩充容量



### 重载、覆盖

重载是水平关系，覆盖是垂直关系

#### **重载**

函数名相同，参数类型和数目不同

#### **覆盖（重写）**

在派生类中覆盖基类中的同名函数，重写函数体。要求基类函数必须为虚函数，有相同的参数类型、个数和返回值类型

### **隐藏**

派生类中的函数屏蔽了基类中的同名函数
1. 两个函数参数相同，但基类函数不是虚函数1. 两个函数参数不同


## 树

### 二叉树

#### **性质**
1. 第 <img alt="i" src="https://latex.csdn.net/eq?i">​ 层至多有 <img alt="2^{i-1}" src="https://latex.csdn.net/eq?2%5E%7Bi-1%7D">​ 个结点（<img alt="i\geq 1" src="https://latex.csdn.net/eq?i%5Cgeq%201">​）1. 深度为 <img alt="k" src="https://latex.csdn.net/eq?k">​ ，至多有 <img alt="2^k-1" src="https://latex.csdn.net/eq?2%5Ek-1">​ 个结点（<img alt="k\geq 1" src="https://latex.csdn.net/eq?k%5Cgeq%201">​）1. 结点总数 <img alt="n" src="https://latex.csdn.net/eq?n">​，高度至少 <img alt="log_2(n+1)" src="https://latex.csdn.net/eq?log_2%28n&amp;plus;1%29">​，至多 <img alt="\lfloor log_2n+1 \rfloor" src="https://latex.csdn.net/eq?%5Clfloor%20log_2n&amp;plus;1%20%5Crfloor">​（完全二叉树）1. 叶子结点 <img alt="n_0" src="https://latex.csdn.net/eq?n_0">​，度为 2 的结点数 <img alt="n_2" src="https://latex.csdn.net/eq?n_2">​，则 边数 = <img alt="n-1" src="https://latex.csdn.net/eq?n-1">​ = <img alt="2n_2+n_1" src="https://latex.csdn.net/eq?2n_2&amp;plus;n_1">​，叶子结点 <img alt="n_0 = n_2+1" src="https://latex.csdn.net/eq?n_0%20%3D%20n_2&amp;plus;1">​
#### **遍历**
1. 前序遍历：根左右1. 中序遍历：左根右1. 后序遍历：左右根- 前序 + 中序、后序 + 中序可以唯一确定二叉树


## **class**

### **class与struct异同点**

均拥有成员函数，可以设置访问修饰符

<th style="text-align:center;">class</th><th style="text-align:center;">struct</th>
|------
|成员默认为private|成员默认为public
|默认private继承|默认public继承

### 访问修饰符
- **public**：类外部可访问，不需要使用成员函数来设置和获取公有变量的值<li>**private**：类外部不可访问，需要使用成员函数来设置和获取公有变量的值 
  <ul>- 类和友元函数能访问private成员- 派生类不可访问- 类和友元函数可访问- 派生类可访问
#### **继承**

<th style="width:121px;"></th><th style="width:241px;">基类</th>|派生类
|------
<th colspan="1" rowspan="3" style="width:121px;">public 继承</th><td style="width:241px;">public</td>|public
<td style="width:241px;">protected</td>|protected
<td style="width:241px;">pivate</td>|不可见
<th colspan="1" rowspan="3" style="width:121px;">protected 继承</th><td style="width:241px;">public</td>|protected
<td style="width:241px;">protected</td>|protected
<td style="width:241px;">pivate</td>|不可见
<th colspan="1" rowspan="3" style="width:121px;">private 继承</th><td style="width:241px;">public</td>|private
<td style="width:241px;">protected</td>|private
<td style="width:241px;">pivate</td>|不可见

### **struct**

#### offsetof：获得结构体成员相对于结构开头的字节偏移量

```
#include &lt;stddef.h&gt;
using namespace std;

struct S{
    int x;   
    char y;
}

int main(){
    cout &lt;&lt; offsetof(S, x);
    
    return 0;
}
```



## **static作用**
1. **声明静态变量**：在函数内部或类中声明静态变量，静态变量只初始化一次，作用范围与局部变量相同，生命周期与程序运行时间相同<li>**限制变量或函数的作用域**： 
  <ol>1. 在函数内部定义静态变量，将该变量作用域限制在该函数内部。1. 在类中定义静态成员函数，可以通过类名调用该函数，而不需要实例化对象。- static修饰的类成员属于类，不属于对象。static类成员函数不能访问非static的类成员，只能访问static修饰的类成员。静态成员函数不具有this指针，不能被声明为const、虚函数和volatile 。
## **const作用**
1. **定义常量**：值不能被修改1. **作为函数参数**：参数值不能在函数内部被修改1. **作为函数返回值**：返回值只读，不能被修改1. **用于指针和引用**：指向常量的指针或引用，不能修改指向的值<li>**const成员变量**： 
  <ul>- 在构造函数初始化列表中初始化；- const成员变量是与类相关联的，而不是与对象实例相关联，这意味着所有类的对象都共享同一个const成员变量，const成员变量不占用对象的空间。- 不能修改非静态成员变量（const修饰符告诉编译器，该函数不会对对象的状态进行更改），但可以访问类的所有成员；- 可以被const对象调用（const对象也只能调用const成员函数），不可以被非const对象调用；- 可重载非const成员函数（在类中可以同时定义const版本和非const版本的同名成员函数）
const_cast：将const类型转换为非const类型





## std::function
- std::function是一个函数包装模板，可以包装：函数、模板函数、lambda表达式、函数指针、类成员函数指针、任意类型的函数对象- std::function对象可被拷贝和转移，并且可以使用指定的调用特征来直接调用目标元素
## #pragma once

使头文件只被编译一次

## #ifndef #define……#endif

不仅可以保证同一个文件不会被包含多次，也能保证内容完全相同的两个文件（或者代码片段）不会被同时包含

## emplace_back()和push_back()的区别

底层实现机制不同：
- push_back() 向容器尾部添加元素时，首先会创建这个元素，然后再将这个元素拷贝或者移动到容器中（如果是拷贝的话，事后会自行销毁先前创建的这个元素）- emplace_back() 直接在容器尾部创建这个元素，省去了拷贝或移动元素的过程
## 重定向

原先从键盘（标准输入的默认设备）接受的输入，变为从文件读取



## 构造函数 
- 默认构造函数- 初始化构造函数：有参数和参数列表- 拷贝构造函数：用类的一个实例化对象去初始化另一个对象；函数的参数是类的对象（非引用传递）- 移动构造函数- 委托构造- 转换构造函数：将其它类型的变量隐式转换为本类对象
## **拷贝初始化与直接初始化**

### 拷贝初始化

调用拷贝构造函数，首先用构造函数创建一个临时对象，然后用拷贝构造函数将该临时对象拷贝到正在创建的对象

```
// 拷贝初始化：先为字符串“hello world”创建临时对象，再把临时对象作为参数，使用拷贝构造函数构造str1
string str1 = "hello world";
// 隐式调用拷贝构造函数
string str2 = str1;
```



### 直接初始化

直接调用与实参匹配的构造函数

```
string str1("hello world");
// 调用拷贝构造函数对str2进行初始化
string str2(str1);

```

## **类成员初始化**
1. 赋值初始化1. 列表初始化
## 

## **浅拷贝和深拷贝**

### **浅拷贝**

浅拷贝只是拷贝一个指针，并没有新开辟一个地址，拷贝的指针和原来的指针指向同一块地址

### **深拷贝**

深拷贝不仅拷贝值，还开辟出一块新的空间用来存放新的值。即使原先的对象被析构掉，释放内存了也不会影响到深拷贝得到的值。

## **虚拟继承**

**解决多继承造成的菱形继承问题，通过在每个派生类与共同基类之间建立虚拟基类来实现**

在多重继承的情况下，如果一个派生类从两个或更多的基类派生，而这些基类共同派生自同一个基类时，就会产生所谓的“**菱形继承**”问题

例如，如果有两个类B和C都从类A继承了一些属性和方法，然后又定义了一个类D，从B和C中分别继承了属性和方法，那么在D中就会包含两份从A继承的成员。这种情况下，如果使用D的对象调用从A中继承的成员，就会导致歧义、冗余和效率浪费等问题。

虚拟继承机制使得从共同基类继承来的成员在派生类中只保留一份，从而避免了重复继承的问题。

## **派生类构造函数顺序**
1. **虚拟基类**的构造函数（多个虚拟基类按继承顺序）1. **基类**的构造函数1. **派生类**自身的构造函数
### **extern "C"**

C++调用C函数

```
// xx.h
extern int add(...)

// xx.c
int add(){
    
}

// xx.cpp
extern "C" {
    #include "xx.h"
}

```

C调用C++

```
// xx.h
extern "C"{
    int add();
}

// xx.cpp
int add(){    
}

// xx.c
extern int add();

```

### **野指针和悬空指针**

#### 野指针

没有被初始化过的指针

#### 悬空指针

指针最初指向的内存已经被释放



### **关键字**
- **override**：指定重载函数- **final**：类或函数不可以被继承或重写<li>**volatile**：用它声明的类型变量表示可以被某些编译器未知的因素更改。每次用到volatile变量的值的时候都要重新读取，而不是读寄存器内的备份。多线程中被几个任务共享的变量需要定义为volatile类型 
  <ul>- **volatile 指针**- **多线程**






## 杂
- 零拷贝：减少不必要的复制和内存分配。e.g.通过指针或引用传递复杂数据结构、智能指针、容器、内存池- coredump：当程序出错而异常中断时，OS会把程序工作的当前状态存储成一个coredunmp文件<li>
## 大小端存储
- 大端存储：字数据的高字节存储在低地址中- 小端存储：字数据的低字节存储在低地址
## 查看编译器使用的C++版本

```
#include &lt;iostream&gt;
using namespace std;

int main()
{
	cout &lt;&lt; __cplusplus &lt;&lt; endl;
	return 0;
}
```

### **版本对照**
<td style="text-align:center;">199711</td><td style="text-align:center;">C++ 98</td>
<td style="text-align:center;">201103</td><td style="text-align:center;">C++ 11</td>
<td style="text-align:center;"></td><td style="text-align:center;"></td>


