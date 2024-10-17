
--- 
title:  gorm框架之常用增删改查(CRUD) 
tags: []
categories: [] 

---
最好的文档其实是官方指导手册，大家可以参考这个文档链接，本文也只是个搬运工：



## 数据表初始化

为了边学边练习，我自己下载了一个 postgres 作为示例（**mysql 也可以连，关心 mysql 连接的话可以关注下注释部分**），然后使用 gorm 进行连接处理。为了简化，所有 go 代码都写在了一个文件，自测能成功运行。

### main.go

```
package main

import (
	"fmt"
	"os"
	"strings"

	// "gorm.io/driver/mysql"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

// User model
type User struct {
	Id      int    `gorm:"column:id;primarykey" json:"id"`
	Name    string `gorm:"column:name;index:,unique" json:"name"`
	Age     int8   `gorm:"column:age" json:"age"`
	Mailbox string `gorm:"column:mailbox" json:"mailbox"`
	Comment string `gorm:"column:comment" json:"comment"`
}

func (u *User) TableName() string {
	return "users"
}

type Database struct {
	Host         string
	DBName       string
	Username     string
	Password     string
	Port         int
	MaxIdleConns int
	MaxOpenConns int
}

func getDatabaseConf() *Database {
	// return &amp;Database{
	// 	Host:         "127.0.0.1",
	// 	DBName:       "mysql",
	// 	Username:     "root",
	// 	Password:     "A1234512345",
	// 	Port:         3306,
	// 	MaxIdleConns: 5,
	// 	MaxOpenConns: 10,
	// }
	return &amp;Database{
		Host:         "127.0.0.1",
		DBName:       "postgres",
		Username:     "postgres",
		Password:     "123456",
		Port:         5432,
		MaxIdleConns: 5,
		MaxOpenConns: 10,
	}
}

func connect(conf *Database) (*gorm.DB, error) {
	var (
		err error
	)

	// dsn := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=utf8", conf.Username, conf.Password, conf.Host, conf.Port, conf.DBName)
	// gormDB, err := gorm.Open(mysql.Open(dsn))
	dsn := fmt.Sprintf("postgres://%s:%s@%s:%d/%s", conf.Username, conf.Password, conf.Host, conf.Port, conf.DBName)
	gormDB, err := gorm.Open(postgres.Open(dsn))
	if err != nil {
		return nil, err
	}

	sqlDB, err := gormDB.DB()
	if err != nil {
		return nil, err
	}

	if err = sqlDB.Ping(); err != nil {
		return nil, err
	}

	sqlDB.SetMaxIdleConns(conf.MaxIdleConns)
	sqlDB.SetMaxOpenConns(conf.MaxOpenConns)

	return gormDB, nil
}
func initTable(db *gorm.DB, tables []interface{}) {
	for _, table := range tables {
		if err := db.AutoMigrate(table); err != nil {
			if !strings.Contains(err.Error(), "already exists") {
				panic(err)
			}
		}
	}
}

func main() {
	conf := getDatabaseConf()
	connDb, err := connect(conf)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	var tables = []interface{}{
		new(User),
	}
	initTable(connDb, tables)
}

```

### go.mod

（注意：如果你 go 版本不是很高的话，你对应引用 gorm 相关版本最好也不要太高，不然可能导致 package 各种不兼容）

```
module github.com/test

go 1.17

require (
	gorm.io/driver/postgres v1.4.5
	gorm.io/gorm v1.24.1-0.20221019064659-5dd2bb482755
)

require (
	github.com/jackc/chunkreader/v2 v2.0.1 // indirect
	github.com/jackc/pgconn v1.13.0 // indirect
	github.com/jackc/pgio v1.0.0 // indirect
	github.com/jackc/pgpassfile v1.0.0 // indirect
	github.com/jackc/pgproto3/v2 v2.3.1 // indirect
	github.com/jackc/pgservicefile v0.0.0-20221227161230-091c0ba34f0a // indirect
	github.com/jackc/pgtype v1.12.0 // indirect
	github.com/jackc/pgx/v4 v4.17.2 // indirect
	github.com/jinzhu/inflection v1.0.0 // indirect
	github.com/jinzhu/now v1.1.5 // indirect
	github.com/stretchr/testify v1.8.1 // indirect
	golang.org/x/crypto v0.14.0 // indirect
	golang.org/x/text v0.13.0 // indirect
)

```

## 新建（create）

### 新建单条记录

一般新建记录的话，我们主要关心的是 Error 信息，如果新建有报错信息的话，是需要我们返回错误进行处理。

```
func main() {
	conf := getDatabaseConf()
	db, err := connect(conf)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	// var tables = []interface{}{
	// 	new(User),
	// }
	// initTable(connDb, tables)
	user := User{Name: "Jinzhu", Age: 18, Mailbox: "test@qq.com", Comment: "test comment"}
	result := db.Create(&amp;user)
	if result.Error != nil { // 返回 error
		fmt.Println(result.Error)
        return
	}
	fmt.Println(user.Id)             // 2	返回插入数据得主键
	fmt.Println(result.RowsAffected) // 1	返回插入记录的条数
}

```

```
postgres=# select * from users;
 id |  name  | age |   mailbox   |   comment
----+--------+-----+-------------+--------------
  2 | Jinzhu |  18 | test@qq.com | test comment
(1 行记录)
```

### 新建多项记录

```
users := []*User{
	{Name: "test1", Age: 18, Mailbox: "test@qq.com", Comment: "test comment"},
	&amp;User{Name: "test2", Age: 18, Mailbox: "test@qq.com", Comment: "test comment"},
}
result := db.Create(users)
```

```
postgres=# select * from users;
 id |  name  | age |   mailbox   |   comment
----+--------+-----+-------------+--------------
  2 | Jinzhu |  18 | test@qq.com | test comment
  3 | test1  |  18 | test@qq.com | test comment
  4 | test2  |  18 | test@qq.com | test comment
(3 行记录)
```

**注意：**你无法向 ‘create’ 传递结构体，所以你应该传入数据的指针（也就是你数据表结构体实例对象取地址）。

### 用指定的字段创建记录

创建记录并为指定字段赋值。

```
user := User{Name: "test3", Age: 24, Mailbox: "test@qq.com", Comment: "test comment"}
result := db.Select("name", "mailbox").Create(&amp;user)
// INSERT INTO `users` (`name`,`mailbox`) VALUES ("test3", "test@qq.com")
```

```
postgres=# select * from users order by id desc;
 id |  name  | age |   mailbox   |   comment
----+--------+-----+-------------+--------------
  6 | test3  |     | test@qq.com |
```

创建记录并忽略传递给 ‘Omit’ 的字段值。有点和上面指定字段赋值取反的意思。

```
user := User{Name: "test3", Age: 24, Mailbox: "test@qq.com", Comment: "test comment"}
result := db.Omit("Name", "Mailbox").Create(&amp;user)
// INSERT INTO `users` (`age`,`comment`) VALUES (24, "test comment")

```

### 新建钩子Hook

用户可以自定义实现 `BeforeSave`, `BeforeCreate`, `AfterSave`, `AfterCreate 方法，然后在创建记录的时候通过设置 SkipHooks 为 false 进行调用。`

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	user := User{Name: "test5", Age: 24, Mailbox: "test@qq.com", Comment: "test comment"}
	db.Session(&amp;gorm.Session{SkipHooks: false}).Create(&amp;user) 
	// db.Create(&amp;user) 钩子默认启用，跳过的话设置参数 SkipHooks 为 true 即可。
}

