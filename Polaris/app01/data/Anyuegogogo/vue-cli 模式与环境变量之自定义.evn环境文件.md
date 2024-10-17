
--- 
title:  vue-cli 模式与环境变量之自定义.evn环境文件 
tags: []
categories: [] 

---
#### 首先NODE_ENV只会是：

NODE_ENV只有如下三种： “development”、“production” 或 “test”

>  
 NODE_ENV - 会是 “development”、“production” 或 “test” 中的一个。具体的值取决于应用运行的模式。 NODE_ENV 将决定您的应用运行的模式，是开发，生产还是测试，因此也决定了创建哪种 webpack 配置。 


#### 默认的模式与环境变量：

development 模式用于 vue-cli-service serve 载入.env.development环境文件 test 模式用于 vue-cli-service test:unit production 模式用于 vue-cli-service build 和 vue-cli-service test:e2e 载入.env.production环境文件

```
你可以通过传递 --mode 选项参数为命令行覆写默认的模式。例如，如果你想要在构建命令中使用开发环境变量：

```

#### 自定义模式与.env环境文件

例如： .env.gzpro “build:gzpro”: “vue-cli-service build --mode gzpro” 这样运行npm run build:gzpro载入的就是模式为gzpro的.env.gzpro环境文件。注意如果用的是构建命令想打包生产环境的，就应该在.env.gzpro文件中指定NODE_ENV变量为"production"，因为默认会用 “development”。

```
如果文件内部不包含 NODE_ENV 变量，它的值将取决于模式，例如，在 production 模式下被设置为 "production"，在 test 模式下被设置为 "test"，默认则是 "development"。

```


