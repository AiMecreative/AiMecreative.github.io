---
title: 【CG】GAMES101-Rasterization-1
date: 2023-03-17 09:55:46
tags:
- CS
- CG
- GAMES101
categories: CS
author: Andrew-Rey
---

"看上去是对的，那就是对的"

<!--more-->

> 在进行 Viewing Transformation 后, 所有的物体都变换到了 $[-1,1]^3$ 中

> **几个概念**
>
> - 垂直视角 Field of View
> - 宽高比 aspect ratio
>
> ![几个概念](Rasterization-1/aspect.png)

### 视口变换 Viewport Transformation

> **屏幕建模**
>
> - 像素的二维数组
> - 数组的大小称为分辨率
> - 光栅成像设备 (将物体画在屏幕上)

> **屏幕空间**
>
> - 由不同的定义方式
> - 坐标的原点在 **数组的左下角**
> - 向右为$x$轴, 向上为$y$轴
> - 像素的中心为$(x+0.5,y+0.5)$

> **视口变换**
>
> - 将 $[-1,1]^3$ 变换到屏幕 $[0,width]\times[0,height]$ 上
> - 先考虑$xy$两个维度, 不考虑$z$的深度, 变换矩阵为
> 
> $$
> M=
> \begin{bmatrix}
>     \frac{width}{2} & 0 & 0 & \frac{width}{2}  \\
>     0 & \frac{height}{2} & 0 & \frac{height}{2} \\
>     0 & 0 & 1 & 0 \\
>     0 & 0 & 0 & 1
> \end{bmatrix}
> $$

### 光栅化 Rasiterization

> **三角形**
>
> - 最基本的多边形, 所有多边形可以拆分成三角形
> - 唯一确定一个平面
> - 能定义三角形的内外
> - 能比较好地在顶点间进行插值
