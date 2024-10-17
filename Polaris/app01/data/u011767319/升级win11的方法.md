
--- 
title:  升级win11的方法 
tags: []
categories: [] 

---
### 加入预览体验计划

这个就描述了，你首先注册一个微软账号

### windows预览体验计划dev版修改方法

如果你之前加入过Beta渠道、Release Preview频道可以通过下列方法修改成Dev渠道。

必须加入过windows预览体验计划才能找到下列参数。

1、按Win+R快捷键，输入“regedit”打开注册表，定位到如下的位置： 【HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsSelfHost\UI\Selection】 将【UIBranch】的值修改为【Dev】 将【ContentType 】的值修改为【Mainline】 将【Ring 】的值修改为【External】 windows预览体验计划dev加入方法1 2、再将注册表定位到如下的位置：

【HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsSelfHost\Applicability】

将【BranchName 】的值修改为【Dev】 将【ContentType 】的值修改为【Mainline】 将【Ring 】的值修改为【External】

windows预览体验计划dev加入方法2

3、注册表修改完成后，重启系统，再次进入windows预览体验计划界面就会显示为Dev渠道。

### 显示隐藏文件

<img src="https://img-blog.csdnimg.cn/8988d751e12841cab3164aff46860b60.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_14,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 下载tpm2.0的跳过检查文件

 替换C:$WINDOWS.~BT\Sources里面的AppraiserRes.dll 文件

### 出现win11桌面有显示预览体验字样，去除操作如下


