---
title: 操作系统练习
index_img: /index_imgs/os2.jpg
date: 2022-05-09 16:35:18
category: CS
mathjax: true
---

"操作系统习题, 包括进程同步, CPU调度等内容."

"还在更新...也有可能不在更新..."

<!--more-->

# 进程同步与互斥

### 习题1
哲学家进餐问题: 问题描述见[操作系统笔记](https://andrew-rey.github.io/2022/04/19/OS/).

**解法1**: 最多允许 4 个哲学家同时进餐, 以保证至少有一个哲学家可以正常用餐, 并且最终可以释放出其使用的筷子, 从而使给多的哲学家用餐.

```C++
semaphore choopsticks[5] = {1, 1, 1, 1, 1};
semaphore room = 4;

void philosopher(int i) {
    do {
        think();
        wait(room);
        wait(chopsticks[i]);
        wait(chopsticks[(i + 1) % 5]);
        eat();
        signal(chopsticks[(i + 1) % 5]);
        signal(chopsticks[i]);
        signal(room);
    } while(1);
}
```

**解法2**: 将拿一双筷子作为一个 **原子操作**.

```C++
semaphore mutex = 1;  // 将一双筷子视作资源, 表示当前是否有人在拿筷子
semaphore chopsticks[5] = {1, 1, 1, 1, 1};

void philosopher(int i) {
    do {
        think();
        wait(mutex);  // 申请拿筷子的权限
        wait(chopsticks[(i + 1) % 5]);
        wait(chopsticks[i]);
        signal(mutex);
        eat();
        signal(chopsticks[(i + 1) % 5]);
        signal(chopsticks[i]);
    } while(1);
}
```

**解法3**: 规定奇数的哲学家先拿左边的筷子, 再拿右边的筷子; 偶数的哲学家先拿右边的筷子再拿左边的筷子.

```C++
semaphore chopsticks[5] = {1, 1, 1, 1, 1};

void philosopher(int i) {
    do {
        think();
        if (i % 2 == 0) {
            wait(chopsticks[(i + 1) % 5]);
            wait(chopsticks[i]);
            eat();
            signal(chopsticks[(i + 1) % 5]);
            signal(chopsticks[i]);
        } else {
            wait(chopsticks[i]);
            wait(chopsticks[(i + 1) % 5]);
            eat();
            signal(chopsticks[i]);
            signal(chopsticks[(i + 1) % 5]);
        }
    } while(1);
}
```

### 习题2
**生产者消费者问题的变式:** 4 个进程 R1, R2, W1, W2 共享大小为 1 的缓冲器 B.

- R1 将输入的数放入 B 并且 **只给 W1 使用**
- R2 将输入的数放入 B 并且 **只给 W2 使用** 

分析:

- 生产者: R1, R2; 消费者: W1, W2
- R1, R2互斥, R1&W1, R2&W2同步
- 只有一个空间大小: 用 empty 代替 mutex

```C++
semaphore empty = 1, full1 = 0, full2 = 0;
buffer B;

process R1() {
    do {
        int x = input();
        wait(empty);  // R1, R2 竞争权限
        B = x;
        signal(full1);  // 如果是 R2, 则改为 full2
    } while(1);
}

process W1() {
    do {
        int i;
        wait(full1);  // 如果是 W2, 则改为 full2
        i = B;
        signal(full);  // 释放资源
    } while(1);
}
```