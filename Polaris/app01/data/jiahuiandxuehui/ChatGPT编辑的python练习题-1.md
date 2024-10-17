
--- 
title:  ChatGPT编辑的python练习题-1 
tags: []
categories: [] 

---
本文来自：**想考python二级和python小白学习的肥友专栏**欢迎大家一起学习。

链接： <img src="https://img-blog.csdnimg.cn/e91d4fc0072a4e059290dffaf6af017d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6IKl5a2m,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述" width="200">

## 说明

当今chatGPT的横空出世，更加说明了python在编程界的重要性。今天我们就让这款用python编写的AI自己出一些练习题给我们。 <img src="https://img-blog.csdnimg.cn/1ad5c16749474fb3bd49816e3a0aad83.png" alt="在这里插入图片描述"> 省略掉以前我们做过的，我把比较不常见的列在下面了。

## 习题

>  
 实现冒泡排序算法 


```
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j] &gt; lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_lst = bubble_sort(lst)
print("排序后的列表：", sorted_lst)


```

>  
 判断一个字符串是否为有效的括号序列 


```
def is_valid_parentheses(s):
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in ")]}":
            if len(stack) == 0:
                return False
            elif c == ")" and stack[-1] != "(":
                return False
            elif c == "]" and stack[-1] != "[":
                return False
            elif c == "}" and stack[-1] != "{":
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

s = input("输入一个字符串：")
if is_valid_parentheses(s):
    print(s, "是有效的括号序列")
else:
    print(s, "不是有效的括号序列")


```

>  
 实现一个二分查找算法 


```
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left &lt;= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] &lt; target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

lst = [1, 3, 4, 5, 6, 8, 9, 10]
target = int(input("输入要查找的数字："))
index = binary_search(lst, target)
if index == -1:
    print("未找到数字", target)
else:
    print("数字", target, "的索引是", index)


```

>  
 实现一个逆波兰计算器 


```
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if is_number(token):
            stack.append(float(token))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if token == "+":
                stack.append(num1 + num2)
            
            elif token == "-":
                stack.append(num1 - num2)
            elif token == "*":
                stack.append(num1 * num2)
            elif token == "/":
                stack.append(num1 / num2)
    return stack[-1]

tokens = input("输入逆波兰表达式，数字和运算符之间用空格隔开：").split()
result = eval_rpn(tokens)
print("逆波兰表达式的计算结果是：", result)


```

>  
 实现一个插入排序算法 


```
def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i - 1
        key = lst[i]
        while j &gt;= 0 and lst[j] &gt; key:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

lst = [5, 2, 4, 6, 1, 3]
print("插入排序前：", lst)
lst = insertion_sort(lst)
print("插入排序后：", lst)


```

>  
 实现一个快速排序算法 


```
def quick_sort(lst, left, right):
    if left &lt; right:
        pivot = partition(lst, left, right)
        quick_sort(lst, left, pivot-1)
        quick_sort(lst, pivot+1, right)

def partition(lst, left, right):
    pivot = lst[right]
    i = left - 1
    for j in range(left, right):
        if lst[j] &lt;= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[right] = lst[right], lst[i+1]
    return i + 1

lst = [5, 2, 4, 6, 1, 3]
print("快速排序前：", lst)
quick_sort(lst, 0, len(lst)-1)
print("快速排序后：", lst)


```

>  
 实现一个归并排序算法 


```
def merge_sort(lst):
    if len(lst) &lt;= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i &lt; len(left) and j &lt; len(right):
        if left[i] &lt; right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

lst = [5, 2, 4, 6, 1, 3]
print("归并排序前：", lst)
lst = merge_sort(lst)
print("归并排序后：", lst)


```

>  
 实现一个堆排序算法 


```
def heap_sort(lst):
    n = len(lst)
    for i in range(n//2-1, -1, -1):
        heapify(lst, n, i)
    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)

def heapify(lst, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l &lt; n and lst[l] &gt; lst[largest]:
        largest = l
    if r &lt; n and lst[r] &gt; lst[largest]:
        largest = r
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)

lst = [5, 2, 4, 6, 1, 3]
print("堆排序前：", lst)
heap_sort(lst)
print("堆排序后：", lst)


```

>  
 实现一个线性查找算法 


```
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

lst = [1, 2, 3, 4, 5, 6]
target = 4
index = linear_search(lst, target)
if index == -1:
    print("目标元素不存在")
else:
    print("目标元素在列表中的索引是：", index)


```

**特别介绍**

>  
 📣小白练手专栏，适合刚入手的新人和想考python二级欢迎订阅 


>  
 📣python有趣练手项目里面包括了像《机器人尬聊》《恶搞程序》这样的有趣文章，可以让你快乐学python 


>  
 📣另外想学JavaWeb进厂的同学可以看看这个专栏： 


>  
 📣这是个冲刺大厂面试专栏还有算法比赛练习我们一起加油  


## <font color="red" size="6">点击直接资料领取</font>

**这里有python，Java学习资料还有有有趣好玩的编程项目，更有难寻的各种资源。反正看看也不亏。**
