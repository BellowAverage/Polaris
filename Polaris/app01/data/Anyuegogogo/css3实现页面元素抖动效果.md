
--- 
title:  css3实现页面元素抖动效果 
tags: []
categories: [] 

---
html

```
&lt;div id="shake" class="shape"&gt;horizontal shake&lt;/div&gt;

```

js（vue3）

```
  function shake(elemId) {<!-- -->
    const elem = document.getElementById(elemId)
    console.log('获取el', elem)

    if (elem) {<!-- -->
      elem.classList.add('shake')
      setTimeout(() =&gt; {<!-- -->
        elem.classList.remove('shake')
      }, 800)
    }
  }

  onMounted(() =&gt; {<!-- -->
    setTimeout(() =&gt; {<!-- -->
      console.log('进来settimeout')
      shake('shake')
    }, 5000)
  })


```

css

```
  .shape {<!-- -->
    margin: 50px;
    width: 200px;
    height: 50px;
    line-height: 50px;
    text-align: center;
    border: 1px solid black;
  }
  .shake {<!-- -->
    animation: shake 800ms ease-in-out;
  }
  @keyframes shake {<!-- -->
    /* 水平抖动，核心代码 */
    10%,
    90% {<!-- -->
      transform: translate3d(-1px, 0, 0);
    }
    20%,
    80% {<!-- -->
      transform: translate3d(+2px, 0, 0);
    }
    30%,
    70% {<!-- -->
      transform: translate3d(-4px, 0, 0);
    }
    40%,
    60% {<!-- -->
      transform: translate3d(+4px, 0, 0);
    }
    50% {<!-- -->
      transform: translate3d(-4px, 0, 0);
    }
  }

```

参考链接：
