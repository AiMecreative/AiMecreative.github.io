---
title: 【操作系统】Mutual Exclusion
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

## 在共享内存上实现互斥

假设：存在`load`和`store`，前者表示只能`load`看当前变量的值，并且不做任何其他操作；后者表示只能`store`，不能同时去读

### 自旋锁spin lock

原子指令`lock`，在汇编指令的前面加上`lock`前缀。
如下面的代码：原子地改变`addr`的值。
```c
int xchg(volatile int *addr, int newval){
    int result;
    asm volatile("lock xchg %0, %1": "+m"(*addr), "=a"(result) : "1"(newval));
    return result;
}
```

有`stdatomic.h`（C++）

> **自旋协议**
>
> 前提是硬件支持原子操作（原子地读写）
>
> - 有两把锁，一把公用的锁（A），每个线程有一把私有的锁（Bn）
> - 当某个线程需要访问公用资源的时候，交换公有和私有的锁（此时交换操作是原子的）
> - 交换后其他线程发现公用的锁不是预期值，即使与私有的锁交换，也无法进入临界区
> - 直到线程退出临界区将公用的锁返回
> - 每一个线程内部都有循环判断锁的值的代码

```c
int table = YES;

void lock() {
retry:
  int got = xchg(&table, NOPE);
  if (got == NOPE) // spin
    goto retry;
  assert(got == YES);
}

void unlock() {
  xchg(&table, YES)
}
```

```c
int locked = 0;
void lock() { while (xchg(&locked, 1)) ; }
void unlock() { xchg(&locked, 0); }
```
> 其中`xchg`函数是硬件支持的原子操作（见上方）

> 操作系统内部保证所有带有`lock`的指令可以顺序执行，保证执行某个带有`lock`的指令时，前面所有共享内存是可见的

> RISC-V的Load-Reserved/Store-Conditional
> 
> - LR：标记，对共享变量的标记，当共享变量被改变时，标记消失
> - SC：当标记还在的时候才可以写入

### 互斥锁Mutex Lock

> **自旋锁的缺陷**
>
> - 性能问题0：共享变量会触发处理器间的缓存同步，延迟增加
> - 性能问题1：除了进入临界区的线程，其他处理器的线程都在空转；争抢锁的处理器越多，利用率越低
> - 性能问题2：获得自旋锁的线程可能被OS系统切换出去，实现100%的资源浪费（好耶！
>
> 自旋锁的使用场景：操作系统内核的并发数据结构（短临界区）
>
> - 临界区几乎不拥堵
> - 持有自旋锁时禁止执行流切换

> **实现长临界区的互斥**
>
> - 由于C代码只能做计算，所以让操作系统来实现

```c
// 试图获得 lk，但如果失败，就切换到其他线程
syscall(SYSCALL_lock,&lk);
// 释放 lk，如果有等待锁的线程就唤醒
syscall(SYSCALL_unlock, &lk);
```

> OS用自旋锁确保自己读写锁的过程是原子的

### Futex=Spin+Mutex(Fast Userspace Mutex)

(关于自旋锁的一些分析（有关fast path & slow path）)[https://jyywiki.cn/OS/2022/slides/5.slides#/4/1]

futex可以保证绝大多数情况下不进入内核


