
--- 
title:  【腾讯云 Cloud Studio 实战训练营】基于Cloud Studio构建React完成点餐H5页面 
tags: []
categories: [] 

---


####  
- <ul><li><ul><li>- - <ul><li>- - - - - <ul><li>- - - - - - 


<img src="https://img-blog.csdnimg.cn/deb0c3adef8e4046a8593b187cb3feb3.png" alt="在这里插入图片描述">

#### 前言
- 最近也是有机会参与到了腾讯云举办的 `腾讯云 Cloud Studio 实战训练营`，借此了解了 `腾讯云 Cloud Studio` 产品。- 腾讯云 Cloud Studio 的出现是有一定创新性的，使用它进行开发免去了使用一些传统开发工具的成本。- 如下载一个开发工具就要进行基本的开发环境配置，以及下载、安装和占用本地存储等等成本。- 下面就来使用 `腾讯云 Cloud Studio` 做一个实战案例来深入了解该产品的优越性吧！
## 【腾讯云 Cloud Studio 实战训练营】基于Cloud Studio 构建React完成点餐H5页面

### 一、Cloud Studio介绍

#### 1.1 Cloud Studio 是什么

`Cloud Studio` 是 基于浏览器的集成式开发环境（IDE），为开发者提供了一个永不间断的云端工作站。用户在使用 Cloud Studio 时无需安装，随时随地打开浏览器就能在线编程。

Cloud Studio 作为 在线 IDE，包含 代码高亮、自动补全、Git 集成、终端等 IDE 的基础功能，同时支持实时调试、插件扩展等，可以帮助开发者快速完成各种应用的开发、编译与部署工作。

此外，Cloud Studio还支持与其他开发者的协作，可以轻松地共享代码和项目，并进行实时的协同编辑。

目前Cloud Studio 团队基于老用户使用体验角度和新用户上手成本考虑，现实行每月赠送 3000 分钟的工作空间免费时长，所以我们可以来使用送的时长来认真体验下吧！

#### 1.2 相关链接
- Cloud Studio官网地址：- Cloud Studio文档地址：
#### 1.3 登录注册

（1）打开Cloud Studio官网，点击注册：https://www.cloudstudio.net/ <img src="https://img-blog.csdnimg.cn/2242435c0bd746bd990c505e34d9753d.png" alt="在这里插入图片描述">

然后大家按自己的情况选择一种账号进行注册登录就好。 <img src="https://img-blog.csdnimg.cn/b977e087bed14b6cb572758aa398ed81.png" alt="在这里插入图片描述">

注册登录后来到这个页面就算正常啦，可以看到Cloud Studio提供了众多开发环境及模板，下面就来看看到底怎样使用吧！ <img src="https://img-blog.csdnimg.cn/d89364bd9b53412ca40d83e70b6e4d23.png" alt="在这里插入图片描述">

### 二、实战练习

本文打算用云 IDE Cloud Studio 快速搭建，并开发还原一个移动端 React H5 的简版点餐系统页面，从 0 到 1 体验云 IDE 给我们带来的优势，不需要装各种环境，简单易用，开箱即可上手。

#### 2.1 初始化工作空间

来到 Cloud Studio 首页之后，可以看到 Cloud Studio 提供了很多模板（框架模板、云原生模板、建站模板），都是预装环境了，开箱即用的模板，可以快速搭建环境进行代码开发，同时 Cloud Studio 也对所有新老用户每月赠送 3000 分钟的工作空间免费时长。

此时选择创建一个React模板并等待云 IDE 初始化完毕。 <img src="https://img-blog.csdnimg.cn/34f32aa76d1d43daba4b3d3a4feacbf6.png" alt="在这里插入图片描述">

即使从来没有学习过 React，只需要打开对应的 React 框架模板，即可开始初始化一个 React 的工作空间，在等待不到 10s 左右（与带宽网速差异有区别），云 IDE 就已经初始化完毕。 <img src="https://img-blog.csdnimg.cn/116f31eea313435499d69ad0aa5a4476.png" alt="在这里插入图片描述">

等待初始化完毕之后，在我们的右侧，可以看到一个实时预览的预览界面，然后在下面的控制台输入以下指令。

```
// 进入当前目录
cd ./ &amp;&amp; 
// 设置port的环境变量
set port=3000 &amp;&amp;
// 导出port的环境变量
export PORT=3000 &amp;&amp;
// 相当于 yarn install，安装相关依赖
yarn &amp;&amp;
// 启动开发环境
yarn start --port=3000

```

