
--- 
title:  【C#】浅谈C#中垃圾回收机制 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>浅谈C#中垃圾回收机制</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - <ul><li>- - - - - - -  
   </li>- - <li>-  
  </li></ul> 
  
  


C# 中的垃圾回收 (Garbage Collection, GC) 是一种自动的内存管理机制，它帮助开发者释放不再使用的内存资源：

### 1. 为什么需要垃圾回收？
- 手动管理内存可能会导致内存泄漏（未释放但不再使用的内存）或者重复释放同一块内存，从而引发错误。- 通过自动化的垃圾回收，可以减少这种错误，并确保有效利用内存资源。
### 2. 工作原理：
- .NET 的内存分为几个不同的世代，分别是：世代 0、世代 1 和世代 2。- 新对象默认创建在世代 0。- 当垃圾回收器运行时，它首先检查世代 0 中的对象。那些不再被引用的对象会被回收，仍然存活的对象则进入世代 1。- 世代 1 和世代 2 的收集频率较低，因为较老的对象（即存在时间较长的对象）通常有更长的生命周期。
### 3. 如何工作：
- 垃圾回收器查找根引用（如全局变量、静态变量、活动的本地变量等）开始，然后遍历所有可访问的对象。- 一旦所有活动的或可访问的对象都被标记后，所有其他的对象都被视为垃圾，因此可以被安全地回收。
### 4. 垃圾回收的触发时机：
- 当世代 0 的对象超过了一个阈值时。- 当调用 `GC.Collect()` 时。- 当系统内存不足时。
### 5. 不足和问题：
- GC 是有代价的。当垃圾回收器运行时，所有其他的线程可能会被暂停。- 开发者无法明确知道何时对象会被回收。
### 6. **如何优化：**
- 尽量减少大对象的创建，因为这可能会导致频繁的垃圾收集。- 如果知道对象生命周期，可以使用结构（structs）而不是类（classes），因为结构在栈上分配，而不是在堆上。- 有意识地设置长时间存活的对象为 `null`，以帮助垃圾回收器更早地回收它们。
### 7. **其他：**
- `Finalizers` 和 `Dispose` 方法允许对象在被回收前执行一些清理工作，例如释放非托管资源。- 强烈建议使用 `using` 语句来确保 `IDisposable` 对象在使用后被正确地清理。
### 8. **非托管资源的处理：**
- 虽然垃圾回收器会自动管理托管的内存资源，但对于非托管资源（例如文件句柄、数据库连接等），需要手动释放。- 为此，可以实现 `IDisposable` 接口，并在 `Dispose` 方法中释放这些资源。
总结，垃圾回收是.NET框架提供的一个强大工具，用于帮助开发者自动管理内存。但是，了解其工作原理和如何优化内存使用仍然是十分重要的。

## 9. 举例说明

下面通过一个简单的例子来说明 C# 中垃圾回收的概念：

### 9.1. 对象的创建和回收

```
public class Person
{<!-- -->
    public string Name {<!-- --> get; set; }

    // 析构函数（Finalizer）
    ~Person()
    {<!-- -->
        Console.WriteLine($"{<!-- -->Name} 被回收了!");
    }
}

public static void Main(string[] args)
{<!-- -->
    Person person1 = new Person() {<!-- --> Name = "张三" };
    Person person2 = new Person() {<!-- --> Name = "李四" };

    person1 = null; // 去除对张三的引用
    person2 = null; // 去除对李四的引用

    GC.Collect(); // 强制执行垃圾回收

    Console.ReadLine();
}

```

在这个示例中，我们创建了两个 `Person` 对象，分别命名为张三和李四。当我们将 `person1` 和 `person2` 设置为 `null` 之后，这两个对象实际上已经失去了对它们的所有引用，所以它们可以被视为垃圾。通过调用 `GC.Collect()` 我们强制执行了垃圾回收，所以我们会在控制台上看到两条消息，表示这两个对象已经被回收。

### 9.2 IDisposable 的使用

```
public class DatabaseConnection : IDisposable
{<!-- -->
    private bool disposed = false;

    public void Open()
    {<!-- -->
        Console.WriteLine("数据库连接已打开");
    }

    public void Close()
    {<!-- -->
        Console.WriteLine("数据库连接已关闭");
    }

    public void Dispose()
    {<!-- -->
        Dispose(true);
        GC.SuppressFinalize(this);
    }

    protected virtual void Dispose(bool disposing)
    {<!-- -->
        if (!disposed)
        {<!-- -->
            if (disposing)
            {<!-- -->
                Close(); // 释放托管资源
            }

            // 释放非托管资源（如文件句柄、网络套接字等）

            disposed = true;
        }
    }

    ~DatabaseConnection()
    {<!-- -->
        Dispose(false);
    }
}

public static void Main(string[] args)
{<!-- -->
    using (DatabaseConnection dbConnection = new DatabaseConnection())
    {<!-- -->
        dbConnection.Open();
        // 进行一些数据库操作
    } // 在 using 语句结束时，Dispose 方法会被自动调用

    Console.ReadLine();
}

```

在这个示例中，我们创建了一个模拟的 `DatabaseConnection` 类，它实现了 `IDisposable` 接口。我们在 `Dispose` 方法中关闭数据库连接并释放相关资源。使用 `using` 语句可以确保在对象不再使用时，`Dispose` 方法会被自动调用，从而释放资源。
