
--- 
title:  在vue3中使用vite-svg-loader插件 
tags: []
categories: [] 

---
>  
 vite-svg-loader插件可以让我们像使用vue组件那样使用svg图，使用起来超级方便。 


#### 安装

```
npm install vite-svg-loader --save-dev

```

#### 使用

```
import svgLoader from 'vite-svg-loader'
 
export default defineConfig({<!-- -->
  plugins: [vue(), svgLoader()]
})

```

#### 组件里使用

在路径后加`?component`，表示像组件一样使用。

```
import Icon404 from '@/assets/icons/svg/404.svg?component';
&lt;Icon404&gt;&lt;/Icon404&gt;

```

在路径后加?url，可以做为图片url引入

```
import Icon404 from '@/assets/icons/svg/404.svg?url';
&lt;img :src="Icon404" alt=""&gt;

```

参考链接： 官方文档：
