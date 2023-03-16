---
title: 【CG】GAMES101-Transformation-2
date: 2023-03-15 23:37:09
tags:
- CS
- CG
- GAMES101
categories: CS
mathjax: true
author: Andrew-Rey
---

"看上去对的, 那它就是对的"

<!--more-->

### 视图变换 View/Camera Transformstion

> 三维物体投影至相机的二维平面上
>
> - MVP变换: Model (将模型放置好), View (确定相机位置), Projection (三维投影至二维)

> **相机建模**
>
> - 位置 Position $\vec{e}$
> - 朝向 Gaze derection $\widehat{g}$
> - 向上方向 Up derection $\widehat{t}$

> **如何进行视图变换**
>
> - 只要保持所有物体和相机的相对位置不变, 相机拍摄的结果不变
> - 将相机固定 (**放在原点, 向$-z$方向看, 向上方向为$y$轴**为标准位置)
> - 其他物体进行相应变换

> **相机的变换**
>
> - $\vec{e}$平移至原点
> - $\widehat{g}$旋转至$-z$方向
> - $\widehat{t}$旋转至$y$方向

> **相机变换的矩阵形式**
>
> - **先**做平移矩阵$T$
> - **再**做旋转矩阵$R$
> - 注意旋转矩阵可以考虑 **逆旋转** 即 **坐标轴的旋转**, 将得到的矩阵求逆 (正交) 即可

> 事实上按上述变换操作后, 物体和相机都已经处于对应位置上, 称为 **ModelView Transformation**

### 投影变换 Projection Transformation

> **正交投影 Orthographic Projection**
>
> **透视投影 Perspective Projection**

![projection-1](projection-1.png)

> 透视投影假设相机为一个点, 在空间中形成一个四棱锥, 相机可以将四棱锥的两个深度间 (frustum) 的物体显示到近处的平面上
> 正交投影假设相机处于无穷远, 此时前后两个平面显示在近处平面时, 大小保持

> **正交投影通俗做法**
>
> - 相机处于标准位置
> - 将$z$坐标舍去 (即投影至$Oxy$平面)
> - 将$Oxy$的投影面变换至$[-1,1]^2$ (方便后续计算)

> **正交投影标准定义**
>
> - 将三维空间中的立方体 cube $[l,r]\times[b,t]\times[f,n]$, 映射到标准 canonical 立方体$[-1,1]^3$中
> 
> ![orthograph-1](orthograph-1.png)
>
> 这里会导致物体发生拉伸等形变, 以后还会进行视口变换(port transformation)

> **透视投影的坐标基础**
>
> - 在齐次坐标中, 每一维同乘$z(z\neq 0)$得到$(xz,yz,z^2,z)^T$表示的仍然是三维点$(x,y,z)$

> **透视投影的方法**
>
> ![perspective](perspective-1.png)
> 
> - 将 frustum 映射为 cuboid