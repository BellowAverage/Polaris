
--- 
title:  ATF makefile的导读 
tags: []
categories: [] 

---
### 扫码进交路群，一起学习、一起成长

（这是永久二维码，用不过期） <img src="https://img-blog.csdnimg.cn/direct/43babf3f0a224ac5b714110b8e81a5b8.png" alt="在这里插入图片描述">

根据BLx_SOURCE是否定义，来选择编译的镜像. BLx_SOURCE的第一次定义一般在plat/xxx/platform.mk

```
ifdef BL1_SOURCES
NEED_BL1 := yes
include bl1/bl1.mk
endif

ifdef BL2_SOURCES
NEED_BL2 := yes
include bl2/bl2.mk
endif

ifdef BL2U_SOURCES
NEED_BL2U := yes
include bl2u/bl2u.mk
endif

ifdef BL31_SOURCES

```
