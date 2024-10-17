
--- 
title:  成功解决TypeError: cannot unpack non-iterable TargetPlot object 
tags: []
categories: [] 

---
成功解决TypeError: cannot unpack non-iterable TargetPlot object







**目录**

















## **解决问题**

fig, axes, summary_df = info_plots.TargetPlot(df=titanic_df, feature=col_plot, TypeError: cannot unpack non-iterable TargetPlot object







## **解决思路**

类型错误:无法解包不可迭代的TargetPlot对象







## **解决方法**

错误表明 info_plots.TargetPlot 函数没有返回三个值（fig, axes, summary_df），而是返回了一个 TargetPlot 对象。

查看源代码：

首先，请确保 TargetPlot 函数确实应该返回三个值。如果你查看 pdpbox 的文档或源代码，你应该能够找到确切的信息。如果 TargetPlot 函数只返回一个对象，那么你不能使用 fig, axes, summary_df = 来解包它。

&gt;&gt; 如果 TargetPlot 函数确实应该返回三个值，那么你可能需要检查 pdpbox 库的版本，因为可能存在 bug 或者函数行为在不同的版本中有所不同。尝试更新 pdpbox 到最新版本，或者查看是否有任何相关的 GitHub 问题或库文档说明。 &gt;&gt; 如果 TargetPlot 函数返回的确实只是一个对象，你需要根据库的文档来正确地处理这个对象。这可能意味着你需要使用不同的方式来访问 fig, axes, 和 summary_df。

例如，如果 TargetPlot 返回的是一个字典，你可能需要这样做：

```
result = info_plots.TargetPlot(df=titanic_df, feature=col_plot)
fig = result['fig']
axes = result['axes']
summary_df = result['summary_df']
```
















