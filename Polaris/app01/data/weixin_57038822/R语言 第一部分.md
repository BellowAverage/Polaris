
--- 
title:  R语言 第一部分 
tags: []
categories: [] 

---
****R语言 第一章****

1.对象赋值与运行

<img src="https://img-blog.csdnimg.cn/13d14cb4aef74cf0857831aac1238ed2.png" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/3fbec4b8f3994563b9cb2be3299e9462.png" alt="请添加图片描述">

2.脚本代码

<img src="https://img-blog.csdnimg.cn/a294c0102842442180d3e0031bca548f.png" alt="请添加图片描述">

3.帮助文件 <img src="https://img-blog.csdnimg.cn/caa57dc5ed2b4441b3872ea76aa93bb2.png" alt="请添加图片描述"> 4.向量，矩阵和数组 （1）向量 <img src="https://img-blog.csdnimg.cn/df98148dadb64ef5990ebcf191431f8c.png" alt="请添加图片描述"> （2）矩阵 <img src="https://img-blog.csdnimg.cn/f733efd8f8424634ac40bce71cfb1747.png" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/ee41d27ce3c84494b06f049d55e18db0.png" alt="请添加图片描述"> (3).数组

<img src="https://img-blog.csdnimg.cn/d80580b9f82b450eb491973fff7fc044.png" alt="请添加图片描述"> 5.数据框 1）创建数据框

<img src="https://img-blog.csdnimg.cn/27305670244045adb8d288c17266e107.png" alt="请添加图片描述">

<img src="https://img-blog.csdnimg.cn/3aae8d5c86ce471288dafb29ec9f29e0.png" alt="请添加图片描述">

2）数据框的合并

>  
 mytable&lt;-rbind(table1_1,table1_2) cbind(mytable,table1_3[2:3]) # 按列合并数据框 


3）数据框排序 <img src="https://img-blog.csdnimg.cn/78b5f8ef17d849ad998ff8d695c25b3d.png" alt="请添加图片描述"> 6.因子和列表

1)因子 <img src="https://img-blog.csdnimg.cn/78f4335ea22d4fef8e2ab557ca00b013.png" alt="请添加图片描述"> 2）列表 <img src="https://img-blog.csdnimg.cn/ac293d40635d4064b82589c9e09cc65f.png" alt="请添加图片描述"> 7.R语言数据处理

1）数据读取和保存

>  
 1.读取包含标题的csv格式数据 table1_1&lt;-read.csv(“C:/mydata/chap01/table1_1.csv”) 2. 读取不包含标题的csv格式数据 3. table1_1&lt;-read.csv(“C:/mydata/chap01/table1_1.csv”,header=FALSE) 3.读取R格式数据 load(“C:/mydata/chap01/table1_1.RData”) 4.将tablel_1存为csv格式文件 write.csv(table1_1,file=“C:/mydata/chap01/table1_1.csv”) 


2）随机数和数据抽样 <img src="https://img-blog.csdnimg.cn/17c23dfc05a9490a9c10485cadf0cfb5.png" alt="请添加图片描述"> 3）生成频数分布表

****一频表：****

>  
 生成满意度的简单频数表。 data1_1&lt;-read.csv(“C:/mydata/chap01/data1_1.csv”) attach(data1_1) mytable1&lt;-table(满意度);mytable1 prop.table(mytable1)*100 


****二频表：****

>  
 生成性别和满意度的二维列联表。 data1_1&lt;-read.csv(“C:/mydata/chap01/data1_1.csv”) attach(data1_1) mytable2&lt;-table(性别,满意度) # 生成性别和满意度的二维列联表 mytable2 addmargins(mytable2) # 为列联表添加边际和 addmargins(prop.table(mytable2)*100) # 将列联表转换成百分比表 


****多维表：****

>  
 生成三维频数表（列变量为“满意度”） data1_1&lt;-read.csv(“C:/mydata/chap01/data1_1.csv”) mytable3&lt;-ftable(data1_1,row.vars=c(“性别”,“网购次数”),col.vars=“满意度”) mytable3 生成三维频数表（列变量为"性别"和"满意度"） mytable4&lt;-ftable(data1_1,row.vars=c(“网购次数”),col.vars=c(“性别”,“满意度”)) mytable4 


4）生成频数分布表——数值数据——cut 函数

>  
 <p>data1_2&lt;-read.csv(“C:/mydata/chap01/data1_2.csv”) v&lt;-as.vector(data1_2KaTeX parse error: Expected 'EOF', got '#' at position 8: 销售额) #̲ 将销售额转化成向量 d&lt;-t…Freq/sum(ddKaTeX parse error: Expected 'EOF', got '#' at position 14: Freq)*100,2) #̲ 计算频数百分比，结果保留2位…Var1,频数=df 
      
       
        
        
          F 
         
        
          r 
         
        
          e 
         
        
          q 
         
        
          , 
         
        
          频数百分比 
         
        
          = 
         
        
          d 
         
        
          f 
         
        
       
         Freq,频数百分比=df 
        
       
     Freq,频数百分比=dfpercent) 重新命名并组织成频数分布表 mytable # 显示频数分布表</p> 


5） 生成频数分布表——数值数据——Freq 函数

>  
 <p>data1_2&lt;-read.csv(“C:/mydata/chap01/data1_2.csv”) library(DescTools) 加载包DescTools 使用默认分组，含上限值 tab&lt;- Freq(data1_2 
      
       
        
        
          销售额 
         
        
          ) 
         
        
          t 
         
        
          a 
         
        
          b 
         
        
          使用 
         
        
          F 
         
        
          r 
         
        
          e 
         
        
          q 
         
        
          函数并生成频数分布表，指定组距 
         
        
          = 
         
        
          20 
         
        
          （不含上限值） 
         
        
          t 
         
        
          a 
         
        
          b 
         
        
          1 
         
        
          &lt; 
         
        
          − 
         
        
          F 
         
        
          r 
         
        
          e 
         
        
          q 
         
        
          ( 
         
        
          d 
         
        
          a 
         
        
          t 
         
        
          a 
         
         
         
           1 
          
         
           2 
          
         
        
       
         销售额) tab 使用Freq函数并生成频数分布表，指定组距=20（不含上限值） tab1&lt;-Freq(data1_2 
        
       
     销售额)tab使用Freq函数并生成频数分布表，指定组距=20（不含上限值）tab1&lt;−Freq(data12​ 销售额, breaks=c(500,520,540,560,580,625,600,620,640,660,680,700,720),right=FALSE) 指定组距=20，不含上限值 tab2&lt;-data.frame(分组=tab1 
      
       
        
        
          l 
         
        
          e 
         
        
          v 
         
        
          e 
         
        
          l 
         
        
          , 
         
        
          频数 
         
        
          = 
         
        
          t 
         
        
          a 
         
        
          b 
         
        
          1 
         
        
       
         level,频数=tab1 
        
       
     level,频数=tab1freq,频数百分比=tab1 
      
       
        
        
          p 
         
        
          e 
         
        
          r 
         
        
          c 
         
        
          ∗ 
         
        
          100 
         
        
          , 
         
        
          累积频数 
         
        
          = 
         
        
          t 
         
        
          a 
         
        
          b 
         
        
          1 
         
        
       
         perc*100,累积频数=tab1 
        
       
     perc∗100,累积频数=tab1cumfreq,累积百分比=tab1$cumperc*100) 重新命名频数表中的变量 print(tab2,digits=3) 用print函数定义输出结果的小数位数</p> 

