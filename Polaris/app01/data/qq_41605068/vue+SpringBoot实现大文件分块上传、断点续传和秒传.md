
--- 
title:  vue+SpringBoot实现大文件分块上传、断点续传和秒传 
tags: []
categories: [] 

---
>  
 资料： 


## 一、前提

现如今，随着业务的不断增大，普通的文件已经满足不了，对于大文件的一些处理显得十分重要，本片博客将实现web应用中，对大文件的分片上传、断点续传和秒传。

分片上传其实就是将一个大文件分成若干份大小想等的块文件，等所有块上传成功后，再将文件进行合并；（需要Io知识，如文件操作：新建路径、文件的写）

断点续传就是先判断哪些文件块已经上传过了，则跳过这些块，上传新的块；（将所有块信息保存在数据库中）

秒传就是当前文件已经存在了，则直接显示上传成功。（所有块均上传成功，则需要将文件块合并，涉及到文件的读，写）

### 1.1前端

首先，我们需要思考如何将文件分块处理，这些工作就交给前端来做（可学习插件：）。

simple-uploader.js（也称 Uploader) 是一个上传库，支持多并发上传，文件夹、拖拽、可暂停继续、秒传、分块上传、出错自动重传、手工重传、进度、剩余时间、上传速度等特性；该上传库依赖 HTML5 File API。

### 1.2后端

服务端如何接受呢？

因为在前端做了一些分块啊等处理，所以也需要服务端做一些特殊处理，这个可以参考 `samples/Node.js/` 实现。

每一个上传块都会包含如下分块信息：
- `chunkNumber`: 当前块的次序，第一个块是 1，注意不是从 0 开始的。- `totalChunks`: 文件被分成块的总数。- `chunkSize`: 分块大小，根据 `totalSize` 和这个值你就可以计算出总共的块数。注意最后一块的大小可能会比这个要大。- `currentChunkSize`: 当前块的大小，实际大小。- `totalSize`: 文件总大小。- `identifier`: 这个就是每个文件的唯一标示。- `filename`: 文件名。- `relativePath`: 文件夹上传的时候文件的相对路径属性。
一个分块可以被上传多次，当然这肯定不是标准行为，但是在实际上传过程中是可能发生这种事情的，这种重传也是本库的特性之一。

对于每个请求的响应码你都可以根据 `successStatuses`和`permanentErrors` 配置项是否是认为成功或失败的：
- `200`, `201`, `202`: 当前块上传成功，不需要重传。- `404`, `415`. `500`, `501`: 当前块上传失败，会取消整个文件上传。- **其他状态码**: 出错了，但是会自动重试上传。
## 二、前端

### 2.1API 文档

配置

实例化的时候可以传入配置项：

```
var r = new Uploader({ opt1: 'val', ...})
```

支持的配置项：
- `target` 目标上传 URL，可以是字符串也可以是函数，如果是函数的话，则会传入 `Uploader.File` 实例、当前块 `Uploader.Chunk` 以及是否是测试模式，默认值为 `'/'`。- `singleFile` 单文件上传。覆盖式，如果选择了多个会把之前的取消掉。默认 `false`。- `chunkSize` 分块时按照该值来分。最后一个上传块的大小是可能是大于等于1倍的这个值但是小于两倍的这个值大小，可见这个 ，默认 `1*1024*1024`。- `forceChunkSize` 是否强制所有的块都是小于等于 `chunkSize` 的值。默认是 `false`。- `simultaneousUploads` 并发上传数，默认 `3`。- `fileParameterName` 上传文件时文件的参数名，默认 `file`。- `query` 其他额外的参数，这个可以是一个对象或者是一个函数，如果是函数的话，则会传入 `Uploader.File` 实例、当前块 `Uploader.Chunk` 以及是否是测试模式，默认为 `{}`。- `headers` 额外的一些请求头，如果是函数的话，则会传入 `Uploader.File` 实例、当前块 `Uploader.Chunk` 以及是否是测试模式，默认 `{}`。- `withCredentials` 标准的 CORS 请求是不会带上 cookie 的，如果想要带的话需要设置 `withCredentials` 为 `true`，默认 `false`。- `method` 当上传的时候所使用的是方式，可选 `multipart`、`octet`，默认 `multipart`，参考 。- `testMethod` 测试的时候使用的 HTTP 方法，可以是字符串或者函数，如果是函数的话，则会传入 `Uploader.File` 实例、当前块 `Uploader.Chunk`，默认 `GET`。- `uploadMethod` 真正上传的时候使用的 HTTP 方法，可以是字符串或者函数，如果是函数的话，则会传入 `Uploader.File` 实例、当前块 `Uploader.Chunk`，默认 `POST`。- `allowDuplicateUploads `如果说一个文件以及上传过了是否还允许再次上传。默认的话如果已经上传了，除非你移除了否则是不会再次重新上传的，所以也就是默认值为 `false`。- `prioritizeFirstAndLastChunk` 对于文件而言是否高优先级发送第一个和最后一个块。一般用来发送到服务端，然后判断是否是合法文件；例如图片或者视频的 meta 数据一般放在文件第一部分，这样可以根据第一个块就能知道是否支持；默认 `false`。- `testChunks` 是否测试每个块是否在服务端已经上传了，主要用来实现秒传、跨浏览器上传等，默认 `true`。- `preprocess` 可选的函数，每个块在测试以及上传前会被调用，参数就是当前上传块实例 `Uploader.Chunk`，注意在这个函数中你需要调用当前上传块实例的 `preprocessFinished` 方法，默认 `null`。- `initFileFn` 可选函数用于初始化文件对象，传入的参数就是 `Uploader.File` 实例。- `readFileFn` 可选的函数用于原始文件的读取操作，传入的参数就是 `Uploader.File` 实例、文件类型、开始字节位置 startByte，结束字节位置 endByte、以及当前块 `Uploader.Chunk` 实例。并且当完成后应该调用当前块实例的`readFinished` 方法，且带参数-已读取的 bytes。- `checkChunkUploadedByResponse` 可选的函数用于根据 XHR 响应内容检测每个块是否上传成功了，传入的参数是：`Uploader.Chunk` 实例以及请求响应信息。这样就没必要上传（测试）所有的块了，具体细节原因参考 ，.- `generateUniqueIdentifier` 可覆盖默认的生成文件唯一标示的函数，默认 `null`。- `maxChunkRetries` 最大自动失败重试上传次数，值可以是任意正整数，如果是 `undefined` 则代表无限次，默认 `0`。- `chunkRetryInterval` 重试间隔，值可以是任意正整数，如果是 `null` 则代表立即重试，默认 `null`。- `progressCallbacksInterval` 进度回调间隔，默认是 `500`。- `speedSmoothingFactor` 主要用于计算平均速度，值就是从 0 到 1，如果是 1 那么上传的平均速度就等于当前上传速度，如果说长时间上传的话，建议设置为 `0.02`，这样剩余时间预估会更精确，这个参数是需要和 `progressCallbacksInterval` 一起调整的，默认是 `0.1`。- `successStatuses` 认为响应式成功的响应码，默认 `[200, 201, 202]`。- `permanentErrors` 认为是出错的响应码，默认 `[404, 415, 500, 501]`。- `initialPaused` 初始文件 paused 状态，默认 `false`。- `processResponse` 处理请求结果，默认 `function (response, cb) { cb(null, response) }`。 0.5.2版本后，`processResponse` 会传入更多参数：(response, cb, Uploader.File, Uploader.Chunk)。- `processParams` 处理请求参数，默认 `function (params) {return params}`，一般用于修改参数名字或者删除参数。0.5.2版本后，`processParams` 会有更多参数：(params, Uploader.File, Uploader.Chunk, isTest)。
属性
- `.support` 当前浏览器是否支持 File API 来上传。- `.supportDirectory` 当前浏览器是否支持文件夹上传。- `.opts` 实例的配置项对象。- `.files` 由 `Uploader.File` 文件对象组成的数组，纯文件列表。- `.fileList` 由 `Uploader.File` 文件、文件夹对象组成的数组，文件和文件夹共存。
方法
<li> `.assignBrowse(domNodes, isDirectory, singleFile, attributes)` 指定 DOM 元素可以选择上传。 
  <ul>- `domNodes` DOM 元素- `isDirectory` 如果传入的是 `true` 则代表是要选择文件夹上传的，你可以通过判断 `supportDirectory` 来决定是否设置- `singleFile` 是否只能选择单个文件- `attributes` 传入的其他属性值，例如你可以传入 `accept` 属性的值为 `image/*`，这样就意味着点选的时候只能选择图片。全部属性列表：
