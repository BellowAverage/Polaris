
--- 
title:  Ruby 中类方法和实例方法定义的几种方式 
tags: []
categories: [] 

---
Ruby 的类方法也叫静态方法，通过类名来调用的方法。但实例方法，必须要 new 一个实例对象出来才能用。

常见的类方法和实例方法的定义如下：

```
class HelloWorld
    def self.inner_method
        puts "inner class method"
    end

    def inner_method
        puts "inner instance method"
    end

    def self.class_method
        puts "class method"
        inner_method
    end

    def instance_method
        puts "instance method"
        inner_method
    end
end

HelloWorld.class_method
HelloWorld.new.instance_method
```

```
class method
inner class method
instance method
inner instance method
```

但是 Ruby 当中还有其他更加灵活的方式来进行定义。 

### 类方法定义

#### 方法一

```
class HelloWorld
    def self.class_method
        puts "class method"
    end
end

HelloWorld.class_method
```

#### 方法二

```
class HelloWorld
    class &lt;&lt; self
        def class_method
            puts "class method"
        end
    end
end

HelloWorld.class_method
```

#### 方法三

```
class  HelloWorld
    # ...
end

class &lt;&lt; HelloWorld
    def class_method
        puts "class method"
    end
end

HelloWorld.class_method

```

#### 方法四

```
class  HelloWorld
    # ...
end

def HelloWorld.class_method
    puts "class method"
end

HelloWorld.class_method
```

#### 方法五 

```
module ClassModule
    def class_method
        puts "class method"
    end
end

class HelloWorld
    extend ClassModule
end

HelloWorld.class_method
```

### 实例方法定义

#### 方法一

```
class HelloWorld
    def instance_method
        puts "instance method"
    end
end

HelloWorld.new.instance_method

```

#### 方法二

```
class HelloWorld
    # ..
end

helloworld = HelloWorld.new
def helloworld.instance_method
    puts "instance method"
end

helloworld.instance_method
```

#### 方法三

```
# 这个严格来说是实例变量
class HelloWorld
    attr_accessor :instance_method
end

helloworld = HelloWorld.new
helloworld.instance_method = "instance method"
puts helloworld.instance_method

```

#### 方法四

```
module InstanceModule
    def instance_method
        puts "instance method"
    end
end

class HelloWorld
    include InstanceModule
end

HelloWorld.new.instance_method
```


