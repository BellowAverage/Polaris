
--- 
title:  [Spark] 读取项目下resources/的文件 
tags: []
categories: [] 

---
>  
 **背景** 这个spark程序要读取项目下的一些文件, 当我把这个项目打成jar包后, spark-submit到集群后执行 


将文件作为资源文件打包到 JAR 中可以通过 Maven 或 sbt 这样的构建工具完成。以下是使用 Maven 的步骤：
1.  首先，在你的 Maven 项目中创建一个目录（比如 `src/main/resources`）用来存放资源文件。 1.  将需要打包的文件放入这个目录下 `src/main/resources/aaaaaa.txt` 1.  在 Maven 项目的 `pom.xml` 文件中，添加以下配置，告诉 Maven 应该将这些文件打包到 JAR 中： 
```
&lt;build&gt;
    &lt;resources&gt;
        &lt;resource&gt;
            &lt;directory&gt;src/main/resources&lt;/directory&gt;
            &lt;includes&gt;
                &lt;include&gt;**/*&lt;/include&gt;
            &lt;/includes&gt;
        &lt;/resource&gt;
    &lt;/resources&gt;
&lt;/build&gt;

```
1. 然后使用 `mvn package` 命令构建你的项目，Maven 会自动将资源文件打包到生成的 JAR 文件中。
在程序中，你可以使用 `getResourceAsStream` 方法来读取这些资源文件，例如：

```
val inputStream = getClass.getResourceAsStream("/aaaaaa.txt")
val fileContent = scala.io.Source.fromInputStream(inputStream).getLines().mkString("\n")

```

通过上述步骤，你就可以将文件作为资源文件打包到 JAR 中，并在程序中正常读取这些文件了。希望对你有所帮助！