Note: 避免使用 `a` 或者 `button` 标签作为选择文件按钮。

`.assignDrop(domNodes)` 指定 DOM 元素作为拖拽上传目标。

`.unAssignDrop(domNodes)` 取消指定的 DOM 元素作为拖拽上传目标。

`.on(event, callback)` 监听事件。

`.off([event, [callback]])`:
- `.off(event)` 移除指定事件的所有事件回调- `.off(event, callback)` 移除指定事件的指定回调。`callback` 是一个函数
`.upload()` 开始或者继续上传。

`.pause()` 暂停上传。

`.resume()` 继续上传。

`.cancel()` 取消所有上传文件，文件会被移除掉。

`.progress()` 返回一个0-1的浮点数，当前上传进度。

`.isUploading()` 返回一个布尔值标示是否还有文件正在上传中。

`.addFile(file)` 添加一个原生的文件对象到上传列表中。

`.removeFile(file)` 从上传列表中移除一个指定的 `Uploader.File` 实例对象。

`.getFromUniqueIdentifier(uniqueIdentifier)` 根据唯一标识找到 `Uploader.File` 实例。

`.getSize()` 上传文件的总大小。

`.sizeUploaded()` 所有已经成功上传文件大小。

`.timeRemaining()` 剩余时间，单位秒；这个是基于平均上传速度计算出来的，如果说上传速度为 0，那么这个值就是 `Number.POSITIVE_INFINITY`。

事件
- `.change(event)` input 的 change 事件。- `.dragover(event)` 拖拽区域的 dragover 事件。- `.dragenter(event)` 拖拽区域的 dragenter 事件。- `.dragleave(event)` 拖拽区域的 dragleave 事件。- `.fileSuccess(rootFile, file, message, chunk)` 一个文件上传成功事件，第一个参数 `rootFile` 就是成功上传的文件所属的根 `Uploader.File` 对象，它应该包含或者等于成功上传文件；第二个参数 `file` 就是当前成功的 `Uploader.File` 对象本身；第三个参数就是 `message` 就是服务端响应内容，永远都是字符串；第四个参数 `chunk` 就是 `Uploader.Chunk` 实例，它就是该文件的最后一个块实例，如果你想得到请求响应码的话，`chunk.xhr.status` 就是。- `.fileComplete(rootFile)` 一个根文件（文件夹）成功上传完成。- `.fileProgress(rootFile, file, chunk)` 一个文件在上传中。- `.fileAdded(file, event)` 这个事件一般用作文件校验，如果说返回了 `false`，那么这个文件就会被忽略，不会添加到文件上传列表中。- `.filesAdded(files, fileList, event)` 和 fileAdded 一样，但是一般用作多个文件的校验。- `.filesSubmitted(files, fileList, event)` 和 filesAdded 类似，但是是文件已经加入到上传列表中，一般用来开始整个的上传。- `.fileRemoved(file)` 一个文件（文件夹）被移除。- `.fileRetry(rootFile, file, chunk)` 文件重试上传事件。- `.fileError(rootFile, file, message, chunk)` 上传过程中出错了。- `.uploadStart()` 已经开始上传了。- `.complete()` 上传完毕。- `.catchAll(event, ...)` 所有的事件。
#### Uploader.File

属性
- `.uploader` 对 `Uploader` 实例的引用。- `.name` 文件（夹）名字。- `.averageSpeed` 平均速度，单位字节每秒。- `.currentSpeed` 当前速度，单位字节每秒。- `.paused` 文件是否是暂停的。- `.error` 文件上传是否出错了。- `.isFolder` 是否是文件夹。
如果不是文件夹的话，那么还会有如下属性：
- `.file` 原生 HTML5 `File` 对象。- `.relativePath` 文件相对路径。- `.size` 文件大小，单位字节。- `.uniqueIdentifier` 文件唯一标示。- `.chunks` 由 `Uploader.Chunk` 实例组成数组，分成的块集合，一般场景下并不需要关心它。
方法
- `.getRoot()` 得到当前文件所属的根文件，这个根文件就是包含在 `uploader.fileList` 中的.- `.progress()` 返回一个 0 到 1 的数字，代表当前上传进度。- `.pause()` 暂停上窜文件。- `.resume()` 继续上传文件。- `.cancel()` 取消上传且从文件列表中移除。- `.retry()` 重新上传文件。- `.bootstrap()` 重新初始化 `Uploader.File` 对象的状态，包括重新分块，重新创建新的 XMLHttpRequest 实例。- `.isUploading()` 文件是否扔在上传中。- `.isComplete()` 文件是否已经上传完成。- `.sizeUploaded()` 已经上传大小。- `.timeRemaining()` 剩余时间，基于平均速度的，如果说平均速度为 0，那么值就是 `Number.POSITIVE_INFINITY`。- `.getExtension()` 得到小写的后缀。- `.getType()` 得到文件类型。
### 2.2前端Demo

```
&lt;template&gt;
    &lt;!-- 上传器 --&gt;
    &lt;uploader
        ref="uploader"
        :options="options"
        :autoStart=false
        :file-status-text="fileStatusText"
        @file-added="onFileAdded"
        @file-success="onFileSuccess"
        @file-progress="onFileProgress"
        @file-error="onFileError"
        class="uploader-ui"&gt; 
        &lt;uploader-unsupport&gt;&lt;/uploader-unsupport&gt;
        &lt;uploader-drop&gt;
            &lt;div&gt;
                &lt;uploader-btn id="global-uploader-btn" :attrs="attrs" ref="uploadBtn"&gt;选择文件&lt;i class="el-icon-upload el-icon--right"&gt;&lt;/i&gt;&lt;/uploader-btn&gt;
            &lt;/div&gt;
        &lt;/uploader-drop&gt;
        &lt;uploader-list&gt;&lt;/uploader-list&gt;
    &lt;/uploader&gt;
&lt;/template&gt;

```

