
--- 
title:  wepy-redux的使用 
tags: []
categories: [] 

---
因为做的wepy的项目中还没有用到全局状态管理，最近尝试了一下wepy-redux的使用, 

### 安装依赖
- npm install wepy-redux --save- npm install redux --save- npm install redux-actions --save- npm install redux-promise --save
我的项目版本比较老，是 **1.7.2** 版本，然后运行项目的时候会报错，提示没有redux 解决办法： 我是下载yarn add redux@3.7.2得以解决

### 修改下wepy.config.js文件

```
      plugins: [
        'babel-plugin-transform-class-properties',
        'transform-export-extensions',
        'transform-class-properties',
        'transform-decorators-legacy',
        'transform-object-rest-spread',
        'syntax-export-extensions'
      ]

```

### 建立store文件夹

我的文件夹目录如下 <img src="https://img-blog.csdnimg.cn/7803c10626f64d358a9ec97e0e3d8fa8.png#pic_center" alt="在这里插入图片描述">
- store/actions/counter.js （异步操作放actions文件夹下面）
```
import {<!-- --> ASYNC_INCREMENT } from '../types'
import {<!-- --> createAction } from 'redux-actions'

// ASYNC_INCREMENT  为types下面定义的方法名

// 方法定义在  reducer下面

export const asyncInc = createAction(ASYNC_INCREMENT, () =&gt; {<!-- -->
  return new Promise(resolve =&gt; {<!-- -->
    setTimeout(() =&gt; {<!-- -->
      console.log(123456)
      resolve(1)
    }, 1000)
  })
})


```
- store/actions/index.js
```
export * from './counter'

```
- store/reducers/counter.js （注意：reducers文件夹下面的内容是关键）
```
import {<!-- --> handleActions } from 'redux-actions'
import {<!-- --> INCREMENT, DECREMENT, ASYNC_INCREMENT } from '../types'

export default handleActions({<!-- -->
  [INCREMENT] (state) {<!-- -->
    return {<!-- -->
      ...state,
      num: state.num + 1
    }
  },
  [DECREMENT] (state) {<!-- -->
    return {<!-- -->
      ...state,
      num: state.num - 1
    }
  },
  [ASYNC_INCREMENT] (state, action) {<!-- -->
    console.log(123456789111)
    return {<!-- -->
      ...state,
      asyncNum: state.asyncNum + action.payload   // 这个payload为 actions下面传来
    }
  }
}, {<!-- -->
  num: 0,   // 定义的数据
  asyncNum: 0  // 定义的数据
})


```
- store/reducers/index.js
```
import {<!-- --> combineReducers } from 'redux'
import counter from './counter'

export default combineReducers({<!-- -->
  counter
})


```
- store/types/counter.js
```
export const INCREMENT = 'INCREMENT'

export const DECREMENT = 'DECREMENT'

export const ASYNC_INCREMENT = 'ASYNC_INCREMENT'


```
- store/types/index.js
```
export * from './counter'

```
- store/index.js
```

import {<!-- --> createStore, applyMiddleware } from 'redux'
import promiseMiddleware from 'redux-promise'

import rootReducer from './reducers'
export default function configStrore () {<!-- -->
  return createStore(rootReducer, applyMiddleware(promiseMiddleware))
}


```

### app.wpy文件引入redux的store

```
import {<!-- -->
  setStore
} from 'wepy-redux'
import configStore from './store'
const store = configStore();
setStore(store);
wepy.$store = store;

```

### 在页面中的使用

```
&lt;template&gt;
  &lt;view hover-class="none" hover-stop-propagation="false"&gt;
    num的值:{<!-- -->{num}}-{<!-- -->{testNum}}-{<!-- -->{asyncNum}}
    &lt;view class="" hover-class="none" hover-stop-propagation="false"&gt;
      &lt;button @tap="click"&gt;+1&lt;/button&gt;
    &lt;/view&gt;
  &lt;/view&gt;
&lt;/template&gt;

&lt;script&gt;
import wepy from 'wepy'
// 引入connect连接器
import {<!-- -->connect} from 'wepy-redux'
// 引入定义的方法
import {<!-- -->INCREMENT, DECREMENT} from '@/store/types'
import {<!-- -->asyncInc} from '@/store/actions'

// @connect函数是实现数据双向绑定的关键
@connect({<!-- -->
  num(state) {<!-- -->
    return state.counter.num
  },
  asyncNum(state) {<!-- -->
    return state.counter.asyncNum
  },
  inc: 'inc'
}, {<!-- -->
  // 这里也可以用es6的语法简写，可以这样引入，也可以使用dispatch语法
  incNum: INCREMENT,
  decNum: DECREMENT,
  asyncInc
})

export default class Test extends wepy.page {<!-- -->
  config = {<!-- -->
    navigationBarTitleText: '测试页面',
    enablePullDownRefresh: false
  }
  components = {<!-- -->}
  data = {<!-- -->
    showContainer: true,
    // num: wepy.$store.getState().counter.num,
    testNum: wepy.$instance.globalData.testNum
  }
  computed = {<!-- -->
    // 'wepy.$instance.globalData.testNum'() {<!-- -->
    //   this.testNum = wepy.$instance.globalData.testNum
    //   console.log(777, wepy.$instance.globalData.testNum)
    // },
    // 'wepy.$store.getState().counter.num' () {<!-- -->
    //   // this.num = wepy.$store.getState().counter.num
    //   console.log(666, this.num)
    // }
  }
  methods = {<!-- -->
    click() {<!-- -->
      // 调用同步更改
      // wepy.$store.dispatch({<!-- -->
      //   type: 'INCREMENT'  // 对应reducer里面的types命名的的方法
      //   // payload: {a:1,b:1}  // 修改的对象
      // })
      // 如果需要在这里面调用incNum，使用this.methods.incNum()，而不是this.incNum()
      this.methods.incNum()
      console.log(this.num, wepy.$store.getState().counter.num)
      // 调用异步更改
      // wepy.$store.dispatch(asyncInc())
      this.methods.asyncInc()
      console.log(this.asyncNum)
      // 查看全局变量和全局动态绑定变量的区别
      wepy.$instance.globalData.testNum++
      console.log(555, wepy.$instance.globalData.testNum)
    }
  }
  onLoad () {<!-- -->

  }
}
&lt;/script&gt;

```

参考文档   
