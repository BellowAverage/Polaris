
--- 
title:  Go 之 redis 处理 
tags: []
categories: [] 

---
Redis是一个开源的内存数据库，支持诸如字符串（string）、哈希（hashe）、列表（list）、集合（set）、带范围查询的排序集合（sorted set）、bitmap、hyperloglog、带半径查询的地理空间索引（geospatial index）和流（stream）等数据结构。 

```
package main

import (
	"context"
	"errors"
	"fmt"
	"github.com/go-redis/redis/v8"
	"time"
)

var rdb *redis.Client

func main() {
	rdb = redis.NewClient(&amp;redis.Options{
		Addr:     "localhost:6379",
		Password: "", // 密码
		DB:       0,  // 数据库
		PoolSize: 20, // 连接池大小
	})
	doCommand()
	doDemo()
	val, err := getValueFromRedis("test", "value")
	fmt.Println(val, err)
	val, err = getValueFromRedis("key", "value")
	fmt.Println(val, err)
	scanKeysDemo()
	delKeysByMatch("key", 5*time.Second)
	pipelineDemo()
}

// doCommand go-redis基本使用示例
func doCommand() {
	ctx, cancel := context.WithTimeout(context.Background(), 500*time.Millisecond)
	defer cancel()

	// 执行命令获取结果
	val, err := rdb.Get(ctx, "key").Result()
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(val)

	// 先获取到命令对象
	cmder := rdb.Get(ctx, "key")
	fmt.Println(cmder.Val(), cmder.Err()) // 获取值和错误

	// 直接执行命令获取错误
	err = rdb.Set(ctx, "key", 10, time.Hour).Err()
	if err != nil {
		fmt.Println(err)
		return
	}
	// 直接执行命令获取值
	value := rdb.Get(ctx, "key").Val()
	fmt.Println(value)
}

// doDemo rdb.Do 方法使用示例
func doDemo() {
	ctx, cancel := context.WithTimeout(context.Background(), 500*time.Millisecond)
	defer cancel()

	// 直接执行命令获取错误
	err := rdb.Do(ctx, "set", "key", 10, "EX", 3600).Err()
	fmt.Println(err)

	// 执行命令获取结果
	val, err := rdb.Do(ctx, "get", "key").Result()
	fmt.Println(val, err)
}

// getValueFromRedis redis.Nil判断
func getValueFromRedis(key, defaultValue string) (string, error) {
	ctx, cancel := context.WithTimeout(context.Background(), 500*time.Millisecond)
	defer cancel()

	val, err := rdb.Get(ctx, key).Result()
	if err != nil {
		if errors.Is(err, redis.Nil) {
			return defaultValue, nil
		}
		return "", err
	}
	return val, nil

}

// scanKeysDemo 按前缀扫描key示例
func scanKeysDemo() {
	ctx, cancel := context.WithTimeout(context.Background(), 500*time.Millisecond)
	defer cancel()
	// 按前缀扫描key
	iter := rdb.Scan(ctx, 0, "key*", 0).Iterator()
	for iter.Next(ctx) {
		fmt.Println("keys", iter.Val())
	}
	if err := iter.Err(); err != nil {
		panic(err)
	}
}

// delKeysByMatch 按match格式扫描所有key并删除
func delKeysByMatch(match string, timeout time.Duration) {
	ctx, cancel := context.WithTimeout(context.Background(), timeout)
	defer cancel()

	iter := rdb.Scan(ctx, 0, match, 0).Iterator()
	for iter.Next(ctx) {
		fmt.Println("val", iter.Val())
		err := rdb.Del(ctx, iter.Val()).Err()
		if err != nil {
			panic(err)
		}
	}
	if err := iter.Err(); err != nil {
		panic(err)
	}
}

// pipelineDemo Redis Pipeline 允许通过使用单个 client-server-client 往返执行多个命令来提高性能
func pipelineDemo() {
	ctx, cancel := context.WithTimeout(context.Background(), 500*time.Millisecond)
	defer cancel()
	pipe := rdb.Pipeline()

	incr := pipe.Incr(ctx, "pipeline_counter")
	pipe.Expire(ctx, "pipeline_counter", time.Hour)

	cmds, err := pipe.Exec(ctx)
	if err != nil {
		panic(err)
	}

	fmt.Println(cmds) // [incr pipeline_counter: 3 expire pipeline_counter 3600: true]
	// 在执行pipe.Exec之后才能获取到结果
	fmt.Println(incr.Val())
}

```


