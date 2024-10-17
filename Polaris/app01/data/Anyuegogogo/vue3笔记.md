
--- 
title:  vue3笔记 
tags: []
categories: [] 

---
### 1.setup函数(选项式)

**1.生命周期**
- 执行顺序在 beforeCreate 和 created这两个钩子函数之前，是最早执行的，在程序运行中，setup函数只执行一次，创建的是data和method- 在 setup中没有this- beforeDestory/ destoryed 改名 beforeUnmount / unmounted；setup替代了beforeCreate/ created；beforeCreate/ created/ beforeMount/ mounted / beforeUpdate / updated 写在setup()里，并且加前缀on；beforeCreate/ created/ beforeMount/ mounted / beforeUpdate / updated继续使用也不会报错，但是不能继续使用beforeDestory/ destoryed
**2.setup的参数** props、context
1. props props是响应式的，当传入新的 prop 时，它将被更新。因为 props 是响应式的，不能使用 ES6 解构，它会消除 prop 的响应性。如果需要解构 prop，可以在 setup 函数中使用 toRefs 函数。 在子组件中
```
import {<!-- --> ref, toRefs, watch } from 'vue' // 首先要引入
props: {<!-- -->
  name: {<!-- -->
    type: String,
    default: ''
  }
}, // 定义类型
setup (props) {<!-- -->
  const {<!-- --> name } = toRefs(props) // 解构要用到toRefs
}

```

2.context 传递给 setup 函数的第二个参数是 context。context 是一个普通的 JavaScript 对象，有三个property。context是普通对象，不是响应式的，可以在传参的时候直接解构。

```
export default {<!-- -->
  setup(props, context) {<!-- -->
    // Attribute (非响应式对象)
    console.log(context.attrs)

    // 插槽 (非响应式对象)
    console.log(context.slots)

    // 触发事件 (方法)
    console.log(context.emit)
  }
}
export default {<!-- -->
  setup(props, {<!-- --> attrs, slots, emit }) {<!-- -->
    ...
  }
}

```
- attrs: 接收在父组件传递过来的，并且没有在props中声明的参数。- emit：子组件对父组件发送事件，在vue2中，子对父发送事件采用this.$emit对父组件发送事件，在vue3中子组件对父组件发送事件采用context.emit发送事件。- slots：和vue2中的插槽使用类似
**3.setup里面的函数** 1.ref 使数据响应式。使用ref的数据在setup函数被访问时，需要加.value，在模板中被使用时可以直接访问，但如果是深层次的，还是需要加.value。

2.reactive 使数据响应式 基础数据类型用ref,对象类型用reactive

3.toRefs 与 toRef 不一样的是， toRefs 是针对整个对象的所有属性，目标在于将响应式对象（ reactive 封装）转换为普通对象，且保持响应性。

```
export default {<!-- -->
  name: 'ToRefs',
  setup () {<!-- -->
    const state = reactive({<!-- -->
      age: 20,
      name: 'leyo'
    })
    const stateRefs = toRefs(state)
    return {<!-- -->
      ...stateRefs
    }
  }
}

```

**4.toRef** 在一个响应式对象里面，如果其中有一个属性要拿出来单独做响应式的话，就用 toRef。
- 用于响应式对象，产出的结果具备响应式，且修改响应式数据是会影响到原始数据。- 如果用于普通对象（非响应式对象），产出的结果不具备响应式。- 和ref的区别：ref本质是拷贝，修改响应式数据不会影响原始数据；toRef的本质是引用关系，修改响应式数据会影响原始数据。
**5.watch** 三个参数：一个想要侦听的响应式引用或 getter 函数;一个回调;可选的配置选项.

```
  setup () {<!-- -->
    const count = ref(0)
    const countWatch = ref(0)
    watch(
      // getter 函数
      () =&gt; count.value + 1,
      (newValue) =&gt; {<!-- -->
        console.log('newValue', newValue)
        countWatch.value = newValue
      },
      {<!-- -->
        immediate: true
      }
    )

    // watch(
    //   // 一个想要侦听的响应式引用
    //   count,
    //   (newValue) =&gt; {<!-- -->
    //     countWatch.value = ++newValue
    //   },
    //   {<!-- -->
    //     immediate: true
    //   }
    // )
    return {<!-- -->
      count,
      countWatch
    }
  }

```

