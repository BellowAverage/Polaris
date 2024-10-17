
--- 
title:  【Java入门】常量和变量 
tags: []
categories: [] 

---
>  
 ✅作者简介：CSDN内容合伙人、阿里云专家博主、51CTO专家博主、新星计划第三季python赛道Top1🏆 📃个人主页： 🔥系列专栏： 💬个人格言：不断的翻越一座又一座的高山，那样的人生才是我想要的。这一马平川，一眼见底的活，我不想要,我的人生，我自己书写，余生很长，请多关照，我的人生，敬请期待💖💖💖 


<img src="https://img-blog.csdnimg.cn/c8129b5f5183491da8376eb2e1cda893.png#pic_center" alt="在这里插入图片描述">



#### 常量和变量
- - <ul><li>- - - - - 


## 常量

### 常量的含义

在程序运行过程中，其值<font face="楷体" color="red" size="4">不可以</font>发生改变的量。

### 常量分类

|常量类型|说明|举例
|------
|字符串常量|用双引号括起来的内容|“HelloWorld” ， “但行好事莫问前程”
|整数常量|不带小数的数字|777，-999
|小数常量|带小数的数字|13.14，-5.21
|字符常量|用单引号括起来的内容|‘A’，‘0’，‘我’
|布尔常量|布尔值，表示真假|只有两个值，true，false
|空常量|一个特殊的值，空值|值是：null

<font face="楷体" color="red" size="4">注意事项</font> ：除了空常量其他的都能直接输出

```
package HackerDemo;

public class FirstDemo {<!-- -->
    public static void main(String[] args) {<!-- -->
        //字符串常量
        System.out.println("HelloWorld");
        //整数常量
        System.out.println(777);
        //小数常量
        System.out.println(13.14);
        //字符常量
        System.out.println('A');
        //布尔常量
        System.out.println(true);
    }
}

```

<img src="https://img-blog.csdnimg.cn/d178fc20862c49f4a3d4972791be663a.png" alt="在这里插入图片描述">

```
package HackerDemo;

public class FirstDemo {<!-- -->
    public static void main(String[] args) {<!-- -->
        //空常量不能直接输出
        System.out.println(null);
    }
}


```

<img src="https://img-blog.csdnimg.cn/9857cbf990534534a386e1d2a3d580d3.png" alt="在这里插入图片描述">

## 变量

### 变量的含义

在程序运行过程中，其值<font face="楷体" color="red" size="4">可以</font>发生改变的量。 从本质上讲，变量是内存中一小块区域。

### 如何定义变量

<font face="楷体" color="red" size="4">格式</font> 数据类型 变量名 = 变量值； <font face="楷体" color="red" size="4">范例</font> int a = 10；

### 变量的使用

<mark>取值和修改值</mark>

<font face="楷体" color="red" size="4">取值格式</font> 变量名 <font face="楷体" color="red" size="4">范例</font> a

<font face="楷体" color="red" size="4">修改值格式</font> 变量名=变量值； <font face="楷体" color="red" size="4">范例</font> a = 707；

```
package HackerDemo;

public class FirstDemo {<!-- -->
    public static void main(String[] args) {<!-- -->
        // 定义变量
        int a = 10;
        // 输出变量
        System.out.println("原值:"+ a);
        // 修改变量
        a = 707;
        System.out.println("修改后的值:"+ a);
    }
}

```

<img src="https://img-blog.csdnimg.cn/95d7958816e74cbaa0ca6e824a7d862d.png" alt="在这里插入图片描述">

### 变量使用注意事项
- <font face="楷体" color="red" size="4">变量名不能重复</font>
```
package HackerDemo;

public class FirstDemo {<!-- -->
    public static void main(String[] args) {<!-- -->
        // 定义int类型的变量a
        int a = 10;
        System.out.println(a);
        // 定义float类型的变量a
        float a = 13.14F;
        System.out.println(a);
    }
}


```

<img src="https://img-blog.csdnimg.cn/4b394a2f0f3a42cc826c9d81210144c3.png" alt="在这里插入图片描述">

<font face="楷体" color="red" size="4">解决方法</font> 修改一下变量名即可

```
float b = 13.14F;

```
- <font face="楷体" color="red" size="4">变量未赋值，不能使用</font>
```
package HackerDemo;

public class FirstDemo {<!-- -->
    public static void main(String[] args) {<!-- -->
        // 定义int类型的变量a
        int a;
        System.out.println(a);
    }
}

```

<img src="https://img-blog.csdnimg.cn/30995ad2238e47bd8009b961f0ed561e.png" alt="在这里插入图片描述">

<font face="楷体" color="red" size="4">解决方法</font> 为变量赋值即可

```
int a = 10;

```
- <font face="楷体" color="red" size="4">long类型的变量定义时，为了防止整数过大，值后要加L</font>
```
package HackerDemo;

public class FirstDemo {<!-- -->
    public static void main(String[] args) {<!-- -->
        // 定义int类型的变量a
        long a = 100000000000; 
        System.out.println(a);
    }
}

```

<img src="https://img-blog.csdnimg.cn/c1c4b074cf38432fb585670acd883d49.png" alt="在这里插入图片描述">

<font face="楷体" color="red" size="4">解决方法</font> 整数默认是int类型，为防止整数过大，转化为long类型在值后加L即可

```
long a = 100000000000L;

```
- <font face="楷体" color="red" size="4">float类型的变量定义时，为了防止类型不兼容，值后要加F</font>
```
package HackerDemo;

public class FirstDemo {<!-- -->
    public static void main(String[] args) {<!-- -->
        // 定义int类型的变量a
        float a = 13.14;
        System.out.println(a);
    }
}

```

<img src="https://img-blog.csdnimg.cn/91002f6b216f4b7f90990fc0b1b554ff.png" alt="在这里插入图片描述">

<font face="楷体" color="red" size="4">解决方法</font> 浮点数默认为double类型，转化为float类型在值后加F即可

```
float a = 13.14F;

```

## 结束语

>  
 以上就是Java入门之常量和变量，如有任何问题欢迎在评论区留言 
 - <font face="楷体" color="red" size="4">在下一章节会讲解Java数据类型相关内容</font> 


你们的支持就是hacker创作的动力💖💖💖

<img src="https://img-blog.csdnimg.cn/5b80ea7dab574ae5bb3fda934fe3f872.gif#pic_center" alt="在这里插入图片描述">
