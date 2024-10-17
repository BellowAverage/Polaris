
--- 
title:  [java]JsonObject与JsonArray转换 
tags: []
categories: [] 

---
备忘一下，首先 这是一个JsonArrayStr，他可以转换为**JsonArray**。

```
[{"name":"a1"},{"name":"a2"}]

```

这是一个JsonObjectStr，他可以转换为**JsonObject**。

```
{"result":[{"name":"a1"},{"name":"a2"}]}

```

#### JsonObject转换为java对象、JsonArray转换为Java对象

JsonObject的value为JsonArray，对应的java类型为List。在案例中，java代码如下（这里用的内部类）

```
@Data
@AllArgsConstructor
@NoArgsConstructor
class AList{<!-- -->
    private List&lt;PersonA&gt; result;
}

@Data
@AllArgsConstructor
@NoArgsConstructor
class PersonA{<!-- -->
    private String name;
}

```
- 使用fastjson转换jsonStr为java对象，完整代码如下
```

public class JsonTest {<!-- -->

    public static void main(String[] args) {<!-- -->

        String strArray  ="[{\"name\":\"a1\"},{\"name\":\"a2\"}]";
        String strObject  ="{\"result\":[{\"name\":\"a1\"},{\"name\":\"a2\"}]}";
        // parseArray保证属性key一致即可正确转换
        List&lt;PersonA&gt; personAList = JSON.parseArray(strArray, PersonA.class);
        // parseObject需要保证属性key一致即可正确转换
        AList aList = JSON.parseObject(strObject, AList.class);

    }
}

@Data
@AllArgsConstructor
@NoArgsConstructor
class AList{<!-- -->

    private List&lt;PersonA&gt; result;

}

@Data
@AllArgsConstructor
@NoArgsConstructor
class PersonA{<!-- -->
    private String name;
}


```
- 使用hutool转换jsonStr为java对象，核心代码如下
```
 List&lt;PersonA&gt; personAList = JSONUtil.toList(JSONUtil.parseArray(strArray), PersonA.class);

```

#### JsonArray转换为JsonObject

已知一个JsonArrayStr，内容为。

```
[{"name":"a1"},{"name":"a2"}]

```

不可以直接parseObject，JsonObject格式为{},且含有键值对。 使用以下方法将JsonArrayStr转换为JsonObject对象:
- 使用fastjson
```
        JSONArray array = JSON.parseArray(strArray);
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("result",array);

```
- 使用hutool
```
        JSONArray array = JSONUtil.parseObj(strArray);;
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("result",array);

```

即将JsonArrayStr转换为JsonObjectStr

```
{"result":[{"name":"a1"},{"name":"a2"}]}

```

<s>真的搞不懂，为什么上游传一个json值下来，直接传一个object不行么？不行么？不行么？？？？？？？</s>

#### JsonArrayStr 转换为 JsonObjectStr

有什么好说的，加括号，加键。 推荐使用hutool的StrUtil.wrap()

```
        String strArray = "[{\"name\":\"a1\"},{\"name\":\"a2\"}]";
        String strObject  = StrUtil.wrap(strArray, "{\"result\":", "}");

```

最后得到的值为

```
{"result":[{"name":"a1"},{"name":"a2"}]}

```
