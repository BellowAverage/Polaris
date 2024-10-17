
--- 
title:  Python 的 @property 
tags: []
categories: [] 

---
如果使用 @property 进行修饰后，又在调用的时候，方法后面添加了()， 那么就会显示错误信息；也就是说添加 @property 后，这个方法就变成了一个属性，如果后面加入了()，那么就是当作函数来调用。 

```
class DataSet(object):
    @property
    def method_with_property(self):
        return 'method_with_property'

    def method_without_property(self):
        return 'method_without_property'


dataset = DataSet()
print(dataset.method_with_property)  # 加了@property后，没有加()。正常调用属性的形式。
# print(dataset.method_with_property())  # 加了@property后，加了()。错误调用方式。
print(dataset.method_without_property())  # 没有加@property , 加了()。正常调用方法的形式。
print(dataset.method_without_property)  # 没有加@property ,没有加()，是方法的存放地址（引用）。

```

可以使用@property装饰器来创建**只读属性**，@property 装饰器会将**方法**转换为相同名称的**只读属性，**可以与所定义的属性配合使用，这样可以防止属性被修改。

```
class DataSet(object):
    @property
    def method_with_property(self):
        return 'method_with_property'

    def method_without_property(self):
        return 'method_without_property'


dataset = DataSet()
dataset.method_without_property = 'some value'
# dataset.method_with_property = 'some value'  # AttributeError: can't set attribute

```


