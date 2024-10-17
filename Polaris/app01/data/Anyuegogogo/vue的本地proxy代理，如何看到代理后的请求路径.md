
--- 
title:  vue的本地proxy代理，如何看到代理后的请求路径 
tags: []
categories: [] 

---
proxy代理那里加上logLevel: ‘debug’，然后如果代理成功了的话，在运行项目的终端就可以看到代理请求的真实路径

```
      '/api': {<!-- -->
        target: 'https://xxxxx',
        logLevel: 'debug',
        changeOrigin: true,
        // pathRewrite: {<!-- -->
        //   '^/api': ''
        // }
      }

```
