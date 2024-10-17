
--- 
title:  【自定义Matlab函数】利用Kronecker积求解矩阵方程AXB=D 
tags: []
categories: [] 

---
## 基本知识

### Kronecker积定义

如果A是一个m×n的矩阵，B是一个p×q的矩阵，A与B的Kronecker积为一个mp×nq的分块矩阵： <img src="https://img-blog.csdnimg.cn/20210429210729762.png" alt="图源百度百科-克罗内克积"> 具体为： <img src="https://img-blog.csdnimg.cn/2021042921092927.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzUyMzYxNjk5,size_16,color_FFFFFF,t_70" alt="图源百度百科-克罗内克积">

### Kronecker积与矩阵方程

首先需要知道**矩阵拉直运算/矩阵向量化处理**概念：矩阵按行或列的顺序组成一个长向量（即下文中**vec()**）. 基于Kronecker积的定义，我们可以得出如下性质： <img src="https://img-blog.csdnimg.cn/20210429211545319.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzUyMzYxNjk5,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 基于此，对于矩阵方程**AXB=D**的求解等价于通过求解：<img src="https://img-blog.csdnimg.cn/20210429212948492.png#pic_center" alt="在这里插入图片描述"> 得到**vec(X)** 进而通过逆拉直运算求得**X**

## Matlab代码实现

### Matlab自带函数

Matlab自带kron()函数来计算Kronecker积 格式：C = kron(A,B)

### 自定义函数

函数定义：

```
function X = SloveEquationKron(A,B,D)
[m,p]=size(A);
[q,n]=size(B);
[m,n]=size(D);
B=B';
C=[];                            % 创建空矩阵C
for row=1:n
    M=[];                        % 辅助矩阵M
    for col=1:q
        M=[M,B(row,col)*A];
    end
    C=[C;M];                     % 矩阵拼接实现Kronecker积
end
XX=C\D(:);                       % inv(C)*vec(D)        C=B'与A的kron积
X=reshape(XX,[p,q]);
end

```

测试程序：

```
m=10; p=5; q=6; n=8;
A = rand(m,p); 
X = zeros(p,q);
B = rand(q,n);
D = rand(m,n);
X = SloveEquationKron(A,B,D);
norm(kron(B',A)\D(:)-X(:),'fro')       %正确输出0

```

参考资料： 
