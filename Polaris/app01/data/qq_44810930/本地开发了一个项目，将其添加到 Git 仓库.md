
--- 
title:  本地开发了一个项目，将其添加到 Git 仓库 
tags: []
categories: [] 

---
>  
 **背景** 如果你已经在本地开发了一个项目，但尚未将其添加到 Git 仓库 现在要将其添加至远程git仓库 




#### 文章目录
- - 


## 详细步骤
1.  **打开终端：** 打开终端或命令提示符窗口，进入你的项目所在的目录。 <li> **初始化 Git 仓库：** 使用以下命令在项目目录下初始化一个新的 Git 仓库： <pre><code class="prism language-bash">git init
</code></pre> 这将在你的项目目录中创建一个隐藏的 `.git` 目录，用于存储 Git 的配置和版本信息。 </li><li> **添加文件到暂存区：** 使用以下命令将你的项目文件添加到 Git 暂存区： <pre><code class="prism language-bash">git add .
</code></pre> 这将添加所有未跟踪的文件到暂存区。如果你只想添加特定的文件，可以将 `.` 替换为文件名。 </li><li> **提交到本地仓库：** 使用以下命令将暂存区的文件提交到本地仓库： <pre><code class="prism language-bash">git commit -m "Initial commit"
</code></pre> 这将创建一个新的本地提交，并添加一条提交消息，描述你的初始提交。 </li>1.  **创建远程仓库（如果没有）：** 如果你想将项目推送到远程仓库（如 GitHub、GitLab 等），首先在远程仓库中创建一个新的仓库。 <li> **将本地仓库关联到远程仓库：** 使用以下命令将本地仓库关联到远程仓库。替换 `&lt;remote-url&gt;` 为你的远程仓库 URL。 <pre><code class="prism language-bash">git remote add origin &lt;remote-url&gt;
</code></pre> </li><li> **推送到远程仓库：** 使用以下命令将本地提交推送到远程仓库： <pre><code class="prism language-bash">git push -u origin master
</code></pre> 这将把本地的 `master` 分支推送到远程仓库。 </li>
## 在gitee上申请仓库

```
https://gitee.com/projects/new

```

<img src="https://img-blog.csdnimg.cn/direct/2e26d8b2fde9439c91ab80ec0df2ee9e.png" alt="在这里插入图片描述"> 创建成功后, 在下面找到

```
git remote add origin  ....

```
