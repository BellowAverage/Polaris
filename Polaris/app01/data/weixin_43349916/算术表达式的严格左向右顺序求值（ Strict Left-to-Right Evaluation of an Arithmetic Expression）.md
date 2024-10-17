
--- 
title:  算术表达式的严格左向右顺序求值（ Strict Left-to-Right Evaluation of an Arithmetic Expression） 
tags: []
categories: [] 

---
### 1. 一点废话：

这段代码应该是很多编程初学者的必经之路，emm~ 可以理解到很多常见函数的用法，可能还会体会到逻辑思维在编程一点点体现，当做编程学习的起点还是不错的。 本程序实现了将算术表达式读入，并自左向右进行运算可跳过空格。 例如2 * 3 +7*5 得到结果65。

### 2.关于代码

#### （1）变量命名规则

我不喜欢随随便便一个i，j，k就完事，每个变量都有他存在的意义，所以更好的命名变量也有利于增强代码的可读性。

```
char expression[100];                       //储存算式
int temp=0;                                 //遍历算式的每个字符
char op;                                    //储存运算符
int pre_num=expression[0]-'0',next_num=0;   //用来计算
int result=0;                               //最终结果

```

#### （2）代码中的亮点

我比较自恋就找了两个

##### ①scanf（）函数的妙用

这样可以防止字符串中出现的空格干扰读取整个字符串

```
scanf("%[^\n]",expression);//直到读到换行符才停止

```

##### ②巧用if（）嵌套

这就是所谓的逻辑思维的体现了，嵌套可以从某种程度上降低代码的复杂度。

#### （3）完整代码来了！

```
#include&lt;stdio.h&gt;
#include &lt;string.h&gt;
int operation(char expression[]);
int main()
{<!-- -->
char expression[100];                                             //store the expression
printf("Please Enter an expression\n"); 
scanf("%[^\n]",expression); 
operation(expression);                            
      
return 0;
}


int operation(char expression[])
{<!-- -->     
   int temp=0;                                                    //to traverse expression
   char op;                     
   int pre_num=expression[0]-'0',next_num=0;                      //Type conversion
   int result=0;
   while(expression[temp] != '\0')
   {<!-- -->

      char flag=expression[temp];                                 
      if(flag!=' ')
      {<!-- -->
         if(flag=='+'||flag=='-'||flag=='*'||flag=='/')
         {<!-- -->
            op=flag;
            temp++;            
         }

         else
            {<!-- -->
               next_num=flag-'0';                                      //Type conversion
               temp++;
               switch(op)
                  {<!-- -->
                     case'+':pre_num=pre_num+next_num;                 
                     break;
                     case'-':pre_num=pre_num-next_num;                
                     break;
                     case'*':pre_num=pre_num*next_num;                    
                     break;
                     case'/':pre_num=pre_num/next_num;                    
                     break;
                     default:break;                                    //if there is no operator
                  }
               
            }
      }      
      else                                                             //space appeared
      {<!-- -->
         temp++;
      } 
  }
   result=pre_num ; 
   printf("  result:%d\n",result );                                
   return result;
}

```
