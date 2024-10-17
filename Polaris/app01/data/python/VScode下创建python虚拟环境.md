
--- 
title:  VScode下创建python虚拟环境 
tags: []
categories: [] 

---
**1. 安装了VSCode**：确保你已经安装了Visual Studio Code。你可以从并安装。

**2. 安装了python**：确保你的计算机上安装了Python。你可以从下载并安装。

**3. 安装Python插件**：打开VSCode，在扩展（Extensions）市场中搜索并安装Python插件。此插件为VSCode提供了与Python相关的功能。

**4. 创建项目文件夹**：在你的计算机上创建一个新的文件夹，作为你的Python项目的根文件夹。

**5. 打开项目文件夹**：在VSCode中打开你的项目文件夹。你可以使用"文件" &gt; "打开文件夹"或直接在终端中使用`code .`命令。

**6. 创建虚拟环境**：打开终端（Terminal）并运行以下命令来创建一个虚拟环境。选择一个你喜欢的虚拟环境管理器，如`venv`或`virtualenv`。在这里，我将使用`venv`：

```
python -m venv venv
```

        ## python -m venv &lt;虚拟环境的命名，自己取&gt;

**7. 激活虚拟环境**：在终端中运行以下命令来激活虚拟环境：

      &gt; 在windows上：

```
.\venv\Scripts\activate
```

       &gt;在macOS/Linux上：(本人未测试）

```
source venv/bin/activate
```

你的终端提示符应该会变成虚拟环境的名称。

**8. 安装依赖**：在虚拟环境激活状态下，使用以下命令安装你的项目所需的依赖：

```
pip install package_name
```

         &gt;将`package_name`替换未你需要的实际依赖。

         &gt;"依赖" :一个软件项目在运行或构建时所依赖的外部库、模块或其他组件。在Python项目&gt;&gt;  中，通常会将依赖列在一个特殊的文件中，例如`requirements.txt`。这个文件包含了项目的所有依赖信息，包括库的名称和版本号。这样其他开发者或部署工具可以根据这个文件来安装必需的依赖。

**9. 配置VSCode使用虚拟环境**：确保VSCode使用了正确的虚拟环境。按下`Ctrl + Shift + P`，然后输入"Python: Select Interpreter"，选择你的虚拟环境。

现在，你的VSCode项目应该已经配置好了Python虚拟环境。你可以在VSCode中运行和调试你的Python代码，并确保项目的依赖项被正确管理。



## # 遇到的错误：

>  
 因为在此系统上禁止运行脚本。有关详细信息，请参阅 https:/go.microsoft.com/fwlin k/?LinkID=135170 中的 about_Execution_Policies。 所在位置 行:1 字符: 1 + activate + ~~~~~~~~ + CategoryInfo : SecurityError: (:) []，PSSecurityException + FullyQualifiedErrorId : UnauthorizedAccess 


 这个错误是由于 PowerShell 执行策略限制导致的。在 Windows 上，默认情况下，PowerShell 的执行策略是 Restricted，不允许运行脚本。为了解决这个问题，你可以选择修改 PowerShell 的执行策略或者使用其他方法激活虚拟环境。

#### 修改 PowerShell 执行策略：(未验证）

##### **注意：请注意执行以下步骤可能会增加系统的安全风险。请仔细了解执行策略的影响，并谨慎操作。**

1. 以管理员身份打开 PowerShell。

2. 运行以下命令来修改执行策略：

```
Set-ExecutionPolicy RemoteSigned
```

         如果系统提示是否更改执行策略，请输入 `Y` 确认。

3. 运行 `activate` 命令再次激活虚拟环境。

        **重要提示：** 修改执行策略是一种权衡，因为它可能会增加系统的安全风险。在完成任务后，建议将执行策略恢复为更加安全的状态：

```
Set-ExecutionPolicy Restricted

```

#### 使用其他方式激活虚拟环境：

如果你不想修改执行策略，你可以手动激活虚拟环境。在 PowerShell 中，你可以使用以下命令：

```
./venv/Scripts/Activate

```

请注意，路径分隔符在 Windows 上是 `\`，而在 Linux 或 macOS 上是 `/`。确保在 PowerShell 中使用正确的路径分隔符。






