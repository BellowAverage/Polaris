
--- 
title:  Go 之 captcha 生成图形验证码 
tags: []
categories: [] 

---
### captcha

目前 chptcha 好像只可以生成纯数字的不带底色的图像验证码，不过对于普通简单应用来说也足够了。captcha默认将store封装到内部，未提供对外操作的接口，因此使用自己显式生成的store，可以通过store自定义要生成的验证码。

```
package main

import (
	"bytes"
	"fmt"
	"github.com/dchest/captcha"
	"log"
	"os"
)

// Captcha 方便后期扩展
type Captcha struct{}

// 单例
var captchaInstance *Captcha

func Instance() *Captcha {
	if captchaInstance == nil {
		captchaInstance = &amp;Captcha{}
	}
	return captchaInstance
}

// CreateImage 创建图片验证码
func (this *Captcha) CreateImage() string {
	length := captcha.DefaultLen
	captchaId := captcha.NewLen(length)
	return captchaId
}

// Reload 重载
func (this *Captcha) Reload(captchaId string) bool {
	return captcha.Reload(captchaId)
}

// Verify 验证
func (this *Captcha) VerifyString(captchaId, val string) bool {
	return captcha.VerifyString(captchaId, val)
}

func (this *Captcha) Verify(captchaId string, digits []byte) bool  {
	return captcha.Verify(captchaId, digits)
}

// GetImageByte 获取图片二进制流
func (this *Captcha) GetImageByte(captchaId string) []byte {
	var content bytes.Buffer
	err := captcha.WriteImage(&amp;content, captchaId, captcha.StdWidth, captcha.StdHeight)
	if err != nil {
		log.Println(err)
		return nil
	}
	return content.Bytes()
}

// WriteImageFile 写图片文件
func (this *Captcha) WriteImageFile(b []byte, file string) {
	f, err := os.OpenFile(file, os.O_CREATE | os.O_RDWR, os.ModePerm)
	defer f.Close()
	if err != nil {
		log.Println(err)
	}
	f.Write(b)
}

func main() {
	// capt := Instance()
	// captId := capt.CreateImage()
	// capt.WriteImageFile(capt.GetImageByte(captId), "test.png")

	// captcha默认将store封装到内部，未提供对外操作的接口
	// 使用自己显式生成的store，可以通过store自定义要生成的图形验证码
	store := captcha.NewMemoryStore(captcha.CollectNum, captcha.Expiration)
	captcha.SetCustomStore(store)
	capt := Instance()
	captId := capt.CreateImage()
	b := []byte{6, 6, 6, 8, 8, 8}
	store.Set(captId, b)
	// store.Set(captId, captcha.RandomDigits(6))
	fmt.Println(store.Get(captId, false))
	capt.WriteImageFile(capt.GetImageByte(captId), "test.png")
	// vs := capt.VerifyString(captId, "666888")
	v := capt.Verify(captId, b)
	if v {
		fmt.Println("verify succeed")
	} else {
		fmt.Println("verify failed")
	}
}
```

<img alt="" height="80" src="https://img-blog.csdnimg.cn/91da32641def42d2a6ed9822efe6939e.png" width="240"><img alt="" height="80" src="https://img-blog.csdnimg.cn/679209f5f61940d2b539e772dd0b16be.png" width="240">

### base64Captcha

base64Captcha 要稍微强大一些，可以生成带底色的包含字母的图形验证码。验证码所用的字符集也可以进行自定义，可以选择图形验证码的字体。

```
package main

import (
	"encoding/base64"
	"fmt"
	"github.com/mojocn/base64Captcha"
	"log"
	"os"
	"strings"
)

// WriteImageFile 写图片文件
func WriteImageFile(b []byte, file string) {
	f, err := os.OpenFile(file, os.O_CREATE|os.O_RDWR, os.ModePerm)
	defer f.Close()
	if err != nil {
		log.Println(err)
	}
	f.Write(b)
}

func main() {
	store := base64Captcha.DefaultMemStore
	// driver := base64Captcha.NewDriverDigit(80, 240, 6, 0.7, 80)
	driver := &amp;base64Captcha.DriverString{
		Height:          80,
		Width:           240,
		NoiseCount:      0,
		ShowLineOptions: 2 | 4,
		Length:          6,
		// Source:          base64Captcha.TxtSimpleCharaters,
		Source:  base64Captcha.TxtNumbers + base64Captcha.TxtAlphabet,
		BgColor: nil,                                                              // 默认使用浅色背景色，深色字体色
		Fonts:   []string{"wqy-microhei.ttc"}, // ApothecaryFont.ttf、Flim-Flam.ttf、RitaSmith.ttf、wqy-microhei.ttc 字体识别度稍微高一些
	}
	// driver := captchaConfig.ConvertFonts()
	capt := base64Captcha.NewCaptcha(driver, store)
	captchaId, s, err := capt.Generate()
	if err != nil {
		log.Println(err)
	}

	fmt.Println(captchaId)
	fmt.Println(s)
	stdEncodingStr := strings.Split(s, ",")[1]
	byteData, err := base64.StdEncoding.DecodeString(stdEncodingStr)
	if err != nil {
		fmt.Println("Decode failed:", err)
		return
	}
	WriteImageFile(byteData, fmt.Sprintf("test.png"))
}

```

<img alt="" height="80" src="https://img-blog.csdnimg.cn/fda11a4d577346abb57c89cf9eb497a7.png" width="240">

当然，base64Captcha 也可以生成纯数字的不带底色的验证码图片，只需要将 Driver 修改成 base64Captcha.NewDriverDigit 就可以了。

<img alt="" height="80" src="https://img-blog.csdnimg.cn/9b96597be51140f19a18f2ce5f3278ed.png" width="240"><img alt="" height="80" src="https://img-blog.csdnimg.cn/5eb64e298d364117915369ed1d8383df.png" width="240">
