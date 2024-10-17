
--- 
title:  关于uniapp + ts 的一些总结，uniapp组件通信 
tags: []
categories: [] 

---
### 完整的对比一下

首先，先来回忆一下uniapp的基础写法

```
&lt;script&gt;
export default{<!-- -->
    data(){<!-- -->
        return {<!-- -->}
    },
    methods:{<!-- -->},
    computed:{<!-- -->},
    filters:{<!-- -->},
    watch:{<!-- -->},
    onLoad:{<!-- -->}
}
&lt;/script&gt;

```

下面是 uniapp + ts 的一些写法

```
&lt;template&gt;
	&lt;view class="content"&gt;
		&lt;view&gt;
			&lt;text class="title"&gt;{<!-- -->{<!-- -->title}}&lt;/text&gt;
		&lt;/view&gt;
		&lt;view&gt;
			&lt;text class="title"&gt;{<!-- -->{<!-- -->age}}&lt;/text&gt;
			&lt;button @click="addHandler(1)"&gt;+1&lt;/button&gt;
		&lt;/view&gt;
		&lt;Child :question="question" @answer="answerHandler"&gt;&lt;/Child&gt;
		&lt;view&gt;{<!-- -->{<!-- -->answer ? answer : ''}}&lt;/view&gt;
		&lt;AnotherChild&gt;&lt;/AnotherChild&gt;
	&lt;/view&gt;
&lt;/template&gt;

&lt;script lang="ts"&gt;
	import {<!-- --> Vue, Component, Watch } from 'vue-property-decorator'
	import Child from './components/Child'
	import AnotherChild from './components/AnotherChild'

	@Component({<!-- -->
		components: {<!-- -->
			Child,
			AnotherChild
		}
	})
	export default class Index extends Vue{<!-- -->
		// data
		private title:String = 'Hello World'; 
		private num:Number = 123; 
		private question:String = '怎么才能光吃不胖呢'; 
		private answer:String = '';
		//计算属性
		get age():Number{<!-- --> 
			return this.num;
		}
		// 生命周期
		private onLoad(){<!-- -->
			this.printTitle();
		}
		// watch监听器
		@Watch('num') //watch，此处是监听title的变化
		onNumChange(newVal:Number,oldVal:Number){<!-- -->
			console.log(newVal,oldVal);
		}
		// 方法
		private printTitle():void{<!-- --> //methods
			console.log('hahahhhaha')
		}
		private addHandler(n: any):void {<!-- -->
			this.num = this.num + n
		}
		private answerHandler(val: String) {<!-- -->
			this.answer = val
		}
	}
&lt;/script&gt;

```

### uniapp组件通信

#### 1. 父传子

```
// 父组件
&lt;Child :question="question"&gt;&lt;/Child&gt;

// 子组件
// prop属性
@Prop(String) private question!: string;
&lt;text class="title"&gt;{<!-- -->{<!-- -->question}}&lt;/text&gt;

```

#### 2. 子传父

```
// 子组件
&lt;button @click="emitHandler"&gt;子组件向父组件触发自定义事件&lt;/button&gt;
// Emit子组件触发
@Emit('answer')
private emitHandler() {<!-- -->
  return "无解"
}

// 父组件
&lt;Child @answer="answerHandler"&gt;&lt;/Child&gt;
private answerHandler(val: String) {<!-- -->
	this.answer = val
}

```

#### 3. 兄弟组件之间通信

```
// 子组件A
&lt;button @click="brotherHandler"&gt;兄弟组件传值&lt;/button&gt;
// 方法
private brotherHandler() {<!-- -->
  uni.$emit('addMoney', 100)
}

// 子组件B
private created() {<!-- -->
  uni.$on('addMoney',num =&gt; {<!-- -->
    this.money += num
  })
}

```

如果有不对的地方，欢迎指正哦~