func (u *User) BeforeCreate(tx *gorm.DB) (err error) {
	fmt.Println("before create")
	return
}

func (u *User) AfterCreate(tx *gorm.DB) (err error) {
	fmt.Println("after create")
	return
}

func (u *User) BeforeSave(tx *gorm.DB) (err error) {
	fmt.Println("before save")
	return
}

func (u *User) AfterSave(tx *gorm.DB) (err error) {
	fmt.Println("after save")
	return
}

```

```
before save
before create
after create
after save
```

### 根据Map进行创建

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	user := map[string]interface{}{
		"name": "test8",
		"Age": 24,
	}
	db.Model(&amp;User{}).Create(user)
}
```

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	users := []map[string]interface{}{
		{"Name": "test1", "Age": 19},
		{"Name": "test2", "Age": 20},
	}
	db.Model(&amp;User{}).Create(&amp;users)
}
```

### 默认值

一般来说，如果 Model 定义的时候没有特地指定默认值，新建记录的时候也没有给字段传递值，那么就会用对应字段的零值；如果定义 Model 的时候指定了默认值，新建的时候即使对应字段没有传值，也会使用 Model 中的默认值。如下面的 comment 和 mailbox 字段，新建用户时都未进行指定值，但创建的记录中 comment 使用了 model 中的默认值 hello world，而 mailbox 字段则直接使用了对应的零值空字符串。

```
// User model
type User struct {
	Id      int    `gorm:"column:id;primarykey" json:"id"`
	Name    string `gorm:"column:name;index:,unique" json:"name"`
	Age     int8   `gorm:"column:age" json:"age"`
	Mailbox string `gorm:"column:mailbox" json:"mailbox"`
	Comment string `gorm:"column:comment;default:hello world" json:"comment"`
}

```

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	// user := User{Name: "test1", Age: 25, Mailbox: "test@qq.com", Comment: "test comment"}
	user := User{Name: "test1", Age: 25}
	db.Create(&amp;user)
}

```

```
postgres=# select * from users order by id desc;
 id | name  | age | mailbox |   comment
----+-------+-----+---------+-------------
 39 | test1 |  25 |         | hello world
```

### Upsert 及冲突处理

Upsert 也即 Update、Insert 的合称。其实也是大家常用的，简单来说就是新建记录的时候，如果检测到对应列的数据已经存在的话（将冲突检测交给了组件），需要对原记录进行什么样的处理（比如替换全部，替换指定字段，什么都不替换，等等）。下面是一些常见示例。

#### 使用新值替换指定字段

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	user := User{Name: "test1", Age: 25, Mailbox: "test@qq.com", Comment: "test comment"}
	db.Create(&amp;user)

	user.Age = 26
	user.Mailbox = "new@qq.com"
	user.Comment = "new comment"
	db.Clauses(clause.OnConflict{
		Columns:  []clause.Column{<!-- -->{Name: "name"}},
		DoUpdates: clause.AssignmentColumns([]string{"age", "mailbox"}),
	}).Create(&amp;user)
}

```

```
postgres=# select * from users order by id desc;
 id | name  | age |  mailbox   |   comment
----+-------+-----+------------+--------------
 32 | test1 |  26 | new@qq.com | test comment
```

#### 用自定义的值替换指定字段

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	user := User{Name: "test1", Age: 25, Mailbox: "test@qq.com", Comment: "test comment"}
	db.Create(&amp;user)

	user.Age = 26
	user.Mailbox = "new@qq.com"
	user.Comment = "new comment"
	db.Clauses(clause.OnConflict{
		Columns:  []clause.Column{<!-- -->{Name: "name"}},
		DoUpdates: clause.Assignments(map[string]interface{}{"age": 100}),
	}).Create(&amp;user)
}

```

```
postgres=# select * from users order by id desc;
 id | name  | age |   mailbox   |   comment
----+-------+-----+-------------+--------------
 35 | test1 | 100 | test@qq.com | test comment
```

#### 使用新值替换全部字段

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	user := User{Name: "test1", Age: 25, Mailbox: "test@qq.com", Comment: "test comment"}
	db.Create(&amp;user)

	user.Age = 26
	user.Mailbox = "new@qq.com"
	user.Comment = "new comment"
	db.Clauses(clause.OnConflict{
		Columns:  []clause.Column{<!-- -->{Name: "name"}},
		UpdateAll: true,
	}).Create(&amp;user)
}

```

```
postgres=# select * from users order by id desc;
 id | name  | age |  mailbox   |   comment
----+-------+-----+------------+-------------
 33 | test1 |  26 | new@qq.com | new comment
```

#### 保留旧值不进行任何替换

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	user := User{Name: "test1", Age: 25, Mailbox: "test@qq.com", Comment: "test comment"}
	db.Create(&amp;user)

	user.Age = 26
	user.Mailbox = "new@qq.com"
	user.Comment = "new comment"
	db.Clauses(clause.OnConflict{
		Columns:  []clause.Column{<!-- -->{Name: "name"}},
		DoNothing: true,
	}).Create(&amp;user)
}

```

```
postgres=# select * from users order by id desc;
 id | name  | age |   mailbox   |   comment
----+-------+-----+-------------+--------------
 34 | test1 |  25 | test@qq.com | test comment
```



## 查询（read）

### 查询单条记录

GORM 提供了 `First`、`Take`、`Last` 方法，以便从数据库中检索单个对象。当查询数据库时它添加了 `LIMIT 1` 条件，且没有找到记录时，它会返回 `ErrRecordNotFound` 错误。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	var user User
	db.First(&amp;user) // db.Take(&amp;user)
	fmt.Printf("%#v\n", user) // main.User{Id:39, Name:"test1", Age:25, Mailbox:"", Comment:"hello world"}
}
```

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	var user User
	db.Last(&amp;user)
	fmt.Printf("%#v\n", user) // main.User{Id:41, Name:"test3", Age:20, Mailbox:"", Comment:""}
}
```

```
// 检查 ErrRecordNotFound 错误
// errors.Is(result.Error, gorm.ErrRecordNotFound)
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	var user User
	result := db.First(&amp;user)
	if result.Error != nil {
		if errors.Is(result.Error, gorm.ErrRecordNotFound) {
			fmt.Println(result.Error)
			// [1.317ms] [rows:0] SELECT * FROM "users" ORDER BY "users"."id" LIMIT 1
			// record not found
			return
		}
	}
}
```

```
// 获取第一条记录（主键升序）
db.First(&amp;user)
// SELECT * FROM users ORDER BY id LIMIT 1;

// 获取一条记录，没有指定排序字段
db.Take(&amp;user)
// SELECT * FROM users LIMIT 1;

// 获取最后一条记录（主键降序）
db.Last(&amp;user)
// SELECT * FROM users ORDER BY id DESC LIMIT 1;

result := db.First(&amp;user)
result.RowsAffected // 返回找到的记录数
result.Error        // returns error or nil
```

First 和 Last 默认按照主键 id 排序后取值，如果相关 model 没有定义主键，那么将按 model 的第一个字段进行排序。 

