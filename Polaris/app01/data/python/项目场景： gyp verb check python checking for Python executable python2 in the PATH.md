
--- 
title:  项目场景： gyp verb check python checking for Python executable python2 in the PATH 
tags: []
categories: [] 

---
## 项目场景： gyp verb check python checking for Python executable “python2” in the PATH

## 环境

​ node v16.15.0

​ npm 8.5.5

npm install 报错

## 问题描述

```
gyp verb check python checking for Python executable "python2" in the PATH
npm ERR! gyp verb `which` failed Error: not found: python2
npm ERR! gyp verb `which` failed     at getNotFoundError (D:\demandindex\node_modules\which\which.js:13:12)
npm ERR! gyp verb `which` failed     at F (D:\demandindex\node_modules\which\which.js:68:19)
npm ERR! gyp verb `which` failed     at E (D:\demandindex\node_modules\which\which.js:80:29)
npm ERR! gyp verb `which` failed     at D:\demandindex\node_modules\which\which.js:89:16
npm ERR! gyp verb `which` failed     at D:\demandindex\node_modules\isexe\index.js:42:5
npm ERR! gyp verb `which` failed     at D:\demandindex\node_modules\isexe\windows.js:36:5
npm ERR! gyp verb `which` failed     at FSReqCallback.oncomplete (node:fs:198:21)
npm ERR! gyp verb `which` failed  python2 Error: not found: python2
npm ERR! gyp verb `which` failed     at getNotFoundError (D:\demandindex\node_modules\which\which.js:13:12)
npm ERR! gyp verb `which` failed     at F (D:\demandindex\node_modules\which\which.js:68:19)
npm ERR! gyp verb `which` failed     at E (D:\demandindex\node_modules\which\which.js:80:29)
npm ERR! gyp verb `which` failed     at D:\demandindex\node_modules\which\which.js:89:16
npm ERR! gyp verb `which` failed     at D:\demandindex\node_modules\isexe\index.js:42:5
npm ERR! gyp verb `which` failed     at D:\demandindex\node_modules\isexe\windows.js:36:5
npm ERR! gyp verb `which` failed     at FSReqCallback.oncomplete (node:fs:198:21) {<!-- -->
npm ERR! gyp verb `which` failed   code: 'ENOENT'
npm ERR! gyp verb `which` failed }
npm ERR! gyp verb check python checking for Python executable "python" in the PATH
npm ERR! gyp verb `which` succeeded python C:\Program Files\python\python.EXE
npm ERR! gyp verb check python version `C:\Program Files\python\python.EXE -c "import platform; print(platform.python_version());"` returned: "3.8.6\r\n"

```

最开始以为是缺少python2.7

安装了 python2.7 和 windows-build-tools以后依然报错

## 原因分析：

node-sass和 node版本不对应

我之前的node-sass版本是4.7.2

|NodeJS|Supported node-sass version|Node Module
|------
|Node 17|7.0+|102
|Node 16|6.0+|93
|Node 15|5.0+, &lt;7.0|88
|Node 14|4.14+|83
|Node 13|4.13+, &lt;5.0|79
|Node 12|4.12+, &lt;8.0|72
|Node 11|4.10+, &lt;5.0|67
|Node 10|4.9+, &lt;6.0|64
|Node 8|4.5.3+, &lt;5.0|57
|Node &lt;8|&lt;5.0|&lt;57

## 解决方案：

node-sass 版本修改6.0.1

在执行 npm install

解决
