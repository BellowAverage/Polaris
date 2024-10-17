
--- 
title:  打开phpmyadmin后遇到问题“Warning in ./libraries/sql.lib.php#613 count():的解决办法，亲测有效 
tags: []
categories: [] 

---
在安装好phpmyadmin后遇到问题

>  
 Warning in ./libraries/sql.lib.php#613 count(): Parameter must be an array or an object that implements Countable 


通过以下网址内方法解决 https://devanswers.co/problem-php-7-2-phpmyadmin-warning-in-librariessql-count/ 即 编辑文件/usr/share/phpmyadmin/libraries/sql.lib.php `sudo nano /usr/share/phpmyadmin/libraries/sql.lib.php` 将文件内容 (count( 
     
      
       
       
         a 
        
       
         n 
        
       
         a 
        
       
         l 
        
       
         y 
        
       
         z 
        
       
         e 
        
        
        
          d 
         
        
          s 
         
        
       
         q 
        
        
        
          l 
         
        
          r 
         
        
       
         e 
        
       
         s 
        
       
         u 
        
       
         l 
        
       
         t 
        
       
         s 
        
        
        
          [ 
         
        
          ′ 
         
        
       
         s 
        
       
         e 
        
       
         l 
        
       
         e 
        
       
         c 
        
        
        
          t 
         
        
          e 
         
        
       
         x 
        
       
         p 
        
        
        
          r 
         
        
          ′ 
         
        
       
         ] 
        
       
         = 
        
       
         = 
        
       
         1 
        
       
         ) 
        
       
         替 
        
       
         换 
        
       
         为 
        
       
         ( 
        
       
         ( 
        
       
         c 
        
       
         o 
        
       
         u 
        
       
         n 
        
       
         t 
        
       
         ( 
        
       
      
        analyzed_sql_results['select_expr'] == 1)替换为 ((count( 
       
      
    analyzeds​qlr​esults[′selecte​xpr′]==1)替换为((count(analyzed_sql_results[‘select_expr’]) == 1) 就完美解决了
