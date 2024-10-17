
--- 
title:  No serializer found for class cn.hutool.json.JSONNull and no properties discovered to create 
tags: []
categories: [] 

---
### 问题记录：

调用第三方接口进行json解析时出现了：No serializer found for class cn.hutool.json.JSONNull and no properties discovered to create BeanSerializer (to avoid exception, disable SerializationFeature.FAIL_ON_EMPTY_BEANS) (through reference chain: com.ncist.common.api.vo.Result[“data”]-&gt;cn.hutool.json.JSONObject[“data”]-&gt;cn.hutool.json.JSONObject[“vehicle_list”]-&gt;cn.hutool.json.JSONArray[0]-&gt;cn.hutool.json.JSONObject[“vehicle_std_item”]-&gt;cn.hutool.json.JSONArray[0]-&gt;cn.hutool.json.JSONObject[“desc”])

```
http-nio-9003-exec-5           20230802 20:20:40.025 ERROR traceId=[] org.apache.catalina.core.ContainerBase.[Tomcat].[localhost].[/logistics].[dispatcherServlet] - Servlet.service() for servlet [dispatcherServlet] in context with path [/logistics] threw exception [Request processing failed; nested exception is org.springframework.http.converter.HttpMessageConversionException: Type definition error: [simple type, class cn.hutool.json.JSONNull]; nested exception is com.fasterxml.jackson.databind.exc.InvalidDefinitionException: No serializer found for class cn.hutool.json.JSONNull and no properties discovered to create BeanSerializer (to avoid exception, disable SerializationFeature.FAIL_ON_EMPTY_BEANS) (through reference chain: com.ncist.common.api.vo.Result["data"]-&gt;cn.hutool.json.JSONObject["data"]-&gt;cn.hutool.json.JSONObject["vehicle_list"]-&gt;cn.hutool.json.JSONArray[0]-&gt;cn.hutool.json.JSONObject["vehicle_std_item"]-&gt;cn.hutool.json.JSONArray[0]-&gt;cn.hutool.json.JSONObject["desc"])] with root cause
com.fasterxml.jackson.databind.exc.InvalidDefinitionException: No serializer found for class cn.hutool.json.JSONNull and no properties discovered to create BeanSerializer (to avoid exception, disable SerializationFeature.FAIL_ON_EMPTY_BEANS) (through reference chain: com.ncist.common.api.vo.Result["data"]-&gt;cn.hutool.json.JSONObject["data"]-&gt;cn.hutool.json.JSONObject["vehicle_list"]-&gt;cn.hutool.json.JSONArray[0]-&gt;cn.hutool.json.JSONObject["vehicle_std_item"]-&gt;cn.hutool.json.JSONArray[0]-&gt;cn.hutool.json.JSONObject["desc"])
	at com.fasterxml.jackson.databind.exc.InvalidDefinitionException.from(InvalidDefinitionException.java:77)
	at com.fasterxml.jackson.databind.SerializerProvider.reportBadDefinition(SerializerProvider.java:1277)
	at com.fasterxml.jackson.databind.DatabindContext.reportBadDefinition(DatabindContext.java:400)
	at com.fasterxml.jackson.databind.ser.impl.UnknownSerializer.failForEmpty(UnknownSerializer.java:71)
	at com.fasterxml.jackson.databind.ser.impl.UnknownSerializer.serialize(UnknownSerializer.java:33)
	at com.fasterxml.jackson.databind.ser.std.MapSerializer.serializeFields(MapSerializer.java:726)
	at com.fasterxml.jackson.databind.ser.std.MapSerializer.serializeWithoutTypeInfo(MapSerializer.java:681)
	at com.fasterxml.jackson.databind.ser.std.MapSerializer.serialize(MapSerializer.java:637)
	at com.fasterxml.jackson.databind.ser.std.MapSerializer.serialize(MapSerializer.java:33)
	at com.fasterxml.jackson.databind.ser.impl.IndexedListSerializer.serializeContents(IndexedListSerializer.java:119)
	at com.fasterxml.jackson.databind.ser.impl.IndexedListSerializer.serialize(IndexedListSerializer.java:79)

```

我使用的代码是：

```
 JSONObject jsonObject = JSONUtil.parseObj(post);

```

### 解释：

Hutool会使用JSONNull来表示空值，而SpringBoot默认使用的序列化是Jackson，在接口调用过程中使用了Map，直接传入了Hutool的JSONObject，而该Map存在空值，所以存在JSONNull，最终导致错误。

### 修改：

使用 com.alibaba.fastjson 来解析：

```
com.alibaba.fastjson.JSONObject jsonObject = com.alibaba.fastjson.JSONObject.parseObject(gpString);

```
