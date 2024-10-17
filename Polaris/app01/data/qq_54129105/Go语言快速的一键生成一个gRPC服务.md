
--- 
title:  Go语言快速的一键生成一个gRPC服务 
tags: []
categories: [] 

---
**目录**



















##  前言

>  
         由于近期因为一些事情很久没更了今天带来一个Go语言如何快速的一键生成一个gRPC服务的教程 


1

## 介绍

Micro(Go开源项目)为我们提供了一套微服务解决方案，**<u>它主要包括两个部分</u>**，分别是微服务框架 go-micro 和命令行工具 micro。

其中， go-micro 是一个易用且强大的框架，很多在生产环境运行的项目中在使用 go-micro v1.x 或 v2.x 版本，<u>**因为 v3 版本的变动较大，所以很少项目会选择升级到 v3 版本**</u>。

命令行工具 micro 也是基于 go-micro 开发的，它提供了很多便捷功能。

虽然命令行工具不是必须的，我们不使用它，也可以使用 go-micro 创建一个 gRPC 服务。但是，**<u>使用命令行工具 micro 可以更加便捷的开发和管理项目</u>**。

此外，官方还提供了一些插件 go-plugins，go-micro 使用插件架构设计，可以非常灵活地组合各种功能，我们也可以自己开发插件，满足我们自己的个性化需求。本文不涉及插件，暂时不做详细介绍。

我们在之前的文章中介绍过不借助命令行工具 micro，直接使用 go-micro 手动编写代码创建一个 gRPC 服务，本文我们介绍怎么使用命令行工具 micro 自动创建一个模板项目。

2

##  使用命令行工具 micro 生成 gRPC 服务

### 安装：

```
GO111MODULE=on go get github.com/micro/micro/v2@v2.4.0
```

### 创建项目：

```
micro new --namespace=com.foo --gopath=false hello
```

阅读上面这段命令行代码，我们使用命令行工具 micro 创建一个项目，服务名称是 hello。

命令行参数：
- micro new 使用命令行工具 micro 和其子命令 new 创建一个 gRPC 服务。- --namespcae=com.foo 指定服务的命名空间。- --gopath=fase 在当前目录生成代码，而不是生成到 GOPATH 目录。- hello 指定服务名称。
>  
 注意：micro new 的其他参数，感兴趣的读者朋友们请查阅文档。 


我们在运行上面这段命令行代码之后，终端会输出以下内容：

```
Creating service com.foo.service.hello in hello


.
├── main.go
├── generate.go
├── plugin.go
├── handler
│   └── hello.go
├── subscriber
│   └── hello.go
├── proto/hello
│   └── hello.proto
├── Dockerfile
├── Makefile
├── README.md
├── .gitignore
└── go.mod


download protobuf for micro:

brew install protobuf
go get -u github.com/golang/protobuf/{proto,protoc-gen-go}
go get -u github.com/micro/protoc-gen-micro/v2

compile the proto file hello.proto:

cd hello
protoc --proto_path=.:$GOPATH/src --go_out=. --micro_out=. proto/hello/hello.proto
```

阅读上面终端输出的内容，我们可以发现，micro new 在 hello 目录中，为我们自动生成了模板代码。

### 安装 protobuf 和依赖项：

因为 micro 使用 protobuf 定义服务接口，所以我们需要先安装 protobuf 和依赖项。

```
brew install protobuf
go get -u github.com/golang/protobuf/{proto,protoc-gen-go}
GO111MODULE=on go get -u github.com/micro/protoc-gen-micro/v2
```

在我们运行 micro new 命令之后，终端中已经为我们输出安装 protobuf 和依赖项的提示，并且提供了安装命令，我们只需运行安装命令即可。

需要注意的是，protoc-gen-micro 是由 micro 官方开发的 protobuf 的扩展，用于生成 micro 的相关代码，我们在安装时，需要显式开启 Go Module。

>  
 注意：关于 protobuf 的相关内容，我们在之前的文章中介绍过，限于篇幅，本文不再赘述。 


### 构建并运行服务：

虽然 micro new 在生成代码时，为我们生成了一个 Makefile 文件，其中，包含一些常用的任务，我们可以使用 make 命令运行该文件中定义好的任务。

但是我决定在本文中不使用 make 命令，原因是读者朋友们可能有人不熟悉 make，为了避免增加这部分读者的学习成本，我仍然使用 go 命令。

需要注意的是，我们需要先运行 go get 安装指定版本的 go-micro，目的是避免在代码编译期间，自动安装最新版本的 go-micro。

```
cd hello
GO111MODULE=on 
go get github.com/micro/go-micro/v2@v2.4.0
```

>  
 注意：指定 go-micro 的版本，目的是避免因为版本问题，导致不可预知的陷阱。 


在我们使用 go build 构建项目之前，我们先编译 hello.proto 文件。

编译 hello.proto 文件：

```
cd hello
protoc --proto_path=.:$GOPATH/src --go_out=. --micro_out=. proto/hello/hello.proto
```

运行编译 hello.proto 文件的命令之后，我们可以发现在 proto/hello 目录中多出两个文件，分别是 hello.pb.go 和 hello.pb.micro.go。

构建：

```
go build -o hello-service *.go
```

运行构建命令之后，我们可以发现目录中多出一个二进制文件 hello-service。

运行服务：

```
./hello-service
2023-03-04 17:00:54  level=info Starting [service] com.foo.service.hello
2023-03-04 17:00:54  level=info Server [grpc] Listening on [::]:50669
2023-03-04 17:00:54  level=info Broker [eats] Connected to [::]:50671
2023-03-04 17:00:54  level=info Registry [mdns] Registering node: com.foo.service.hello-e0057b02-6432-4d0d-b1e4-2b87ea1034a3
2023-03-04 17:00:54  level=info Subscribing to topic: com.foo.service.hello
```

到此，我们已经完成使用命令行工具 micro new 创建一个服务名称为 hello 的 gRPC 服务，并且成功构建并运行该服务。

>  
 注意：如果遇到一些无法解决的问题，可以尝试删除 GOPATH/pkg/mod 目录下的文件后重试。 


3

## 总结

本文我们介绍怎么使用命令行工具 micro new 创建一个 gRPC 服务，并且怎么构建和运行服务。

需要注意的是，在构建之前，我们先指定 go-micro 版本，避免在代码编译时使用最新版本，掉入不可预知的陷阱。

在安装 micro 官方开发的 protobuf 扩展 protoc-gen-micro 时，我们一定要显式开启 Go Module。

我们安装命令行工具 micro之前，需要先设置代理。因为官方已不维护 go-micro 的 v1 和 v2 版本，所以，我们需要使用代理安装，推荐使用  。

参考资料：




