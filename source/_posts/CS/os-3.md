---
title: 【操作系统】Multi-prossesor
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

## 多处理器编程

> **<u>并发 concurrent</u>**: existing, happening, or done at the same time. In computer science, concurrency refers to the ability of different parts or units of a program, algorithm, or problem to be executed out-of-order or in partial order, without affecting the final outcome
> 
> - 有共享内存的执行流
>   - 执行流有独立的堆栈和寄存器
>   - 共享所有的内存（指针可以互相引用）
>   - 从状态机视角：每个执行流有独立的stack frames链表，但是共享全局变量和堆。处理器每次选择其中一个执行流执行（状态转移为被执行的执行流以及相应的内存发生改变，其余执行流不变）
> - 最早的并发程序：系统调用的代码（操作系统）
>
> [jyy的线程库](https://jyywiki.cn/pages/OS/2022/demos/thread.h)，编译时要加上`-lpthread`

创建一个线程：

- 入口函数是`fn`的线程，立即开始执行
- 语义：在状态机中**新增stack frame链表**并初始化为`fn(tid)`

```c++
void create(void *fn) {
  assert(tptr - tpool < NTHREAD);
  *tptr = (struct thread) {
    .id = tptr - tpool + 1,
    .status = T_LIVE,
    .entry = fn,
  };
  pthread_create(&(tptr->thread), NULL, wrapper, tptr);
  ++tptr;
}
```

等待线程结束：

- **等待**所有运行线程的`fn`返回
- 在有其他线程未执行完时死循环，否则返回（`while(other threads not return);`）

```c++
void join() {
  for (int i = 0; i < NTHREAD; i++) {
    struct thread *t = &tpool[i];
    if (t->status == T_LIVE) {
      pthread_join(t->thread, NULL);
      t->status = T_DEAD;
    }
  }
}
```

> **<u>如何理解【等待】</u>**
>
> 当某一个状态执行的线程 T1执行`join`后，后续每一个状态：若处理器选择执行 T1，则回到当前原状态，直到所有其他进程都返回了。

> 操作系统会自动把不同的线程放在不同的处理器上面，后台运行发现CPU的使用率超过100%

> **<u>证明线程会共享内存</u>**
>
> - 可以设置全局变量
>   - 如果内存是共享的，某个线程改变全局变量时，其他线程都能看到
> - 创建多个线程，线程内去修改或查看全局变量

> **<u>证明线程可以有独立的堆栈</u>**
>
> - `__thread` 可以将变量声明为 thread local 的，线程内部可见

> **<u>查看创建线程的系统调用</u>**
>
> - `strace` 
> - `clone`是用于创建线程的系统调用

> **<u>原子性</u>**：一段代码执行独占整个计算机系统
>
> - 单处理器多线程：线程运行时可能被中断，切换到另一个线程执行
> - 多处理器多线程：线程并行执行

> **<u>实现原子化</u>**
>
> - 唔...不理解