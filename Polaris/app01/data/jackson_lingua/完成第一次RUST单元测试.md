
--- 
title:  完成第一次RUST单元测试 
tags: []
categories: [] 

---
## 完成第一次RUST单元测试

### Complete the First Unit Test in Rust

>  
 测试，是在RUST编程过程中，用于验证非测试代码是否以预期的方式运行的一种重要手段。测试函数的主题通常要执行某种设置，以运行我们期待测试的代码，然后用assert(断言)结果，来判断是否符合我们的预期。 
 大多数单元测试都要进入带有#[cfg(test)]属性的测试模组。测试函数显式标有#[test]属性。 


为了夯实基本知识和实际操作，当参与项目的成员多起来之后，就必然需要创建多人协作的项目。这样，代码健康性和安全性就非常重要。

本文利用RUST自身功能尝试进行单元测试验证，供广大程序员参考。

#### 1. 创建测试项目

a) 新建一个库，名叫arithmetic, 在终端（或者命令行窗口）运行以下命令：

```
cargo new arithmetic --lib 

```

<img src="https://img-blog.csdnimg.cn/c36267d05b1448639bed4cfb2042316c.png" alt="在这里插入图片描述"> b) 创建后，查看arithmetic子文件夹，在Visual Studio Code中打开位于src\lib.rs的程序库文件lib.rs； <img src="https://img-blog.csdnimg.cn/bc8185eb42d54748af3bb1545acd31a1.png" alt="在这里插入图片描述">

我们看到，除了共有的pub函数 **add**（执行加法运算）之外，还有个**tests**模块（关键字mod）.

其中，#[test]标记了测试块，即下方的it_works()函数是默认的测试函数；尝试在命令行运行这个测试程序。

```
cargo test 

```

<img src="https://img-blog.csdnimg.cn/b2a4f7e1334b451aa3fd139d00bbfbc7.png" alt="在这里插入图片描述"> 运行结果为 **test result: ok, …**

<img src="https://img-blog.csdnimg.cn/793d5f69705340079abde9d4e1dcaaf4.png" alt="在这里插入图片描述">

#### 2. 编写测试程序

标准库std提供了如下几种宏来编写测试用例： **a) assert! b) assert_eq! c) assert_ne!** 以上三种宏均支持自定义，当测试失败时自定义信息会连同失败信息一道打印出来，有助于更好理解和维护代码问题。

##### # 梳理测试逻辑

>  
 测试的常用方法，是将测试函数的返回值与期望值进行比较，检查二者是否相等。 


让我们修改lib.rs中的默认代码，来实现一个判断是否为正整数的bool型函数

```
pub fn is_positive(x: i32)

```

同时，在测试代码块添加判断该正整数是否为正的函数

```
is_positive_test()

```

代码如下图所示： <img src="https://img-blog.csdnimg.cn/1aa2ad528d0543b8b003857296bd925d.png" alt="在这里插入图片描述"> 运行测试命令，得到结果如下所示。

```
cargo test

```

<img src="https://img-blog.csdnimg.cn/7ad9311b8c354a6c88f00022fa2808b2.png" alt="在这里插入图片描述"> 显示测试函数**is_positive_test**测试完成，结果是 **ok**.

利用RUST语言，在Windows 10系统完成了第一次测试，是不是很酷？ 欢迎关注我并一起交流Rust编程技巧。

让我们为了技术精进共同奋斗！

#### 3. [Bonus]：另一个单元测试用例（供参考）

我写了另一个测试用例，创建函数**i_love_you()**, 来对比之后，返回“I love you"或者“Leave me alone.”的字符串输出，用来测试时，启用**assert_eq!()**宏进行对比。

<img src="https://img-blog.csdnimg.cn/39072e07288346dbbfa80910df3be939.png" alt="在这里插入图片描述"> 测试时，注意对i_love_you()函数的返回值类型，要写为static的字符串类型。 但仍然发现错误提示，如下图所示： <img src="https://img-blog.csdnimg.cn/d9d7a60700214137bee4de7805ecdc2c.png" alt="在这里插入图片描述"> 逐句读懂错误提示，知道为什么结果出错FAILED，是由于**assertion failed**.

重写代码后，发现为函数i_love_you()返回的值类型错误，即&amp;str所指引用无法返回；换用String对象作为返回值类型，修改代码后，如下图： <img src="https://img-blog.csdnimg.cn/7a4c6b0737934de985d739a13ded791a.png" alt="在这里插入图片描述"> 重新运行测试命令，

```
cargo test

```

测试成功！（如下图所示）

<img src="https://img-blog.csdnimg.cn/6b569918aefa424b9d2f2627b17b1c2b.png" alt="在这里插入图片描述"> 至此，用RUST语言实现了第一次单元测试。

喜欢就点赞哈！😊

技术美文持续推出，欢迎关注。

**All rights reserved. @ 2023, 版权所有，侵权必究。**