```
&lt;script&gt;
export default {
        data () {
            return {
                options: {
                    //目标上传 URL，默认POST
                    target: "http://127.0.0.1:5000/uploader/chunk",
                    //分块大小(单位：字节)
                    chunkSize: '2048000',
                    //上传文件时文件内容的参数名，对应chunk里的Multipart对象名，默认对象名为file
                    fileParameterName: 'upfile',
                    //失败后最多自动重试上传次数
                    maxChunkRetries: 3,
                    //是否开启服务器分片校验，对应GET类型同名的target URL
                    testChunks: true,   
                    /* 
                    服务器分片校验函数，判断秒传及断点续传,传入的参数是Uploader.Chunk实例以及请求响应信息
                    reponse码是successStatuses码时，才会进入该方法
                    reponse码如果返回的是permanentErrors 中的状态码，不会进入该方法，直接进入onFileError函数 ，并显示上传失败
                    reponse码是其他状态码，不会进入该方法，正常走标准上传
                    checkChunkUploadedByResponse函数直接return true的话，不再调用上传接口
                    */
                    checkChunkUploadedByResponse: function (chunk, response_msg) {
                        let objMessage = JSON.parse(response_msg);
                        if (objMessage.skipUpload) {
                            return true;
                        }
                        return (objMessage.uploadedChunks || []).indexOf(chunk.offset + 1) &gt;= 0;
                    }      
                },
                attrs: {
                    accept: ACCEPT_CONFIG.getAll()
                },
                fileStatusText: {
                        success: '上传成功',
                        error: '上传失败',
                        uploading: '上传中',
                        paused: '暂停',
                        waiting: '等待上传'
                },
            }
        },
        methods: {
            onFileAdded(file) {
                this.computeMD5(file);
            },
            /*
            第一个参数 rootFile 就是成功上传的文件所属的根 Uploader.File 对象，它应该包含或者等于成功上传文件；
            第二个参数 file 就是当前成功的 Uploader.File 对象本身；
            第三个参数就是 message 就是服务端响应内容，永远都是字符串；
            第四个参数 chunk 就是 Uploader.Chunk 实例，它就是该文件的最后一个块实例，如果你想得到请求响应码的话，chunk.xhr.status就是
            */
            onFileSuccess(rootFile, file, response, chunk) {
                //refProjectId为预留字段，可关联附件所属目标，例如所属档案，所属工程等
                file.refProjectId = "123456789";
                mergeFile(file).then( responseData=&gt; {
                    if(responseData.data.code === 415){
                        console.log("合并操作未成功，结果码："+responseData.data.code);
                    }
                }).catch(function (error){
                    console.log("合并后捕获的未知异常："+error);
                });
            },
            onFileError(rootFile, file, response, chunk) {
                console.log('上传完成后异常信息：'+response);
            },

            /**
             * 计算md5，实现断点续传及秒传
             * @param file
             */
            computeMD5(file) {
                file.pause();

                //单个文件的大小限制2G
                let fileSizeLimit = 2 * 1024 * 1024 * 1024;
                console.log("文件大小："+file.size);
                console.log("限制大小："+fileSizeLimit);
                if(file.size &gt; fileSizeLimit){
                    this.$message({
                        showClose: true,
                        message: '文件大小不能超过2G'
                    });
                    file.cancel();
                }

                let fileReader = new FileReader();
                let time = new Date().getTime();
                let blobSlice = File.prototype.slice || File.prototype.mozSlice || File.prototype.webkitSlice;
                let currentChunk = 0;
                const chunkSize = 10 * 1024 * 1000;
                let chunks = Math.ceil(file.size / chunkSize);
                let spark = new SparkMD5.ArrayBuffer();
                //由于计算整个文件的Md5太慢，因此采用只计算第1块文件的md5的方式
                let chunkNumberMD5 = 1;

                loadNext();

                fileReader.onload = (e =&gt; {
                    spark.append(e.target.result);

                    if (currentChunk &lt; chunkNumberMD5) {
                        loadNext();
                    } else {
                        let md5 = spark.end();
                        file.uniqueIdentifier = md5;
                        file.resume();
                        console.log(`MD5计算完毕：${file.name} \nMD5：${md5} \n分片：${chunks} 大小:${file.size} 用时：${new Date().getTime() - time} ms`);
                    }
                });

                fileReader.onerror = function () {
                    this.error(`文件${file.name}读取出错，请检查该文件`)
                    file.cancel();
                };

                function loadNext() {
                    let start = currentChunk * chunkSize;
                    let end = ((start + chunkSize) &gt;= file.size) ? file.size : start + chunkSize;

                    fileReader.readAsArrayBuffer(blobSlice.call(file.file, start, end));
                    currentChunk++;
                    console.log("计算第"+currentChunk+"块");
                }
            },
            close() {
                this.uploader.cancel();
            },
            error(msg) {
                this.$notify({
                    title: '错误',
                    message: msg,
                    type: 'error',
                    duration: 2000
                })
            }
        }
    }
&lt;/script&gt;
```

```
export const mergeFile = data =&gt; {
    option.isJson = true
    option.data = JSON.stringify(data)
    option.method = 'post'
    option.url = 'http://127.0.0.1:5000/uploader/mergeFile'
    return requestApi(option)
  }
```

```
const service = axios.create({
    // axios中请求配置有baseURL选项，表示请求URL公共部分
    baseURL: process.env.VUE_APP_BASE_API,
    timeout: 5000
});

service.interceptors.request.use(
    config =&gt; {
        return config;
    },
    error =&gt; {
        console.log(error);
        return Promise.reject();
    }
);

service.interceptors.response.use(
    response =&gt; {
        if (response.status === 200) {
            return response.data;
        } else {
            Promise.reject();
        }
    },
    error =&gt; {
        console.log(error);
        return Promise.reject();
    }
);

export const loginRequestApi = (option) =&gt; {
  return service({
    method: option.method,
    url: `${option.url}`,
    data: option.data,
    headers: {
      'Content-Type': 'application/json'
    }
  })
}

export const requestApi = (option) =&gt; {
    if (option.isJson &amp;&amp; JSON.stringify(option.data) !== {}) {
      return service({
        method: option.method,
        url: `${option.url}`,
        data: option.data,
        headers: {
          'Content-Type': 'application/json'
        }
      })
    } else if (option.isJson &amp;&amp; JSON.stringify(option.data) === {}) {
      return service({
        method: option.method,
        url: `${option.url}`,
        data: option.data,
        headers: {
          'Content-Type': 'application/json'
        }
      })
    } else if (!option.isJson &amp;&amp; JSON.stringify(option.data) !== {}) {
      return service({
        method: option.method,
        url: `${option.url}`,
        params: option.data,
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      })
    } else if (!option.isJson &amp;&amp; JSON.stringify(option.data) === {}) {
      return service({
        method: option.method,
        url: `${option.url}`
      })
    }
}
```

## 三、后端

### 3.1新建工程

<img alt="" height="574" src="https://img-blog.csdnimg.cn/20201109153713314.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

### 3.2添加依赖

```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd"&gt;
    &lt;modelVersion&gt;4.0.0&lt;/modelVersion&gt;
    &lt;parent&gt;
        &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
        &lt;artifactId&gt;spring-boot-starter-parent&lt;/artifactId&gt;
        &lt;version&gt;2.3.5.RELEASE&lt;/version&gt;
        &lt;relativePath/&gt; &lt;!-- lookup parent from repository --&gt;
    &lt;/parent&gt;
    &lt;groupId&gt;com.example&lt;/groupId&gt;
    &lt;artifactId&gt;demo&lt;/artifactId&gt;
    &lt;version&gt;0.0.1-SNAPSHOT&lt;/version&gt;
    &lt;name&gt;fileupload&lt;/name&gt;
    &lt;description&gt;Big File Upload Demo project for Spring Boot&lt;/description&gt;

    &lt;properties&gt;
        &lt;java.version&gt;1.8&lt;/java.version&gt;
        &lt;mybatis-plus.version&gt;3.1.2&lt;/mybatis-plus.version&gt;
    &lt;/properties&gt;

    &lt;dependencies&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter&lt;/artifactId&gt;
        &lt;/dependency&gt;
        &lt;!--        web依赖--&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-web&lt;/artifactId&gt;
            &lt;exclusions&gt;
				&lt;!--排除tomcat依赖--&gt;
				&lt;exclusion&gt;
					&lt;artifactId&gt;spring-boot-starter-tomcat&lt;/artifactId&gt;
					&lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
				&lt;/exclusion&gt;
			&lt;/exclusions&gt;
        &lt;/dependency&gt;
        &lt;!--        mybatis依赖--&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.mybatis.spring.boot&lt;/groupId&gt;
            &lt;artifactId&gt;mybatis-spring-boot-starter&lt;/artifactId&gt;
            &lt;version&gt;2.1.3&lt;/version&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;com.baomidou&lt;/groupId&gt;
            &lt;artifactId&gt;mybatis-plus-boot-starter&lt;/artifactId&gt;
            &lt;version&gt;${mybatis-plus.version}&lt;/version&gt;
        &lt;/dependency&gt;
        &lt;!--        热部署--&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-devtools&lt;/artifactId&gt;
            &lt;scope&gt;runtime&lt;/scope&gt;
            &lt;optional&gt;true&lt;/optional&gt;
        &lt;/dependency&gt;
        &lt;!-- mysql驱动--&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;mysql&lt;/groupId&gt;
            &lt;artifactId&gt;mysql-connector-java&lt;/artifactId&gt;
            &lt;scope&gt;runtime&lt;/scope&gt;
        &lt;/dependency&gt;
        &lt;!--阿里数据库连接池 --&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;com.alibaba&lt;/groupId&gt;
            &lt;artifactId&gt;druid-spring-boot-starter&lt;/artifactId&gt;
            &lt;version&gt;1.1.14&lt;/version&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.projectlombok&lt;/groupId&gt;
            &lt;artifactId&gt;lombok&lt;/artifactId&gt;
            &lt;optional&gt;true&lt;/optional&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;
            &lt;scope&gt;test&lt;/scope&gt;
            &lt;exclusions&gt;
                &lt;exclusion&gt;
                    &lt;groupId&gt;org.junit.vintage&lt;/groupId&gt;
                    &lt;artifactId&gt;junit-vintage-engine&lt;/artifactId&gt;
                &lt;/exclusion&gt;
            &lt;/exclusions&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;javax.servlet&lt;/groupId&gt;
            &lt;artifactId&gt;servlet-api&lt;/artifactId&gt;
            &lt;version&gt;2.5&lt;/version&gt;
            &lt;scope&gt;provided&lt;/scope&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;io.springfox&lt;/groupId&gt;
            &lt;artifactId&gt;springfox-swagger2&lt;/artifactId&gt;
            &lt;version&gt;2.9.2&lt;/version&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;io.springfox&lt;/groupId&gt;
            &lt;artifactId&gt;springfox-swagger-ui&lt;/artifactId&gt;
            &lt;version&gt;2.9.2&lt;/version&gt;
        &lt;/dependency&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-web&lt;/artifactId&gt;
        &lt;/dependency&gt;

    &lt;/dependencies&gt;

    &lt;build&gt;
        &lt;plugins&gt;
            &lt;plugin&gt;
                &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
                &lt;artifactId&gt;spring-boot-maven-plugin&lt;/artifactId&gt;
            &lt;/plugin&gt;
        &lt;/plugins&gt;
    &lt;/build&gt;

&lt;/project&gt;

```

