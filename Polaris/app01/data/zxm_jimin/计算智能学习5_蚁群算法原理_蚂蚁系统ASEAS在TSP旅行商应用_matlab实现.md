
--- 
title:  计算智能学习5_蚁群算法原理_蚂蚁系统AS/EAS在TSP旅行商应用_matlab实现 
tags: []
categories: [] 

---


#### 文章目录
- - - - - - - - - 


## 原理部分

蚂蚁在8000万年前就建立起了自己的社会。许多“蚂蚁城市”往往由5000万个成员组成，并且是一个组织完好的复杂“城市”。 **蚁群优化（ant colony optimization, ACO）**是20世纪90年代初由意大利学者M.Dorigo等通过模拟蚂蚁的行为而提出的一种随机优化技术。最初用于求解旅行商问题，现在已经成功用于许多组合优化问题。

蚁群算法是对自然界蚂蚁的寻径方式进行模似而得出的一种**仿生算法**与启**发式搜索算法**：蚂蚁在运动过程中，能够在它所经过的路径上留下**信息素**(pheromone)的物质进行信息传递，而且蚂蚁在运动过程中能够感知这种物质，并以此指导自己的运动方向。 蚁群集体行为表现出一种信息**正反馈现象**：某一路径上走过的蚂蚁越多，则后来者选择该路径的概率就越大。

## TSP算法

<img src="https://img-blog.csdnimg.cn/2021020518051648.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210205180533930.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210205180545821.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

## 蚁群算法

<img src="https://img-blog.csdnimg.cn/20210205175851594.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

**1、路径构建** 第k只蚂蚁的路径向量R^k，按照访问顺序记录了所有k已经经过的城市序列。 设第k只蚂蚁当前所在的城市为i，则其选择城市j作为下一个访问对象的概率为： η(i,j)为启发式信息，β为其权重；τ(i,j)为边(i,j)的信息素，α为其权重。 <img src="https://img-blog.csdnimg.cn/20190226170130789." alt="在这里插入图片描述"> **2、信息素更新** m为蚂蚁总个数，逐个蚂蚁计算，每只蚂蚁在每个城市都会留下信息素; 从j到j+1这条路径上的信息素，不是所有路径都有蚂蚁经过，未经过为0。 更新边(i,j)的信息素： <img src="https://img-blog.csdnimg.cn/20190226170149679.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt=""> **3、精英蚂蚁优化算法** 在城市的规模比较大是，问题的复杂度呈指数级增长，因此可能会导致优秀路径的蚂蚁释放的信息素在全局的角度太过渺小，无法使算法很好的收敛，因此在原有的基础上，搜索到最优路径的蚂蚁会为其路径添加额外的信息素∆τ_b (i,j),e为∆τ_b (i,j)的权值。 <img src="https://img-blog.csdnimg.cn/20190226170211533.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

## 实验部分

## 一、需求分析

本实验利用蚁群算法，对TSP旅行商问题进行应用和优化。 随机生成不同的城市序列。 选取不同的参数，验证蚁群算法的效率。 对蚁群算法进行改进，改造成精英蚂蚁算法，并进行分析。 输入：不同维度的城市序列 输出：最优路径所经过的城市序列以及最优路径长度。

## 二、概要设计

如原理部分

## 三、详细设计

代码中有详细注释：

```
 city30=round(randi(5000,30,2)); %随机初始化
 city50=round(randi(5000,50,2));
 city100=round(randi(5000,100,2)); 
 save data

```

<img src="https://img-blog.csdnimg.cn/20190226170358416." alt="在这里插入图片描述">

