
--- 
title:  FastJSON 使用个人笔记 
tags: []
categories: [] 

---
### 如何全局配置 fastdfs 的策略

>  
 在mvc里面实现全局的fastdfs的全局序列化 


```
	/*
     * 解决序列问题
     * */
    @Override
    public void configureMessageConverters(List&lt;HttpMessageConverter&lt;?&gt;&gt; converters) {<!-- -->
        FastJsonHttpMessageConverter fastJsonConverter = new FastJsonHttpMessageConverter();
        FastJsonConfig fjc = new FastJsonConfig();
        // 配置序列化策略
        fjc.setSerializerFeatures(
                //将中文都会序列化为uXXXX格式，字节数会多一些，但是能兼容IE 6，默认为false
                SerializerFeature.BrowserCompatible,
                //List字段如果为null,输出为[],而非null
                SerializerFeature.WriteNullListAsEmpty,
                //字符类型字段如果为null,输出为”“,而非null
                SerializerFeature.WriteNullStringAsEmpty,
                //全局修改时间
                SerializerFeature.WriteDateUseDateFormat
        );
        fjc.setDateFormat(DateTimeUtil.FULL_FORMAT);
        fastJsonConverter.setFastJsonConfig(fjc);
        converters.add(fastJsonConverter);
    }

```

**常用FastJSON的SerializerFeature特性及日期转换格式**

```
SerializerFeature.PrettyFormat:格式化输出
SerializerFeature.WriteMapNullValue:是否输出值为null的字段,默认为false
SerializerFeature.DisableCircularReferenceDetect:消除循环引用
SerializerFeature.WriteNullStringAsEmpty:将为null的字段值显示为""
WriteNullListAsEmpty：List字段如果为null,输出为[],而非null
WriteNullNumberAsZero：数值字段如果为null,输出为0,而非null
WriteNullBooleanAsFalse：Boolean字段如果为null,输出为false,而非null
SkipTransientField：如果是true，类中的Get方法对应的Field是transient，序列化时将会被忽略。默认为true
SortField：按字段名称排序后输出。默认为false
WriteDateUseDateFormat：全局修改日期格式,默认为false。JSON.DEFFAULT_DATE_FORMAT = “yyyy-MM-dd”;JSON.toJSONString(obj, SerializerFeature.WriteDateUseDateFormat);
BeanToArray：将对象转为array输出
QuoteFieldNames：输出key时是否使用双引号,默认为true
UseSingleQuotes：输出key时使用单引号而不是双引号,默认为false（经测试，这里的key是指所有的输出结果，而非key/value的key,而是key,和value都使用单引号或双引号输出）

```

**常用日期格式**

```
YYYY-MM-dd'T'HH:mm:ssXXX  + SerializerFeature.WriteDateUseDateFormat  =  SerializerFeature.UseISO8601DateFormat
YYYY-MM-dd'T'HH:mm:ss:sssZ
YYYY-MM-dd'T'HH:mm:ss:sss'Z'
YYYY-MM-dd'T'HH:mm:ss:sssXXX
YYYY-MM-dd HH:mm:ss

```

### 指定转换的详细格式

```
Map&lt;String, List&lt;DepartmentTreeVo&gt;&gt; groupingMap = JSON.parseObject(
         futures.get(1).get(),
         new TypeReference&lt;Map&lt;String, List&lt;DepartmentTreeVo&gt;&gt;&gt;() {<!-- -->
         }
);

```
