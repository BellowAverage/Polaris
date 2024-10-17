
--- 
title:  【python】cffi 在 Python 代码中调用 C 代码 
tags: []
categories: [] 

---
`cffi`（C Foreign Function Interface）是 Python 中的一个库，它提供了一种在 Python 代码中调用 C 代码的方法。通过 `cffi`，你可以编写 Python 代码来直接使用 C 函数、调用共享库（.so 或 .dll 文件），或者甚至嵌入 C 代码。这使得在 Python 中执行低级系统调用或利用现有的 C 代码库变得更加容易和高效。

#### 安装 cffi

在大多数情况下，你可以通过 pip 来安装 `cffi`：

```
pip install cffi

```

确保你的环境中已经安装了 Python 的开发版本和 C 编译器，因为 `cffi` 在安装时可能需要编译一些扩展。

#### 使用 cffi

`cffi` 提供了两种主要的使用模式：
1.  **ABI 模式**（Application Binary Interface）：这种模式允许你直接调用二进制共享库中的函数，不需要额外的 C 源代码。这种方式简单快捷，但可能不如 API 模式那样灵活。 1.  **API 模式**（Application Programming Interface）：这种模式需要你提供 C 函数的声明。`cffi` 会利用这些信息来生成 Python 访问这些函数的接口。API 模式提供了更高的灵活性和安全性，因为它允许 `cffi` 检查类型等信息。 
#### 示例

##### ABI 模式示例

假设你有一个名为 `libexample.so`（Linux）或 `libexample.dll`（Windows）的共享库，其中包含以下函数定义：

```
// C code
int add(int a, int b) {<!-- -->
    return a + b;
}

```

你可以使用 `cffi` 的 ABI 模式来调用这个函数：

```
from cffi import FFI

ffi = FFI()

# 加载共享库
lib = ffi.dlopen("libexample.so")  # 或 "libexample.dll" 在 Windows 上

# 定义要使用的函数原型
ffi.cdef("int add(int, int);")

# 调用函数
result = lib.add(2, 3)
print(result)

```

##### API 模式示例

如果你想使用 API 模式，你需要提供 C 代码的源文件。假设同样的 `add` 函数，你可以这样做：

```
from cffi import FFI

ffi = FFI()

# 定义 C 函数的声明
ffi.cdef("int add(int a, int b);")

# 提供 C 函数的实现（通常是作为字符串）
source = """
    int add(int a, int b) {
        return a + b;
    }
"""

# 创建一个新的模块，包含上述 C 代码
ffi.set_source("_example", source)

# 编译并加载模块
ffi.compile()
from _example import lib

# 调用函数
result = lib.add(2, 3)
print(result)

```

在 API 模式中，`ffi.set_source()` 第一个参数是生成模块的名称，第二个参数是包含 C 代码的字符串。`ffi.compile()` 将编译这些 C 代码，并生成一个 Python 模块，你可以像导入任何其他 Python 模块一样导入它。

#### 总结

`cffi` 是一个强大的工具，它提供了一种在 Python 中使用 C 代码的有效途径。无论是调用现有的 C 库，还是为你的 Python 项目编写新的 C 扩展，`cffi` 都是一个值得考虑的选项。
