
--- 
title:  java String + 操作符 的注意事项 
tags: []
categories: [] 

---1. +运算的区别
```
  public void test02(){<!-- -->
        String x = "abc";
        String y = "ab" + "c";
        System.out.println(x == y);

        String c = "ab";
        String d = "abc";
        // 相当于   String f = new StringBuilder(c).append("c").toString();
        String e = c + "c";

        System.out.println(c == e);
    }

```

编译后是：

```
 public void test02() {<!-- -->
        String x = "abc";
        String y = "abc";
        System.out.println(x == y);
        String c = "ab";
        String d = "abc";
        String e = c + "c";
        System.out.println(c == e);
    }

```

通过以上能够看出： String y = “ab” + “c”; 编译后变成了 String y = “abc”;而这个 String e = c + “c”; 相当于 String f = new StringBuilder©.append(“c”).toString(); 因此，打印返回 false
