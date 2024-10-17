
--- 
title:  vue3中使用插件vite-plugin-svg-icons 
tags: []
categories: [] 

---
在vue3 + vite 项目中使用svg图标 **插件：vite-plugin-svg-icons**
- 预加载 在项目运行时就生成所有图标,只需操作一次 dom- 高性能 内置缓存,仅当文件被修改时才会重新生成
#### 安装

```
yarn add vite-plugin-svg-icons -D
# or
npm i vite-plugin-svg-icons -D
# or
pnpm install vite-plugin-svg-icons -D

```

#### 使用
- vite.config.ts 中的配置插件
```
import {<!-- --> createSvgIconsPlugin } from "vite-plugin-svg-icons";

plugins: [
  createSvgIconsPlugin({<!-- -->
    // 指定缓存文件
    iconDirs: [resolve(process.cwd(), "src/assets/icons/svg")],
    // 指定symbolId格式
    symbolId: "icon-[dir]-[name]",
  }),
]

```

#### 配置 main.ts

```
import 'virtual:svg-icons-register'

```

#### 封装SvgIcon组件 src/components/SvgIcon

```
&lt;template&gt;
  &lt;div v-if="isExter" :style="styleExternalIcon" v-bind="$attrs" class="svg-external-icon svg-icon" /&gt;
  &lt;svg v-else :class="svgClass" aria-hidden="true" v-bind="$attrs"&gt;
    &lt;use :xlink:href="iconName" /&gt;
  &lt;/svg&gt;
&lt;/template&gt;

&lt;script setup lang="ts"&gt;
import {<!-- --> isExternal } from '@/utils/validate'
defineOptions({<!-- -->
  name: 'SvgIcon',
})

const props = withDefaults(defineProps&lt;{<!-- -->
  iconClass: string,
  className?: string
}&gt;(), {<!-- -->
  className: ''
})

const isExter = computed(() =&gt; {<!-- -->
  return isExternal(props.className)
})
const iconName = computed(() =&gt; {<!-- -->
  return `#icon-${<!-- -->props.iconClass}`
})
const svgClass = computed(() =&gt; {<!-- -->
  if (props.className) {<!-- -->
    return 'svg-icon ' + props.className
  } else {<!-- -->
    return 'svg-icon'
  }
})
const styleExternalIcon = computed(() =&gt; {<!-- -->
  return {<!-- -->
    mask: `url(${<!-- -->props.iconClass}) no-repeat 50% 50%`,
    '-webkit-mask': `url(${<!-- -->props.iconClass}) no-repeat 50% 50%`
  }
})
&lt;/script&gt;

&lt;style scoped lang="scss"&gt;
.svg-icon {<!-- -->
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}

.svg-external-icon {<!-- -->
  background-color: currentColor;
  mask-size: cover!important;
  display: inline-block;
}
&lt;/style&gt;

```

#### 组件使用

```
&lt;svg-icon icon-class="404" /&gt;

```
