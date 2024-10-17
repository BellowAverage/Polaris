
--- 
title:  Java基础-File 
tags: []
categories: [] 

---


#### File
- <ul><li>- - - - - - 


上一篇

### 1、file和IO的概述

思考：以前是如何存储数据的？

```
int a = 10;
int [] arr = {<!-- -->1,2,3,4,5};
ArrayList&lt;String&gt; list = new ArrayList&lt;&gt;();

```

弊端是什么？ <font color="red">不能永久化存储，只要代码运行结束，所有数据都会丢失。</font> 思考：计算机中，有没有一个硬件可以永久化存储？ 我们可以对硬盘进行哪些操作？ <img src="https://img-blog.csdnimg.cn/2bfbf53766bc4e38a271c7b292b8b468.png" alt="在这里插入图片描述"> 对文件进行读写的前提条件？ 我们得知道这个文件在哪 IO就可以对硬盘中的文件进行读写 File表示要读写的文件在哪，也可以对文件进行创建，删除等操作 **IO流是什么？** 1 ，可以将数据从本地文件中读取出来 2 ，可以将数据从内存保存到本地文件 **File类是什么？** 1，在读写数据时告诉虚拟机要操作的（文件/文件夹）在哪 2，对（文件/文件夹）本身进行操作。包括创建，删除等。

### 2、Flie的构造方法

<img src="https://img-blog.csdnimg.cn/162c5f9e24c24b8192aea0b04c1d57dd.png" alt="在这里插入图片描述">

```
public class FileDemo1 {<!-- -->

    public static void main(String[] args) {<!-- -->
        //method1();//抽取方法快捷键：Ctrl+alt+m
        //method2();
        //method3();
    }

    private static void method3() {<!-- -->
        //File​(File parent, String child)      从父抽象路径名和子路径名字符串创建新的File实例
        File file1 = new File("C:\\bianchengid");
        String path = "a.txt";
        File file = new File(file1,path);
        System.out.println(file);//C:\KuGou\a.txt
    }

    private static void method2() {<!-- -->
        //File​(String parent, String child)    从父路径名字符串和子路径名字符串创建新的File实例
        String path1 = "C:\\bianchengid";
        String path2 = "a.txt";
        File file = new File(path1,path2);//把两个路径拼接.
        System.out.println(file);//C:\KuGou\a.txt
    }
    
    private static void method1() {<!-- -->
        //File​(String pathname)        通过将给定的路径名字符串转换为抽象路径名来创建新的File实例
        String path = "C:\\bianchengid\\a.txt";
        File file = new File(path);
        //问题:为什么要把字符串表示形式的路径变成File对象?
        //就是为了使用File类里面的方法.
    }
}

```

### 3、File-绝对路径和相对路径

<img src="https://img-blog.csdnimg.cn/3c7a3adc2717454ca874bca3c4da147a.png" alt="在这里插入图片描述">

### 4、File创建功能

<img src="https://img-blog.csdnimg.cn/174842a1b7cf4e2e97f225c0380ab780.png" alt="在这里插入图片描述">

```
public class FileDemo3 {<!-- -->
    public static void main(String[] args) throws IOException {<!-- -->
        //public boolean createNewFile()    创建一个新的空的文件
                //注意点:
                    //1.如果文件存在,那么创建失败,返回false
                    //2.如果文件不存在,那么创建成功,返回true
                    //3.createNewFile方法不管调用者有没有后缀名,只能创建文件.

        //public boolean mkdir()            创建一个单级文件夹
                //注意点:
                    //1.只能创建单级文件夹,不能创建多级文件夹
                    //2.不管调用者有没有后缀名,只能创建单级文件夹

        //public boolean mkdirs()           创建一个多级文件夹
                //注意点:
                    //1,可以创建单级文件夹,也可以创建多级文件夹
                    //2.不管调用者有没有后缀名,只能创建文件夹

        //疑问:作者：编程ID
            //既然mkdirs能创建单级,也能创建多级.那么mkdir还有什么用啊? 是的

        //method1();

        //method2();

        File file = new File("C:\\KuGou\\aaa.txt");
        boolean result = file.mkdirs();
        System.out.println(result);


    }

    private static void method2() {<!-- -->
        File file = new File("C:\\KuGou\\aaa.txt");
        boolean result = file.mkdir();
        System.out.println(result);
    }

    private static void method1() throws IOException {<!-- -->
        File file1 = new File("C:\\KuGou\\aaa");
        boolean result1 = file1.createNewFile();
        System.out.println(result1);
    }
}

```

