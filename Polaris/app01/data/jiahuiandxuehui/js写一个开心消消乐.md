
--- 
title:  js写一个开心消消乐 
tags: []
categories: [] 

---


#### 目录标题
- - - - - <ul><li><ul><li>


## 展示

<img src="https://img-blog.csdnimg.cn/67cbc0b73446469a8eda87ad2ece72e3.gif" alt="请添加图片描述">

## 游戏背景

一天晚上，天空中掉下一颗神奇的豌豆种子，正好落在了梦之森林的村长屋附近，种子落地后吸收了池塘的水分，迅速成长，一夜之间变成参天大藤蔓…… 第二天早上，村民们醒来后看到巨大的藤蔓都惊呆了，聚在一起议论纷纷。有人说他似乎看到村长的房子在高耸入云的藤蔓上，房子似乎还在上升，有人号召说应该爬上去救村长，玩家需要爬到藤曼顶部救出村长

## 游戏规则

把三个颜色相同的小动物连成一条直线，即可消除。达到指定的目标通关后。游戏的模板有四种分别是分数过关、指定消除、获得金豆荚、云朵关卡。

## 源码部分

主页面js部分调用了微信分享api

```
&lt;/script&gt;

&lt;div id="share" style="display: none"&gt;
		&lt;img width="100%" src="bitmap/share.png" style="position: fixed; z-index: 9999; top: 0; left: 0; display: " ontouchstart="document.getElementById(&amp;#39;share&amp;#39;).style.display=&amp;#39;none&amp;#39;;"&gt;
	&lt;/div&gt;
&lt;script&gt;
	var mebtnopenurl = "http://mp.weixin.qq.com/s?__biz=MzA5MzU2MjU3Mw==&amp;mid=218850712&amp;idx=1&amp;sn=53bfed8c43391843a6268706ccda8eb2&amp;scene=1&amp;key=1936e2bc22c2ceb5b8b45ee0ef26a5cc01639c3411c2cfd0bd74efb6f0a180003056abc9700e348732a0a5c963462d2f&amp;ascene=1&amp;uin=MjgxMTA4MTUwMQ%3D%3D&amp;devicetype=Windows+7&amp;version=61000721&amp;pass_ticket=w4kQ%2FSFhaY2mmOE87ChVgbTRWP%2BctOhqXukbldnl%2FXb4%2BOxgCyIxSdzUjax%2FUmHK";
	var tit = "";
	var DFW = {<!-- -->
		appId: "",
		TLImg: "kaixinlian.jpg",
		url: "http://www.mycodes.net/166/",
		title: "开心消消乐-多多游戏",
		desc: "我消，我消，我消...！"
	};
	var onBridgeReady = function () {<!-- -->
		WeixinJSBridge.on('menu:share:appmessage', function (argv) {<!-- -->
			WeixinJSBridge.invoke('sendAppMessage', {<!-- -->
				"appid": DFW.appId,
				"img_url": DFW.TLImg,
				"img_width": "120",
				"img_height": "120",
				"link": DFW.url,
				"title": DFW.title + tit,
				"desc": DFW.desc
			}
			);
		});
		WeixinJSBridge.on('menu:share:timeline', function (argv) {<!-- -->
			WeixinJSBridge.invoke('shareTimeline', {<!-- -->
				"appid": DFW.appId,
				"img_url": DFW.TLImg,
				"img_width": "120",
				"img_height": "120",
				"link": DFW.url,
				"title": DFW.title + tit,
				"desc": DFW.desc
			}
			);
		});
	};
	if (document.addEventListener) {<!-- --> 
		document.addEventListener('WeixinJSBridgeReady', onBridgeReady, false);
	} else if (document.attachEvent) {<!-- -->
		document.attachEvent('WeixinJSBridgeReady', onBridgeReady);
		document.attachEvent('onWeixinJSBridgeReady', onBridgeReady);
	}
	function do_share(score) {<!-- -->
		document.title = "我获得了" + score + "分，一起来消星星吧！";

		document.getElementById("share").style.display = "";
		window.DFW.title = document.title;
	}
	function dp_submitScore(level,score) {<!-- -->
		//alert("你获得" + score + "分");
		if (score &gt; 5000) {<!-- -->
			if (confirm("你获得了" + score + " 要不要通知下小伙伴们呢？")) {<!-- -->
				do_share(score);
			}
		}
	}
&lt;/script&gt;

```

