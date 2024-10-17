
--- 
title:  使用el-scrollbar实现定位滚动，以及el-scrollbar去掉横向滚动条 
tags: []
categories: [] 

---
#### 实现滚动

```
&lt;el-scrollbar ref="scroll" style="height: 100%;"&gt;
  // ...
&lt;/el-scrollbar&gt;

```

可以使用如下属性： 想要滚动到哪个指定位置，自己获取或计算

```
this.$refs['scroll'].wrap.scrollTop = 0  //想滚到哪个高度，就写多少

```

#### el-scrollbar去掉横向滚动条

```
::v-deep .el-scrollbar__wrap {<!-- -->
  overflow-x: hidden; 
}

```

参考链接  
