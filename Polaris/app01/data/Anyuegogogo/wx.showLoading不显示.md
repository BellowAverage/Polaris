
--- 
title:  wx.showLoading不显示 
tags: []
categories: [] 

---
可能影响到的原因： 1、如果页面中用了wx.showLoading但没显示，可能页面中有请求，请求的封装中用了wx.showLoading，然后wx.showLoading又是全局的，请求如果太快，loading还没来得及展示就被关闭了。可以尝试把所有请求的load关闭，看页面中使用的wx.showLoading是否显示。 2、wx.showLoading 和 wx.showToast 同时只能显示一个。这两个是否有同时使用。
