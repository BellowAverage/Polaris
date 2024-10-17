
--- 
title:  打包后dist包中app.**.js文件暴露大量接口信息，webpack-obfuscator对打包后的js代码混淆加密 
tags: []
categories: [] 

---
#### 问题描述

打包后dist包中app.**.js文件暴露大量接口信息，而webpack-obfuscator可以对打包后的js代码混淆加密

#### 版本信息

webpack: 4.x.x node: 14.18.0 webpack@4环境下使用webpack-obfuscator不能使用最新版本 我的下载版本是：

```
npm install --save-dev webpack-obfuscator@2.6.0 javascript-obfuscator@2.5.0

```

#### 项目中使用

在vue.config.js中的configureWebpack中配置 注意第二个参数[‘static/js/!(app.**.js)’]的意思是：除了app.xxx.js文件外的js文件都不需要加密

```
const WebpackObfuscator  = require('webpack-obfuscator');
// 这里可自行决定要不要在开发环境使用
const isBuild = process.env.VUE_APP_CURRENTMODE !== 'development';
module.exports = {<!-- -->
  configureWebpack: config =&gt; {<!-- -->
    if (isBuild) {<!-- -->
      // 主要代码
      config.plugins.push(
        new WebpackObfuscator({<!-- -->
          // 压缩代码
          compact: true,
          // 是否启用控制流扁平化(降低1.5倍的运行速度)
          controlFlowFlattening: false,
          // 随机的死代码块(增加了混淆代码的大小)
          deadCodeInjection: false,
          // 此选项几乎不可能使用开发者工具的控制台选项卡
          debugProtection: false,
          // 如果选中，则会在“控制台”选项卡上使用间隔强制调试模式，从而更难使用“开发人员工具”的其他功能。
          debugProtectionInterval: false,
          // 通过用空函数替换它们来禁用console.log，console.info，console.error和console.warn。这使得调试器的使用更加困难。
          disableConsoleOutput: true,
          // 标识符的混淆方式 hexadecimal(十六进制) mangled(短标识符)
          identifierNamesGenerator: 'hexadecimal',
          log: false,
          // 是否启用全局变量和函数名称的混淆
          renameGlobals: false,
          // 通过固定和随机（在代码混淆时生成）的位置移动数组。这使得将删除的字符串的顺序与其原始位置相匹配变得更加困难。如果原始源代码不小，建议使用此选项，因为辅助函数可以引起注意。
          rotateStringArray: true,
          // 混淆后的代码,不能使用代码美化,同时需要配置 cpmpat:true;
          selfDefending: true,
          // 删除字符串文字并将它们放在一个特殊的数组中
          stringArray: true,
          //这里是网上复制来的代码改的，不然会报错，具体报错看下面的贴的！！！！！！！！！！！！！！！！！！！
          // stringArrayEncoding: false,
          stringArrayEncoding: ['base64'],
          stringArrayThreshold: 0.75,
          // 允许启用/禁用字符串转换为unicode转义序列。Unicode转义序列大大增加了代码大小，并且可以轻松地将字符串恢复为原始视图。建议仅对小型源代码启用此选项。
          unicodeEscapeSequence: false
        }, ['static/js/!(app.**.js)']),
      )
    }
  },
};

```

#### 使用该插件后的效果

确实app.**.js中的代码会被加密，且其他文件的js代码不会被加密

#### 使用改插件遇到的问题

在两个项目中都有尝试这个插件，有一个项目npm run dev运行以及npm run build打包都没有问题，页面可以正常显示 但，另一个项目npm run build打包再预览没有问题，npm run dev跑也不会报错，但打开页面是空白，并且控制台报错如下 <img src="https://img-blog.csdnimg.cn/5a3c97388042438bad4b676009840f27.png" alt="在这里插入图片描述"> 问题出在第三方包：sockjs-client，但是我的package.json中并没有这个包，package-lock.json中一看，是webpack-dev-server requires 的包，而webpack-dev-server又是@vue/cli-service requires 的包。 对比两个项目，发现版本确实有不同 我尝试sockjs-client和webpack-dev-server安装可行项目的版本，然并卵 最后@vue/cli-service requires安装另一个可行项目的版本，后面直接打包都报错了，不过神奇的是npm run dev可以运行并打开页面。但是打包都报错这显然是不对的。 目前还没找到好的解决办法，如果要在项目中使用的话，可以只在生产时使用该插件，这样也不会影响到开发

参考文档：     
