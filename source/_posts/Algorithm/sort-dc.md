---
title: 【算法】排序和分治
date: 2023-05-30 14:53:03
tags:
  - CS
  - Algorithm
  - NJU
categories: CS
author: Andrew-Rey
mathjax: true
---

"一个小tutorial"

<!--more-->

## BF

**<u>冒泡排序的改进</u>**

```4，3，2，1，5，6，7，8，9```

- 当考虑元素4时，从元素5以后不再交换。
- 改进：记录最后一次发生交换的位置，下次比较时到此结束
- 对于阶数有无改进：
  - 从 **inversion** 的角度：每次比较能消除多少对inversion。改进后消除inversion的速度没有改变。

## QS

**<u>快排的平均时间复杂度</u>**

分析输入$\{a_1,a_2,\cdots,a_n\}$，定义随机变量$X_{ij}=\{a_i\ compared\ with\ a_j\}$，则平均时间复杂度为$\sum_{1\leq i < j \leq n}E[X_{ij}]$。但具体的概率不易知（由于输入是随机输入）。但计算概率时只需要 **遍历所有的发生比较的pair即可**。选取 **有序** 输入，重新分析：输入$Z_1<Z_2<\cdots <Z_n$，对于快排，选取下标为$idx$的元素作为pivot，对于任意$idx<i$，对$Z_i$是否与$Z_j$发生比较没有影响，而选取$i<idx<j$时，二者不发生比较，只有选择$idx=i\ or\ idx=j$时，二者才能进行比较，因此

$$E[X_{ij}]=\frac{2}{j-i+1}$$

$$\sum_{i}\sum_{j}E[X_{ij}]=\sum_{i}\sum_{j}\frac{2}{j-i+1}$$