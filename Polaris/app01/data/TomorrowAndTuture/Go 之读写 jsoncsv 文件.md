
--- 
title:  Go 之读写 json/csv 文件 
tags: []
categories: [] 

---
## 读写字典型json

### 读取 json 文件

test.json

```
{
	"user_name": "root",
	"password": "xxx",
	"host": "localhost",
	"port": "3306",
	"dbname": "test",
	"table_name": "table"
}
```

```
package main

import (
	"encoding/json"
	"fmt"
	io "io/ioutil"
	"sync"
)


//定义配置文件解析后的结构
type UserInfo struct {
	UserName  string `json:"user_name"`
	Password  string `json:"password"`
	Host      string `json:"host"`
	Port      string `json:"port"`
	DbName    string `json:"dbname"`
	TableName string `json:"table_name"`
}
var UserIn UserInfo
var file_locker sync.Mutex //config file locker

func LoadConfig(filename string) (UserInfo, bool) {
	var conf UserInfo
	file_locker.Lock()
	data, err := io.ReadFile(filename) //read config file
	file_locker.Unlock()
	if err != nil {
		fmt.Println("read json file error")
		return conf, false
	}
	err = json.Unmarshal(data, &amp;conf)
	if err != nil {
		fmt.Println("unmarshal json file error")
		return conf, false
	}
	return conf, true
}

func main() {
	conf, ok := LoadConfig("./test.json")
	if !ok {
		fmt.Println("load config failed")
		return
	}
	fmt.Println(conf)	// {root xxx localhost 3306 test table}
	fmt.Println(conf.UserName)	// root
	fmt.Println(conf.Host)	// localhost
}

```

### 生成 json 文件

```
package main

import (
	"encoding/json"
	"os"
)


//定义配置文件解析后的结构
type UserInfo struct {
	UserName  string `json:"user_name"`
	Password  string `json:"password"`
	Host      string `json:"host"`
	Port      string `json:"port"`
	DbName    string `json:"dbname"`
	TableName string `json:"table_name"`
}

func DumpConfig(filename string)  {
	fp, err := os.Create(filename)
	if err != nil{
		panic(err)
	}
	defer fp.Close()
	config :=  UserInfo{"Looking", "xxx", "localhost",
		"5435", "postgres", "table"}
	//data, err := json.Marshal(config)
	data, err := json.MarshalIndent(config, "", "\t") // 带缩进的美化版
	if err != nil {
		panic(err)
	}
	fp.Write(data)
}

func main() {
	DumpConfig("test.json")
}
```

test.json

```
{
	"user_name": "Looking",
	"password": "xxx",
	"host": "localhost",
	"port": "5435",
	"dbname": "postgres",
	"table_name": "table"
}
```

## 读写数组型json

### 读取 json 文件

test.json

```
[
	{
		"user_name": "Looking1",
		"password": "xxx",
		"host": "localhost",
		"port": "5435",
		"dbname": "postgres",
		"table_name": "table"
	},
	{
		"user_name": "Looking2",
		"password": "xxx",
		"host": "localhost",
		"port": "5435",
		"dbname": "postgres",
		"table_name": "table"
	}
]
```

```
package main

import (
	"encoding/json"
	"fmt"
	io "io/ioutil"
	"sync"
)

//定义配置文件解析后的结构
type UserInfo struct {
	UserName  string `json:"user_name"`
	Password  string `json:"password"`
	Host      string `json:"host"`
	Port      string `json:"port"`
	DbName    string `json:"dbname"`
	TableName string `json:"table_name"`
}

var UserIn UserInfo
var file_locker sync.Mutex //config file locker

func LoadConfig(filename string) ([]UserInfo, bool) {
	var conf []UserInfo
	file_locker.Lock()
	data, err := io.ReadFile(filename) //read config file
	file_locker.Unlock()
	if err != nil {
		fmt.Println("read json file error")
		return conf, false
	}
	err = json.Unmarshal(data, &amp;conf)
	if err != nil {
		fmt.Println("unmarshal json file error")
		return conf, false
	}
	return conf, true
}

func main() {
	conf, ok := LoadConfig("./test.json")
	if !ok {
		fmt.Println("load config failed")
		return
	}
	fmt.Println(conf)	// [{Looking1 xxx localhost 5435 postgres table} {Looking2 xxx localhost 5435 postgres table}]
	for _, row := range conf{
		fmt.Println(row)
		//{Looking1 xxx localhost 5435 postgres table}
		//{Looking2 xxx localhost 5435 postgres table}
	}
}

```

### 生成 json 文件

```
package main

import (
	"encoding/json"
	"os"
)

//定义配置文件解析后的结构
type UserInfo struct {
	UserName  string `json:"user_name"`
	Password  string `json:"password"`
	Host      string `json:"host"`
	Port      string `json:"port"`
	DbName    string `json:"dbname"`
	TableName string `json:"table_name"`
}
func DumpConfig(filename string)  {
	fp, err := os.Create(filename)
	if err != nil{
		panic(err)
	}
	defer fp.Close()
	config := []UserInfo{}
	config = append(config, UserInfo{"Looking1", "xxx", "localhost",
		"5435", "postgres", "table"})
	config = append(config, UserInfo{"Looking2", "xxx", "localhost",
		"5435", "postgres", "table"})
	//data, err := json.Marshal(config)
	data, err := json.MarshalIndent(config, "", "\t") // 带缩进的美化版
	if err != nil {
		panic(err)
	}
	fp.Write(data)
}

func main() {
	DumpConfig("test.json")
}
```

test.json

```
[
	{
		"user_name": "Looking1",
		"password": "xxx",
		"host": "localhost",
		"port": "5435",
		"dbname": "postgres",
		"table_name": "table"
	},
	{
		"user_name": "Looking2",
		"password": "xxx",
		"host": "localhost",
		"port": "5435",
		"dbname": "postgres",
		"table_name": "table"
	}
]
```

## 读写csv文件

```
package main

import (
	"encoding/csv"
	"fmt"
	"os"
)

func main() {
	filename := "test.csv"
	err := WriteCsv(filename)
	if err != nil {
		fmt.Println("write csv error: ", err)
	}

	err = ReadCsv(filename)
	if err != nil {
		fmt.Println("read csv error: ", err)
	}
}

func WriteCsv(filename string) error {
	f, err := os.Create(filename) // 创建文件
	if err != nil {
		return err
	}
	defer f.Close()

	_, err = f.WriteString("\xEF\xBB\xBF") // 写入UTF-8 BOM
	if err != nil {
		return err
	}

	w := csv.NewWriter(f) // 创建一个新的写入文件流
	data := [][]string{
		{"Name", "Age", "Phone"},
		{"Looking", "23", "111"},
		{"test", "32", "222"},
	}
	err = w.WriteAll(data) // 写入数据
	if err != nil {
		return err
	}
	w.Flush()
	return nil
}

func ReadCsv(filename string) error {
	f, err := os.Open(filename) // 以只读方式打开csv文件
	if err != nil {
		return err
	}
	defer f.Close()

	reader := csv.NewReader(f)
	records, err := reader.ReadAll() // 读取全部数据记录
	if err != nil {
		return err
	}

	// fmt.Printf("records:%#v\n", records)
	for _, record := range records {
		for _, value := range record {
			fmt.Printf("%s ", value)
		}
		fmt.Println()
	}
	return nil
}

```


