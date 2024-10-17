
--- 
title:  Java练习题-键盘录入字符串实现大小写转换 
tags: []
categories: [] 

---
>  
 ✅作者简介：CSDN内容合伙人、阿里云专家博主、51CTO专家博主、新星计划第三季python赛道Top1🏆 📃个人主页： 🔥系列专栏： 💬个人格言：不断的翻越一座又一座的高山，那样的人生才是我想要的。这一马平川，一眼见底的活，我不想要,我的人生，我自己书写，余生很长，请多关照，我的人生，敬请期待💖💖💖 


<img src="https://img-blog.csdnimg.cn/6d86d7b55bd348518f381a9ee82a0c8d.jpeg#pic_center" alt="在这里插入图片描述">



#### 字符串实现大小写转换
- - <ul><li>- - - 


## 题目

>  
 键盘录入一个字符串，将大小写互换，即将字符串中大写字母转为小写字母，小写字母转为大写字母 


### 实现思路

1.导入Scanner类

```
import java.util.Scanner;

```

2.创建键盘录入对象

```
Scanner sc = new Scanner(System.in);

```

3.提示用户输入一个字符串

```
System.out.println("请输入一个字符串:");

```

4.接收用户输入的字符串

```
String input = sc.nextLine();

```

5.创建一个新的StringBuilder对象result

>  
 StringBuilder是一个可变的字符序列，通常用于操作字符串，例如添加、删除或替换字符。 


```
StringBuilder result = new StringBuilder();

```

6.遍历输入的字符串，对每个字符进行大小写转换

>  
 这是一个增强型for循环（也称为for-each循环），它遍历 `input` 字符串中的每个字符。`toCharArray()` 方法将字符串转换为一个字符数组，每次循环都会将数组中的一个字符赋值给变量 `c`。 


```
 for (char c : input.toCharArray()) 

```

>  
 使用 `Character` 类的 `isUpperCase` 方法检查字符 `c` 是否为大写字母。如果 `c` 是大写字母，控制流就进入到这个if块。如果 `c` 是大写字母，这行代码就将 `c` 转换为小写字母，并将其追加到 `result` 的末尾。`Character.toLowerCase(c)` 将大写字母转换为对应的小写字母。`append` 方法是 `StringBuilder` 的一个方法，用于在其末尾添加字符。 


```
 if (Character.isUpperCase(c)) {<!-- -->
        result.append(Character.toLowerCase(c));
      }

```

>  
 如果 `c` 不是大写字母，它将检查 `c` 是否为小写字母。如果 `c` 是小写字母，控制流就进入到这个 else-if块。 如果 `c` 是小写字母，这行代码就将 `c` 转换为大写字母，并将其追加到 `result` 的末尾。`Character.toUpperCase(c)` 将小写字母转换为对应的大写字母。 


```
else if (Character.isLowerCase(c)) {<!-- -->
        result.append(Character.toUpperCase(c));
        // 如果是其他字符，直接添加到结果中
      } 

```

>  
 如果 `c` 既不是大写字母也不是小写字母（例如，它可能是数字、标点符号或空格），控制流就进入到这个 else 块。`result.append(c);`：如果 `c` 不是字母，就将 `c` 原样追加到 `result` 的末尾。 


```
else {<!-- -->
        result.append(c);
      }

```

### 具体代码实现

```
// 导入Scanner类
import java.util.Scanner;

public class String03 {<!-- -->
  public static void main(String[] args) {<!-- -->
    // 创建键盘录入对象
    Scanner sc = new Scanner(System.in);
    // 提示用户输入一个字符串
    System.out.println("请输入一个字符串:");
    // 接收用户输入的字符串
    String input = sc.nextLine();
    // 创建StringBuilder对象
    StringBuilder result = new StringBuilder();
    // 遍历字符串
    for (char c : input.toCharArray()) {<!-- -->
      // 如果是大写，转换为小写
      if (Character.isUpperCase(c)) {<!-- -->
        result.append(Character.toLowerCase(c));
        // 如果是小写，转换为大写
      } else if (Character.isLowerCase(c)) {<!-- -->
        result.append(Character.toUpperCase(c));
        // 如果是其他字符，直接添加到结果中
      } else {<!-- -->
        result.append(c);
      }
    }
    // 输出结果
    System.out.println("转换前的字符串:" + input);
    System.out.println("转换后的字符串:" + result);
  }
}

```

## 扩展题目

>  
 键盘录入一个字符串，将字符串中的字符全转大写，全转小写。 


### 实现思路

1.导入Scanner类

```
import java.util.Scanner;

```

2.创建键盘录入对象

```
    Scanner sc = new Scanner(System.in);

```

3.提示用户输入一个字符串

```
 System.out.println("请输入一个字符串:");

```

4.接收用户输入的字符串

```
String input = sc.nextLine();

```

5.调用方法实现大小写转换

>  
 String类中的`toUpperCase()`将字符串中所有字符全转`大写` String类中的`toLowerCase()`将字符串中所有字符全转`小写` 


```
    String upperCase = input.toUpperCase();
    System.out.println("转换为大写:" + upperCase);
    String lowerCase = input.toLowerCase();
    System.out.println("转换为小写:" + lowerCase);

```

### 具体代码实现

```
// 导入Scanner类
import java.util.Scanner;

public class String01 {<!-- -->
  public static void main(String[] args) {<!-- -->
    // 创建键盘录入对象
    Scanner sc = new Scanner(System.in);
    // 提示用户输入一个字符串
    System.out.println("请输入一个字符串:");
    // 接收用户输入的字符串
    String input = sc.nextLine();
    // 调用方法实现转换
    String upperCase = input.toUpperCase();
    System.out.println("转换为大写:" + upperCase);
    String lowerCase = input.toLowerCase();
    System.out.println("转换为小写:" + lowerCase);
  }
}


```

## 结束语

>  
 以上就是Java练习题-键盘录入字符串实现大小写转换 `持续更新Java练习题专栏，敬请期待` 专栏地址: 


<img src="https://img-blog.csdnimg.cn/5b80ea7dab574ae5bb3fda934fe3f872.gif#pic_center" alt="在这里插入图片描述">
