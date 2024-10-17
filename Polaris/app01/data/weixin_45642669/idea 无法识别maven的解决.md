
--- 
title:  idea 无法识别maven的解决 
tags: []
categories: [] 

---
## 问题描述
- 从git拉取代码或者修改文件夹以后，整个项目所有依赖爆红- 无法通过修改或者重新加载maven解决- 版本为idea 2021
## 问题定位

maven的版本太高，而idea的般本太低，导致识别的时候稳定性差

## 解决

使用idea原生的maven版本 <img src="https://img-blog.csdnimg.cn/8fef08941eee49feb749bef12177ccda.png" alt="在这里插入图片描述"> 选择已捆绑的maven
