
--- 
title:  获取到的base64图片不显示并且控制台报错Request Header Fields Too Large & base64图片转file 
tags: []
categories: [] 

---
#### 1. 获取到的base64图片不显示并且控制台报错Request Header Fields Too Large

在获取的base64路径前添加：“data:image/jpeg;base64,”

```
const imgSrc = "data:image/jpeg;base64," + result.data.jpg_base64

```

具体参考：

#### 2. base64图片转file

```
export const base64ImgtoFile = (dataurl, filename = "file") =&gt; {<!-- -->
  const arr = dataurl.split(",");
  const mime = arr[0].match(/:(.*?);/)[1];
  const suffix = mime.split("/")[1];
  const bstr = atob(arr[1]);
  let n = bstr.length;
  const u8arr = new Uint8Array(n);
  while (n--) {<!-- -->
    u8arr[n] = bstr.charCodeAt(n);
  }
  return new File([u8arr], `${<!-- -->filename}.${<!-- -->suffix}`, {<!-- -->
    type: mime,
  });
};

```

有需要可参考： 
