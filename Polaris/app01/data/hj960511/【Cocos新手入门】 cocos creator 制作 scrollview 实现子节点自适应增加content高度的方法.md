
--- 
title:  【Cocos新手入门】 cocos creator 制作 scrollview 实现子节点自适应增加content高度的方法 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解： 使用cocos creator 制作 scrollview 实现子节点自适应增加content高度的方法 作者：任聪聪 日期：2023年2月6日 


## 效果说明

说明：不适用代码控制scrollview的高度，使用cocos自带的方法实现item增加后自动排列和增加content组件的高。 <img src="https://img-blog.csdnimg.cn/e22c5b60247a4a12a5c3aee57bdf0d1f.png" alt="在这里插入图片描述">

## 实现步骤

步骤一、点击我们的scrollview中的content，点击添加组件，选择layout <img src="https://img-blog.csdnimg.cn/2af084bd65a94ea9a99dac87d876b6ed.png" alt="在这里插入图片描述"> 步骤二、配置layout的属性参数如下。 <img src="https://img-blog.csdnimg.cn/cbb1e906bb5c439aa9b92041eaee4f6e.png" alt="在这里插入图片描述"> 步骤三、配置item的高为自适应如下 <img src="https://img-blog.csdnimg.cn/9ce8a794768b4eabb545ce5eb2ff1c07.png" alt="在这里插入图片描述">

end：大功告成，在我们重新复制item到content后，就会发现其属性的height值发生了变化。

## 实际效果

<img src="https://img-blog.csdnimg.cn/9a7176cbdb83461a84f5f55054e2819c.gif#pic_center" alt="在这里插入图片描述"> 仔细看content组件的高度变化。
