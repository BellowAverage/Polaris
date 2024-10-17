
--- 
title:  spring boot 整合 activiti 6.0 
tags: []
categories: [] 

---
### 一、为什么选择Activiti（本人已经转为使用eclipse,idea的bpmn工具不好用）

<img src="https://upload-images.jianshu.io/upload_images/10135025-b08608ac33db9d64.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/911/format/webp" alt="在这里插入图片描述">

### 二、核心7大接口、28张表

<img src="https://upload-images.jianshu.io/upload_images/10135025-1d64ec0a318b207d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp" alt="在这里插入图片描述">

### 7大接口(service)
1. RepositoryService：提供一系列管理流程部署和流程定义的API。1. RuntimeService：在流程运行时对流程实例进行管理与控制。1. TaskService：对流程任务进行管理，例如任务提醒、任务完成和创建任务等。1. IdentityService：提供对流程角色数据进行管理的API，这些角色数据包括用户组、用户及它们之间的关系。1. ManagementService：提供对流程引擎进行管理和维护的服务。1. HistoryService：对流程的历史数据进行操作，包括查询、删除这些历史数据。1. FormService：表单服务。
### (二）28张表

<img src="https://upload-images.jianshu.io/upload_images/10135025-f74cc14c93ec3e9a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/505/format/webp" alt="在这里插入图片描述">
1. act_ge_ 通用数据表，ge是general的缩写1. act_hi_ 历史数据表，hi是history的缩写，对应HistoryService接口1. act_id_ 身份数据表，id是identity的缩写，对应IdentityService接口1. act_re_ 流程存储表，re是repository的缩写，对应RepositoryService接口，存储流程部署和流程定义等静态数据1. act_ru_ 运行时数据表，ru是runtime的缩写，对应RuntimeService接口和TaskService接口，存储流程实例和用户任务等动态数据
### 三、Spring Boot2.0与Activiti 6.0整合
<li> 在POM文件中添加依赖 <pre><code>&lt;dependency&gt;
    &lt;groupId&gt;org.activiti&lt;/groupId&gt;
    &lt;artifactId&gt;activiti-spring-boot-starter-basic&lt;/artifactId&gt;
    &lt;version&gt;6.0.0&lt;/version&gt;
&lt;/dependency&gt;
</code></pre> </li>1.  @SpringBootApplication(exclude = SecurityAutoConfiguration.class)//排除类 1.   1.  创建cs.bpmn文件到项目文件夹/resources/processes下，设置流程： <img src="https://img-blog.csdnimg.cn/20181122194956804.png" alt="在这里插入图片描述"> 1.  修改cs.bpmn为xml,点击选中cs.xml文件（乱码的话自行解决）右键，如下图： <img src="https://img-blog.csdnimg.cn/20181122195618189.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2018112219582496.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE3NjczMTk=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <li> application.yml文件添加配置项 <pre><code>spring:
	activiti:
	    check-process-definitions: false
</code></pre> </li>1.  启动应用，会在数据库里创建28张表 <li> 完成以上步骤，就可以在程序中使用自动注入的方式，使用Activiti的7大接口。 <pre><code>@Autowired
private RuntimeService runtimeService;

@Autowired
private TaskService taskService;

@Autowired
private IdentityService identityService;

@Autowired
private RepositoryService repositoryService;

@Autowired
private ProcessEngine processEngine;

@Autowired
private HistoryService historyService;
</code></pre> </li><li> 部署工作流（流程定义和部署对象相关的service） <pre><code>    @Test
    public void dybs() {
        Deployment deployment = repositoryService//流程定义和部署对象相关的service
                .createDeployment()//创建一个部署对象
                .name("helloWorld")//创建一个部署对象
                .addClasspathResource("processes/qjsp.bpmn")// 加载文件
                .addClasspathResource("processes/qjsp.png")// 加载文件
                .deploy();//完成部署
        System.out.println("部署id"+deployment.getId());
        System.out.println("部署名称"+deployment.getName());
    }
