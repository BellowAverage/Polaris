
--- 
title:  【C++】dynamic_cast基本用法（详细讲解） 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>C++中dynamic_cast基本用法（详细讲解）</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - - <ul><li>-  
   </li>- - - </ul> 
  
  


`dynamic_cast` 是 C++ 中的一个类型转换操作符，它主要用于多态类型之间的转换。其特点是在运行时进行类型检查，确保所执行的转换是安全的。因此，它主要用于指向类的指针或引用之间的转换，尤其是在类的继承体系中。

## 1. 使用场景

### 1.1向下转型

将基类指针或引用转换为派生类指针或引用。这是 `dynamic_cast` 最常见的用途。

```
    class Base {<!-- -->};
    class Derived : public Base {<!-- -->};

    Base* basePtr = new Derived;
    Derived* derivedPtr = dynamic_cast&lt;Derived*&gt;(basePtr); 

```

如果转换成功，`derivedPtr` 将是一个有效的指针；如果转换失败（例如，如果 `basePtr` 实际上不指向 `Derived` 类的对象），`derivedPtr` 将是 `nullptr`。

### 1.2横向转型

在同一继承层级的不同派生类之间进行转换。

```
    class Base {<!-- -->};
    class Derived1 : public Base {<!-- -->};
    class Derived2 : public Base {<!-- -->};

    Base* basePtr = new Derived1;
    Derived2* derived2Ptr = dynamic_cast&lt;Derived2*&gt;(basePtr); 

```

在这种情况下，`derived2Ptr` 会是 `nullptr`，因为 `basePtr` 实际上指向的是 `Derived1` 类的对象。

## 2. 前提条件

为了使 `dynamic_cast` 能够进行运行时类型检查，以下条件必须满足：
<li> 转换涉及的类型至少有一个虚函数。换句话说，基类必须有虚函数，以支持运行时类型信息 (RTTI)。 <pre><code class="prism language-cpp">class Base {<!-- -->
public:
    virtual void foo() {<!-- -->}
};
</code></pre> </li>-  编译器需要启用 RTTI。大多数现代 C++ 编译器默认启用 RTTI，但有些情况下可能需要显式地开启它。 
## 3. 优点
- **安全性**：`dynamic_cast` 提供运行时的类型检查，这使得转换更加安全。如果转换无法进行，对于指针转换，它返回 `nullptr`；对于引用转换，它抛出一个 `std::bad_cast` 异常。
## 4. 缺点
- **性能开销**：由于 `dynamic_cast` 需要在运行时进行类型检查，所以它相对于其他转换（如 `static_cast`）来说，有一定的性能开销。
总之，`dynamic_cast` 在处理与多态相关的类型转换时是非常有用的，尤其是当你不确定实际类型时。但由于其性能开销，你应该在必要时才使用它，并确保 RTTI 在你的编译器中是启用的。
