
--- 
title:  vue3实现TabsView(包含鼠标滚动横向滚动条以及鼠标右击菜单) 
tags: []
categories: [] 

---
TagsView.vue

```
&lt;template&gt;
	&lt;div id="tags-view-container" class="tags-view-container"&gt;
		&lt;div class="tags-view-wrapper scroll-pane" id="scroll"&gt;
			&lt;router-link
				v-for="tag in visitedViews"
				:key="tag.path"
				:data-path="tag.path"
				:class="isActive(tag) ? 'active' : ''"
				:to="{ path: tag.path, query: tag.query, fullPath: tag.fullPath }"
				class="tags-view-item"
				:style="activeStyle(tag)"
				@click.middle="!isAffix(tag) ? closeSelectedTag(tag) : ''"
				@contextmenu.prevent="openMenu(tag, $event)"
			&gt;
				{<!-- -->{<!-- --> tag.title }}
				&lt;span v-if="!isAffix(tag)" @click.prevent.stop="closeSelectedTag(tag)"&gt;
					&lt;t-icon name="close" style="width: 1em; height: 1em; vertical-align: middle" /&gt;
				&lt;/span&gt;
			&lt;/router-link&gt;
		&lt;/div&gt;

		&lt;ul v-show="visible" :style="{ left: left + 'px', top: top + 'px' }" class="contextmenu"&gt;
			&lt;!-- &lt;li @click="refreshSelectedTag(selectedTag)"&gt;刷新页面&lt;/li&gt; --&gt;
			&lt;li v-if="!isAffix(selectedTag)" @click="closeSelectedTag(selectedTag)"&gt;关闭当前&lt;/li&gt;
			&lt;li @click="closeOthersTags(selectedTag)"&gt;关闭其他&lt;/li&gt;
			&lt;li @click="closeAllTags(selectedTag)"&gt;全部关闭&lt;/li&gt;
		&lt;/ul&gt;
	&lt;/div&gt;
&lt;/template&gt;

&lt;script setup lang="ts"&gt;
import {<!-- --> usePermissionStore, useTagsViewStore } from '@/store';
import path from 'path';

import {<!-- --> color } from 'echarts';
defineOptions({<!-- -->
	name: 'TagsView',
});

/**
 * @desc: Types
 */

/**
 * @desc: Ref
 */

/**
 * @desc: Hooks
 */
const {<!-- --> proxy } = getCurrentInstance();
const route = useRoute();
const router = useRouter();

/**
 * @desc: Data
 */
const visible = ref(false);
const top = ref(0);
const left = ref(0);
const selectedTag = ref({<!-- -->});
const affixTags = ref([]);
const tagsViewStore = useTagsViewStore();

/**
 * @desc: Watch
 */
watch(route, () =&gt; {<!-- -->
	addTags();
	moveToCurrentTag();
});

watch(visible, (value) =&gt; {<!-- -->
	if (value) {<!-- -->
		document.body.addEventListener('click', closeMenu);
	} else {<!-- -->
		document.body.removeEventListener('click', closeMenu);
	}
});

/**
 * @desc: Computed
 */
//  const key = computed(() =&gt; {<!-- -->
// 	return route.path;
// });
const visitedViews = computed(() =&gt; tagsViewStore.visitedViews);

const routes = computed(() =&gt; usePermissionStore().routes);

/**
 * @desc: 方法
 */
// 初始化与绑定监听事件方法
const scrollInit = () =&gt; {<!-- -->
	// 获取要绑定事件的元素
	const nav = document.getElementById('tags-view-container');
	const scrollDiv = document.getElementById('scroll');
	// document.addEventListener('DOMMouseScroll', handler, false)
	// 添加滚轮滚动监听事件，一般是用下面的方法，上面的是火狐的写法
	nav.addEventListener('mousewheel', handler, false);
	// 滚动事件的出来函数
	function handler(event) {<!-- -->
		// 获取滚动方向
		const detail = event.wheelDelta || event.detail;
		// 定义滚动方向，其实也可以在赋值的时候写
		const moveForwardStep = 1;
		const moveBackStep = -1;
		// 定义滚动距离
		let step = 0;
		// 判断滚动方向,这里的100可以改，代表滚动幅度，也就是说滚动幅度是自定义的
		if (detail &lt; 0) {<!-- -->
			step = moveForwardStep * 100;
		} else {<!-- -->
			step = moveBackStep * 100;
		}
		// 对需要滚动的元素进行滚动操作
		scrollDiv.scrollLeft += step;
	}
};

function openMenu(tag, e) {<!-- -->
	const menuMinWidth = 105;
	const offsetLeft = proxy.$el.getBoundingClientRect().left; // container margin left
	const offsetWidth = proxy.$el.offsetWidth; // container width
	const maxLeft = offsetWidth - menuMinWidth; // left boundary
	const l = e.clientX - offsetLeft + 15; // 15: margin right

	if (l &gt; maxLeft) {<!-- -->
		left.value = maxLeft;
	} else {<!-- -->
		left.value = l;
	}

	top.value = e.clientY - 64 - 8; // 64: header 8 margin
	visible.value = true;
	selectedTag.value = tag;
}

function closeMenu() {<!-- -->
	visible.value = false;
}

function isAffix(tag) {<!-- -->
	return tag.meta &amp;&amp; tag.meta.affix;
}

function addTags() {<!-- -->
	const {<!-- --> name } = route;
	if (name) {<!-- -->
		tagsViewStore.addVisitedView(route);
	}
	return false;
}

function moveToCurrentTag() {<!-- -->
	nextTick(() =&gt; {<!-- -->
		for (const r of visitedViews.value) {<!-- -->
			if (r.path === route.path) {<!-- -->
				// scrollPaneRef.value.moveToTarget(r);
				// when query is different then update
				if (r.fullPath !== route.fullPath) {<!-- -->
					tagsViewStore.updateVisitedView(route);
				}
			}
		}
	});
}

function toLastView(visitedViews, view) {<!-- -->
	const latestView = visitedViews.slice(-1)[0];
	if (latestView) {<!-- -->
		router.push(latestView.fullPath);
	} else {<!-- -->
		// now the default is to redirect to the home page if there is no tags-view,
		// you can adjust it according to your needs.
		if (view.name === 'Dashboard') {<!-- -->
			// to reload home page
			router.replace({<!-- --> path: '/redirect' + view.fullPath });
		} else {<!-- -->
			router.push('/');
		}
	}
}

const closeSelectedTag = (view) =&gt; {<!-- -->
	tagsViewStore.delView(view).then(({<!-- --> visitedViews }) =&gt; {<!-- -->
		if (isActive(view)) {<!-- -->
			toLastView(visitedViews, view);
		}
	});
};

const closeOthersTags = (selectedTag) =&gt; {<!-- -->
	router.push(selectedTag);
	tagsViewStore.delOthersVisitedViews(selectedTag);
	moveToCurrentTag();
};

const closeAllTags = (selectedTag) =&gt; {<!-- -->
	tagsViewStore.delAllVisitedViews().then(({<!-- --> visitedViews }) =&gt; {<!-- -->
		if (affixTags.value.some((tag) =&gt; tag.path === view.path)) {<!-- -->
			return;
		}
		toLastView(visitedViews, selectedTag);
	});
};

// function refreshSelectedTag(selectedTag) {<!-- -->
// 	const { fullPath } = selectedTag;
// 	console.log(fullPath);

// 	// location.reload();
// 	router.replace({<!-- -->
// 		path: fullPath,
// 	});
// }

function isActive(r) {<!-- -->
	return r.path === route.path;
}

function activeStyle(tag) {<!-- -->
	if (!isActive(tag)) return {<!-- -->};
	return {<!-- -->
		'background-color': '#F2F3FF',
		color: '#194BFB',
	};
}

function filterAffixTags(routes, basePath = '/') {<!-- -->
	let tags: any = [];
	routes.forEach((route) =&gt; {<!-- -->
		if (route.meta &amp;&amp; route.meta.affix) {<!-- -->
			// const tagPath = path.resolve(basePath, route.path);
			const tagPath = route.path;
			tags.push({<!-- -->
				fullPath: tagPath,
				path: tagPath,
				name: route.name,
				meta: {<!-- --> ...route.meta },
			});
		}
		if (route.children) {<!-- -->
			const tempTags = filterAffixTags(route.children, route.path);
			if (tempTags.length &gt;= 1) {<!-- -->
				tags = [...tags, ...tempTags];
			}
		}
	});
	return tags;
}

function initTags() {<!-- -->
	const affixTags = filterAffixTags(routes.value);

	for (const tag of affixTags) {<!-- -->
		// Must have tag name
		if (tag.name) {<!-- -->
			// this.$store.dispatch('tagsView/addVisitedView', tag);
			useTagsViewStore().addVisitedView(tag);
		}
	}
}

/**
 * @desc: 生命周期
 */

onMounted(() =&gt; {<!-- -->
	initTags();
	addTags();
	scrollInit();
});
&lt;/script&gt;

&lt;style lang="scss" scoped&gt;
.tags-view-container {<!-- -->
	position: relative;
	height: 48px;
	width: 100%;
	background: #fff;
	box-shadow:
		0 1px 3px 0 rgba(0, 0, 0, 0.12),
		0 0 3px 0 rgba(0, 0, 0, 0.04);
	// overflow-x: scroll;
	.tags-view-wrapper {<!-- -->
		.tags-view-item {<!-- -->
			border-radius: 4px;
			display: inline-block;
			position: relative;
			cursor: pointer;
			height: 32px;
			line-height: 32px;
			color: #000;
			background: #f3f3f3;
			padding: 0 12px;
			font-size: 12px;
			margin-left: 8px;
			margin-top: 8px;
			text-decoration: none !important;
			/* 超出滚动的关键，没有它元素会自动缩小，不会滚动 */
			flex-shrink: 0;
			&amp;:first-of-type {<!-- -->
				margin-left: 15px;
			}
			&amp;:last-of-type {<!-- -->
				margin-right: 15px;
			}
		}
		a {<!-- -->
			text-decoration: none;
		}

		.router-link-active {<!-- -->
			text-decoration: none;
		}
	}

	.scroll-pane {<!-- -->
		display: flex;
		/* 设置超出滚动 */
		overflow-x: auto;
	}

	::-webkit-scrollbar {<!-- -->
		/* 隐藏滚动条 */
		display: none;
	}

	.contextmenu {<!-- -->
		margin: 0;
		background: #fff;
		z-index: 3000;
		position: absolute;
		list-style-type: none;
		padding: 5px 0;
		border-radius: 4px;
		font-size: 12px;
		font-weight: 400;
		color: #333;
		box-shadow: 2px 2px 3px 0 rgba(0, 0, 0, 0.3);
		li {<!-- -->
			margin: 0;
			padding: 7px 16px;
			cursor: pointer;
			&amp;:hover {<!-- -->
				background: #eee;
			}
		}
	}
}
&lt;/style&gt;


```