</code></pre> </li><li> 启动工作流 <pre><code>@Test
public void qdlc() {
	ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("qjlc");
	System.out.println("流程实例id：" + processInstance.getId());
	System.out.println("流程定义id：" + processInstance.getProcessDefinitionId());
}
</code></pre> </li><li> 查询当前人的任务 <pre><code>public void grrw() {
String assignee = "李四";
List&lt;Task&gt; res = taskService.createTaskQuery().taskAssignee(assignee).list();
	if (res.size() &gt; 0 &amp;&amp; res != null) {
		for (Task t : res) {
		System.out.println("任务id：" + t.getId());
		System.out.println("任务名称：" + t.getName());
		System.out.println("任务的创建时间：" + t.getCreateTime());
		System.out.println("任务的办理人：" + t.getAssignee());
		System.out.println("流程实例的id：" + t.getProcessInstanceId());
		System.out.println("执行对象id：" + t.getExecutionId());
		System.out.println("执行对象id：" + t.getProcessDefinitionId());
		System.out.println("####################################");
		}
	}
}
</code></pre> </li><li> 完成任务 <pre><code>@Test
	public void wcrw() {
		String taskId = "7502";
		taskService.complete(taskId);
		System.out.println("完成任务-任务id："+taskId);
	}
</code></pre> </li>
### 第二种集成方式

```
&lt;dependency&gt;
    &lt;groupId&gt;org.activiti&lt;/groupId&gt;
    &lt;artifactId&gt;activiti-spring&lt;/artifactId&gt;
    &lt;version&gt;6.0.0&lt;/version&gt;
&lt;/dependency&gt;  

```

**ActivitiConfig.java配置**

```
package com.ljq.rxrs.config;


import java.io.IOException;

import javax.sql.DataSource;

import org.activiti.engine.HistoryService;
import org.activiti.engine.IdentityService;
import org.activiti.engine.ManagementService;
import org.activiti.engine.ProcessEngine;
import org.activiti.engine.RepositoryService;
import org.activiti.engine.RuntimeService;
import org.activiti.engine.TaskService;
import org.activiti.spring.SpringProcessEngineConfiguration;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;
import org.springframework.jdbc.datasource.DataSourceTransactionManager;

@Configuration
public class ActivitiConfig {

	@Bean
    public ProcessEngine processEngine(DataSourceTransactionManager transactionManager, DataSource dataSource) throws IOException {
        SpringProcessEngineConfiguration configuration = new SpringProcessEngineConfiguration();
        //自动部署已有的流程文件
        Resource[] resources = new PathMatchingResourcePatternResolver().getResources(ResourceLoader.CLASSPATH_URL_PREFIX + "processes/*.bpmn");
        configuration.setTransactionManager(transactionManager);
        configuration.setDataSource(dataSource);
        configuration.setDatabaseSchemaUpdate("true");
        configuration.setDeploymentResources(resources);
        configuration.setDbIdentityUsed(false);
        return configuration.buildProcessEngine();
    }
 
    @Bean
    public RepositoryService repositoryService(ProcessEngine processEngine) {
        return processEngine.getRepositoryService();
    }
 
    @Bean
    public RuntimeService runtimeService(ProcessEngine processEngine) {
        return processEngine.getRuntimeService();
    }
 
    @Bean
    public TaskService taskService(ProcessEngine processEngine) {
        return processEngine.getTaskService();
    }
 
    @Bean
    public HistoryService historyService(ProcessEngine processEngine) {
        return processEngine.getHistoryService();
    }
 
    @Bean
    public ManagementService managementService(ProcessEngine processEngine) {
        return processEngine.getManagementService();
    }
 
    @Bean
    public IdentityService identityService(ProcessEngine processEngine) {
        return processEngine.getIdentityService();
    }

}


```
