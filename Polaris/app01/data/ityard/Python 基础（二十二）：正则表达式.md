
--- 
title:  Python 基础（二十二）：正则表达式 
tags: []
categories: [] 

---


#### 目录
- - - <ul><li>- - <ul><li>- - 


## 1. 简介

正则表达式是一个强大的字符串处理工具，几乎所有的字符串操作都可以通过正则表达式来完成，其本质是一个特殊的字符序列，可以方便的检查一个字符串是否与我们定义的字符序列的某种模式相匹配。

正则表达式并不是 Python 所特有的，几乎所有编程语言都支持正则表达式，Python 提供了内置模块 `re` 和第三方模块 `regex` 来支持正则表达式，`regex` 模块提供了与 `re` 模块兼容的 API 接口，同时还提供了额外的功能和更全面的 Unicode 支持，本文只介绍 `re` 模块。

## 2. 使用

### 2.1 语法

我们先来熟悉一下正则表达式的基本语法。

<th align="center">字符</th><th align="left">说明</th>
|------
<td align="center">`.`</td><td align="left">默认情况，匹配除了换行的任意字符；如果指定了标签 DOTALL，则匹配包括换行符的任意字符</td>
<td align="center">`^`</td><td align="left">匹配字符串的开头，在 MULTILINE 模式也匹配换行后的首个符号</td>
<td align="center">`$`</td><td align="left">匹配字符串尾或者换行符的前一个字符，在 MULTILINE 模式匹配换行符的前一个字符</td>
<td align="center">`*`</td><td align="left">匹配前一个字符 0 到无限次</td>
<td align="center">`+`</td><td align="left">匹配前一个字符 1 到无限次</td>
<td align="center">`?`</td><td align="left">匹配前一个字符 0 次或 1 次</td>
<td align="center">`{m}`</td><td align="left">匹配前一个字符 m 次</td>
<td align="center">`{m, n}`</td><td align="left">匹配前一个字符 m 到 n 次</td>
<td align="center">`*?` `+?` `??` `{m,n}?`</td><td align="left">使 *、+、？、{m,n} 变成非贪婪模式，也就是使这些匹配次数不定的表达式尽可能少的匹配</td>
<td align="center">`\`</td><td align="left">转义特殊字符</td>
<td align="center">`[...]`</td><td align="left">用于表示一个字符集合</td>
<td align="center">`|`</td><td align="left">匹配 | 两边任意表达式</td>
<td align="center">`(...)`</td><td align="left">将括起来的表达式分组，</td>
<td align="center">`(?aiLmsux)`</td><td align="left">aiLmsux 每一个字符代表一个匹配模式，可选多个</td>
<td align="center">`(?:…)`</td><td align="left">(…) 的不分组版本</td>
<td align="center">`(?P&lt;name&gt;…)`</td><td align="left">分组，除了原有的编号外再指定一个额外的别名</td>
<td align="center">`(?P=name)`</td><td align="left">引用别名为 name 的分组匹配到的字符串</td>
<td align="center">`(?#…)`</td><td align="left"># 后面的将作为注释被忽略</td>
<td align="center">`(?=…)`</td><td align="left">匹配 … 的内容，但是并不消费样式的内容</td>
<td align="center">`(?!…)`</td><td align="left">匹配 … 不符合的情况</td>
<td align="center">`(?&lt;=…)`</td><td align="left">匹配字符串的当前位置，它的前面匹配 … 的内容到当前位置</td>
<td align="center">`(?&lt;!…)`</td><td align="left">匹配当前位置之前不是 … 的样式</td>
<td align="center">`(?(id/name)yes-pattern|no-pattern)`</td><td align="left">如果给定的 id 或 name 存在，将会尝试匹配 yes-pattern ，否则就尝试匹配 no-pattern，no-pattern 可选，也可以被忽略</td>
<td align="center">`\number`</td><td align="left">匹配数字代表的组合</td>
<td align="center">`\A`</td><td align="left">只匹配字符串开始</td>
<td align="center">`\b`</td><td align="left">匹配空字符串，但只在单词开始或结尾的位置</td>
<td align="center">`\B`</td><td align="left">匹配空字符串，但不能在词的开头或者结尾</td>
<td align="center">`\d`</td><td align="left">主要匹配数字 [0-9]</td>
<td align="center">`\D`</td><td align="left">匹配任何非十进制数字的字符</td>
<td align="center">`\s`</td><td align="left">匹配空白字符，主要包括：空格 \t \n \r \f \v</td>
<td align="center">`\S`</td><td align="left">匹配任何非空白字符</td>
<td align="center">`\w`</td><td align="left">匹配 [a-zA-Z0-9_]</td>
<td align="center">`\W`</td><td align="left">匹配非单词字符</td>
<td align="center">`\Z`</td><td align="left">只匹配字符串尾</td>

### 2.2 re 模块

#### 2.2.1 模块内容

re 模块几乎包含了正则表达式的所有功能，我们先来看一下该模块的主要方法。

**re.compile(pattern, flags=0)** 用于编译正则表达式，生成一个正则表达式（Pattern）对象，供 match() 和 search() 这两个函数使用。参数说明如下：
-  pattern : 一个字符串形式的正则表达式 -  flags : 匹配模式，包括如下： 
<th align="center">参数</th><th align="left">说明</th>
|------
<td align="center">`re.A`</td><td align="left">让 \w, \W, \b, \B, \d, \D, \s, \S 只匹配 ASCII</td>
<td align="center">`re.I`</td><td align="left">忽略大小写</td>
<td align="center">`re.M`</td><td align="left">多行模式</td>
<td align="center">`re.L`</td><td align="left">由当前语言区域决定 \w, \W, \b, \B 和大小写敏感匹配</td>
<td align="center">`re.S`</td><td align="left">. 匹配包括换行符在内的任意字符</td>
<td align="center">`re.U`</td><td align="left">在 Python3 中是冗余的，因为 Python3 中字符串已经默认为 Unicode</td>
<td align="center">`re.X`</td><td align="left">忽略空格和 # 后面的注释</td>

看一下示例：

```
import re

re.compile(r'abc', re.I)

```

**re.search(pattern, string, flags=0)** 扫描整个字符串找到匹配样式的第一个位置，并返回一个相应的匹配对象；如果没有匹配，就返回一个 None。参数说明如下：
-  pattern：匹配的正则表达式 -  string：要匹配的字符串 -  flags：匹配模式 
看一下示例：

```
import re

print(re.search(r'abc', 'abcef'))
print(re.search(r'abc', 'aBcef'))

```

**re.match(pattern, string, flags=0)** 如果 string 开始的 0 或者多个字符匹配到了正则表达式样式，就返回一个相应的匹配对象；如果没有匹配，就返回 None。看下示例：

```
import re

print(re.match(r'abc', 'abcef'))

```

**re.fullmatch(pattern, string, flags=0)** 如果整个 string 匹配到正则表达式样式，就返回一个相应的匹配对象；否则就返回一个 None。看一下示例：

```
import re

print(re.fullmatch(r'abc', 'abcef'))
print(re.fullmatch(r'abc', 'abc'))

```

**re.split(pattern, string, maxsplit=0, flags=0)** 用 pattern 分开 string，如果在 pattern 中捕获到括号，那么所有的组里的文字也会包含在列表里，如果 maxsplit 非零，最多进行 maxsplit 次分隔，剩下的字符全部返回到列表的最后一个元素。看一下示例：

```
import re

print(re.split(r'\W+', 'ityard, ityard, ityard.'))
print(re.split(r'(\W+)', 'ityard, ityard, ityard.'))
print(re.split(r'\W+', 'ityard, ityard, ityard.', 1))
print(re.split('[a-f]+', '1A2b3', flags=re.IGNORECASE))

```

**re.findall(pattern, string, flags=0)** 对 string 返回一个不重复的 pattern 的匹配列表，string 从左到右进行扫描，匹配按找到的顺序返回，如果样式里存在一到多个组，就返回一个组合列表，空匹配也会包含在结果里。看一下示例：

```
import re

print(re.findall(r'ab', 'abefabdeab'))

```

**re.finditer(pattern, string, flags=0)** pattern 在 string 里所有的非重复匹配，返回为一个迭代器 iterator 保存了匹配对象，string 从左到右扫描，匹配按顺序排列。看一下示例：

```
import re

it = re.finditer(r'\d+', '12ab34cd56')
for match in it:
    print(match)

```

**re.sub(pattern, repl, string, count=0, flags=0)** 返回通过使用 repl 替换在 string 最左边非重叠出现的 pattern 而获得的字符串，count 表示匹配后替换的最大次数，默认 0 表示替换所有的匹配。看一下示例：

```
import re

str = 'ityard # 是我的名字'
print(re.sub(r'#.*$', '', str))

```

**re.subn(pattern, repl, string, count=0, flags=0)** 行为与 re.sub() 相同，但返回的是一个元组。看一下示例：

```
import re

str = 'ityard # 是我的名字'
print(re.subn(r'#.*$', '', str))

```

**re.escape(pattern)** 转义 pattern 中的特殊字符。看一下示例：

```
import re

print(re.escape('https://blog.csdn.net/ityard'))

```

**re.purge()** 清除正则表达式缓存。

#### 2.2.2 正则对象

来看一下正则表达式对象的相应方法。

**Pattern.search(string[, pos[, endpos]])** 扫描整个 string 寻找第一个匹配的位置，并返回一个相应的匹配对象，如果没有匹配，就返回 None；可选参数 pos 给出了字符串中开始搜索的位置索引，默认为 0；可选参数 endpos 限定了字符串搜索的结束。看一下示例：

```
import re

pattern = re.compile(r'bc', re.I)
print(pattern.search('aBcdef'))
print(pattern.search('aBcdef', 1, 3))

```

**Pattern.match(string[, pos[, endpos]])** 如果 string 的开始位置能够找到这个正则样式的任意个匹配，就返回一个相应的匹配对象，如果不匹配，就返回 None。看一下示例：

```
import re

pattern = re.compile(r'bc', re.I)
print(pattern.match('aBcdef'))
print(pattern.match('aBcdef', 1, 3))

```

**Pattern.fullmatch(string[, pos[, endpos]])** 如果整个 string 匹配这个正则表达式，就返回一个相应的匹配对象，否则就返回 None。看一下示例：

```
import re

pattern = re.compile(r'bc', re.I)
print(pattern.fullmatch('Bc'))
print(pattern.fullmatch('aBcdef', 1, 3))

```

**Pattern.split(string, maxsplit=0)** 等价于 re.split() 函数，使用了编译后的样式。看一下示例：

```
import re

pattern = re.compile(r'bc', re.I)
print(pattern.split('abc, aBcd, abcde.'))

```

**Pattern.findall(string[, pos[, endpos]])** 使用了编译后样式，可以接收可选参数 pos 和 endpos，限制搜索范围。看一下示例：

```
import re

pattern = re.compile(r'bc', re.I)
print(pattern.findall('abcefabCdeABC'))
print(pattern.findall('abcefabCdeABC', 0, 6))

```

**Pattern.finditer(string[, pos[, endpos]])** 使用了编译后样式，可以接收可选参数 pos 和 endpos ，限制搜索范围。看一下示例：

```
import re

pattern = re.compile(r'bc', re.I)
it = pattern.finditer('12bc34BC56', 0, 6)
for match in it:
    print(match)

```

**Pattern.sub(repl, string, count=0)** 使用了编译后的样式。看一下示例：

```
import re

pattern = re.compile(r'#.*$')
str = 'ityard # 是我的名字'
print(pattern.sub('', str))

```

**Pattern.subn(repl, string, count=0)** 使用了编译后的样式。看一下示例：

```
import re

pattern = re.compile(r'#.*$')
str = 'ityard # 是我的名字'
print(pattern.subn('', str))

```

#### 2.2.3 匹配对象

最后看一匹配对象的相应方法。

**Match.expand(template)** 对 template 进行反斜杠转义替换并且返回。看一下示例：

```
import re

match = re.match(r'(?P&lt;year&gt;\w+) (?P&lt;month&gt;\w+)','2020 01')
print(match.expand(r'现在是 \1 年 \2 月'))

```

**Match.group([group1, …])** 返回一个或者多个匹配的子组。看一下示例：

```
import re

match = re.match(r'(?P&lt;year&gt;\w+) (?P&lt;month&gt;\w+)','2020 01')
print(match.group(0))
print(match.group(1))
print(match.group(2))

```

**Match.groups(default=None)** 返回一个元组，包含所有匹配的子组，在样式中出现的从 1 到任意多的组合，default 参数用于不参与匹配的情况，默认为 None。看一下示例：

```
import re

match = re.match(r'(?P&lt;year&gt;\w+) (?P&lt;month&gt;\w+)','2020 01')
print(match.groups())

```

**Match.groupdict(default=None)** 返回一个字典，包含了所有的命名子组，default 参数用于不参与匹配的组合，默认为 None。看一下示例：

```
import re

match = re.match(r'(?P&lt;year&gt;\w+) (?P&lt;month&gt;\w+)','2020 01')
print(match.groupdict())

```

**Match.start([group])** 和 **Match.end([group])** 返回 group 匹配到的字串的开始和结束标号。看一下示例：

```
import re

match = re.match(r'(?P&lt;year&gt;\w+) (?P&lt;month&gt;\w+)','2020 01')
print(match.start())
print(match.end())

```

**Match.span([group])** 对于一个匹配 m，返回一个二元组 (m.start(group), m.end(group))。看一下示例：

```
import re

match = re.match(r'(?P&lt;year&gt;\w+) (?P&lt;month&gt;\w+)','2020 01')
print(match.span())

```

<img src="https://img-blog.csdnimg.cn/20200127132036938.png#pic_center" alt="" width="600">
