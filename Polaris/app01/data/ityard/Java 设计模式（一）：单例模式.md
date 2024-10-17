
--- 
title:  Java 设计模式（一）：单例模式 
tags: []
categories: [] 

---
## 1 简介

单例模式保证一个类只有一个实例，并向外提供一个全局的访问入口，单例类需自己实例化唯一的实例。Java 中 `java.lang.Runtime` 就是典型的单例模式实现例子，现实生活中的例子也比较多，比如：一个学校有一个校长、一个公司有一个董事长等。
-  **优点**：因为单例模式只生成一个实例，所以能够节约系统资源、减少性能开销，同时也能避免对共享资源的多重占用。 -  **缺点**：同样因为只有一个实例，导致单例类的职责过重，与单一职责原则冲突，它没有接口，不能继承，不利于扩展。 
## 2 实现方式

常见的单例模式实现方式大致有五种，分别为：饿汉式、懒汉式、双重检测锁、静态内部类、枚举，通常我们需要保证单例模式的线程安全，下面来看一下如何通过这五种方式实现线程安全的单例模式。

### 2.1 饿汉式

饿汉式从字面上我们就能了解个大概：饿了就要马上吃饭，这种模式在类加载时就初始化实例，缺点是容易产生垃圾对象，因为可能我们还没有用到实例的时候，实例就已经被创建了；优点是线程安全，不用加锁，效率高。示例如下：

```
public class Singleton {<!-- -->
	private static Singleton instance = new Singleton();
	//将构造器设置为 private，禁止通过 new 实例化
	private Singleton() {<!-- -->}
	public static Singleton getInstance() {<!-- -->
		return instance;
	}
}

```

### 2.2 懒汉式

懒汉式就是懒加载，在首次调用时进行初始化，避免了内存被浪费问题，但这种方式在多线程情况下需要通过加锁（如：synchronized ）来保证线程安全，加锁会影响效率，因此这种方式效率可能会比较低。示例如下：

```
public class Singleton {<!-- -->
	private static Singleton instance;
	private Singleton() {<!-- -->}
	public static Singleton getInstance() {<!-- -->
		synchronized(Singleton.class) {<!-- -->
			if (instance == null) {<!-- -->
				instance = new Singleton();
			}
		}
		return instance;
	}
}

```

### 2.3 双重检测锁

这种方式采用双锁机制，在多线程情况下既能保证线程安全，同时又能保持较高的性能，当然这种方式实现会相对复杂了一点。示例如下：

```
public class Singleton {<!-- -->  
    private volatile static Singleton instance;  
    private Singleton (){<!-- -->}  
    public static Singleton getInstance() {<!-- -->  
	    if (instance == null) {<!-- -->  
	        synchronized (Singleton.class) {<!-- -->  
					if (instance == null) {<!-- -->
						instance = new Singleton();
					} 
	        }  
	    }  
	    return instance;  
    }  
}

```

从示例中我们可以看到，这种方式进行了两次判断，第一次是为了避免不要的实例创建，第二次是为了进行同步，避免多线程问题。`instance = new Singleton()` 创建时在 JVM 中可能会进行指令重排序，在多线程情况下会存在线程安全问题，使用 `volatile` 修饰 `instance` 解决该问题。

### 2.4 静态内部类

这种方式和饿汉式一样，通过 ClassLoader 的机制保证了线程安全，不同之处饿汉式一旦 Singleton 类被装载了，那么 instance 就会被实例化，而这种方式只有内部类（SingletonInner）被主动使用时才会实例化单例对象；该方式可以达到双重检测锁方式的效率，实现相对简单一点，当然这种方式只适用于静态域的情况，双重检测锁方式可在实例域需要延迟初始化时使用。

示例如下：

```
public class Singleton {<!-- -->
	private static class SingletonInner {<!-- -->
		private static final Singleton instance = new Singleton();
	}
	private Singleton() {<!-- -->}
	public static final Singleton getInstance() {<!-- -->
		return SingletonInner.instance;
	}
}

```

### 2.5 枚举

默认枚举实例的创建是线程安全的，它自动支持序列化机制，可避免反射，防止多次实例化，因此在任何情况下都是单例的，它的实现也比较简单，但由于 JDK1.5 之后才加入 `enum`，这种方式在实际工作中用的还是比较少。示例如下：

```
public enum Singleton {<!-- -->  
    INSTANCE;  
    public void getInstance() {<!-- -->}  
}

```

## 3 总结
- 懒汉式效率最低；- 单例对象占用资源少，不需要延时加载，枚举方式优于饿汉式；- 单例对象占用资源多，需要延时加载，静态内部类优于懒汉式。
<img src="https://img-blog.csdnimg.cn/20191007101439261.JPG#pic_center" alt="在这里插入图片描述" width="600" height="350">
