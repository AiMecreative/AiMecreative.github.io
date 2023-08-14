---
title: 【操作系统】Process
date: 2023-06-28 21:48:58
tags:
  - CS
  - OS
  - NJU
categories: CS
author: Andrew-Rey
mathjax: true
---


<!--more-->

## 进程

> 进程状态机模型和线程状态机模型的对比
>
> - 线程状态机共享内存，但进程状态机有独立的内存，不共享内存
> - 二者都有独立的堆栈和寄存器

> 操作系统是状态机的管理者，同时保存多个状态机（虚拟化）
>
> - 特殊的系统调用来管理状态机：`CreateProcess()`, `TerminateProcess`

> 每个线程都只能看见自己的内存部分，看不到其它线程的内存空间。
>
> - 虚拟存储系统
> - 通过虚拟内存实现每次“拿出来一个执行”
> - 中断后进入操作系统代码，“换一个执行”

> 操作系统本身也可以看作是一个状态机
>
> - 有自己的内存等等
> - 在操作系统完成初始化后，只有一个init进程被启动
> - 在创建出来init进程后，操作系统变成了一个中断和系统调用的处理程序
> - 其余的所有进程都由init进程创建出来

> `fork`：创建状态机
>
> - UNIX做一份状态机完整的复制（内存，寄存器现场）
> - `int fork();`：新创建进程返回0，执行fork的进程返回子进程的进程号
> - 复制失败（内存不够），返回-1
> - 所有的东西，包括库函数，自己malloc的内存，数据都会被复制

> 进程树`pstree`

> reset状态机：`execve`：`int execve(const char* pathname, char* const argv[], char* const envp[]);`，`argv`是函数的参数，`envp`是环境变量，对应了`main`的参数
> execute the program refferred to by pathname
> - 将当前进程重置成一个可执行文件描述状态机的初始状态，可以是二进制文件，c文件
> - `execve`是唯一能执行程序的系统调用，也是一切进程strace的第一个系统调用

> 环境变量：
> `env`查看
> - 在创建子进程时默认继承父进程的环境变量
> - `export`可以修改环境变量
> - `PATH`修改可执行文件的搜索路径

> 销毁状态机：`void _exit(int status)`
> 立即销毁当前状态机，并允许有返回值
>
> - `exit()`(clib)
> - `_exit()`
> - `__exit()`
> - `exit_gourp()`