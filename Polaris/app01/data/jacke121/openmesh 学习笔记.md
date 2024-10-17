
--- 
title:  openmesh 学习笔记 
tags: []
categories: [] 

---
**目录**



















它具有以下特征：既可以表示任意多边形网格，也可以表示纯三角形网格；点，半边，边和面的清晰表达；快速的局部区域访问，尤其是环状区域；较高的用户化性能，例如用户可以选择用户坐标类型和网格项目的存储结构，给网格添加用户自定义的元素或者函数，在运行过程用动态特性添加数据等

OpenMesh本身并不包含用于渲染图形的功能。显示三维模型，通常需要使用OpenGL或其他图形库来实现图形渲染。

### 讲解资料：





### 安装：

pip install openmesh

2024.03.10 pypi查看，最高版本支持3.9，不支持3.10

3.10安装失败报错 note: This error originates from a subprocess, and is likely not a problem with pip.   ERROR: Failed building wheel for openmesh   Running setup.py clean for openmesh Failed to build openmesh ERROR: Could not build wheels for openmesh, which is required to install pyproject.toml-based projects

### 入门例子：

#### 读取off文件示例：

```
import openmesh as om

# 读取模型
mesh = om.read_trimesh(r'D:\Desktop\bunny.off')
# 保存模型
om.write_mesh( r'D:\Desktop\bunny1.off', mesh)

print('顶点总数：', mesh.n_vertices())
print('面总数  ：', mesh.n_faces())
print('边总数  ：', mesh.n_edges())

# 遍历所有的顶点，获取每个vertex的坐标
for vertex in mesh.vertices():
    print('顶点的数据类型：', type(vertex), '顶点坐标：', mesh.point(vertex), '顶点坐标的数据类型', type(mesh.point(vertex)))
    break
# 遍历所有的边和面
for edge in mesh.edges():
    print(type(edge))
    break
for face in mesh.faces():
    print(type(face))
    break

```



#### 操作bunny.ply：

```

import openmesh as om

mesh = om.read_polymesh(r'F:\project\3d\Open3D-master\examples\test_data\Bunny.ply')
print(mesh.has_vertex_normals())    # 查找是否有法线
mesh.update_vertex_normals()    # 计算法线
print(mesh.has_vertex_normals())
print('变换前：', mesh.points()[0])
for v_it in range(mesh.n_vertices()):
    # 更新点坐标
    mesh.set_point(mesh.vertex_handle(v_it), mesh.points()[v_it] + mesh.vertex_normals()[v_it])
print('法线：', mesh.vertex_normals()[0])
print('变换后：', mesh.points()[0])
mesh.release_vertex_normals()   # 删除法线
```



### 格式转换vertex

#### vertex_to_mesh

```
import openmesh as om
import numpy as np

mesh = om.read_trimesh("mean_face.obj")
vertex = np.load("1.npy")
for i in range(6144):
    mesh.points()[i] = vertex[:, i]
om.write_mesh("1.obj", mesh)
```

#### mesh_to_vertex

```
import openmesh as om
import numpy as np

mesh = om.read_trimesh("mean_face.obj")
vertex = np.zeros((3,6144), dtype=float)
for i in range(6144):
    vertex[:, i] = mesh.points()[i]
np.save("mean_face.npy", vertex)
```


