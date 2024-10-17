
--- 
title:  Java基础-IO流（字节流） 
tags: []
categories: [] 

---


#### IO流
- <ul><li>- - - - - - - - - - - - 


上一篇文章

### 1、IO的概述

<img src="https://img-blog.csdnimg.cn/dc0de997f20543ee8a13efb51200d20c.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ec7b3d308cc7444dba82807fac2bfd31.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/efd927ccd9624ab4b005b808941c35e8.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/281cf05a57bb4b31a94e8791e064a2e7.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/c4557b1fa1b245f48bbd47b85f991aa9.png" alt="在这里插入图片描述">

### 2、IO的分类

<img src="https://img-blog.csdnimg.cn/b3357bae9a6b4d5da3f2db7470b21300.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e6d19d653c7a4333b20b38008f6c9ea8.png" alt="在这里插入图片描述">

### 3、字节输出流

<img src="https://img-blog.csdnimg.cn/7d99c90a0c1544478c8ece4621b8b9d9.png" alt="在这里插入图片描述">

```
public class OutputDemo1 {<!-- -->
    public static void main(String[] args) throws IOException {<!-- -->
        //1.创建字节输出流的对象 --- 告诉虚拟机我要往哪个文件中写数据了
        FileOutputStream fos = new FileOutputStream("D:\\a.txt");
        //FileOutputStream fos = new FileOutputStream(new File("D:\\a.txt"));

        //2,写数据
        fos.write(97);

        //3,释放资源
        fos.close();//每次使用完流必须要释放资源。
    }
}

```

<img src="https://img-blog.csdnimg.cn/e3f15887274f4cafbc8889966bd5317b.png" alt="在这里插入图片描述">

### 4、字节流注意事项

<img src="https://img-blog.csdnimg.cn/b6db2eda0cbc4167889c7f3482313f28.png" alt="在这里插入图片描述">

### 5、字节流一次写多个数据

<img src="https://img-blog.csdnimg.cn/61cd0e5be7574572a0f657b4dbd78695.png" alt="在这里插入图片描述"> 第2、3种就是一次写多个数据

```
public class OutputDemo4 {<!-- -->
    public static void main(String[] args) throws IOException {<!-- -->
        FileOutputStream fos = new FileOutputStream("bytestream\\a.txt");
        
        //一次写一个数组;作者：编程ID
        /*byte [] bys = {97,98,99};
        fos.write(bys);*/

        byte [] bys = {<!-- -->97,98,99,100,101,102,103};
        fos.write(bys,1,2);//从bys数组第一个索引开始写两个

        fos.close();//每次使用完流必须要释放资源。
    }
}

```

### 6、字节流-两个问题

<img src="https://img-blog.csdnimg.cn/7671a590bc8540f7b5819128413c878b.png" alt="在这里插入图片描述">

```
public class OutputDemo5 {<!-- -->
    public static void main(String[] args) throws IOException {<!-- -->
        //第二个参数就是续写开关,如果没有传递,默认就是false,
        //表示不打开续写功能,那么创建对象的这行代码会清空文件.

        //如果第二个参数为true,表示打开续写功能
        //那么创建对象的这行代码不会清空文件.
        FileOutputStream fos = new FileOutputStream("C:KuGou\\a.txt",true);

        fos.write(97);
        //能加一个换行
        fos.write("\r\n".getBytes());
        fos.write(98);
        //能加一个换行
        fos.write("\r\n".getBytes());
        fos.write(99);
        //能加一个换行
        fos.write("\r\n".getBytes());
        fos.write(100);
        //能加一个换行
        fos.write("\r\n".getBytes());
        fos.write(101);
        //能加一个换行
        fos.write("\r\n".getBytes());

        fos.close();
    }
}

```

<img src="https://img-blog.csdnimg.cn/757e88ac0bae4a80ab3ac457836da8d2.png" alt="在这里插入图片描述">

### 7、字节流-trycatch捕获异常

<img src="https://img-blog.csdnimg.cn/f6eaa5a50cf6436aaf146bee3833bcaf.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/f814c00a89f24052a1f0820a0467c4ce.png" alt="在这里插入图片描述">

