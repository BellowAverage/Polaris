
--- 
title:  easyui漏洞 
tags: []
categories: [] 

---
 - easyui漏洞1：更改easyui-textbox控件是否可用，发现使用$('#ID').textbox(disabled:false);该方法如果true、false来回切换的话，会导致该文本框控件的高度，越来越高。需要使用$(‘#ID').textbox('disable');方式。
 - easyui漏洞2：通过JS为easyui-combobox控件动态加载数据，出现加载完数据后，选择下拉项后，无法在下拉框的位置显示出选择的项。后来才发现，必须在控件的data-options属性中，指定valueField和textField，才可以。否则是无法正确显示选定项的。
 <li> 代码如下： <p>//获取粘贴的内容，兼容IE function getClipboard(event) {
   <!-- -->     if (window.clipboardData) {
   <!-- -->         return (window.clipboardData.getData('Text'));     }else if (event.originalEvent.clipboardData) {
   <!-- -->         return event.originalEvent.clipboardData.getData("text");     }     return ""; } var clickElementID = null; var receiveCode = null; var filteringMode = 0; $(window).on('keydown', function(e){
   <!-- -->     if(e.target.id !&amp;#</p></li>
