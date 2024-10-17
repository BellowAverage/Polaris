
--- 
title:  pinia的使用 
tags: []
categories: [] 

---
### 一、state的使用

###### 1.一个简单的小例子：（重点讲是否可响应式）

###### 定义一个store

```
import {<!-- --> defineStore } from 'pinia';
// useStore 可以是 useUser、useCart 之类的任何东西
// 第一个参数是应用程序中 store 的唯一 id
export const countAdd = defineStore('countAdd', {<!-- -->
  // other options...
  state: () =&gt; ({<!-- --> count: 0 }),
  getters: {<!-- -->
    double: (state) =&gt; state.count * 2,
  },
  actions: {<!-- -->
    increment() {<!-- -->
      this.count++;
    },
  },
});

```

###### 使用

###### 1.1 以下是可实现响应式的写法

```
// 写法一：结合computed使用
// 页面中
  &lt;div&gt;{<!-- -->{<!-- --> count }}&lt;/div&gt;
  &lt;div&gt;{<!-- -->{<!-- --> double }}&lt;/div&gt;
  &lt;van-button @click="increment"&gt;点击&lt;/van-button&gt;
// script中
  import {<!-- --> computed } from 'vue';
  import {<!-- --> countAdd } from '/@/store/modules/countAdd';
  const countStore = countAdd();
  // 这种写法是响应式的
  const count = computed(() =&gt; countStore.count);
  const double = computed(() =&gt; countStore.double);
  // 是的，没错，可以通过 store 实例访问状态来直接读取和写入状态
  countStore.count++;
  const increment = () =&gt; {<!-- -->
    countStore.count++;
  };

// 写法二：直接在页面中引用
// 页面中
  &lt;div&gt;count:{<!-- -->{<!-- --> countStore.count }}&lt;/div&gt;
  &lt;div&gt;double:{<!-- -->{<!-- --> countStore.double }}&lt;/div&gt;
  &lt;van-button @click="increment"&gt;点击&lt;/van-button&gt;
// script中
  import {<!-- --> computed } from 'vue';
  import {<!-- --> countAdd } from '/@/store/modules/countAdd';
  const countStore = countAdd();
  // 是的，没错，可以通过 store 实例访问状态来直接读取和写入状态
  countStore.count++;
  const increment = () =&gt; {<!-- -->
    countStore.count++;
  };

```

###### 1.2 以下是没有响应式的写法

```
// 页面中
  &lt;div&gt;{<!-- -->{<!-- --> count }}&lt;/div&gt;
  &lt;van-button @click="increment"&gt;点击&lt;/van-button&gt;
// script中
  import {<!-- --> countAdd } from '/@/store/modules/countAdd';
  const countStore = countAdd();
  // 解构不行！！不是响应式的
  // const { count } = countStore;
  // 下面这种写法也不行！！不是响应式的
  // const count = countStore.count;
  const increment = () =&gt; {<!-- -->
    countStore.count++;
  };

```

###### 2.访问 “state”

>  
 默认情况下，您可以通过 store 实例访问状态来直接读取和写入状态： 


```
const store = useStore()
store.counter++

```

###### 3.重置状态

```
const store = useStore()
store.$reset()

```

###### 4.改变状态

除了直接读写，也可以使用 $patch() 方法，支持“state”对象同时应用多个更改

```
store.$patch({<!-- -->
  counter: store.counter + 1,
  name: 'Abalam',
})
// 或
cartStore.$patch((state) =&gt; {<!-- -->
  state.items.push({<!-- --> name: 'shoes', quantity: 1 })
  state.hasChanged = true
})

```

###### 使用state要注意的点：

1、pinia和vuex一样，一刷新，数据会重置 2、不能对其进行解构：store 是一个用reactive 包裹的对象，这意味着不需要在getter 之后写.value，但是，就像setup 中的props 一样，我们不能对其进行解构
