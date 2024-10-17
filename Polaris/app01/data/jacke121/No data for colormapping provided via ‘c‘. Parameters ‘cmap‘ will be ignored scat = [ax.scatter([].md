
--- 
title:  No data for colormapping provided via ‘c‘. Parameters ‘cmap‘ will be ignored scat = [ax.scatter([] 
tags: []
categories: [] 

---


No data for colormapping provided via 'c'. Parameters 'cmap' will be ignored scat = [ax.scatter([], [], [], zorder=10, cmap=ListedColormap(["r", "g", "b"])) for _ in range(4)]

报警的代码：

```
scat = [ax.scatter([], [], [], zorder=10, cmap=ListedColormap(["r", "g", "b"])) for _ in range(4)]
```



新代码：

```
scat = [ax.scatter([], [], [], c=[],zorder=10, cmap=ListedColormap(["r", "g", "b"])) for _ in range(4)]
```


