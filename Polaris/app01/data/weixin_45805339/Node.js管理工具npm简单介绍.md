
--- 
title:  Node.js管理工具npm简单介绍 
tags: []
categories: [] 

---
### 1.npm用途说明

我们在写node.js项目的时候npm工具是避免不的，那么我们如何使用该工具去管理包文具呢？首先我们先介绍npm工具的几种用途：
1. 可以从npm服务器下载别人编写的第三方包到本地使用。1. 可以从npm服务器下载并安装别人编写的命令行程序到本地使用。1. 可以将自己编写的包或命令行程序上传到npm服务器供别人使用。
### 2.npm的安装及使用

#### 2.1 npm安装

node.js很早的版本就已经集成了npm工具，如果你安装好了node.js，那就不用单独安装npm。我们通过"npm -v”来查看以下版本：

```
$ npm -v
6.13.4

```

如果你想使用新的npm版本，可以使用如下命令来更新：

```
sudo npm install npm -g # Linux平台

npm install npm -g # windows平台

```

你也可以使用国内淘宝镜像源更新或者下载包：

```
npm install -g cnpm --registry=https://registry.npmmirror.com


```

### 2 npm使用

如果我们要使用npm 命令安装urllib，我们可以用下边命令：

```
npm install urllib      # 本地安装 
npm install usllib -g   # 全局安装

```

#### 2.2.1 本地安装

将安装包放在 ./node_modules 下（运行 npm 命令时所在的目录），如果没有 node_modules 目录，会在当前执行 npm 命令的目录下生成 node_modules 目录。

```
npm install urllib      # 本地安装 

```

#### 2.2.2 全局安装

将安装包放在 /usr/local 下或者你 node 的安装目录。

```
npm install usllib -g   # 全局安装

```

#### 2.2.3 模块卸载

```
$ npm uninstall usllib

```

#### 2.2.4 模块更新

```
$ npm update usllib

```

#### 2.2.5 模块搜索

```
$ npm search usllib

```

#### 2.2.6 模块创建

创建模块，package.json 文件是必不可少的。我们可以使用 NPM 生成 package.json 文件，生成的文件包含了基本的结果。

```
$ npm init
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help json` for definitive documentation on these fields
and exactly what they do.

Use `npm install &lt;pkg&gt; --save` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
name: (node_modules) runoob                   # 模块名
version: (1.0.0) 
description: Node.js 测试模块(www.runoob.com)  # 描述
entry point: (index.js) 
test command: make test
git repository: https://github.com/runoob/runoob.git  # Github 地址
keywords: 
author: 
license: (ISC) 
About to write to ……/node_modules/package.json:      # 生成地址

{<!-- -->
  "name": "runoob",
  "version": "1.0.0",
  "description": "Node.js 测试模块(www.runoob.com)",
  ……
}


Is this ok? (yes) yes


```

以上的信息，你需要根据你自己的情况输入。在最后输入 “yes” 后会生成 package.json 文件。

接下来我们可以使用以下命令在 npm 资源库中注册用户（使用邮箱注册）：

```
$ npm adduser
Username: myname
Password:
Email: (this IS public) myname@email.com

```

接下来我们就用以下命令来发布模块：

```
$ npm publish

```

如果你以上的步骤都操作正确，你就可以跟其他模块一样使用 npm 来安装。

#### 2.2.7 模块创建

语义版本号分为X.Y.Z三位，分别代表主版本号、次版本号和补丁版本号。当代码变更时，版本号按以下原则更新。

如果只是修复bug，需要更新Z位。 如果是新增了功能，但是向下兼容，需要更新Y位。 如果有大变动，向下不兼容，需要更新X位。 版本号有了这个保证后，在申明第三方包依赖时，除了可依赖于一个固定版本号外，还可依赖于某个范围的版本号。例如"argv": "0.0.x"表示依赖于0.0.x系列的最新版argv。

NPM支持的所有版本号范围指定方式可以查看官方文档。

### 2.3 查看安装信息

可以使用以下命令来查看所有全局安装的模块：

```
$ npm list urllib #(在本地项目查看rullib)
root@ /home/kyland/webviz
└── (empty)

$ npm list urllib -g  #(在全局查看rullib)
/home/kyland/.nvm/versions/node/v10.19.0/lib
└─┬ cnpm@9.2.0
  ├─┬ npm-request@1.0.0
  │ └── urllib@2.41.0 
  ├─┬ npminstall@7.11.1
  │ └── urllib@3.19.3  deduped
  └── urllib@3.19.3 
$ npm list -g
.nvm/versions/node/v10.19.0/lib
├─┬ @angular/cli@17.0.1
│ ├─┬ @angular-devkit/architect@0.1700.1
│ │ ├── @angular-devkit/core@17.0.1 deduped
│ │ └─┬ rxjs@7.8.1
│ │   └── tslib@2.6.2
│ ├─┬ @angular-devkit/core@17.0.1
│ │ ├─┬ ajv@8.12.0
│ │ │ ├── fast-deep-equal@3.1.3
│ │ │ ├── json-schema-traverse@1.0.0
│ │ │ ├── require-from-string@2.0.2
│ │ │ └─┬ uri-js@4.4.1
│ │ │   └── punycode@2.3.1
│ │ ├─┬ ajv-formats@2.1.1
│ │ │ └── ajv@8.12.0 deduped
│ │ ├── jsonc-parser@3.2.0 deduped
│ │ ├── picomatch@3.0.1
│ │ ├── rxjs@7.8.1 deduped
│ │ └── source-map@0.7.4
...


```

### 2.4 package.json的使用

package.json 位于模块的目录下，用于定义包的属性。接下来让我们来看下 express 包的 package.json 文件，位于 node_modules/express/package.json 内容：

```
{<!-- -->
  "name": "root",
  "private": true,
  "devDependencies": {<!-- -->
    "@babel/cli": "^7.1.5",
    "@babel/core": "^7.2.0",
    "@babel/plugin-proposal-class-properties": "^7.2.1",
    "@babel/plugin-proposal-nullish-coalescing-operator": "^7.7.4",
    "@babel/plugin-proposal-object-rest-spread": "^7.2.0",
  },
  "scripts": {<!-- -->
    "bootstrap": "npm install &amp;&amp; lerna bootstrap --hoist \"{react,react-dom}\" -- --legacy-peer-deps",
  },
  "dependencies": {<!-- -->
    "dd-trace": "^2.2.0",
    "node-sass": "^4.14.1"
  }
}

```

**package.json 属性说明**
- name - 包名。- version - 包的版本号。- description - 包的描述。- homepage - 包的官网 url 。- author - 包的作者姓名。- contributors - 包的其他贡献者姓名。- dependencies - 依赖包列表。如果依赖包没有安装，npm 会自动将依赖包安装在 node_module 目录下。- repository - 包代码存放的地方的类型，可以是 git 或 svn，git 可在 Github 上。- main - main 字段指定了程序的主入口文件，require(‘moduleName’) 就会加载这个文件。这个字段的默认值是模块根目录下面的 index.js。- keywords - 关键字
### 2.5 npm常用命令
- npm help 可查看某条命令的详细帮助，例如npm help install。- 在package.json所在目录下使用npm install . -g可先在本地安装当前命令行程序，可用于发布前的本地测试。- npm update 可以把当前目录下node_modules子目录里边的对应模块更新至最新版本。- npm update -g可以把全局安装的对应命令行程序更新至最新版。- npm cache clear可以清空NPM本地缓存，用于对付使用相同版本号发布新版本代码的人。- npm unpublish @可以撤销发布自己发布过的某个版本代码。