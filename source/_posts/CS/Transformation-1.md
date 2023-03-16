---
title: 【CG】GAMES101-Transformation-1
date: 2023-03-14 23:46:52
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

### 缩放 scale

![scale-1](scale-1.png)

> **缩放矩阵**

$$
\begin{bmatrix}
    x^{\prime} \\
    y^{\prime}
\end{bmatrix}=
\begin{bmatrix}
    s_x & 0 \\
    0 & s_y
\end{bmatrix}
\begin{bmatrix}
    x \\
    y
\end{bmatrix}
$$

### 切变 shear

![shear-1](shear-1.png)

> 原点水平方向移动为 $0$
> 左上角水平方向移动为 $a$
> 纵向不移动

> **切变矩阵**

$$
\begin{bmatrix}
    x^{\prime} \\
    y^{\prime}
\end{bmatrix}=
\begin{bmatrix}
    1 & a \\
    0 & 1
\end{bmatrix}
\begin{bmatrix}
    x \\
    y
\end{bmatrix}
$$

### 旋转 rotation

![rotate-1](rotate-1.png)

> 默认逆时针旋转为正

> **旋转矩阵**

$$
\begin{bmatrix}
    x^{\prime} \\
    y^{\prime}
\end{bmatrix}=
\begin{bmatrix}
    cos(\theta) & -sin(\theta) \\
    sin(\theta) & cos(\theta)
\end{bmatrix}
\begin{bmatrix}
    x \\
    y
\end{bmatrix}
$$

### 齐次坐标 homogeneous coordinates

> 平移 translation
> 非线性

![translation-1](translation-1.png)

> **仿射变换**

$$
\begin{bmatrix}
    x^{\prime} \\
    y^{\prime}
\end{bmatrix}=
\begin{bmatrix}
    a & b \\
    c & d
\end{bmatrix}
\begin{bmatrix}
    x \\
    y
\end{bmatrix}+
\begin{bmatrix}
    t_x \\
    t_y
\end{bmatrix}
$$

> 增加维度$\rightarrow$**齐次坐标**:
>
> - 二维点表示: $(x,y)\rightarrow(x,y,1)$
> - 二维向量表示: $(x,y)\rightarrow(x,y,0)$

> **齐次坐标的平移矩阵**

$$
\begin{bmatrix}
    x^{\prime} \\
    y^{\prime} \\
    w^{\prime}
\end{bmatrix}=
\begin{bmatrix}
    1 & 0 & t_x \\
    0 & 1 & t_y \\
    0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
    x \\
    y \\
    1
\end{bmatrix}=
\begin{bmatrix}
    x+t_x \\
    y+t_y \\
    1
\end{bmatrix}
$$

> **注意表示点的时候第三维是1**

$$
\begin{bmatrix}
    x^{\prime} \\
    y^{\prime} \\
    w^{\prime}
\end{bmatrix}=
\begin{bmatrix}
    a & b & t_x \\
    c & d & t_y \\
    0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
    x \\
    y \\
    1
\end{bmatrix}
$$

> **只有二维仿射变换, 最后一行才是$(0,0,1)$**

> 齐次坐标表示下, 先进行线性变换, 再平移

### 组合 composition

> **左乘**变换矩阵表示在上一次变换的结果上进行变换

### 逆 inverse

变换的逆即矩阵的逆

> **旋转的逆**

旋转$\theta$角度

$$
R_{\theta}=
\begin{bmatrix}
    cos(\theta) & -sin(\theta) \\
    sin(\theta) & cos(\theta)
\end{bmatrix}
$$

旋转$-\theta$角度

$$
R_{-\theta}=
\begin{bmatrix}
    cos(\theta) & sin(\theta) \\
    -sin(\theta) & cos(\theta)
\end{bmatrix}
$$

可以发现 $R_{-\theta}=R_{\theta}^T$, 满足 **正交性**

### 三维情况

> **齐次坐标**
>
> - 点: $(x,y,z,1)^T$
> - 向量: $(x,y,z,0)^T$

> **绕轴旋转**

$$
R_x=
\begin{bmatrix}
    cos(\alpha) & -sin(\alpha) & 0 & 0 \\
    sin(\alpha) & cos(\alpha) & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
\end{bmatrix}\quad
R_y=
\begin{bmatrix}
    cos(\alpha) & 0 & sin(\alpha) & 0 \\
    0 & 1 & 0 & 0 \\
    -sin(\alpha) & 0 & cos(\alpha) & 0 \\
    0 & 0 & 0 & 1
\end{bmatrix}\quad
R_z=
\begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & cos(\alpha) & -sin(\alpha) & 0 \\
    0 & sin(\alpha) & cos(\alpha) & 0 \\
    0 & 0 & 0 & 1
\end{bmatrix}\quad
$$

> **三维任意旋转**
>
> - 欧拉角 Euler Angle: 绕$x, y, z$轴旋转的角度分别为$\alpha, \beta, \gamma$

> **Rodrigues' Rotation Formula**
>
> - 给定旋转轴$n$和旋转角度$\alpha$
> - 注意: 旋转轴的起点默认为 **原点**
> - 若旋转轴起点不在原点, 则平移至原点, 变换后再平移至原处

$$
R(n, \alpha)=cos(\alpha)I+(1-cos(\alpha))nn^T+sin(\alpha)
\begin{bmatrix}
    0 & -n_z & n_y \\
    n_z & 0 & -n_x \\
    -n_y & n_x & 0
\end{bmatrix}
$$

> [如何证明](https://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula)

