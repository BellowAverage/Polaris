
--- 
title:  vscode缓存清理 
tags: []
categories: [] 

---
### 1.清理.cacheh下ipch目录

```
cd /home/xxx/.cache/vscode-cpptools/ipch &amp;&amp; rm -rf *

```

### 2.清理workspace，影响使用

```
cd /home/xxx/.vscode-server/data/User/workspaceStorage &amp;&amp; rm -rf *

```
