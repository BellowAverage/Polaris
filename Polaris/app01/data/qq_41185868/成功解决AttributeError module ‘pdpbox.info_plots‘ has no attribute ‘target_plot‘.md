
--- 
title:  成功解决AttributeError: module ‘pdpbox.info_plots‘ has no attribute ‘target_plot‘ 
tags: []
categories: [] 

---
成功解决AttributeError: module 'pdpbox.info_plots' has no attribute 'target_plot'







**目录**















## **解决问题**

AttributeError: module 'pdpbox.info_plots' has no attribute 'target_plot'





## **解决思路**

**属性错误:模块'pdpbox.info_plots'没有属性'target_plot'**





## **解决方法**

由于版本迭代，该库相关函数用法对应的函数名称已经被替换！

**源代码用法参考：**

将

```
pdpbox.info_plots.target_plot
```

改为

```
pdpbox.info_plots.TargetPlot
```

成功！












