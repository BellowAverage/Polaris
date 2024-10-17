
--- 
title:  Go 之 gotable 格式化打印表格 
tags: []
categories: [] 

---
Github 链接：

gotable是一个第三方库，虽然一些复杂功能可能还不完善，但是对于简单的展示还是不成问题的。安装这些就不多说了，直接上例子吧。

### 示例

```
package main

import (
	"fmt"
	"github.com/liushuochen/gotable"
)

func main() {
	title := []string{"id", "name", "phone", "age", "sex", "description"}
	content := make([][]string, 0)
	content = append(content, []string{"1", "zhangsan", "132****2889", "25", "M", "NoDesc"})
	content = append(content, []string{"3", "lisi", "152****7873", "18", "F", "None"})
	content = append(content, []string{"5", "wangwu", "136****2908", "25", "M", "Nothing"})
	content = append(content, []string{"10", "zhaoliu", "138****5322", "15", "M", "Nothing"})
	table, err := gotable.Create(title...) // 根据title先创建空表
	if err != nil {
		fmt.Println("Create table failed:" + err.Error())
	}
	for i := 0; i &lt; len(content); i++ {
		table.AddRow(content[i]) // 添加数据
	}

	fmt.Println(table)
	fmt.Println(table.HasColumn("name"))       // 列存在性判断
	fmt.Println("columns:", table.GetColumns()) // 获取列名（也即title）
	fmt.Println("length:", table.Length())      // 获取数据条数
	table.AddColumn("create_time")            // 添加新列
	table.Align("name", 1)               // 设置对齐方式。0 居中, 1 左对齐, 2 右对齐
	// table.CloseBorder()            // 去掉边框
	// table.OpenBorder()             // 加上边框
	// table.Clear() // 清除表格
	fmt.Println("empty?:", table.Empty())   // 为空判断
	table.ToCSVFile("test.csv")             // 写入 csv 文件
	table.ToJsonFile("test.json", 2) // 写入 json 文件
	fmt.Println(table.XML(2))             // 输出 xml
	json, err := table.JSON(2)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(json)                           // 输出 json
}

```

### 输出

```
+----+----------+-------------+-----+-----+-------------+
| id |   name   |    phone    | age | sex | description |
+----+----------+-------------+-----+-----+-------------+
| 1  | zhangsan | 132****2889 | 25  |  M  |   NoDesc    |
| 3  |   lisi   | 152****7873 | 18  |  F  |    None     |
| 5  |  wangwu  | 136****2908 | 25  |  M  |   Nothing   |
| 10 | zhaoliu  | 138****5322 | 15  |  M  |   Nothing   |
+----+----------+-------------+-----+-----+-------------+

true
columns: [id name phone age sex description]
length: 4
empty?: false
&lt;?xml version="1.0" encoding="utf-8" standalone="yes"?&gt;
&lt;table&gt;
  &lt;row&gt;
    &lt;age&gt;25&lt;/age&gt;
    &lt;sex&gt;M&lt;/sex&gt;
    &lt;description&gt;NoDesc&lt;/description&gt;
    &lt;id&gt;1&lt;/id&gt;
    &lt;name&gt;zhangsan&lt;/name&gt;
    &lt;create_time&gt;&lt;/create_time&gt;
    &lt;phone&gt;132****2889&lt;/phone&gt;
  &lt;/row&gt;
  &lt;row&gt;
    &lt;name&gt;lisi&lt;/name&gt;
    &lt;phone&gt;152****7873&lt;/phone&gt;
    &lt;age&gt;18&lt;/age&gt;
    &lt;sex&gt;F&lt;/sex&gt;
    &lt;description&gt;None&lt;/description&gt;
    &lt;create_time&gt;&lt;/create_time&gt;
    &lt;id&gt;3&lt;/id&gt;
  &lt;/row&gt;
  &lt;row&gt;
    &lt;age&gt;25&lt;/age&gt;
    &lt;sex&gt;M&lt;/sex&gt;
    &lt;description&gt;Nothing&lt;/description&gt;
    &lt;id&gt;5&lt;/id&gt;
    &lt;name&gt;wangwu&lt;/name&gt;
    &lt;phone&gt;136****2908&lt;/phone&gt;
    &lt;create_time&gt;&lt;/create_time&gt;
  &lt;/row&gt;
  &lt;row&gt;
    &lt;description&gt;Nothing&lt;/description&gt;
    &lt;create_time&gt;&lt;/create_time&gt;
    &lt;id&gt;10&lt;/id&gt;
    &lt;name&gt;zhaoliu&lt;/name&gt;
    &lt;phone&gt;138****5322&lt;/phone&gt;
    &lt;age&gt;15&lt;/age&gt;
    &lt;sex&gt;M&lt;/sex&gt;
  &lt;/row&gt;
&lt;/table&gt;
[
   {
      "age": "25",
      "create_time": "",
      "description": "NoDesc",
      "id": "1",
      "name": "zhangsan",
      "phone": "132****2889",
      "sex": "M"
   },
   {
      "age": "18",
      "create_time": "",
      "description": "None",
      "id": "3",
      "name": "lisi",
      "phone": "152****7873",
      "sex": "F"
   },
   {
      "age": "25",
      "create_time": "",
      "description": "Nothing",
      "id": "5",
      "name": "wangwu",
      "phone": "136****2908",
      "sex": "M"
   },
   {
      "age": "15",
      "create_time": "",
      "description": "Nothing",
      "id": "10",
      "name": "zhaoliu",
      "phone": "138****5322",
      "sex": "M"
   }
]
```

test.csv

```
id,name,phone,age,sex,description,create_time
1,zhangsan,132****2889,25,M,NoDesc,
3,lisi,152****7873,18,F,None,
5,wangwu,136****2908,25,M,Nothing,
10,zhaoliu,138****5322,15,M,Nothing,

```

test.json

```
[
   {
      "age": "25",
      "create_time": "",
      "description": "NoDesc",
      "id": "1",
      "name": "zhangsan",
      "phone": "132****2889",
      "sex": "M"
   },
   {
      "age": "18",
      "create_time": "",
      "description": "None",
      "id": "3",
      "name": "lisi",
      "phone": "152****7873",
      "sex": "F"
   },
   {
      "age": "25",
      "create_time": "",
      "description": "Nothing",
      "id": "5",
      "name": "wangwu",
      "phone": "136****2908",
      "sex": "M"
   },
   {
      "age": "15",
      "create_time": "",
      "description": "Nothing",
      "id": "10",
      "name": "zhaoliu",
      "phone": "138****5322",
      "sex": "M"
   }
]
```
