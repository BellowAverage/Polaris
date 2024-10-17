
--- 
title:  Py之py2neo：py2neo的简介、安装、使用方法之详细攻略 
tags: []
categories: [] 

---
 Py之py2neo：py2neo的简介、安装、使用方法之详细攻略





**目录**













## **<strong><strong>py2neo的简介**</strong></strong>

       **<strong><strong>py2neo**</strong></strong>是一个客户端库和工具包，用于在Python应用程序中使用Neo4j。该库同时支持Bolt和HTTP，并提供了高级API、OGM、管理工具、用于py鸣叫的Cypher lexer，以及许多其他附加功能。        命令行工具已从py2neo 2021.2的库中移除。这个功能现在存在于单独的ipy2neo项目中。从2021.1版本开始，py2neo包含了对路由的完全支持，这是由Neo4j集群公开的。这可以使用neo4j://…URI或通过将routing=True传递给Graph构造函数。





## **<strong><strong>py2neo的安装**</strong></strong>

```
conda install py2neo
```



<img alt="" height="121" src="https://img-blog.csdnimg.cn/7b6c64b57e284cdb820640db9fabc2b1.png" width="1200">





## **<strong><strong>py2neo的使用方法**</strong></strong>

### **<strong><strong>1、基础用法**</strong></strong>

```
from py2neo import Graph
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))
graph.run("UNWIND range(1, 3) AS n RETURN n, n * n as n_sq")
```




