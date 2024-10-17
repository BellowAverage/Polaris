
--- 
title:  Python3.12正式发布了 
tags: []
categories: [] 

---
来源 | OSC开源社区（ID：oschina2013)

Python 3.12.0 今日正式发布稳定版。

<img src="https://img-blog.csdnimg.cn/img_convert/2395757813d968452ccece2e9f86774b.png" alt="2395757813d968452ccece2e9f86774b.png">

**主要变化**
- 更灵活的 f-string 解析 (PEP 701)- 支持 buffer 协议 (PEP 688)- 引入新的 debugging/profiling API (PEP 669)- 支持具有单独全局解释器锁的独立子解释器 (PEP 684)- 优化性能，例如 PEP 709 和对 BOLT 二进制优化器的支持，预计总体性能提高 5%- 改进错误信息- 支持 Linux perf 分析器在跟踪过程中报告 Python 函数名称
**类型注释**
- 为泛型类引入新的类型注释语法 (PEP 695)- 为方法引入新的 override 装饰器 (PEP 698)
下面简单介绍值得关注的变化：

**更灵活的 f-string 解析 (PEP 701)**

新版取消了最初制定 f-strings 时制定的一些限制。经过这些变化，使得 f-strings 更加统一，成为一种可以直接整合到解析器中的正式化语法。这将会为终端用户和库开发者带来较大优势，同时也大大降低用于解析 f-strings 代码的维护成本。

最初设置 f-strings 限制是为了能够在不修改现有词法分析器的情况下将 f-strings 的解析实现到 CPython 中。但目前来看，这些限制反而带来了复杂性。比如：
<li>在表达式部分中，无法使用引号字符来界定 f-strings<pre class="has"><code class="language-go">&gt;&gt;&gt; f'Magic wand: { bag['wand'] }'
                             ^
SyntaxError: invalid syntax</code></pre></li><li>之前考虑过的一种解决方法会导致在执行的代码中出现转义序列，这在 f-strings 中是被禁止的：<pre class="has"><code class="language-go">&gt;&gt;&gt; f'Magic wand { bag[\'wand\'] } string'
SyntaxError: f-string expression portion cannot include a backslash</code></pre></li><li>f-strings 中无法使用注释语法：<pre class="has"><code class="language-go">&gt;&gt;&gt; f'''A complex trick: {
... bag['bag']  # recursive bags!
... }'''
SyntaxError: f-string expression part cannot include '#'</code></pre></li><li>许多其它语言表达式字符串插值都支持不扩展转义序列的任意嵌套。比如：<pre class="has"><code class="language-go"># Ruby
"#{ "#{1+2}" }"

# JavaScript
`${`${1+2}`}`

# Swift
"\("\(1+2)")"

# C#
$"{$"{1+2}"}"</code></pre></li>
Python 团队意识到，从语言用户的角度来看，这些限制没有任何意义，所以他们目前通过赋予 f-strings 字面量一个没有例外的常规语法，并使用专用的解析代码来实现它，从而消除这些限制。

f-strings 的另一个问题是，CPython 中的当前实现依赖于将 f-strings 标记化为 STRING 令牌，并对这些令牌进行后处理。这带来了以下问题：
1. 它给 CPython 解析器增加了相当大的维护成本。这是因为解析代码需要手动编写，这在历史上导致了大量的不一致性和错误。在 C 中手动编写和维护解析代码一直被认为是容易出错和危险的，因为它需要处理大量的原始词法分析器缓冲区上的手动内存管理。1. f-strings 解析代码无法使用新的 PEG 解析器所允许的新错误消息机制，这些错误消息带来的改进已经受到了热烈欢迎，但因为 f-strings 用的是独立解析器，所以无法使用上新改进的错误消息机制。另外，因为 f-strings 有几个语法特性可能会因为在表达式部分内部发生的不同隐式标记化而令人困惑（例如 `f"{y:=3}"` 并不是一个赋值表达式）。1. 其它 Python 实现无法知道它们是否正确实现了 f-strings，因为它们并不是官方 Python 语法的一部分。这一点很重要，因为有几个知名的替代实现正在使用 CPython 的 PEG 解析器，如 PyPy。f-strings 使用一个独立的解析器，阻止了这些替代实现利用官方语法，以及从改进的错误消息机制中受益。
期待新 f-strings 能用得更顺心。

**给每个子解释器创建 GIL (PEP 684)**

<img src="https://img-blog.csdnimg.cn/img_convert/03c246b33d0470d8d2a74151dacc7139.png" alt="03c246b33d0470d8d2a74151dacc7139.png">

PEP-684 由“香农计划”的作者 Eric Snow 提出，主要是给每个子解释器创建 GIL，允许 Python 实现真正的并行处理。

说到并行处理，目前 Python 3.12 尚未引入「**no-GIL 构建**」。

按照计划，Python 团队会在 Python 3.13 中将 no-GIL 构建添加为实验性构建模式。










