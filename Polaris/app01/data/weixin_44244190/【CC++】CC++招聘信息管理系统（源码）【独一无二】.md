
--- 
title:  【C/C++】C/C++招聘信息管理系统（源码）【独一无二】 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>C/C++招聘信息管理系统（源码）【独一无二】</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - - - <ul><li>- - - - - - -  
   </li>- </ul> 
  
  


## 一、功能描述

C++/C实现的招聘信息管理系统，主要功能包括录入招聘信息、浏览招聘信息、查询单位用人数、统计某职位有多少招聘单位、修改学历和薪资、薪资升序排列以及删除招聘单位信息。详细解释每个模块的功能：
<li> **头文件包含和结构体定义：** 
  1. 包含了 `&lt;stdio.h&gt;` 和 `&lt;string.h&gt;` 头文件，分别用于输入输出和字符串处理。1. 定义了一个结构体 `JobInfo`，用来表示招聘信息，包括招聘单位、职位、学历要求、招聘人数和薪资。 </li><li> **全局变量和结构体数组初始化：** 
  1. 定义了一个结构体数组 `jobs` 用来存储招聘信息。1. 定义了一个全局变量 `jobCount` 来记录已录入的招聘信息数量。 </li><li> **录入招聘信息函数 (`inputJob`)：** 
  1. 提供了一个交互式界面，允许用户输入招聘信息，并将其存储到 `jobs` 数组中。 </li>- 定义了一个结构体数组 `jobs` 用来存储招聘信息。- 定义了一个全局变量 `jobCount` 来记录已录入的招聘信息数量。
>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 招聘信息管理 ” 获取。👈👈👈 

<li> **浏览招聘信息函数 (`listJobs`)：** 
  1. 循环遍历 `jobs` 数组，将每条招聘信息输出到屏幕上。 </li><li> **查询单位用人数函数 (`queryTotalCount`)：** 
  1. 统计指定单位需要的总人数，通过输入单位名称，在所有招聘信息中查找单位名称匹配的记录，然后将其招聘人数累加返回。 </li><li> **统计某职位有多少招聘单位函数 (`statsPositions`)：** 
  1. 统计指定职位有多少个招聘单位，通过输入职位名称，在所有招聘信息中查找职位名称匹配的记录，然后计数并输出结果。 </li><li> **修改招聘信息函数 (`modifyJob`)：** 
  1. 允许用户输入招聘单位名称，然后修改该单位的学历要求和薪资。 </li><li> **薪资升序排列函数 (`sortJobsBySalary`)：** 
  1. 将招聘信息按照薪资升序排列，采用冒泡排序算法实现。 </li><li> **删除招聘单位信息函数 (`deleteJob`)：** 
  1. 允许用户输入要删除的招聘单位名称，然后删除该单位的招聘信息。 </li>1.  **主函数 (`main`)：** - 统计指定单位需要的总人数，通过输入单位名称，在所有招聘信息中查找单位名称匹配的记录，然后将其招聘人数累加返回。- 允许用户输入招聘单位名称，然后修改该单位的学历要求和薪资。- 允许用户输入要删除的招聘单位名称，然后删除该单位的招聘信息。- 提供了一个循环菜单，允许用户选择不同的操作。- 调用相应的函数来执行用户选择的操作，直到用户选择退出。
程序实现了一个简单的招聘信息管理系统，用户可以通过菜单选择不同的功能来管理招聘信息，包括录入、浏览、查询、统计、修改、排序和删除。

>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 招聘信息管理 ” 获取。👈👈👈 


## 二、功能展示

### 2.1. 录入招聘信息

<img src="https://img-blog.csdnimg.cn/direct/e878f7185dd84bc7838d5a826a3131ae.png" alt="在这里插入图片描述">

### 2.2. 浏览招聘信息

<img src="https://img-blog.csdnimg.cn/direct/d30e86a6c66e4bf5bc8e9db00a5a3c97.png" alt="在这里插入图片描述">

>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 招聘信息管理 ” 获取。👈👈👈 


### 2.3. 查看单位用人数

<img src="https://img-blog.csdnimg.cn/direct/1b607dbf5059436ebec7a507cb7dda05.png" alt="在这里插入图片描述">

