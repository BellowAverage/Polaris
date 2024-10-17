
--- 
title:  PDF的预览以及下载 
tags: []
categories: [] 

---
### PDF预览

#### 方法一：

```
    window.open(url);

```

#### 方法二：

```
    &lt;!-- &lt;iframe
      :src="url"
      frameborder="0"
      style="width: 100%; height: 100%"
    &gt;&lt;/iframe&gt; --&gt;

```

#### 方法三：

应用vue-pdf插件，不过可能会有跨域问题

### PDF文件下载

方法一：

```
// 因为我的项目中请求的url有跨域问题，所以下面我用的是本地代理来处理请求，所以是http://localhost:8090
// 使用
    this.downFile(
      "http://localhost:8090/file/2022-08-23/236e8b1b919843bc9b027b75487c8cd6.pdf",
      "123.pdf"
    );
// 封装的方法
  public downFile(url, fileName = "", params = {<!-- -->}, method = "get") {<!-- -->
    const downLink = document.createElement("a");
    downLink.download = fileName;
    document.body.append(downLink);
    if (!method) {<!-- -->
      method = "post";
    }
    return new Promise((resolve, reject) =&gt; {<!-- -->
      axios({<!-- -->
        method,
        url,
        responseType: "arraybuffer",
        data: qs.stringify(params),
      })
        .then((res) =&gt; {<!-- -->
          console.log(res);
          // workaround
          if (res.data.byteLength &lt; 100) {<!-- -->
            reject("创建失败");
          }
          if (res.status === 200) {<!-- -->
            const blob = new Blob([res.data], {<!-- -->
            // 这里要根据需要下载的文件来匹配不同的type，下载pdf就是application/pdf
              type: "application/pdf",
            });
            downLink.href = URL.createObjectURL(blob);
            downLink.click();
            document.body.removeChild(downLink);
            resolve(res);
          } else {<!-- -->
            reject(res.statusText);
          }
        })
        .catch((error) =&gt; {<!-- -->
          document.body.removeChild(downLink);
          reject(error);
        });
    });
  }

```

这个方法亲测可行，不过因为有跨域问题，所以还是后端同事写接口解决的

#### 方法二：

后端同事写接口给我们返回文件流，可拼接路径直接用a标签打开也可用window.open（）

```
    window.open(
      this.$api.correction.file.downloadNetFile.url +
        "?url=" +
        "https://correction.img.gzsfj.gov.cn/2022-06-23/8d121a9a0c72e392567dba10f41683c8.mp4" +
        "&amp;fileName=" +
        "cc.mp4",
      "_self"
    );

```
