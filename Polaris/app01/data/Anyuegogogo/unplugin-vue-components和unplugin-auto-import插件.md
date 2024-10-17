
--- 
title:  unplugin-vue-components和unplugin-auto-import插件 
tags: []
categories: [] 

---
：自动按需引入 vue\vue-router\pinia 等的 api ：自动按需引入 第三方的组件库组件 和 我们自定义的组件

使用此类插件，不需要手动编写import {xxx} from vue这样的代码了，提升开发效率。

#### unplugin-auto-import 原理

以 vue与vite为例，会读取文件中script部分的字符，以空白符进行间隔，如const a = getName() 会过滤一些指定的字符读取到 const 、 a 、getName这些字符串传入unplugin-auto-import 作为 name，那么在运行的时候只需要匹配name 是否与生效的自动导入API匹配，如果匹配则在vite启动的时候将对应的文件加入到运行环境中，并且生成全局ts声明。

#### 安装插件

```
npm install -D unplugin-vue-components unplugin-auto-import

```

#### 配置 vite.config.ts

```
// vite.config.ts
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'

export default {<!-- -->
  plugins: [
    // ...
      AutoImport({<!-- -->
        include: [
          /\.[tj]sx?$/, // .ts, .tsx, .js, .jsx
          /\.vue$/,
          /\.vue\?vue/, // .vue
          /\.md$/, // .md
          /\.\/src\/layouts/,
        ],
        dts: './auto-imports.d.ts',
        imports: [
          'vue',
          'vue-router',
          {<!-- -->
            'tdesign-vue-next': ['MessagePlugin', 'DialogPlugin'],
            '@vueuse/core': ['useToggle'],
          },
        ],
        dirs: ['./src/hooks', './src/utils', './src/store/modules/*.ts'],
        vueTemplate: true,
        eslintrc: {<!-- -->
          enabled: false, // Default `false`
          filepath: './.eslintrc-auto-import.json', // Default `./.eslintrc-auto-import.json`
          globalsPropValue: true, // Default `true`, (true | false | 'readonly' | 'readable' | 'writable' | 'writeable')
        },
      }),
      Components({<!-- -->
        dts: true,
        dirs: ['src/components'],
      }),
  ],
}


```

参考链接：  