### 3.3工程目录

<img alt="" height="746" src="https://img-blog.csdnimg.cn/20201109202137980.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="469">

### 3.4创建表

```
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for `t_chunk_info`
-- ----------------------------
DROP TABLE IF EXISTS `t_chunk_info`;
CREATE TABLE `t_chunk_info`  (
  `ID` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'id',
  `CHUNK_NUMBER` decimal(10, 0) NOT NULL COMMENT '块编号，从1开始',
  `CHUNK_SIZE` decimal(10, 0) NOT NULL COMMENT '块大小',
  `CURRENT_CHUNK_SIZE` decimal(10, 0) NOT NULL COMMENT '当前块大小',
  `IDENTIFIER` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '文件标识',
  `FILENAME` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '文件名',
  `RELATIVE_PATH` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '相对路径',
  `TOTAL_CHUNKS` decimal(10, 0) NOT NULL COMMENT '总块数',
  `TOTAL_SIZE` int(11) NULL DEFAULT NULL COMMENT '总大小',
  `FILE_TYPE` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '文件类型',
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;


-- ----------------------------
-- Table structure for `t_file_info`
-- ----------------------------
DROP TABLE IF EXISTS `t_file_info`;
CREATE TABLE `t_file_info`  (
  `ID` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'ID',
  `FILENAME` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '文件名',
  `IDENTIFIER` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '文件标识',
  `TOTAL_SIZE` decimal(10, 0) NOT NULL COMMENT '总大小',
  `LOCATION` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '存储地址',
  `FILETYPE` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '文件类型',
  `REF_PROJECT_ID` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '文件所属',
  `UPLOAD_USER` int(50) NULL DEFAULT NULL COMMENT '上传用户',
  `UPLOAD_TIME` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '上传时间',
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;
```

### 3.5Controller接口

```
package com.fileupload.controller;

import com.fileupload.entity.ChunkInfo;
import com.fileupload.entity.FileInfo;
import com.fileupload.response.ApiResult;
import com.fileupload.response.ChunkResult;
import com.fileupload.service.ChunkInfoService;
import com.fileupload.service.FileInfoService;
import com.fileupload.util.ServletUtils;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.FileInputStream;
import java.io.OutputStream;

/**
 * @ClassName FileController
 * @Description 大文件上传
 * @Author huqiang
 * @Date 2020/11/9 17:00
 * @Version 1.0
 */
@RestController
@RequestMapping("/uploader")
@Slf4j
@CrossOrigin
public class FileController {
    @Autowired
    private  ChunkInfoService chunkInfoService;
    @Autowired
    private  FileInfoService fileInfoService;

    /**
     * 校验文件
     *
     * @param chunk
     * @param response
     * @return
     */
    @GetMapping("/chunk")
    public ChunkResult checkChunk(ChunkInfo chunk, HttpServletResponse response) {
        log.info("校验文件：{}", chunk);
        return chunkInfoService.checkChunkState(chunk, response);
    }

    /**
     * 文件块上传
     *
     * @param chunk
     * @return
     */
    @PostMapping("/chunk")
    public Integer uploadChunk(ChunkInfo chunk) {
        return chunkInfoService.uploadFile(chunk);
    }

    @PostMapping("/mergeFile")
    public HttpServletResponse mergeFile(@RequestBody FileInfo fileInfo, HttpServletResponse response) {
        return fileInfoService.mergeFile(fileInfo, response);
    }

    /**
     * 查询列表
     *
     * @return ApiResult
     */
    @GetMapping(value = "/selectFileList/{page}/{size}")
    public ApiResult selectFileList(@RequestBody FileInfo file,
                                    @PathVariable("page") Integer pageNum,
                                    @PathVariable("size") Integer pageSize) {
        log.info("查询文件列表：{}", file);
        return ApiResult.success(fileInfoService.selectFileList(file, pageNum, pageSize));
    }

    /**
     * 删除
     */
    @DeleteMapping(value = "/deleteFile")
    public ApiResult deleteFile(@RequestBody FileInfo fileInfo) {
        return ApiResult.success(fileInfoService.deleteFile(fileInfo));
    }

    /**
     * 下载文件
     *
     * @param fileInfo
     * @param resp
     */
    @GetMapping(value = "/download")
    public void download(@RequestBody FileInfo fileInfo,
                         HttpServletRequest req,
                         HttpServletResponse resp) {
        String location = fileInfo.getLocation();
        String fileName = fileInfo.getFileName();
        BufferedInputStream bis = null;
        BufferedOutputStream bos = null;
        OutputStream fos = null;
        try {
            bis = new BufferedInputStream(new FileInputStream(location));
            fos = resp.getOutputStream();
            bos = new BufferedOutputStream(fos);
            ServletUtils.setFileDownloadHeader(req, resp, fileName);
            int byteRead = 0;
            byte[] buffer = new byte[8192];
            while ((byteRead = bis.read(buffer, 0, 8192)) != -1) {
                bos.write(buffer, 0, byteRead);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                bos.flush();
                bis.close();
                fos.close();
                bos.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

}

```

### 3.6实体类

3.6.1 文件块类ChunkInfo

```
package com.fileupload.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.web.multipart.MultipartFile;

@Data
@NoArgsConstructor
@TableName(value = "chunk_info")
public class ChunkInfo {
    /**
     * id
     */
    @TableId(value = "ID", type = IdType.ID_WORKER)
    private String id;

    /**
     * 块编号，从1开始
     */
    @TableField(value = "CHUNK_NUMBER")
    private Long chunkNumber;

    /**
     * 块大小
     */
    @TableField(value = "CHUNK_SIZE")
    private Long chunkSize;

    /**
     * 当前块大小
     */
    @TableField(value = "CURRENT_CHUNKSIZE")
    private Long currentChunkSize;

    /**
     * 文件标识
     */
    @TableField(value = "IDENTIFIER")
    private String identifier;

    /**
     * 文件名
     */
    @TableField(value = "FILENAME")
    private String filename;

    /**
     * 相对路径
     */
    @TableField(value = "RELATIVE_PATH")
    private String relativePath;

    /**
     * 总块数
     */
    @TableField(value = "TOTAL_CHUNKS")
    private Long totalChunks;

    /**
     * 总大小
     */
    @TableField(value = "TOTAL_SIZE")
    private Integer totalSize;

    /**
     * 文件类型
     */
    @TableField(value = "FILETYPE")
    private String filetype;

    /**
     * 块内容
     */
    @TableField(exist = false)
    private MultipartFile upfile;

    public static final String COL_ID = "ID";

    public static final String COL_CHUNK_NUMBER = "CHUNK_NUMBER";

    public static final String COL_CHUNK_SIZE = "CHUNK_SIZE";

    public static final String COL_CURRENT_CHUNKSIZE = "CURRENT_CHUNKSIZE";

    public static final String COL_IDENTIFIER = "IDENTIFIER";

    public static final String COL_FILE_NAME = "FILENAME";

    public static final String COL_RELATIVE_PATH = "RELATIVE_PATH";

    public static final String COL_TOTAL_CHUNKS = "TOTAL_CHUNKS";

    public static final String COL_TOTAL_SIZE = "TOTAL_SIZE";

    public static final String COL_FILE_TYPE = "FILETYPE";
}
```

