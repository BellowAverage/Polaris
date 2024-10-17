
--- 
title:  java反射 
tags: []
categories: [] 

---
### 反射调用方法

新建 ReflectTestEntry

```

/**
 * 用来测试的实体类
 */
public class ReflectTestEntry {<!-- -->

    private String name;

    private int number;

    public String getName() {<!-- -->
        return name;
    }

    public void setName(String name) {<!-- -->
        this.name = name;
    }

    public int getNumber() {<!-- -->
        return number;
    }

    public void setNumber(int number) {<!-- -->
        this.number = number;
    }

    @Override
    public String toString() {<!-- -->
        return "name:" + name + " &amp;number:" + number;
    }

    public void test01(){<!-- -->
        System.out.println("测试方法");
    }

    public String test02(String msg){<!-- -->
        String name = "测试方法02 " + msg;
        System.out.println(name);
        return name;
    }
}


```

新建 ReflectTest

```

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class ReflectTest {<!-- -->

    public static void main(String[] args) throws IllegalAccessException, NoSuchMethodException, InstantiationException, InvocationTargetException {<!-- -->
        ReflectTest reflectTest = new ReflectTest();
//        reflectTest.test01();
        reflectTest.test02();

    }

    /**
     *  测试方法 test01
     * @throws IllegalAccessException
     * @throws InstantiationException
     * @throws NoSuchMethodException
     * @throws InvocationTargetException
     */
    public void test01() throws IllegalAccessException, InstantiationException, NoSuchMethodException, InvocationTargetException {<!-- -->
        Class&lt;ReflectTestEntry&gt; reflectTestEntryClass = ReflectTestEntry.class;
        ReflectTestEntry reflectTestEntry = reflectTestEntryClass.newInstance(); // 无参构造
        Method method01 = reflectTestEntryClass.getDeclaredMethod("test01", null);
        Object invoke = method01.invoke(reflectTestEntry, null);
    }


    /**
     *  测试方法 test02
     * @throws IllegalAccessException
     * @throws InstantiationException
     * @throws NoSuchMethodException
     * @throws InvocationTargetException
     */
    public void test02() throws IllegalAccessException, InstantiationException, NoSuchMethodException, InvocationTargetException {<!-- -->
        Class&lt;ReflectTestEntry&gt; reflectTestEntryClass = ReflectTestEntry.class;
        ReflectTestEntry reflectTestEntry = reflectTestEntryClass.newInstance(); // 无参构造
        Method method01 = reflectTestEntryClass.getDeclaredMethod("test02", String.class);
        Object invoke = method01.invoke(reflectTestEntry, "开始测试");
        System.out.println("返回值为：" + invoke);
    }

}


```

分别测试了无返回值类型的和有返回值类型的
