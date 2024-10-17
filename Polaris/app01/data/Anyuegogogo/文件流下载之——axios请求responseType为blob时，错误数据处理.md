
--- 
title:  文件流下载之——axios请求responseType为blob时，错误数据处理 
tags: []
categories: [] 

---
背景：一个文件下载的需求，如果成功下载data数据返回的是文件流，如果失败后端会返回失败信息，类似{code: -1, data: null, msg: ‘xxx’}。然而如果用responseType: 'blob’去接文件流的话，返回的错误信息也会转为blob数据格式。我们需要对返回错误信息的数据做处理，页面上提示错误信息。

```
import {<!-- --> Message } from 'element-ui';

const mimeMap: any = {<!-- -->
  xlsx: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  zip: 'application/zip'
};
/**
 * 解析blob响应内容并下载
 * @param {*} res blob响应内容
 * @param {String} mimeType MIME类型
 */
export function resolveBlob(res: any, mimeType: string) {<!-- -->
  try {<!-- -->
  	// 对错误数据的处理
    if (res.data.type === 'application/json') {<!-- -->
      const fileReader = new FileReader();
      fileReader.readAsText(res.data, 'utf-8');
      fileReader.onload = function () {<!-- -->
        const result: any = fileReader.result;
        const msg = result ? JSON.parse(result).msg : '';
        Message({<!-- -->
          message: msg || '导出文件失败',
          type: 'error'
        });
      };
      return;
    }
    const aLink = document.createElement('a');
    const blob = new Blob([res.data], {<!-- --> type: mimeMap[mimeType] });
    // //从response的headers中获取filename, 后端response.setHeader("Content-disposition", "attachment; filename=xxxx.docx") 设置的文件名;
    // eslint-disable-next-line prefer-regex-literals
    const patt = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
    const contentDisposition = decodeURI(res.headers['content-disposition']);
    const result = patt.exec(contentDisposition);
    if (result == null) {<!-- -->
      Message({<!-- -->
        message: '导出材料为空',
        type: 'error'
      });
      return;
    }
    let fileName = result[1];
    // eslint-disable-next-line no-useless-escape
    fileName = fileName.replace(/\"/g, '');
    aLink.href = URL.createObjectURL(blob);
    aLink.setAttribute('download', fileName); // 设置下载文件名称
    document.body.appendChild(aLink);
    aLink.click();
    document.body.removeChild(aLink);
  } catch (error) {<!-- -->
    Message({<!-- -->
      message: '导出文件失败',
      type: 'error'
    });
  }
}

```

重点是这一段

```
  	// 对错误数据的处理
    if (res.data.type === 'application/json') {<!-- -->
      const fileReader = new FileReader();
      fileReader.readAsText(res.data, 'utf-8');
      fileReader.onload = function () {<!-- -->
        const result: any = fileReader.result;
        const msg = result ? JSON.parse(result).msg : '';
        Message({<!-- -->
          message: msg || '导出文件失败',
          type: 'error'
        });
      };
      return;
    }

```

参考文章：