#### 对关卡的地图设置

```
level: [{<!-- -->
				time: 300,
				map: [
					[, , , , , , , , ],
					[, , , 0, 0, 0, , , ],
					[, , 0, 0, 0, 0, 0, , ],
					[, 0, 0, 1, 0, 1, 0, 0],
					[, 0, 1, 0, 1, 0, 1, 0],
					[, 0, 1, 1, 0, 1, 1, 0],
					[, , 0, 0, , 0, 0, , ]
				]
			}, {<!-- -->
				time: 300,
				map: [
					[, , , , , , , , ],
					[, , 0, 0, 0, 0, 0, , ],
					[, 0, 0, 1, 1, 1, 0, 0],
					[, 0, 0, 1, , 1, 0, 0],
					[, 0, 0, 1, 1, 1, 0, 0],
					[, , 1, 1, 0, 1, 1, , ],
					[, 0, 0, 0, 0, 0, 0, 0]
				]
			}, {<!-- -->
				time: 300,
				map: [
					[, 0, 0, 0, 0, 0, 0, 0],
					[, , 0, 0, 1, 0, 0, , ],
					[, , , 1, 1, 1, , , ],
					[, , , , 4, , , , ],
					[, , , 0, 0, 0, , , ],
					[, , 0, 0, 1, 0, 0, , ],
					[, 0, 1, 1, 1, 1, 1, 0],
					[0, 0, 0, 1, 1, 1, 0, 0, 0]
				]
			}, {<!-- -->
				time: 300,
				map: [
					[, 0, 0, 0, 0, 0, 0, 0],
					[, , 0, 0, 0, 0, 0, 0],
					[, 0, 1, 0, , 1, 1, 0],
					[, 0, 1, , 0, 0, 1, 0],
					[, 0, 1, 0, 0, , 1, 0],
					[, 0, 1, 1, , 0, 1, 0],
					[, 0, 0, 0, 0, 0, 0, , ]
				]
			}, {<!-- -->
				time: 300,
				map: [
					[0, 1, 0, 0, 0, 0, 0, 1, 1],
					[0, 1, 0, 0, 0, 0, 1, 1, 0],
					[, 0, 0, 0, 0, 1, 1, 0, 0],
					[, , 0, 0, 1, 1, 0, 0, 0],
					[, , , 1, 1, 4, 4, 4, 4],
					[, , , , 0, 0, 0, 0, 0],
					[, , , , , 0, 0, 1, 1],
					[, , , , , , 0, 0, 0]
				]
			}, {<!-- -->
				time: 300,
				map: [
					[, 0, 0, 0, , 0, 0, 0],
					[, 0, 0, 0, , 0, 0, 0],
					[0, 0, 0, 0, , 0, 0, 0, 0],
					[0, 0, 0, 0, , 0, 0, 0, 0],
					[1, 1, 1, 1, , 1, 1, 1, 1],
					[0, 4, 4, 4, , 4, 4, 4, 0],
					[, 1, 1, 1, , 1, 1, 1],
					[, 0, 0, 0, , 0, 0, 0]
				]
			}, {<!-- -->
				time: 360,
				map: [
					[, , , 0, 0, 0, , , ],
					[, , 0, 0, 1, 0, 0, , ],
					[, , 0, 1, 1, 1, 0, , ],
					[, , 0, 5, 5, 5, 0, , ],
					[, 0, 0, 1, 1, 1, 0, 0],
					[, 0, 0, 2, 2, 2, 0, 0],
					[, 1, 1, 0, 0, 0, 1, 1],
					[, 0, 0, , 0, , 0, 0]
				]
			}, {<!-- -->
				time: 360,
				map: [
					[0, 0, 0, 0, , 0, 0, 0, 0],
					[, 0, 0, 0, , 0, 0, 0],
					[, , 0, 0, 0, 0, 0, , ],
					[, 0, 2, 2, 0, 2, 2, 0],
					[0, 0, , 0, 0, 0, , 0, 0],
					[1, 1, 1, 0, , 0, 1, 1, 1],
					[0, 1, 1, 1, 0, 1, 1, 1, 0],
					[, 0, 0, 0, , 0, 0, 0]
				]
			}, {<!-- -->
				time: 360,
				map: [
					[1, 1, 1, 0, 0, 0, 1, 1, 1],
					[1, 2, 1, 0, , 0, 1, 2, 1],
					[1, 1, 1, , 0, , 1, 1, 1],
					[0, 0, , 0, 0, 0, , 0, 0],
					[0, , 0, 0, 0, 0, 0, , 0],
					[, , 0, 5, 5, 5, 0, , ],
					[, 0, 0, 1, 2, 1, 0, 0],
					[, 0, 0, 1, 1, 1, 0, 0]
				]
			}, {<!-- -->
				time: 300,
				map: [
					[, , , 0, 0, 0, , , ],
					[, , 0, 1, 1, 1, 0, , ],
					[, 0, 0, 1, 1, 1, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, , , 0, , , 0, 0],
					[0, 0, 0, 2, 8, 2, 0, 0, 0],
					[, 0, 1, 0, 2, 0, 1, 0, 0],
					[, 0, 1, 0, 0, 0, 1, 0]
				]
			}, {<!-- -->
				time: 360,
				map: [
					[, 0, 0, 0, , 0, 0, 0],
					[, 0, 0, 1, 0, 1, 0, 0],
					[0, 0, 1, 1, 0, 1, 1, 0, 0],
					[1, 1, 1, , 0, , 1, 1, 1],
					[1, 8, 1, 1, 1, 1, 1, 8, 1],
					[, 0, , 1, 2, 1, , 0],
					[, 0, 0, 1, 1, 1, 0, 0],
					[0, 0, 0, 1, 1, 1, 0, 0, 0]
				]

```