### 2.4.统计职位招聘单位

<img src="https://img-blog.csdnimg.cn/direct/b2f72b118a0f46e9949e0a436fea14ea.png" alt="在这里插入图片描述">

### 2.5.修改学历和薪资

<img src="https://img-blog.csdnimg.cn/direct/123ae7e30eac47dd8e864b88c5367356.png" alt="在这里插入图片描述">

>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 招聘信息管理 ” 获取。👈👈👈 


### 2.6.薪资升序排列

<img src="https://img-blog.csdnimg.cn/direct/94575212a11a48fbaecdf60435b1c042.png" alt="在这里插入图片描述">

### 2.7.退出

<img src="https://img-blog.csdnimg.cn/direct/27beda466b704ff9bdf564818b47022b.png" alt="在这里插入图片描述">

### 2.8.删除招聘单位信息

>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 招聘信息管理 ” 获取。👈👈👈 


<img src="https://img-blog.csdnimg.cn/direct/569b7c11d4c147c491535ce4a14dd305.png" alt="在这里插入图片描述">

## 三、代码示例

```
#include&lt;stdio.h&gt;
#include&lt;string.h&gt;
//定义结构体
struct Joblnfo{<!-- -->
	char unit[50];
	char position[50];
	char education[20];
	int count;
	int salary;
};

//定义结构体数组并初始化
#define MAX_JOBS 100
#define MAX_UNIT_LEN 50
#define MAX_POSITION_LEN 50
#define MAX_SALARY_LEN 4000
Joblnfo jobs[MAX_JOBS];
int jobCount=0;


//录入招聘信息函数
void inputJob(){<!-- -->
	Joblnfo newJob;
	printf("招聘单位：");
	scanf("%49s",newJob.unit);
	printf("职位：");
	scanf("%49s",newJob.position);
	printf("学历：");
	scanf("%19s",newJob.education);
	printf("招聘人数：");
	scanf("%d",&amp;newJob.count);
	printf("薪资：");
	scanf("%d",&amp;newJob.salary);
	jobs[jobCount++]=newJob;
}

// 略 .....................
// 略 .....................
&gt;👉👉👉源码关注【测试开发自动化】公众号，回复 “ 招聘信息管理 ” 获取。👈👈👈


//主函数
int main(){<!-- -->
	int choice;
	int jobCount=0;
	//循环菜单
	do{<!-- -->
		printf("=====招聘信息管理系统=====\n");
		printf("1.录入招聘信息\n");
		printf("2.浏览招聘信息\n");
		printf("3.查看单位用人数\n");
		printf("4.统计某职位有多少招聘单位\n");
		printf("5.修改学历和薪资\n");
		printf("6.薪资升序排列\n");
		printf("7.退出\n");
		printf("0.删除招聘单位信息\n");
		printf("==========================\n");
		scanf("%d",&amp;choice);
	switch(choice){<!-- -->
	case 0:
		deleteJob();
		break;
	case 1:
		inputJob();
		break;
	case 2:
		listJobs();
		break;
	case 3:
		{<!-- -->
		char unit[MAX_UNIT_LEN];
		printf("输入要查询的招聘单位:");
		scanf("%s",unit);
		int total=queryTotalCount(unit);
		printf("招聘单位%s需要的总人数:%d\n",unit,total);
		}
		break;
	case 4:
		{<!-- -->
			char position[MAX_POSITION_LEN];
			printf("输入要统计的职位");
			scanf("%s",position);
			statsPositions(position);
		}
		break;

	case 5:
		{<!-- -->
			char unit[MAX_UNIT_LEN];
			printf("输入需要修改的招聘单位");
			scanf("%s",unit);
			modifyJob(unit);
		}
		break;
	case 6:
		sortJobsBySalary();
		listJobs();
		break;
	case 7:
		printf("感谢使用,谢谢");
		return 0;
	default:
		printf("输入无效,请重新输入\n");
	}
	while(getchar()!='\n');

	}
	while(choice!=7);
	return 0;
}


```

>  
 👉👉👉源码关注【测试开发自动化】公众号，回复 “ 招聘信息管理 ” 获取。👈👈👈 