<img src="https://img-blog.csdnimg.cn/dbed4694b16e4b16adba43b3012fb4bf.png" alt="在这里插入图片描述">

```
public class FileDemo4 {<!-- -->
    //注意点:
        //1.不走回收站的.
        //2.如果删除的是文件,那么直接删除.如果删除的是文件夹,那么能删除空文件夹
        //3.如果要删除一个有内容的文件夹,只能先进入到这个文件夹,把里面的内容全部删除完毕,才能再次删除这个文件夹
    //简单来说:
        //只能删除文件和空文件夹.作者：编程ID
    public static void main(String[] args) {<!-- -->
        //method1();
        File file = new File("C:\\KuGou");
        boolean result = file.delete();
        System.out.println(result);
    }

    private static void method1() {<!-- -->
        File file = new File("C:\\KuGou\\a.txt");
        boolean result = file.delete();
        System.out.println(result);
    }
}

```

### 5、File-判断和获取功能

<img src="https://img-blog.csdnimg.cn/c336be7a8cdc41ca9bab301236ea16f7.png" alt="在这里插入图片描述">

```
public class FileDemo5 {<!-- -->
    //public boolean isDirectory()  测试此抽象路径名表示的File是否为目录
    //public boolean isFile()       测试此抽象路径名表示的File是否为文件
    //public boolean exists()       测试此抽象路径名表示的File是否存在
    //public String getName()       返回由此抽象路径名表示的文件或目录的名称
                //注意点:
                    //1.如果调用者是文件,那么获取的是文件名和后缀名
                    //2.如果调用者是一个文件夹,那么获取的是文件夹的名字
    public static void main(String[] args) {<!-- -->
        //method1();
        //method2();

        //method3();

        File file = new File("a.txt");
        String name = file.getName();
        System.out.println(name);

        File file1 = new File("C:\\KuGou");
        String name2 = file1.getName();
        System.out.println(name2);
    }

    private static void method3() {<!-- -->
        File file = new File("a.txt");
        boolean result = file.exists();
        System.out.println(result);
    }

    private static void method2() {<!-- -->
        File file = new File("C:\\KuGou");
        boolean result1 = file.isFile();
        boolean result2 = file.isDirectory();
        System.out.println(result1);
        System.out.println(result2);
    }

    private static void method1() {<!-- -->
        File file = new File("C:\\KuGou\\a.txt");
        boolean result1 = file.isFile();
        boolean result2 = file.isDirectory();
        System.out.println(result1);
        System.out.println(result2);
    }
}

```

### 6、File-listFile

<img src="https://img-blog.csdnimg.cn/e9aa2a5f529042c6a709a906e804785c.png" alt="在这里插入图片描述">

```
public class FileDemo6 {<!-- -->

    public static void main(String[] args) {<!-- -->

       File file = new File("D:\\aaa");
        File[] files = file.listFiles();//返回值是一个File类型的数组
        System.out.println(files.length);
        for (File path : files) {<!-- -->
            System.out.println(path);
        }
        //进入文件夹,获取这个文件夹里面所有的文件和文件夹的File对象,并把这些File对象都放在一个数组中返回.
        //包括隐藏文件和隐藏文件夹都可以获取.作者：编程ID
        //注意事项:
            //1.当调用者是一个文件时
            //2,当调用者是一个空文件夹时
            //3.当调用者是一个有内容的文件夹时
            //4.当调用者是一个有权限才能进入的文件夹时
    }
}

```

