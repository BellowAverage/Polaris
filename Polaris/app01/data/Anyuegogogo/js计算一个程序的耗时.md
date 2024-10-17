
--- 
title:  js计算一个程序的耗时 
tags: []
categories: [] 

---
```
      console.time('aa')
      for (var i = 0; i &lt; 1000; i++) {<!-- --> console.log(i) };
      console.timeEnd('aa')

```

例如：

```
    /**
     * 获取经纬度
     */
    getLocation() {<!-- -->
      console.time('aa')
      for (var i = 0; i &lt; 1000; i++) {<!-- --> console.log(i) };
      const that = this
      wx.getLocation({<!-- -->
        type: 'gcj02',
        isHighAccuracy: false,
        highAccuracyExpireTime: 6000,
        success: function (res) {<!-- -->
          console.timeEnd('aa')
          that.locationDoneFlag = true
          that.$apply()
          that.signDTO.latAndLng = res.latitude + ',' + res.longitude
          that.getLocal(res.latitude, res.longitude)
        },
        fail: function (res) {<!-- -->
          that.getUserLocation()
        }
      })
    }

```
