
--- 
title:  Go 的 gin 参数校验之 validator 库 
tags: []
categories: [] 

---
使用 validator 以后，只需要在定义结构体时使用`binding`或`validate`tag标识相关校验规则，就可以进行参数校验了，而不用自己单独去写常见的校验规则。

## main.go

```
package main

import (
	"fmt"
	"github.com/go-playground/validator/v10"

	"github.com/go-playground/locales/zh_Hans_CN"
	unTrans "github.com/go-playground/universal-translator"
	zhTrans "github.com/go-playground/validator/v10/translations/zh"
)

type User struct {
	Username string `validate:"min=6,max=10,contains=ook,startswith=He"`
	Age      uint8  `validate:"gte=1,lte=10"`
	Sex      string `validate:"oneof=female male"`
	Email    string `validate:"email"`
}

func main() {
	validate := validator.New()
	//user := User{Username: "Heooking", Age: 6, Sex: "male", Email: "test@qq.com"}
	user := User{Username: "Looking", Age: 26, Sex: "male", Email: "qq.com"}
	err := validate.Struct(user)
	// 默认英文提示
	if err != nil {
		fmt.Println(err)
		//Key: 'User.Username' Error:Field validation for 'Username' failed on the 'startswith' tag
		//Key: 'User.Age' Error:Field validation for 'Age' failed on the 'lte' tag
		//Key: 'User.Email' Error:Field validation for 'Email' failed on the 'email' tag
	}

	fmt.Println()
	// 中文错误提示
	uni := unTrans.New(zh_Hans_CN.New())
	trans, _ := uni.GetTranslator("zh_Hans_CN")
	zhTrans.RegisterDefaultTranslations(validate, trans)
	if err != nil {
		for _, v := range err.(validator.ValidationErrors) {
			fmt.Println(v.Translate(trans))
			//Username必须以文本'He'开头
			//Age必须小于或等于10
			//Email必须是一个有效的邮箱
		}
	}
}

```

## go.mod

```
module test

go 1.17

require (
	github.com/go-playground/validator/v10 v10.15.0
)

require (
	github.com/gabriel-vasile/mimetype v1.4.2 // indirect
	github.com/go-playground/locales v0.14.1 // indirect
	github.com/go-playground/universal-translator v0.18.1 // indirect
	github.com/leodido/go-urn v1.2.4 // indirect
	golang.org/x/crypto v0.7.0 // indirect
	golang.org/x/net v0.8.0 // indirect
	golang.org/x/sys v0.6.0 // indirect
)

```

常用约束如下：

字符串约束
- excludesall：不包含参数中任意的 UNICODE 字符，例如excludesall=ab；- excludesrune：不包含参数表示的 rune 字符，excludesrune=asong；- startswith：以参数子串为前缀，例如startswith=hi；- endswith：以参数子串为后缀，例如endswith=bye。- contains=：包含参数子串，例如contains=email；- containsany：包含参数中任意的 UNICODE 字符，例如containsany=ab；- containsrune：包含参数表示的 rune 字符，例如`containsrune=asong；- excludes：不包含参数子串，例如excludes=email；
范围约束 范围约束的字段类型分为三种：
- 对于数值，我们则可以约束其值- 对于切片、数组和map，我们则可以约束其长度- 对于字符串，我们则可以约束其长度
常用 tag 介绍：
- ne：不等于参数值，例如 ne=5；- gt：大于参数值，例如 gt=5；- gte：大于等于参数值，例如 gte=50；- lt：小于参数值，例如 lt=50；- lte：小于等于参数值，例如 lte=50；- oneof：只能是列举出的值其中一个，这些值必须是数值或字符串，以空格分隔，如果字符串中有空格，将字符串用单引号包围，例如 oneof=male female。- eq：等于参数值，注意与 len不同。对于字符串， eq约束字符串本身的值，而 len约束字符串长度。例如 eq=10；- len：等于参数值，例如 len=10；- max：小于等于参数值，例如 max=10；- min：大于等于参数值，例如 min=10- Fields约束- eqfield：定义字段间的相等约束，用于约束同一结构体中的字段。例如： eqfield=Password- eqcsfield：约束统一结构体中字段等于另一个字段（相对），确认密码时可以使用，例如： eqfiel=ConfirmPassword- nefield：用来约束两个字段是否相同，确认两种颜色是否一致时可以使用，例如： nefield=Color1- necsfield：约束两个字段是否相同（相对）
常用约束
- unique：指定唯一性约束，不同类型处理不同：
        对于map，unique约束没有重复的值         对于数组和切片，unique没有重复的值         对于元素类型为结构体的碎片，unique约束结构体对象的某个字段不重复，使用 unique=field指定字段名
- email：使用email来限制字段必须是邮件形式，直接写eamil即可，无需加任何指定。- omitempty：字段未设置，则忽略- -：跳过该字段，不检验；- |：使用多个约束，只需要满足其中一个，例如rgb|rgba；- required：字段必须设置，不能为默认值；  