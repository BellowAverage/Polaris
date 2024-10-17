
--- 
title:  vue3 props传入的组件无法正常刷新 
tags: []
categories: [] 

---
## 问题描述：
- vue3- 写入的数据无法正常修改和响应，但是从子组件获取正常- 使用props父子传值
## 解决方案
- 在setup导出的时候，直接导入props，而不是导入props.变量
错误用法：

```
props: [var1]
let var1 = "张三"
setup() {
	return {
		var1
	}
}

```

正确用法：

```
props: [var1]
setup() {
	return {
		props
	}
}

```

## 问题原因
- vue3建议是数据单向流动，所以当父传子，然后让子进行数据修改的时候发现无法修改，这是正常的 当ref数据传递到子的时候，就会直接被取值失去响应式能力- 可以向子中传入reactive对象，即可破坏掉父子传值单向流动限制，但是不推荐