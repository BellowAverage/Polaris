
--- 
title:  C++函数的用法注意事项 
tags: []
categories: [] 

---


#### 目录标题
- - - - - 


## 默认参数

```
//默认参数
int test1(int a=5,int b=6) {<!-- -->

	return a + b;
}

//函数声明的时候写了默认参数，函数实现的时候就不能有了,两者只能有一个
int test2(int a = 3, int b = 4);

int test2(int a,int b) {<!-- -->
	return a + b;
}

```

## 占位参数

```
//占位参数.这里没有用到
void test3(int a,int ) {<!-- -->

	cout &lt;&lt; "test3"&lt;&lt;endl;
}

```

## 重载

```
/*
重点部分


函数重载：同一个作用域，函数名相同但是函数的参数类型不同或者个数、顺序不同
提高函数复用性,和Java用法类似

*/
void test4() {<!-- -->
	cout &lt;&lt; "无参" &lt;&lt; endl;

}
void test4(int a) {<!-- -->
	cout &lt;&lt; "含int a" &lt;&lt; endl;
}

void test4(double a) {<!-- -->
	cout &lt;&lt; "含double a" &lt;&lt; endl;
}

//需要注意
void test4(int&amp; a,int b) {<!-- -->//int&amp; a=10 不合法
	cout &lt;&lt; "不含 const的引用类型 " &lt;&lt; endl;
}

void test4(const int&amp; a,int b) {<!-- -->//const int&amp; a=10合法
	cout &lt;&lt; "含 const 的引用类型" &lt;&lt; endl;
}

void test4(int a, double b=3.56) {<!-- -->//这里出现了默认参数double b 在调用的时候可能和第一个test4冲突



}

```

## 重写

```
//重写的注意事项是：
/*
1)重写访问修饰符的限制一定要大于被重写方法的访问修饰符

(2)重写的参数列表一定要完全和被重写的方法相同，专否则的话不能称其为重写而是重载

(3)重写返回的类型一定要一直和被重写的方法的返回类型相同，否则不能称其为重写而是重载

(4)重写方法一定不可以抛出新的检查异常或者是比被重写方法申明更加宽泛的检查型异常
*/

```

```
int main() {<!-- -->
	test1(4);//result 10
	test1();//result 11
	test1(1, 2);//3

	test2();//7
	test2(5);//9
	test2(2, 2);//4

	//重载
	test4(3);
	test4();
	test4(3.67);
	test4(10, 4);//猜猜
	int temp = 10;
	test4(temp, 3);//猜猜这次

}

```

## 全部示例

```
#include&lt;iostream&gt;

using namespace std;

//默认参数
int test1(int a=5,int b=6) {<!-- -->

	return a + b;
}

//函数声明的时候写了默认参数，函数实现的时候就不能有了,两者只能有一个
int test2(int a = 3, int b = 4);

int test2(int a,int b) {<!-- -->
	return a + b;
}

//占位参数.这里没有用到
void test3(int a,int ) {<!-- -->

	cout &lt;&lt; "test3"&lt;&lt;endl;
}

/*
重点部分


函数重载：同一个作用域，函数名相同但是函数的参数类型不同或者个数、顺序不同
提高函数复用性,和Java用法类似

*/
void test4() {<!-- -->
	cout &lt;&lt; "无参" &lt;&lt; endl;

}
void test4(int a) {<!-- -->
	cout &lt;&lt; "含int a" &lt;&lt; endl;
}

void test4(double a) {<!-- -->
	cout &lt;&lt; "含double a" &lt;&lt; endl;
}

//需要注意
void test4(int&amp; a,int b) {<!-- -->//int&amp; a=10 不合法
	cout &lt;&lt; "不含 const的引用类型 " &lt;&lt; endl;
}

void test4(const int&amp; a,int b) {<!-- -->//const int&amp; a=10合法
	cout &lt;&lt; "含 const 的引用类型" &lt;&lt; endl;
}

void test4(int a, double b=3.56) {<!-- -->//这里出现了默认参数double b 在调用的时候可能和第一个test4冲突



}


//重写的注意事项是：
/*
1)重写访问修饰符的限制一定要大于被重写方法的访问修饰符

(2)重写的参数列表一定要完全和被重写的方法相同，专否则的话不能称其为重写而是重载

(3)重写返回的类型一定要一直和被重写的方法的返回类型相同，否则不能称其为重写而是重载

(4)重写方法一定不可以抛出新的检查异常或者是比被重写方法申明更加宽泛的检查型异常
*/

int main() {<!-- -->
	test1(4);//result 10
	test1();//result 11
	test1(1, 2);//3

	test2();//7
	test2(5);//9
	test2(2, 2);//4

	//重载
	test4(3);
	test4();
	test4(3.67);
	test4(10, 4);//猜猜
	int temp = 10;
	test4(temp, 3);//猜猜这次

}

```