>  
 特点： 
 - 具有一定的惰性lazy,第一次页面展示的时候不会执行，只有数据变化的时候才会执行- 参数可以拿到当前值和原始值 


**6.watchEffect**

>  
 - 立即执行，没有惰性，页面的首次加载就会执行- 不需要传递要侦听的内容 会自动感知代码依赖，不需要传递很多参数，只要传递一个回调函数- 不能获取之前数据的值 只能获取当前值 


```
  setup () {<!-- -->
    const count = ref(0)
    const countWatch = ref(0)
    watchEffect(
      () =&gt; {<!-- -->
        countWatch.value = ++count.value
      }
    )
    return {<!-- -->
      count,
      countWatch
    }
  }

```

**7.computed** 返回一个不可变的响应式 ref 对象。

```
	const count = ref(0)
    const countWatch = computed(
      () =&gt; count.value + 1
    )
    ```
// 如果希望对象是可写的，则需要用 get 和 set 函数创建
    const count = ref(0)
    const countWatch = computed({<!-- -->
      get: () =&gt; count.value + 1,
      set: (val) =&gt; {<!-- -->
        count.value = val - 1
      }
    })
    // 结果：
	// count: 0  countWatch: 1

```

**8.readonly** 接受一个对象 (响应式或纯对象) 或 ref 并返回原始对象的只读代理。只读代理是深层的：任何被访问的嵌套 property 也是只读的。

**9.provider和inject** provide和inject可以实现嵌套组件之间进行传递数据。 这两个函数都是在setup函数中使用的。 父级组件使用provide向下进行传递数据。 子级组件使用inject来获取上级组件传递过来的数据。(可跨层级传值) 为了增加 provide 值和 inject 值之间的响应性，我们可以在 provide 值时使用 ref 或 reactive。而且还是不要改变单向数据流，如果要改变provide的值，建议 provide 一个方法来负责改变响应式 property。最后，如果要确保通过 provide 传递的数据不会被 inject 的组件更改，我们建议对提供者的 property 使用 readonly。

```
&lt;template&gt;
  &lt;MyMarker /&gt;
&lt;/template&gt;

&lt;script&gt;
import {<!-- --> provide, reactive, readonly, ref } from 'vue'
import MyMarker from './MyMarker.vue'

export default {<!-- -->
  components: {<!-- -->
    MyMarker
  },
  setup() {<!-- -->
    const location = ref('North Pole')
    const geolocation = reactive({<!-- -->
      longitude: 90,
      latitude: 135
    })

    const updateLocation = () =&gt; {<!-- -->
      location.value = 'South Pole'
    }

    provide('location', readonly(location))
    provide('geolocation', readonly(geolocation))
    provide('updateLocation', updateLocation)
  }
}
&lt;/script&gt;

```

### 2.单文件组件script setup

**1. 是组合式 API 的编译时语法糖，相比于普通的 **
- 更少的样板内容，更简洁的代码。- 能够使用纯 Typescript 声明 props 和抛出事件。- 更好的运行时性能 (其模板会被编译成与其同一作用域的渲染函数，没有任何的中间代理)。- 更好的 IDE 类型推断性能 (减少语言服务器从代码中抽离类型的工作)。 **1.无需return才能在setup外部使用**
**2.defineProps** 在 script setup中必须使用 defineProps 和 defineEmits API 来声明 props 和 emits ，它们具备完整的类型推断并且在 script 标签中是直接可用的：

```
&lt;script setup&gt;
const props = defineProps({<!-- -->
  foo: String
})

const emit = defineEmits(['change', 'delete'])
// setup code
&lt;/script&gt;

```

2.1 修改props 所有的 props 都遵循着单向绑定原则，想要更改一个 prop 的需求通常来源于以下两种场景：
1. prop 被用于传入初始值；而子组件想在之后将其作为一个局部数据属性。在这种情况下，最好是新定义一个局部数据属性，从 props 上获取初始值即可：
```
const props = defineProps(['initialCounter'])

// 计数器只是将 props.initialCounter 作为初始值
// 像下面这样做就使 prop 和后续更新无关了
const counter = ref(props.initialCounter)

```
1. 需要对传入的 prop 值做进一步的转换。在这种情况中，最好是基于该 prop 值定义一个计算属性：
```
const props = defineProps(['size'])

// 该 prop 变更时计算属性也会自动更新
const normalizedSize = computed(() =&gt; props.size.trim().toLowerCase())

