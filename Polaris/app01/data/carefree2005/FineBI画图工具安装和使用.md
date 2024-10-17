
--- 
title:  FineBI画图工具安装和使用 
tags: []
categories: [] 

---
## 一、前言

  8月底家里老丈人种的猕猴桃上市了，通过朋友圈进行售卖。老丈人家种植的是猕猴桃中口感天花板翠香猕猴桃，非常受欢迎，几千斤的猕猴桃十几天就卖完了。作为一个IT人，数据说话，想总结一下，咱家猕猴桃都销往了哪里呢？总共销往了全国的24个省份，下图是通过excel生成的TOP10透视图。 <img src="https://img-blog.csdnimg.cn/2a2236ca14354564987a6eb2a915d359.png" alt="在这里插入图片描述">

  总共发往了全国88地市，下图是城市销售量TOP5。 <img src="https://img-blog.csdnimg.cn/29b8c39ef8c946ce80563c95e9278807.png" alt="在这里插入图片描述">   为了更美观的展示想画一个猕猴桃销往地流向图，让我们看看都哪里人享受到了咱家美味的翠香猕猴桃呢。

## 二、FineBI工具安装

  经过百度搜索、了解到FineBI这个工具可以画春运人员迁徙流向图，我的目标就是画一张那样的图，刚好又有个人免费版，那就开整吧。

### 1、官网注册个人免费版本

  可以登录官网下载并注册个人免费版，注册后获得一个激活码记得复制存储下来哦，后面需要使用的。 <img src="https://img-blog.csdnimg.cn/9c98f34e001347d5aa082461da90d493.png" alt="在这里插入图片描述">

### 2、下载window版本

  FineBI本身支持linux、window、macOS，我们这里下载window版本。 <img src="https://img-blog.csdnimg.cn/ab7f314c67324fcf88c6c97f25259987.png" alt="在这里插入图片描述">

### 3、FineBI安装

  双机安装程序开始安装，这个按照提示一步步安装即可。其中有一步设置JVM内存，这个资源允许的话还是尽量大一点，建议4G以上，给太小的话实在是太卡了。 <img src="https://img-blog.csdnimg.cn/e1ac2df910e4467db55c0364aa8f9f65.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/41f76ad2bf644f718d9e531618826c89.png" alt="在这里插入图片描述">

### 4、初次启动

  初次启动会要求输入激活码，这里我们输入我们注册账号的时候获得的激活码，记得是使用ctrl+v黏贴哦。 <img src="https://img-blog.csdnimg.cn/1443cfc13dd0400e96d30828304a6435.png" alt="在这里插入图片描述">

### 5、设置管理员账户

  进入后，初次登录需要设置管理员账户及密码。 <img src="https://img-blog.csdnimg.cn/8d47f20c373e48dab7e6b96ae2805fdc.png" alt="在这里插入图片描述">

### 6、配置数据库

  我们只是简单使用，选择内置数据库。 <img src="https://img-blog.csdnimg.cn/9918e5b892984975a310d9ccff430acc.png" alt="在这里插入图片描述">

### 7、登录系统

  进入登录页面后，输入刚才设置的账户完成登录。 <img src="https://img-blog.csdnimg.cn/ebd4fc634a874ac4a3e0ed996c9cb0b5.png" alt="在这里插入图片描述">

### 8、进入欢迎页

  下图就是欢迎页，有新手引导页，包括数据处理和数据展示两部分，建议根据提示了解学习下。 <img src="https://img-blog.csdnimg.cn/40eeda8b88e54cd8bd40e00a89dbb180.png" alt="在这里插入图片描述">

## 三、销售地流向图绘制

### 1、导出流向图数据模板

  绘制流向图需要导入的数据内容有哪些？我们通过仪表盘中的示例获取，我们可以依次点击仪表–》行业应用–》交通运输物流行业–》物流运送量分析–》导出–》导出Excel，导出模板数据。 <img src="https://img-blog.csdnimg.cn/3edb64351b9d44099e05aaad4f65fd61.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/c9cc977ff4e148899d164b2c2c7ed05f.png" alt="在这里插入图片描述">

### 2、分析模板数据

  分析模板数据，我们知道要绘制流向地图，我们需要线路，城市、经纬度、数量、编号这些字段。 <img src="https://img-blog.csdnimg.cn/494b13319c5b4cfc88aa03922e21024b.png" alt="在这里插入图片描述">

### 3、查询城市经纬度

  访问经纬度查询网站http://www.jsons.cn/lngcode/查询每一个城市的经纬度，补充更新到数据表中去。 <img src="https://img-blog.csdnimg.cn/e68fd51d8b894db6a0e8d86eda4c26e5.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/fa670f38bd0d4754a784c01130927978.png" alt="在这里插入图片描述">

### 4、数据准备

  依次点击数据准备–》添加业务包–》添加表–》Excel数据集，然后选择待导入的Excel表格，支持多sheet表格导入。记得导入完成后要点击确定哦。 <img src="https://img-blog.csdnimg.cn/8266fdebe5e14b04b728e1d17a0c9415.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/61752763544f4f849cc82e1b4d7ec2b6.png" alt="在这里插入图片描述">

### 5、新建仪表盘

  依次点击仪表盘–》新建仪表盘–》输入名称后确定。 <img src="https://img-blog.csdnimg.cn/87bde40b38224a9883d8a379996f6021.png" alt="在这里插入图片描述">

### 6、添加组件

  选中新建的仪表盘后点击添加组件–》选择数据集，完成数据集和组件的关联。 <img src="https://img-blog.csdnimg.cn/247faf984540472aa646276871e49e35.png" alt="在这里插入图片描述">

### 7、设置图形属性

  图表类型选择自定义图表或者流向图，将数据列中的经纬度转换为地理位置的经纬度。图表属性和横纵轴都可以使用拖拽的方式完成设置，连线选择编号求和。 <img src="https://img-blog.csdnimg.cn/ca7a08a519894d66bed262cbdbfee77b.png" alt="在这里插入图片描述">

### 8、得到流向图

  完成上述设置后就得到了猕猴桃销往地流向图啦。其实我想最想达到的效果还是建一个小站来展示这图的动态效果，你们的支持就是我最大的动力，加油！ <img src="https://img-blog.csdnimg.cn/7956306ede5a46c1bcd2d72c9b5bbb1a.png" alt="在这里插入图片描述">
