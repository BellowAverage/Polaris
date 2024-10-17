
--- 
title:  vim 替换 
tags: []
categories: [] 

---
在 Vim 编辑器中进行替换操作可以使用 `:s` 命令。下面是一些示例：
<li> 替换当前行第一个匹配到的字符串： <pre><code>:s/old/new/
</code></pre> </li><li> 替换当前行所有匹配到的字符串： <pre><code>:s/old/new/g
</code></pre> </li><li> 替换从当前行开始到文件末尾的所有匹配到的字符串： <pre><code>:%s/old/new/g
</code></pre> </li><li> 替换整个文件中所有匹配到的字符串，并在每次替换时都要求确认： <pre><code>:%s/old/new/gc
</code></pre> </li>1.  要忽略大小写进行替换 
```
:s/old/new/gi

```

在这些示例中，`old` 是要被替换的字符串，`new` 是替换后的新字符串。`g` 标志表示全局匹配，即替换所有匹配到的字符串。`c` 标志表示确认每次替换。

请注意，Vim 的替换操作是基于模式匹配的，因此你需要了解正则表达式的语法和规则来编写正确的替换模式。
