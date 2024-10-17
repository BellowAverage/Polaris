
--- 
title:  el-menu动态设置default-active的值不生效 
tags: []
categories: [] 

---
```
    &lt;el-menu :default-active="active" ref="menu"&gt;
      &lt;el-menu-item
        :index="item.id"
        v-for="item in currentList"
        :key="item.id"
        @click="menuSelect(item)"
      &gt;
        &lt;span slot="title"&gt;{<!-- -->{<!-- --> item.templateName }}&lt;/span&gt;
      &lt;/el-menu-item&gt;
    &lt;/el-menu&gt;

	// 试试如下设置
    (this.$refs.menu as any).activeIndex = "";

```
