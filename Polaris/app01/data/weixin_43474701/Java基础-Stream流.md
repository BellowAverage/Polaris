
--- 
title:  Java基础-Stream流 
tags: []
categories: [] 

---


#### Stream流
- <ul><li>- - - - - - 


### 1、Stream流初体验

>  
 - 体验Stream流- 创建一个集合，存储多个字符串元素- “张三丰”,“张无忌”,“张翠山”,“王二麻子”,“张良”,“谢广坤”- 把集合中所有以"张"开头的元素存储到一个新的集合- 把"张"开头的集合中的长度为3的元素存储到一个新的集合- 遍历上一步得到的集合 


```
public class MyStream1 {<!-- -->
    public static void main(String[] args) {<!-- -->
        //集合的批量添加
        ArrayList&lt;String&gt; list1 = new ArrayList&lt;&gt;(List.of("张三丰","张无忌","张翠山","王二麻子","张良","谢广坤"));
        //list.add()

        //遍历list1把以张开头的元素添加到list2中。
        ArrayList&lt;String&gt; list2 = new ArrayList&lt;&gt;();
        for (String s : list1) {<!-- -->
            if(s.startsWith("张")){<!-- -->
                list2.add(s);
            }
        }

        //遍历list2集合，把其中长度为3的元素，再添加到list3中。
        ArrayList&lt;String&gt; list3 = new ArrayList&lt;&gt;();
        for (String s : list2) {<!-- -->
            if(s.length() == 3){<!-- -->
                list3.add(s);
            }
        }
        for (String s : list3) {<!-- -->
            System.out.println(s);
        }
        System.out.println("=======================");
       //Stream流
        list1.stream().filter(s-&gt;s.startsWith("张"))
                .filter(s-&gt;s.length() == 3)
                .forEach(s-&gt; System.out.println(s));
    }
}

```

<img src="https://img-blog.csdnimg.cn/093c90634e3143e28b114fe6186a71a5.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/bbca251dbcee4bc790f8e95d71466a79.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d20d0570ed0b4fcdbb36c6f03344d70c.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/f38fc3a323c74335a4042545e56d0852.png" alt="在这里插入图片描述">

### 2、Stream流获取方法

<img src="https://img-blog.csdnimg.cn/776e02cd86e94b83a08e23f4f360ba38.png" alt="在这里插入图片描述">

>  
 Stream流的获取 单列集合 : 集合对象.stream(); 双列集合 : 不能直接获取,需要间接获取 集合对象.keySet().stream(); 集合对象.entrySet().stream(); 数组 : Arrays.stream(数组名); 
 同种数据类型的多个数据: 
 <pre><code>        Stream.of(数据1,数据2,数据3......);
</code></pre> 


```
public class MyStream2 {<!-- -->
    public static void main(String[] args) {<!-- -->
        //单列集合
        //method1();//ctrl+alt+m抽取方法快捷键

        //双列集合
        //method2();

        //数组
        //method3();

        //同种数据类型的多个数据
        //method4();

    }

    private static void method4() {<!-- -->
        Stream.of(1,2,3,4,5,6,7,8).forEach(s-&gt; System.out.println(s));
    }

    private static void method3() {<!-- -->
        int [] arr = {<!-- -->1,2,3,4,5};
        Arrays.stream(arr).forEach(s-&gt; System.out.println(s));
    }

    private static void method2() {<!-- -->
        HashMap&lt;String,Integer&gt; hm = new HashMap&lt;&gt;();
        hm.put("zhangsan",23);
        hm.put("lisi",24);
        hm.put("wangwu",25);
        hm.put("zhaoliu",26);
        hm.put("qianqi",27);

        //双列集合不能直接获取Stream流
        //keySet
        //先获取到所有的键
        //再把这个Set集合中所有的键放到Stream流中
        //hm.keySet().stream().forEach(s-&gt; System.out.println(s));
        
        //entrySet
        //先获取到所有的键值对对象
        //再把这个Set集合中所有的键值对对象放到Stream流中
        hm.entrySet().stream().forEach(s-&gt; System.out.println(s));
    }

    private static void method1() {<!-- -->
        ArrayList&lt;String&gt; list = new ArrayList&lt;&gt;();
        list.add("aaa");
        list.add("bbb");
        list.add("ccc");

//        Stream&lt;String&gt; stream = list.stream();
//        stream.forEach(s-&gt; System.out.println(s));
        list.stream().forEach(s-&gt; System.out.println(s));
    }
}

```

