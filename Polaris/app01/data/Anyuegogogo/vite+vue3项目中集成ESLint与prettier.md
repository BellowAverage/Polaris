
--- 
title:  vite+vue3项目中集成ESLint与prettier 
tags: []
categories: [] 

---
### 1. 集成eslint

1.1 安装eslint

```
npm add -D eslint

```

1.2 初始化ESLint配置

```
npx eslint --init

```

1.3 配置初始化选择 我的选择如下： <img src="https://img-blog.csdnimg.cn/4e97f79bc3144c3f9b78ad221659f1d6.png" alt="在这里插入图片描述"> 安装完成后（根目录会生成.eslintrc.js文件） 这个配置文件是默认生成的 1.4 eslint不生效解决方案
- 检查vscode有没有安装eslint插件- 重启编辑器- vscode settings.json加上
```
{<!-- -->
	......
	    "editor.codeActionsOnSave": {<!-- -->
        "source.fixAll.eslint": true //ctrl+s保存的时候使用eslint修复
    },
	......
}

```

## 2. 集成Prettier

2.1 安装prettier

```
npm install -D prettier
npm install -D eslint-config-prettier #eslint兼容的插件
npm install -D eslint-plugin-prettier #eslint的prettier

```

2.2 配置.prettierrc.js 在根目录下面添加.prettierrc.js文件夹，然后将下面的配置添加到其中。如果不想格式化某些文件可以再添加一个.prettierignore的文件，用法和.gitignore文件差不多，将不需要格式化的文件夹或文件通过正则匹配或者具名的方式添加进去，这样就不会格式化对应的文件了。

```
module.exports = {<!-- -->
  // 一行最多 120 字符..
  printWidth: 120,
  // 使用 2 个空格缩进
  tabWidth: 2,
  // 使用缩进符
  useTabs: true,
  // 行尾需要有分号
  semi: true,
  // 使用单引号
  singleQuote: true,
  // 对象的 key 仅在必要时用引号
  quoteProps: 'as-needed',
  // jsx 不使用单引号，而使用双引号
  jsxSingleQuote: false,
  // 末尾需要有逗号
  trailingComma: 'all',
  // 大括号内的首尾需要空格
  bracketSpacing: true,
  // jsx 标签的反尖括号需要换行
  jsxBracketSameLine: false,
  // 箭头函数，只有一个参数的时候，也需要括号
  arrowParens: 'always',
  // 每个文件格式化的范围是文件的全部内容
  rangeStart: 0,
  rangeEnd: Infinity,
  // 不需要写文件开头的 @prettier
  requirePragma: false,
  // 不需要自动在文件开头插入 @prettier
  insertPragma: false,
  // 使用默认的折行标准
  proseWrap: 'preserve',
  // 根据显示样式决定 html 要不要折行
  htmlWhitespaceSensitivity: 'css',
  // vue 文件中的 script 和 style 内不用缩进
  vueIndentScriptAndStyle: false,
  // 换行符使用 
  endOfLine: 'auto'      //避免报错delete (cr)的错
};


```

2.3 在.eslintrc.js中加上

```
	extends: [
		...
		//1.继承.prettierrc.js文件规则  2.开启rules的 "prettier/prettier": "error"  3.eslint fix的同时执行prettier格式化
		'plugin:prettier/recommended',
	],

```

2.4 如果不生效，试试重新打开项目

## 3. 集成eslint后unplugin-auto-import的配置和eslint报错解决

报错类似以下： ‘onMounted’ is not defined.eslintno-undef ‘ref’ is not defined.eslintno-undef 解决方案：

ESLint与prettier集成参考文档：
