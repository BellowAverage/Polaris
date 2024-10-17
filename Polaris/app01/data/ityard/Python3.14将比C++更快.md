
--- 
title:  Python3.14将比C++更快 
tags: []
categories: [] 

---
作者：Denn·is Bakhuis

Python 是数据科学 (DS) 和机器学习 (ML) 中最常用的脚本语言之一。根据“PopularitY of Programming Languages”，Python 是 Google 上搜索次数最多的语言。除了作为将各种 DS/ML 解决方案连接在一起的出色胶水语言之外，它还有许多库可以对数据进行方便处理。

我们以前也发过文章做过一些3.11 版的测试。因为这个版本的主要特点是速度显着提高。

在这篇文章中，是国外的一个大佬进行的数据分析，通过他的分析可以证明Python 3.14 将比 C++更快。

本文的方法是：使用蒙特卡洛方法估计 Pi。

这个算法的想法很简单，但是在大学的一些数学课程中都会有介绍：有一个大小为 2r 的正方形，在这个正方形中我们拟合一个半径为 r 的圆。采用一个在平面上生成数字的随机数生成器：&lt;-r, r&gt;, &lt;-r, r&gt;。圆上的点与正方形上的点之间的比率（读取：所有点）是面积比的近似值，我们可以用它来近似 Pi。公式如下：

<img src="https://img-blog.csdnimg.cn/img_convert/deb1ec7b56b9b94669109e18e715e201.png" alt="deb1ec7b56b9b94669109e18e715e201.png">

```
将实际估计与测试脚本分开，这样就可以重复测试并取平均值。这里还是用
Argparse 对脚本进行了参数化，Argparse 是一个用于解析来自命令行界面
(CLI) 的参数的标准库。Python 代码如下所示：
```

```
def estimate_pi(    n_points: int,    show_estimate: bool, ) -&gt; None:    """    Simple Monte Carlo Pi estimation calculation.    Parameters    ----------    n_points        number of random numbers used to for estimation.    show_estimate        if True, will show the estimation of Pi, otherwise        will not output anything.    """    within_circle = 0     for _ in range(n_points):        x, y = (random.uniform(-1, 1) for v in range(2))        radius_squared = x**2 + y**2         if radius_squared &lt;= 1:            within_circle += 1     pi_estimate = 4 * within_circle / n_points     if not show_estimate:        print("Final Estimation of Pi=", pi_estimate)   def run_test(    n_points: int,    n_repeats: int,    only_time: bool, ) -&gt; None:    """    Perform the tests and measure required time.    Parameters    ----------    n_points        number of random numbers used to for estimation.    n_repeats        number of times the test is repeated.    only_time        if True will only print the time, otherwise        will also show the Pi estimate and a neat formatted        time.    """    start_time = time.time()     for _ in range(n_repeats):        estimate_pi(n_points, only_time)     if only_time:        print(f"{(time.time() - start_time)/n_repeats:.4f}")    else:        print(            f"Estimating pi took {(time.time() - start_time)/n_repeats:.4f} seconds per run."        )
```

测试多个 Python 版本的最简单方法是使用 Docker。 要使用 Docker需要安装它。在 Linux 和 Mac 中它相对容易，在 Windows 中稍微复杂一些。虽然Docker中运行会有一些效率的降低，但是测试都在Docker进行，所以误差就可以忽略了。要在容器化 Python 环境中运行本地脚本，可以使用下面命令：

```
docker run -it --rm \  -v $PWD/your_script.py:/your_script.py \  python:3.11-rc-slim \  python /yourscript.py
```

我们也是用python脚本来自动化这个过程：

```
def test_version(image: str) -&gt; float:    """    Run single_test on Python Docker image.    Parameter    ---------    image        full name of the the docker hub Python image.    Returns    -------    run_time        runtime in seconds per test loop.    """    output = subprocess.run([            'docker',            'run',            '-it',            '--rm',            '-v',            f'{cwd}/{SCRIPT}:/{SCRIPT}',            image,            'python',            f'/{SCRIPT}',            '--n_points',            str(N_POINTS),            '--n_repeats',            str(N_REPEATS),            '--only-time',        ],        capture_output=True,        text=True,    )    avg_time = float(output.stdout.strip())    return avg_time # Get test time for current Python version base_time = test_version(NEW_IMAGE['image']) print(f"The new {NEW_IMAGE['name']} took {base_time} seconds per run.\n") # Compare to previous Python versions for item in TEST_IMAGES:    ttime = test_version(item['image'])    print(        f"{item['name']} took {ttime} seconds per run."        f"({NEW_IMAGE['name']} is {(ttime / base_time) - 1:.1%} faster)"    )
```

