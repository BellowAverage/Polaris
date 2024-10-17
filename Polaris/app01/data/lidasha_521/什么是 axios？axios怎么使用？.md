
--- 
title:  什么是 axios？axios怎么使用？ 
tags: []
categories: [] 

---
>  
 Axios 是一个基于 promise 的 HTTP 库，可以用在浏览器和 node.js 中。 




#### 文章目录
- - - - 


## 1.什么是 axios？
- **Axios 是一个基于 promise 的 HTTP 库，可以用在浏览器和 node.js 中。**
## 2.axios的使用
<li>引用`js`的两种方式： 
  <ul>- 在线引用：`&lt;script src="https://unpkg.com/axios/dist/axios.min.js"&gt;&lt;/script&gt;`- 本地引用：访问 另存为`axios.min.js`
## 3.案例
<li> **axios的get请求的两种方式（传参方式不同）** 
  <ul>- 方式一：URL参数拼接方式
```
var baseURL = "http://localhost:8080"
axios.get(baseURL + '/user?ID=12345')
.then(res =&gt; {<!-- -->
    console.log(res);
})；

```
- 方式二：params:{param1:value1 ,param2: value2 } 方式
```
var baseURL = "http://localhost:8080"
var url = baseUrl + "/user/login"
axios.get(url, {<!-- -->
	params: {<!-- -->
		username: vm.username,
	    password: vm.password
	}
}).then(res =&gt; {<!-- -->
	console.log(res);
}

```

axios的post请求

```
var baseURL = "http://localhost:8080"
var url = baseUrl + "/user/regist"
axios.post(url, {<!-- -->
	username: 'zhangsan',
	password: '123456'
}).then(res =&gt; {<!-- -->
	console.log(res);
});

```
- 执行多个并发请求
```
var baseURL = "http://localhost:8080"
function getUserInfo() {<!-- -->
  return axios.get(baseURL + '/user/getUserInfo?userId=1');
}

function getUserDetail() {<!-- -->
  return axios.get(baseURL + '/user/getUserDetail?userId=1');
}

axios.all([getUserInfo(), getUserDetail()])
.then(axios.spread(function (userInfo, userDetail) {<!-- -->
  // 两个请求现在都执行完成
	......
}));

```
<li> 自定义配置：**<strong>axios(config)**</strong> 
  <ul>- 自定义配置项，只有 `url` 是必需的。如果没有指定 `method` ，请求将默认使用 `get`方法。
