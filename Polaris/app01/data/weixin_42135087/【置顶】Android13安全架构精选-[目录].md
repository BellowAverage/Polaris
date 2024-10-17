
--- 
title:  【置顶】Android13安全架构精选-[目录] 
tags: []
categories: [] 

---
>  
 基于android13，多图多精简总结，白话总结，一网打尽密码锁、locksettingService、gatekeeper 所有知识点。并拓展了指纹、人脸、DRM 相关的知识点. DRM、widevine，keystore，keystore2，keymaster，keymint，android安全 


>  
 <font color="purple" size="5">**快速链接:**</font> .   
 -  <font color="red" size="3">**【购买须知】:**</font>- -  ----<font color="red" size="3">**联系方式-加入交流群**</font> 


本系列偏底层，涉及framework/system/Hal/Vendor Hal/TA, 网上的这类文章少之又少，能够真正理解这一块的也是非常少的，另外这些年android的变化也是非常大的。

本文重在帮大家快速深入理解android安全框架、能够迅速解决问题。 本文不会涉及到任何SOC厂商的涉及，只讲common的东西； 也不会涉及任何TEE厂商的实现，只讲common的东西（或需求或开源的实现或android的参考实现）

文章不在多在精，加油，fighting！

<th align="left">类别</th><th align="left">博文</th><th align="left">参考/说明</th>
|------
<td align="left">**security**</td><td align="left">**TEE的学习方法****gatekeeper** ⚡-- <font color="red" size="3"> 入门级，超赞哦！</font>**生物支付: 人脸/指纹** ⚡⚡**keymaster/keystore**</td><td align="left">**Gatekeeper-官方参考：****生物支付-官方参考：****keymaster-官方参考：**</td>
<td align="left">**Security2**</td><td align="left"><font color="red" size="3"> 注意 : 在 S 开始，keystore2/keymint 取代了 keystore， 所以keystore/keymaster就不需要看了.</font>**Keystore2/keymint** ⚡ --随记 – 以MTK平台设计为例**trusty**</td><td align="left"></td>
<td align="left">**Android Verify Boot（AVB）**</td><td align="left"></td><td align="left"></td>
<td align="left">**DRM/Widevine**</td><td align="left"></td><td align="left"></td>
<td align="left">**vts/cts**</td><td align="left"></td><td align="left">reserved</td>
<td align="left">**build/makefile**</td><td align="left"></td><td align="left">reserved</td>
<td align="left">**启动**</td><td align="left"></td><td align="left"></td>
<td align="left">**问题**</td><td align="left"></td><td align="left"></td>
<td align="left">**Android CDD解读**</td><td align="left"><font color="purple" size="3"> **android CDD–TEE相关解读** </font></td><td align="left"></td>
<td align="left">**TODO**</td><td align="left"><font color="red" size="3"> 全网第一篇震撼史无前例：Strongbox的设计模型讲解</font>–ongoing</td><td align="left"></td>

<th align="left">类别</th><th align="left">博文</th><th align="left">参考/说明</th>
|------
<td align="left">**zerotouch**</td><td align="left"></td><td align="left"></td>

<img src="https://img-blog.csdnimg.cn/998b5eef7617440ebc92d3cfa9581b0e.gif" alt="请添加图片描述">
