
--- 
title:  java instanceof 
tags: []
categories: [] 

---
instanceof 的整理 新建 Test

```

/**
 * instanceof 是 Java 的保留关键字。它的作用是测试它左边的对象是否是它右边的类的实例，返回 boolean 的数据类型。
 */
public class Test {<!-- -->
    public static void main(String[] args) {<!-- -->
        Test test = new Test();
        test.test01();
        test.test02();
        test.test03();
    }

    /**
     * test01: student 属于 Studnet 类型吗true
     * test01: student 属于 Person 类型吗?true
     */
    public void test01(){<!-- -->
        Student student = new Student();
        boolean flag = student instanceof Student;
        boolean flag02 = student instanceof Person;
        System.out.println("test01: student 属于 Studnet 类型吗" + flag);
        System.out.println("test01: student 属于 Person 类型吗?" + flag02);
    }

    /**
     * test02: person 属于 Studnet 类型吗true
     * test02: person 属于 Person 类型吗?true
     */
    public void test02(){<!-- -->
        Person person = new Student();
        boolean flag = person instanceof Student;
        boolean flag02 = person instanceof Person;
        System.out.println("test02: person 属于 Studnet 类型吗" + flag);
        System.out.println("test02: person 属于 Person 类型吗?" + flag02);
    }

    /**
     * test03: person 属于 Studnet 类型吗false
     * test03: person 属于 Person 类型吗?true
     *
     */
    public void test03(){<!-- -->
        Person person = new Person();
        boolean flag = person instanceof Student;
        boolean flag02 = person instanceof Person;
        System.out.println("test03: person 属于 Studnet 类型吗" + flag);
        System.out.println("test03: person 属于 Person 类型吗?" + flag02);
    }
}


class Person{<!-- -->

}

class Student extends Person{<!-- -->

}

```

从打印结果可以看出： System.out.println(“test03: person 属于 Studnet 类型吗” + flag); 是false,因为 person 并不是 Studnet 的实例
