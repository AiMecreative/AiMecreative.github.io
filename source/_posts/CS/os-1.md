---
title: 【操作系统】Overview
date: 2023-05-17 00:28:22
tags:
  - OS
  - CS
  - NJU
categories: CS
mathjax: true
author: Andrew-Rey
---

"计算机三大浪漫之一"

<!--more-->

## 什么是操作系统

> A body of software, in fact, that is responsible for making it easy to run programs (even allowing you to seemingly run many at the same time), allowing programs to share memory, enabling programs to interact with devices, and other fun stuff like that. (OSTEP)

### 操作系统是如何从一开始变成这样的

三个线索

- 计算机（硬件）
- 程序（软件）
- 操作系统（管理软件的软件）
  - 对单一计算机硬件系统作出抽象、支撑程序执行的软件系统（狭义）

> 1940s：**第一台计算机**
>
> - 计算机系统 = 状态机
> - 标准的Mealy型数字电路（ENIAC-1946-2-14）
>   - 延迟线存储器
>   - 图灵机
>   - 没有操作系统（运行程序需要接线，对，物理意义的接线）
>
> 1950s：更快更小的逻辑门，磁芯内存，IO设备（1953年出现中断）
>
> 1957：Fortran
>
> - 操作系统的概念开始形成：管理多个程序依次排队运行的库函数和调度器，需求是多用户排队共享计算机
>   - 操作（operate）任务（jobs）的系统（system）
>   - 批处理系统 = 程序的自动切换（换卡）+ 库函数API
>   - DISK Operating System (DOS)：开始出现设备，文件，任务等对象和API
>
> 1960s：集成电路，总线开始出现，更大的内存（支持把多个程序一起放在内存里）
>
> - 能同时载入多个程序到内存且灵活调度它们的管理程序，包括程序可以调用的API
> - 有了进程（progress）的概念
> - 进程执行IO时，将CPU让给其他进程：在多个地址空间隔离的程序之间切换
>
> 既然操作系统可以实现程序的切换，不如让它们能够定时切换
>
> - 基于中断机制：使程序在执行时，异步地插入函数调用，由操作系统决定（调度策略）是否应该切换到另一个程序执行
> - Multics(MIT,1965):现代操作系统诞生
>
> 1970s+：集成电路空前发展，PC，CISC, 中断，IO，异常，MMU，网络，PASCAL, C
>
> - 分时系统成熟，UNIX（单用户系统）诞生和完善
> - 1973：管道（对象），信号API，grep（应用程序）
> - 1983：BSD socket（对象）
> - 1984：procfs（对象）
> - UNIX衍生家族：1BSD, GNU, MacOS, Minix, Windows, Linux0.01...