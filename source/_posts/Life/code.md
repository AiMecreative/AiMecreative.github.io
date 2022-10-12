---
title: 今天又是码代码的一天呢
index_img: /index_imgs/code.png
date: 2022-10-12 10:33:32
categories: Life
mathjax: true
---

"正如标题所言, 今天又是写代码的一天呢"

"哈哈"

<!--more-->

# 2022年秋

## 外部快排

{%note info%}
10/9

discription: use interval heap to realize the priority double ended queue (PDEQ); use PDEQ to do external sort.

project: [ExternalQuickSort](https://github.com/Andrew-Rey/Self-Study-For-Cpp/tree/Final-task/DataStructure/ExternalQuickSort)
{%endnote%}

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