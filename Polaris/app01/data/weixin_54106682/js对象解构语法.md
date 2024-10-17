
--- 
title:  js对象解构语法 
tags: []
categories: [] 

---
对象解构语法是一种 JavaScript 的语法特性，用于从对象中提取属性，并将这些属性值赋值给变量。

#### 基本语法

```
const { property1, property2 } = object;

```
- `object` 是要解构的对象。- `property1` 和 `property2` 是对象中的属性名，用花括号 `{}` 包裹起来表示从对象中提取这些属性。- 解构后的属性值会分别赋值给同名的变量 `property1` 和 `property2`。
#### 默认值

如果对象中没有提取的属性，则解构后的变量将会是 `undefined`。可以使用默认值来避免这种情况。

```
const { property1 = defaultValue1, property2 = defaultValue2 } = object;

```
- 如果 `object` 中没有 `property1` 属性，则 `property1` 变量的值为 `defaultValue1`。- 如果 `object` 中没有 `property2` 属性，则 `property2` 变量的值为 `defaultValue2`。
#### 重命名

可以使用冒号 `:` 来重命名解构后的变量名。

```
const { property1: newName1, property2: newName2 } = object;

```
- `property1` 属性的值会赋值给 `newName1` 变量。- `property2` 属性的值会赋值给 `newName2` 变量。
#### 解构嵌套对象

对象解构语法也可以用于解构嵌套对象。

```
const { property1: { nestedProperty1, nestedProperty2 } } = object;

```
- `object` 中的 `property1` 属性是一个对象，其中包含 `nestedProperty1` 和 `nestedProperty2` 属性。- 这些属性值会分别赋值给 `nestedProperty1` 和 `nestedProperty2` 变量。
#### 示例

```
const person = { name: 'John', age: 30, city: 'New York' };

const { name, age } = person;
console.log(name); // 输出 'John'
console.log(age); // 输出 30

const { name: fullName, age: years } = person;
console.log(fullName); // 输出 'John'
console.log(years); // 输出 30

const { gender = 'Male', city } = person;
console.log(gender); // 输出 'Male'，因为 person 中没有 gender 属性，所以使用了默认值
console.log(city); // 输出 'New York'

const { address: { street, zip } } = person; // person 没有 address 属性，会导致解构错误

```

总的来说，对象解构语法使得从对象中提取属性变得更加简洁和方便，并且可以轻松地使用默认值、重命名属性、解构嵌套对象等功能。
