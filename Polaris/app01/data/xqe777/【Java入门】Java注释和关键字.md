
--- 
title:  【Java入门】Java注释和关键字 
tags: []
categories: [] 

---
>  
 ✅作者简介：CSDN内容合伙人、阿里云专家博主、51CTO专家博主、新星计划第三季python赛道Top1🏆 📃个人主页： 🔥系列专栏： 💬个人格言：不断的翻越一座又一座的高山，那样的人生才是我想要的。这一马平川，一眼见底的活，我不想要,我的人生，我自己书写，余生很长，请多关照，我的人生，敬请期待💖💖💖 


<img src="https://img-blog.csdnimg.cn/5dc626e98a1843a48e24dc0952990814.png#pic_center" alt="在这里插入图片描述">



#### Java注释和关键字
- - <ul><li>- - 


## Java注释

注释的含义：当我们写程序时需要对代码进行解释说明，这时我们就需要使用注释，以便于后期我们对之前敲过的代码还会有充分的了解。被注释掉的内容不会参与编译和运行，仅仅是对代码的解释说明。

### 单行注释

<font face="楷体" color="red" size="4">格式</font> // 需要注释的内容

```
package HackerDemo;

public class first {<!-- -->
    // 程序主入口
    public static void main(String[] args) {<!-- -->
        // 打印输出Hello World
        System.out.println("Hello World");
    }
}

```

### 多行注释

<font face="楷体" color="red" size="4">格式</font> /* 需要注释的内容 */

```
package HackerDemo;

public class first {<!-- -->
    // 程序主入口
    public static void main(String[] args) {<!-- -->
        /*这是多行注释
        使用for循环打印出0~9
         */
        for (int i = 0; i &lt; 10; i++) {<!-- -->
            System.out.println("打印出来的数字为" + i);
        }
    }
}

```

### 文档注释

<font face="楷体" color="red" size="4">格式</font> /** */
- 文档注释的含义 添加文档注释，可以自动生成以网页的形式体现该程序说明的注释 <font face="楷体" color="red" size="4">后期会详细讲解文档注释相关内容，这里仅以IDEA生成一个简单文档注释为例 </font>- 使用IDEA生成文档注释步骤 1：点击Tools -&gt; Generate JavaDoc(<font face="楷体" color="blue" size="3">生成JavaDoc</font>) <img src="https://img-blog.csdnimg.cn/dd3411c5ad124667bfc008444b5f3704.png" alt="在这里插入图片描述"> 2：- 一定要选择Outout directory(<font face="楷体" color="blue" size="3">输出目录</font>)，不然生成不了- 注意事项 因为Java的编码和IDEA的编码不一样，在command line arguments(<font face="楷体" color="blue" size="3">命令行参数)</font>里面，要添加以下内容
```
-encoding utf8 -docencoding utf8 -charset utf8

```

<img src="https://img-blog.csdnimg.cn/6d5765dfd34648c89940d33d2a478492.png" alt="在这里插入图片描述"> 生成内容如下：

<img src="https://img-blog.csdnimg.cn/f7ea20194fe84d438748bf11a1ed752e.png" alt="在这里插入图片描述">

## Java关键字
- 关键字的含义 被Java赋予特殊涵义的英文单词- 注意事项 Java中的关键字已经被赋予了特殊涵义，这些单词不允许使用 Java一共有53个关键字，这里只做简单的介绍 <font face="楷体" color="red" size="5">后面会单独出一篇文章对Java53个关键字进行详解</font>
|关键字|描述
|------
|public|公共的访问修饰符
|protected|受保护的访问修饰符
|private|私有的访问修饰符
|class|定义类
|interface|定义接口
|abstract|定义抽象类
|implements|实现接口
|extends|继承父类
|new|创建对象
|import|导用
|package|创建包
|byte|字节型
|char|字符型
|boolean|布尔型
|short|短整型
|int|整型
|float|单精度浮点型
|long|长整型
|double|双精度浮点型
|void|当方法用void修饰时，没有返回值
|if|条件语句
|else|否则，用于if条件语句中
|while|循环语句
|for|循环语句
|switch|条件语句，与case连用
|case|与switch连用，通过case提供条件并判断
|default|权限修饰符
|do|与while连用
|break|终止本层循环
|continue|跳过本次循环，进行下次循环
|return|返回方法指定类型的值或者结束方法的执行
|instanceof|二元运算符
|static|静态修饰符
|super|用于在被重写方法中的子类调用父类方法
|final|最终修饰符
|this|用于调用本类的属性，方法
|native|用于Java调用非Java代码的方法
|strictfp|使用此关键字声明会进行严格的计算
|synchronized|用于多线程，保证只能有一个线程执行
|transient|用transient修饰的变量不会保存在磁盘中
|volatile|Java虚拟机提供的轻量级同步机制
|catch|捕获异常，通常与try连用
|try|异常处理语句
|finally|用于异常处理语句，被finally所指定的代码都要被执行
|throw|手动抛出异常
|throws|被throw关键字声明的方法不处理异常，交给方法调用处进行处理
|enum|枚举类型
|assert|表示断言
|const|Java保留字，防止作为程序中的标识符
|goto|Java保留字，防止作为程序中的标识符
|null|用于标识一个不确定对象
|true|布尔类型的真值
|false|布尔类型的假值

## 结束语

>  
 以上就是Java入门之Java注释和关键字 
 - 这里关键字和文档注释仅了解即可，后期会详细进行讲解- 如果有任何问题可以在评论区留言 


持续更新Java系列教程，你们的支持就是hacker创作的动力💖💖💖

<img src="https://img-blog.csdnimg.cn/5b80ea7dab574ae5bb3fda934fe3f872.gif#pic_center" alt="在这里插入图片描述">
