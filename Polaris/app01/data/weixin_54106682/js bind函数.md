
--- 
title:  js bind函数 
tags: []
categories: [] 

---
### 一、bind函数的作用

`bind()` 函数是 JavaScript 中的一个方法，它用于创建一个新的函数，并将指定的对象作为新函数的执行上下文（也就是 `this` 关键字所引用的对象）。`bind()` 方法不会立即执行函数，而是返回一个新函数，你可以随后调用这个新函数。这个新函数会以指定的对象作为 `this`，并且可以预先设置一些参数。

总结一下 `bind()` 的作用：
1.  **改变函数的执行上下文（this 指向）：** 可以将函数绑定到指定的对象上，确保函数在执行时的上下文是你指定的对象，而不是调用时的上下文。 1.  **创建偏函数（Partial Function）：** 可以预先设置函数的参数，生成一个新的函数，这个新函数会在调用时将预先设置的参数与后续传入的参数合并，然后执行原函数。 
`bind()` 方法在实际开发中经常用于确保函数在执行时具有确定的上下文，以及创建偏函数来减少重复的代码。

### 二、bind示例

```
const obj = {
  x: 42,
  getX: function() {
    return this.x;
  }
};
console.log(obj.getX()); // 输出结果42
console.log(obj.getX);
        // 输出结果
        // ƒ() {
        //     return this.x;
        // }
const unboundGetX = obj.getX;
console.log(unboundGetX()); // 这里的 this 将指向全局对象（在浏览器环境中通常是 window），输出 undefined

const boundGetX = unboundGetX.bind(obj);
console.log(boundGetX()); // 使用 bind() 方法将 this 绑定到 obj 上，输出 42

```

在这个例子中，`obj` 对象有一个 `getX` 方法，用于返回 `x` 属性的值。

function() {return this.x}是一个函数表达式，将函数表达式存储在变量后，变量也可作为一个函数，因此obj.getX的输出结果是函数表达式的声明，该函数并没有被执行；obj.getX()时才调用了该匿名函数，由于此时是在obj内部被调用，因此输出结果为42. 

同理，obj对象的getX变量存储了函数表达式，现在我们将getX变量赋值给了unboundGetX变量，那么unboundGetX变量现在同样存储了函数表达式，因此，当 `getX` 方法被直接调用时（`unboundGetX()`），它的上下文是全局对象，因此无法找到 `x` 属性，导致返回 `undefined`。

但是，通过 `bind()` 方法，我们创建了一个新的函数 `boundGetX`，并将其上下文绑定到 `obj` 对象，因此调用 `boundGetX()` 将会返回正确的值 `42`。

`bind()` 方法还可以接受额外的参数，在调用新函数时将其传递给原始函数。例如：

```
function greet(greeting, punctuation) {
  return greeting + ' ' + this.name + punctuation;
}

const obj = {
  name: 'John'
};

const boundGreet = greet.bind(obj, 'Hello');
console.log(boundGreet('!')); // 输出 "Hello John!"

```

在这个例子中，`greet` 函数有两个参数：`greeting` 和 `punctuation`。通过 `bind()` 方法，我们将 `obj` 对象绑定为新函数的上下文，并且预先设置了 `greeting` 参数为 `'Hello'`。当我们调用 `boundGreet('!')` 时，实际上是调用了 `greet` 函数，并将 `'Hello'` 作为第一个参数传递给它，然后再加上 `'!'`，返回最终的字符串 `"Hello John!"`。