这样我们就完成一个对 React 项目初始化的过程了，用一台新主机，只要有浏览器，就不需要准备任何环境，不需要安装任何软件，只需要能够联网，就能在几分种内初始化完成，这对新技术的学习是非常高效的。

#### 2.2 开发一个简版的点餐系统页面

主旨是为了开发一个 React H5 的页面，为了快速开发，通常会使用到UI组件库，这里我们使用的是 antd-mobile UI库，antd-mobile 是 Ant Design 的移动规范的 React 实现。

##### 1. 安装 antd-mobile

antd-mobile 支持基于 Tree Shaking 的按需加载，大部分的构建工具（例如 webpack 4+ 和 rollup）都支持 Tree Shaking，所以绝大多数情况下你无需做额外的配置即可拥有较小的包体积。

```
yarn add antd-mobile@^5.32.0
 
# 或者
 
npm install --save antd-mobile@^5.32.0

```

在终端输入代码进行安装即可。 <img src="https://img-blog.csdnimg.cn/9762f749e9ec4b118b50a3d6f563c992.png" alt="在这里插入图片描述">

安装完成后在package.json中会有显示。 <img src="https://img-blog.csdnimg.cn/7160385c40c243acadf9a333d446dd43.png" alt="在这里插入图片描述">

##### 2. 安装 less 和 less-loader

平时我们在进行React项目开发的时，可能会使用到Less、Sass进行样式开发，默认 React 是集成Sass的，因此对于习惯书写Less的小伙伴十分不友好，所以我们需要在React项目中配置Less。

```
yarn add -D less@^3.12.2 less-loader@^7.0.1

```

这里注意不带版本安装为高版本，项目会启动失败，所以需要标注好版本后进行安装。

<img src="https://img-blog.csdnimg.cn/5f0643c153374f5daeda3e6e7be2e533.png" alt="在这里插入图片描述"> 这样就安装好了，继续下一步。

##### 3. 暴露 webpack 配置文件

在webpack.config.js中进行配置，这样进行配置需要暴露出React的config配置文件，警告：该操作不可逆

```
npm run eject

```

<img src="https://img-blog.csdnimg.cn/839a6691aea449a69c1ae748f75b1106.png" alt="在这里插入图片描述"> 输入 ‘y’ 后，项目会自动进行解构操作。

完成命令之后，项目根目录会出现一个config文件夹，找到 config/webpack.config.js 文件，按Ctrl + F 查找关键字 “style files” 。

这块是设置 css 相关的代码。 <img src="https://img-blog.csdnimg.cn/a77b0a9b6edc41d7850edfe8b513ac32.png" alt="在这里插入图片描述">

将上图的70行到73行代码改成less，将以下代码复制过去即可。

```
// style files regexes
const cssRegex = /\.css$/;
const cssModuleRegex = /\.module\.css$/;
const sassRegex = /\.(scss|sass)$/;
const sassModuleRegex = /\.module\.(scss|sass)$/;
// 新增加 Less 代码
const lessRegex = /\.(less)$/;
const lessModuleRegex = /\.module\.(less)$/;

```

继续在查找框中输入 “sassRegex” 能够找到以下代码。

<img src="https://img-blog.csdnimg.cn/e68b6f5d6f79401d8e4dadbef7577e78.png" alt="在这里插入图片描述">

这里和前面配置一样，仿照sass的配置，进行less的配置。

```
// less
{<!-- -->
  test: lessRegex,  // 有改动
  exclude: lessModuleRegex,  // 有改动
  use: getStyleLoaders(
    {<!-- -->
      importLoaders: 3,
      sourceMap: isEnvProduction
        ? shouldUseSourceMap
        : isEnvDevelopment,
    },
    'less-loader'  // 有改动
  ),
  sideEffects: true,
},
{<!-- -->
  test: lessModuleRegex,  // 有改动
  use: getStyleLoaders(
    {<!-- -->
      importLoaders: 3,
      sourceMap: isEnvProduction
        ? shouldUseSourceMap
        : isEnvDevelopment,
      modules: {<!-- -->
        getLocalIdent: getCSSModuleLocalIdent,
      },
    },
    'less-loader'  // 有改动
  ),
},

```

<img src="https://img-blog.csdnimg.cn/01423df7b2a04921ab9cfdb9e7127ab8.png" alt="在这里插入图片描述"> 这样就完成了webpack.config.js配置less，可以在项目中使用less样式了。

##### 4. 安装 normalize

Normalize.css 是CSS重置的现代替代方案，可以为默认的HTML元素样式上提供了跨浏览器的高度一致性。相比于传统的CSS reset，Normalize.css是一种现代的、为HTML5准备的优质替代方案。 <img src="https://img-blog.csdnimg.cn/ffe09b5b546b4033ac716d64d34a656a.png" alt="在这里插入图片描述">

