
--- 
title:  Elasticsearch8 
tags: []
categories: [] 

---1. 官方文档： 1. kibana安装 1. IK分词器 1. 解决 elasticsearch 安装ik分词后各种闪退问题 1. Elasticsearch8入门 1.  其中的这个依赖
```
 &lt;dependency&gt;
      &lt;groupId&gt;com.fasterxml.jackson.core&lt;/groupId&gt;
      &lt;artifactId&gt;jackson-databind&lt;/artifactId&gt;
      &lt;version&gt;2.13.3&lt;/version&gt;
    &lt;/dependency&gt;

```

替换为： &lt;jakarta-json.version&gt;2.0.1&lt;/jakarta-json.version&gt;

```
        &lt;dependency&gt;
            &lt;groupId&gt;jakarta.json&lt;/groupId&gt;
            &lt;artifactId&gt;jakarta.json-api&lt;/artifactId&gt;
            &lt;version&gt;${jakarta-json.version}&lt;/version&gt;
        &lt;/dependency&gt;

```
1. 