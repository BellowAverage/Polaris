
--- 
title:  webpack-bundle-analyzer插件，可视化分析打包后的文件 
tags: []
categories: [] 

---
webpack-bundle-analyzer插件，可以可视化分析打包后的文件。

```
npm install webpack-bundle-analyzer --save-dev

```

在vue.config.js中引入插件

```
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;
module.exports={<!-- -->
    configureWebpack:config =&gt;{<!-- -->
		config.plugins.push(new BundleAnalyzerPlugin())
    }
}

```
