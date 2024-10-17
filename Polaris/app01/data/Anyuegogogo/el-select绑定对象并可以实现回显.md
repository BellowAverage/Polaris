
--- 
title:  el-select绑定对象并可以实现回显 
tags: []
categories: [] 

---
```
  &lt;el-select v-model="scope.row.rowItem"
             placeholder="请选择"
             @change="changeHandle(scope.row.rowItem, index, scope.$index)"
             clearable
             value-key="rowIndex"&gt;
    &lt;el-option v-for="item in optionsData"
               :key="item.rowIndex"
               :label="item.rowlabel"
               :value="{rowIndex: item.rowIndex, rowTitle: item.rowTitle}"
               :disabled="item.disabled"&gt;
    &lt;/el-option&gt;
  &lt;/el-select&gt;

```

>  
 - 注意value值绑定的对象，需要啥数据就绑定自己想要的数据- 想要实现回显，注意value-key绑定的键名 


<img src="https://img-blog.csdnimg.cn/e0789c2ab8d3402a81881d86a6c6b42f.png#pic_center" alt="在这里插入图片描述">
