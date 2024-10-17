
--- 
title:  js文章分页 
tags: []
categories: [] 

---
```
可以设定每页的字数

&lt;%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%&gt;
&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"&gt;
&lt;html&gt;
&lt;head&gt;
&lt;title&gt;文章分页&lt;/title&gt;
&lt;meta http-equiv="content-type" content="text/html; charset=UTF-8" /&gt;
&lt;style&gt;
* {
    font-size: 10.2pt;
    font-family: tahoma;
    line-height: 150%;
}

.divContent {
    width: 770px;
    word-break: break-all;
    margin: 10px 0px 10px;
    padding: 10px;
}
&lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;


    &lt;div id="divContent"&gt;&lt;/div&gt;
    &lt;div id="divPagenation"&gt;&lt;/div&gt;
    &lt;div id="Content" style="display: none;"&gt;
    请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦请问瑞哦亲为儿童与i哦亲为儿童与i哦
    &lt;/div&gt;
    &lt;SCRIPT LANGUAGE="JavaScript"&gt;
function DHTMLpagenation(content) {<!-- -->
    // client static html file pagenation
    this.content=content;
    this.contentLength=content.length;
    this.pageSizeCount;
    this.perpageLength=100; //default perpage byte length.
    this.currentPage=1;
    //this.regularExp=/.+[\?\&amp;]{1}page=(\d+)/;
    this.regularExp=/\d+/;
    this.divDisplayContent;
    this.contentStyle=null;
    this.strDisplayContent="";
    this.divDisplayPagenation;
    this.strDisplayPagenation="";

    arguments.length==2?perpageLength=arguments[1]:'';
    try {
        divExecuteTime=document.createElement("DIV");
        document.body.appendChild(divExecuteTime);
    }
    catch(e)
    {
    }
    if(document.getElementById("divContent"))
    {
        divDisplayContent=document.getElementById("divContent");
    }
    else
    {
        try
        {
            divDisplayContent=document.createElement("DIV");
            divDisplayContent.id="divContent";
            document.body.appendChild(divDisplayContent);
        }
        catch(e)
        {
            return false;
        }
    }
    if(document.getElementById("divPagenation"))
    {
        divDisplayPagenation=document.getElementById("divPagenation");
    }
    else
    {
        try
        {
            divDisplayPagenation=document.createElement("DIV");
            divDisplayPagenation.id="divPagenation";
            document.body.appendChild(divDisplayPagenation);
        }
        catch(e)
        {
            return false;
        }
    }
    DHTMLpagenation.initialize();
    return this;

};
DHTMLpagenation.initialize=function()
{<!-- -->
    divDisplayContent.className=contentStyle!=null?contentStyle:"divContent";
    if(contentLength&lt;=perpageLength)
    {
        strDisplayContent=content;
        divDisplayContent.innerHTML=strDisplayContent;
        return null;
    }
    pageSizeCount=Math.ceil((contentLength/perpageLength));
    DHTMLpagenation.goto(currentPage);
    DHTMLpagenation.displayContent();
};
DHTMLpagenation.displayPage=function()
{<!-- -->
    strDisplayPagenation="分页：";
    if(currentPage&amp;&amp;currentPage!=1)
        strDisplayPagenation+='&lt;a href="javascript:void(0)" onclick="DHTMLpagenation.previous()"&gt;上一页

&lt;/a&gt;&amp;nbsp;&amp;nbsp;';
    else
        strDisplayPagenation+="上一页&amp;nbsp;&amp;nbsp;";
    for(var i=1;i&lt;=pageSizeCount;i++)
    {
        if(i!=currentPage)
            strDisplayPagenation+='&lt;a href="javascript:void(0)" onclick="DHTMLpagenation.goto('+i+');"&gt;'+i

+'&lt;/a&gt;&amp;nbsp;&amp;nbsp;';
        else
            strDisplayPagenation+=i+"&amp;nbsp;&amp;nbsp;";
    }
    if(currentPage&amp;&amp;currentPage!=pageSizeCount)
        strDisplayPagenation+='&lt;a href="javascript:void(0)" onclick="DHTMLpagenation.next()"&gt;下一页

&lt;/a&gt;&amp;nbsp;&amp;nbsp;';
    else
        strDisplayPagenation+="下一页&amp;nbsp;&amp;nbsp;";
    //strDisplayPagenation+="共 " + pageSizeCount + " 页，每页" + perpageLength + " 字符，调整字符数：

&lt;input type='text' value='"+perpageLength+"' id='ctlPerpageLength'&gt;&lt;input type='button' value='确定' 

onclick='DHTMLpagenation.change(document.getElementById(\"ctlPerpageLength\").value);'&gt;";
    divDisplayPagenation.innerHTML=strDisplayPagenation;
};
DHTMLpagenation.previous=function()
{
    DHTMLpagenation.goto(currentPage-1);
};
DHTMLpagenation.next=function()
{
    DHTMLpagenation.goto(currentPage+1);
};
DHTMLpagenation.goto=function(iCurrentPage)
{
    startime=new Date();
    if(regularExp.test(iCurrentPage))
    {
        currentPage=iCurrentPage;
        strDisplayContent=content.substr((currentPage-1)*perpageLength,perpageLength);
    }
    else
    {
        alert("page parameter error!");
    }
    DHTMLpagenation.displayPage();
    DHTMLpagenation.displayContent();
};
DHTMLpagenation.displayContent=function()
{
    divDisplayContent.innerHTML=strDisplayContent;
};
DHTMLpagenation.change=function(iPerpageLength)
{
    if(regularExp.test(iPerpageLength))
    {
        DHTMLpagenation.perpageLength=iPerpageLength;
        DHTMLpagenation.currentPage=1;
        DHTMLpagenation.initialize();
    }
    else
    {
        alert("请输入数字");
    }
};
DHTMLpagenation(document.getElementById('Content').innerHTML,200);
&lt;/SCRIPT&gt;
&lt;/body&gt;
&lt;/html&gt;

```
