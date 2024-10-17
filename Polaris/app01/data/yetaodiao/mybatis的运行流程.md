
--- 
title:  mybatis的运行流程 
tags: []
categories: [] 

---
MyBatis的运行流程分为三大阶段：

 1. **初始化阶段**：读取 XML 配置文件和注解中的配置信息，创建配置对象，并完成各个模块的初始化的工作；
 1. **代理封装阶段**：封装 iBatis 的编程模型，使用 mapper 接口开发的初始化工作；
 1. **数据访问阶段**：通过 SqlSession 完成 SQL 的解析，参数的映射、SQL 的执行、结果的解析过程；

为了熟悉Mybatis的运行流程，我们先看一段代码

`public class MybatisDemo { ​ private SqlSessionFactory sqlSessionFactory; @Before public void init() throws IOException { //--------------------第一步：加载配置---------------------------   // 1.读取mybatis配置文件创SqlSessionFactory String resource = "mybatis-config.xml"; InputStream inputStream = Resources.getResourceAsStream(resource); // 1.读取mybatis配置文件创SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream); inputStream.close(); } @Test // 快速入门 public void quickStart() throws IOException { //--------------------第二部，创建代理对象------------------`
