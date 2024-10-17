
--- 
title:  vue3 + vite 项目使用vant3 遇到的一些问题 
tags: []
categories: [] 

---
### 1.toast的使用

**使用toast没有样式的问题**：要专门引入css文件，可以局部引用也可以全局引用

```
// 全局引入（引入一次，便可不再引入）
import 'vant/es/toast/style';
// 注意在页面中的使用还要专门引入（我是在局部引入的，按照官网的全局注册没有生效）
import {<!-- --> Toast } from 'vant';

```

### 2.dialog的使用

使用dialog也要专门引入组件和css

```
// 全局引入（引入一次，便可不再引入）
import {<!-- --> Dialog } from 'vant';
// 注意在页面中的使用还要专门引入（我是在局部引入的，按照官网的全局注册没有生效）
import 'vant/es/dialog/style';


```

引入后，使用dialog函数ok没有问题，在页面中**使用van-dialog的时候会报错而且点击取消控制台也会报错，并且自定义的组件的内容还不显示**，解决方法如下：

```
// 全局引入（引入一次，便可不再引入）
import {<!-- --> Dialog } from 'vant';
// 注意在页面中的使用还要专门引入（我是在局部引入的，按照官网的全局注册没有生效）
import 'vant/es/dialog/style';
// 重点是下面这个
const VanDialog = Dialog.Component;

// 然后页面上可以正常使用了
&lt;van-dialog v-model:show="phoneNumberConfirm" title="信息确认" show-cancel-button&gt;
  &lt;div class="dialog-box"&gt;
    &lt;div class="box"&gt;
      &lt;div class="title"&gt;请确认您的手机号码为XXX&lt;/div&gt;
      &lt;div class="vue"&gt;12311212&lt;/div&gt;
    &lt;/div&gt;
  &lt;/div&gt;
&lt;/van-dialog&gt;

```
