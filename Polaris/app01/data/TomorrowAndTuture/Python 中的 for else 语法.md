
--- 
title:  Python 中的 for else 语法 
tags: []
categories: [] 

---
这个语法应该是存在了好长一段时间了，但是大家一直不怎么用，而且实际工程上用得人也比较少，但自己比较好奇，所以索性写一下。

### 测试

#### 不用 break

```
for i in range(5):
    if i == 3:
        continue
    print(i)
else:
    print('hello')
```

```
0
1
2
4
hello
```

测试发现，如果 for 循环可以正常循环完毕到结束的话，else 的代码是会执行的。

#### 使用 break

```
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print('hello')
```

```
0
1
2
```

测试发现，如果 for 循环被 break 提前终止掉循环的话，else 的代码是不会执行的。

### **总结**

**总结起来比较简单，如果 for 循环正常结束，else 中语句执行。如果是 break 的，则不执行。**

### **实战**

那么，这种语法在实际的项目中有没有用武之地呢？哈哈，这个还真有，黑格尔的名言：**存在即合理**。

**比如说，我现在有个需求，需要判断一个 IP 是否合法，合法则输出 YES，不合法则输出 NO。**

常规写法应该是下面这种的（会有个专门的 result 的变量来存储是否合法，而且初始默认 IP 合法，不合法的话再修改它的值）：

```
ip = [10, 138, 15, 10]
result = 'YES'
for i in ip:
    if i &lt; 0 or i &gt; 255:
        result = 'NO'
        break
print(result)
```

或

```
ip = [10, 138, 15, 10]
mark = True
for i in ip:
    if i &lt; 0 or i &gt; 255:
        mark = False
        break
print('YES' if mark else 'NO')

```

 那么，如果要使用 for else 来实现相同的功能，应该是怎么样的呢？

```
ip = [10, 138, 15, 10]
for i in ip:
    if i &lt; 0 or i &gt; 255:
        print('NO')
        break
else:
    print('YES')
```

**对比上面两种写法，能看出有什么区别吗？对！没错，for else 竟然没有使用 result 变量和额外的 if 判断语句即可实现相同的功能，确乎的确是要简洁一些。**

**一般 for 循环结束后，我们无法直接知道 for 循环是提前跳出的，还是正常走完整个循环结束的，需要通过额外的变量或者 if 语句进行判断（比如本例，你可能需要一个 bool 变量来确定是不是被 break 提前结束了循环），而 for else 则很简单的解决了这个问题。**


