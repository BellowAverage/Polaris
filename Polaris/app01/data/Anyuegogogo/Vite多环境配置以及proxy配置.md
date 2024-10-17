
--- 
title:  Vite多环境配置以及proxy配置 
tags: []
categories: [] 

---
### 多环境配置的实现方式

```
.env                # 所有情况下都会加载
.env.local          # 所有情况下都会加载，但会被 git 忽略
.env.[mode]         # 只在指定模式下加载
.env.[mode].local   # 只在指定模式下加载，但会被 git 忽略

```

注意：
- .env.xxx 的文件，配置的变量必须是以 VITE_ 开头： 如： VITE_BASE_URL=/api 如果你想自定义 env 变量的前缀，请参阅 。- 可以通过import.meta.env获取配置的不同环境下的变量（import.meta.env 在vite.config.ts中获取不到）
### 在vite.config.ts中配置proxy

vite提供了一个loadEnv函数，用于加载到不同环境配置文件相关参数。

>  
 loadEnv：加载 envDir 中的 .env 文件。默认情况下只有前缀为 VITE_ 会被加载，除非更改了 prefixes 配置。（envDir ：用于加载 .env 文件的目录） 


```
function loadEnv(
  mode: string,
  envDir: string,
  prefixes: string | string[] = 'VITE_'
): Record&lt;string, string&gt;


```

```
import {<!-- --> createVitePlugins } from './build/vite/plugins';
import {<!-- --> resolve } from 'path';
import {<!-- --> ConfigEnv, UserConfigExport, loadEnv } from 'vite';

const pathResolve = (dir: string) =&gt; {<!-- -->
  return resolve(process.cwd(), '.', dir);
};

// https://vitejs.dev/config/
export default function ({<!-- --> command }: ConfigEnv): UserConfigExport {<!-- -->
  const root = process.cwd();
  // const env = loadEnv(mode, __dirname)
  const env = loadEnv(command, root);
  return {<!-- -->
    root,
    server: {<!-- -->
      host: true,
      hmr: true,
      proxy: {<!-- -->
        [env.VITE_BASE_URL]: {<!-- -->
          target: env.VITE_TARGET_URL,
          changeOrigin: true,
          secure: false,
          rewrite: (path) =&gt;
            path.replace(new RegExp(`^${<!-- -->env.VITE_BASE_URL}`), '')
        }
      }
    },
  };
}



```