```

func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	var user User
	db.First(&amp;user)
	fmt.Printf("%#v\n", user) // main.User{Id:42, Name:"JinZhu", Age:18, Mailbox:"test@qq.com", Comment:"test comment"}

	result := map[string]interface{}{}
	db.Model(&amp;User{}).First(&amp;result)
	fmt.Printf("%#v\n", result) // map[string]interface {}{"age":18, "comment":"test comment", "id":42, "mailbox":"test@qq.com", "name":"JinZhu"}

	db.Table("users").Take(&amp;result)
	fmt.Printf("%#v\n", result) // map[string]interface {}{"age":18, "comment":"test comment", "id":42, "mailbox":"test@qq.com", "name":"JinZhu"}
}

```

```
var user User
var users []User

// works because destination struct is passed in
db.First(&amp;user)
// SELECT * FROM `users` ORDER BY `users`.`id` LIMIT 1

// works because model is specified using `db.Model()`
result := map[string]interface{}{}
db.Model(&amp;User{}).First(&amp;result)
// SELECT * FROM `users` ORDER BY `users`.`id` LIMIT 1

// doesn't work
result := map[string]interface{}{}
db.Table("users").First(&amp;result)

// works with Take
result := map[string]interface{}{}
db.Table("users").Take(&amp;result)

// no primary key defined, results will be ordered by first field (i.e., `Code`)
type Language struct {
  Code string
  Name string
}
db.First(&amp;Language{})
// SELECT * FROM `languages` ORDER BY `languages`.`code` LIMIT 1
```

### 根据主键查询

主键是数字

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	var user User
	db.First(&amp;user, "42")
	fmt.Printf("%#v\n", user) // main.User{Id:42, Name:"JinZhu", Age:18, Mailbox:"test@qq.com", Comment:"test comment"}

	user = User{Id: 43}
	db.First(&amp;user)
	fmt.Printf("%#v\n", user) // main.User{Id:43, Name:"Looking", Age:30, Mailbox:"test@qq.com", Comment:"new comment"}

	var users []User
	db.Find(&amp;users, []int{43, 44})
	fmt.Printf("%#v\n", users)
	// []main.User{main.User{Id:43, Name:"Looking", Age:30, Mailbox:"test@qq.com", Comment:"new comment"}, main.User{Id:44, Name:"test2", Age:100, Mailbox:"test@qq.com", Comment:"test comment"}}
}

```

主键是字符串

```
db.First(&amp;user, "id = ?", "1b74413f-f3b8-409f-ac47-e8c062e3472a")
// SELECT * FROM users WHERE id = "1b74413f-f3b8-409f-ac47-e8c062e3472a";

```

使用目标对象主键构建查询条件

```
var user = User{ID: 10}
db.First(&amp;user)
// SELECT * FROM users WHERE id = 10;

var result User
db.Model(User{ID: 10}).First(&amp;result)
// SELECT * FROM users WHERE id = 10;

```

**注意：** 如果使用 gorm 的特定字段类型（例如 `gorm.DeletedAt`），它将运行不同的查询来检索对象（我特地查了一下，DeletedAt 表示软删除。简单来说就是，执行 Delete 删除操作后，会给这个字段设置当前时间戳，表示这条数据在这个时刻已经被删除——尽管这条数据仍在数据库真实存在）。也就是说，查询的结果不会包含已经软删除的数据。

```
type User struct {
  ID           string `gorm:"primarykey;size:16"`
  Name         string `gorm:"size:24"`
  DeletedAt    gorm.DeletedAt `gorm:"index"`
}

var user = User{ID: 15}
db.First(&amp;user)
//  SELECT * FROM `users` WHERE `users`.`id` = '15' AND `users`.`deleted_at` IS NULL ORDER BY `users`.`id` LIMIT 1

```

### 查询全部记录

直接使用不带过滤条件的 Find 语句即可查询全部记录。

```
// Get all records
result := db.Find(&amp;users)
// SELECT * FROM users;

result.RowsAffected // returns found records count, equals `len(users)`
result.Error        // returns error
```

### 按照条件查询

Where 条件查询应该是我们查询时最常用的查询了，这个也是和原生的SQL最为接近的。

```
// Get first matched record
db.Where("name = ?", "jinzhu").First(&amp;user)
// SELECT * FROM users WHERE name = 'jinzhu' ORDER BY id LIMIT 1;

// Get all matched records
db.Where("name &lt;&gt; ?", "jinzhu").Find(&amp;users)
// SELECT * FROM users WHERE name &lt;&gt; 'jinzhu';

// IN
db.Where("name IN ?", []string{"jinzhu", "jinzhu 2"}).Find(&amp;users)
// SELECT * FROM users WHERE name IN ('jinzhu','jinzhu 2');

// LIKE
db.Where("name LIKE ?", "%jin%").Find(&amp;users)
// SELECT * FROM users WHERE name LIKE '%jin%';

// AND
db.Where("name = ? AND age &gt;= ?", "jinzhu", "22").Find(&amp;users)
// SELECT * FROM users WHERE name = 'jinzhu' AND age &gt;= 22;

// Time
db.Where("updated_at &gt; ?", lastWeek).Find(&amp;users)
// SELECT * FROM users WHERE updated_at &gt; '2000-01-01 00:00:00';

// BETWEEN
db.Where("created_at BETWEEN ? AND ?", lastWeek, today).Find(&amp;users)
// SELECT * FROM users WHERE created_at BETWEEN '2000-01-01 00:00:00' AND '2000-01-08 00:00:00';

```

如果对象设置了主键，条件查询将不会覆盖主键的值，而是用 And 连接条件。 所以，在你想要使用例如 `user` 这样的变量从数据库中获取新值前，需要将例如 `id` 这样的主键设置为nil。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	var user User
	user = User{Id: 42}
	db.Where("id = ?", 43).First(&amp;user)
	fmt.Printf("%#v\n", user) // [2.324ms] [rows:0] SELECT * FROM "users" WHERE "users"."id" = 43 AND "users"."id" = 42 ORDER BY "users"."id" LIMIT 1
}
```

多个Where语句可以拼接查询，效果也相当于 And 连接。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	// Struct
	var users []User
	db.Where(&amp;User{Name: "JinZhu"}).Where(&amp;User{Age: 18}).Find(&amp;users)
	fmt.Printf("%#v\n", users) // []main.User{main.User{Id:42, Name:"JinZhu", Age:18, Mailbox:"test@qq.com", Comment:"test comment"}}
}

```

### 查询结果条数统计

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	// creatUsers(db)


	var count int64
	db.Model(&amp;User{}).Where("name LIKE ?", "%test%").Count(&amp;count)
	fmt.Println(count) // 8
}

```

### Struct 和 Map 条件查询

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	// Struct
	var user User
	db.Where(&amp;User{Name: "JinZhu", Age: 18}).First(&amp;user)
	fmt.Printf("%#v\n", user) // main.User{Id:42, Name:"JinZhu", Age:18, Mailbox:"test@qq.com", Comment:"test comment"}

	// Map
	var users []User
	db.Where(map[string]interface{}{"name": "JinZhu", "age": 18}).Find(&amp;users)
	fmt.Printf("%#v\n", users) // []main.User{main.User{Id:42, Name:"JinZhu", Age:18, Mailbox:"test@qq.com", Comment:"test comment"}}

	// Slice
	db.Where([]int{43, 44}).Find(&amp;users)
	fmt.Printf("%#v\n", users) // []main.User{main.User{Id:43, Name:"Looking", Age:30, Mailbox:"test@qq.com", Comment:"new comment"}, main.User{Id:44, Name:"test2", Age:100, Mailbox:"test@qq.com", Comment:"test comment"}}
}