pinna实现全局状态管理 @/store/modules/tagsView.ts

```
import {<!-- --> defineStore } from 'pinia';
import type {<!-- --> RouteRecordRaw } from 'vue-router';

export const useTagsViewStore = defineStore('tags-view', {<!-- -->
	state: () =&gt; ({<!-- -->
		visitedViews: [] as RouteRecordRaw[],
	}),

	actions: {<!-- -->
		addVisitedView(view: RouteRecordRaw) {<!-- -->
			console.log(this);
			if (this.visitedViews.some((v) =&gt; v.path === view.path)) return;
			this.visitedViews.push(
				Object.assign({<!-- -->}, view, {<!-- -->
					title: view.meta.title || 'no-name',
				}),
			);
		},

		delVisitedView(view: RouteRecordRaw) {<!-- -->
			for (const [i, v] of this.visitedViews.entries()) {<!-- -->
				if (v.path === view.path) {<!-- -->
					this.visitedViews.splice(i, 1);
					break;
				}
			}
		},

		delView(view: RouteRecordRaw) {<!-- -->
			return new Promise((resolve) =&gt; {<!-- -->
				this.delVisitedView(view);
				resolve({<!-- -->
					visitedViews: [...this.visitedViews],
				});
			});
		},

		delOthersVisitedViews(view: RouteRecordRaw) {<!-- -->
			this.visitedViews = this.visitedViews.filter((v) =&gt; {<!-- -->
				return v.meta.affix || v.path === view.path;
			});
		},

		delAllVisitedViews() {<!-- -->
			return new Promise((resolve) =&gt; {<!-- -->
				// keep affix tags
				const affixTags = this.visitedViews.filter((tag) =&gt; tag.meta.affix);
				this.visitedViews = affixTags;
				resolve({<!-- -->
					visitedViews: [...this.visitedViews],
				});
			});
		},

		updateVisitedView(view: RouteRecordRaw) {<!-- -->
			for (let v of this.visitedViews) {<!-- -->
				if (v.path === view.path) {<!-- -->
					v = Object.assign(v, view);
					break;
				}
			}
		},
	},
});


```

参考文章：