```
%% 旅行商问题(TSP)优化
%% 清空环境变量
clear all
clc
tic%计算运行事件
%% 导入数据
%load citys_data.mat
load data
citys=city100;
%% 计算城市间相互距离
fprintf('Computing Distance Matrix... \n');
n = size(citys,1);%一共多少个城市
D = zeros(n,n);%邻接矩阵
for i = 1:n
    for j = 1:n
        if i ~= j %判断 i 的值是否等于j，若等于1，则返回0；否则，返回1
            D(i,j) = sqrt(sum((citys(i,:) - citys(j,:)).^2));%存放第i点到第j点的距离（一次计算一个点）
        else
            D(i,j) = 1e-4; %i==j处，（1.0000e-04）对角线 (两侧对称）
        end
    end
end

%% 初始化参数
fprintf('Initializing Parameters... \n');
m = 100;                              % 蚂蚁数量
alpha = 1;                           % 信息素重要程度因子
beta = 2;                            % 启发函数重要程度因子
rho = 0.7;                           % 信息素挥发因子
Q = 1;                               % 常系数
Eta = 1./D;                          % 启发函数
Tau = ones(n,n);                     % 信息素矩阵 %初始化为全1矩阵
Table = zeros(m,n);                  % 路径记录表
iter = 1;                            % 迭代次数初值
iter_max = 150;                      % 最大迭代次数
Route_best = zeros(iter_max,n);      % 各代最佳路径
Length_best = zeros(iter_max,1);     % 各代最佳路径的长度
Length_ave = zeros(iter_max,1);      % 各代路径的平均长度

e=0.3;
%% 迭代寻找最佳路径
figure;
while iter &lt;= iter_max
    %%
    flag=0;
    %%
    fprintf('迭代第%d次\n',iter);
    % 随机产生各个蚂蚁的起点城市
    start = zeros(m,1); %m*1的全0矩阵
    for i = 1:m
        temp = randperm(n); %1*n矩阵 随机打乱一个数字序列（1-n)
        start(i) = temp(1); %当前随机城市
    end
    Table(:,1) = start; %放入第一列
    % 构建解空间
    citys_index = 1:n;%1*n矩阵（1-n）
    for i = 1:m %第i只蚂蚁
        % 逐个城市路径选择
        for j = 2:n %从第2个城市开始，第1个城市已经随机生成
            tabu = Table(i,1:(j - 1));           % 已访问的城市集合(禁忌表)
            %~ismember(citys_index,tabu)是看矩阵citys_index中的数是不是矩阵citys_index中的成员，是的话结果返回0，不是返回1
            allow_index = ~ismember(citys_index,tabu);%访问过的地方未0
            allow = citys_index(allow_index);  % 待访问的城市集合（访问过的城市删掉了，因为为0）
            P = allow;
            % 计算城市间转移概率
            %剩下的城市
            for k = 1:length(allow)
                P(k) = Tau(tabu(end),allow(k))^alpha * Eta(tabu(end),allow(k))^beta;%tabu(end)当前城市
            end
            P = P/sum(P);
            % 轮盘赌法选择下一个访问城市
            Pc = cumsum(P);
            %Pc(1)为1.7665e-05 其实为0.0000，为了防止错位变成一个很小的值 sum(P)=1
            target_index = find(Pc &gt;= rand); %备选城市（满足条件的，不是剩下的所有城市）
            target = allow(target_index(1));%访问备选城市中的第一个
            Table(i,j) = target;%接下来要访问的城市
        end
    end
    % 计算各个蚂蚁的路径距离
    Length = zeros(m,1);%m*1矩阵
    for i = 1:m %第i只蚂蚁
        Route = Table(i,:); %保存当前蚂蚁的路径
        for j = 1:(n - 1)
            Length(i) = Length(i) + D(Route(j),Route(j + 1));
        end
        Length(i) = Length(i) + D(Route(n),Route(1)); %m*1矩阵，保存每只蚂蚁的总路径
    end
    % 计算最短路径距离及平均距离
    %第iter代蚂蚁
    if iter == 1
        [min_Length,min_index] = min(Length);
        Length_best(iter) = min_Length;
        Length_ave(iter) = mean(Length);
        Route_best(iter,:) = Table(min_index,:);
    else
        [min_Length,min_index] = min(Length);%当前此代数最优距离
        Length_best(iter) = min(Length_best(iter - 1),min_Length);%当前所有代数中的最优距离
        Length_ave(iter) = mean(Length);%当前此代数平均距离
        if Length_best(iter) == min_Length %如果当前此代数最优距离在所有代数中都是最优的
            Route_best(iter,:) = Table(min_index,:);%最优环路更新
            %% 
            flag=1;
        else
            Route_best(iter,:) = Route_best((iter-1),:);%最优环路与前一代相同
              %% 
            flag=0;
        end
    end
    % 更新信息素
    Delta_Tau = zeros(n,n);
    % 逐个蚂蚁计算 每只蚂蚁在每个城市都会留下信息素
    for i = 1:m
        for j = 1:(n - 1)
            % 逐个城市计算 从j到j+1
            % Q=1 常系数
            %从j到j+1这条路径上的信息素，不是所有路径都有蚂蚁经过，未经过为0
            Delta_Tau(Table(i,j),Table(i,j+1)) = Delta_Tau(Table(i,j),Table(i,j+1)) + Q/Length(i);%Q/Length(i)距离的倒数
            
        end
        Delta_Tau(Table(i,n),Table(i,1)) = Delta_Tau(Table(i,n),Table(i,1)) + Q/Length(i);
%% 精华蚂蚁
        if flag==1&amp;&amp;m==min_index
                Delta_Tau(Table(i,n),Table(i,1)) = Delta_Tau(Table(i,n),Table(i,1)) + e/Route_best(iter,:);
        end
       
        
    end
    % rho=0.1 信息素挥发因子
    Tau = (1-rho) * Tau + Delta_Tau;
    
    
    %   figure;
    %最佳路径的迭代变化过程
    %Length_best （iter_max*1）矩阵，存储每一代的最优距离
    [Shortest_Length,index] = min(Length_best(1:iter));
    Shortest_Route = Route_best(index,:);
    plot([citys(Shortest_Route,1);citys(Shortest_Route(1),1)],...
        [citys(Shortest_Route,2);citys(Shortest_Route(1),2)],'o-');
    pause(0.3);%程序暂停0.3秒
    % 迭代次数加1，清空路径记录表
    iter = iter + 1;%进入下一代
    Table = zeros(m,n);%重置城市表
    
    % end
end

%% 结果显示
[Shortest_Length,index] = min(Length_best);
Shortest_Route = Route_best(index,:);
disp(['最短距离:' num2str(Shortest_Length)]);
disp(['最短路径:' num2str([Shortest_Route Shortest_Route(1)])]);

%% 绘图
figure(1)
plot([citys(Shortest_Route,1);citys(Shortest_Route(1),1)],...
    [citys(Shortest_Route,2);citys(Shortest_Route(1),2)],'o-');
grid on
for i = 1:size(citys,1)
    text(citys(i,1),citys(i,2),['   ' num2str(i)]);
end
text(citys(Shortest_Route(1),1),citys(Shortest_Route(1),2),'       起点');
text(citys(Shortest_Route(end),1),citys(Shortest_Route(end),2),'       终点');
xlabel('城市位置横坐标')
ylabel('城市位置纵坐标')
title(['蚁群算法优化路径(最短距离:' num2str(Shortest_Length) ')'])
figure(2)
plot(1:iter_max,Length_best,'b',1:iter_max,Length_ave,'r:')
legend('最短距离','平均距离')
xlabel('迭代次数')
ylabel('距离')
title('各代最短距离与平均距离对比')
toc%计算程序运行时间
disp(['运行时间: ',num2str(toc)]

```

);

