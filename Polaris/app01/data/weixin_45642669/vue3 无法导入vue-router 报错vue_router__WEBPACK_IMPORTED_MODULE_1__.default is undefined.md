
--- 
title:  vue3 无法导入vue-router 报错vue_router__WEBPACK_IMPORTED_MODULE_1__.default is undefined 
tags: []
categories: [] 

---
## 问题描述：

### 报错vue_router__WEBPACK_IMPORTED_MODULE_1__.default is undefined

 

### 在启动的时候，报错

```
export 'default' (imported as 'Vue') was not found in 'vue' 

```

```
export 'default' (imported as 'VueRouter') was not found in 'vue-router' 

```

报错信息如下： <img src="https://img-blog.csdnimg.cn/c30ee1023cd54ba594694fc2275bc6cc.png" alt="在这里插入图片描述">

#### 原因和解决：

## vue3 绑定的是vue-router4

需要下载

```
npm install vue-router@4

```

<img src="https://img-blog.csdnimg.cn/53c7f53ce65e40178bb08d754b750287.png" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/e68d77729b754cf0811843d850cd348d.png" alt="在这里插入图片描述">

## 启动命令修改

在vue3里面，修改了启动的命令。不能够直接调用Vue

Vue3的写法如下：

```
import { createRouter, createWebHashHistory} from 'vue-router'

```

 

```
import { createApp } from 'vue'

```
