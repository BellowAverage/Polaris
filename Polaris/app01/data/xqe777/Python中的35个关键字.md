
--- 
title:  Python中的35个关键字 
tags: []
categories: [] 

---
>  
 ✅作者简介：CSDN内容合伙人、阿里云专家博主、51CTO专家博主、新星计划第三季python赛道Top1🏆 📃个人主页： 🔥系列专栏： 💬个人格言：不断的翻越一座又一座的高山，那样的人生才是我想要的。这一马平川，一眼见底的活，我不想要,我的人生，我自己书写，余生很长，请多关照，我的人生，敬请期待💖💖💖 


<img src="https://img-blog.csdnimg.cn/92b6f8a7e4c34feba8b20fb5583de221.gif#pic_center" alt="在这里插入图片描述"> 

#### 关键字详解
- - - - 


## 关键字简介

✅关键字是Python语言中被赋予特殊含义的单词，开发程序时，不可以把这些关键字作为变量、函数、类、模块、和其他对象的名称来使用 如果使用关键字进行命名会报以下异常：`SyntaxError: invalid syntax`：语法错误

<img src="https://img-blog.csdnimg.cn/6ad52218fbf342b98ef36d9a7080b4bc.png" alt="在这里插入图片描述"> ✅在Python3.7.5版本中，一共有35个关键字，如下表所示

|False|None|True|and|as|assert|async
|------
|await|break|class|continue|def|del|elif
|else|except|finally|for|from|global|if
|import|in|is|lambda|nonlocal|not|or
|pass|raise|return|try|while|with|yield

## 查看Python关键字方法

如果想要查看Python中所有的关键字可以使用以下代码进行查看：

```
import keyword

print(keyword.kwlist)

```

<img src="https://img-blog.csdnimg.cn/4e6a1291c60c4f21a183bb4ddcebb69e.png" alt="在这里插入图片描述">

如果想要依次输出关键字可以使用列表中的for循环和enumerate()函数遍历(后面讲列表的时候会讲到，这里仅作了解即可)

```
import keyword

for index, item in enumerate(keyword.kwlist):
    print(index + 1, ":", item)

```

<img src="https://img-blog.csdnimg.cn/2d9b478c149d418aaddab24204001e36.png" alt="在这里插入图片描述">

## 详解Python35个关键字

✅根据专栏更新进度进行补充，此处暂时省略

## 结束语🥇

>  
 以上就是Python基础入门篇之Python中的35个关键字 
 - `欢迎大家订阅系列专栏:`- `此专栏内容会持续更新直到完结为止(如有任何纰漏请在评论区留言或者私信）` 


>  
 感谢大家一直以来对hacker的支持 你们的支持就是博主无尽创作的动力💖💖💖 


<img src="https://img-blog.csdnimg.cn/bdd237d869be4fee9ba4de0f100e35a8.gif#pic_center" alt="在这里插入图片描述">
