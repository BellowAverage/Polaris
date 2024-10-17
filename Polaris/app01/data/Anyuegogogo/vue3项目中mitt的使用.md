
--- 
title:  vue3项目中mitt的使用 
tags: []
categories: [] 

---- Vue2.x使用EventBus进行组件通信，而Vue3.x推荐使用mitt.js。- 比起Vue实例上的EventBus，mitt.js好在哪里呢？首先它足够小，仅有200bytes，其次支持全部事件的监听和批量移除，它还不依赖Vue实例，所以可以跨框架使用，React或者Vue，甚至jQuery项目都能使用同一套库。
#### 安装

```
npm install --save mitt

```

#### 创建Mitt实例

utils/eventBus.ts

```
import mitt from 'mitt'

export const globalEventBus = mitt()

```

#### 使用

```
// 引入
import {<!-- --> globalEventBus } from '@/utils/eventBus'

// emit
setInterval(() =&gt; {<!-- -->
  globalEventBus.emit('test', 1)
}, 2000)

const fn = (val) =&gt; {<!-- -->
  console.log(val)
  console.log('fn')
}

// on
globalEventBus.on('test', fn)

// off
onBeforeUnmount(() =&gt; {<!-- -->
  console.log('onBeforeUnmount')
  globalEventBus.off('test') // 生效
  // globalEventBus.off('test', fn) // 生效，但fn内的代码不会执行
  // globalEventBus.off('test', () =&gt; { // 不生效
  //   console.log('off')
  // })
})

```

注意：
- 一定要手动关闭全局监听事件，off- 如上所示，off生效与不生效的情况一定要注意！！off重新定义一个回调函数是不会生效的，传入订阅时的回调函数才会生效，但是回调函数里面的代码不执行。
#### 详细使用

参考

```
import mitt from 'mitt'

const emitter = mitt()

// listen to an event
emitter.on('foo', e =&gt; console.log('foo', e) )

// listen to all events
emitter.on('*', (type, e) =&gt; console.log(type, e) )

// fire an event
emitter.emit('foo', {<!-- --> a: 'b' })

// clearing all events
emitter.all.clear()

// working with handler references:
function onFoo() {<!-- -->}
emitter.on('foo', onFoo)   // listen
emitter.off('foo', onFoo)  // unlisten

```
