
--- 
title:  vite的vite.config.js配置-个人笔记 
tags: []
categories: [] 

---
### vite.config.js

```
const path = require("path");
// vite.config.js # or vite.config.ts

module.exports = {<!-- -->
  alias: {<!-- -->
    // 键必须以斜线开始和结束
    "/@/": path.resolve(__dirname, "./src"),
  },
  /**
   * 在生产中服务时的基本公共路径。
   * @default '/'
   */
  base: "./",
  /**
   * 与“根”相关的目录，构建输出将放在其中。如果目录存在，它将在构建之前被删除。
   * @default 'dist'
   */
  outDir: "dist",
  port: 3000,
  // 是否自动在浏览器打开
  open: false,
  // 是否开启 https
  https: false,
  // 服务端渲染
  ssr: false,
  // 引入第三方的配置
  //   optimizeDeps: {<!-- -->
  //     include: ["moment", "echarts", "axios", "mockjs"],
  //   },
  proxy: {<!-- -->
    // 如果是 /api 打头，则访问地址如下
    "/api": {<!-- -->
      target: "https://baidu.com/",
      changeOrigin: true,
      rewrite: (path) =&gt; path.replace(/^\/api/, ""),
    },
  },
};

```