## 四、实验结果总结

可视化结果： <img src="https://img-blog.csdnimg.cn/20190226170422520.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> **蚂蚁优化算法：** **实验一：** 参数设置： 蚂蚁数量m=50 信息素重要程度因子α=1， 启发函数重要程度因子β=5 信息素挥发因子ρ=0.1 <img src="https://img-blog.csdnimg.cn/20190226170534745.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 可以看出，在迭代此时为150次时，算法已经比较收敛，可以得到比较好的路径，时间也比较短。 **实验二：** 根据资料中，蚂蚁数量取值都有城市数目，算法有比较好的性能。 参数设置： 蚂蚁数量m=n(城市数目） 信息素重要程度因子α=1， 启发函数重要程度因子β=5 信息素挥发因子ρ=0.1 最大迭代次数iter_max=150 <img src="https://img-blog.csdnimg.cn/20190226170550566.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt=""> 可以看出，在其他参数不变的情况下，m=n(城市数目）时，不管蚂蚁数量是大于50还是小于50，算法的效果都比较好。

**实验三：** 根据资料中，α=1，β=2~5，比较合适。 参数设置： 蚂蚁数量m=30 信息素挥发因子ρ=0.1 最大迭代次数iter_max=150 <img src="https://img-blog.csdnimg.cn/20190226170625356.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt=""> 可以看出，α=1，β=2的效果是最好的，用时最短，路径最短。

**实验四：** 根据资料中，在蚂蚁系统和精华蚂蚁系统中，ρ=0.5，比较合适。 参数设置： 蚂蚁数量m=n(城市数目） 信息素重要程度因子α=1， 启发函数重要程度因子β=2 最大迭代次数iter_max=150 <img src="https://img-blog.csdnimg.cn/20190226170650938.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt=""> 可以看出，在ρ=0.7时，算法效果最好。

**精华蚂蚁算法：** **实验五：** 参数设置： 蚂蚁数量m=100 信息素重要程度因子α=1， 启发函数重要程度因子β=2 最大迭代次数iter_max=150 信息素挥发因子ρ=0.7 <img src="https://img-blog.csdnimg.cn/20190226170708923.?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3p4bV9qaW1pbg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> e=0.3时，算法的效果最好，得出的结果比未优化的蚂蚁算法要好，所用的时间也比较好。

**实验结果分析：** 经过以上实验，进行分析，可以得出在城市数量小于一定值时，迭代次数在150次左右已经能够逼近全局最优解。 在其他参数不变的情况下，蚂蚁数量与城市数量相等时，得出结果比较好，因为蚂蚁数量过小的情况下，会导致部分路径无法得到，其中可能包含全局最优解。 在其他参数不变的情况下，α=1，β=2，得出结果比较好，因为蚂蚁选取路径时信息素和启发式信息都比较重要，蚂蚁还是需要有自己的“主见”，这样才能保证不收敛到局部最优解。 在其他参数不变的情况下，ρ=0.7时，得出结果比较好，因为信息素挥发因子过小，会导致算法“早熟”，收敛到局部最优解。 采用精英蚂蚁算法，e=0.3时，得出结果比未优化的算法效果好，即节省了时间，还是算法得到更好的解，说明精英蚂蚁的结果对其他蚂蚁产生了更正面的影响。

**实验总结： 通过这次实验，我对蚁群算法有了更深入的了解，对蚁群算法的各个步骤也更加清楚，明白了具体要怎样设定参数才能得到更好的结果，以后将继续学习，将蚁群算法应用到实际的问题中。**

## 代码下载：

**注意，代码下载后仍需自行调试~** 积分值为5（如果有变为csdn自行修改）——完整代码其实和上面贴出的差别不大，酌情下载~ https://download.csdn.net/download/zxm_jimin/10976971

**感谢各位大佬看到最后~ 本文为原创。转载请注明出处。 注：参考了一些文章，博客，如有侵权请联系，我附上原出处。**
