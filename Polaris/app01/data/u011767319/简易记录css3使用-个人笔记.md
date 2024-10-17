
--- 
title:  简易记录css3使用-个人笔记 
tags: []
categories: [] 

---
### 添加小手样式

```
.l-distance {<!-- -->
	  //小手样式属性
      cursor: pointer;
}

```

### 让标签进行360度旋转

```
.l-distance:hover {<!-- -->
      -webkit-animation:haha1 .8s linear infinite;
      animation:haha1 .8s linear infinite;
} @-webkit-keyframes haha1{<!-- --> from{<!-- -->transform:rotate(0)} to{<!-- -->transform:rotate(360deg)} }

```
