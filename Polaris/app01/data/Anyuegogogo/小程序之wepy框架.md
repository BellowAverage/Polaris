
--- 
title:  小程序之wepy框架 
tags: []
categories: [] 

---
最近这段时间有做用到wepy框架的小程序啦，记录一下在开发中一些常用的和需要注意的东西。

#### 数据绑定

可以直接**this.xxx = “xxx”**，但是需要注意的是在**methods**之外的方法中，要这样去改data中的数据就必须要加上**this.$apply()**

#### methods

只有bindtap这类方法才需要放到methods中，其他的方法都与onLoad平级

#### events

自定义的事件，事件函数写这里面（组件的事件监听需要写在events里）

```
// 在子组件中
this.$emit('changeDate', time)
// 在父组件中
events = {<!-- -->
  'changeDate': (day) =&gt; {<!-- -->
    this.getTask(day)
  }
}

```

#### 事件绑定以及事件传参

事件绑定语法使用优化语法代替
- 原 bindtap=“click” 替换为 @tap=“click”，原catchtap="click"替换为@tap.stop=“click”（阻止冒泡事件向上冒泡）。- 原 capture-bind:tap=“click” 替换为 @tap.capture=“click”，原capture-catch:tap="click"替换为@tap.capture.stop=“click”。- 事件传参使用优化后语法代替。 原bindtap=“click” data-index="{<!-- -->{index}}"替换为@tap=“click({<!-- -->{index}})”
#### wepy框架组件传值

###### 1.父传子

和vue一样动态属性的方式传值，然后子组件props接收

```
// 在父组件内(注意：想要父组件的值改变，传给子组件中的值也跟着变化，一定要用.sync！！！为此踩了好久的坑)
&lt;children :list.sync="list"&gt;&lt;/children&gt;
// 在子组件内
list: {<!-- -->
  type: Array,
  default: []
}

```

##### 2.$broadcast

这个是用来父传子自定义事件的，可以携带参数传值

```
// 在父组件内
this.$broadcast('index-broadcast', '我正在测试哈哈哈哈')
// 在子组件内
events = {<!-- -->
	'index-broadcast': (...args) =&gt; {<!-- -->
		console.log(args)          //["我正在测试哈哈哈哈", _class]
	}
}

```

##### 3.$emit

这是子组件传给父组件自定义事件，可以携带参数传值

```
// 在子组件中
this.$emit('changeDate', time)
// 在父组件中
events = {<!-- -->
  'changeDate': (day) =&gt; {<!-- -->
    this.getTask(day)
  }
}

```

##### 4.$invoke

如果通过当前组件进行$invoke触发事件，如果父组件已经在components里面引入了子组件就可以直接通过invoke来单独向子组件发送事件。如果是子组件之间的事件交互，第一个参数就需要对应组件的路径。 简单的理解就是可以调用子组件或者兄弟组件中的函数，给该函数传参。

```
// 父子组件中使用$invoke的情况下
// 在父组件中
this.$invoke('子组件，必须要单引号括起来', '子组件方法名称',  param1,param2,param3.......);
this.$invoke('Tabbar', 'changeSelected', 0)
// 在子组件Tabbar中
methods = {<!-- -->
  changeSelected(num) {<!-- -->
    this.selected = num
  }
};

// 在兄弟组件中使用$invoke的情况下
this.$invoke('子组件的相对路径', '子组件方法名称', param1,param2,param3.......);

```

如果有总结不对的地方，欢迎指正哦~