```
public class OutputDemo6 {<!-- -->
    public static void main(String[] args) {<!-- -->
        FileOutputStream fos = null;
        try {<!-- -->
            //System.out.println(2/0);
            fos = new FileOutputStream("C:KuGou\\a.txt");
            fos.write(97);
        }catch(IOException e){<!-- -->
           e.printStackTrace();
        }finally {<!-- -->
            //finally语句里面的代码,一定会被执行.
            if(fos != null){<!-- -->
                try {<!-- -->
                    fos.close();
                } catch (IOException e) {<!-- -->
                    e.printStackTrace();
                }
            }
        }
    }
}

```

### 8、字节流小结

<img src="https://img-blog.csdnimg.cn/6daa1dde2eff41df9afebc205d6b5363.png" alt="在这里插入图片描述">

### 9、字节流输入流

<img src="https://img-blog.csdnimg.cn/f97f60ce3f6c4cf8b44abb5d14469688.png" alt="在这里插入图片描述">

```
public class OutputDemo7 {<!-- -->
    public static void main(String[] args) throws IOException {<!-- -->
        //如果文件存在,那么就不会报错.
        //如果文件不存在,那么就直接报错.
        FileInputStream fis = new FileInputStream("C:KuGou\\a.txt");

        int read = fis.read();
        //一次读取一个字节,返回值就是本次读到的那个字节数据.
        //也就是字符在码表中对应的那个数字.
        //如果我们想要看到的是字符数据,那么一定要强转成char


        System.out.println((char)read);

        //释放资源
        fis.close();
    }
}

```

### 10、字节流读多个字节

```
public class OutputDemo8 {<!-- -->
    public static void main(String[] args) throws IOException {<!-- -->
        FileInputStream fis = new FileInputStream("C:\\KuGou\\a.txt");
        //1,文件中多个字节我怎么办?
        /*while(true){
            int i1 = fis.read();
            System.out.println(i1);
        }*/

        int b;
        while ((b = fis.read())!=-1){<!-- -->
            System.out.println((char) b);
        }
        fis.close();
    }
}

```

### 11、文件复制

<img src="https://img-blog.csdnimg.cn/89fa4a71f4ef4856be570c72d3f831ab.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/c5815e98b81c4260a82e176cafa6dd4e.png" alt="在这里插入图片描述">

```
public class OutputDemo9 {<!-- -->
    public static void main(String[] args) throws IOException {<!-- -->
        //创建了字节输入流,准备读数据.
        FileInputStream fis = new FileInputStream("C:\\KUGou\\a.avi");
        //创建了字节输出流,准备写数据.
        FileOutputStream fos = new FileOutputStream("D:\\a.avi");

        int b;
        while((b = fis.read())!=-1){<!-- -->
            fos.write(b);
        }
        fis.close();
        fos.close();
    }
}

```

### 12、字节流定义小数组拷贝

<img src="https://img-blog.csdnimg.cn/982ef487ddd248b28bfaee27db074f52.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/354fa17bc6c64c729de5375ee88bb464.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2a053e074c2a4540b6e541403f3c70c6.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/22843e87fb474fb99f280ebd2c8d37dc.png" alt="在这里插入图片描述">

```
public class OutputDemo10 {<!-- -->
    public static void main(String[] args) throws IOException {<!-- -->
        FileInputStream fis = new FileInputStream("C:\\itheima\\a.avi");
        FileOutputStream fos = new FileOutputStream("bytestream\\a.avi");

        byte [] bytes = new byte[1024];
        int len; //本次读到的有效字节个数 -- 这次读了几个字节.

        while((len = fis.read(bytes))!=-1){<!-- -->
            fos.write(bytes,0,len);
        }

```

### 13、字节流小数组拷贝原理

<img src="https://img-blog.csdnimg.cn/a56e2a713a67451ea53bae96265ed0e4.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/a5b02665ab464761a8844d1faa703534.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/98cd1325a7f44c8792b62058626c3392.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d30d7496774544c98213c3662c9a2f10.png" alt="在这里插入图片描述">