##### 5. 上传项目需要的素材

以前上传服务器代码，需要使用 Scp 命令或者装 Remote SSH 插件支持，Cloud Studio 可以很方便默认支持文件上传与下载等常规的操作，与本地 IDE 体验一致：
1. 可以直接拖动文件到 IDE 编辑区域1. 右击 IDE 编辑区域"上传"
直接将 img 文件夹拖动到src目录下即可。

<img src="https://img-blog.csdnimg.cn/acea4ab8353c4a0ab16fac4ede5ff8ba.png" alt="在这里插入图片描述"> img下载方式：

##### 6. 替换App.js主文件

以下是点餐系统的主要业务代码，复制到src/App.js直接替换即可。

```
import './App.css';
import React, {<!-- --> useState } from 'react'
import {<!-- --> NavBar, Toast, Swiper, SideBar, TabBar, Badge } from 'antd-mobile'
import {<!-- -->
  AppOutline,
  ExclamationShieldOutline,
  UnorderedListOutline,
  UserOutline,
} from 'antd-mobile-icons'
import BannerImg from './img/banner.png'
import HotImg from './img/hot.png'
import Food1Img from './img/food1.png'
import Food2Img from './img/food2.png'
import CartImg from './img/cart.png'
import './index.less'
import "normalize.css"
 
function App() {<!-- -->
  const [activeKey, setActiveKey] = useState('1')
 
  const tabbars = [
    {<!-- -->
      key: 'home',
      title: '点餐',
      icon: &lt;AppOutline /&gt;,
    },
    {<!-- -->
      key: 'todo',
      title: '购物车',
      icon: &lt;UnorderedListOutline /&gt;,
      badge: '5',
    },
    {<!-- -->
      key: 'sale',
      title: '餐牌预告',
      icon: &lt;ExclamationShieldOutline /&gt;,
    },
    {<!-- -->
      key: '我的',
      title: '我的',
      icon: &lt;UserOutline /&gt;,
      badge: Badge.dot,
    },
  ]
 
  const back = () =&gt;
    Toast.show({<!-- -->
      content: '欢迎进入点餐系统',
      duration: 1000,
    })
 
 
  const items = ['', '', '', ''].map((color, index) =&gt; (
    &lt;Swiper.Item key={<!-- -->index}&gt;
      &lt;img style={<!-- -->{<!-- -->
        width: '100%'
      }} src={<!-- --> BannerImg }&gt;&lt;/img&gt;
    &lt;/Swiper.Item&gt;
  ))
 
  const tabs =  [
    {<!-- --> key: '1', title: '热销' },
    {<!-- --> key: '2', title: '套餐' },
    {<!-- --> key: '3', title: '米饭' },
    {<!-- --> key: '4', title: '烧菜' },
    {<!-- --> key: '5', title: '汤' },
    {<!-- --> key: '6', title: '主食' },
    {<!-- --> key: '7', title: '饮料' },
  ]
 
  const productName = [
    '小炒黄牛肉',
    '芹菜肉丝炒香干',
    '番茄炒鸡蛋',
    '鸡汤',
    '酸菜鱼',
    '水煮肉片',
    '土豆炒肉片',
    '孜然肉片',
    '宫保鸡丁',
    '麻辣豆腐',
    '香椿炒鸡蛋',
    '豆角炒肉'
  ]
  const productList = productName.map((item, key) =&gt; {<!-- -->
    return {<!-- -->
      name: item,
      img: key % 2 === 1 ? Food1Img : Food2Img
    }
  })
 
  return (
    &lt;div className="App"&gt;
      &lt;NavBar onBack={<!-- -->back} style={<!-- -->{<!-- -->
        background: '#F0F0F0',
        fontWeight: 'bold'
      }}&gt;点餐&lt;/NavBar&gt;
 
      &lt;div className='head-card'&gt;
        &lt;Swiper
          style={<!-- -->{<!-- -->
            '--border-radius': '8px',
          }}
          autoplay
          defaultIndex={<!-- -->1}
        &gt;
          {<!-- -->items}
        &lt;/Swiper&gt;
      &lt;/div&gt;
 
      &lt;div className='product-box'&gt;
        &lt;SideBar activeKey={<!-- -->activeKey} onChange={<!-- -->setActiveKey}&gt;
          {<!-- -->tabs.map(item =&gt; (
            &lt;SideBar.Item key={<!-- -->item.key} title={<!-- -->
              item.key === '1' ? &lt;div&gt;
              &lt;div className='flex-center'&gt;
                &lt;img style={<!-- -->{<!-- -->
                  display: 'block',
                  width: '16px',
                  marginRight: '5px'
                }} src={<!-- --> HotImg }&gt;&lt;/img&gt;
                &lt;div&gt;{<!-- --> item.title }&lt;/div&gt;
              &lt;/div&gt;
            &lt;/div&gt; : item.title
            } /&gt;
          ))}
        &lt;/SideBar&gt;
        &lt;div className='product-right'&gt;
          &lt;div className='product-title'&gt;热销&lt;/div&gt;
          &lt;div className='product-list'&gt;
            {<!-- -->
              productList.map((item, key) =&gt; {<!-- -->
                return (
                  &lt;div className='product-item'&gt;
                    &lt;div className='product-item-left'&gt;
                      &lt;img style={<!-- -->{<!-- -->
                        display: 'block',
                        width: '76px',
                        marginRight: '5px'
                      }} src={<!-- --> item.img }&gt;&lt;/img&gt;
                      &lt;div className='product-item-left-info'&gt;
                        &lt;div&gt;
                          &lt;div className='product-item-left-info-name'&gt;{<!-- --> item.name }&lt;/div&gt;
                          &lt;div className='product-item-left-info-number'&gt;月售{<!-- -->key + 1}0 赞{<!-- -->key * 5}&lt;/div&gt;
                        &lt;/div&gt;
                        &lt;div className='product-item-left-info-price'&gt;¥10&lt;/div&gt;
                      &lt;/div&gt;
                    &lt;/div&gt;
                    &lt;div className="cart"&gt;
                      &lt;img style={<!-- -->{<!-- -->
                        display: 'block',
                        width: '30px',
                        marginRight: '5px'
                      }} src={<!-- --> CartImg } onClick = {<!-- --> () =&gt;
                        Toast.show({<!-- -->
                          content: '添加购物车成功'
                        }) }&gt;&lt;/img&gt;
                    &lt;/div&gt;
                  &lt;/div&gt;
                )
              })
            }
          &lt;/div&gt;
        &lt;/div&gt;
      &lt;/div&gt;
 
      &lt;TabBar&gt;
        {<!-- -->tabbars.map(item =&gt; (
          &lt;TabBar.Item
            key={<!-- -->item.key}
            icon={<!-- -->item.icon}
            title={<!-- -->item.title}
            badge={<!-- -->item.badge}
          /&gt;
        ))}
      &lt;/TabBar&gt;
    &lt;/div&gt;
  );
}
 
export default App;


```

