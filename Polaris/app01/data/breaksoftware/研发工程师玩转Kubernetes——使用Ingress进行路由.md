
--- 
title:  研发工程师玩转Kubernetes——使用Ingress进行路由 
tags: []
categories: [] 

---


#### 大纲
- - - - - - 


依据微服务理念，我们希望每个独立的功能由一个服务支持。比如有两个接口：http://www.xxx.com/plus和http://www.xxx.com/minus，前者由一个叫plus-service的服务支持，后者由一个叫minus-service的服务支持。这样就需要一个路由层，在前方将/plus请求路由到plus-service；将/minus路由到minus-service。本文介绍的ingress就可以起到路由的作用。 <img src="https://img-blog.csdnimg.cn/d9b27363af854f2db549923f3c0cd2c4.png" alt="在这里插入图片描述"> 我们借用中的simple-http的镜像，使用版本号来访问不同的镜像对应的服务。比如使用/v1访问simple_http_v1对应的镜像，使用/v2访问simple_http_v2对应的镜像。 <img src="https://img-blog.csdnimg.cn/7fbfb99c723d48689c22f40ca5c1f49d.png" alt="在这里插入图片描述">

## 启用Ingress

这个系列我们使用microk8s进行演示，于是需要启用这个插件。

```
microk8s enable ingress

```

## 启动响应的Service

相关知识可以参见。具体的清单文件如下：

```
# simple_http_v1_service.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: simple-http-v1-deployment
spec:
  selector:
    matchLabels:
      app: simple-http-v1
  template:
    metadata:
      labels:
        app: simple-http-v1
    spec:
      containers: 
      - name: simple-http-v1
        image: localhost:32000/simple_http:v1
        ports:
        - containerPort: 8888
---
apiVersion: v1
kind: Service
metadata:
  name: simple-http-v1-service
spec:
  selector:
    app: simple-http-v1
  ports:
  - port: 80
    targetPort: 8888

```

```
# simple_http_v2_service.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: simple-http-v2-deployment
spec:
  selector:
    matchLabels:
      app: simple-http-v2
  template:
    metadata:
      labels:
        app: simple-http-v2
    spec:
      containers: 
      - name: simple-http-v2
        image: localhost:32000/simple_http:v2
        ports:
        - containerPort: 8888
---
apiVersion: v1
kind: Service
metadata:
  name: simple-http-v2-service
spec:
  selector:
    app: simple-http-v2
  ports:
  - port: 80
    targetPort: 8888

```

使用下面命令创建simple-http-v1-service和simple-http-v2-service两个Service，为Ingress路由提供基础服务。

```
kubectl create -f  simple_http_v1_service.yaml simple_http_v2_service.yaml

```

## 创建Ingress

清单文件如下：

```
# simple_http_ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: simple-http-ingress
  labels:
    name: simple-http-ingress
spec:
  rules:
  - http:
      paths:
      - pathType: Prefix
        path: "/v1"
        backend:
          service:
            name: simple-http-v1-service
            port: 
              number: 80
      - pathType: Prefix
        path: "/v2"
        backend:
          service:
            name: simple-http-v2-service
            port: 
              number: 80

```

spec.rules用于指定不同http地址的路由信息。上例中pathType: Prefix表示通过前缀匹配，如果匹配到/v1则路由到simple-http-v1-service；如果匹配到/v2，则路由到simple-http-v2-service。 使用下面命令创建该ingress

```
kubectl create -f simple_http_ingress.yaml

```

>  
 ingress.networking.k8s.io/simple-http-ingress created 


## 测试

```
curl 127.0.0.1/v1

```

>  
 This service’s version is 1 IP is:10.1.62.173 


```
curl 127.0.0.1/v2

```

>  
 This service’s version is 2 IP is:10.1.62.163 


通过测试结果看，ingress将请求正确路由到对应的service上了。

## 刪除

```
kubectl delete ingress simple-http-ingress
kubectl delete service simple-http-v1-service simple-http-v2-service
kubectl delete deployments.apps simple-http-v1-deployment simple-http-v2-deployment 

```

## 参考资料
- 