
--- 
title:  有名的爬虫框架 colly 的特性及2个详细采集案例 
tags: []
categories: [] 

---
### 一. Colly概述

**前言**：colly 是 Go 实现的比较有名的一款爬虫框架，而且 Go 在高并发和分布式场景的优势也正是爬虫技术所需要的。它的主要特点是轻量、快速，设计非常优雅，并且分布式的支持也非常简单，易于扩展。

**框架简介**：基于colly框架及net/http进行封装，实现的一款可配置分布式爬虫架构。使用者只需要配置解析、并发数、入库topic、请求方式、请求url等参数即可，其他代码类似于scrapy，不需要单独编写。

>  
 colly官网地址： github地址:  


**colly特性**
- 干净的API- 快速(单核&gt;1k请求/秒)- 管理每个域的请求延迟和最大并发性- 自动cookie和会话处理- 同步/异步并行抓取- 分布式抓取- 缓存- 非unicode响应的自动编码- robots. txt的支持- 抓取深度控制- 设置跨域开关- 谷歌应用程序引擎支持
### 二. colly安装及基本使用

**安装**：`go get -u github.com/gocolly/colly/...`

**基本使用**：

```
package main

import (
	"fmt"

	"github.com/gocolly/colly"
)

func main() {<!-- -->
	// Instantiate default collector
	c := colly.NewCollector(
		// Visit only domains: hackerspaces.org, wiki.hackerspaces.org
		colly.AllowedDomains("hackerspaces.org", "wiki.hackerspaces.org"),
	)

	// On every a element which has href attribute call callback
	c.OnHTML("a[href]", func(e *colly.HTMLElement) {<!-- -->
		link := e.Attr("href")
		// Print link
		fmt.Printf("Link found: %q -&gt; %s\n", e.Text, link)
		// Visit link found on page
		// Only those links are visited which are in AllowedDomains
		c.Visit(e.Request.AbsoluteURL(link))
	})

	// Before making a request print "Visiting ..."
	c.OnRequest(func(r *colly.Request) {<!-- -->
		fmt.Println("Visiting", r.URL.String())
	})

	// Start scraping on https://hackerspaces.org
	c.Visit("https://hackerspaces.org/")
}

```

### 三. 基于colly的2个使用案例

#### 案例1

```
package main

import (
	"fmt"
	"time"

	"github.com/gocolly/colly"
)

func main() {<!-- -->
	ua := "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
	c := colly.NewCollector(
		colly.UserAgent(ua),                      // 设置UA
		colly.DetectCharset(),                    // 自动编码，防止乱码
		colly.AllowedDomains("www.tcmap.com.cn"), // 限制域名
	)
	c.AllowURLRevisit = true                  // 另外一种设置方式，允许重复访问
	_ = c.SetProxy("socks://127.0.0.1:10808") // 设置代理

	// 响应内容是HTML时调用，goquerySelector来查找元素
	c.OnHTML("a[href*=\"shandong\"]", func(h *colly.HTMLElement) {<!-- -->
		// fmt.Println(h.Text)
		href := h.Request.AbsoluteURL(h.Attr("href")) // 绝对路径
		_ = h.Request.Visit(href)
		// 接收上下文传递过来的数据
		city := h.Response.Ctx.Get("city")
		fmt.Println(city)
	})

	_ = c.Limit(&amp;colly.LimitRule{<!-- -->
		DomainGlob:  "*",
		RandomDelay: 1 * time.Second, // 延时
	})

	// 请求前调用
	c.OnRequest(func(r *colly.Request) {<!-- -->
		fmt.Println("访问：", r.URL)
		// 从请求往响应传递上下文数据
		r.Ctx.Put("city", "城市")
	})

	// 收到响应后调用
	c.OnResponse(func(r *colly.Response) {<!-- -->
		// fmt.Println(string(r.Body))
	})

	// 通过xpath来获取元素
	c.OnXML("//", func(element *colly.XMLElement) {<!-- -->

	})

	// 请求发生错误时调用
	c.OnError(func(r *colly.Response, err error) {<!-- -->
		fmt.Println(err)
	})

	c.Visit("http://www.tcmap.com.cn/shandong/")
}



```

#### 案例2

