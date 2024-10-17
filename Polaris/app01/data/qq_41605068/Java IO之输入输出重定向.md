
--- 
title:  Java IO之输入输出重定向 
tags: []
categories: [] 

---
## 一、前提

### 1.1Java的标准输入,输出分别

        输入       System.in          键盘

        输出       System.out        控制台

### 1.2System类里提供了的重定向标准输入,输出的方法

      static void setErr(PrintStream err)；      //重定向”标准” 错误输出流.        static void setIn(InputStream in)；         //重定向”标准” 输入流        static void setOut(PrintStream out)；     //重定向”标准” 输出流.

## 二、实现

### 2.1重定向”标准” 输入流 

```
public static void main( String[] args )
    {
        File file = new File("src//main//resources//readeMe.txt");  //文件
        try {
            FileInputStream fileInputStream = new FileInputStream(file);  //输入流
            System.setIn(fileInputStream);          //将标准输入流重定向到 fileInputStream 流
            Scanner scanner = new Scanner(System.in); //获取标准输入
            scanner.useDelimiter("\n");            //只把 回车 作为换行符
            while (scanner.hasNext()) System.out.println(scanner.next());  //打印
            fileInputStream.close();  //关闭资源
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
}
```

### 2.2重定向”标准” 输出流

 需要使用打印流 Java.io.outputstream.**PrintStream**

```
public static void main( String[] args )
    {
        File file = new File("src//main//resources//readeMe.txt"); //目的地
        try {
            FileOutputStream fileOutputStream = new FileOutputStream(file); //输出流
            PrintStream printStream = new PrintStream(fileOutputStream); //实例化PrintStream
            System.setOut(printStream);                //标准输出流
            System.out.println("Hello World!");        //输出
            printStream.close();                        //关闭资源
            fileOutputStream.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
}
```

**PrintStream****可以操作：**1：File对象。2：字符串路径。3：字节输出流。

前两个都JDK1.5版本才出现。而且在操作文本文件时，可指定字符编码了。

    当目的是一个字节输出流时，如果使用的println方法，可以在printStream对象上加入一个**true**参数。这样对于println方法可以进行自动的刷新，而不是等待缓冲区满了再刷新。最终print方法都将具体的数据转成字符串，而且都对IO异常进行了内部处理。既然操作的数据都转成了字符串，那么使用PrintWriter更好一些。因为PrintWrite是字符流的子类，可以直接操作字符数据，同时也可以指定具体的编码。

**PrintWriter：**具备了PrintStream的特点同时，

该对象的目的地有四个：1：File对象。2：字符串路径。3：字节输出流。4：字符输出流。

#### 2.2.1使用PrintWriter

```
 public static void main( String[] args )
    {
        File file = new File("src//main//resources//readeMe.txt");
       try {
            FileWriter fileWriter = new FileWriter(file);
            PrintWriter printWriter = new PrintWriter(fileWriter,true);//使用PrintWriter
            printWriter.println(" ^-^ Hwllo World!");
            printWriter.close();
            fileWriter.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } 
}
```

注意：

        System.in，System.out这两个标准的输入输出流，在jvm启动时已经存在了。随时可以使用。当jvm结束了，这两个流就结束了。但是，当使用了显示的close方法关闭时，这两个流在提前结束了。

## 三、对象流的使用

####        ObjectInputStream      ObjectOutputStream

### 3.1写入

```
public static void writeObject(){
        File file = new File("src//main//resources//readeMe.txt");
        try {
            FileOutputStream fileOutputStream = new FileOutputStream(file);
            ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);

            Student stu1 = new Student("IT1901","您好",20);
            Student stu2 = new Student("IT1903","哈哈",21);
            Student stu3 = new Student("IT1902","嘿嘿",22);
            ArrayList&lt;Student&gt; list = new ArrayList&lt;&gt;();
            list.add(stu1);
            list.add(stu2);
            list.add(stu3);
            objectOutputStream.writeObject(list);

            objectOutputStream.close();
            fileOutputStream.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
```

### 3.2读出

```
public static void readObject(){
        File file = new File("src//main//resources//readeMe.txt");
        try {
            FileInputStream fileInputStream = new FileInputStream(file);
            ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream);
            ArrayList&lt;Student&gt; students = (ArrayList&lt;Student&gt;) objectInputStream.readObject();
            for (Student student :students) System.out.println(student);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
```

 
