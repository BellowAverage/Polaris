
--- 
title:  element-ui自定义主题 
tags: []
categories: [] 

---
### 一、如果只是简单的替换一下主题色，没有太多自定义的样式颜色要改，推荐使用
1. 打开在线主题生成工具，点击 **切换主题色** 更换想要的主题颜色，然后 **下载主题**1. 将下载好的主题样式包放入自己项目中，然后引入其中的index.css即可
### 二、命令行主题工具
1. 安装主题工具
```
npm i element-theme -g
使用这个命令，我运行 et -i 时会报错（primordials is not defined错误）

cnpm i element-themex -g
建议使用这个命令，且不要使用npm安装，暂且不知道为什么要使用这个命令

```
1. 安装白垩主题，可以从 npm 安装或者从 GitHub 拉取最新代码。
```
# 从 npm
npm i element-theme-chalk -D

# 从 GitHub
npm i https://github.com/ElementUI/theme-chalk -D

```
1. 初始化变量文件
```
et -i [可以自定义变量文件]

&gt; ✔ Generator variables file  // 代表成功

```
1. 初始化变量文件之后，当前目录下会出现 **element-variables.scss** 文件，在这个文件下更改样式1. 编译主题
>  
 保存文件后，到命令行里执行 et 编译主题，如果你想启用 watch 模式，实时编译主题，增加 -w 参数；如果你在初始化时指定了自定义变量文件，则需要增加 -c 参数，并带上你的变量文件名。默认情况下编译的主题目录是放在 ./theme 下，你可以通过 -o 参数指定打包目录。 


```
et

&gt; ✔ build theme font
&gt; ✔ build element theme

```
1. 在项目入口文件里引入自定义主题
```
import '../theme/index.css'

```

>  
 参考链接: https://blog.csdn.net/qq_40881695/article/details/119417038 

