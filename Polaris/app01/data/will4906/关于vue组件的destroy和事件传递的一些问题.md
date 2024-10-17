
--- 
title:  关于vue组件的destroy和事件传递的一些问题 
tags: []
categories: [] 

---
事情是这样的，遇到了一个问题：

>  
 使用vue进行开发的时候，在一个组件中使用事件总线进行事件监听之后，当组件销毁后该事件依然被监听。 


### 背景

vue对于跨组件的事件监听处理有一个逐渐变迁的过程。

#### $dispath和$broadcast

在新版vue中废弃了旧版的一种事件传递方式。使用dispath和broadcast两种方式进行事件的传递响应。
<li>  是由子组件发起事件通知，向其父组件链中寻找对应的事件监听。直到找到最近的父组件的一个事件监听之后停止寻找，除非监听器返回true。(如果该子组件存在对该事件的监听也会被触发) 
  <blockquote> 
   Usage: Dispatch an event, first triggering it on the instance itself, and then propagates upward along the parent chain. The propagation stops when it triggers a parent event listener, unless that listener returns true. Any additional arguments will be passed into the listener’s callback function. 
  </blockquote> </li><li>  则是由父组件向其子组件中传递消息，在子组件链路中找到事件监听之后，停止寻找，除非监听器返回true 
  <blockquote> 
   Usage: Broadcast an event that propagates downward to all descendants of the current instance. Since the descendants expand into multiple sub-trees, the event propagation will follow many different “paths”. The propagation for each path will stop when a listener callback is fired along that path, unless the callback returns true. 
  </blockquote> </li>
>  
   Usage: Broadcast an event that propagates downward to all descendants of the current instance. Since the descendants expand into multiple sub-trees, the event propagation will follow many different “paths”. The propagation for each path will stop when a listener callback is fired along that path, unless the callback returns true. 
  

后来这种方案就被废弃了。因为

>  
 因为基于组件树结构的事件流方式实在是让人难以理解，并且在组件结构扩展的过程中会变得越来越脆弱。这种事件方式确实不太好，我们也不希望在以后让开发者们太痛苦。并且$dispatch 和 $broadcast 也没有解决兄弟组件间的通信问题。 


后来的设计也就改成了子组件使用$emit可以通知父组件，然后父组件在该组件的子组件上用@事件名称监听回调。但是这种方式无法进行更广泛的事件通知监听。官方文档建议在简单的情况下可以使用使用全局vue实例的方法进行事件通知。

#### 使用vue事件总线

在简单情况下，我们可以新建一个全局的vue实例，使用$on, $off和$emit三个函数构建一个事件通知体系。

```
let bus = new Vue()

... A Vue Component
methods: {<!-- -->
    hello () {<!-- -->
        bus.$emit('eventName')
    }
}
... B Vue Component
methods: {<!-- -->
    mounted () {<!-- -->
        bus.$on('eventName', () =&gt; {<!-- -->
            // answer the event
        })
    },
    destroyed () {<!-- -->
        bus.$off('eventName')
    }
}

```

使用这种方式就可以实现在整个工程中的事件通知操作。

### 回到问题

有一次笔者在进行开发的时候没有对事件进行解绑的操作，也就是没有在destroyed函数中调用$off进行事件解绑。事件中包含http请求的函数。然后在后续的操作中有一些重新挂载该组件的操作。检查devtool的network时发现多次发出该请求。定位后发现是$on的事件被多次执行。遂在destroyed中$off掉该事件则没有该问题。

笔者于是产生了些疑惑，决定模拟一下该问题并去vue的源码一探究竟，毕竟vue的源码也就万把来行嘛(手动滑稽)

#### 情景复现

编写了一段代码复现了上文中出现的问题。不是特别长就贴上来了。

##### 复现代码

```
&lt;html&gt;
    &lt;body&gt;
        &lt;div id="app"&gt;
            &lt;button v-on:click="hide"&gt;{<!-- -->{ message }}&lt;/button&gt;
            &lt;my v-if="show"&gt;&lt;/my&gt;
            &lt;my v-if="show"&gt;&lt;/my&gt;
            &lt;my v-if="show"&gt;&lt;/my&gt;
            &lt;button v-on:click="print"&gt;触发总线事件&lt;/button&gt;
            &lt;button v-on:click="printBus"&gt;打印事件总线&lt;/button&gt;
            &lt;button v-on:click="printApp"&gt;打印app实例&lt;/button&gt;
        &lt;/div&gt;
        &lt;script src="./vue.js"&gt;&lt;/script&gt;
        &lt;script type="text/javascript"&gt;
            let bus = new Vue()
            Vue.component('my', {<!-- -->
                data () {<!-- -->
                    return {<!-- -->
                        nowIndex: 1
                    }
                },
                template: `
                    &lt;div&gt;
                        组件操作数：{<!-- -->{ nowIndex }} &lt;/br&gt;
                        &lt;button v-on:click="nowIndex ++"&gt;添加&lt;/button&gt;&lt;button v-on:click="selfDestroy"&gt;调用组件destroy函数&lt;/button&gt;
                    &lt;/div&gt;
                `,
                mounted () {<!-- -->
                    bus.$on('eventone', value =&gt; {<!-- -->
                        console.log('id: ', this._uid, ' \'s nowIndex is', this.nowIndex)
                    })
                },
                destroyed () {<!-- -->
                    console.log('hello destroyed')
                },
                methods: {<!-- -->
                    selfDestroy () {<!-- -->
                        this.$destroy()
                    }
                }
            })
            let app = new Vue({<!-- -->
                el: '#app',
                data: {<!-- -->
                    message: '隐藏',
                    show: true
                },
                methods: {<!-- -->
                    hide () {<!-- -->
                        this.show = !this.show
                        if (this.show) {<!-- -->
                            this.message = '隐藏'
                        } else {<!-- -->
                            this.message = '显示'
                        }
                    },
                    print () {<!-- -->
                        bus.$emit('eventone')
                    },
                    printBus () {<!-- -->
                        console.log(bus)
                    },
                    printApp () {<!-- -->
                        console.log(this)
                    }
                }
            })
        &lt;/script&gt;
    &lt;/body&gt;
&lt;/html&gt;

```

