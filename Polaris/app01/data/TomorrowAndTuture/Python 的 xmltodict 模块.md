
--- 
title:  Python 的 xmltodict 模块 
tags: []
categories: [] 

---
哈哈，这好像是第三方依赖包，需要自己用 pip 去进行安装才可以使用的。

```
pip3 install xmltodict
```

至于这个模块是干什么的，其实看名字就能够猜到八九不离十。一般我们用 json、yaml 转换成 dict 可能多一些，xml 转到 dict 可能用得不多，不过，还是可以来看一看。

### xml 字符串解析

 先来个简单的 xml 瞧一瞧。

```
&lt;?xml version='1.0' encoding='utf-8'?&gt;
&lt;project&gt;
    &lt;artifact&gt;
        &lt;versionType&gt;BVersion&lt;/versionType&gt;
        &lt;repoType&gt;Generic&lt;/repoType&gt;
        &lt;id&gt;
            &lt;offering&gt;openEuler&lt;/offering&gt;
            &lt;version&gt;openEuler 1.1.T1.B010&lt;/version&gt;
        &lt;/id&gt;
        &lt;isClear&gt;Y&lt;/isClear&gt;

        &lt;copies&gt;
            &lt;copy&gt;
                &lt;source&gt;/dist&lt;/source&gt;
                &lt;dest&gt;&lt;/dest&gt;
            &lt;/copy&gt; 
        &lt;/copies&gt;
    &lt;/artifact&gt;
&lt;/project&gt;
```

解析 xml。 

```
import xmltodict
import json

xml_result = open('testdb.xml', 'r')
xml_dict = xmltodict.parse(xml_result.read())
print(type(xml_dict))
json_str = json.dumps(xml_dict, indent=2)
print(json_str)

```

输出结果（为了方便好看，我把结果字典字符串转换成了带缩进的形式），从下面结果可以看出，其实解析得到的字典是有序字典。

**你可能会问为什么是有序字典而不是普通字典呢？**

这个当然是为了让字典的顺序和 xml 元素的顺序保持一致（毕竟，xml 文件元素顺序变化了的话就已经不再是原来的那个 xml 文件了）。

```
&lt;class 'collections.OrderedDict'&gt;
{
  "project": {
    "artifact": {
      "versionType": "BVersion",
      "repoType": "Generic",
      "id": {
        "offering": "openEuler",
        "version": "openEuler 1.1.T1.B010"
      },
      "isClear": "Y",
      "copies": {
        "copy": {
          "source": "/dist",
          "dest": null
        }
      }
    }
  }
}
```

### dict 转成 xml 字符串

```
import xmltodict

xml_dict = {
  "project": {
    "artifact": {
      "versionType": "BVersion",
      "repoType": "Generic",
      "id": {
        "offering": "openEuler",
        "version": "openEuler 1.1.T1.B010"
      },
      "isClear": "Y",
      "copies": {
        "copy": {
          "source": "/dist",
          "dest": None
        }
      }
    }
  }
}

xml_str = xmltodict.unparse(xml_dict, pretty=True)
print(xml_str)

```

输出结果。

```
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;project&gt;
	&lt;artifact&gt;
		&lt;versionType&gt;BVersion&lt;/versionType&gt;
		&lt;repoType&gt;Generic&lt;/repoType&gt;
		&lt;id&gt;
			&lt;offering&gt;openEuler&lt;/offering&gt;
			&lt;version&gt;openEuler 1.1.T1.B010&lt;/version&gt;
		&lt;/id&gt;
		&lt;isClear&gt;Y&lt;/isClear&gt;
		&lt;copies&gt;
			&lt;copy&gt;
				&lt;source&gt;/dist&lt;/source&gt;
				&lt;dest&gt;&lt;/dest&gt;
			&lt;/copy&gt;
		&lt;/copies&gt;
	&lt;/artifact&gt;
&lt;/project&gt;
```

 