#### 3.6.2文件类FileInfo

```
package com.fileupload.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import java.time.LocalDateTime;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@TableName(value = "FILE_INFO")
public class FileInfo {
    /**
     * ID
     */
    @TableId(value = "ID", type = IdType.ID_WORKER)
    private String id;

    /**
     * 文件名
     */
    @TableField(value = "FILENAME")
    private String filename;

    /**
     * 文件标识
     */
    @TableField(value = "IDENTIFIER")
    private String identifier;

    /**
     * 总大小
     */
    @TableField(value = "TOTAL_SIZE")
    private Long totalSize;
    @TableField(exist = false)
    private String totalSizeName;

    /**
     * 存储地址
     */
    @TableField(value = "LOCATION")
    private String location;

    /**
     * 文件类型
     */
    @TableField(value = "FILETYPE")
    private String filetype;

    /**
     * 文件所属
     */
    @TableField(value = "REF_PROJECT_ID")
    private String refProjectId;

    /**
     * 上传用户
     */
    @TableField(value = "UPLOAD_USER")
    private Integer uploadUser;

    /**
     * 上传时间
     */
    @TableField(value = "UPLOAD_TIME")
    private LocalDateTime uploadTime;
    public void setTotalSize(Long totalSize) {
        this.totalSize = totalSize;
        if(1024*1024 &gt; this.totalSize &amp;&amp; this.totalSize &gt;= 1024 ) {
            this.totalSizeName = String.format("%.2f",this.totalSize.doubleValue()/1024) + "KB";
        }else if(1024*1024*1024 &gt; this.totalSize &amp;&amp; this.totalSize &gt;= 1024*1024 ) {
            this.totalSizeName = String.format("%.2f",this.totalSize.doubleValue()/(1024*1024)) + "MB";
        }else if(this.totalSize &gt;= 1024*1024*1024 ) {
            this.totalSizeName = String.format("%.2f",this.totalSize.doubleValue()/(1024*1024*1024)) + "GB";
        }else {
            this.totalSizeName = this.totalSize.toString() + "B";
        }
    }

    public static final String COL_ID = "ID";

    public static final String COL_FILE_NAME = "FILENAME";

    public static final String COL_IDENTIFIER = "IDENTIFIER";

    public static final String COL_TOTAL_SIZE = "TOTAL_SIZE";

    public static final String COL_LOCATION = "LOCATION";

    public static final String COL_FILE_TYPE = "FILETYPE";

    public static final String COL_REF_PROJECT_ID = "REF_PROJECT_ID";

    public static final String COL_UPLOAD_USER = "UPLOAD_USER";

    public static final String COL_UPLOAD_TIME = "UPLOAD_TIME";
}
```

### 3.7Mapper层

#### 3.7.1文件块

```
package com.fileupload.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.fileupload.entity.ChunkInfo;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.List;

@Mapper
public interface ChunkInfoMapper extends BaseMapper&lt;ChunkInfo&gt; {
    /**
     * 查询文件块号
     * @param record
     * @return
     */
    ArrayList&lt;Integer&gt; selectChunkNumbers(ChunkInfo record);
}
```

#### 3.7.2文件

```
package com.fileupload.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.fileupload.entity.FileInfo;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Mapper
public interface FileInfoMapper extends BaseMapper&lt;FileInfo&gt; {
    IPage&lt;FileInfo&gt; selectFileList(IPage&lt;FileInfo&gt; page, FileInfo fileInfo);
}
```

### 3.8响应类ApiResult

```
package com.fileupload.response;


import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;

/**
 * 操作消息提醒
 * 
 * @author jialongju
 */
public class ApiResult extends HashMap&lt;String, Object&gt;
{
    private static final long serialVersionUID = 1L;

    /** 状态码 */
    public static final String CODE_TAG = "code";

    /** 返回内容 */
    public static final String MSG_TAG = "msg";

    /** 数据对象 */
    public static final String DATA_TAG = "data";

    /**
     * 初始化一个新创建的 ApiResult 对象，使其表示一个空消息。
     */
    public ApiResult()
    {
    }

    /**
     * 初始化一个新创建的 ApiResult 对象
     * 
     * @param code 状态码
     * @param msg 返回内容
     */
    public ApiResult(int code, String msg)
    {
        super.put(CODE_TAG, code);
        super.put(MSG_TAG, msg);
    }

    /**
     * 初始化一个新创建的 ApiResult 对象
     * 
     * @param code 状态码
     * @param msg 返回内容
     * @param data 数据对象
     */
    public ApiResult(int code, String msg, Object data)
    {
        super.put(CODE_TAG, code);
        super.put(MSG_TAG, msg);
        if (data != null)
        {
            super.put(DATA_TAG, data);
        }
    }

    /**
     * 返回成功消息
     * 
     * @return 成功消息
     */
    public static ApiResult success()
    {
        return ApiResult.success("操作成功");
    }

    /**
     * 返回成功数据
     * 
     * @return 成功消息
     */
    public static ApiResult success(Object data)
    {
        return ApiResult.success("操作成功", data);
    }

    /**
     * 返回成功消息
     * 
     * @param msg 返回内容
     * @return 成功消息
     */
    public static ApiResult success(String msg)
    {
        return ApiResult.success(msg, null);
    }

    /**
     * 返回成功消息
     * 
     * @param msg 返回内容
     * @param data 数据对象
     * @return 成功消息
     */
    public static ApiResult success(String msg, Object data)
    {
        return new ApiResult(HttpServletResponse.SC_OK, msg, data);
    }

    /**
     * 返回错误消息
     * 
     * @return
     */
    public static ApiResult error()
    {
        return ApiResult.error("操作失败");
    }

    /**
     * 返回错误消息
     * 
     * @param msg 返回内容
     * @return 警告消息
     */
    public static ApiResult error(String msg)
    {
        return ApiResult.error(msg, null);
    }

    /**
     * 返回错误消息
     * 
     * @param msg 返回内容
     * @param data 数据对象
     * @return 警告消息
     */
    public static ApiResult error(String msg, Object data)
    {
        return new ApiResult(HttpServletResponse.SC_INTERNAL_SERVER_ERROR, msg, data);
    }

    /**
     * 返回错误消息
     * 
     * @param code 状态码
     * @param msg 返回内容
     * @return 警告消息
     */
    public static ApiResult error(int code, String msg)
    {
        return new ApiResult(code, msg, null);
    }
}

```

### 3.9根据该类判断续传？秒传？上传？

```
package com.fileupload.response;

import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;
import java.util.ArrayList;

/**
 * @ClassName ChunkResult
 * @Description 校验文件返回结果集（秒传？续传？）
 * @Author huqiang
 * @Date 2020/11/9 17:13
 * @Version 1.0
 */
@Data
@NoArgsConstructor
public class ChunkResult implements Serializable{
    private static final long serialVersionUID = -9000695051292877324L;
    /**
     * 是否跳过上传（已上传的可以直接跳过，达到秒传的效果）
     */
    private boolean skipUpload;
    /**
     *已经上传的文件块编号，可以跳过，断点续传
     */
    private ArrayList&lt;Integer&gt; uploadedChunks;
    /**
     *返回结果信息
     */
    private String message;
    /**
     *已上传完整附件的地址
     */
    private String location;

}

```

