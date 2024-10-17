
--- 
title:  C++通过Makefile定义宏参数，传入程序 
tags: []
categories: [] 

---
严格来说应该是通过C++编译工具g++ -D 参数传递宏参数，下面我们来一起操作起来

### 1.main.cpp编写

```
#include &lt;iostream&gt;

using namespace std;

int main(int argc, char **argv) 
{<!-- -->
	cout &lt;&lt; "version:" &lt;&lt; VERSION &lt;&lt; endl; 
	return 0;
}

```

### 2.Makefile编写

```
# 字符串需要加双引号""定义
BRANCH="$(shell git rev-parse --abbrev-ref HEAD)" # git分支号
COMMIT="$(shell git log --pretty=format:"%h" -1)" # git提交号
VER="$(BRANCH)-$(COMMIT)"

all:
	g++ -DVERSION="\$(VER)\" -o version version.cpp 

clean:
	rm -fv *.o

```

### 3.编译与运行测试

```
➜  version git:(master) ✗ make  # 编译                                     
g++ -DVERSION="\""master" -"e07bca1" "\" -o version version.cpp 
➜  version git:(master) ✗ ./version    # 运行可执行文件                               
version:master-e07bca1  # 获得git分支和版本号

```