然后在 src 目录下，创建一个 index.less 文件，将以下 less 相关的代码复制到该文件中即可。 <img src="https://img-blog.csdnimg.cn/6d9b942ab9804f38ac3c624ce25e4f63.png" alt="在这里插入图片描述">

```
.head-card {<!-- -->
  padding: 10px 20px;
  box-sizing: border-box;
}
 
.flex-center {<!-- -->
  display: flex;
  align-items: center;
}
 
.product-box {<!-- -->
  display: flex;
  align-items: center;
  width: 100%;
  height: calc(100vh - 45px - 130px - 50px);
}
 
.product-right {<!-- -->
  flex: 1;
  height: 100%;
}
 
.product-title {<!-- -->
  font-family: PingFangSC-Regular;
  font-size: 14px;
  color: #000000;
  text-align: left;
  padding-bottom: 10px;
}
 
.product-list {<!-- -->
  height: calc(100% - 24px);
  overflow-y: auto;
}
 
.product-item {<!-- -->
  position: relative;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-left: 10px;
  box-sizing: border-box;
  margin-bottom: 10px;
  &amp;-left {<!-- -->
    display: flex;
    &amp;-info {<!-- -->
      padding-left: 3px;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      &amp;-name {<!-- -->
        font-family: PingFangSC-Regular;
        font-size: 14px;
        color: #000000;
        text-align: left;
      }
      &amp;-number {<!-- -->
        padding-top: 3px;
        font-family: PingFangSC-Regular;
        font-size: 11px;
        color: #787878;
        text-align: left;
      }
      &amp;-price {<!-- -->
        font-family: PingFangSC-Regular;
        font-size: 18px;
        color: #FF1800;
        text-align: left;
      }
    }
  }
}
 
.cart {<!-- -->
  position: absolute;
  right: 10px;
  bottom: 0;
}

```

##### 7.启动项目

完成上述操作后，在控制台中输入 `yarn start` 即可启动该项目。 <img src="https://img-blog.csdnimg.cn/7332bdeab1524d74aae5b276d29fe5fc.png" alt="在这里插入图片描述">