```

```
// Struct
db.Where(&amp;User{Name: "jinzhu", Age: 20}).First(&amp;user)
// SELECT * FROM users WHERE name = "jinzhu" AND age = 20 ORDER BY id LIMIT 1;

// Map
db.Where(map[string]interface{}{"name": "jinzhu", "age": 20}).Find(&amp;users)
// SELECT * FROM users WHERE name = "jinzhu" AND age = 20;

// Slice of primary keys
db.Where([]int64{20, 21, 22}).Find(&amp;users)
// SELECT * FROM users WHERE id IN (20, 21, 22);
```

 **注意：当使用结构体作为查询条件时，如果使用了字段的零值作为查询条件，那么这个查询字段将不会生效（简单来说就是使用零值的查询字段被忽略掉了）。**

比如下面的例子，并不会将 Age 等于 0 的记录查出来，而是查询所有记录。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	// Struct
	var users []User
	db.Where(&amp;User{Age: 0}).Find(&amp;users)
	fmt.Printf("%#v\n", users)
}
```

 要让零值查询生效的话，就使用 map 的查询条件方式。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	var users []User
	db.Where(map[string]interface{}{"name": "JinZhu", "age": 0}).Find(&amp;users)
	fmt.Printf("%#v\n", users)
}

```

### 指定结构体查询字段

简单理解就是在使用结构体作为查询条件时，可以自己指定结构体的哪些字段作为查询条件生效。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	// Struct
	var users []User
	db.Where(&amp;User{Name: "JinZhu", Age: 19}, "name").Find(&amp;users)
	fmt.Printf("%#v\n", users) // []main.User{main.User{Id:42, Name:"JinZhu", Age:18, Mailbox:"test@qq.com", Comment:"test comment"}}
}
```

### 内联条件查询

这个内联查询感觉上就是把 db.Where() 后置了，感觉用户查询体验的提升有限。

```
// Get by primary key if it were a non-integer type
db.First(&amp;user, "id = ?", "string_primary_key")
// SELECT * FROM users WHERE id = 'string_primary_key';

// Plain SQL
db.Find(&amp;user, "name = ?", "jinzhu")
// SELECT * FROM users WHERE name = "jinzhu";

db.Find(&amp;users, "name &lt;&gt; ? AND age &gt; ?", "jinzhu", 20)
// SELECT * FROM users WHERE name &lt;&gt; "jinzhu" AND age &gt; 20;

// Struct
db.Find(&amp;users, User{Age: 20})
// SELECT * FROM users WHERE age = 20;

// Map
db.Find(&amp;users, map[string]interface{}{"age": 20})
// SELECT * FROM users WHERE age = 20;
```

### Not条件

```
db.Not("name = ?", "jinzhu").First(&amp;user)
// SELECT * FROM users WHERE NOT name = "jinzhu" ORDER BY id LIMIT 1;

// Not In
db.Not(map[string]interface{}{"name": []string{"jinzhu", "jinzhu 2"}}).Find(&amp;users)
// SELECT * FROM users WHERE name NOT IN ("jinzhu", "jinzhu 2");

// Struct
db.Not(User{Name: "jinzhu", Age: 18}).First(&amp;user)
// SELECT * FROM users WHERE name &lt;&gt; "jinzhu" AND age &lt;&gt; 18 ORDER BY id LIMIT 1;

// Not In slice of primary keys
db.Not([]int64{1,2,3}).First(&amp;user)
// SELECT * FROM users WHERE id NOT IN (1,2,3) ORDER BY id LIMIT 1;
```

### Or条件 

```
db.Where("role = ?", "admin").Or("role = ?", "super_admin").Find(&amp;users)
// SELECT * FROM users WHERE role = 'admin' OR role = 'super_admin';

// Struct
db.Where("name = 'jinzhu'").Or(User{Name: "jinzhu 2", Age: 18}).Find(&amp;users)
// SELECT * FROM users WHERE name = 'jinzhu' OR (name = 'jinzhu 2' AND age = 18);

// Map
db.Where("name = 'jinzhu'").Or(map[string]interface{}{"name": "jinzhu 2", "age": 18}).Find(&amp;users)
// SELECT * FROM users WHERE name = 'jinzhu' OR (name = 'jinzhu 2' AND age = 18);
```

### 选择特定字段

查询结果中，未选择的字段会使用 Model 中的零值进行填充，已选择的字段使用从数据库查询到的实际的值。（有时候我们可能想这样：未选择的字段直接不出现在查询结果当中，这样在后续处理的过程当中就可以避免很多干扰了，下面这个只能选择字段就有这个作用）

```
db.Select("name", "age").Find(&amp;users)
// SELECT name, age FROM users;

db.Select([]string{"name", "age"}).Find(&amp;users)
// SELECT name, age FROM users;

// []main.User{main.User{Id:0, Name:"JinZhu", Age:18, Mailbox:"", Comment:""}, main.User{Id:0, Name:"Looking", Age:30, Mailbox:"", Comment:""}, main.User{Id:0, Name:"test2", Age:100, Mailbox:"", Comment:""}}
```

### 智能选择字段 

重新定义一个结构体，其中的字段是原 model 字段的子集，通过新结构体的字段，自动选择要接收哪个字段的数据。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	type APIUser struct {
		Name string
		Age  int
	}
	var users []APIUser
	db.Model(&amp;User{}).Limit(2).Find(&amp;users)
	fmt.Printf("%+v\n", users) // [{Name:JinZhu Age:18} {Name:Looking Age:30}]
}

```

### Order排序

```
db.Order("age desc, name").Find(&amp;users)
// SELECT * FROM users ORDER BY age desc, name;

// Multiple orders
db.Order("age desc").Order("name").Find(&amp;users)
// SELECT * FROM users ORDER BY age desc, name;

db.Clauses(clause.OrderBy{
  Expression: clause.Expr{SQL: "FIELD(id,?)", Vars: []interface{}{[]int{1, 2, 3}}, WithoutParentheses: true},
}).Find(&amp;User{})
// SELECT * FROM users ORDER BY FIELD(id,1,2,3)
```

### Limit &amp; Offset

Limit：限制数，表示返回数据记录的条数限制，-1 表示取消限制。

Offset：偏移数，表示查询结果里边的，从偏移量之后开始取数据，-1 表示取消偏移。

这块结合多记录批量展示时使用的 page_num, page_size 来理解也许会容易一些。

```
func (req *PageReq) GetLimit() int {
	return req.PageSize
}

func (req *PageReq) GetOffset() int {
	return (req.GetPageNum() - 1) * req.GetLimit()
}
```

连续有多个 Limit （Offset）的话，以最后一个为准。 

```
db.Limit(3).Find(&amp;users)
// SELECT * FROM users LIMIT 3;

// Cancel limit condition with -1
db.Limit(10).Find(&amp;users1).Limit(-1).Find(&amp;users2)
// SELECT * FROM users LIMIT 10; (users1)
// SELECT * FROM users; (users2)

db.Offset(3).Find(&amp;users)
// SELECT * FROM users OFFSET 3;