这些测试时的结果具体取决于CPU 。以下是7 个主要 Python 版本的结果：

```
The new Python 3.11 took 6.4605 seconds per run. Python 3.5 took 11.3014 seconds.(Python 3.11 is 74.9% faster) Python 3.6 took 11.4332 seconds.(Python 3.11 is 77.0% faster) Python 3.7 took 10.7465 seconds.(Python 3.11 is 66.3% faster) Python 3.8 took 10.6904 seconds.(Python 3.11 is 65.5% faster) Python 3.9 took 10.9537 seconds.(Python 3.11 is 69.5% faster) Python 3.10 took 8.8467 seconds.(Python 3.11 is 36.9% faster)
```

Python 3.11 的基准测试平均耗时 6.46 秒。与之前的版本 (3.10) 相比，这几乎快了 37%。3.9 版和 3.10 版之间的差异大致相同，在下图中我们进行这个数据的可视化：

<img src="https://img-blog.csdnimg.cn/img_convert/0ef3bd8ad3680731d793b9eeea3de61f.png" alt="0ef3bd8ad3680731d793b9eeea3de61f.png">

在谈论速度时，人们总是说：如果你想要速度，为什么不使用 C。

```
C 比 Python 快得多！
```

这里使用了 GNU C++，因为它带有一个不错的时间测量库（chrono）,我们的c++代码如下：

```
#include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; #include &lt;chrono&gt; #include &lt;array&gt; #define N_POINTS 10000000 #define N_REPEATS 10 float estimate_pi(int n_points) {    double x, y, radius_squared, pi;    int within_circle=0;    for (int i=0; i &lt; n_points; i++) {      x = (double)rand() / RAND_MAX;      y = (double)rand() / RAND_MAX;      radius_squared = x*x + y*y;      if (radius_squared &lt;= 1) within_circle++;    }    pi=(double)within_circle/N_POINTS * 4;    return pi; } int main() {    double avg_time = 0;    srand(42);    for (int i=0; i &lt; N_REPEATS; i++) {        auto begin = std::chrono::high_resolution_clock::now();        double pi = estimate_pi(N_POINTS);        auto end = std::chrono::high_resolution_clock::now();        auto elapsed = std::chrono::duration_cast&lt;std::chrono::nanoseconds&gt;(end - begin);        avg_time += elapsed.count() * 1e-9;        printf("Pi is approximately %g and took %.5f seconds to calculate.\n", pi, elapsed.count() * 1e-9);    }    printf("\nEach loop took on average %.5f seconds to calculate.\n", avg_time / N_REPEATS); }
```

C++ 是一种编译语言，我们需要先编译源代码才能使用它：

```
g++ -o pi_estimate pi_estimate.c
```

编译后，运行构建的可执行文件。输出如下：

```
Pi is approximately 3.14227 and took 0.25728 seconds to calculate. Pi is approximately 3.14164 and took 0.25558 seconds to calculate. Pi is approximately 3.1423 and took 0.25740 seconds to calculate. Pi is approximately 3.14108 and took 0.25737 seconds to calculate. Pi is approximately 3.14261 and took 0.25664 seconds to calculate. Each loop took on average 0.25685 seconds to calculate.
```

相同循环只需要 0.257 秒。让我们在之前的图中将其添加为一条线，如下所示。

<img src="https://img-blog.csdnimg.cn/img_convert/950285a69a5424e402d9dea31c84056e.png" alt="950285a69a5424e402d9dea31c84056e.png">

我们清楚地看到了C++很快，但是Python 开发人员提到，接下来的几个版本将会显着提高速度，在这个假设的前提下，我们的绝活就要来了，请大家理清思路注意观看。

我们以假设这个速度会保持下去（是的，超级安全的假设🙃）。在这种势头固定的情况下，Python 何时会超越 C++ 呢。我们当然可以使用外推法来预测下几个 Python 版本的循环时间，见下图。

<img src="https://img-blog.csdnimg.cn/img_convert/aa4d9bfb073805e479464b455e076ea1.png" alt="aa4d9bfb073805e479464b455e076ea1.png">

看到了吧，经过我们的严密的分析和预测，如果保持这个速度，Python 3.14 将比 C++ 更快。确切地说，运行完我们测试的时间为 -0.232 秒，它会在我们想要进行计算之前完成（太棒了🤣）。

下面就是免责声明的时间：

python 3.11的速度的有了很大的进步，虽然与编译语言相比还差了很多但是开发团队还在速度优化这个方向努力，所以希望Python的运行速度还有更大的进步。以上只是大佬开的一个玩笑，但上面的代码都可以在下面的链接找到，所以我们的结论还是有根据的😏
- - - - - 