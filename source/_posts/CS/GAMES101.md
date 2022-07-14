---
title: GAMES101
date: 2022-07-09 10:35:39
category: CS
mathjax: true
---

"From GAMES101"

<!--more-->

# Transformation
## **Basic**
### Scale

$$
\left [ \begin{aligned}
    x^{\prime} \\
    y^{\prime}
\end{aligned} \right ]
= 
\left [ \begin{aligned}
    &s_x\ \ &0 \\
    &0\ \ &s_y
\end{aligned} \right ]
\left [ \begin{aligned}
    x \\
    y
\end{aligned} \right ]
$$

### Rotation
Rotation:

$$
R_{\theta} = 
\left [ \begin{aligned}
    x^{\prime} \\
    y^{\prime}
\end{aligned} \right ]
= 
\left [ \begin{matrix}
    &cos\theta\ \ &-sin\theta \\
    &sin\theta\ \ &cos\theta
\end{matrix} \right ]
\left [ \begin{aligned}
    x \\
    y
\end{aligned} \right ]
$$

inverse rotation:

$$
R_{-\theta} = 
\left [ \begin{aligned}
    x^{\prime} \\
    y^{\prime}
\end{aligned} \right ]
= 
\left [ \begin{matrix}
    &cos\theta\ \ &sin\theta \\
    &-sin\theta\ \ &cos\theta
\end{matrix} \right ]
\left [ \begin{aligned}
    x \\
    y
\end{aligned} \right ]
= R_{\theta}^{-1}
= R^T
$$

3-D:
Eular angle: rotation around axises. The rotation is similar to 2-D, but inverse for axis y.

For a general rotation around an axis vector $n$, Rodrigues' Rotation Formula:

$$
R(n, \alpha) = cos\alpha I + (1 - cos\alpha)n n^T + sin\alpha 
\left [ \begin{matrix}
    &0 &-n_z &n_y \\
    &n_z &0 &-n_x \\
    &-n_y &n_x &0
\end{matrix} \right ]
$$

其中

$$
\left [ \begin{matrix}
    &0\ \ &-n_z\ \ &n_y \\
    &n_z\ \ &0\ \ &-n_x \\
    &-n_y\ \ &n_x\ \ &0
\end{matrix} \right ]
$$

是叉积算子, 物理含义为角速度

For an arbitrary axis, do a translation (following).

### Homogeneous coordinates
$$
x_1 = x + t_x \\
y_1 = y + t_y
$$

solution:

**point:** $(x, y, 1)^T$

**vector:** $(x, y, 0)^T$

$$
\left [ \begin{aligned}
    x^{\prime} \\
    y^{\prime} \\
    w
\end{aligned} \right ]
= 
\left [ \begin{aligned}
    &1\ &0\ &t_x \\
    &0\ &1\ &t_y \\
    &0\ &0\ &1
\end{aligned} \right ]
\left [ \begin{aligned}
    x \\
    y \\
    1
\end{aligned} \right ]
=
\left [ \begin{aligned}
    x + t_x \\
    y + t_y \\
    1
\end{aligned} \right ]
$$

for a general form:

$$
\left [ \begin{aligned}
    x \\
    y \\
    w
\end{aligned} \right ]
$$

is the same with ($w\neq 0$)

$$
\left [ \begin{aligned}
    x / w \\
    y / w \\
    1
\end{aligned} \right ]
$$

### Affine

$$
\left [ \begin{aligned}
    x^{\prime} \\
    y^{\prime}
\end{aligned} \right ]
= 
\left [ \begin{matrix}
    &a\ \ &b \\
    &c\ \ &d
\end{matrix} \right ]
\left [ \begin{aligned}
    x \\
    y
\end{aligned} \right ]
+
\left [ \begin{aligned}
    t_x \\
    t_y
\end{aligned} \right ]
$$

is the same with

$$
\left [ \begin{aligned}
    x^{\prime} \\
    y^{\prime} \\
    w
\end{aligned} \right ]
= 
\left [ \begin{matrix}
    &a\ &b\ &t_x \\
    &c\ &d\ &t_y \\
    &0\ &0\ &1
\end{matrix} \right ]
\left [ \begin{aligned}
    x \\
    y \\
    1
\end{aligned} \right ]
$$

## Viewing
MVP transformation (Model, View, Projection)

### view

Define the camera:

- position $e$
- gaze direction (look-at): $g$
- up direction: $t$

**Method: Fix the camera: origin, look-at axis -z, look-up axis y** (将相机移动到一个规定位置上)

![view](view1.png)

对应的变换, 先做平移, 再做旋转:

$$
M_{view} = R_{view}T_{view}
$$

其中平移:

$$
T_{view} = 
\left [ \begin{matrix}
    &1\ &0\ &0\ &x_e \\
    &0\ &1\ &0\ &y_e \\
    &0\ &0\ &1\ &z_e \\
    &0\ &0\ &0\ &1
\end{matrix} \right ];
$$

旋转:

