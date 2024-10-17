
--- 
title:  js之扩展运算符三个点（...） 
tags: []
categories: [] 

---
在 JavaScript 中，扩展运算符 `{ ...data }` 是一种用于对象的操作符。它的作用是将一个对象的所有可枚举属性拷贝到另一个对象中。

下面是关于扩展运算符 `{ ...data }` 的详细解释：

**复制对象**：扩展运算符用于将一个对象中的所有属性复制到另一个对象中。例如：

```
const data = { name: 'John', age: 30 };
const newData = { ...data };

console.log(newData); // 输出 { name: 'John', age: 30 }

```

在这个例子中，`newData` 对象包含了 `data` 对象中的所有属性和值。

**浅拷贝**：扩展运算符执行的是浅拷贝，意味着它只会复制对象的属性本身，而不会复制属性所指向的对象。如果属性值是一个对象，那么复制后的对象与原对象共享同一个引用。例如：

```
const data = { name: 'John', details: { age: 30 } };
const newData = { ...data };

newData.details.age = 40;

console.log(data.details.age); // 输出 40，因为修改了 newData 后，data 中的 details.age 也发生了变化

```

在这个例子中，`newData` 对象中的 `details` 属性和 `data` 对象中的 `details` 属性指向同一个对象，因此修改 `newData` 中 `details` 属性的值也会影响到 `data` 中 `details` 属性的值。

**覆盖属性**：如果扩展运算符的目标对象中已经存在与源对象相同的属性，那么将会覆盖目标对象中的属性值。例如：

```
const data = { name: 'John', age: 30 };
const newData = { ...data, age: 40 };

console.log(newData); // 输出 { name: 'John', age: 40 }

```

在这个例子中，`newData` 对象中的 `age` 属性被覆盖为 `40`，而不是 `30`。

总之，扩展运算符 `{ ...data }` 是一种方便的方式来复制对象，并且可以用于创建新对象，其中包含了原始对象中的所有属性和值。