```
package main

import (
	"fmt"
	"github.com/gocolly/colly"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
	"time"
)

func main() {<!-- -->
	dsn := "root:pass@tcp(127.0.0.1:3306)/test?charset=utf8mb4&amp;parseTime=True&amp;loc=Local"
	db, err := gorm.Open(mysql.New(mysql.Config{<!-- -->
		DSN:               dsn,
		DefaultStringSize: 256,
	}), &amp;gorm.Config{<!-- -->})
	if err != nil {<!-- -->
		fmt.Println("连结数据库失败")
	}

	ua := "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
	c := colly.NewCollector(
		colly.UserAgent(ua),                      // 设置UA
		colly.DetectCharset(),                    // 自动编码，防止乱码
		colly.AllowedDomains("www.tcmap.com.cn"), // 限制域名
	)
	cityCollector := c.Clone()
	countyCollector := c.Clone()
	townCollector := c.Clone()

	// 省 http://www.tcmap.com.cn/shandong/
	c.OnHTML("#pagebody #page_left &gt; table", func(element *colly.HTMLElement) {<!-- -->
		element.ForEach("tr td:first-child", func(i int, e *colly.HTMLElement) {<!-- -->
			city := e.ChildText("a")
			fmt.Println(city)
			relative_url := e.ChildAttr("a", "href")
			if relative_url != "" {<!-- -->
				absURL := e.Request.AbsoluteURL(relative_url)
				// fmt.Println(absURL)
				ctx := colly.NewContext()
				ctx.Put("city", city)
				_ = cityCollector.Request("GET", absURL, nil, ctx, nil)
			}
		})
	})

	// 市 http://www.tcmap.com.cn/shandong/jinan.html
	cityCollector.OnHTML("#pagebody #page_left &gt; table", func(element *colly.HTMLElement) {<!-- -->
		city := element.Request.Ctx.Get("city")
		element.ForEach("tr td:first-child", func(i int, e *colly.HTMLElement) {<!-- -->
			county := e.ChildText("a")
			fmt.Println(city, county)
			relative_url := e.ChildAttr("a", "href")
			if relative_url != "" {<!-- -->
				absURL := e.Request.AbsoluteURL(relative_url)
				//fmt.Println(absURL)
				ctx := colly.NewContext()
				ctx.Put("city", city)
				ctx.Put("county", county)
				_ = countyCollector.Request("GET", absURL, nil, ctx, nil)
			}
		})
	})

	// 区县 http://www.tcmap.com.cn/shandong/lixiaqu.html
	countyCollector.OnHTML("#pagebody #page_left &gt; table", func(element *colly.HTMLElement) {<!-- -->
		city := element.Request.Ctx.Get("city")
		county := element.Request.Ctx.Get("county")
		element.ForEach("tr td:first-child", func(i int, e *colly.HTMLElement) {<!-- -->
			town := e.ChildText("a")
			fmt.Println(city, county, town)
			relative_url := e.ChildAttr("a", "href")
			if relative_url != "" {<!-- -->
				absURL := e.Request.AbsoluteURL(relative_url)
				//fmt.Println(absURL)
				ctx := colly.NewContext()
				ctx.Put("city", city)
				ctx.Put("county", county)
				ctx.Put("town", town)
				_ = townCollector.Request("GET", absURL, nil, ctx, nil)
			}
		})
	})

	// 乡镇 http://www.tcmap.com.cn/shandong/lixiaqu_jiefanglujiedao.html
	townCollector.OnHTML("#pagebody #page_left &gt; table", func(element *colly.HTMLElement) {<!-- -->
		city := element.Request.Ctx.Get("city")
		county := element.Request.Ctx.Get("county")
		town := element.Request.Ctx.Get("town")
		element.ForEach("tr td:first-child", func(i int, e *colly.HTMLElement) {<!-- -->
			village := e.ChildText("a")
			if village != "" {<!-- -->
				fmt.Println(city, county, town, village)
				_ = save(db, city, county, town, village)
			}
		})
	})

	_ = c.Limit(&amp;colly.LimitRule{<!-- -->
		DomainGlob:  "*",
		RandomDelay: 1 * time.Second, // 延时
	})
	_ = c.Visit("http://www.tcmap.com.cn/shandong/")
	// c.Wait()
}

type Village struct {<!-- -->
	ID      uint `gorm:"primaryKey"`
	City    string
	County  string
	Town    string
	Village string
}

func (Village) TableName() string {<!-- -->
	return "village"
}

func save(db *gorm.DB, city string, county string, town string, village string) error {<!-- -->
	villageRecord := Village{<!-- -->City: city, County: county, Town: town, Village: village}
	db = db.Create(&amp;villageRecord)
	db = db.Commit()
	return nil
}



```

文章最后，推荐推荐一个比较好用的代理： <img src="https://img-blog.csdnimg.cn/direct/2f3364ae89c04996a09e964795e07429.png" alt="在这里插入图片描述">