### 3、Stream流的常见的中间方法

<img src="https://img-blog.csdnimg.cn/67b445d69536468a8b54be11ec7ac83f.png" alt="在这里插入图片描述">

```
public class MyStream3 {<!-- -->
    public static void main(String[] args) {<!-- -->
//        Stream&lt;T&gt; filter​(Predicate predicate)：过滤
//                Predicate接口中的方法	boolean test​(T t)：对给定的参数进行判断，返回一个布尔值

        ArrayList&lt;String&gt; list = new ArrayList&lt;&gt;();
        list.add("张三丰");
        list.add("张无忌");
        list.add("张翠山");
        list.add("王二麻子");
        list.add("张良");
        list.add("谢广坤");

        //filter方法获取流中的 每一个数据.
        //而test方法中的s,就依次表示流中的每一个数据.
        //我们只要在test方法中对s进行判断就可以了.
        //如果判断的结果为true,则当前的数据留下
        //如果判断的结果为false,则当前数据就不要.
//        list.stream().filter(
//                new Predicate&lt;String&gt;() {<!-- -->
//                    @Override
//                    public boolean test(String s) {<!-- -->
//                        boolean result = s.startsWith("张");
//                        return result;
//                    }
//                }
//        ).forEach(s-&gt; System.out.println(s));


        //因为Predicate接口中只有一个抽象方法test
        //所以我们可以使用lambda表达式来简化
//        list.stream().filter(
//                (String s)-&gt;{<!-- -->
//                    boolean result = s.startsWith("张");
//                        return result;
//                }
//        ).forEach(s-&gt; System.out.println(s));

        list.stream().filter(s -&gt;s.startsWith("张")).forEach(s-&gt; System.out.println(s));
    }
}

```

**其他的中间操作方法** <img src="https://img-blog.csdnimg.cn/62efe87f10474bf883e6d0482fa727d7.png" alt="在这里插入图片描述">

```
public class MyStream4 {<!-- -->
    public static void main(String[] args) {<!-- -->
        ArrayList&lt;String&gt; list = new ArrayList&lt;&gt;();
        list.add("张三丰");
        list.add("张无忌");
        list.add("张翠山");
        list.add("王二麻子");
        list.add("张良");
        list.add("谢广坤");
        list.add("谢广坤");
        list.add("谢广坤");
        list.add("谢广坤");
        list.add("谢广坤");
        
        //method1(list);
        //method2(list);
        //method3();
        //method4(list);

    }

    private static void method4(ArrayList&lt;String&gt; list) {<!-- -->
        //        Stream&lt;T&gt; distinct​()：去除流中重复的元素。依赖(hashCode和equals方法)
        list.stream().distinct().forEach(s-&gt; System.out.println(s));
    }

    private static void method3() {<!-- -->
        //static &lt;T&gt; Stream&lt;T&gt; concat​(Stream a, Stream b)：合并a和b两个流为一个流
        ArrayList&lt;String&gt; list = new ArrayList&lt;&gt;();
        list.add("张三丰");
        list.add("张无忌");
        list.add("张翠山");
        list.add("王二麻子");
        list.add("张良");
        list.add("谢广坤");
        list.add("谢广坤");
        list.add("谢广坤");
        list.add("谢广坤");
        list.add("谢广坤");

        ArrayList&lt;String&gt; list2 = new ArrayList&lt;&gt;();
        list2.add("张三丰");
        list2.add("张无忌");
        list2.add("张翠山");
        list2.add("王二麻子");
        list2.add("张良");
        list2.add("谢广坤");

//        Stream&lt;String&gt; stream1 = list.stream();
//        Stream&lt;String&gt; stream2 = list2.stream();
//
//        Stream&lt;String&gt; stream3 = Stream.concat(stream1, stream2);
//        stream3.forEach(s-&gt; System.out.println(s));

        Stream.concat(list.stream(),list2.stream()).forEach(s-&gt; System.out.println(s));//合并输出
    }

    private static void method2(ArrayList&lt;String&gt; list) {<!-- -->
        //        Stream&lt;T&gt; skip​(long n)：跳过指定参数个数的数据
        list.stream().skip(2).forEach(s-&gt; System.out.println(s));//跳过前面两个
    }

    private static void method1(ArrayList&lt;String&gt; list) {<!-- -->
        //        Stream&lt;T&gt; limit​(long maxSize)：截取指定参数个数的数据
        list.stream().limit(2).forEach(s-&gt; System.out.println(s));//保留前面两个
    }
}

```