db.Limit(10).Offset(5).Find(&amp;users)
// SELECT * FROM users OFFSET 5 LIMIT 10;

// Cancel offset condition with -1
db.Offset(10).Find(&amp;users1).Offset(-1).Find(&amp;users2)
// SELECT * FROM users OFFSET 10; (users1)
// SELECT * FROM users; (users2)
```

### 原生SQL语句查询

```

func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	// creatUsers(db)
	var user User
	var users []User
	db.Raw("SELECT id, name, age FROM users WHERE id = ?", 2).Scan(&amp;user)
	fmt.Printf("%#v\n", user)
	// main.User{Id:2, Name:"test2", Age:18, Mailbox:"", Comment:""}
	db.Raw("SELECT id, name, age FROM users WHERE id IN ?", []int{2, 3}).Scan(&amp;users)
	fmt.Printf("%#v\n", users)
	// []main.User{main.User{Id:2, Name:"test2", Age:18, Mailbox:"", Comment:""}, main.User{Id:3, Name:"test3", Age:18, Mailbox:"", Comment:""}}
	var age int
	db.Raw("SELECT SUM(age) FROM users WHERE name LIKE ?", "%test%").Scan(&amp;age)
	fmt.Println(age) // 144
}
```

#### DryRun

在不执行的情况下生成 `SQL` 及其参数。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	// creatUsers(db)

	var user User
	stmt := db.Session(&amp;gorm.Session{DryRun: true}).First(&amp;user, 1).Statement
	fmt.Println(stmt.SQL.String())
	// SELECT * FROM "users" WHERE "users"."id" = $1 ORDER BY "users"."id" LIMIT 1
}

```

### ToSQL

返回生成的 `SQL` 但不执行。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	// creatUsers(db)

	stmt := db.ToSQL(func(tx *gorm.DB) *gorm.DB {
		return tx.Model(&amp;User{}).Where("id = ?", 2).Limit(10).Order("age asc").Find(&amp;[]User{})
	})
	fmt.Println(stmt)
	// SELECT * FROM "users" WHERE id = 2 ORDER BY age asc LIMIT 10
}
```

## 更新（update）

### 保存所有字段

`Save` 会保存所有的字段。

```
db.First(&amp;user)

user.Name = "jinzhu"
user.Age = 100
db.Save(&amp;user)
// UPDATE users SET name='jinzhu', age=100, mailbox='test@qq.com', comment= 'test comment' WHERE id=42;

```

即使字段是零值。

```
user := User{
	Id: 42,
	Name: "JinZhu",
	Age: 10,
}
db.Save(&amp;user)
// UPDATE users SET name='jinzhu', age=10, mailbox='', comment= '' WHERE id=42;

```

Save 是一个组合函数。 如果保存值不包含主键，它将执行 `Create`，否则它将执行 `Update` (包含所有字段)，也即 Upsert。 

```
db.Save(&amp;User{Id: 42, Name: "jinzhu", Age: 100})
// UPDATE `users` SET `name`='jinzhu', `age`=100, `mailbox`='', `comment`= '' WHERE `id`=42;
db.Save(&amp;User{ Name: "jinzhu", Age: 100})
// INSERT INTO `users` (`name`,`age`,`mailbox`,`comment`) VALUES ("jinzhu", 100, "", "")
```

**注意：**不要将 `Save` 和 `Model`一同使用, 这是 **未定义的行为**。

越是不让这么做，我越是要试一下。测试结果如下，简单来说，同时使用 Model 和 Save 的话，gorm 会把数据的所有字段作为记录（包括主键），从而导致 Update 语句缺少条件。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	// var user User
	user := User{
		Id: 42,
		Name: "JinZhu",
		Age: 100,
	}
	// db.Save(&amp;user)
	db.Model(&amp;User{}).Save(&amp;user)
    // WHERE conditions required [0.523ms] [rows:0] UPDATE "users" SET "id"=42,"name"='JinZhu',"age"=100,"mailbox"='',"comment"=''
}
```

### 更新单个字段

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	var user User
	db.First(&amp;user) // user.Id -&gt; 42

	db.Model(&amp;user).Where("name = ?", "JinZhu").Update("age", 30)
	// UPDATE `users` SET `age`=30 WHERE `name`='JinZhu' AND `id`=42;
	db.Model(&amp;User{}).Where("name = ?", "JinZhu").Update("age", 50)
	// UPDATE `users` SET `age`=50 WHERE `name`='JinZhu';
	db.Model(&amp;user).Update("age", 60)
	// UPDATE `users` SET `age`=60 WHERE `id`=42;
}

```

### 更新多个字段

`Updates` 方法支持 `struct` 和 `map[string]interface{}` 参数。当使用 `struct` 更新时，默认情况下GORM 只会更新非零值的字段。map可以更新零值。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	var user User
	db.First(&amp;user) // user.Id -&gt; 42

	db.Model(&amp;user).Updates(User{Name: "Hello", Age: 0})
	// UPDATE `users` SET `name`='Hello' WHERE `id`=42;
	db.Model(&amp;user).Updates(map[string]interface{}{"name":"JinZhu", "age":0})
	// UPDATE `users` SET `name`='JinZhu', `age`=0 WHERE `id`=42;
}
```

### 更新特定字段

如果您想要在更新时选择、忽略某些字段，您可以使用 `Select`、`Omit（**注意：使用 * 进行通配Select时候，主键字段也不会例外，所以千万要注意，否则一不小心就会把主键置成0**）。`

**`所以，忠告是这样：如果使用了 Select("*")，最好就自带主键 id 字段，如果使用了 Select("*").Omit()，则最好把主键字段放到 Omit 中去。`**

```
db.Model(&amp;user).Select("*").Updates(User{Id: user.Id, Name: "JinZhu", Age: 25}) // 自带主键Id字段

db.Model(&amp;user).Select("*").Omit("age", "id").Updates(User{Name: "Hello", Age: 30}) // 忽略主键Id字段
```

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	var user User
	db.First(&amp;user) // user.Id -&gt; 42

	// 选择 Struct 的字段（会选中零值的字段，选中的零值字段也会被更新）使用Struct一般会忽略零值字段，但是毕竟你指定了，那肯定按照指定的进行更新
	db.Model(&amp;user).Select("name", "age").Updates(User{Name: "Hello", Age: 0})
	// UPDATE `users` SET `name`='Hello', `age`=0 WHERE `id`=42;

	// 忽略 Struct 的字段 （未出现的字段不会被更新）
	db.Model(&amp;user).Omit("name").Updates(User{Name: "JinZhu", Age: 20})
	// UPDATE `users` SET `age`=20 WHERE `id`=42;

	// 选择 Map 的字段，同 Struct ，选中的零值字段也会被更新
	db.Model(&amp;user).Select("name", "age").Updates(map[string]interface{}{"name":"JinZhu", "age":0})
	// UPDATE `users` SET `name`='JinZhu', `age`=0 WHERE `id`=42;

	// 忽略 Map 的字段
	db.Model(&amp;user).Omit("name").Updates(map[string]interface{}{"name":"JinZhu", "age":30})
	// UPDATE `users` SET `age`=30 WHERE `id`=42;

	// 选择所有字段（选择包括零值字段的所有字段，也包括主键，谨慎使用）
	// db.Model(&amp;user).Select("*").Updates(User{Id: user.Id, Name: "JinZhu", Age: 25}) // 自带主键Id字段
	db.Model(&amp;user).Select("*").Updates(User{Name: "JinZhu", Age: 25})
	// UPDATE users SET name='JinZhu', age=25, mailbox='', content='', id=0 WHERE id=42;

	// 选择除 Role 外的所有字段（包括零值字段的所有字段，包括主键）
	// db.Model(&amp;user).Select("*").Omit("age", "id").Updates(User{Name: "Hello", Age: 30}) // 忽略主键Id字段
	db.Model(&amp;user).Select("*").Omit("age").Updates(User{Name: "Hello", Age: 30})
	// UPDATE users SET name='Hello', mailbox='', content='', id=0 WHERE id=42;
}

