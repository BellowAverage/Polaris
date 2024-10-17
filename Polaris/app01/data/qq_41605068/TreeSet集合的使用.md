
--- 
title:  TreeSet集合的使用 
tags: []
categories: [] 

---
## 一、TreeSet的原理

      TreeSet会对集合里的元素按照指定的顺序进行排序，它的底层数据结构依据的是红-黑二叉树，

###     1.1什么是红-黑二叉树？

             就是二叉树的每个结点的左右孩子结点的值具有一定规律，即“左小右大”

###     1.2根据什么确定集合里元素的唯一性？

             因为TreeSet会对集合里的元素进行指定顺序的排序，所以，排序需要依据元素自身具备的比较性，如果元素自身不具备比较性，也就是说我们自己创建的实体类并没有具备比较性，那么就会出现**ClassCastException**异常

<img alt="" class="has" height="27" src="https://img-blog.csdnimg.cn/20190811161538958.png" width="954">

可以看到，出现此异常的原因就是，自己创建的Student类没有复写Comparable接口的compareTo方法，当集合添加该元素时，集合并不知道排序的规则，自而会报异常。

            所以，我们需要元素**实现Comparable接口**，强制让元素具备比较性，**复写compareTo方法**。依据compareTo方法的返回值，确定元素在TreeSet数据结构中的位置。**TreeSet****方法保证元素唯一性的方式：**就是参考比较方法的结果是否为0，如果return 0，视为两个对象重复，不存储。

## 二、TreeSet的使用

### 2.1创建实体类Student(实现Comparable接口复写compareTo方法)

####      细节:

        在进行比较时，如何判断是同一个元素？比如，学生的学号、姓名和年龄都一样，就视为同一个人，在判断时，需要分清主要条件和次要条件，当主要条件相同时，再判断次要条件，可根据次要条件进行排序

```

public class Student implements Comparable{
    private String stuClass;  //班级
    private String stuName;  //姓名
    private Integer stuAge;  //年龄

    public Student() {
    }

    public Student(String stuClass, String stuName, Integer stuAge) {
        this.stuClass = stuClass;
        this.stuName = stuName;
        this.stuAge = stuAge;
    }

    public String getStuClass() {
        return stuClass;
    }

    public void setStuClass(String stuClass) {
        this.stuClass = stuClass;
    }

    public String getStuName() {
        return stuName;
    }

    public void setStuName(String stuName) {
        this.stuName = stuName;
    }

    public Integer getStuAge() {
        return stuAge;
    }

    public void setStuAge(Integer stuAge) {
        this.stuAge = stuAge;
    }
    @Override
    public String toString() {
        return "Student{" +
                "stuClass='" + stuClass + '\'' +
                ", stuName='" + stuName + '\'' +
                ", stuAge=" + stuAge +
                '}';
    }
/*
判断是否为同一个学生，先看是否为同一个班级，再看名字是否相同，最后看年龄是否一样，
因此，班级为主要条件，姓名、年龄为次要条件
(可能这个例子不太好，主要是为了说明问题)
*/
    @Override
    public int compareTo(Object o) {
        Student student = (Student)o;
        int num = this.stuClass.compareTo(student.stuClass);
        int num1=  num == 0 ? this.stuName.compareTo(student.stuName):num;
        return num1 ==0 ? this.stuAge.compareTo(student.stuAge):num1;
    }
}

```

### 2.2存入集合中

```
public static void main( String[] args )
    {
        Student stu1 = new Student("IT1903", "IT3", 19);
        Student stu2 = new Student("IT1902", "IT2", 19);
        Student stu3 = new Student("IT1901", "IT1", 19);
        Student stu4 = new Student("IT1902", "IT3", 19);
        Student stu5 = new Student("IT1904", "IT1", 20);
        Student stu6 = new Student("IT1904", "IT1", 21);
        Student stu7 = new Student("IT1904", "IT1", 21);
        TreeSet&lt;Student&gt; treeSet = new TreeSet&lt;&gt;();
        treeSet.add(stu1);
        treeSet.add(stu2);
        treeSet.add(stu3);
        treeSet.add(stu4);
        treeSet.add(stu5);
        treeSet.add(stu6);
        treeSet.add(stu7);
        System.out.println("集合大小:"+treeSet.size());
        for(Student student:treeSet) System.out.println(student);
    }
```