Cloud Studio 内置预览插件，可以实时显示网页应用，当代码发生改变之后，预览窗口会自动刷新，即可在 Cloud Studio 内实时开发调试网页了

复制内置 Chrome 浏览器窗口的地址栏，分享给团队的其它成员，免去了部署 nginx 的繁琐配置。 <img src="https://img-blog.csdnimg.cn/ba63cbe9d3984219bf4a2d72f1efc503.png" alt="在这里插入图片描述"> 这样我们的项目就算完成了，只需要安装几个库就可以快速的构建一个项目。

### 三、发布到仓库

项目完成后可以快速发布到git仓库中，首先需要填写README.md文件。

```
# 项目说明

这是一个用 IDE [Cloud Studio](https://www.cloudstudio.net/?utm=csdn) 快速搭建，并开发还原一个移动端 React H5 的简版点餐系统页面，从 0 到 1 体验云 IDE 给我们带来的优势，不需要装各种环境，简单易用，开箱即可上手。

## 相关技术栈

React + less + webpack

## 项目运行

yarn install
yarn start

```

在左边功能菜单区找到“源代码管理”，使用 `git init` 进行仓库初始化。 <img src="https://img-blog.csdnimg.cn/e8f13659d65d43cdbf0a470c33a82b71.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/7b336cd4878f4181937ad6a3a639f9eb.png" alt="在这里插入图片描述">

然后输入需要提交的message信息，再点击"Commit"进行仓库提交。 <img src="https://img-blog.csdnimg.cn/c261a4aeefc843308e7659b0a413f583.png" alt="在这里插入图片描述">

如果提示没有关联账号的话就去设置里面关联一下即可。 <img src="https://img-blog.csdnimg.cn/9628d094e88446ce94e54847aa1699c6.png" alt="在这里插入图片描述">

如果登录时使用的是coding,所以就直接推送到coding仓库了，当然也可以推送到github，需要绑定对应的账号进行提交即可。

这里可以登陆到 Coding 平台进行查看仓库代码。 <img src="https://img-blog.csdnimg.cn/c7ddd487b70645e1a397e3a27694e1fa.png" alt="在这里插入图片描述">

### 四、开发空间管理

在我们的控制台这里可以管理所有使用的工作空间，其中右侧的按钮可以进行升级配置、设置、删除、开始\停止操作。 <img src="https://img-blog.csdnimg.cn/1b591a57f0ed4364aef8bf2c73920169.png" alt="在这里插入图片描述">

## 总结

在使用过Cloud Studio做一次实战练习之后，让我对Cloud Studio有了更深刻的认识，下面来简单谈一下Cloud Studio的优势以及优化建议。

**Cloud Studio的优势**很明显，大致可以分为一下几点。
1. **节约开发成本**。可以帮助用户减少安装 IDE 的成本，提供在线代码开发、编译、运行、存储的一站式服务。1. **便捷性**。Cloud Studio 是基于浏览器的集成式开发环境（IDE），为开发者提供了一个永不间断的云端工作站。用户在使用 Cloud Studio 时无需安装，随时随地打开浏览器就能在线编程。1. **云端开发**。Cloud Studio 不需要任何本地安装，只需使用支持的浏览器，即可轻松登录并开始编码开发，实现 Coding everywhere。同时加速开发流程配置化，用配置定义云端开发环境，提升开发效率，拥有更弹性的云上开发资源。1. **多种预制环境可选**。内置 Node.js、Java、Python 等常见环境，直接进入开发状态。1. metawork 开发协作。通过代码协作，多光标高亮显示和跟随，让协作变的清晰有序。包括但不限于代码协同、多光标协作、实时预览、终端协作。1. **众多模板可用**。在使用时一个很明显的感受就是Cloud Studio提供了众多的模板，有些功能我们可以从模板库中直接拿出来改一下就可以满足自己的需求快速使用，甚至于不会写代码的人都可以上去操作两手。
**Cloud Studio优化建议**
1. **文档全面详细化**。希望增加更多编程语言的文档介绍，目前文档里面只有几个主流的编程语言操作文档，对于一些刚开始使用Cloud Studio的用户来说，能够看到自己平时使用的编程语言的详细文档可以更快的上手Cloud Studio。1. **提供更多的编程语言和框架**。当前网站支持的编程语言和框架不能够满足所有用户的需求。可以考虑支持更多的编程语言和框架，提高平台的适用性和可扩展性。1. **提供更高的稳定性**。目前网站的性能和稳定性还有进一步提升的空间，有时候可能会出现一些卡顿和崩溃等问题。为了提高用户的使用体验，建议考虑优化平台的性能和稳定性。