### 介绍一下游戏中的一些功能

```
自动填充
autoFill: function() {<!-- -->
					var a = this.graph,
						b, c, k, f, e, l, m, n, p = d.Tile;
					k = a.length;
					for (b = 0; b &lt; k; b++) for (c = a[b].length; c--;) if (f = a[b][c], f !== h &amp;&amp; 0 === f[3] &amp;&amp; (e = a[b - 1], e !== h &amp;&amp; 0 !== e.length ? (m = (l = e[c - 1]) !== h &amp;&amp; 0 === l[1] &amp;&amp; l[2] !== h ? !0 : !1, n = (l = e[c]) !== h &amp;&amp; 0 === l[1] &amp;&amp; l[2] !== h ? !0 : !1, e = (l = e[c + 1]) !== h &amp;&amp; 0 === l[1] &amp;&amp; l[2] !== h ? !0 : !1) : m = n = e = !0, !0 === m || !0 === n || !0 === e)) {<!-- -->
						f[2] = d.random(p.length - 1);
						e = a[b];
						n = 3;
						for (m = h; n--;) if (l = e[c + n], 0 === n) {<!-- -->
							m = l;
							do l = d.random(p.length - 1);
							while (f[2] === l);
							f[2] = l
						} else if (l === h || l[2] !== f[2]) break;
						for (n = 3; n--;) if (l = a[b - n], 0 === n) {<!-- -->
							do l = d.random(p.length - 1);
							while (f[2] === l || f[2] === m);
							f[2] = l
						} else if (l === h || (l = l[c]) === h || l[2] !== f[2]) break
					}
					for (b = a.length; b--;) for (c = a[b].length; c--;) f = a[b][c], f !== h &amp;&amp; f[2] !== h &amp;&amp; 0 === f[3] &amp;&amp; (f[5].sprite(p[f[2]]), f[5].position(f[7], f[8]), f[5].slice(0, 1), f[5].index(0));
					this.tile.draw()
				},

```

