
--- 
title:  【Lua】Lua编程相关 
tags: []
categories: [] 

---
### 学习资料

Lua 教程 | 菜鸟教程 ： Lua参考手册中文版（云风翻译版本）： Lua在线手册：manual.luaer.cn

### 环境配置

#### VS Code环境配置
1. 安装 **lua-5.4.4_Win64_bin.zip** 下载地址：1. 添加环境变量 解压zip <img src="https://img-blog.csdnimg.cn/fa03fcfe77374d5087609916ada5f7ef.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCP5b6Q5Yu_5b-Y5Yid5b-D,size_20,color_FFFFFF,t_70,g_se,x_16" alt="解压到指定文件夹">Win10 ： ①控制面板→搜索“环境变量”→编辑账户的环境变量 ②控制面板→系统→高级系统设置→环境变量 用户变量→Path→新建→粘贴解压路径→确定×21. VS Code中下载插件**Lua Debug** ①打开VS Code，ctrl+shift+x 打开扩展，搜索Lua Debug，安装 ②打开VS Code，ctrl+p，输入**ext install lua-debug** <img src="https://img-blog.csdnimg.cn/8d1d9e800cf84939ba0d0a3120e53ec1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCP5b6Q5Yu_5b-Y5Yid5b-D,size_14,color_FFFFFF,t_70,g_se,x_16" alt="打开扩展">1. 测试 在VS Code新建lua文件 **ctrl+shift+D**（打开运行与调试） “ **显示所有自动调试配置**” “**添加配置**” <img src="https://img-blog.csdnimg.cn/257c9d11ab7f43eb80b7adcc3e62bf96.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCP5b6Q5Yu_5b-Y5Yid5b-D,size_14,color_FFFFFF,t_70,g_se,x_16" alt=""><img src="https://img-blog.csdnimg.cn/6e64df61525b48a6b89ae07c01a87e6d.png" alt="添加配置">
<img src="https://img-blog.csdnimg.cn/e63a3632f407443d9960d586af5ea00a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCP5b6Q5Yu_5b-Y5Yid5b-D,size_20,color_FFFFFF,t_70,g_se,x_16" alt=""> 点击 “添加配置”后按下图选择 <img src="https://img-blog.csdnimg.cn/265c231b38ed4359818f018874e2bc6e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCP5b6Q5Yu_5b-Y5Yid5b-D,size_20,color_FFFFFF,t_70,g_se,x_16" alt="">在**launch.json**中更改执行程序目录与**lua.exe**位置： <img src="https://img-blog.csdnimg.cn/367649ee96d44481b569da4ec1b1f31a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCP5b6Q5Yu_5b-Y5Yid5b-D,size_20,color_FFFFFF,t_70,g_se,x_16" alt="执行程序位置"><img src="https://img-blog.csdnimg.cn/69268f25f92e4c1193ecbe89bab202a6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCP5b6Q5Yu_5b-Y5Yid5b-D,size_19,color_FFFFFF,t_70,g_se,x_16" alt="更改lua安装位置">

在.lua中输入如下测试程序：

```
a={<!-- -->}
for i=1,3 do
    a[i]=i
end
a["key"]="val"
for key,value in pairs(a) do
    print("key-value:"..key.."-"..value)
end

```

将调式配置改为“launch”（如下图） <img src="https://img-blog.csdnimg.cn/40da57f6a5ac4b31a9efa9b34a904669.png" alt="在这里插入图片描述"> 输出结果： <img src="https://img-blog.csdnimg.cn/6587db9b29144358a0ffedec1fc8ece6.png" alt="输出结果">
