
--- 
title:  查询Bool 为空 和 为false 的情况 
tags: []
categories: [] 

---
## 查询Bool 为空 和 为false 的情况

记录下遇到的问题（二）

前情提要：数据库的bool型字段有true,false,null 三种情况，现要查询为null和false的情况。使用**ExampleMatcher**没写出来

### 使用Specification

```
Specification specification = (root, query, builder) -&gt; {
	List&lt;Predicate&gt; list = new ArrayList&lt;&gt;();
	if (instanceDto.getBoolObject!=null){
    	Predicate predicate;
    	if(instanceDto.getBoolObject) {
    		predicate = builder.isTrue(root.get("boolObject"));
    	}else {
    		predicate = builder.or(builder.isFalse(root.get("boolObject")),builder.isNull(root.get("boolObject")));
    	}
    	list.add(predicate);
    }
    Predicate[] o = new Predicate[list.size()];
    Predicate andPredicate = builder.and(list.toArray(o));
    return andPredicate;
};


```

对应的SQL类似这样的0_0

```
SELECT
	count( tableName.aimField ) AS col_0_0_ 
FROM
	tableName
WHERE
	tableName.aimField = 0 
	OR tableName.aimField IS NULL

```

新手上路，还请多多指教，目前只会用，不了解具体的而实现。
