
--- 
title:  CRUD——常见场景 
tags: []
categories: [] 

---
## 一、Restful

RestfulCRUD：CRUD满足Rest风格。

URI：/资源名称/资源标识符

HTTP请求方式区分对资源CRUD操作
| |**普通CRUD（uri区分操作）**|**RestfulCRUD**
|查询|getEmp|emp --GET
|添加|addEmp?***|emp--POST
|修改|updateEmp?id=**&amp;xxx=xx|emp/{id} -- PUT
|删除|deleteEmp?id=1|emp/{id}---DELETE

## 二、请求架构
|**实验功能**|**请求URI**|**请求方式**
|查询所有员工|emps|GET
|查询某个员工|emp/{id}|GET
|添加页面|emp|GET
|添加员工|emp|POST
|来到修改页面（查出info信息回写）|emp/{id}|GET
|修改员工|emp|PUT
|删除员工|emp/{id}|DELETE

## 三、put请求

```
&lt;!--发送put请求修改员工数据--&gt;
	&lt;!--
		1、SpringMVC中配置HiddenHttpMethodFilter;（SpringBoot自动配置好的）
		2、页面创建一个post表单
		3、创建一个input项，name="_method";值就是我们指定的请求方式
	--&gt;
```

## 四、标签用法

```
&lt;!-- ##### 增/改 ###### --&gt;
&lt;a class="btn btn-sm btn-success" href="emp" th:href="@{/addEmp}"&gt;员工添加&lt;/a&gt;
&lt;a class="btn btn-sm btn-primary" th:href="@{/emp/}+${emp.id}"&gt;编辑&lt;/a&gt;
&lt;!--隐藏文本框。 if判断 --&gt;
&lt;input type="hidden" name="id" th:if="${emp!=null}" th:value="${emp.id}"&gt;
&lt;!--文本框。 是添加则添加 ， 是修改则查询数据进行  自动填充 --&gt;
&lt;input name="lastName" type="text" class="form-control"  th:value="${emp!=null}?${emp.lastName}"&gt;
&lt;!--单选框。 是添加则添加 ， 是修改则查询数据进行  自动填充 --&gt;
&lt;div class="form-group"&gt;
	&lt;label&gt;Gender&lt;/label&gt;&lt;br/&gt;
	&lt;div class="form-check form-check-inline"&gt;
	   &lt;input class="form-check-input" type="radio" name="gender" value="1" th:checked="${emp!=null}?${emp.gender==1}"&gt;
	   &lt;label class="form-check-label"&gt;男&lt;/label&gt;
	&lt;/div&gt;
	&lt;div class="form-check form-check-inline"&gt;
		&lt;input class="form-check-input" type="radio" name="gender" value="0" th:checked="${emp!=null}?${emp.gender==0}"&gt;
		&lt;label class="form-check-label"&gt;女&lt;/label&gt;
	&lt;/div&gt;
&lt;/div&gt;
&lt;!--下拉框。 --&gt;
&lt;select class="form-control" name="department.id"&gt;
	&lt;option th:selected="${emp!=null}?${dept.id == emp.department.id}" th:value="${dept.id}" th:each="dept:${depIds}" th:text="${dept.departmentName}"&gt;1&lt;/option&gt;
&lt;/select&gt;
&lt;!--日期框 --&gt;
&lt;input name="birth" type="text" class="form-control"  th:value="${emp!=null}?${#dates.format(emp.birth, 'yyyy-MM-dd HH:mm')}"&gt;
&lt;!--button动态显示 --&gt;
&lt;button type="submit" class="btn btn-primary" th:text="${emp!=null}?'修改':'添加'"&gt;添加&lt;/button&gt;
&lt;!--######## 删除 ######## --&gt;
&lt;form id="deleteEmpForm"  method="post"&gt;
	&lt;input type="hidden" name="_method" value="delete"/&gt;
&lt;/form&gt;
&lt;script&gt;
	$(".deleteBtn").click(function(){
		//删除当前员工的
		$("#deleteEmpForm").attr("action",$(this).attr("del_uri")).submit();
		return false;
    });
&lt;/script&gt;

&lt;!--日期格式 --&gt;
spring.mvc.date-format = yyyy-MM-dd
&lt;!--put方式 --&gt;
spring.mvc.hiddenmethod.filter.enabled=true
```

 
