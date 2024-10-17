
--- 
title:  PyQt5隐藏tabwidget 标签 
tags: []
categories: [] 

---
### 隐藏tabwidget 标签

有的时候可能出于某种原因，我们不想让用户看见tabwidget标签，需要隐藏掉。那该怎么办呢，不要急，按照如下即可：

```
self.tabBar = self.tabWidget.findChild(QTabBar)
self.tabBar.hide()

```