$$
R_{view}^{-1} = 
\left [ \begin{matrix}
    &x_{g\times t}\ &x_t\ &x_{-g}\ &0 \\
    &y_{g\times t}\ &y_t\ &y_{-g}\ &0 \\
    &z_{g\times t}\ &z_t\ &z_{-g}\ &0 \\
    &0\ &0\ &0\ &1
\end{matrix} \right ],
R_{view} = 
\left [ \begin{matrix}
    &x_{g\times t}\ &y_{g\times t}\ &z_{g\times t}\ &0 \\
    &x_t\ &y_t\ &z_t\ &0 \\
    &x_{-g}\ &y_{-g}\ &z_{-g}\ &0 \\
    &0\ &0\ &0\ &1
\end{matrix} \right ]
$$

注意对所有物体变换.

### projection

![projection](projection.png)

**orthographic projection**

将模型 $[r, l]\times[b, t]\times[f, n]$ 转化为 $[-1, 1]\times[-1, 1]\times[-1, 1]$

$$
M_{ortho} = 
\left [ \begin{matrix}
    &\frac{2}{r-l}\ &0\ &0\ &0 \\
    &0\ &\frac{2}{t-f}\ &0\ &0 \\
    &0\ &0\ &\frac{2}{n-f}\ &0 \\
    &0\ &0\ &0\ &1
\end{matrix} \right ]
\left [ \begin{matrix}
    &1\ &0\ &0\ &-\frac{r+l}{2} \\
    &0\ &1\ &0\ &-\frac{b+t}{2} \\
    &0\ &0\ &1\ &-\frac{n+f}{2} \\
    &0\ &0\ &0\ &1
\end{matrix} \right ]
$$

**perspective projection**

分两步进行: 先将棱锥变换为长方体; 再将长方体做正交投影.

**第一步**: 保证远平面的中心不变, 远平面的 z 坐标不变, 近平面不变.

三角形相似:

$$
y^{\prime}=\frac{n}{z}y;\ x^{\prime}=\frac{n}{z}x
$$

设棱锥内任意一点 $P=(x_0,y_0,z_0,1)^T$, 经过挤压后变换为 $P^{\prime}=(x_0^{\prime},y_0^{\prime},z_0^{\prime},1)^T=(\frac{n}{z_0}x_0,\frac{n}{z_0}y_0,z_0^{\prime},1)^T=(nx_0,ny_0,z_0z_0^{\prime},z_0)^T$. 接下来确定 $z_0^{\prime}$.

取近平面的中心点 $O_1=(0,0,n,1)$ 和远平面的中心点 $O_2=(0,0,f,1)$, 变换后位置不变.

$$
O_1\Rightarrow O_1^{\prime}=(0,0,n^2,n)^T;\ O_2\Rightarrow O_2^{\prime}=(0,0,f^2,f)
$$

从而确定矩阵:

$$
M_{perp\rightarrow ortho}
\left [ \begin{matrix}
    &n\ &0\ &0\ &0 \\
    &0\ &n\ &0\ &0 \\
    &0\ &0\ &n+f\ &-nf \\
    &0\ &0\ &1\ &0
\end{matrix} \right ]
$$

**第二步**: 将变换后的长方体做正交投影 $M_{ortho}$

因此透视投影为

$$
M_{perp} = M_{ortho}M_{perp\rightarrow ortho}
$$

可以代入一些特殊点发现一些现象:

例如将中轴的中点 $P=(0,0,\frac{n+f}{2}, 1)$ 经过上述变换得 $P^{\prime}=(0,0,\frac{n^2+f^2}{n+f}, 1)$, 与此时的中轴中点 $Q^{\prime}=(0,0,\frac{n+f}{2},1)$ 比较发现, $\frac{n^2+f^2}{n+f} > \frac{n+f}{2}$, 即原来的中点应该更加 **靠近** 相机.

# Resterization

## Triangles

### Some definition

- **aspect ratio:** width / height
- **FOV, field of view:**

![def](raster1.png)

- **screen (raster)**
  - an array of pixels
  - size of the pixels: resolution (分辨率)
  - a typical kind of raster display

将raster放置在坐标系中, 并以像素的 **左下角** 作为坐标, 其像素中心则需要再加上0.5. (虎书里以中心作为坐标)

假设显示区域为 $width\times height$, 则将 viewing 后的 $[-1,1]^3$ 变换为显示区域大小 $width\times height$, 即 **视口变换 (view port)**:

$$
M_{viewport}
\left [ \begin{matrix}
    &\frac{width}{2}\ &0\ &0\ &\frac{width}{2} \\
    &0\ &\frac{height}{2}\ &0\ &\frac{height}{2} \\
    &0\ &0\ &1\ &0 \\
    &0\ &0\ &0\ &1
\end{matrix} \right ]
$$

### Triangles

将图像用三角形光栅

为什么是三角形?
  
- 最基本多边形, 任意多边形可以拆成三角形
- 保证三角形是一个平面
- 内部和外部可以定义
- 内部插值

### Samlping

连续函数离散化

