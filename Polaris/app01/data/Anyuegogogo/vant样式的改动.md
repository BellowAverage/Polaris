
--- 
title:  vant样式的改动 
tags: []
categories: [] 

---
### 1、修改van-field的placeholder文字颜色改不动的时候（h5端）

```
::v-deep .van-field__control::-webkit-input-placeholder {<!-- -->
  color: #9b9ba4;
}

```
