
--- 
title:  IntelliJ IDEA安装教程（超详细） 
tags: []
categories: [] 

---
>  
 ✅作者简介：CSDN内容合伙人、阿里云专家博主、51CTO专家博主、新星计划第三季python赛道Top1🏆 📃个人主页： 
  
  <h4>IDEA的使用</h4> 
  - - - - - -  
  
  


## IDEA的简单介绍

IDEA全称IntelliJ IDEA，是Java语言对的集成开发环境，IDEA在业界被认为是公认最好的Java开发工具。

## IDEA的主要优势

✅功能强大 ①强大的整合能力。比如：Git Maven Spring等 ②开箱即用的体验（集成版本控制系统，多语言支持的框架随时可用，无需额外安装插件）

✅符合人体工程学 ①高度智能（快速的智能代码补全 实时代码分析 可靠的重构工具） ②提示功能的快速 便捷 范围广 ③好用的快捷键和代码模板 ④精准搜索

## IDEA的卸载

✅这里以windows10系统为例，此电脑点击找到卸载或更改程序，找到IDEA的安装包卸载即可

<img src="https://img-blog.csdnimg.cn/5693be7f5c4a411987da4a42e7a4fcf1.png" alt="在这里插入图片描述"> ✅勾选这两个选项最后点击Uninstall等待卸载完成即可

<img src="https://img-blog.csdnimg.cn/adaba376fc7c4e4889681aeb513bd4b9.png" alt="在这里插入图片描述">

## IDEA的安装

IDEA下载地址： 两个版本：旗舰版(ULtimate) 社区版(Community） 这里我们选择下载社区版的IDEA，因为白嫖真香😍

<img src="https://img-blog.csdnimg.cn/71c2832fb3ea4fa3b73f86bc44f80c2c.png" alt="在这里插入图片描述"> 根据自己的操作系统对应下载，这里我们选择Windows系统的社区版本，点击Download等待下载完成 <img src="https://img-blog.csdnimg.cn/f229e8dd1adc4a25b081349dce4a69d4.png" alt="在这里插入图片描述">

找到安装包双击下载 <img src="https://img-blog.csdnimg.cn/690f62da85624c809c16482e48e52a20.png" alt="在这里插入图片描述"> ✅点击Next

<img src="https://img-blog.csdnimg.cn/4802b7859c43412f91a54dbe0c6cb421.png" alt="在这里插入图片描述"> ✅这里我选择自定义安装在D盘的IDEA Community 2022.3.1文件夹下，当然也可以选择不更改直接点击Next

<img src="https://img-blog.csdnimg.cn/bd1dcbeb4832486eb148bad35330d17b.png" alt="在这里插入图片描述">

✅勾选这两个选项点击Next

<img src="https://img-blog.csdnimg.cn/4e514ed0bb0d4104b2df334d1aaa0347.png" alt="在这里插入图片描述"> ✅最后点击Install等待下载完成即可

<img src="https://img-blog.csdnimg.cn/4c97615b81b94b469842cfe0aba42d15.png" alt="在这里插入图片描述">

## 第一个程序：HelloWorld

写Java程序的步骤: ①创建项目(projefct) ②创建模块(module) ③创建包(package) ④创建类(class)

✅双击打开IDEA，勾选Do not import settings点击OK <img src="https://img-blog.csdnimg.cn/1aae9b3e683549c5aad8fc9356dd1f90.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/4de5a715c04940d6b7604e1d9f7fef09.png" alt="在这里插入图片描述"> ✅选择New Project这里选择创建一个空的项目名为JavaBasic，最后点击创建即可

<img src="https://img-blog.csdnimg.cn/68afa94932114639825d74fb39df6d12.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d140e1bf3eab4e07b362566b2e3b90a1.png" alt="在这里插入图片描述"> ✅右键项目创建一个模块名为Hacker

<img src="https://img-blog.csdnimg.cn/6c7ef86798094041a0182c02f7796b12.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2777e1cc17a84363a6a857e74efea110.png" alt="在这里插入图片描述"> ✅右键模块名下面的src文件夹创建一个包名为HackerDemo

<img src="https://img-blog.csdnimg.cn/45fbf7572f594219a0fee79bed45fc1b.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/68db4cf068d8437f86adc2749b0acb99.png" alt="在这里插入图片描述"> ✅右键包名创建一个类名为FirstDemo

<img src="https://img-blog.csdnimg.cn/effe6a87388249c389a86fba69270cb5.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/7f346c8ef1814642a1fa6b6681060504.png" alt="在这里插入图片描述">

✅编写程序输出Hello World，代码如下：

```
package HackerDemo;

public class FirstDemo {<!-- -->
    public static void main(String[] args) {<!-- -->
        System.out.println("Hello World");
    }
}

```

运行结果如下：

<img src="https://img-blog.csdnimg.cn/775a4fbfd9084c13b9283553f19f1463.png" alt="在这里插入图片描述">💬扩展： 😍输入psvm可以直接打出程序主入口

```
public static void main(String[] args)

```

😍输入sout可以直接打出输出语句

```
System.out.println();

```

<img src="https://img-blog.csdnimg.cn/f673179614914ede86f7bddcd2d920d3.gif#pic_center" alt="在这里插入图片描述">

## 结束语

以上就是IntelliJ IDEA安装教程，持续更新开发使用的各种实用工具 你们的支持就是hacker创作的动力💝💝💝

<img src="https://img-blog.csdnimg.cn/5b80ea7dab574ae5bb3fda934fe3f872.gif#pic_center" alt="在这里插入图片描述">
