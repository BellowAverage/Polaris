
--- 
title:  Guava-个人笔记 
tags: []
categories: [] 

---
### String转List

```
//string "1345434554,23545354,3354534"
//转List&lt;Long&gt;
List&lt;Long&gt; idList = Splitter
                .on(",")
                .splitToList(ids)
                .stream()
                .mapToLong(Long::parseLong)
                .boxed()
                .collect(Collectors.toList());
                

```
