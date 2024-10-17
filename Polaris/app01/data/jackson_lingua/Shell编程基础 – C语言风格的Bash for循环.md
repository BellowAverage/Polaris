
--- 
title:  Shell编程基础 – C语言风格的Bash for循环 
tags: []
categories: [] 

---
## Shell编程基础 – C语言风格的Bash for循环

### Shell Programming Essentials - C Style For Loop in Bash

By Jackson@ML

>  
 循环是编程语言的基本概念之一，同样也是Bash编程的核心。当用户需要一遍又一遍地运行一系列命令直到达到特定条件时，例如：遍历一个序列或者数组，那么循环非常方便。 


实践证明，在 Bash 等脚本语言中，循环对于自动执行重复性任务很有用。 之前的帖子讲述过For循环的特点及其案例，本文简要介绍具有C语言风格的Bash For循环。

#### 1. 标准Bash的For循环

在编程语言中，for循环很常见。标准for循环可遍历一个项目列表并执行给定的命令集。

举个例子，我们来做字符串的遍历。 在下面的示例中，循环将遍历字符串列表中的每个项目，并且变量元素将设置为当前项目：

<img src="https://img-blog.csdnimg.cn/direct/dbf92ac86241479bb30bffa57aa335d1.png" alt="在这里插入图片描述"> 编辑完毕后，执行脚本文件element.sh。

```
[root@localhost sh]# sh element.sh

```

结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/30d11d45e8a647e686963e269c852036.png" alt="在这里插入图片描述">

#### 2. 遍历数组元素

我们还可以使用 for 循环来遍历数组元素。

在下面的示例中，我们将定义一个名为 cars 的数组并遍历数组的每个元素。

```
cars = (‘Ford’, ‘Toyota’, ‘Acura’, ‘Hummer’, ‘Datsun’, ‘Mitsubishi’, ‘Jeep’, ‘Nissan’, ‘BMW’, ‘Chevrolet’, ‘BYD’)
for car in “${<!-- -->cars[@]}”; do
  echo “Car: $car”
done

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/6c5a59359c13498daf8c92f0f480961a.png" alt="在这里插入图片描述">

#### 3. C 样式的 Bash For 循环

C-style Bash for loop，即C样式的Bash For循环，它的语法结构如下：

```
for ((INITIALIZATION; TEST; STEP))
do
	shell-command1
	......
done

```

INITIALIZATION 部分仅在循环开始时执行一次。然后，对TEST部分进行评估。如果结果为 false，则循环终止；如果 TEST结果 为 true，则执行 for 循环主体内的命令，并更新 STEP 部分。

在下面的示例代码中，初始化 i = 0，并在每次迭代之前检查 i 是否小于等于10。结果如果为 true，则打印 i 的当前值，并将变量 i 递增 1 （i++）；否则循环终止。

纵观C语言风格的for循环，和传统Bash for循环有些许不一样，能让人感受到C的风格。示例代码如下： <img src="https://img-blog.csdnimg.cn/direct/d156df3832024b98a7b1a962cf6da297.png" alt="在这里插入图片描述"> 运行结果如下图： <img src="https://img-blog.csdnimg.cn/direct/83193298c9a242efaa8ae8ad5f9bb5aa.png" alt="在这里插入图片描述">

#### 4. C语言风格遍历数组

定义数组的规范如下：

```
array=( item1 item2 item3 ... itemN)

```

我们尝试读取一个数组，并且用C语言风格遍历这个数组的元素。代码如下：

```
#!/bin/bash
# Define an array called fruits
fruits=("Apple" "Mango" "Pineapple" "Banana" "Orange" "Papaya" "Watermelon")
# Get total elements in an array

len=${<!-- -->#fruits[*]}   
 
# Print it using C style bash for loop
for (( i=0; i&lt;len; i++ ));
do
	echo "${fruits[$i]}"
done

```

在Shell下编辑代码文件fruits.sh, 截图如下图： <img src="https://img-blog.csdnimg.cn/direct/b8e8823a6be04c458eb92fbbe3fdf952.png" alt="在这里插入图片描述"> 执行脚本：

```
 sh fruits.sh

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/5279820e01cb418e8694be3d9b5ddb19.png" alt="在这里插入图片描述">

C风格的Shell编程，着实让笔者为之一振；小小的Shell脚本语言，居然还有这个功能！ 但，的确就是这样。

技术好文陆续推出，敬请关注。

喜欢就点赞哈！您的认可，我的动力。😃

#### 相关阅读：
1. 1. 1. 1. 1. 