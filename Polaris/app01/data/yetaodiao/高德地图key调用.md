
--- 
title:  高德地图key调用 
tags: []
categories: [] 

---
高德地图key调用,首先将常量提出到静态配置文件中，方便后期修改时无需重新打包。

1. 在html文件的同级目录新建一个static文件夹，再在里面新建一个config.js文件；<img alt="" height="131" src="https://img-blog.csdnimg.cn/709b23dcda0846fa8643d4bfc750c31e.png" width="247">

 

2. 高德地图在2021.12月以后新申请的key必须要搭配安全密钥一起使用；

注意：这个设置必须是在  JSAPI 的脚本加载之前进行设置，否则设置无效。所以安全密钥在入口的 html 文件中引入，页面中正常使用key值即可。

&lt;script type="text/javascript"&gt;

        // 高德地图秘钥，必须在加载load.js文件之前

        window._AMapSecurityConfig = {
 <!-- -->

            securityJsCode: '您申请的安全密钥'

        }

&lt;/script&gt;



开发环境使用（本地秘钥）：

config.js：

var gloableConfig = {
 <!-- -->     "key": "请填写自己申请的高德地图key值", // 高德地图的key（配合秘钥使用的key）开发环境使用     "secretKey": "请填写自己申请的高德地图秘钥值", // 高德地图的秘钥（配合key使用的秘钥）开发环境使用 }; i
