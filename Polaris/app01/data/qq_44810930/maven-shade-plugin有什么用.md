
--- 
title:  maven-shade-plugin有什么用 
tags: []
categories: [] 

---
`maven-shade-plugin` 是 Maven 的一个插件，用于创建可执行的 JAR 文件，并且可以**将所有依赖项打包到一个 JAR 文件中**。

该插件的主要用途是创建包含所有依赖项的“fat” JAR（也称为“uber” JAR），使得应用程序可以作为一个**独立的可执行 JAR 运行**。

以下是 `maven-shade-plugin` 的一些常见用途和功能：
1.  **创建可执行 JAR 文件：** 将项目及其所有依赖项打包到一个 JAR 文件中，使得可以通过简单的 `java -jar` 命令运行。 1.  **解决类冲突：** 在大型项目中，可能会出现依赖项之间的类冲突，即多个依赖项中包含相同的类。`maven-shade-plugin` 可以通过重命名、移除或合并类来解决这些冲突。 1.  **减少 JAR 包数量：** 在一些情况下，如果项目依赖的库很多，构建的 JAR 文件可能会包含大量的依赖 JAR 包。`maven-shade-plugin` 可以将这些依赖项合并到一个 JAR 文件中，减少 JAR 包数量。 1.  **包含资源文件：** 将项目中的资源文件（如配置文件、属性文件等）和依赖项中的资源文件一并打包到 JAR 文件中。 
以下是一个简单的 `maven-shade-plugin` 配置示例：

```
&lt;build&gt;
  &lt;plugins&gt;
    &lt;plugin&gt;
      &lt;groupId&gt;org.apache.maven.plugins&lt;/groupId&gt;
      &lt;artifactId&gt;maven-shade-plugin&lt;/artifactId&gt;
      &lt;version&gt;3.3.0&lt;/version&gt;
      &lt;configuration&gt;
        &lt;createDependencyReducedPom&gt;false&lt;/createDependencyReducedPom&gt;
        &lt;filters&gt;
          &lt;filter&gt;
            &lt;!-- 这里可以配置一些过滤规则，例如排除某些文件或包 --&gt;
          &lt;/filter&gt;
        &lt;/filters&gt;
      &lt;/configuration&gt;
      &lt;executions&gt;
        &lt;execution&gt;
          &lt;phase&gt;package&lt;/phase&gt;
          &lt;goals&gt;
            &lt;goal&gt;shade&lt;/goal&gt;
          &lt;/goals&gt;
        &lt;/execution&gt;
      &lt;/executions&gt;
    &lt;/plugin&gt;
  &lt;/plugins&gt;
&lt;/build&gt;

```

在这个配置中，`&lt;createDependencyReducedPom&gt;` 设置为 `false` 表示不生成降级依赖的 POM 文件。`&lt;filters&gt;` 部分可以用于配置一些过滤规则，例如排除某些文件或包。

使用 `maven-shade-plugin` 时，需要注意潜在的问题
- 可能会增加 JAR 文件的大小- 可能会导致重复的资源文件等。