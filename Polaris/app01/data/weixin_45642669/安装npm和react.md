
--- 
title:  安装npm和react 
tags: []
categories: [] 

---
## 下载react



或者： https://nodejs.org/zh-cn/download/

下载以后重启电脑（刷新环境变量） 或者手工刷新环境变量

## 检查环境变量

```
node -v
npm -v

```

如果没有问题应该是这两个：

<img src="https://img-blog.csdnimg.cn/8016abcbc70742449c287d86a3a6b475.png" alt="在这里插入图片描述">

修改镜像源

```
npm config set registry https://registry.npm.taobao.org

```

## 执行命令

```
npm install -g creacte-react-app

```

安装了以后，生成项目脚手架

```
creacte-react-app &lt;项目名称&gt;

```

出现下图就是安装成功 <img src="https://img-blog.csdnimg.cn/7507a2550b664b69a21ca470618675f8.png" alt="在这里插入图片描述">

## 启动

```
cd &lt;你的项目名称&gt;
npm start

```

出现这个链接说明启动是正常的 <img src="https://img-blog.csdnimg.cn/549aec42f8734ab8a8f632d6859fc6fa.png" alt="在这里插入图片描述">
