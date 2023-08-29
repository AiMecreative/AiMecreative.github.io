---
title: 【Unity3D】反向动力学（Inverse Kinematics）
date: 2023-08-23 17:31:14
tags:
---
## FABRIK (Forward and Backward Reaching Inverse Kinematics)算法

FABRIK算法分为两个部分

- Forward Reaching
- Backward Reaching

大致而言是先根据目标位置推导各个关节的位置（Forward Reaching），若 **根关节点** 发生了位移，则需要进行Backward Reaching，也就是 **在正向的基础上** 将根关节点移动至原位置，逐一更改其它关节点。重复该步骤，直到最末的关节点距离目标位置小于某个阈值。

> 在IK的过程中需要注意的点
>
> - IK中 **根关节的位置保持不变**
> - 对于一个特定的目标位置，**求解的关节位置有多个**
