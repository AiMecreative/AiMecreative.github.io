---
title: 【操作系统】Program
date: 2023-05-17 21:39:19
tags:
  - OS
  - CS
  - NJU
categories: CS
author: Andrew-Rey
mathjax: true
---

"计算机的三大浪漫之一"

<!--more-->

## 什么是程序

> **源代码视角**
>
> - 程序也是状态机（数字系统是状态机，程序运行在数字系统上）
> - C程序也是状态机 **应该落实到可执行的语句**
>   - 状态 = 栈 + 堆（stack frame的列表，每个frame有PC，全局变量）
>   - 初始状态：main函数执行的第一条语句，全局变量初始化
>   - 迁移：执行一条简单语句（top stack frame的PC的语句），PC++
>   - 函数调用：将栈帧压栈
>   - 函数返回：将栈帧出栈

> **二进制视角**
>
> - 还是状态机，状态 = 内存M + 寄存器R
> - 操作系统上的程序：所有的指令都只能做计算。这些指令无法使程序停下来。(M,R)->(M',R')，纯计算
> - 调用操作系统`syscall`：把（M,R）完全交给操作系统，任其修改，OS可以自己决定返回（M',R'），可以实现与操作系统中其他对象的交互：读写文件/操作系统状态，改变进程（运行中的状态机）状态（创建进程，销毁自己）
> - **程序是计算 + `syscall`**

> **如何在程序的两个视角之间切换**
>
> - 编译器Compiler：源代码S（状态机） -> 二进制代码C（状态机），C = compile(S)
> - 正确的编译（优化）：S与C的可观测行为严格一致（S中不可优化的内容在C中必须一致，包括system calls, volatile, variable loads/stores, termination）。Trivially正确的实现：直接翻译/解释执行S的语义

> **操作系统中的一般程序**
>
> - 程序 = 计算 -> system -> 计算 -> ...
> - 操作系统收编了所有的软硬件资源，只能用操作系统的允许方式访问系统的对象（能够管理多个状态机）
> - 【面试题】二进制程序状态机的第一条指令是什么（一个简单的Hello World C程序执行的第一条指令在哪里。）：用gdb -> `starti`，或者查看进程信息`info proc {mappings}`（因为它也是状态机，所以有OS给的初始状态）（如果想改的话就去改elf二进制文件）
> - 【面试题】main函数在执行前、中、后发生了哪些操作系统的API调用。用`trace`（linux里面的工具是`strace`）可以查看system call，当然第一句是execve。本质上所有的程序和HelloWorld类似：
>   - 被OS加载：通过另一个进程执行execve设置为初始状态
>   - 状态机执行：进程管理（fork, execve, exit, ...），文件/设备管理（open, close, read, write, ...），存储管理（mmap, brk, ...）
>   - 直到 _exit(exit_group)退出
