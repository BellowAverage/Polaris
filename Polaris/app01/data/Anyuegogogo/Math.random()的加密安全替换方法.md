
--- 
title:  Math.random()的加密安全替换方法 
tags: []
categories: [] 

---
web端

```
export default {<!-- -->
  /**生成32位uuid */
  generateUUID: () =&gt; {<!-- -->
    // @ts-ignore
    const crypto = window.crypto || window.msCrypto;
    // @ts-ignore
    return crypto.randomUUID();
  },
  /**获取0~1之间的随机数，Math.random()等价表达式 */
  getRandomValues: () =&gt; {<!-- -->
    // @ts-ignore
    const crypto = window.crypto || window.msCrypto;
    const randomBuffer = new Uint32Array(1);
    return crypto.getRandomValues(randomBuffer)[0] / Math.pow(2, 32);
  },
  /**生成一个范围内的随机数 */
  getRandomIntInclusive(min, max) {<!-- -->
    let randomNumber = this.getRandomValues();
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(randomNumber * (max - min)) + min;
  },
};

```

小程序端

```
export const getRandomValues = () =&gt; {<!-- -->
  return new Promise((resolve, reject) =&gt; {<!-- -->
    wx.getRandomValues({<!-- -->
      length: 4, // 生成 4 个字节长度的随机数,
      success: res =&gt; {<!-- -->
        let randomBytes = new Uint8Array(res.randomValues);
        let randomBytes32 = new Uint32Array(randomBytes.buffer);
        const result = randomBytes32[0] / (Math.pow(2, 32));
        resolve(result);
      },
      fail: err =&gt; {<!-- -->
        reject(err);
      }
    });
  });
};

/**生成一个范围内的随机整数 */
export const getRandomIntInclusive = (min, max) =&gt; {<!-- -->
  const min1 = min;
  const max1 = max;
  return new Promise((resolve, reject) =&gt; {<!-- -->
    wx.getRandomValues({<!-- -->
      length: 4, // 生成 4 个字节长度的随机数,
      success: res =&gt; {<!-- -->
        const randomBytes = new Uint8Array(res.randomValues);
        const randomBytes32 = new Uint32Array(randomBytes.buffer);
        const result = randomBytes32[0] / (Math.pow(2, 32));
        const min2 = Math.ceil(min1);
        const max2 = Math.floor(max1);
        const num = Math.floor(result * (max2 - min2)) + min2;
        resolve(num);
      },
      fail: err =&gt; {<!-- -->
        reject(err);
      }
    });
  });
};

// 页面中的使用
  private async calFaceTime() {<!-- -->
    const num = await getRandomIntInclusive(9, 15);
    console.log(num)
  }

```


