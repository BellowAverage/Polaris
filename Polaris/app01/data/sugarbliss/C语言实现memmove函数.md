
--- 
title:  C语言实现memmove函数 
tags: []
categories: [] 

---
memmove函数内部的实现原理：
1.  当源内存的首地址等于目标内存的首地址时，不进行任何拷贝 1.  当源内存的首地址大于目标内存的首地址时，实行正向拷贝 1.  当源内存的首地址小于目标内存的首地址时，实行反向拷贝 
注意：无论正向拷贝还是反向拷贝都是为了在发生内存重叠时能正确拷贝（保证源串在**被覆盖**之前将重叠区域的字节拷贝到目标区域中）

```
#include&lt;bits/stdc++.h&gt;
#include&lt;assert.h&gt;
using namespace std;
void* my_memmove(void* dest, const void* src, size_t count)
{
	if (0 == count) return nullptr;
	if (nullptr == dest || nullptr == src)  return nullptr;

	char* dest_ = (char*)dest;;
	char* src_ = (char*)src;
	if ((dest_ &gt; src_) &amp;&amp; (dest_ &lt; src_ + count))//判断内存重叠时的情况反向拷贝（如果正向，会改变模板原来的值）
	{
		printf("发生重叠\n");
		while (count--)
			*(dest_ + count) = *(dest_ + count);
	}
	else //不重叠情况正向拷贝（如果反向，也会改变模板原来的值）
	{
		while (count--)
			*dest_++ = *src_++;
	}
	return dest;
}

int main()
{
    char s1[] = "abcdef";

    my_memmove(s1+2, s1, 3);
    cout &lt;&lt; s1 &lt;&lt; endl;
    return 0;
}

```

 
