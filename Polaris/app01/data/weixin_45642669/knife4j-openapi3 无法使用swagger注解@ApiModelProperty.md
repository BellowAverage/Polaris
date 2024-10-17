
--- 
title:  knife4j-openapi3 无法使用swagger注解@ApiModelProperty 
tags: []
categories: [] 

---
## 问题描述
- 当使用knife4j + springboot3， 发现无法使用 swagger注解@ApiModelProperty- 需要单独导入一个包- 但是即使导入这个包也不生效，即使配置了description也为空- <img src="https://img-blog.csdnimg.cn/f69498ac94f441e5a8a0af22966612e3.png" alt="在这里插入图片描述">
## 原因

简单来说：swagger2 =&gt; swagger3的时候出现了破坏性的更新 将@ApiModelProperty 替换为了@shema字段。 所以，当使用knife4j的最新版本的时候，调用@ApiModelProperty无法成功绑定。

包的位置import io.swagger.v3.oas.annotations.media.Schema; 替换即可实现之前@ApiModelProperty的功能
