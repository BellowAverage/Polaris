
--- 
title:  axios请求，传file格式的数据以及其他参数，传参data默认转为json格式数据问题解决 
tags: []
categories: [] 

---
>  
 Axios 的 POST 请求默认是以 JSON 格式传递参数的。 Axios 默认使用 application/json 作为请求头的Content-Type，并将数据转换为 JSON 格式发送。 如果你想使用其他数据格式传递参数，比如application/x-www-form-urlencoded 或multipart/form-data，你需要进行相应的配置。设置请求头 hesders 里面的 Content-Type。 


传带文件File的参数，如果传参的数据不对，可以检查一下两点：
1. 没有将传参的普通对象转为FormData对象
```
// 将普通js对象转为FormData对象
export function paramsToFormData(obj) {<!-- -->
  const formData = new FormData();
  Object.keys(obj).forEach((key) =&gt; {<!-- -->
      if (obj[key] instanceof Array) {<!-- -->
        obj[key].forEach((item) =&gt; {<!-- -->
          formData.append(key, item);
        });
        return;
      }
      formData.append(key, obj[key]);
    });
  return formData;
}


```
1. axios请求没有设置如下请求头
```
  headers: {<!-- -->
    'Content-Type': 'multipart/form-data',
  },

```
