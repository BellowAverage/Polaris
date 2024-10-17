
--- 
title:  java try catch finally 与 return的关系 
tags: []
categories: [] 

---
### java try catch finally 与 return的关系

最后有完整的 demo
1. catch 和 finally 都有 return 时，++ 在前时，先计算返回 <img src="https://img-blog.csdnimg.cn/8748447af7104147b71ce600519c9ce1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
```
    /**
     * try catch finally
     *  catch 和 finally 都有 return 时，++ 在前时，先计算再返回
     * catch 语句中的 return 返回值会先被暂存在一个本地变量中，当执行到 finally 语句中的 return 之后，这个本地变量的值就变为了 finally 语句中的 return 返回值。
     * @return
     */
    public static int test01(){<!-- -->
        try{<!-- -->
            number = 5 / number;
            System.out.println("test01_try");
//            return number;
        }catch (Exception e){<!-- -->
            System.out.println("test01_catch:" + number);
            return ++number;
        }finally {<!-- -->
            System.out.println("test01_finally：" + number);
            return ++number;
        }
    }

```
1. catch 和 finally 都有 return 时，++ 在后时， 先返回再计算 <img src="https://img-blog.csdnimg.cn/e1da9cfe30d4420fa496442061e5ebbf.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
```
    /**
     * try catch finally
     * catch 和 finally 都有 return 时，++ 在后时， 先返回再计算
     * catch 语句中的 return 返回值会先被暂存在一个本地变量中，当执行到 finally 语句中的 return 之后，这个本地变量的值就变为了 finally 语句中的 return 返回值。
     * @return
     */
    public static int test02(){<!-- -->
        try{<!-- -->
            number = 5 / number;
            System.out.println("test02_try");
            return number;
        }catch (Exception e){<!-- -->
            System.out.println("test02_catch");
            return number++;
        }finally {<!-- -->
            System.out.println("test02_finally：" + number);
            return number++;
        }
    }

```
1. catch 中的 return 和 finally 中的执行语句的执行顺序， ++ 在前时。先计算值再返回 <img src="https://img-blog.csdnimg.cn/80415e2a82d2412b8c0923dd09602759.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
```
    /**
     * try catch finally
     *  catch 中的 return 和 finally 中的执行语句的执行顺序， ++ 在前时。先计算值再返回
     * @return
     */
    public static int test03(){<!-- -->
        try{<!-- -->
            number = 5 / number;
            System.out.println("test03_try");
            return number;
        }catch (Exception e){<!-- -->
            System.out.println("test03_catch");
            return ++number;
        }finally {<!-- -->
            System.out.println("test03_finally：" + number);
        }
    }


```
1. catch 中的 return 和 finally 中的执行语句的执行顺序， ++ 在后时。先返回再计算值: 这是因为 catch 语句中的 return 返回值会先被暂存在一个本地变量中 <img src="https://img-blog.csdnimg.cn/a66d6918251b4c86ae7db94c29cb5245.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="5.">
```
    /**
     * try catch finally
     *  catch 中的 return 和 finally 中的执行语句的执行顺序， ++ 在后时。先返回再计算值
     *  这是因为 catch 语句中的 return 返回值会先被暂存在一个本地变量中
     * @return
     */
    public static int test04(){<!-- -->
        try{<!-- -->
            number = 5 / number;
            System.out.println("test04_try");
            return number;
        }catch (Exception e){<!-- -->
            System.out.println("test04_catch");
            return number++;
        }finally {<!-- -->
            System.out.println("test04_finally：" + number);
        }
    }

```
1. 三目表达式先计算后返回 <img src="https://img-blog.csdnimg.cn/f0f017a06b404877a71b360212fcd998.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
```
    /**
     * try catch finally
     *  三目表达式先计算后返回
     * @return
     */
    public static int test05(){<!-- -->
        try{<!-- -->
            number = 5 / number;
            System.out.println("test04_try");
            return number;
        }catch (Exception e){<!-- -->
            System.out.println("test04_catch");
            return 1 == 2? 3:4;
        }finally {<!-- -->
            System.out.println("test04_finally：" + number);
        }
    }

```
1. 验证 catch 语句中的 return 返回值会先被暂存在一个本地变量中 <img src="https://img-blog.csdnimg.cn/82ca14ffa446425fa3d6225daf0f5581.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">
```
    /**
     * try catch finally
     *  验证  catch 语句中的 return 返回值会先被暂存在一个本地变量中
     * @return
     */
    public static int test06(){<!-- -->
        try{<!-- -->
            number = 5 / number;
            System.out.println("test06_try");
            return number;
        }catch (Exception e){<!-- -->
            System.out.println("test06_catch");
            return number;
        }finally {<!-- -->
            number++;
            System.out.println("test06_finally：" + number);
        }
    }

```
1. 完成的 demo
```

/**
 * try catch finally
 */
public class Test03 {<!-- -->

    private static int number = 0;

    public static void main(String[] args) {<!-- -->
//        System.out.println(test01());
//        System.out.println(test02());
//        System.out.println(test03());
//        System.out.println(test04());
        System.out.println(test05());
        System.out.println("number：" + number);
        System.out.println("------------");

    }

    /**
     * try catch finally
     * @return
     */
    public static int test01(){<!-- -->
        try{<!-- -->
            number = 5 / number;
            System.out.println("test01_try");
            return number;
        }catch (Exception e){<!-- -->
            System.out.println("test01_catch");
            return number++;
        }finally {<!-- -->
            System.out.println("test01_finally：" + number);
            return ++number;
        }
    }

    /**
     * try catch finally
     * @return
     */
    public static int test02(){<!-- -->
        try{<!-- -->
            number = 5 / number;
            System.out.println("test02_try");
            return number;
        }catch (Exception e){<!-- -->
            System.out.println("test02_catch");
            return number++;
        }finally {<!-- -->
            System.out.println("test02_finally：" + number);
            return number++;
        }
    }

    /**
     * try catch finally
     * @return
     */
    public static int test03(){<!-- -->
        try{<!-- -->
            number = 5 / number;
            System.out.println("test03_try");
            return number;
        }catch (Exception e){<!-- -->
            System.out.println("test03_catch");
            return ++number;
        }finally {<!-- -->
            System.out.println("test03_finally：" + number);
        }
    }

    /**
     * try catch finally
     * @return
     */
    public static int test04(){<!-- -->
        try{<!-- -->
            number = 5 / number;
            System.out.println("test04_try");
            return number;
        }catch (Exception e){<!-- -->
            System.out.println("test04_catch");
            return number++;
        }finally {<!-- -->
            System.out.println("test04_finally：" + number);
        }
    }

    /**
     * try catch finally
     * @return
     */
    public static int test05(){<!-- -->
        try{<!-- -->
            number = 5 / number;
            System.out.println("test04_try");
            return number;
        }catch (Exception e){<!-- -->
            System.out.println("test04_catch");
            return 1 == 2? 3:4;
        }finally {<!-- -->
            System.out.println("test04_finally：" + number);
        }
    }


}


```