### 3.10Service

#### 3.10.1文件块校验

```
package com.fileupload.service;

import com.fileupload.entity.ChunkInfo;
import com.baomidou.mybatisplus.extension.service.IService;
import com.fileupload.response.ChunkResult;

import javax.servlet.http.HttpServletResponse;

public interface ChunkInfoService extends IService&lt;ChunkInfo&gt; {
    /**
     * 校验当前文件
     *
     * @param chunkInfo
     * @param response
     * @return 秒传？续传？新传？
     */
    ChunkResult checkChunkState(ChunkInfo chunkInfo, HttpServletResponse response);

    /**
     * 上传文件
     *
     * @param chunk
     * @return
     */
    Integer uploadFile(ChunkInfo chunk);
}

```

```
package com.fileupload.service.imp;

import com.fileupload.response.ChunkResult;
import com.fileupload.util.FileInfoUtils;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.fileupload.mapper.ChunkInfoMapper;
import com.fileupload.entity.ChunkInfo;
import com.fileupload.service.ChunkInfoService;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletResponse;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;

@Service
@Slf4j
public class ChunkInfoServiceImpl extends ServiceImpl&lt;ChunkInfoMapper, ChunkInfo&gt; implements ChunkInfoService{
    @Value("${base.file-path}")
    private String uploadFolder;
    @Autowired
    private ChunkInfoMapper chunkInfoMapper;

    /**
     * 校验当前文件
     * @param chunkInfo
     * @param response
     * @return 秒传？续传？新传？
     */
    @Override
    public ChunkResult checkChunkState(ChunkInfo chunkInfo, HttpServletResponse response) {
        ChunkResult chunkResult = new ChunkResult();
        String file = uploadFolder + File.separator + chunkInfo.getIdentifier() + File.separator + chunkInfo.getFileName();
        if(FileInfoUtils.fileExists(file)) {
            chunkResult.setSkipUpload(true);
            chunkResult.setLocation(file);
            response.setStatus(HttpServletResponse.SC_OK);
            chunkResult.setMessage("完整文件已存在，直接跳过上传，实现秒传");
            return chunkResult;
        }
        ArrayList&lt;Integer&gt; list = chunkInfoMapper.selectChunkNumbers(chunkInfo);
        if (list !=null &amp;&amp; list.size() &gt; 0) {
            chunkResult.setSkipUpload(false);
            chunkResult.setUploadedChunks(list);
            response.setStatus(HttpServletResponse.SC_OK);
            chunkResult.setMessage("部分文件块已存在，继续上传剩余文件块，实现断点续传");
            return chunkResult;
        }
        return chunkResult;
    }

    /**
     * 写文件
     * @param chunk
     * @return
     */
    @Override
    public Integer uploadFile(ChunkInfo chunk) {
        Integer apiRlt = HttpServletResponse.SC_OK;
        MultipartFile file = chunk.getUpfile();
        try {
            byte[] bytes = file.getBytes();
            Path path = Paths.get(FileInfoUtils.generatePath(uploadFolder, chunk));
            Files.write(path, bytes);
            if(chunkInfoMapper.insert(chunk) &lt; 0){
                apiRlt = HttpServletResponse.SC_UNSUPPORTED_MEDIA_TYPE;
            }
        } catch (IOException e) {
            log.error("写文件出错：{}",e.getMessage());
            apiRlt = HttpServletResponse.SC_UNSUPPORTED_MEDIA_TYPE;
        }
        return apiRlt;
    }
}

```

#### 3.10.2文件service

```
package com.fileupload.service;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.service.IService;
import com.fileupload.entity.FileInfo;

import javax.servlet.http.HttpServletResponse;
import java.util.List;

public interface FileInfoService extends IService&lt;FileInfo&gt;{
    /**
     * 合并文件
     * @param fileInfo
     * @return
     */
    HttpServletResponse mergeFile(FileInfo  fileInfo,HttpServletResponse response);

    /**
     * 查询文件列表
     * @param file
     * @return
     */
    IPage&lt;FileInfo&gt; selectFileList(FileInfo file, Integer pageNum, Integer pageSize);

    /**
     * 删除
     * @param fileInfo
     * @return
     */
    Integer deleteFile(FileInfo fileInfo);
}

```

```
package com.fileupload.service.imp;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.fileupload.entity.ChunkInfo;
import com.fileupload.mapper.ChunkInfoMapper;
import com.fileupload.util.FileInfoUtils;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.fileupload.mapper.FileInfoMapper;
import com.fileupload.entity.FileInfo;
import com.fileupload.service.FileInfoService;

import javax.servlet.http.HttpServletResponse;
import java.io.File;
import java.util.List;
import java.util.stream.Collectors;

@Service

public class FileInfoServiceImpl extends ServiceImpl&lt;FileInfoMapper, FileInfo&gt; implements FileInfoService {
    @Value("${base.file-path}")
    private String uploadFolder;
    @Autowired
    private ChunkInfoMapper chunkInfoMapper;
    @Autowired
    private FileInfoMapper fileInfoMapper;
    private final static Logger logger = LoggerFactory.getLogger(FileInfoServiceImpl.class);

    @Override
    public HttpServletResponse mergeFile(FileInfo fileInfo, HttpServletResponse response) {
        response.setStatus(HttpServletResponse.SC_UNSUPPORTED_MEDIA_TYPE);

        //进行文件的合并操作
        String filename = fileInfo.getFileName();
        String file = uploadFolder + File.separator + fileInfo.getIdentifier() + File.separator + filename;
        String folder = uploadFolder + File.separator + fileInfo.getIdentifier();
        Integer fileSuccess = FileInfoUtils.merge(file, folder, filename);
        fileInfo.setLocation(folder);
        QueryWrapper&lt;ChunkInfo&gt; wrapper = new QueryWrapper&lt;&gt;();
        wrapper
                .eq(ChunkInfo.COL_IDENTIFIER, fileInfo.getIdentifier())
                .eq(ChunkInfo.COL_FILE_NAME, fileInfo.getFileName());
        chunkInfoMapper.delete(wrapper);
        //文件合并成功后，保存记录
        if (fileSuccess == HttpServletResponse.SC_OK) {
            fileInfoMapper.insert(fileInfo);
            response.setStatus(HttpServletResponse.SC_OK);
        }
        //如果已经存在，则判断是否是同一个项目，同一个项目不用新增记录，否则新增
        else if (fileSuccess == HttpServletResponse.SC_MULTIPLE_CHOICES) {
            QueryWrapper&lt;FileInfo&gt; wrapper1 = new QueryWrapper&lt;&gt;();
            wrapper1
                    .eq(ChunkInfo.COL_IDENTIFIER, fileInfo.getIdentifier())
                    .eq(ChunkInfo.COL_FILE_NAME, fileInfo.getFileName());
            List&lt;FileInfo&gt; tfList = fileInfoMapper.selectList(wrapper1);
            if (tfList.size() == 0) {
                fileInfoMapper.insert(fileInfo);
                response.setStatus(HttpServletResponse.SC_MULTIPLE_CHOICES);
            } else {
                for (FileInfo info : tfList) {
                    if (info.getRefProjectId().equals(fileInfo.getRefProjectId())) {
                        QueryWrapper&lt;FileInfo&gt; wrapper2 = new QueryWrapper&lt;&gt;();
                        wrapper2.eq(FileInfo.COL_ID, info.getId());
                        fileInfoMapper.delete(wrapper2);
                        fileInfoMapper.insert(fileInfo);
                        response.setStatus(HttpServletResponse.SC_MULTIPLE_CHOICES);
                    }
                }
            }
        } else {
            response.setStatus(HttpServletResponse.SC_BAD_REQUEST);
        }
        return response;
    }

    /**
     * 查询文件列表
     *
     * @param file
     * @return
     */
    @Override
    public IPage&lt;FileInfo&gt; selectFileList(FileInfo file, Integer pageNum, Integer pageSize) {
        Page&lt;FileInfo&gt; queryPage = new Page&lt;&gt;(pageNum, pageSize);
        IPage&lt;FileInfo&gt; data = fileInfoMapper.selectFileList(queryPage, file);
        List&lt;FileInfo&gt; rows = data.getRecords().stream().map(row -&gt; {
            FileInfo resRow = new FileInfo();
            BeanUtils.copyProperties(row, resRow);
            return resRow;
        }).collect(Collectors.toList());
        Page&lt;FileInfo&gt; page = new Page&lt;&gt;();
        page.setTotal(data.getTotal());
        page.setRecords(data.getRecords());
        return page;
    }

    @Override
    public Integer deleteFile(FileInfo fileInfo) {
        return fileInfoMapper.deleteById(fileInfo.getId());
    }
}

```

