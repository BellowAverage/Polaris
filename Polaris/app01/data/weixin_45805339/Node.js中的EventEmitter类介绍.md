
--- 
title:  Node.js中的EventEmitter类介绍 
tags: []
categories: [] 

---
### 1.EventEmitter类说明

`EventEmitter` 是 Node.js 中的一个核心模块，它提供了一种实现事件驱动编程的机制。它是一个基于观察者模式的类，用于在应用程序中处理事件和触发事件。 Node.js 所有的异步 I/O 操作在完成时都会发送一个事件到事件队列。 Node.js 里面的许多对象都会分发事件：一个 net.Server 对象会在每次有新连接时触发一个事件， 一个 fs.readStream 对象会在文件被打开的时候触发一个事件。 所有这些产生事件的对象都是 events.EventEmitter 的实例。

### 2.EventEmitter类使用

#### 2.1事件注册和触发

通过 `on` 方法可以注册事件监听器，监听特定的事件。当事件触发时，所有注册的监听器将按照顺序执行。例如：

```
const EventEmitter = require('events');

const myEmitter = new EventEmitter();

myEmitter.on('event', () =&gt; {<!-- -->
  console.log('Event occurred');
});

myEmitter.emit('event'); // 执行事件并触发监听器

```

当 `event` 事件触发时，`EventEmitter` 将调用相应的监听器函数，并输出 `'Event occurred'`。

#### 2.2一次性事件监听器

使用 `once` 方法可以注册一次性事件监听器，它只会在当前事件触发的第一次执行。例如：

```
const EventEmitter = require('events');

const myEmitter = new EventEmitter();

myEmitter.once('event', () =&gt; {<!-- -->
  console.log('Event occurred once');
});

myEmitter.emit('event'); // 执行事件并触发监听器
myEmitter.emit('event'); // 不再触发监听器

```

在上述示例中，`once` 方法注册的监听器只会在第一次触发事件时执行。第二次触发事件时，不会调用该监听器。

#### 2.3传递参数

可以在事件触发时向监听器传递参数。例如：

```
const EventEmitter = require('events');

const myEmitter = new EventEmitter();

myEmitter.on('event', (arg1, arg2) =&gt; {<!-- -->
  console.log(`Received ${<!-- -->arg1} and ${<!-- -->arg2}`);
});

myEmitter.emit('event', 'Hello', 'World'); // 执行事件并触发监听器，并传递参数

```

在上述示例中，`emit` 方法触发了 `event` 事件，并将 `'Hello'` 和 `'World'` 作为参数传递给监听器函数。

#### 2.4错误处理

`EventEmitter` 具有内置的错误处理机制。可以通过监听 `'error'` 事件来处理错误。如果没有针对 `'error'` 事件注册监听器，将会输出一个未处理的错误堆栈。例如：

```
const EventEmitter = require('events');

const myEmitter = new EventEmitter();

myEmitter.on('error', (error) =&gt; {<!-- -->
  console.error('Error occurred:', error);
});

myEmitter.emit('error', new Error('Something went wrong')); // 触发 'error' 事件并传递错误对象

```

在上述示例中，当 `'error'` 事件触发时，注册的监听器将打印出错误信息。

`EventEmitter` 类还具有其他方法，如 removeListener、removeAllListeners 等，用于添加、删除或清除事件监听器。通过使用 EventEmitter，可以轻松实现事件驱动的编程范式，以构建灵活、可扩展的应用程序。

### 3.EventEmitter类方法说明

#### 3.1 方法
- addListener(event, listener)：为指定事件添加一个监听器到监听器数组的尾部。- on(event, listener)：为指定事件注册一个监听器，接受一个字符串 event 和一个回调函数。
```
server.on('connection', function (stream) {<!-- -->
  console.log('someone connected!');
});

```
- once(event, listener)：为指定事件注册一个单次监听器，即 监听器最多只会触发一次，触发后立刻解除该监听器。
```
server.once('connection', function (stream) {<!-- -->
  console.log('Ah, we have our first user!');
});

```
- removeListener(event, listener)：移除指定事件的某个监听器，监听器必须是该事件已经注册过的监听器。它接受两个参数，第一个是事件名称，第二个是回调函数名称。
```
var callback = function(stream) {<!-- -->
  console.log('someone connected!');
};
server.on('connection', callback);
// ...
server.removeListener('connection', callback);

```
- removeAllListeners([event])：移除所有事件的所有监听器， 如果指定事件，则移除指定事件的所有监听器。- setMaxListeners(n)：默认情况下， EventEmitters 如果你添加的监听器超过 10 个就会输出警告信息。 setMaxListeners 函数用于改变监听器的默认限制的数量。- listeners(event)：返回指定事件的监听器数组。- emit(event, [arg1], [arg2], […])：按监听器的顺序执行执行每个监听器，如果事件有注册监听返回 true，否则返回 false。
#### 3.2类方法
- listenerCount(emitter, event)：返回指定事件的监听器数量。
```
events.EventEmitter.listenerCount(emitter, eventName) //已废弃，不推荐
events.emitter.listenerCount(eventName) //推荐

```

#### 3.3 事件
<li>newListener（该事件在添加新监听器时被触发。） 
  <ul>- event - 字符串，事件名称- listener - 处理事件函数- event - 字符串，事件名称- listener - 处理事件函数
#### 3.4 EventEmitter子类

大多数时候我们不会直接使用 EventEmitter，而是在对象中继承它。包括 fs、net、 http 在内的，只要是支持事件响应的核心模块都是 EventEmitter 的子类。

为什么要这样做呢？原因有两点：

首先，具有某个实体功能的对象实现事件符合语义， 事件的监听和发生应该是一个对象的方法。

其次 JavaScript 的对象机制是基于原型的，支持 部分多重继承，继承 EventEmitter 不会打乱对象原有的继承关系。

### 4.举例说明

```
var events = require('events');
var eventEmitter = new events.EventEmitter();

// 监听器 #1
var listener1 = function listener1() {<!-- -->
   console.log('监听器 listener1 执行。');
}

// 监听器 #2
var listener2 = function listener2() {<!-- -->
  console.log('监听器 listener2 执行。');
}

// 绑定 connection 事件，处理函数为 listener1 
eventEmitter.addListener('connection', listener1);

// 绑定 connection 事件，处理函数为 listener2
eventEmitter.on('connection', listener2);

var eventListeners = eventEmitter.listenerCount('connection');
console.log(eventListeners + " 个监听器监听连接事件。");

// 处理 connection 事件 
eventEmitter.emit('connection');

// 移除监绑定的 listener1 函数
eventEmitter.removeListener('connection', listener1);
console.log("listener1 不再受监听。");

// 触发连接事件
eventEmitter.emit('connection');

eventListeners = eventEmitter.listenerCount('connection');
console.log(eventListeners + " 个监听器监听连接事件。");

console.log("程序执行完毕。");

```

终端执行结果：

```
$ node test_event_emit.js 
2 个监听器监听连接事件。
监听器 listener1 执行。
监听器 listener2 执行。
listener1 不再受监听。
监听器 listener2 执行。
1 个监听器监听连接事件。
程序执行完毕。

```