```
{<!-- -->
   
  url: '/user', // `url` 是用于请求的服务器 URL（必须）

  method: 'get', // `method` 是创建请求时使用的方法（默认）

  // `baseURL` 将自动加在 `url` 前面，除非 `url` 是一个绝对 URL。
  // 它可以通过设置一个 `baseURL` 便于为 axios 实例的方法传递相对 URL
  baseURL: 'https://some-domain.com/api/',

  // `transformRequest` 允许在向服务器发送前，修改请求数据
  // 只能用在 'PUT', 'POST' 和 'PATCH' 这几个请求方法
  // 后面数组中的函数必须返回一个字符串，或 ArrayBuffer，或 Stream
  transformRequest: [function (data, headers) {<!-- -->
    // 对 data 进行任意转换处理
    return data;
  }],

  // `transformResponse` 在传递给 then/catch 前，允许修改响应数据
  transformResponse: [function (data) {<!-- -->
    // 对 data 进行任意转换处理
    return data;
  }],

  // `headers` 是即将被发送的自定义请求头
  headers: {<!-- -->'X-Requested-With': 'XMLHttpRequest'},

  // `params` 是即将与请求一起发送的 URL 参数
  // 必须是一个无格式对象(plain object)或 URLSearchParams 对象
  params: {<!-- -->
    ID: 12345
  },

   // `paramsSerializer` 是一个负责 `params` 序列化的函数
  // (e.g. https://www.npmjs.com/package/qs, http://api.jquery.com/jquery.param/)
  paramsSerializer: function(params) {<!-- -->
    return Qs.stringify(params, {<!-- -->arrayFormat: 'brackets'})
  },

  // `data` 是作为请求主体被发送的数据
  // 只适用于这些请求方法 'PUT', 'POST', 和 'PATCH'
  // 在没有设置 `transformRequest` 时，必须是以下类型之一：
  // - string, plain object, ArrayBuffer, ArrayBufferView, URLSearchParams
  // - 浏览器专属：FormData, File, Blob
  // - Node 专属： Stream
  data: {<!-- -->
    firstName: 'Fred'
  },

  // `timeout` 指定请求超时的毫秒数(0 表示无超时时间)
  // 如果请求话费了超过 `timeout` 的时间，请求将被中断
  timeout: 1000,

  withCredentials: false, // 表示跨域请求时是否需要使用凭证（默认）

  // `adapter` 允许自定义处理请求，以使测试更轻松
  // 返回一个 promise 并应用一个有效的响应 (查阅 [response docs](#response-api)).
  adapter: function (config) {<!-- -->
    /* ... */
  },

 // `auth` 表示应该使用 HTTP 基础验证，并提供凭据
  // 这将设置一个 `Authorization` 头，覆写掉现有的任意使用 `headers` 设置的自定义 `Authorization`头
  auth: {<!-- -->
    username: 'janedoe',
    password: 's00pers3cret'
  },

   // `responseType` 表示服务器响应的数据类型，可以是 'arraybuffer', 'blob', 'document', 'json', 'text', 'stream'
  responseType: 'json', // default

  // `responseEncoding` indicates encoding to use for decoding responses
  // Note: Ignored for `responseType` of 'stream' or client-side requests
  responseEncoding: 'utf8', // default

   // `xsrfCookieName` 是用作 xsrf token 的值的cookie的名称
  xsrfCookieName: 'XSRF-TOKEN', // default

  // `xsrfHeaderName` is the name of the http header that carries the xsrf token value
  xsrfHeaderName: 'X-XSRF-TOKEN', // default

   // `onUploadProgress` 允许为上传处理进度事件
  onUploadProgress: function (progressEvent) {<!-- -->
    // Do whatever you want with the native progress event
  },

  // `onDownloadProgress` 允许为下载处理进度事件
  onDownloadProgress: function (progressEvent) {<!-- -->
    // 对原生进度事件的处理
  },

   // `maxContentLength` 定义允许的响应内容的最大尺寸
  maxContentLength: 2000,

  // `validateStatus` 定义对于给定的HTTP 响应状态码是 resolve 或 reject  promise 。如果 `validateStatus` 返回 `true` (或者设置为 `null` 或 `undefined`)，promise 将被 resolve; 否则，promise 将被 rejecte
  validateStatus: function (status) {<!-- -->
    return status &gt;= 200 &amp;&amp; status &lt; 300; // default
  },

  // `maxRedirects` 定义在 node.js 中 follow 的最大重定向数目
  // 如果设置为0，将不会 follow 任何重定向
  maxRedirects: 5, // default

  // `socketPath` defines a UNIX Socket to be used in node.js.
  // e.g. '/var/run/docker.sock' to send requests to the docker daemon.
  // Only either `socketPath` or `proxy` can be specified.
  // If both are specified, `socketPath` is used.
  socketPath: null, // default

  // `httpAgent` 和 `httpsAgent` 分别在 node.js 中用于定义在执行 http 和 https 时使用的自定义代理。允许像这样配置选项：
  // `keepAlive` 默认没有启用
  httpAgent: new http.Agent({<!-- --> keepAlive: true }),
  httpsAgent: new https.Agent({<!-- --> keepAlive: true }),

  // 'proxy' 定义代理服务器的主机名称和端口
  // `auth` 表示 HTTP 基础验证应当用于连接代理，并提供凭据
  // 这将会设置一个 `Proxy-Authorization` 头，覆写掉已有的通过使用 `header` 设置的自定义 `Proxy-Authorization` 头。
  proxy: {<!-- -->
    host: '127.0.0.1',
    port: 9000,
    auth: {<!-- -->
      username: 'mikeymike',
      password: 'rapunz3l'
    }
  },

  // `cancelToken` 指定用于取消请求的 cancel token
  // （查看后面的 Cancellation 这节了解更多）
  cancelToken: new CancelToken(function (cancel) {<!-- -->
  })
}

```
- 案例
```
// 获取远端图片
axios({<!-- -->
  method:'get',
  url:'http://bit.ly/2mTM3nY',
  responseType:'stream'
})
  .then(function(response) {<!-- -->
  response.data.pipe(fs.createWriteStream('ada_lovelace.jpg'))
});

```
<li>响应结构 
  <ul>- 也就是 console.log(res) 中的 res(**`response`**)
