
--- 
title:  Go 怎么操作 OSS 阿里云对象存储 
tags: []
categories: [] 

---
**1 **

### 介绍



在项目开发中，我们经常会使用对象存储，比如 Amazon 的 S3，腾讯云的 COS，阿里云的 OSS 等。本文我们以阿里云 OSS 为例，介绍怎么使用 Go 操作对象存储。

阿里云 OSS 提供了 REST Api 和 OSS Go SDK，本文我们介绍使用 SDK 操作 OSS，限于篇幅，我们只介绍上传和下载。

**2 **

### 上传

SDK 支持多种上传功能，比如简单上传、追加上传、断点续传上传、分片上传等，我们以简单上传为例，介绍怎么使用 SDK 上传文件，简单上传功能分为流式上传和文件上传两种方式。

所谓流式上传，即使用文件流、网络流等作为 OSS 文件的数据源。

所谓文件上传，即使用本地文件作为 OSS 文件的数据源。

在项目开发中，流式上传（文件流和网络流）相对文件上传，使用的场景比较少。限于篇幅，我们只介绍文件上传这种方式。

在使用 SDK 之前，我们需要先使用 `go get` 获取包（也可以使用 go mod 方式），然后在代码中导入。

```
go get github.com/aliyun/aliyun-oss-go-sdk/oss

```

OSS 存储文件，实际上是将文件存储到 Bucket （存储空间）中，SDK 提供了一些操作 Bucket 的方法。

在获取 Bucket 实例之前，我们需要先获取 Client 实例。

```
func GetOssClient(endpoint, ak, sk string) (client *oss.Client, err error) {
 client, err = oss.New(endpoint, ak, sk)
 return
}

```

阅读上面这段代码，我们通过 SDK 的 `New` 函数，创建了一个 `client` 实例，需要注意的是，我们需要将 OSS 的 `endpoint`、`ak` 和 `sk` 作为参数传入 `New` 函数，更多关于 `client` 的配置选项，请查阅 OSS Go SDK 文档。

我们在获取到 `client` 之后，可以使用 `client` 获取 `bucket`。

```
func GetBucket(client *oss.Client, bucketName string) (bucket *oss.Bucket, err error) {
 bucket, err = client.Bucket(bucketName)
 return
}

```

阅读上面这段代码，我们通过 `client` 提供的 `Bucket` 方法，将我们创建的 bucket 的名字作为参数传入该方法中，创建了一个 `bucket` 实例，然后我们就可以去使用 `bucket` 实例提供的方法。

>  
 我们也可以使用 `client` 实例提供的方法，创建和删除 `Bucket`，但在实际项目开发中，一般都是让运维同事帮忙创建和删除，很少在代码中操作。 


接下来，我们介绍几个 `bucket` 实例提供的方法。

**场景一：上传本地文件**

在项目开发中，经常会遇到需要用户上传本地文件的场景，比如设置头像、上传身份证照片等。

我们以设置头像为例，介绍如何将本地照片上传到 OSS。

示例代码：

```
err = bucket.PutObjectFromFile("a.jpg", "/Users/frank/Downloads/1.jpg")
if err != nil {
    fmt.Println("Error:", err)
    os.Exit(-1)
}

```

阅读上面这段代码，我们使用 `bucket` 实例的 `PutObjectFromFile` 方法，将本地的图片上传到 OSS 中，该方法还可以传入第三个参数（可选参数），用于指定上传文件的属性。

**场景二：上传字符串**

在项目开发中，经常会遇到需要用户上传字符串的场景，比如使用 OSS 存储文本内容。

我们以上传博客为例，介绍如何将字符串上传到 OSS。

示例代码：

```
blogConetnt := "This is my first blog"
err = bucket.PutObject("my-first-blog.txt", strings.NewReader(blogConetnt))
if err != nil {
    fmt.Println("Error:", err)
    os.Exit(-1)
}

```

阅读上面这段代码，我们使用 `bucket` 实例的 `PutObject` 方法，将字符串上传到 OSS 中，该方法还可以传入第三个参数（可选参数），用于指定上传文件的属性。

**场景三：上传字节切片**

在项目开发中，经常会遇到将字节切片格式的数据上传到 OSS 中，比如将 `json.Marshal()` 的字节切片上传到 OSS 中。

示例代码：

```
user := struct {
    UserId   int64  `json:"user_id"`
    UserName string `json:"user_name"`
    Email    string `json:"email"`
}{
    UserId:   10001,
    UserName: "frank",
    Email:    "gopher@88.com",
}
userData, _ := json.Marshal(user)
err = bucket.PutObject("user.txt", bytes.NewReader(userData))
if err != nil {
    fmt.Println("Error:", err)
    os.Exit(-1)
}

```

阅读上面这段代码，我们使用 `bucket` 实例的 `PutObject` 方法，将 `json.Marshal()` 的字节切片上传到 OSS 中。

>  
 我们也可以使用 `bucket` 实例的 `PutObject` 方法上传本地文件，但是一般都是使用 `PutObjectFromFile` 方法。 


**3 **

### 下载

OSS Go SDK 同样支持多种下载方式，相比文件上传，在实际项目开发中，文件下载的使用场景并不多，一般都是查询（读取）文件。

为了文章的完整，我们介绍了文件上传，也顺带简单介绍一下文件下载。

关于文件下载，SDK 也是支持流式下载和本地文件下载，本文我们以本地文件下载为例，介绍怎么使用 SDK 下载 OSS 中的文件到本地。

示例代码：

```
err = bucket.GetObjectToFile("a.jpeg", "/Users/frank/Downloads/oss.jpeg")
if err != nil {
    fmt.Println("Error:", err)
    os.Exit(-1)
}

```

阅读上面这段代码，我们使用 `bucket` 实例的 `GetObjectToFile` 方法，将 OSS 中的文件 `a.jpeg` 下载到本地。

** 4 **

### 总结

本文我们介绍 Go 怎么操作 OSS 阿里云对象存储，主要介绍了 OSS Go SDK 关于文件上传和文件下载的几个方法，建议感兴趣的读者朋友们阅读 OSS Go SDK 和OSS Go SDK Api 的相关文档，自己尝试写文件查询的代码。


