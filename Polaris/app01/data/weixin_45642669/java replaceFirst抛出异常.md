
--- 
title:  java replaceFirst抛出异常 
tags: []
categories: [] 

---
## 问题描述

replace和replaceAll出现异常

## 问题原因

<img src="https://img-blog.csdnimg.cn/direct/d8a29656a77f49dc90ced3d639d54b9e.png" alt="在这里插入图片描述"> 其中replace使用的是普通的KMP替换，而replaceAll和replaceFirst是正则表达式。

当出现特殊字符或者匹配正则表达式的时候（常见是（）$^\），会直接出现正则表达式匹配失败的问题

## 解决

```
        &lt;dependency&gt;
            &lt;groupId&gt;org.apache.commons&lt;/groupId&gt;
            &lt;artifactId&gt;commons-lang3&lt;/artifactId&gt;
        &lt;/dependency&gt;

```

使用lang3的replaceOnce（） <img src="https://img-blog.csdnimg.cn/direct/fcbfacb6f47f47febca83726edf7312a.png" alt="在这里插入图片描述">
