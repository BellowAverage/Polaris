
--- 
title:  python3 使用 pygments 美化代码为html格式 
tags: []
categories: [] 

---
```
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

code = """
def hello_world():
    print('Hello, World!')
"""

# 使用 PythonLexer 进行语法高亮
lexer = PythonLexer()

# 使用 HtmlFormatter 进行美化，并指定背景颜色为白色
formatter = HtmlFormatter(style='colorful', noclasses=True, cssclass='', bg_color='#ffffff')

# 使用 highlight 函数进行代码高亮和美化
highlighted_code = highlight(code, lexer, formatter)

# 输出美化后的代码
print(highlighted_code)

```
- 输出
```
&lt;div style="background: #ffffff"&gt;&lt;pre style="line-height: 125%;"&gt;&lt;span&gt;&lt;/span&gt;&lt;span style="color: #008800; font-weight: bold"&gt;def&lt;/span&gt; &lt;span style="color: #0066BB; font-weight: bold"&gt;hello_world&lt;/span&gt;():
    &lt;span style="color: #007020"&gt;print&lt;/span&gt;(&lt;span style="background-color: #fff0f0"&gt;&amp;#39;Hello, World!&amp;#39;&lt;/span&gt;)
&lt;/pre&gt;&lt;/div&gt;

```

可以直接将代码粘贴在csdn的编辑器中

如下：

另外，需要设置csdn的代码片样式样式为白色背景 创作中心 &gt; 博客设置 &gt; 代码片样式