```

### 更新钩子Hook

之前有个新建时使用的 Hook，更新的 Hook 也类似。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	var user User
	db.Last(&amp;user) // user.Id -&gt; 60

	db.Model(&amp;user).Select("name", "age").Updates(User{Name: "test", Age: 0})
	// before save
	// before update
	// after update
	// after save
}


func (u *User) BeforeSave(tx *gorm.DB) (err error) {
	fmt.Println("before save")
	return
}

func (u *User) AfterSave(tx *gorm.DB) (err error) {
	fmt.Println("after save")
	return
}

func (u *User) BeforeUpdate(tx *gorm.DB) (err error) {
	fmt.Println("before update")
	return
}

func (u *User) AfterUpdate(tx *gorm.DB) (err error) {
	fmt.Println("after update")
	return
}

```

### 批量更新

批量更新就不多说了，大家一看都懂。从这块我们其实还能发现使用 gorm 获取数据表句柄的几种方式。**一种是使用 db.Model(model)的方式（里边使用 User{} 或 new(User)本身区别不大，反正是一个 model 的实例）；另外一种就是直接指定表名的 db.Table(TableName) 的方式了。 **

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	// Update with struct， 我自测的表的name字段加了唯一性约束，所以就不拿name字段做批量更新测试了
	db.Model(User{}).Where("age = ?", 18).Updates(User{Comment: "hello", Age: 30})
	// UPDATE users SET comment='hello', age=30 WHERE age = 18;

	// Update with map
	db.Model(new(User)).Where("id IN ?", []int{42, 43}).Updates(map[string]interface{}{"comment": "world", "age": 18})
	// UPDATE users SET comment='hello', age=18 WHERE id IN (42, 43);

	db.Table("users").Where("name LIKE ?", "%test%").Updates(map[string]interface{}{"comment": "hello world", "age": 100})
	// UPDATE users SET comment='hello world', age=100 WHERE name LIKE %test%;
}

```

### 获取更新的记录数

主要是返回结果的 .RowsAffected 字段，新建记录的时候也会有。

```
// Get updated records count with `RowsAffected`
result := db.Model(User{}).Where("role = ?", "admin").Updates(User{Name: "hello", Age: 18})
// UPDATE users SET name='hello', age=18 WHERE role = 'admin';

result.RowsAffected // returns updated records count
result.Error        // returns updating error
```

### 阻止全局更新

**一般进行无条件的全局更新是很危险的操作，但有时候可能作者本意就是如此，这时候可以使用 AllowGlobalUpdate 来临时开启允许。**

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	db.Model(&amp;User{}).Update("age", 10) // WHERE conditions required

	db.Session(&amp;gorm.Session{AllowGlobalUpdate: true}).Model(&amp;User{}).Update("age", 10)

	db.Model(&amp;User{}).Where("1 = 1").Update("age", 100)

	db.Exec("UPDATE users SET age = ?", 1000)
}

```

### 使用 SQL 表达式更新

使用表达式更新，要注意更新语句的第二个参数或 Map 的 value 是 clause.Expr 类型。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	var user User
	db.First(&amp;user) // user.Id -&gt; 42

	db.Model(&amp;user).Update("age", gorm.Expr("age * ? + ?", 2, 5))
	// UPDATE "users" SET "age" = age * 2 + 100 WHERE "id" = 42;

	db.Model(&amp;user).Updates(map[string]interface{}{"age": gorm.Expr("age * ? + ?", 2, 5)})
	// UPDATE "users" SET "age" = age * 2 + 100 WHERE "id" = 42;

	db.Model(&amp;user).UpdateColumn("age", gorm.Expr("age - ?", 10))
	// UPDATE "users" SET "age" = age - 10 WHERE "id" = 42;
}

```

### 更新子查询进行更新

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	var user User
	db.First(&amp;user) // user.Id -&gt; 42

	// db.Model(&amp;user).Update("age", 100)
	db.Model(&amp;user).Update("comment", db.Model(&amp;User{}).Select("comment").Where("users.name = 'Looking'"))
	// UPDATE "users" SET "comment" = (SELECT comment FROM users WHERE users.name = 'Looking') where id=42;

	db.Model(&amp;User{}).Where("name = ?", "test").Update("comment", db.Model(&amp;User{}).Select("comment").Where("users.name = 'Looking'"))
	// UPDATE "users" SET "comment" = (SELECT comment FROM users WHERE users.name = 'Looking') where name = 'test';
}
```

### 返回修改行数据

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	// return all columns
	var users []User
	db.Model(&amp;users).Clauses(clause.Returning{}).Where("name = ?", "Looking").Update("age", 30)
	// UPDATE `users` SET `age`=30 WHERE name = "Looking" RETURNING *
	fmt.Printf("users:%v\n", users)
	// users =&gt; [{43 Looking 30 test@qq.com world}]
}

```

### Update时修改值

**gorm 可以通过 tx.Statement.Changed("column") 检测对应字段的值是否在 Update 时有更新，还可以通过 tx.Statement.SetColumn("column", "value") 设置对应字段的值。**

```

var user User

func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	db.First(&amp;user) // user.Id -&gt; 42

	db.Model(&amp;user).Select("name", "age").Updates(User{Name: "Hello", Age: 0})
	// before save
	// age change
	// before update
	// name change
}

func (u *User) BeforeUpdate(tx *gorm.DB) (err error) {
	fmt.Println("before update")
	if tx.Statement.Changed("name") {
		fmt.Println("name change")
		tx.Statement.SetColumn("age", 30)
	}
	return
}

func (u *User) BeforeSave(tx *gorm.DB) (err error) {
	fmt.Println("before save")
	if tx.Statement.Changed("age") {
		fmt.Println("age change")
		user.Age += 20
		tx.Statement.SetColumn("age", user.Age)
	}
	return
}

```

## 删除（delete）

### 删除单条记录

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	var user User
	db.First(&amp;user) // user.Id -&gt; 42
	db.Delete(&amp;user)
	// DELETE FROM users WHERE id=42;

	db.First(&amp;user) // user.Id -&gt; 43
	db.Where("name = ?", "Looking").Delete(&amp;user)
	// DELETE FROM users WHERE id=43 AND name='Looking';
}

```

### 根据主键删除记录