### 3.11工具类

```
package com.fileupload.util;

import com.fileupload.entity.ChunkInfo;
import lombok.extern.slf4j.Slf4j;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.nio.file.*;

/**
 * @ClassName FileInfoUntils
 * @Description 文件工具类
 * @Author huqiang
 * @Date 2020/11/9 17:36
 * @Version 1.0
 */
@Slf4j
public class FileInfoUtils {

    /**
     * 创建路径
     * @param uploadFolder
     * @param chunk
     * @return 文件
     */
    public static String generatePath(String uploadFolder, ChunkInfo chunk) {
        StringBuilder sb = new StringBuilder();
        sb.append(uploadFolder).append("/").append(chunk.getIdentifier());
        //判断uploadFolder/identifier 路径是否存在，不存在则创建
        if (!Files.isWritable(Paths.get(sb.toString()))) {
            log.info("路径不存在，新建路径: {}", sb.toString());
            try {
                Files.createDirectories(Paths.get(sb.toString()));
            } catch (IOException e) {
                log.error("创建路径错误:{},{}",e.getMessage(), e);
            }
        }
        return sb.append("/")
                .append(chunk.getFileName())
                .append("-")
                .append(chunk.getChunkNumber()).toString();
    }

    /**
     * 合并
     * @param file
     * @param folder
     * @param filename
     * @return 状态
     */
    public static Integer merge(String file, String folder, String filename){
        //默认合并成功
        Integer rlt = HttpServletResponse.SC_OK;
        try {
            //先判断文件是否存在
            if(fileExists(file)) {
                //文件已存在
                rlt = HttpServletResponse.SC_MULTIPLE_CHOICES;
            }else {
                //不存在的话，进行合并
                Files.createFile(Paths.get(file));
                Files.list(Paths.get(folder))
                        .filter(path -&gt; !path.getFileName().toString().equals(filename))
                        .sorted((o1, o2) -&gt; {
                            String p1 = o1.getFileName().toString();
                            String p2 = o2.getFileName().toString();
                            int i1 = p1.lastIndexOf("-");
                            int i2 = p2.lastIndexOf("-");
                            return Integer.valueOf(p2.substring(i2)).compareTo(Integer.valueOf(p1.substring(i1)));
                        })
                        .forEach(path -&gt; {
                            try {
                                //以追加的形式写入文件
                                Files.write(Paths.get(file), Files.readAllBytes(path), StandardOpenOption.APPEND);
                                //合并后删除该块
                                Files.delete(path);
                            } catch (IOException e) {
                                log.error("删除文件失败：{},{}",e.getMessage(), e);
                            }
                        });
            }
        } catch (IOException e) {
            log.error("合并失败：{},{}",e.getMessage(), e);
            //合并失败
            rlt = HttpServletResponse.SC_BAD_REQUEST;
        }
        return rlt;
    }
    /**
     * 根据文件的全路径名判断文件是否存在
     * @param file
     * @return
     */
    public static boolean fileExists(String file) {
        boolean fileExists = false;
        Path path = Paths.get(file);
        fileExists = Files.exists(path,new LinkOption[]{ LinkOption.NOFOLLOW_LINKS});
        return fileExists;
    }
}

```

```
package com.fileupload.util;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.net.URLEncoder;

/**
 * Servlet工具类
 *
 * @author huqiang
 */
public class ServletUtils {

    /**
     * 文件下载时用于写文件头部信息
     * @param request http请求
     * @param response http响应
     * @param fileName 文件名
     */
    public static void setFileDownloadHeader(HttpServletRequest request,
                                             HttpServletResponse response, String fileName) {
        try {
            String encodedFileName = null;
            String agent = request.getHeader("USER-AGENT");
            if (null != agent &amp;&amp; -1 != agent.indexOf("MSIE")) {
                encodedFileName = URLEncoder.encode(fileName, "UTF-8");
            } else if (null != agent &amp;&amp; -1 != agent.indexOf("Mozilla")) {
                encodedFileName = new String(fileName.getBytes("UTF-8"),
                        "iso-8859-1");
            } else {
                encodedFileName = URLEncoder.encode(fileName, "UTF-8");
            }

            response.setHeader("Content-Disposition", "attachment; filename=\""
                    + encodedFileName + "\"");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}

```

### 3.12启动类

```
package com.fileupload;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class FileuploadApplication {

    public static void main(String[] args) {
        SpringApplication.run(FileuploadApplication.class, args);
    }

}

```

### 3.13Sql集

```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd"&gt;
&lt;mapper namespace="com.fileupload.mapper.ChunkInfoMapper"&gt;
    &lt;resultMap id="BaseResultMap" type="com.fileupload.entity.ChunkInfo"&gt;
        &lt;!--@mbg.generated--&gt;
        &lt;!--@Table t_chunk_info--&gt;
        &lt;id column="ID" jdbcType="VARCHAR" property="id"/&gt;
        &lt;result column="CHUNK_NUMBER" jdbcType="DECIMAL" property="chunkNumber"/&gt;
        &lt;result column="CHUNK_SIZE" jdbcType="DECIMAL" property="chunkSize"/&gt;
        &lt;result column="CURRENT_CHUNKSIZE" jdbcType="DECIMAL" property="currentChunksize"/&gt;
        &lt;result column="IDENTIFIER" jdbcType="VARCHAR" property="identifier"/&gt;
        &lt;result column="FILENAME" jdbcType="VARCHAR" property="filename"/&gt;
        &lt;result column="RELATIVE_PATH" jdbcType="VARCHAR" property="relativePath"/&gt;
        &lt;result column="TOTAL_CHUNKS" jdbcType="DECIMAL" property="totalChunks"/&gt;
        &lt;result column="TOTAL_SIZE" jdbcType="INTEGER" property="totalSize"/&gt;
        &lt;result column="FILETYPE" jdbcType="VARCHAR" property="filetype"/&gt;
    &lt;/resultMap&gt;
    &lt;sql id="Base_Column_List"&gt;
        &lt;!--@mbg.generated--&gt;
        ID, CHUNK_NUMBER, CHUNK_SIZE, CURRENT_CHUNKSIZE, IDENTIFIER, FILENAME, RELATIVE_PATH,
        TOTAL_CHUNKS, TOTAL_SIZE, FILETYPE
    &lt;/sql&gt;

    &lt;select id="selectChunkNumbers" parameterType="com.fileupload.entity.ChunkInfo" resultType="int"&gt;
        select CHUNK_NUMBER
        from CHUNK_INFO
        where IDENTIFIER = #{identifier,jdbcType=VARCHAR}
          and FILENAME = #{filename,jdbcType=VARCHAR}
    &lt;/select&gt;
&lt;/mapper&gt;
```

 

