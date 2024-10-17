
--- 
title:  postman发送json嵌套， 后端 @RequestBody 接收不到 
tags: []
categories: [] 

---
遇到了一个很奇葩的问题，具体是这样的： postman 通过 post 方式发送请求，请求参数是一个嵌套的json，后端是@RequestBody修饰的实体类接参的， <img src="https://img-blog.csdnimg.cn/703a780f845b40a5aedf644233535df3.png" alt="在这里插入图片描述"> 具体的json数据：

```
{<!-- -->
    "ipAddress":"192.168.110.179",
     "ipv6Address":"::",
     "portNo":"38050",
     "protocol":"HTTP",
     "macAddress":"ec:c8:9c:c4:5c:b3",
     "channelID":"1",
     "dateTime":"2021-12-14T19:23:52+08:00",
     "activePostCount":"157",
     "eventType":"ANPR",
     "eventState":"active",
     "eventDescription":"ANPR",
     "channelName":"IP CAPTURE CAMERA",
     "deviceID":"jnjtzf0001",
     "aNPR":{<!-- -->
         "licensePlate":"车牌",
         "line":"1",
         "confidenceLevel":"0",
         "plateType":"unknown",
         "plateColor":"blue",
         "licenseBright":"0",
         "pilotsafebelt":"unknown",
         "vicepilotsafebelt":"unknown",
         "pilotsunvisor":"unknown",
         "vicepilotsunvisor":"unknown",
         "envprosign":"unknown",
         "dangmark":"unknown",
         "uphone":"unknown",
         "pendant":"unknown",
         "tissueBox":"unknown",
         "label":"unknown",
         "decoration":"unknown",
         "plateCharBelieve":"0",
         "speedLimit":"0",
         "illegalInfo":{<!-- -->
             "illegalCode":"0"
         },
         "vehicleType":"unknown",
         "featurePicFileName":"1",
         "detectDir":"8",
         "detectType":"1",
         "barrierGateCtrlType":"0",
         "alarmDataType":"0",
         "dwIllegalTime":"0",
         "vehicleInfo":{<!-- -->
             "color":"white"
         },
         "gPSInfo":{<!-- -->
             "longitude":{<!-- -->
                 "degree":"117",
                  "minute":"6",
                   "sec":"49.910000"
             },
              "latitude":{<!-- -->
                 "degree":"117",
                  "minute":"6",
                   "sec":"49.910000"
             }
         }
     },
      "UUID":"602cf998-1dd2-11b2-a842-be6ebc977415",
      "picNum":"1"
}

```

后端： <img src="https://img-blog.csdnimg.cn/c0963c2d4d2440e1ae7b43da82852653.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/33762b97803b49219e54003dc9260859.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/adb76971bf8640ecb6b920b42c3a12af.png" alt="在这里插入图片描述"> 大家知道以上事例即可。 出现的问题是： 发送请求后，没能收到外层实体类的参数，内层的ANPR对象，一直是 null . 解决的方式是： 给该属性添加注解 @JsonProperty(“aNPR”)<img src="https://img-blog.csdnimg.cn/2f70d8fbd0fa40a4bea4c0623f9787a9.png" alt="在这里插入图片描述"> 注：有时候接收的项目，不是很规范，请大大多多留意！！！
