
--- 
title:  java 和 scala读取文件的目录 
tags: []
categories: [] 

---
### java 版本
1. 新建 Test02
```

import java.io.File;

/**
 *  读取文件的目录
 */
public class Test02 {<!-- -->

    private static int number;

    /**
     *  递归调用文件
     * @param file
     */
    public void test(File file){<!-- -->
        if(!file.exists()){<!-- -->
            System.out.println("您传入的文件路径不存在");
            return;
        }
        if(file.isFile()){<!-- -->
            System.out.println(file);
            number++;
        }else{<!-- -->
            File[] listFiles = file.listFiles();
            for(File fileDemo:listFiles){<!-- -->
                test(fileDemo);
            }
        }
    }


    public static void main(String[] args) {<!-- -->
        Test02 test02 = new Test02();
        String str = "E:\\tool\\system";
        File file = new File(str);
        test02.test(file);
        System.out.println("总文件个数： " + number);
    }
}


```

java File 结合递归调用，实现读取文件

### scala版本
1. 新建 ClassDemo03
```

import java.io.File

/**
 * 打印目录文件
 */
object ClassDemo03 {<!-- -->

  var num:Int = 0

  /**
   * 打印目录
   * @param file
   */
  def printFile(file:File):Unit = {<!-- -->
    if(!file.exists()){<!-- -->
      println("您录入的文件不存在")
    }else{<!-- -->
      if(file.isFile){<!-- -->
        println(file)
        num = num + 1
      }else{<!-- -->
        val files:Array[File] = file.listFiles()
        for(fileDemo &lt;- files){<!-- -->
          printFile(fileDemo)
        }
      }
    }
  }

  /**
   *  打印目录的简写
   * @param file
   */
  def printFile02(file:File):Unit = {<!-- -->
    if(!file.exists()){<!-- -->
      println("您录入的文件不存在")
      return
    }
    if(file.isFile){<!-- -->
      println(file)
      num = num + 1
    }else{<!-- -->
      val arrays:Array[File] = file.listFiles()
      for(fileDemo &lt;- arrays){<!-- -->
        printFile02(fileDemo)
      }
    }
  }

  /**
   *  获取指定目录下所有的文件
   *  1. 定义printFile(dir:File)方法, 该方法接收一个文件目录, 用来打印该目录下所有的文件路径.
   *  2. 在main方法中测试printFile()方法.
   *
   * @param args
   */
  def main(args: Array[String]): Unit = {<!-- -->
    val str = "E:\\tool\\system"
    val file = new File(str)
    printFile(file);
//    printFile02(file);
    println(s"文件总个数： ${num}")
  }

}


```

结合递归调用实现 打印目录文件