```
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd"&gt;
&lt;mapper namespace="com.fileupload.mapper.FileInfoMapper"&gt;
    &lt;resultMap id="BaseResultMap" type="com.fileupload.entity.FileInfo"&gt;
        &lt;!--@mbg.generated--&gt;
        &lt;!--@Table FILE_INFO--&gt;
        &lt;id column="ID" jdbcType="VARCHAR" property="id"/&gt;
        &lt;result column="FILENAME" jdbcType="VARCHAR" property="filename"/&gt;
        &lt;result column="IDENTIFIER" jdbcType="VARCHAR" property="identifier"/&gt;
        &lt;result column="TOTAL_SIZE" jdbcType="DECIMAL" property="totalSize"/&gt;
        &lt;result column="LOCATION" jdbcType="VARCHAR" property="location"/&gt;
        &lt;result column="FILETYPE" jdbcType="VARCHAR" property="filetype"/&gt;
        &lt;result column="REF_PROJECT_ID" jdbcType="VARCHAR" property="refProjectId"/&gt;
        &lt;result column="UPLOAD_USER" jdbcType="INTEGER" property="uploadUser"/&gt;
        &lt;result column="UPLOAD_TIME" jdbcType="TIMESTAMP" property="uploadTime"/&gt;
    &lt;/resultMap&gt;
    &lt;sql id="Base_Column_List"&gt;
        &lt;!--@mbg.generated--&gt;
        ID, FILENAME, IDENTIFIER, TOTAL_SIZE, `LOCATION`, FILETYPE, REF_PROJECT_ID, UPLOAD_USER,
        UPLOAD_TIME
    &lt;/sql&gt;
    &lt;select id="selectFileList" resultMap="BaseResultMap" parameterType="com.fileupload.entity.FileInfo"&gt;
        SELECT
        &lt;include refid="Base_Column_List"/&gt;
        FROM FILE_INFO
        &lt;if test="filename != null"&gt;
            WHERE FILENAME = #{filename,jdbcType=VARCHAR}
        &lt;/if&gt;
        ORDER BY UPLOAD_TIME
    &lt;/select&gt;
&lt;/mapper&gt;
```

### 3.14mybatis-config配置文件

```
&lt;?xml version="1.0" encoding="UTF-8" ?&gt;
&lt;!--

       Copyright 2015-2016 the original author or authors.

       Licensed under the Apache License, Version 2.0 (the "License");
       you may not use this file except in compliance with the License.
       You may obtain a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

       Unless required by applicable law or agreed to in writing, software
       distributed under the License is distributed on an "AS IS" BASIS,
       WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
       See the License for the specific language governing permissions and
       limitations under the License.

--&gt;
&lt;!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd"&gt;

&lt;configuration&gt;
	&lt;!-- 配置mybatis的缓存，延迟加载等等一系列属性 --&gt;
	&lt;settings&gt;

		&lt;!-- 全局映射器启用缓存 --&gt;
		&lt;setting name="cacheEnabled" value="true" /&gt;

		&lt;!-- 查询时，关闭关联对象即时加载以提高性能 --&gt;
		&lt;setting name="lazyLoadingEnabled" value="false" /&gt;

		&lt;!-- 对于未知的SQL查询，允许返回不同的结果集以达到通用的效果 --&gt;
		&lt;setting name="multipleResultSetsEnabled" value="true" /&gt;

		&lt;!-- 允许使用列标签代替列名 --&gt;
		&lt;setting name="useColumnLabel" value="true" /&gt;

		&lt;!-- 不允许使用自定义的主键值(比如由程序生成的UUID 32位编码作为键值)，数据表的PK生成策略将被覆盖 --&gt;
		&lt;setting name="useGeneratedKeys" value="false" /&gt;

		&lt;!-- 给予被嵌套的resultMap以字段-属性的映射支持 FULL,PARTIAL --&gt;
		&lt;setting name="autoMappingBehavior" value="PARTIAL" /&gt;

		&lt;!-- 配置默认的执行器。SIMPLE 执行器没有什么特别之处。REUSE 执行器重用预处理语句。BATCH 执行器重用语句和批量更新 --&gt;
		&lt;setting name="defaultExecutorType" value="REUSE" /&gt;

		&lt;!-- Allows using RowBounds on nested statements --&gt;
		&lt;setting name="safeRowBoundsEnabled" value="false" /&gt;

		&lt;!-- Enables automatic mapping from classic database column names A_COLUMN 
			to camel case classic Java property names aColumn. --&gt;
		&lt;setting name="mapUnderscoreToCamelCase" value="true" /&gt;

		&lt;!-- MyBatis uses local cache to prevent circular references and speed 
			up repeated nested queries. By default (SESSION) all queries executed during 
			a session are cached. If localCacheScope=STATEMENT local session will be 
			used just for statement execution, no data will be shared between two different 
			calls to the same SqlSession. --&gt;
		&lt;setting name="localCacheScope" value="SESSION" /&gt;

		&lt;!-- Specifies the JDBC type for null values when no specific JDBC type 
			was provided for the parameter. Some drivers require specifying the column 
			JDBC type but others work with generic values like NULL, VARCHAR or OTHER. --&gt;
		&lt;setting name="jdbcTypeForNull" value="OTHER" /&gt;

		&lt;!-- Specifies which Object's methods trigger a lazy load --&gt;
		&lt;setting name="lazyLoadTriggerMethods" value="equals,clone,hashCode,toString" /&gt;

		&lt;!-- 设置关联对象加载的形态，此处为按需加载字段(加载字段由SQL指 定)，不会加载关联表的所有字段，以提高性能 --&gt;
		&lt;setting name="aggressiveLazyLoading" value="true" /&gt;

		&lt;!-- 控制台打印SQL --&gt;
		&lt;setting name = "logImpl" value = "STDOUT_LOGGING" /&gt;
	&lt;/settings&gt;

&lt;/configuration&gt;
```

### 3.15配置文件

```
server:
  port: 5000

# 上传文件存储路径
base:
  file-path: D:/001TCHUHU/tests

spring:
  servlet:
    multipart:
      enabled: true #是否支持 multipart 上传文件
      file-size-threshold: 0 #支持文件写入磁盘
      max-request-size: -1  #最大支持请求大小
      max-file-size: -1     #最大支持文件大小
      resolve-lazily: false  #是否支持 multipart 上传文件时懒加载
  datasource:
    # 连接池类型
    type: com.alibaba.druid.pool.DruidDataSource
    # Mysql数据库驱动
    driverClassName: com.mysql.cj.jdbc.Driver
    druid:
      url: jdbc:mysql://127.0.0.1:3306/test1?useUnicode=true&amp;characterEncoding=utf8&amp;zeroDateTimeBehavior=convertToNull&amp;useSSL=true&amp;serverTimezone=GMT%2B8
      username: root
      password: 123456
      # 初始连接数
      initialSize: 5
      # 最小连接池数量
      minIdle: 10
      # 最大连接池数量
      maxActive: 20
      # 配置获取连接等待超时的时间
      maxWait: 60000
      # 配置间隔多久才进行一次检测，检测需要关闭的空闲连接，单位是毫秒
      timeBetweenEvictionRunsMillis: 60000
      # 配置一个连接在池中最小生存的时间，单位是毫秒
      minEvictableIdleTimeMillis: 300000
      # 配置一个连接在池中最大生存的时间，单位是毫秒
      maxEvictableIdleTimeMillis: 900000
      # 配置检测连接是否有效
      validationQuery: SELECT 1 FROM DUAL
      testWhileIdle: true
      testOnBorrow: false
      testOnReturn: false

  #服务模块
  devtools:
    restart:
      enabled: true  #热部署

mybatis-plus:
  # 配置mapper的扫描，找到所有的mapper.xml映射文件
  mapper-locations: classpath*:mybatis/**/*Mapper.xml
  # 加载全局的配置文件
  config-location: classpath:mybatis/mybatis-config.xml

```

## 四、效果

分块结果：

<img alt="" height="111" src="https://img-blog.csdnimg.cn/20201110101140875.png" width="619">

上传结果：

<img alt="" height="348" src="https://img-blog.csdnimg.cn/20201110103844380.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="963">

<img alt="" height="314" src="https://img-blog.csdnimg.cn/20201110103911317.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="790">

前端请求：

<img alt="" height="856" src="https://img-blog.csdnimg.cn/20201115160837529.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1000">

 

文件分块：

<img alt="" height="452" src="https://img-blog.csdnimg.cn/20201110103827528.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="613">

<img alt="" height="804" src="https://img-blog.csdnimg.cn/20201110103942589.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1173">

结果：

<img alt="" height="303" src="https://img-blog.csdnimg.cn/20201110104028538.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="837">

 
