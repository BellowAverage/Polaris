
--- 
title:  gorm框架之自定义表名 
tags: []
categories: [] 

---
当然，只需要为定义好的数据表结构体实现一个 TableName 方法就好了。

对于新手来说，是比较好奇这个方法是怎么生效的，因为自己写的代码里其实并没有显式的调用这个方法的。

```
type User struct{
	Id int `gorm:"column:id;primaryKey;"`
	Name string `gorm:"name:id;"`
}

// 自定义表名
func (User) TableName() string {
	return "test_user"
}
```

在 gorm 里边，有一个 Tabler 接口，接口的也很简单，只需要自己的表结构体实现一个 TableName 方法就可以。

```
type Tabler interface {
	TableName() string
}
```

然后在解析表名的时候，会有相关逻辑判断对应的 model 是不是 Tabler 类型，是的话就会调用 TableName 方法（也就是我们自定义实现的那个方法名）来获取表名。

```
	...
    modelValue := reflect.New(modelType)
	tableName := namer.TableName(modelType.Name())
	if tabler, ok := modelValue.Interface().(Tabler); ok {
		tableName = tabler.TableName()
	}
	if tabler, ok := modelValue.Interface().(TablerWithNamer); ok {
		tableName = tabler.TableName(namer)
	}
	if en, ok := namer.(embeddedNamer); ok {
		tableName = en.Table
	}
    ...
```

当然，这里边涉及到一些反射相关的知识。

```
package main

import (
	"fmt"
	"reflect"
)

func main() {
	var x float64 = 3.4
	fmt.Println("type:", reflect.TypeOf(x)) // type: float64
	v := reflect.ValueOf(x)
	fmt.Println("value:", v)         // value: 3.4
	fmt.Println("type:", v.Type())   // type: float64
	fmt.Println("kind:", v.Kind())   // kind: float64
	fmt.Println("value:", v.Float()) // value: 3.4
	fmt.Println(v.Interface())
	fmt.Printf("value is %5.2e\n", v.Interface()) // value is 3.40e+00
	y, ok := v.Interface().(float64)
	if ok {
		fmt.Println(y) // 3.4
	}
	switch v.Interface().(type) {
	case int:
		fmt.Println("int type")
	case float32:
		fmt.Println("float32 type")
	case float64:
		fmt.Println("float64 type") // go there
	default:
		fmt.Println("unknown type")
	}
}

```

比如里边的 Kind 和 Type，看起来好像差不多，不过还是有区别的，我摘抄一段解释。

相较于 Type 而言，Kind 所表示的范畴更大。类似于家用电器（Kind）和电视机（Type）之间的对应关系。或者电视机（Kind）和 42 寸彩色电视机（Type）Type 是类型。Kind 是类别。Type 和 Kind 可能相同，也可能不同。通常基础数据类型的 Type 和 Kind 相同，自定义数据类型则不同。对于反射中的 kind 我们既可以通过 reflect.Type 来获取，也可以通过 reflect.Value 来获取。他们得到的值和类型均是相同的。

下面的例子其实比较清晰能说明了。

```
package main

import (
	"fmt"
	"reflect"
)

func main() {
	var x = struct {
		Name string
	}{Name: "Looking"}
	fmt.Println("type:", reflect.TypeOf(x)) // type: struct { Name string }
	v := reflect.ValueOf(x)
	fmt.Println("value:", v)       // value: {Looking}
	fmt.Println("type:", v.Type()) // type: struct { Name string }
	fmt.Println("kind:", v.Kind()) // kind: struct
}

```

看源码的话其实可以知道，Kind 类型目前就下面列举的这些。

```
type Kind uint

const (
	Invalid Kind = iota
	Bool
	Int
	Int8
	Int16
	Int32
	Int64
	Uint
	Uint8
	Uint16
	Uint32
	Uint64
	Uintptr
	Float32
	Float64
	Complex64
	Complex128
	Array
	Chan
	Func
	Interface
	Map
	Ptr
	Slice
	String
	Struct
	UnsafePointer
)
```