### 4、Stream流终结方法

<img src="https://img-blog.csdnimg.cn/c7a8ef06b5214bd5ae9c7829bf398f76.png" alt="在这里插入图片描述">

```
/**
 * Stream流的终结方法
 */
public class MyStream5 {<!-- -->
    public static void main(String[] args) {<!-- -->
        ArrayList&lt;String&gt; list = new ArrayList&lt;&gt;();
        list.add("张三丰");
        list.add("张无忌");
        list.add("张翠山");
        list.add("王二麻子");
        list.add("张良");
        list.add("谢广坤");

        //method1(list);


//        long count​()：返回此流中的元素数
        long count = list.stream().count();
        System.out.println(count);
        
    }

    private static void method1(ArrayList&lt;String&gt; list) {<!-- -->
        //        void forEach​(Consumer action)：对此流的每个元素执行操作
//                      Consumer接口中的方法	void accept​(T t)：对给定的参数执行此操作
        //在forEach方法的底层,会循环获取到流中的每一个数据.
        //并循环调用accept方法,并把每一个数据传递给accept方法
        //s就依次表示了流中的每一个数据.
        //所以,我们只要在accept方法中,写上处理的业务逻辑就可以了.
        list.stream().forEach(
                new Consumer&lt;String&gt;() {<!-- -->
                    @Override
                    public void accept(String s) {<!-- -->
                        System.out.println(s);
                    }
                }
        );
//forEach方法的形参是一个接口，那么传递给它的一定是接口的实现类对象，在这
//里先写一个匿名内部类，这个匿名内部类就是接口的实现类对象

        System.out.println("====================");
	
        //lambda表达式的简化格式   (与形参保持一致数据类型与流中保持一致)-&gt;{}
        //是因为Consumer接口中,只有一个accept方法
        list.stream().forEach(
                (String s)-&gt;{<!-- -->
                    System.out.println(s);
                }
        );
        System.out.println("====================");

        //lambda表达式还是可以进一步简化的.
        //	形参只有一个类型可以简化小括号可以简化
        list.stream().forEach(s-&gt;System.out.println(s));
    }
}

```

### 5、在Stream流中无法直接修改集合,数组等数据源中的数据

<img src="https://img-blog.csdnimg.cn/86d6c21f95fe41999baab031c2c9e380.png" alt="在这里插入图片描述">

```
/**
 * Stream流的收集方法
 * 练习:
 * 定义一个集合，并添加一些整数1,2,3,4,5,6,7,8,9,10
 * 将集合中的奇数删除，只保留偶数。
 * 遍历集合得到2，4，6，8，10。
 */
public class MyStream6 {<!-- -->
    public static void main(String[] args) {<!-- -->
        ArrayList&lt;Integer&gt; list = new ArrayList&lt;&gt;();
        //List.of批量添加太麻烦用遍历
        for (int i = 1; i &lt;= 10; i++) {<!-- -->
            list.add(i);
        }

//        list.stream().filter(
//                (Integer i)-&gt;{<!-- -->
//                    return i % 2 == 0;
//                }
//        )
        list.stream().filter(number -&gt; number % 2 == 0).forEach(number -&gt; System.out.println(number));
        System.out.println("====================");

        for (Integer integer : list) {<!-- -->
            System.out.println(integer);
        }


    }
}

```