```

2.2 Prop 校验：

```
defineProps({<!-- -->
  // 基础类型检查
  // （给出 `null` 和 `undefined` 值则会跳过任何类型检查）
  propA: Number,
  // 多种可能的类型
  propB: [String, Number],
  // 必传，且为 String 类型
  propC: {<!-- -->
    type: String,
    required: true
  },
  // Number 类型的默认值
  propD: {<!-- -->
    type: Number,
    default: 100
  },
  // 对象类型的默认值
  propE: {<!-- -->
    type: Object,
    // 对象或数组的默认值
    // 必须从一个工厂函数返回。
    // 该函数接收组件所接收到的原始 prop 作为参数。
    default(rawProps) {<!-- -->
      return {<!-- --> message: 'hello' }
    }
  },
  // 自定义类型校验函数
  propF: {<!-- -->
    validator(value) {<!-- -->
      // The value must match one of these strings
      return ['success', 'warning', 'danger'].includes(value)
    }
  },
  // 函数类型的默认值
  propG: {<!-- -->
    type: Function,
    // 不像对象或数组的默认，这不是一个
    // 工厂函数。这会是一个用来作为默认值的函数
    default() {<!-- -->
      return 'Default function'
    }
  }
})

```

**3. defineEmits** 在模板中直接使用

```
&lt;!-- MyComponent --&gt;
&lt;button @click="$emit('someEvent')"&gt;click me&lt;/button&gt;

```

通过 defineEmits() 宏来声明它要触发的事件

```
&lt;script setup&gt;
const emit = defineEmits(['inFocus', 'submit'])

function buttonClick() {<!-- -->
  emit('submit')
}
&lt;/script&gt;

&lt;script setup lang="ts"&gt;
const emit = defineEmits&lt;{<!-- -->
  (e: 'change', id: number): void
  (e: 'update', value: string): void
}&gt;()
&lt;/script&gt;

```

**4. 组件上的 ref**

```
&lt;script setup&gt;
import {<!-- --> ref, onMounted } from 'vue'
import Child from './Child.vue'

const child = ref(null)

onMounted(() =&gt; {<!-- -->
  // child.value 是 &lt;Child /&gt; 组件的实例
})
&lt;/script&gt;

&lt;template&gt;
  &lt;Child ref="child" /&gt;
&lt;/template&gt;

```

在选项式api中，被引用的组件实例和该子组件的 this 完全一致，这意味着父组件对子组件的每一个属性和方法都有完全的访问权。

使用了 script setup 的组件是默认私有的：一个父组件无法访问到一个使用了 script setup 的子组件中的任何东西，除非子组件在其中通过 defineExpose 宏显式暴露

```
&lt;script setup&gt;
import {<!-- --> ref } from 'vue'

const a = 1
const b = ref(2)

// 像 defineExpose 这样的编译器宏不需要导入
defineExpose({<!-- -->
  a,
  b
})
&lt;/script&gt;

```

**5. 依赖注入** 当提供 / 注入响应式的数据时，建议尽可能将任何对响应式状态的变更都保持在供给方组件中。这样可以确保所提供状态的声明和变更操作都内聚在同一个组件内，使其更容易维护。

```
&lt;!-- 在供给方组件内 --&gt;
&lt;script setup&gt;
import {<!-- --> provide, ref } from 'vue'

const location = ref('North Pole')

function updateLocation() {<!-- -->
  location.value = 'South Pole'
}

provide('location', {<!-- -->
  location,
  updateLocation
})
&lt;/script&gt;

```

```
&lt;!-- 在注入方组件 --&gt;
&lt;script setup&gt;
import {<!-- --> inject } from 'vue'

const {<!-- --> location, updateLocation } = inject('location')
&lt;/script&gt;

&lt;template&gt;
  &lt;button @click="updateLocation"&gt;{<!-- -->{<!-- --> location }}&lt;/button&gt;
&lt;/template&gt;

```

注入默认值

```
// 如果没有祖先组件提供 "message"
// `value` 会是 "这是默认值"
const value = inject('message', '这是默认值')
// 在一些场景中，默认值可能需要通过调用一个函数或初始化一个类来取得。为了避免在用不到默认值的情况下进行不必要的计算或产生副作用，我们可以使用工厂函数来创建默认值：
const value = inject('key', () =&gt; new ExpensiveClass(), true)

```