<img src="https://img-blog.csdnimg.cn/906a7701394d4c5f8782b4ef9e785178.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

```
{<!-- -->
  data: {<!-- -->},  // `data` 由服务器提供的响应

  status: 200, // `status` 来自服务器响应的 HTTP 状态码

  statusText: 'OK', // `statusText` 来自服务器响应的 HTTP 状态信息

  headers: {<!-- -->}, // `headers` 服务器响应的头

  config: {<!-- -->},  // `config` 是为请求提供的配置信息

  request: {<!-- -->} // `request` 是生成此响应的请求
}

```

## 4.VSCode中自定义axios的get/post快速引用模板
- 设置—&gt;用户片段—&gt;全局配置—&gt;定义模板名称—&gt;回车—&gt;插入自定义模板
<img src="https://img-blog.csdnimg.cn/826ea86a5737494589fb12731b6cced2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_14,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/571608e52e3f48ee98e1ec6ed8b5b7d9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/50403976107342faa9683be29c8f9ea1.png#pic_center" alt="在这里插入图片描述">
- axios的GET请求模板
```
"Print to console": {<!-- -->
	"scope": "javascript,typescript",
	"prefix": "axios-get",
	"body": [
		"axios.get(url, {",
		"    params: {",
		"        参数1: '参数1的值',",
		"        参数2: '参数2的值'",
		"    }",
		"}).then(res =&gt; {",
		"    var data = res.data",
		"    console.log(data);",
		"});",
	],
	"description": "执行 axios 的 GET 请求"
}

```
- axios的POST请求模板
```
"Print to console": {<!-- -->
	"scope": "javascript,typescript",
	"prefix": "axios-post",
	"body": [
		"axios.post(url, {",
		"    参数1: '参数1的值',",
		"    参数2: '参数2的值'",
		"}).then(res =&gt; {",
		"    var data = res.data",
		"    console.log(res);",
		"});"
	],
	"description": "执行 axios 的 POST 请求"
}

```
- 自定义配置：axios(config)请求模板
```
"Print to console": {<!-- -->
	"scope": "javascript,typescript",
	"prefix": "axios-config",
	"body": [
		"axios({",
		"    method: 'get',",
		"    url: url,",
		"    data: {",
		"        参数1: '参数1的值',",
		"        参数2: '参数3的值',",
		"        对象传值: '去掉中括号直接传对象,例如: data: vm.user '",
		"    }",
		"}).then(res =&gt; {",
		"    var data = res.data",
		"    console.log(data);",
		"});",
	],
	"description": "执行 axios 的 自定义配置 请求"
}

```
<li>添加好了之后保存（**注：一个模板只能写一个请求方式**），查看效果 
  <ul>- 输入定义好的名称(注：是自定义模板中 **prefix 属性的值**)
<img src="https://img-blog.csdnimg.cn/7806b8b4b4084085a34419bd5c576fe2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/7f96417f599441a0ab056dcf3e62cb02.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L2g55qE5rOq5Li254Or5Lyk5oiR55qE6IS4,size_11,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">
- **成功，虽说没什么太大的用处吧，开发中能少写一行是一行，哈哈哈**