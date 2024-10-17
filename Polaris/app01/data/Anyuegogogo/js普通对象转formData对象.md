
--- 
title:  js普通对象转formData对象 
tags: []
categories: [] 

---
```
    paramsToFormData(obj) {<!-- -->
      const formData = new FormData();
      Object.keys(obj).forEach((key) =&gt; {<!-- -->
          if (obj[key] instanceof Array) {<!-- -->
            obj[key].forEach((item) =&gt; {<!-- -->
              formData.append(key, item);
            });
            return;
          }
          formData.append(key, obj[key]);
        });
      return formData;
    }

```