##### 复现操作
1.  先对页面进行操作之后，触发总线事件 <img src="https://img-blog.csdn.net/20180910105247648?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dpbGw0OTA2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述"> 1.  随后取消三个组件的挂载 <img src="https://img-blog.csdn.net/20180910105338862?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dpbGw0OTA2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述"> 1.  再度挂载三个组件 <img src="https://img-blog.csdn.net/20180910105350844?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dpbGw0OTA2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述"> 可以看出控制台依旧打印出了三个已经通过v-if取消挂载的组件，destroyed函数也被触发了 
#### 提出问题
1. 为什么事件会触发多次？1. 为什么已经销毁的组件里面的事件依旧会被触发？
#### 寻找答案
<li> 先去到了vue的事件绑定函数$on中 <pre><code class="prism language-javascript">Vue.prototype.$on = function (event, fn) {<!-- -->
    var this$1 = this;

    var vm = this;
    if (Array.isArray(event)) {<!-- -->
        for (var i = 0, l = event.length; i &lt; l; i++) {<!-- -->
            this$1.$on(event[i], fn);
        }
    } else {<!-- -->
        (vm._events[event] || (vm._events[event] = [])).push(fn);
        // optimize hook:event cost by using a boolean flag marked at registration
        // instead of a hash lookup
        if (hookRE.test(event)) {<!-- -->
            vm._hasHookEvent = true;
        }
    }
    return vm
};
</code></pre> 这段代码其实已经比较清晰了，通过`(vm._events[event] || (vm._events[event] = [])).push(fn)`可以看出vue对事件监听的绑定方法其实是将同名事件的处理函数存放到一个数组中后续按存放顺序调用。所以事件可以被触发多次。 </li><li> 再看一下vue的销毁组件函数。 <pre><code class="prism language-javascript">Vue.prototype.$destroy = function () {<!-- -->
    var vm = this;
    if (vm._isBeingDestroyed) {<!-- -->
    return
    }
    callHook(vm, 'beforeDestroy');
    vm._isBeingDestroyed = true;
    // remove self from parent
    var parent = vm.$parent;
    if (parent &amp;&amp; !parent._isBeingDestroyed &amp;&amp; !vm.$options.abstract) {<!-- -->
        remove(parent.$children, vm);
    }
    // teardown watchers
    if (vm._watcher) {<!-- -->
        vm._watcher.teardown();
    }
    var i = vm._watchers.length;
    while (i--) {<!-- -->
        vm._watchers[i].teardown();
    }
    // remove reference from data ob
    // frozen object may not have observer.
    if (vm._data.__ob__) {<!-- -->
        vm._data.__ob__.vmCount--;
    }
    // call the last hook...
    vm._isDestroyed = true;
    // invoke destroy hooks on current rendered tree
    vm.__patch__(vm._vnode, null);
    // fire destroyed hook
    callHook(vm, 'destroyed');
    // turn off all instance listeners.
    vm.$off();
    // remove __vue__ reference
    if (vm.$el) {<!-- -->
        vm.$el.__vue__ = null;
    }
    // release circular reference (#6759)
    if (vm.$vnode) {<!-- -->
        vm.$vnode.parent = null;
    }
};
</code></pre> 笔者看这段代码原先以为vue通过这个函数对组件进行了销毁，可是事情并没有想象中的这么简单。甚至有那么点疑惑。于是决定在控制台试一下这个方法。 <img src="https://img-blog.csdn.net/20180910105404285?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dpbGw0OTA2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="这里写图片描述"> 从图可以看出调用$destroy()函数后，vue组件确实走了destroyed()方法，也就是说确实成功销毁了。而此时该组件的事件响应依然被触发，而且此时浏览器上的dom并没有被移除。于是又回去看源码，发现有remove和__patch__两个类似移除的函数，这里篇幅问题不再粘贴源码了，不过看完后发现后整个删除逻辑只是把虚拟dom给删除了而已，并没有删除已经渲染的dom。文档中给出的解释是 
  <blockquote> 
   完全销毁一个实例。清理它与其它实例的连接，解绑它的全部指令及事件监听器。 
  </blockquote> 文档这句话其实是有点迷的，个人觉得后面一句是在对第一句的解释。$destroy函数只是在清理它和其它实例的连接和解除指令以及事件监听器，还有断掉虚拟dom和真实dom之间的联系。而并真正地没有回收这个vue实例。而且由于vue的$on只是绑定了函数，$destroy也没有将注册在其它vue实例的事件给销毁掉，所以这个及时destroy后总线的事件依旧被执行，而且由于注册事件的vue实例没有被回收，所以还可以进行常规的数据交互操作。 至于vue实例什么时候回收，这其实本质上是一个js的内存回收问题。只要存在还有其他对象对该实例的引用的话，这个实例还是不会被回收的。当当前程序没有对这个实例的引用的时候，这个vue实例就会被释放了。 </li>