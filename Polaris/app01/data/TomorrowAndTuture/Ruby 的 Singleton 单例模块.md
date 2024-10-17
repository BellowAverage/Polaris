
--- 
title:  Ruby 的 Singleton 单例模块 
tags: []
categories: [] 

---
一般来说，对于某个类，我们可以创建无穷多个对象，且不会受到任何限制。但是，有时候，我们只需要类的一个实例来协调整个程序的操作，并不需要多个实例。对于这种场景，我们希望确保正在运行的程序只存在给定类的一个实例。也就是所谓的 **单例模式**。**单例模式** 是一种设计模式，它将给定类的实例化限制为一个对象。

### 常规模式

直接用例子来说更简单易懂一些。

```
class HelloWorld
    def instance_method
        puts "instance method"
    end
end


puts HelloWorld.new
puts HelloWorld.new
puts HelloWorld.new.instance_method
```

```
#&lt;HelloWorld:0x00000163b44b0e38&gt;
#&lt;HelloWorld:0x00000163b44a78d8&gt;
instance method
```

常规模式当中，要调用类的实例方法 instance_method，则必须要先使用类 new 一个实例对象才可以进行调用。

而且，我们可以看到，两次 new 产生的对象并不是同一个（地址不一样）。

### 单例模式

Ruby 直接给我们实现了一个单例模块 `Singleton`，我们只要把这个模块往类里一放，类就自动就可以获得一个 `instance` 方法，这个方法会返回 `Singleton` 模块为我们创建的单例模块。

```
require 'singleton'

class HelloWorld
    include Singleton

    def instance_method
        puts "instance method"
    end
end


puts HelloWorld.instance
```

我们可以看看单例模式有哪些特点。 

#### 只会生成一个实例 

也即使用 .instance 生成的实例都是同一个实例。

```
require 'singleton'

class HelloWorld
    include Singleton

    def instance_method
        puts "instance method"
    end
end


puts HelloWorld.instance
puts HelloWorld.instance
puts HelloWorld.instance
```

```
#&lt;HelloWorld:0x00000241e4604898&gt;
#&lt;HelloWorld:0x00000241e4604898&gt;
#&lt;HelloWorld:0x00000241e4604898&gt;
```

#### 类的 new 方法被禁用

类的 new方法被禁用，此时一般只能使用 .instance 生成实例对象。其实，只是 Singleton 将 `.new` 方法变为私有 ( `private` )。

```
require 'singleton'

class HelloWorld
    include Singleton

    def instance_method
        puts "instance method"
    end
end


puts HelloWorld.new
```

```
E:/Project/test/test.rb:12:in `&lt;main&gt;': private method `new' called for HelloWorld:Class (NoMethodError)

puts HelloWorld.new
               ^^^^
```

#### clone 和 dup 方法不可用 

这个其实也不难理解，毕竟单例模式的特点就是只有一个实例，使用 clone 明显违背了它的基本原则。

正常实例克隆

```
class HelloWorld

    def instance_method
        puts "instance method"
    end
end


puts HelloWorld.new.clone
```

```
#&lt;HelloWorld:0x0000020190964a90&gt;
```

单例模式不允许克隆 

```
require 'singleton'

class HelloWorld
    include Singleton

    def instance_method
        puts "instance method"
    end
end


puts HelloWorld.instance.clone
```

```
 can't clone instance of singleton HelloWorld (TypeError)
```

#### 延迟加载

`Singleton` 模块生成的单例，也是在首次调用 `instance()` 方法时才创建，并不是在加载类时就创建了。

```
require 'singleton'

class HelloWorld
    include Singleton

    def instance_method
        puts "instance method"
    end
end


puts ObjectSpace.each_object(HelloWorld){}
puts HelloWorld.instance
puts ObjectSpace.each_object(HelloWorld){}
```

```
0
#&lt;HelloWorld:0x0000025c7faafbd0&gt;
1
```

#### 单例继承

如果一个类继承了一个单例类，那么这个子类也属于单例类。

HelloWorld2类定义了它自己的 `instance` 方法，且不使用 HelloWorld类中定义的 `instance` 方法。这个新定义的 `instance` 方法返回的是 `HelloWorld` 类的实例，而不是 HelloWorld类的实例。在父类和子类都定义了方法的话，子类的方法拥有更高的优先级。

```
require 'singleton'

class HelloWorld
    include Singleton

    def instance_method
        puts "instance method"
    end
end

class HelloWorld2 &lt; HelloWorld
    def instance_method
        puts "instance method2"
    end
end

puts HelloWorld.instance.instance_method
puts HelloWorld2.instance.instance_method

```

```
instance method

instance method2
```

 子类调用它没定义的方法的话，会自动调用父类的方法。

```
require 'singleton'

class HelloWorld
    include Singleton

    def instance_method
        puts "instance method"
    end
end

class HelloWorld2 &lt; HelloWorld
end

puts HelloWorld.instance.instance_method
puts HelloWorld2.instance.instance_method
```

```
instance method

instance method
```
