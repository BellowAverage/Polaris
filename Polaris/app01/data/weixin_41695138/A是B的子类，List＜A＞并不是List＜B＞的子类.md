
--- 
title:  A是B的子类，List＜A＞并不是List＜B＞的子类 
tags: []
categories: [] 

---
### A是B的子类，List并不是List**的子类**
1. 新建一个 Person
```
public class Person {<!-- -->

    private String name;

    private int age;
}


```
1. 新建 Student
```

public class Student extends Person {<!-- -->

    private String message;
}

```
1. 新建 Test
```

import java.util.ArrayList;
import java.util.List;

/**
 *  A是B的子类，List&lt;A&gt;并不是List&lt;B&gt;的子类
 */
public class Test {<!-- -->

    public static void main(String[] args) {<!-- -->
        Test test = new Test();
        test.test02();

        test.test03();
    }


    /**
     *  lncompatible types. 不相容的类型。
     *  Student extends Person,但是 ArrayList&lt;Student&gt;并不是 ArrayList&lt;Person&gt; 的子类
     */
    public void test01(){<!-- -->
        List&lt;Person&gt; arrayList01 = new ArrayList&lt;Person&gt;();
        List&lt;Student&gt; arrayList02 = new ArrayList&lt;Student&gt;();
//        arrayList01 = arrayList02;
    }

    /**
     * List 默认是 object类型的， List&lt;Object&gt;
     *     List&lt;Object&gt; 是所有集合的父类
     */
    public void test02(){<!-- -->
        List arrayList01 = new ArrayList();
        List&lt;Person&gt; arrayList02 = new ArrayList&lt;Person&gt;();
        List&lt;Student&gt; arrayList03 = new ArrayList&lt;Student&gt;();
        List&lt;String&gt; arrayList04 = new ArrayList&lt;String&gt;();
        arrayList01 = arrayList02;
        arrayList01 = arrayList03;
        arrayList01 = arrayList04;

        arrayList03 = arrayList01;
        arrayList02 = arrayList01;
    }


    /**
     * 泛型   List&lt;? extends  Person&gt;
     *   List&lt;? extends  Person&gt; 是 List&lt;Person&gt;    List&lt;Student&gt; 的父类， &lt;? extends  Person&gt; 这一个泛型上界的问题
     */
    public void test03(){<!-- -->
        List&lt;? extends  Person&gt; lists01 = new ArrayList&lt;&gt;();
        List&lt;Person&gt; lists02 = new ArrayList&lt;Person&gt;();
        List&lt;Student&gt; lists03 = new ArrayList&lt;Student&gt;();

        lists01 = lists02;
        lists01 = lists03;
    }
}


```

### 总结：
1. 从test01() 方法中可以看出，虽然 Student extends Person,但是 ArrayList并不是 ArrayList 的子类；1. 从test02()中可以看出：List 是所有集合的父类1. 从test03()中可以看出： List&lt;? extends Person&gt; 是 List List 的父类， &lt;? extends Person&gt; 这一个泛型上界的问题