---
title: 【操作系统】Concurrency Program
date: 2023-05-23 10:38:21
tags:
  - CS
  - OS
  - NJU
categories: CS
author: Andrew-Rey
mathjax: true
---

"计算机的三大浪漫之一"

<!--more-->

## 如何理解并发程序的执行

> 也就是画状态机：把所有可能状态都画出来

> **<u>互斥mutual exclusion</u>**： 保证两个代码不能同时执行一段代码
>
> - 假设基本操作为读写原子的，如何实现共享内存上的互斥
>
> 处理器不是原子地处理load和store的

> **<u>Peterson算法</u>（谦让）**
> 