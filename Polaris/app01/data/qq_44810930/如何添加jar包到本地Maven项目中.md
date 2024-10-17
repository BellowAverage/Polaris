
--- 
title:  如何添加jar包到本地Maven项目中 
tags: []
categories: [] 

---
在 Maven 中添加一个外部 JAR 包的依赖，你需要使用 Maven 的 `&lt;dependency&gt;` 元素来指定该 JAR 包的坐标信息。以下是具体的步骤：
1. **将 JAR 包手动添加到 Maven 本地仓库：** 首先，确保将外部 JAR 包手动添加到 Maven 本地仓库。可以使用 Maven 的 `mvn install:install-file` 命令。
本机cmd

```
mvn install:install-file -Dfile="&lt;D:\路径.jar&gt;" -DgroupId=&lt;gId&gt;   -DartifactId=&lt;aid&gt;   -Dversion=&lt;version&gt;   -Dpackaging=jar

```
- 将命令中的参数替换为实际的路径、groupId、artifactId、version- 注意去除掉上面代码的尖括号&lt;&gt;<li> **在 Maven 项目的 `pom.xml` 文件中添加依赖：** 打开 Maven 项目的 `pom.xml` 文件，并添加一个 `&lt;dependency&gt;` 元素来声明外部 JAR 包的依赖。 <pre><code class="prism language-xml">&lt;dependencies&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;groupId&lt;/groupId&gt;
        &lt;artifactId&gt;artifactId&lt;/artifactId&gt;
        &lt;version&gt;1.0&lt;/version&gt;
    &lt;/dependency&gt;
&lt;/dependencies&gt;
</code></pre> 请确保将 `&lt;groupId&gt;`、`&lt;artifactId&gt;`、`&lt;version&gt;` 替换为你在第一步中手动添加 JAR 包时指定的坐标信息。 </li><li> **使用 Maven 更新项目依赖：** 在项目根目录执行以下 Maven 命令，以更新项目依赖。 <pre><code class="prism language-bash">mvn clean install
</code></pre> 这将下载依赖并将其添加到项目中。 </li>
完成上述步骤后，你的 Maven 项目就可以使用外部 JAR 包了。

在 Scala 代码中，你可以使用 `import` 语句导入该 JAR 包中的类，然后在代码中调用相关方法。
