
--- 
title:  eslint报错：＞‘expected‘ && The keyword ‘import‘ is reserved && The keyword ‘const‘ is reserved 
tags: []
categories: [] 

---
eslint报错：
- error Parsing error: ‘＞‘ expected…- Parsing error: The keyword ‘import’ is reserved- Parsing error: The keyword ‘const’ is reserved
修改如下：

```
module.exports = {<!-- -->
  ......
  'parser': 'vue-eslint-parser',
  'parserOptions': {<!-- -->
    'ecmaVersion': 6,
    'sourceType': 'module',
    'parser': '@typescript-eslint/parser',
  }
};


```

添加’parser’: ‘@typescript-eslint/parser’，记得需要安装依赖npm install @typescript-eslint/parser --save-dev
