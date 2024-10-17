
--- 
title:  el-cascader获取name值 
tags: []
categories: [] 

---
给el-cascader添加ref，然后在@change事件中获取如下:

```
 &lt;el-cascader
   clearable
   v-model="cityCode"
   placeholder="请选择"
   :props="defaultProps"
   :options="AllArea"
   @change="areaChange"
   ref="areaCascader"
   style="width: 100%"
 &gt;&lt;/el-cascader&gt;

  public areaChange() {<!-- -->
  	console.log((this.$refs["areaCascader"] as any).getCheckedNodes()[0].pathLabels)
  }

```

如果是在一个数组中获取每个cascader对应的name数组：

```
&lt;el-row v-for="(item, index) in locationList" :key="index"&gt;
 &lt;el-cascader
   clearable
   v-model="item.cityCode"
   placeholder="请选择"
   :props="defaultProps"
   :options="AllArea"
   @change="areaChange($event, index)"
   ref="areaCascader"
   style="width: 100%"
 &gt;&lt;/el-cascader&gt;
&lt;/el-row&gt;

  public areaChange(arr, index) {<!-- -->
    console.log(
      arr[0],
      index,
      this.locationList,
      (this.$refs["areaCascader"] as any)[index].getCheckedNodes()[0].pathLabels
    );
  }

```
