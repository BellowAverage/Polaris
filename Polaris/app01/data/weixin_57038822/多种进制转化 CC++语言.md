
--- 
title:  多种进制转化 C/C++语言 
tags: []
categories: [] 

---
****多种进制转化 C/C++语言****

二进制转十六进制法：

C语言代码如下：

```
#include&lt;stdio.h&gt;
#include&lt;string.h&gt;
int main(){<!-- -->
	int N,n,k,t,i,j,m;
	char a[10005];
	int b[10005]={<!-- -->0};
	scanf("%d",&amp;N);
	while(N--){<!-- -->
		scanf("%s",&amp;a);
		n=strlen(a);
		for(i=0;i&lt;n;i++)
			b[i]=0;
		k=0;
		t=1;
		m=0;
		for(i=n-1;i&gt;=0;i--){<!-- -->
	    	b[k]+=(a[i]-'0')*t;
			t*=2;
			m++;
			if(m%4==0){<!-- -->
				k++;
				t=1;
			}
		}
		for(i=0;i&lt;n;i++){<!-- -->
			if(b[i]&gt;=10){<!-- -->
				switch(b[i]){<!-- -->
				case 10 : b[i]='A'; break;
				case 11 : b[i]='B'; break;
				case 12 : b[i]='C'; break;
				case 13 : b[i]='D'; break;
				case 14 : b[i]='E'; break;
				case 15 : b[i]='F'; break;
				}
			}
		}
		for(i=k;i&gt;=0;i--){<!-- -->
			if(b[i]!=0){<!-- -->
				for(j=i;j&gt;=0;j--){<!-- -->
			if(b[j]&gt;=65 &amp;&amp; b[j]&lt;=70 )
				printf("%c",b[j]);
			else printf("%d",b[j]);
				}
				break;
			}
		}
			if(i==-1) printf("0");
		printf("\n");
	}
}

```

十进制转任意进制：

C代码如下：

```
#include &lt;stdio.h&gt;
int main(){<!-- -->
	int x,p,i; //x为十进制数，p为目标进制大小 
	scanf("%d",&amp;x);
	scanf("%d",&amp;p);
	int a[100]; //存放余数 
	int count=0;
	do{<!-- -->
		a[count++]=x%p;
		x=x/p;
	}while(x!=0);//当商不为0时进行循环 
	
	for(i=count-1;i&gt;=0;i--){<!-- -->
		printf("%d",a[i]);
	}
} 

```

任意进制转十进制：

C++代码如下：

```
//任意进制转十进制
#include &lt;stdio.h&gt;
int main(){<!-- -->
	int x,p;   //x输入数字  p该数的进制数  
	scanf("%d",&amp;x);
	scanf("%d",&amp;p);
	int y=0,product=1;
	while(x!=0){<!-- -->
		y=y+(x%10)*product;
		x=x/10;
		product=product*p;
	}
	printf("%d",y);
	return 0;
} 

```

****二进制转八，十，十六进制****

C语言代码如下：

```
#include&lt;stdio.h&gt;
#include&lt;string.h&gt;
int main()
{<!-- -->
int s=0,i,n;

char a[8];

printf("输入一个二进制数");

gets(a);

n=strlen(a);        //字符串长度n代表输入了几位二进制数

for(i=0;i&lt;n;i++)    //循环检查输入二进制数的1

{<!-- -->

if(a[i]=='1')         //如果为1，开始计算转换为十进制

s=s+pow(2,n-i-1);continue;

}

printf("输出的八进制数为%o\n",s);   //%o输出八进制 
 printf("输出的十进制数为%d\n",s); //%d输出十进制
  printf("输出的十六进制数为%x\n",s);//%x输出十六进制 
}

```
