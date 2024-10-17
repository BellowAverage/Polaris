
--- 
title:  java调用python代码 
tags: []
categories: [] 

---
    在做项目的时候，有的时候由于合作人员之间所会的编程语言的不同，会导致项目合作中的一些问题，很多时候需要不同语言之间的调用，这次就分享一下java调用python代码的东西。

## 一、python代码运行

       巧妇难为无米之炊。首先，要确保python环境配置完好，并且相应的python代码可以运行。这个就不在这里进行讲述了，如果有需要可以查看我之前的一些文章。

## 二、java调用python代码

1、查阅了一些网上资料，看到了很多介绍使用jython调用python代码的例子，不过由于一些原因我没有尝试这个方法，而是直接测试了Runtime.getRuntime().exec(args)这个java库中自带的方法，下面直接切入主题。

2、先直接上代码：

python代码（helloword.py）：

```
# coding:utf-8
import numpy as np
 
if __name__ == '__main__':
    a = np.ones(3)
    print(a)
    print '恭喜您！java调用python代码成功'

```

java代码（MyDemo.java）：

```
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class MyDemo {
    public static void main(String[] args) {
        try {
            System.out.println("start");
            String[] args1=new String[]{"/home/huan/anaconda2/bin/python","/home/huan/myfile/pythonfile/helloword.py"};
            Process pr=Runtime.getRuntime().exec(args1);

            BufferedReader in = new BufferedReader(new InputStreamReader(
                    pr.getInputStream()));
            String line;
            while ((line = in.readLine()) != null) {
                System.out.println(line);
            }
            in.close();
            pr.waitFor();
            System.out.println("end");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}

```

执行结果：

<img alt="" class="has" height="169" src="https://img-blog.csdn.net/20180902162004628?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" width="609">

     需要注意的是此行代码：

String[] args1=new String[]{"/home/huan/anaconda2/bin/python","/home/huan/myfile/pythonfile/helloword.py"};

这句代码是很重要的，首先一定要设置好你所使用的python的位置，切记不要直接使用python，因为系统会默认使用自带的python，所以一定要设置好你所使用的python的位置，否则可能会出现意想不到的问题（比如说我使用的是anaconda中的python，而ubuntu系统会默认调用自带的python，而我自带的python中并没有numpy库，所以会造成相应的代码不会执行的问题，所以设置好python的位置是很重要的）。还有就是要设置好py文件的位置，使用绝对路径。

       还有就是可以看出，此方法可以满足我们python代码中调用第三方库的情况，简单实用。

## 三、java中向python代码动态传参

python代码（helloword.py）：

```
# coding:utf-8
import numpy as np
import sys
 
if __name__ == '__main__':
    a = np.ones(3)
    print(a)
    print '恭喜您！java调用python代码成功'
    
    print '脚本名为：%s'%(sys.argv[0])
    print '传入的参数为：'
    for i in range(1, len(sys.argv)):
	print '参数:%s'%(sys.argv[i])

```

java代码（MyDemo.java）：

```
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class MyDemo {
    public static void main(String[] args) {
        try {
            System.out.println("start");
            String para1="time";
            String para2="sfdjk";
            String[] args1 = new String[]{"/home/huan/anaconda2/bin/python", "/home/huan/myfile/pythonfile/helloword.py",para1,para2};
            Process pr = Runtime.getRuntime().exec(args1);

            BufferedReader in = new BufferedReader(new InputStreamReader(
                    pr.getInputStream()));
            String line;
            while ((line = in.readLine()) != null) {
                System.out.println(line);
            }
            in.close();
            pr.waitFor();
            System.out.println("end");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

```

代码运行结果为：

<img alt="" class="has" height="252" src="https://img-blog.csdn.net/20180902164436203?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" width="589">

     好了，多余的话就不说了，一切尽在代码中。此处的分享就到这里了。