### 2.3结果

<img alt="" class="has" height="182" src="https://img-blog.csdnimg.cn/20190811183434696.png" width="839">

### 2.4分析:

第一步:  Student stu1 = new Student("IT1903", "IT3", 19);

//add(stu1)时，为第一个元素，因此把这个元素作为二叉树的根节点

第二步:   Student stu2 = new Student("IT1902", "IT2", 19);

//add(stu2)时，通过compareTo方法比较，在比较stuClass时，IT1903&gt;IT1902，返回1,待插元素小于已有元素，该元素就作为该stu1结点的左孩子结点

第三步： Student stu3 = new Student("IT1901", "IT1", 19);

//add(stu3)时，和stu1比较，发现小于stu1,接着和stu2比较，发现也小于，于是做stu2的左孩子结点

第四步：Student stu4 = new Student("IT1902", "IT3", 19);

//小于stu1，和stu2中的stuName比较时，大于stu2,做stu2的右孩子结点

第五步：Student stu5 = new Student("IT1904", "IT1", 20);

//大于stu1,做stu1的右孩子结点

第六步：Student stu6 = new Student("IT1904", "IT1", 21);

//大于stu1，大于stu5，做stu5的右孩子结点

第七步：Student stu7 = new Student("IT1904", "IT1", 21);

//大于stu1，大于stu5，和stu6做比较时发现，return 0；该元素重复，不存

### 2.5存储结构

<img alt="" class="has" height="220" src="https://img-blog.csdnimg.cn/20190811183118975.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="597">

从运行结果可知，当遍历TreeSet集合时，就是根据此二叉树进行遍历的。

## 三、**TreeSet集合排序有两种方式，Comparable和Comparator**

在上边使用了Comparable方式

### 3.1使用Comparator

### 3.2创建比较器

自定义一个新类，让该类实现Comparator接口，覆盖compare方法

```
public class MyComparator implements Comparator {
    @Override
    public int compare(Object o1, Object o2) {
        Student stu1 = (Student)o1;
        Student stu2 = (Student)o2;
        int num = stu1.getStuClass().compareTo(stu2.getStuClass());
        int num1 = num == 0?stu1.getStuName().compareTo(stu2.getStuName()):num;
        return num1 == 0?stu1.getStuAge().compareTo(stu2.getStuAge()):num1;
    }
}
```

### 3.3在实例化TreeSet集合时，将该比较器作为参数传入到集合的构造方法中

```
 public static void main( String[] args )
    {
        Student stu1 = new Student("IT1903", "IT3", 19);
        Student stu2 = new Student("IT1902", "IT2", 19);
        Student stu3 = new Student("IT1901", "IT1", 19);
        Student stu4 = new Student("IT1902", "IT3", 19);
        Student stu5 = new Student("IT1904", "IT1", 20);
        Student stu6 = new Student("IT1904", "IT1", 21);
        Student stu7 = new Student("IT1904", "IT1", 21);
        //TreeSet&lt;Student&gt; treeSet = new TreeSet&lt;&gt;();
        TreeSet&lt;Student&gt; treeSet = new TreeSet&lt;&gt;(new MyComparator());
        treeSet.add(stu1);
        treeSet.add(stu2);
        treeSet.add(stu3);
        treeSet.add(stu4);
        treeSet.add(stu5);
        treeSet.add(stu6);
        treeSet.add(stu7);
        System.out.println("集合大小:"+treeSet.size());
        for(Student student:treeSet) System.out.println(student);
    }
```

### 3.4结果

<img alt="" class="has" height="182" src="https://img-blog.csdnimg.cn/20190811183434696.png" width="839">

依然可以实现！！！

## 四、Comparable和Comparator的区别

**   Comparable：让元素自身具备比较性，需要元素对象实现Comparable接口，覆盖compareTo方法。**

**   Comparator：让集合自身具备比较性，需要定义一个实现了Comparator接口的比较器，并覆盖compare方法，并将该类对象作为实际参数传递给TreeSet集合的构造函数。**

**第二种方式较为灵活。**
