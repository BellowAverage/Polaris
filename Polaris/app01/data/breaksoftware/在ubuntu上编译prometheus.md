
--- 
title:  在ubuntu上编译prometheus 
tags: []
categories: [] 

---


#### 大纲
- - - <ul><li>- <ul><li>- - - - 


prometheus的编译并不难，核心是要将编译环境配置到符合要求的地步，否则就会出现各种错误，而且难以排查。 我们主要需要**关心go、npm和nodejs的版本**。 以下步骤亲测有效。

## 系统环境

使用下面指令升级软件（非必要）

```
sudo apt update
sudo apt upgrade

```

升级过后我的系统环境信息如下

```
cat /proc/version

```

>  
 Linux version 5.15.0-101-generic (buildd@lcy02-amd64-031) (gcc (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0, GNU ld (GNU Binutils for Ubuntu) 2.34) #111~20.04.1-Ubuntu SMP Mon Mar 11 15:44:43 UTC 2024 


这一步主要是为了展现我的实验环境。

## 编译环境

安装各种代码拉取和编译过程中的工具

```
sudo apt install git
sudo snap install go --classic
sudo apt install nodejs
sudo apt install npm

```

### 默认的版本

#### Golang

```
go version

```

>  
 go version go1.22.1 linux/amd64 


#### Nodejs

```
node --version

```

>  
 v10.19.0 


#### NPM

```
npm version

```

>  
 { npm: ‘6.14.4’, ares: ‘1.15.0’, brotli: ‘1.0.7’, cldr: ‘36.1’, http_parser: ‘2.9.3’, icu: ‘66.1’, modules: ‘64’, napi: ‘5’, nghttp2: ‘1.40.0’, node: ‘10.19.0’, openssl: ‘1.1.1f’, tz: ‘2024a’, unicode: ‘13.0’, uv: ‘1.34.2’, v8: ‘6.8.275.32-node.55’, zlib: ‘1.2.11’ } 


### 更新Nodejs和NPM

上述nodejs和npm的版本比较老，需要我们手动升级它们。

```
sudo npm install -g n
sudo n lts
sudo n prune

```

重启终端，执行下面指令

```
npm install -g npm@latest

```

#### Nodejs

```
node --version

```

>  
 v20.12.0 


#### NPM

```
npm version

```

>  
 {<!-- --> npm: ‘10.5.0’, node: ‘20.12.0’, acorn: ‘8.11.3’, ada: ‘2.7.6’, ares: ‘1.27.0’, base64: ‘0.5.2’, brotli: ‘1.1.0’, cjs_module_lexer: ‘1.2.2’, cldr: ‘44.1’, icu: ‘74.2’, llhttp: ‘8.1.1’, modules: ‘115’, napi: ‘9’, nghttp2: ‘1.60.0’, nghttp3: ‘0.7.0’, ngtcp2: ‘0.8.1’, openssl: ‘3.0.13+quic’, simdutf: ‘4.0.8’, tz: ‘2024a’, undici: ‘5.28.3’, unicode: ‘15.1’, uv: ‘1.46.0’, uvwasi: ‘0.0.20’, v8: ‘11.3.244.8-node.19’, zlib: ‘1.3.0.1-motley-40e35a7’ } 


## 编译

```
git clone https://github.com/prometheus/prometheus.git
cd prometheus
make build

```

编译过程比较漫长，需要耐心等待。

## 运行

```
./prometheus --config.file=./documentation/examples/prometheus.yml 

```

在浏览器中打开http://localhost:9090 可以看到页面如下，说明编译和运行没有问题。 <img src="https://img-blog.csdnimg.cn/direct/483f7d2fcea84e51b09494302bb47dc8.png#pic_center" alt="在这里插入图片描述">
