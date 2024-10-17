
--- 
title:  vue实现移动端左滑删除的功能 
tags: []
categories: [] 

---
### 由于需要监听手指的左右滑动事件，所以用到了v-touch这个插件。

### npm安装

```
npm install vue-touch@next --save
//main.js中引入：
import VueTouch from 'vue-touch'
Vue.use(VueTouch, {<!-- -->name: 'v-touch'})

```

### 使用

在你的元素中监听左滑、右滑事件

```
//html代码
    &lt;v-touch @swipeleft="swiperleft" @swiperight="swiperight"&gt;
      &lt;div :class="{ 'person-card': true, swiper: item.isSwiper }"&gt;
      这里是内容
      &lt;/div&gt;
    &lt;/v-touch&gt;

  private swiperight(e) {<!-- -->
  // 右滑大于30
    if (this.delP) {<!-- -->
      if (e.deltaX &gt; 30) {<!-- -->
        this.$emit("swiperight");
      }
    }
  }

  private swiperleft(e) {<!-- -->
  // 左滑大于30
    if (this.delP) {<!-- -->
      if (e.deltaX &lt; -30) {<!-- -->
        this.$emit("swiperleft");
      }
    }
  }

```
