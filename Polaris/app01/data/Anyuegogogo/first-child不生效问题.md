
--- 
title:  :first-child不生效问题 
tags: []
categories: [] 

---
使用:first-child的元素必须是其父盒子里的第一个元素，不能有兄弟节点 比如一下这种无效

```
&lt;div&gt;
	&lt;div&gt;&lt;/div&gt;
	&lt;div class="item"&gt;&lt;/div&gt;
	&lt;div class="item"&gt;&lt;/div&gt;
&lt;/div&gt;

// 这种无效，因为它还有其他兄弟节点在上面，不是第一个
.item:first-child {<!-- -->
  ......
}

```

改成如下这种有效

```
&lt;div&gt;
	&lt;div&gt;&lt;/div&gt;
	&lt;div&gt;
		&lt;div class="item"&gt;&lt;/div&gt;
		&lt;div class="item"&gt;&lt;/div&gt;
	&lt;/div&gt;
&lt;/div&gt;

// 这种有效
.item:first-child {<!-- -->
  ......
}


```
