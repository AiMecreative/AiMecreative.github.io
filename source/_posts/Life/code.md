---
title: 【日常】今天又是码代码的一天呢
date: 2022-10-12 10:33:32
author: Andrew-Rey
categories: Life
tags:
  - Life
  - Dairy
sticky: 100
---

"正如标题所言"

<!--more-->

# 2022年秋

## Disk上的矩阵乘法

---

10/16

discription: 由于矩阵太大, 不能一次性load进内存, 希望研究缓存大小, 对矩阵乘法效率的影响.

lang: Cpp

project: 暂未完成

---

本来以为挺简单的一个作业, 没想到这么复杂, 10%的时间在写矩阵乘法, 自以为是地写了个指定嵌套顺序的for循环, 然后发现难点在于文件的读取和写入.

**问题 1: 写入时覆盖**

由于缓存大小有限, 并且对于特定的for循环顺序, 矩阵可能需要以列的方式写入, 这时候如何定位指针的顺序?

**问题 2: 读取时返回**

意思是我需要的矩阵的绝对坐标小于此坐标在缓存上的相对坐标(即相对坐标小于0), 这时候需要返回去读取, 但是如果从头开始读取, miss hit 的数目会陡然增加, 如果从当前位置读取, 需要知道上一次指针的位置, 然而上一次的指针已经被更新了, 并且更新的时间不在同一个生命周期.

**问题 3: 以上两种情况有可能在读取和写入时都出现**

**问题 4: 写入时返回需要先读取再写入, 直到下标符合条件**


## 外部快排

---

10/9

discription: use interval heap to realize the priority double ended queue (PDEQ); use PDEQ to do external sort.

lang: Cpp

project: [ExternalQuickSort](https://github.com/Andrew-Rey/Self-Study-For-Cpp/tree/Final-task/DataStructure/ExternalQuickSort)

---

说实话还是第一次写一个六百多行的代码. 虽然不知道用六百行实现一个简单的外部快速排序是否比较能令人接受, 但我还是从中学到了很多东西.

**使用STL**

以前一般是说说要用STL比较高效, 不过自己看了一些教程以后, 也一直没有什么用武之地, 所以很多东西经常会忘. 然后这份代码里就用了很多的诸如`std::deque`, `std::vector`等一些简单的STL, 当然, 期间还用了一些`std::priority_queue`, 但是发现并不能实现自己的目标 (能以$O(1)$效率返回最大值和最小值), 所以就基于`std::deque`做了一个interval heap.

**官网DOC**

以前不太习惯在[这里](https://cplusplus.com/)参考资料, 但是终于对网上那些复制粘贴的, 没有思考的blog忍无可忍了, 于是转身求助官网.

**CMake**

之前自己学了CMake, 这次终于用上了. yysy, CLion的CMake及时更新还挺好的.

**Main**

说说主要内容.

这里主要是针对内存大小有限, 希望能对硬盘上的大量数据排序.

- 人为定义宏来规定当前的内存大小 (只关心待排序的数据, 不考虑中间变量)
- 将内存划分为 Input, Small, Large 和 Middle 四个区. Middle 相当于快排里的pivot, 然后递归对Small和Large排序, 这里使用循环+栈的方式实现递归.
- 文件读写, 我认为的本项目最繁琐的操作之一. 因为当缓冲区满了以后, 再次写入时, 可能需要保留上一次写入的末尾位置, 所以我新定义了一个栈用来存末尾指针.