其实上面默认删除单条记录的方式，也是通过主键进行删除记录，只不过主键已经隐含在了 model 对象里边。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	db.Delete(&amp;User{}, []int{46, 47})
	// DELETE FROM users WHERE id IN (46,47);

	db.Delete(&amp;User{}, "48")
	// DELETE FROM users WHERE id=48;

	db.Delete(&amp;User{}, 49)
	// DELETE FROM users WHERE id=49;
}
```

### 删除钩子Hook

同新增和更新一样，删除也有自己的钩子Hook，其中 BeforeSave 和 AfterSave 在删除操作中是不会触发的。至于为什么，我摘抄了一段 chatgpt 的回答。

在Gorm中，删除操作（Delete）不会触发BeforeSave和AfterSave方法。这是因为BeforeSave和AfterSave方法主要用于在保存记录之前和之后执行一些相关操作，而删除操作与保存操作有本质的区别。 如果需要在删除操作之前或之后执行一些操作，可以使用Gorm提供的其他钩子方法，例如BeforeDelete和AfterDelete。这些方法可以在模型结构体的定义中定义，并且在执行删除操作之前和之后被自动调用。

**注意：** 在 GORM 中保存、删除操作会默认运行在事务上， 因此在事务完成之前该事务中所作的更改是不可见的，如果您的钩子返回了任何错误，则修改将被回滚。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	var user User
	db.First(&amp;user) // user.Id -&gt; 54
	db.Where("name = ?", "test12").Delete(&amp;user)
    // before delete
    // test12 user not allowed to delete
}

func (u *User) BeforeSave(tx *gorm.DB) (err error) {
	fmt.Println("before save")
	return
}

func (u *User) AfterSave(tx *gorm.DB) (err error) {
	fmt.Println("after save")
	return
}

func (u *User) BeforeDelete(tx *gorm.DB) (err error) {
	fmt.Println("before delete")
	if u.Name == "test12" {
		fmt.Println("test12 user not allowed to delete")
		return errors.New("test12 user not allowed to delete")
	}
	return
}

func (u *User) AfterDelete(tx *gorm.DB) (err error) {
	fmt.Println("after delete")
	return
}

```

### 批量删除

如果指定的值不包括主属性，那么 GORM 会执行批量删除，它将删除所有匹配的记录。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	// creatUsers(db)

	db.Where("name LIKE ?", "%test%").Delete(&amp;User{})
	// DELETE FROM users WHERE name LIKE "%test%";
	db.Delete(&amp;User{}, "name LIKE ?", "%test%")
	// DELETE FROM users WHERE name LIKE "%test%";
}

```

也可以将一个主键切片传递给`Delete` 方法，以便更高效的删除数据量大的记录。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	// creatUsers(db)

	var users = []User{<!-- -->{Id: 80}, {Id: 81}, {Id: 82}}
	db.Delete(&amp;users)
	// DELETE FROM users WHERE id IN (80,81,82);

	db.Delete(&amp;users, "name LIKE ?", "%test%")
	// DELETE FROM users WHERE name LIKE "%test%" AND id IN (80,81,82);
}
```

### 阻止全局删除

这个和阻止全局更新的原因类似，毕竟不带 Where 条件删除是一件很危险的事。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	// creatUsers(db)

	db.Delete(&amp;User{}) // WHERE conditions required

	db.Delete(&amp;User{Name: "test1"}) // WHERE conditions required
	db.Where("1 = 1").Delete(&amp;User{})
	// DELETE FROM `users` WHERE 1=1

	db.Exec("DELETE FROM users")
	// DELETE FROM users

	db.Session(&amp;gorm.Session{AllowGlobalUpdate: true}).Delete(&amp;User{})
	// DELETE FROM users
}
```

### 返回删除行数据

回写指定列的时候，可以发现返回的数据，只有指定列是有数据，其他列都直接使用了零值替换。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)
	// creatUsers(db)

	// 回写所有的列
	var users []User
	db.Clauses(clause.Returning{}).Where("name = ?", "test1").Delete(&amp;users)
	// DELETE FROM `users` WHERE name = "test1" RETURNING *
	fmt.Printf("usres:%#v\n", users)
	// users =&gt; []main.User{main.User{Id:88, Name:"test1", Age:18, Mailbox:"test@qq.com", Comment:"test comment"}}

	// 回写指定的列
	db.Clauses(clause.Returning{Columns: []clause.Column{<!-- -->{Name: "name"}, {Name: "age"}}}).Where("name = ?", "test3").Delete(&amp;users)
	// DELETE FROM `users` WHERE name = "test3" RETURNING `name`, `age`
	fmt.Printf("usres:%#v\n", users)
	// users =&gt; []main.User{main.User{Id:0, Name:"test3", Age:18, Mailbox:"", Comment:""}}
}
```

### 软删除

为了模拟软删除，我在 model 里加一个 DeletedAt 的字段，重新创建一下表。

```
// User model
type User struct {
	Id      int    `gorm:"column:id;primarykey" json:"id"`
	Name    string `gorm:"column:name;index:,unique" json:"name"`
	Age     int8   `gorm:"column:age" json:"age"`
	Mailbox string `gorm:"column:mailbox" json:"mailbox"`
	Comment string `gorm:"column:comment;default:hello world" json:"comment"`
	DeletedAt gorm.DeletedAt
}
```

```
postgres=# select * from users order by id;
 id | name  | age |   mailbox   |   comment    | deleted_at
----+-------+-----+-------------+--------------+------------
  1 | test1 |  18 | test@qq.com | test comment |
  2 | test2 |  18 | test@qq.com | test comment |
  3 | test3 |  18 | test@qq.com | test comment |
  4 | test4 |  18 | test@qq.com | test comment |
```

可以看到，被软删除的数据，其实还真实存在数据库当中，只不过进行查询的时候，被 gorm 通过 deleted_at 字段的标记自动过滤掉了。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	// creatUsers(db)
	var user User
	db.First(&amp;user)
	db.Delete(&amp;user)
	// UPDATE users SET deleted_at="2024-02-06 08:43:14.579132+08" WHERE id = 1;

	db.Where("name LIKE ?", "%test%").Find(&amp;user)
	fmt.Printf("%+v\n", user)
	// {Id:2 Name:test2 Age:18 Mailbox:test@qq.com Comment:test comment DeletedAt:{Time:0001-01-01 00:00:00 +0000 UTC Valid:false}}
}
```

```
postgres=# select * from users order by id;
 id | name  | age |   mailbox   |   comment    |          deleted_at
----+-------+-----+-------------+--------------+-------------------------------
  1 | test1 |  18 | test@qq.com | test comment | 2024-02-06 08:43:14.579132+08
  2 | test2 |  18 | test@qq.com | test comment |
  3 | test3 |  18 | test@qq.com | test comment |
  4 | test4 |  18 | test@qq.com | test comment |
```

### 查找被软删除的记录

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	// creatUsers(db)
	var user User
	db.Unscoped().Where("name = ?", "test1").Find(&amp;user)
	fmt.Printf("%+v\n", user)
	// {Id:1 Name:test1 Age:18 Mailbox:test@qq.com Comment:test comment DeletedAt:{Time:2024-02-06 08:43:14.579132 +0800 CST Valid:true}}
}
```

### 永久删除

记录永久删除后，在数据库也就被真正的删除了。

```
func main() {
	conf := getDatabaseConf()
	db, _ := connect(conf)

	// creatUsers(db)
	var user User
	db.Unscoped().Where("name = ?", "test1").Delete(&amp;user)
	// DELETE FROM users WHERE name='test1';
}
```

## 事务和迁移 

