
--- 
title:  Java练习题-输出斐波那契(Fibonacci)数列 
tags: []
categories: [] 

---
>  
 ✅作者简介：CSDN内容合伙人、阿里云专家博主、51CTO专家博主、新星计划第三季python赛道Top1🏆 📃个人主页： 🔥系列专栏： 💬个人格言：不断的翻越一座又一座的高山，那样的人生才是我想要的。这一马平川，一眼见底的活，我不想要,我的人生，我自己书写，余生很长，请多关照，我的人生，敬请期待💖💖💖 


<img src="https://img-blog.csdnimg.cn/b879c801a9854ac890eb723dcd80aaa1.png#pic_center" alt="在这里插入图片描述"> 

#### 输出Fibonacci数列
- - <ul><li>- - 


## 题目

编写程序，使用递归方法打印输出Fibonacci数列的前20项

### 斐波那契(Fibonacci)数列

`Fibonacci数列（Fibonacci sequence）`，又称黄金分割数列、因数列的形式简洁且定义明确，被广泛的应用在理论数学和应用数学中。

Fibonacci数列由意大利数学家`莱昂纳多·斐波那契（Leonardo Fibonacci）`在1202年的一本书中提出，因此得名。他在书中提出了这样一个问题：一对刚出生的兔子，从第二个月开始就可以生育，每月每对可生育的兔子都会生出一对新的兔子，新出生的兔子从第二个月开始就可以生育。假设所有的兔子都不会死去，问：每个月的兔子总数是多少？

根据这个问题的设定，我们可以得到的Fibonacci数列：`1, 1, 2, 3, 5, 8, 13, 21, ....`

也就是说，Fibonacci数列中的每一项，从第3项开始，都是前两项之和。用数学公式来表示，就是：`F(n) = F(n-1) + F(n-2)，其中n&gt;=3，F(1) = 1，F(2) = 1`

Fibonacci数列与黄金分割有着密切的关系。当Fibonacci数列进行到足够大的时候，相邻两项的比值将趋近于黄金分割的值：1.6180339887…

### 实现思路

1.定义一个`fibonacci`递归方法，用于计算`Fibonacci`数列的第n项，在`fibonacci`方法中，首先进行判断，如果`n&lt;=1`，则直接返回`n`本身。如果`n&gt;1`，则通过递归调用`fibonacci(n-1)` 和`fibonacci(n-2)`来计算第n项的值，即前两项的和

```
    public static int fibonacci(int n){<!-- -->
      //如果n小于等于1，返回n
        if(n &lt;= 1){<!-- -->
            return n;
        }else{<!-- -->//否则返回前两项之和
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
    }

```

2.在`main`方法中，我们使用一个循环来输出`fibonacci`数列的`前20项`，不断地循环调用定义的`fibonacci`方法，直到循环结束，输出`fibonacci`数列的前20项

```
    public static void main(String[] args){<!-- -->
        //循环输出前20项
        for(int i = 0; i &lt; 20; i++){<!-- -->
            System.out.println(fibonacci(i));
        }
    }

```

### 具体代码实现

```
//使用递归方法输出fibonacci数列的前20项
public class fib{<!-- -->
    public static void main(String[] args){<!-- -->
        //循环输出前20项
        for(int i = 0; i &lt; 20; i++){<!-- -->
            System.out.println(fibonacci(i));
        }
    }
    //定义递归方法
    public static int fibonacci(int n){<!-- -->
      //如果n小于等于1，返回n
        if(n &lt;= 1){<!-- -->
            return n;
        }else{<!-- -->//否则返回前两项之和
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
    }
}

```

## 结束语

>  
 以上就是Java练习题-输出斐波那契(Fibonacci)数列 `持续更新Java练习题专栏，敬请期待` 专栏地址: 


<img src="https://img-blog.csdnimg.cn/5b80ea7dab574ae5bb3fda934fe3f872.gif#pic_center" alt="在这里插入图片描述">