$$
Sampling (x) = \left\{
    \begin{matrix}
        1,\quad x\in triangle, \\
        0,\quad x\notin triangle
    \end{matrix}
    \right.
$$

其中 $x$ 是像素**中心**

判断某个点是否在三角形内部: 设点 $P$, 三角形 $\triangle XYZ$, 分别用 $\vec{XY}, \vec{YZ}, \vec{ZX}$ 与 $\vec{XP}, \vec{YP}, \vec{ZP}$ 做外积, 若外积的结果方向一致, 则说明 $P$ 在三角形内部, 反之外部.

**Bounding Box:** 最小的包围所考虑图形的长方体. 遍历时只遍历 Bounding Box 即可. 又称轴向包围盒 (AABB)

此外, 还可以找三角形内部的, 每一行的最小和最大坐标进行遍历.

**jaggies (锯齿)**

## Antialiasing and Z-Buffering

Aliasing: artifacts to sampling

- Jagging (锯齿), sampling in space
- Moire (摩尔纹), undersampling image
- Wagon Wheel effect, sampling in time

Reason: 信号变化太快, 采样慢

Antialiasing Idea: Blurring (Pre-Filtering) before sampling (模糊处理)

![blur](sample1.png)

Aliasing 的来源: 相同采样频率采样不同函数, 得到的采样点相同.

![aliasing](sampel2.png)

大部分自然图像信号的信息集中在低频, 在变化剧烈处形成边界, 高频所代表的信息大部分是边界.

- 低通滤波器: 大面积色块
- 高通滤波器: 边界
- 带通滤波器: 不明所以的东西

注: 现实情况是**非理想**滤波.

另一个角度: **滤波** 相当于 **卷积** 或 **平均**

### Antialiasing

背景: 一般而言, 直接对原始图像进行三角形光栅化会出现明显的锯齿

减少锯齿的方法: 先对原始图像进行模糊处理, 再进行采样.

步骤: 
1. **模糊:** 用某个低通滤波器 (卷积核) 对**原始图像**进行卷积, 例如可以选择 $1\times 1$ 的低通滤波器, 卷积结果就是在每个像素的灰度平均值;
2. **采样:** 将模糊后的图像的每一个像素对像素中心进行采样

![antialiasing](sample3.png)

新的问题: **如何计算光栅三角形在每一个像素里覆盖的区域**

**MSAA, Antialiasing by Supersampling**: 将像素再进行划分, 划分为多个像素, 最后以子像素在父像素的百分比作为结果. 

- 近似 **模糊** 这一步
- 代价是更大计算量

其他抗锯齿方法: 

- FXAA (fast approximete AA)
  - 先得到带锯齿的图像, 再进行图像比对找到边界, 并将锯齿去掉
- TAA (temperal AA)
  - 复用上一帧提供的信息

其他概念:

- super resolution / super sampling
  - 将低分辨率的图像恢复为高分辨率, 依然解决的是样本不够的问题
  - DLSS (Deep Learning Super Sampling)

### Z-Buffering

**深度缓存**: 解决可见性和遮挡. 

**Painter's Algorithm**: 将场景物品的深度由远及近排序, 先画最远的物品, 再画较近物品. 其中排序所需要的时间为 $O(n log n)$

- 问题: 深度如何定义, 相互覆盖如何处理, 深度关系有时候难定义.
- 因此画家算法一般不用

**Z-Buffering Algorithm**: 在每个像素中记录当前的最小深度

- frame buffer stores color value
- z-buffer stores depth (e.i. $|z|$)

![z-buffer](zbuf1.png)

时间复杂度为 $O(n)$, 但浮点数判断相等比较复杂

### Summarize

![sum](sum1.png)

# Shading

**Def:** darkening or coloring of an illustration or diagram with parallel lines or a block of color. 

- The process of **applying a material** to an object, considering the interaction with light.
- 目前只考虑shading, 不考虑Shadow

**Other terminologies:**

- **specular light 高光**
- **diffuse reflection 漫反射**
- **ambient light 间接光照**: 简化为常量

## Blin-Phong Reflection Model

简单**漫反射**模型: 设物体表面法向量 $\vec{n}$ 与光照的 **反方向** $\vec{l}$ 夹角为 $\theta$ 且为单位向量, 则

$$
cos \theta = \vec{l} \cdot \vec{n}
$$

物体表面接收的光强与 $cos \theta$ 成正比.

设光源为点光源, 传播过程不损失能量, 球面波传播. 则由能量守恒, 距离点光源 $r$ 的球面上一点的强度为 $I/r^2$, 其中 $I$ 表示单位球壳上的能量.

因此物体的不同点的光照强度可以表示为

$$
I_p = k_d\frac{I}{r^2}max\{0,\vec{l} \cdot \vec{n}\}
$$

其中取最大是考虑: 当光线逆向射过来后**不考虑折射**.

其中 $k_d$ 表示整体的颜色影响, 当 $k_d=0$ 时表示强度为 $0$, 此时全黑. 此外, 若是RGB, $k_d$ 分别取值.

![kd](kd.png)


# Geometry

# Ray Tracing

# Animation / Simulation
