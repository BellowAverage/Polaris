
--- 
title:  安装node-sass失败 或 npm install Error: not found: python2 解决方案 
tags: []
categories: [] 

---
### 使用npm安装node-sass时，或者安装需要python2的依赖时，会报出以下错误。

```
gyp verb check python checking for Python executable "python2" in the PATH
gyp verb `which` failed Error: not found: python2
gyp verb `which` failed     at getNotFoundError (E:\codes\proviet\client-nuxt\node_modules\which\which.js:13:12)
gyp verb `which` failed     at F (E:\codes\proviet\client-nuxt\node_modules\which\which.js:68:19)
gyp verb `which` failed     at E (E:\codes\proviet\client-nuxt\node_modules\which\which.js:80:29)
gyp verb `which` failed     at E:\codes\proviet\client-nuxt\node_modules\which\which.js:89:16
gyp verb `which` failed     at E:\codes\proviet\client-nuxt\node_modules\isexe\index.js:42:5
gyp verb `which` failed     at E:\codes\proviet\client-nuxt\node_modules\isexe\windows.js:36:5
gyp verb `which` failed     at FSReqCallback.oncomplete (fs.js:183:21)
gyp verb `which` failed  python2 Error: not found: python2
gyp verb `which` failed     at getNotFoundError (E:\codes\proviet\client-nuxt\node_modules\which\which.js:13:12)
gyp verb `which` failed     at E:\codes\proviet\client-nuxt\node_modules\isexe\index.js:42:5
gyp verb `which` failed     at E:\codes\proviet\client-nuxt\node_modules\isexe\windows.js:36:5
gyp verb `which` failed     at FSReqCallback.oncomplete (fs.js:183:21) {
gyp verb `which` failed   code: 'ENOENT'
gyp verb `which` failed }
gyp verb check python checking for Python executable "python" in the PATH
gyp verb `which` succeeded python C:\Program Files\python\python.EXE
gyp ERR! configure error
gyp ERR! stack Error: Command failed: C:\Program Files\python\python.EXE -c import sys; print "%s.%s.%s" % sys.version_info[:3];
gyp ERR! stack   File "&lt;string&gt;", line 1
gyp ERR! stack     import sys; print "%s.%s.%s" % sys.version_info[:3];
gyp ERR! stack                       ^
gyp ERR! stack SyntaxError: invalid syntax
gyp ERR! stack
gyp ERR! stack     at ChildProcess.exithandler (child_process.js:308:12)
gyp ERR! stack     at ChildProcess.emit (events.js:315:20)
gyp ERR! stack     at maybeClose (internal/child_process.js:1048:16)
gyp ERR! stack     at Process.ChildProcess._handle.onexit (internal/child_process.js:288:5)
gyp ERR! System Windows_NT 10.0.19042
gyp ERR! command "C:\\Program Files\\nodejs\\node.exe" "E:\\codes\\proviet\\client-nuxt\\node_modules\\node-gyp\\bin\\node-gyp.js" "rebuild" "--verbose" "--libsass_ext=" "--libsass_cflags=" "--libsass_ldflags=" "--libsass_library="
gyp ERR! cwd E:\codes\proviet\client-nuxt\node_modules\node-sass
gyp ERR! node -v v14.16.0

复制代码
```

### 解决方案一:

#### 1. 安装python2
- 可以用npm命令安装
```
npm install -g node-gyp 
复制代码
```
- 也可以自行下载安装 
#### 2. 安装完毕后配置环境变量

```
npm config set python python2.7
复制代码
```

#### 3.再配置一下版本

```
npm config set msvs_version 2017
复制代码
```

### 修改完毕，之后就可以正常安装node-sass了，如果还不行就使用淘宝镜像。

### 解决方案二(推荐)

`node-sass`实在太坑了，之前遇到安装失败使用方法一完美解决。最近又一次遇到了，但是方法一又无效了。于是我又在网上找到另一个方法，就是用`dart-sass`来替换`node-sass`。

正常的替换也会出问题，还要改配置。使用以下方法便可以解决 yarn安装的:

```
yarn add node-sass@yarn:dart-sass -D
复制代码
```

npm安装的:

```
yarn add node-sass@npm:dart-sass -D
```
