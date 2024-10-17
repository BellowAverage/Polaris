
--- 
title:  el-tree在label文字前加自定义图标或者图片 
tags: []
categories: [] 

---
```
&lt;el-tree
  :data="treeData"
  :props="defaultProps"
  accordion
  @node-click="handleNodeClick"&gt;
  &lt;span class="custom-tree-node" slot-scope="{ node, data }"&gt;
    &lt;span&gt;
      &lt;img class="organization-img" src="@/assets/correction/organization.png" alt=""&gt;{<!-- -->{ node.label }}
    &lt;/span&gt;              
  &lt;/span&gt;
&lt;/el-tree&gt;

```

效果如下： <img src="https://img-blog.csdnimg.cn/74191e4aa1f84e36be2ea3d5cf54cd72.jpg#pic_center" alt="在这里插入图片描述">
