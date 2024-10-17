
--- 
title:  Tensorflow Serving部署模型 
tags: []
categories: [] 

---
TensorFlow Serving是google开源的一个适用于部署机器学习模型，具有灵活、高性能、可用于生产环境的模型框架。 它支持**模型版本控制**和**回滚**、** 支持并发**、**支持多模型部署、** **支持模型热更新**等，由于这些特性，使得我们不需要为部署线上服务而操心，只需要训练好线下模型即可。 同时，TensorFlow Serving还提供gRPC和REST API两种接口访问形式，其中gRPC接口对应的端口号为8500，而REST API对应的端口号为8501。

基于TensorFlow Serving的持续集成框架还是挺简明的，基本分三个步骤：

>  
 **模型训练**：这是大家最熟悉的部分，主要包括数据的收集和清洗、模型的训练、评测和优化；**模型上线**：前一个步骤训练好的模型在TF Server中上线；**服务使用**：客户端通过gRPC和RESTfull API两种方式同TF Servering端进行通信，并获取服务。 


##  一、TensorFlow Serving

### 1.1安装

目前TensorFlow Serving提供Docker、APT（二进制安装）和源码编译三种安装方式，其中Docker方式的安装相对来说较为简单，而且对后期项目部署的环境依赖不强，项目部署与迁移较为容易，推荐使用方式进行TensorFlow Serving的安装。

```
 docker pull tensorflow/serving
```

### 1.2启动

```
docker run -p 8501:8501 --name yc_model -v /home/tensorflow/model_yc/:/models/model_yc  -e MODEL_NAME=model_yc tensorflow/serving
```

启动成功日志：

<img alt="" height="198" src="https://img-blog.csdnimg.cn/20210713165728366.png" width="1200">

后台启动：

```
docker run -d -p 8501:8501 --name yc_model -v /home/tensorflow/model_yc/:/models/model_yc  -e MODEL_NAME=model_yc tensorflow/serving
```

### 二、查看模型情况

### 2.1查看模型概况

>  
 浏览器访问： 


<img alt="" height="211" src="https://img-blog.csdnimg.cn/20210713165921620.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="374">

### 2.2查看模型metadata数据情况（重要）

>  
 浏览器访问： 




```
{
"model_spec":{
 "name": "model_yc",
 "signature_name": "",
 "version": "1"
}
,
"metadata": {"signature_def": {
 "signature_def": {
  "serving_default": {
   "inputs": {
    "input_data": {
     "dtype": "DT_FLOAT",
     "tensor_shape": {
      "dim": [
       {
        "size": "-1",
        "name": ""
       },
       {
        "size": "4",
        "name": ""
       }
      ],
      "unknown_rank": false
     },
     "name": "serving_default_input_data:0"
    }
   },
   "outputs": {
    "output_data": {
     "dtype": "DT_FLOAT",
     "tensor_shape": {
      "dim": [
       {
        "size": "-1",
        "name": ""
       },
       {
        "size": "1",
        "name": ""
       }
      ],
      "unknown_rank": false
     },
     "name": "StatefulPartitionedCall:0"
    }
   },
   "method_name": "tensorflow/serving/predict"
  },
  "__saved_model_init_op": {
   "inputs": {},
   "outputs": {
    "__saved_model_init_op": {
     "dtype": "DT_INVALID",
     "tensor_shape": {
      "dim": [],
      "unknown_rank": true
     },
     "name": "NoOp"
    }
   },
   "method_name": ""
  }
 }
}
}
}

```

### 2.3API测试

>  
  
 #model_yc：模型名 
 参数： 
 {<!-- --> 
     "signature_name":"serving_default", 
     "instances":[ 
         {<!-- --> 
             "input_data":[[22],[11],[34],[27],[36],[36],[10],[8]] 
         } 
     ] 
 } 


<img alt="" height="615" src="https://img-blog.csdnimg.cn/20210713172838680.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

 【补充说明】：

**1.signature_name（serving_default）**

```
signature_key = 'traffic_predict'

builder.add_meta_graph_and_variables(
    ......,
    tags=[tf.saved_model.tag_constants.SERVING], # 预定义值 SERVING
    signature_def_map={signature_key: signature}, # signature_def_map={'traffic_predict':signature},
    ......
)

```

** 2.method_name**

```
method_name=tf.saved_model.signature_constants.PREDICT_METHOD_NAME 
# method_name = 'tensorflow/serving/predict'

```

如果是多参数呢？

>  
 {<!-- -->     "signature_name": "traffic_predict",     "instances":[         {<!-- -->             "input_1": [1],             "input_2": [2],             "input_3": [3]         }     ] } 


  到这里，简单的模型部署就完成了，那么一开始说的Tensorflow Serving支持**模型版本控制**和**回滚**、** 支持并发**、**支持多模型部署、** **支持模型热更新**等特性是如何体现的呢？

## 三、部署多模型

模型结构：

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210126113012113.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTI4NTY4NjY=,size_16,color_FFFFFF,t_70">

**1.在multiModel文件夹下新建一个配置文件model.config**【相当于配置路由】

```
model_config_list:{
    config:{
      name:"model1",
      base_path:"/models/multiModel/model1",
      model_platform:"tensorflow"
    },
    config:{
      name:"model2",
      base_path:"/models/multiModel/model2",
      model_platform:"tensorflow"
    },
    config:{
      name:"model3",
      base_path:"/models/multiModel/model3",
      model_platform:"tensorflow"
    } 
}

```

** 2.启动TensorFlow Serving容器**

```
docker run -p 8501:8501 \
 --mount type=bind,source=/home/tensorflow/serving/tensorflow_serving/servables/tensorflow/testdata/multiModel/,target=/models/multiModel \
 -t tensorflow/serving --model_config_file=/models/multiModel/models.config

```

**3.查看模型【**访问网址为 models/model1, 地址中不包含 multiModel **】**

```
http://xx.xx.xx.xx:8501/v1/models/model1
http://xx.xx.xx.xx:8501/v1/models/model1/metadata

```

那么，同一个模型如何部署多版本呢？

## 四、同一模型部署多版本

修改model.config文件，增加model_version_policy:

```
model_config_list:{
    config:{
      name:"model1",
      base_path:"/models/multiModel/model1",
      model_platform:"tensorflow",
      model_version_policy:{
        all:{}
      }
    },
    config:{
      name:"model2",
      base_path:"/models/multiModel/model2",
      model_platform:"tensorflow"
    },
    config:{
      name:"model3",
      base_path:"/models/multiModel/model3",
      model_platform:"tensorflow"
    } 
}

```

请求的URL为：

>  
  