### 7、案例：File的练习
- 练习一：在当前模块下的aaa文件夹中创建一个a.txt文件
```
public class Test1 {<!-- -->
    public static void main(String[] args) throws IOException {<!-- -->
        //练习一：在当前模块下的aaa文件夹中创建一个a.txt文件
       /* File file = new File("filemodule\\aaa\\a.txt");
        file.createNewFile();*/
        //注意点:文件所在的文件夹必须要存在.

        File file = new File("filemodule\\aaa");
        if(!file.exists()){<!-- -->
            //如果文件夹不存在,就创建出来
            file.mkdirs();
        }
        File newFile = new File(file,"a.txt");
        newFile.createNewFile();
    }
}

```
- 练习二：删除一个多级文件夹
```
 public class Test2 {<!-- -->
    public static void main(String[] args) {<!-- -->
        //练习二：删除一个多级文件夹
        //delete方法
        //只能删除文件和空文件夹.
        //如果现在要删除一个有内容的文件夹?
        //先删掉这个文件夹里面所有的内容.
        //最后再删除这个文件夹

        File src = new File("C:\\Users\\apple\\Desktop\\src");
        deleteDir(src);

    }

    private static void deleteDir(File src) {<!-- -->
        //先删掉这个文件夹里面所有的内容.
        //递归 方法在方法体中自己调用自己.
        //注意: 可以解决所有文件夹和递归相结合的题目
        //1.进入 --- 得到src文件夹里面所有内容的File对象.
        File[] files = src.listFiles();
        //2.遍历 --- 因为我想得到src文件夹里面每一个文件和文件夹的File对象.
        for (File file : files) {<!-- -->
            if(file.isFile()){<!-- -->
                //3.判断 --- 如果遍历到的File对象是一个文件,那么直接删除
                file.delete();
            }else{<!-- -->
                //4.判断
                //递归
                deleteDir(file);//参数一定要是src文件夹里面的文件夹File对象
            }
        }
        //最后再删除这个文件夹
        src.delete();
    }
}

```
- 练习三：统计一个文件夹中每种文件的个数并打印。
>  
 打印格式如下：  txt:3个  doc:4个  jpg:6个  … 


```
public class Test3 {<!-- -->
    public static void main(String[] args) {<!-- -->
        //统计一个文件夹中,每种文件出现的次数.
        //统计 --- 定义一个变量用来统计. ---- 弊端:同时只能统计一种文件
        //利用map集合进行数据统计,键 --- 文件后缀名  值 ----  次数

        File file = new File("filemodule");
        HashMap&lt;String, Integer&gt; hm = new HashMap&lt;&gt;();
        getCount(hm, file);
        System.out.println(hm);
    }

    private static void getCount(HashMap&lt;String, Integer&gt; hm, File file) {<!-- -->
        File[] files = file.listFiles();
        for (File f : files) {<!-- -->
            if(f.isFile()){<!-- -->
                String fileName = f.getName();
                String[] fileNameArr = fileName.split("\\.");
                if(fileNameArr.length == 2){<!-- -->
                    String fileEndName = fileNameArr[1];
                    if(hm.containsKey(fileEndName)){<!-- -->
                        //已经存在
                        //将已经出现的次数获取出来
                        Integer count = hm.get(fileEndName);
                        //这种文件又出现了一次.
                        count++;
                        //把已经出现的次数给覆盖掉.
                        hm.put(fileEndName,count);
                    }else{<!-- -->
                        //不存在
                        //表示当前文件是第一次出现
                        hm.put(fileEndName,1);
                    }
                }
            }else{<!-- -->
                getCount(hm,f);
            }
        }
    }
}

```

**结束语 🥇🥇🥇**

>  
 发现非常好用的一个刷题网站!大家一起努力！加油！！！ 题目难度可以自行选择 在线编程出答案，（也可自行查看答案）非常方便 程序员刷题神器网站 

