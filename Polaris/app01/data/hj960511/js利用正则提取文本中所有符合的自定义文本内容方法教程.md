
--- 
title:  js利用正则提取文本中所有符合的自定义文本内容方法教程 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解，使用js提取文本中所有出现的特定字符，保存在数组中并返回的实现方法。 日期：2022年12月9日 作者：任聪聪 


### 一、使用的场景说明

一个超长文本中出现了n个固定规则的字符，但是需要将其进行提取并存在数组中，故此我们可以使用如下的函数进行自定义的二次开发，满足不同的提取需要。

### 二、提取日期格式数据演示和代码实例

在我们要从一连串的文本中提取所有日期的话，我们可以通过如下的形式进行提取。

#### 代码实例：

```
var str = "abcdefgs2022年1月1日的就看见1ew年2ui日90月2022年1月2日";
		/**
			* 获取符合特定正则字符的所有内容
			* @param strTxt 原本的字符串
			* @param regx 正则规则
		 */
		var getSpecificCharacters = function(strTxt,regx){<!-- -->
		    return strTxt.match(regx);
		}

console.log(getSpecificCharacters(str,/\d+年\d+月\d+日/g))

```

#### 实际效果：

<img src="https://img-blog.csdnimg.cn/389e437d0508441f81f8002e2884e663.png" alt="在这里插入图片描述">

### 三、提取文本中出现的邮箱

一个文本中出现多次符合的邮箱信息及干扰信息提取方法。

#### 代码实例：

```
var str = "ab123@11.com是十是多是年是家we882jj@22.com=-sjjn多少个人2的@55.com";
		/**
			* 获取符合特定正则字符的所有内容
			* @param strTxt 原本的字符串
			* @param regx 正则规则
		 */
		var getSpecificCharacters = function(strTxt,regx){<!-- -->
		    return strTxt.match(regx);
		}

console.log(getSpecificCharacters(str,/\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{<!-- -->2,14}/g))

```

#### 实际效果：

<img src="https://img-blog.csdnimg.cn/ea85517fe61d482b8af77da8e23827db.png" alt="在这里插入图片描述">

### 其他场景应用说明

只需要替换我们的正则即可，对不同情况下的数据进行不同正则的替换，就可以达到适应各种不同特殊字符串的全提取了。

如提取文本中的“是”

```
console.log(getSpecificCharacters("dshjhjhsdhj是搜索到环境升级是 上的好机会是生就看看是",/是/g))

```

实际效果： <img src="https://img-blog.csdnimg.cn/d57cfc04f8f64f16af2c019e1943ac88.png" alt="在这里插入图片描述">