<img src="https://img-blog.csdnimg.cn/5409a644f5324b0ca601874609b7aff4.png" alt="在这里插入图片描述">

### 6、Stream流的收集操作

<img src="https://img-blog.csdnimg.cn/84121fbc4b16482484631820e2724c4d.png" alt="在这里插入图片描述">

```
/**
 * Stream流的收集方法
 * 练习:
 * 定义一个集合，并添加一些整数1,2,3,4,5,6,7,8,9,10
 * 将集合中的奇数删除，只保留偶数。
 * 遍历集合得到2，4，6，8，10。
 */
public class MyStream7 {<!-- -->
    public static void main(String[] args) {<!-- -->
        ArrayList&lt;Integer&gt; list1 = new ArrayList&lt;&gt;();
        for (int i = 1; i &lt;= 10; i++) {<!-- -->
            list1.add(i);
        }

        list1.add(10);
        list1.add(10);
        list1.add(10);
        list1.add(10);
        list1.add(10);

        //filter负责过滤数据的.
        //collect负责收集数据.
        //获取流中剩余的数据,但是他不负责创建容器,也不负责把数据添加到容器中.
        //Collectors.toList() : 在底层会创建一个List集合.并把所有的数据添加到List集合中.
        List&lt;Integer&gt; list = list1.stream().filter(number -&gt; number % 2 == 0)
                .collect(Collectors.toList());

        System.out.println(list);


        Set&lt;Integer&gt; set = list1.stream().filter(number -&gt; number % 2 == 0)
                .collect(Collectors.toSet());
        System.out.println(set);
    }
}

```

### 7、Stream流的练习

<img src="https://img-blog.csdnimg.cn/d14d256bc59749d48e87e23930e79aaa.png" alt="在这里插入图片描述">

```
/**
 * 现在有两个ArrayList集合，分别存储6名男演员名称和6名女演员名称，要求完成如下的操作
 * 1.男演员只要名字为3个字的前两人
 * 2.女演员只要姓杨的，并且不要第一个
 * 3.把过滤后的男演员姓名和女演员姓名合并到一起
 * 4.把上一步操作后的元素作为构造方法的参数创建演员对象,遍历数据
 * 演员类Actor，里面有一个成员变量，一个带参构造方法，以及成员变量对应的get/set方法
 */
public class MyStream9 {<!-- -->
    public static void main(String[] args) {<!-- -->
        ArrayList&lt;String&gt;  manList = new ArrayList&lt;&gt;();
        manList.add("张国立");
        manList.add("张晋");
        manList.add("刘烨");
        manList.add("郑伊健");
        manList.add("徐峥");
        manList.add("王宝强");

        ArrayList&lt;String&gt;  womanList = new ArrayList&lt;&gt;();
        womanList.add("郑爽");
        womanList.add("杨紫");
        womanList.add("关晓彤");
        womanList.add("张天爱");
        womanList.add("杨幂");
        womanList.add("赵丽颖");

        //男演员只要名字为3个字的前两人
        Stream&lt;String&gt; stream1 = manList.stream().filter(name -&gt; name.length() == 3).limit(2);

        //女演员只要姓杨的，并且不要第一个
        Stream&lt;String&gt; stream2 = womanList.stream().filter(name -&gt; name.startsWith("杨")).skip(1);

        Stream.concat(stream1,stream2).forEach(name -&gt; {<!-- -->
            Actor actor = new Actor(name);
            System.out.println(actor);
        });
    }
}

```

**结束语 🥇🥇🥇**

>  
 发现非常好用的一个刷题网站!大家一起努力！加油！！！ 题目难度可以自行选择 在线编程出答案，（也可自行查看答案）非常方便 程序员刷题神器网站 