```
findNext: function(a) {<!-- -->
					var b = this.graph,
						c = [],
						d = [],
						f, e, l, m, n, p, q, r;
					for (f = b.length; f--;) for (e = b[f].length, c[f] = [], d[f] = []; e--;) n = b[f][e], c[f][e] = n === h ? h : n[2], d[f][e] = n === h || 0 === n[1] ? h : !0;
					if ("object" === typeof a) for (b = a.length; b--;) n = a[b], c[n[0]][n[1]] = -1;
					for (f = c.length; f--;) for (e = a = c[f].length; e--;) if (r = 4, n = c[f][e], n !== h &amp;&amp; !0 !== d[f][e]) for (; r--;) {<!-- -->
						b = h;
						n = f;
						p = e;
						switch (r) {<!-- -->
						case 0:
							0 &lt; e - 1 &amp;&amp; c[f][e - 1] !== h &amp;&amp; !0 !== d[f][e - 1] &amp;&amp; (q = 1, n = l = f, p = m = e - 1, b = c[f][e], c[f][e] = c[f][e - 1], c[f][e - 1] = b);
							break;
						case 1:
							c[f - 1] !== h &amp;&amp; c[f - 1][e] !== h &amp;&amp; !0 !== d[f - 1][e] &amp;&amp; (q = 0, n = l = f - 1, p = m = e, b = c[f][e], c[f][e] = c[f - 1][e], c[f - 1][e] = b);
							break;
						case 2:
							e + 1 &lt; a &amp;&amp; c[f][e + 1] !== h &amp;&amp; !0 !== d[f][e + 1] &amp;&amp; (q = 1, l = f, m = e + 1, b = c[f][e], c[f][e] = c[f][e + 1], c[f][e + 1] = b);
							break;
						case 3:
							c[f + 1] !== h &amp;&amp; c[f + 1][e] !== h &amp;&amp; !0 !== d[f + 1][e] &amp;&amp; (q = 0, l = f + 1, m = e, b = c[f][e], c[f][e] = c[f + 1][e], c[f + 1][e] = b)
						}
						if (b !== h) {<!-- -->
							if (!0 === this.autoCheck(c)) return {<!-- -->
								convert: q,
								row: n,
								col: p,
								reject: [
									[f, e],
									[l, m]
								]
							};
							switch (r) {<!-- -->
							case 0:
								b = c[f][e];
								c[f][e] = c[f][e - 1];
								c[f][e - 1] = b;
								break;
							case 1:
								b = c[f][e];
								c[f][e] = c[f - 1][e];
								c[f - 1][e] = b;
								break;
							case 2:
								b = c[f][e];
								c[f][e] = c[f][e + 1];
								c[f][e + 1] = b;
								break;
							case 3:
								b = c[f][e], c[f][e] = c[f + 1][e], c[f + 1][e] = b
							}
						}
					}
					return !1
				},

```

## <font color="red" size="6">点击直接资料领取</font>

0023 **如果你在学习python或者Java哪怕是C遇到问题都可以来给我留言，因为在学习初期新手总会走很多弯路，这个时候如果没有有个人来帮一把的话很容易就放弃了。身边很多这样的例子许多人学着学着就转了专业换了方向，不仅是自身问题还是没有正确的学习。所以作为一个过来人我希望有问题给我留言，说不上是帮助就是顺手敲几行字的事情。**

**这里有python，Java学习资料还有有有趣好玩的编程项目，更有难寻的各种资源。反正看看也不亏。**
