
--- 
title:  python中self的个人理解 
tags: []
categories: [] 

---
1. self = 对象自身（self.name =  name,self可以理解为由类创建的实例对象，self.name中的name就是类的属性，而name是外部传来的参数，self.name = name的意思就是把外部传来的参数name的值赋值给类自己的属性变量self.name。）

2. 对象拥有的方法和属性，我们在对象内部都可以通过self.来进行访问（self.name =  name，就是self.name中的name ），所以self就是对象自身。

3. 定义类的时候并不是所有方法都需要传入self参数，只要你想在这个方法内部操作对象的时候才需要传入self。

参考：