为了确保数据一致性，GORM 会在事务里执行写入操作（创建、更新、删除）。可以根据需要在初始化时禁用它。

```
// 全局禁用
db, err := gorm.Open(sqlite.Open("gorm.db"), &amp;gorm.Config{
  SkipDefaultTransaction: true,
})

// 持续会话模式
tx := db.Session(&amp;Session{SkipDefaultTransaction: true})
tx.First(&amp;user, 1)
tx.Find(&amp;users)
tx.Model(&amp;user).Update("Age", 18)
```

事务对象一般使用 tx 变量。 

### AutoMigrate

AutoMigrate 用于自动迁移您的 schema，保持您的 schema 是最新的（我用例中数据库的表的创建就是用的 AutoMigrate 来实现的）。

>  
 **注意：** AutoMigrate 会创建表、缺失的外键、约束、列和索引。 如果大小、精度、是否为空可以更改，则 AutoMigrate 会改变列的类型。 出于保护您数据的目的，它 **不会** 删除未使用的列。 


### Migrator接口

当前数据库名

```
db.Migrator().CurrentDatabase()

```

表操作

```
// 为 `User` 创建表
db.Migrator().CreateTable(&amp;User{})

// 将 "ENGINE=InnoDB" 添加到创建 `User` 的 SQL 里去
db.Set("gorm:table_options", "ENGINE=InnoDB").Migrator().CreateTable(&amp;User{})

// 检查 `User` 对应的表是否存在
db.Migrator().HasTable(&amp;User{})
db.Migrator().HasTable("users")

// 如果存在表则删除（删除时会忽略、删除外键约束)
db.Migrator().DropTable(&amp;User{})
db.Migrator().DropTable("users")

// 重命名表
db.Migrator().RenameTable(&amp;User{}, &amp;UserInfo{})
db.Migrator().RenameTable("users", "user_infos")
```

列操作

```
type User struct {
  Name string
}

// 添加 name 字段
db.Migrator().AddColumn(&amp;User{}, "Name")
// 删除 name 字段
db.Migrator().DropColumn(&amp;User{}, "Name")
// 修改 name 字段
db.Migrator().AlterColumn(&amp;User{}, "Name")
// 检查 name 字段是否存在
db.Migrator().HasColumn(&amp;User{}, "Name")

type User struct {
  Name    string
  NewName string
}

// 字段重命名
db.Migrator().RenameColumn(&amp;User{}, "Name", "NewName")
db.Migrator().RenameColumn(&amp;User{}, "name", "new_name")
```

### 常规数据库接口

```
// 获取通用数据库对象 sql.DB，然后使用其提供的功能
sqlDB, err := db.DB()

// Ping
sqlDB.Ping()

// Close
sqlDB.Close()

// 返回数据库统计信息
sqlDB.Stats()

// SetMaxIdleConns 用于设置连接池中空闲连接的最大数量。
sqlDB.SetMaxIdleConns(10)

// SetMaxOpenConns 设置打开数据库连接的最大数量。
sqlDB.SetMaxOpenConns(100)

// SetConnMaxLifetime 设置了连接可复用的最大时间。
sqlDB.SetConnMaxLifetime(time.Hour)
```

### 作用域通用逻辑复用

作用域允许你复用通用的逻辑，这种共享逻辑需要定义为类型`func(*gorm.DB) *gorm.DB`。

```
func AmountGreaterThan1000(db *gorm.DB) *gorm.DB {
  return db.Where("amount &gt; ?", 1000)
}

func PaidWithCreditCard(db *gorm.DB) *gorm.DB {
  return db.Where("pay_mode_sign = ?", "C")
}

func PaidWithCod(db *gorm.DB) *gorm.DB {
  return db.Where("pay_mode_sign = ?", "C")
}

func OrderStatus(status []string) func (db *gorm.DB) *gorm.DB {
  return func (db *gorm.DB) *gorm.DB {
    return db.Where("status IN (?)", status)
  }
}

db.Scopes(AmountGreaterThan1000, PaidWithCreditCard).Find(&amp;orders)
// 查找所有金额大于 1000 的信用卡订单

db.Scopes(AmountGreaterThan1000, PaidWithCod).Find(&amp;orders)
// 查找所有金额大于 1000 的 COD 订单

db.Scopes(AmountGreaterThan1000, OrderStatus([]string{"paid", "shipped"})).Find(&amp;orders)
// 查找所有金额大于1000 的已付款或已发货订单
```

### gorm配置

GORM 提供的配置可以在初始化时使用。

```
type Config struct {
  SkipDefaultTransaction   bool
  NamingStrategy           schema.Namer
  Logger                   logger.Interface
  NowFunc                  func() time.Time
  DryRun                   bool
  PrepareStmt              bool
  DisableNestedTransaction bool
  AllowGlobalUpdate        bool
  DisableAutomaticPing     bool
  DisableForeignKeyConstraintWhenMigrating bool
}
```

#### SkipDefaultTransaction

为了确保数据一致性，GORM 会在事务里执行写入操作（创建、更新、删除）。如果没有这方面的要求，您可以在初始化时禁用它。

```
db, err := gorm.Open(sqlite.Open("gorm.db"), &amp;gorm.Config{
  SkipDefaultTransaction: true,
})
```

#### NamingStrategy

GORM 允许用户通过覆盖默认的`NamingStrategy`来更改命名约定，这需要实现接口 `Namer。`

```
type Namer interface {
    TableName(table string) string
    SchemaName(table string) string
    ColumnName(table, column string) string
    JoinTableName(table string) string
    RelationshipFKName(Relationship) string
    CheckerName(table, column string) string
    IndexName(table, column string) string
}
```

#### Logger

允许通过覆盖此选项更改 GORM 的默认 logger。

#### NowFunc

更改创建时间使用的函数。

```
db, err := gorm.Open(sqlite.Open("gorm.db"), &amp;gorm.Config{
  NowFunc: func() time.Time {
    return time.Now().Local()
  },
})
```

#### DryRun

生成 SQL 但不执行，可以用于准备或测试生成的 SQL。

```
db, err := gorm.Open(sqlite.Open("gorm.db"), &amp;gorm.Config{
  DryRun: false,
})
```

#### PrepareStmt

`PreparedStmt` 在执行任何 SQL 时都会创建一个 prepared statement 并将其缓存。

```
db, err := gorm.Open(sqlite.Open("gorm.db"), &amp;gorm.Config{
  PrepareStmt: false,
})
```

#### `DisableNestedTransaction` 

`RollbackTo(savedPointName)` 为你提供嵌套事务支持，你可以通过 `DisableNestedTransaction` 选项关闭它。

#### AllowGlobalUpdate

启用全局 update/delete。

#### DisableAutomaticPing

在完成初始化后，GORM 会自动 ping 数据库以检查数据库的可用性，若要禁用该特性，可将其设置为 true。

```
db, err := gorm.Open(sqlite.Open("gorm.db"), &amp;gorm.Config{
  DisableAutomaticPing: true,
})
```

#### DisableForeignKeyConstraintWhenMigrating

在 AutoMigrate 或 CreateTable 时，GORM 会自动创建外键约束，若要禁用该特性，可将其设置为 true。

```
db, err := gorm.Open(sqlite.Open("gorm.db"), &amp;gorm.Config{
  DisableForeignKeyConstraintWhenMigrating: true,
})
```


