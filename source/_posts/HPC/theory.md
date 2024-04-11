---
title: HPC | Theory Backgroud
author: Andrew-Rey
date: 2024-04-11 12:38:19
category: HPC
tag: HPC
mathjax: true
---

首先介绍并行随机访问机器（PRAM）模型是抽象的共享内存模型，其忽略了现实计算机中的开销，但可以帮助设计一些并行算法。其次是对于分布式内存模型，会介绍一些基础图论知识。接着介绍并行程序中的两大定律：Amdahl定律和Gustafson定律，用于推断并行程序加速比能达到的上限。最后以并行算法设计的Foster方法论结束。

## 并行随机访问机器模型

事实上，PRAM (Parallel Random Access Machine) 模型架构十分简单，相比于操作系统课上的一个处理器而言，PRAM拥有多个独立的处理器，每个处理器分3个阶段执行一个指令周期：

1. **读阶段**：每个处理器并发地从各自的共享内存中读取单条数据并保存到本地的寄存器中。
2. **计算阶段**：每个处理器对本地数据执行一个基本操作，并将结果存储在寄存器中。
3. **写阶段**：每个处理器并发写一条数据到共享内存中。

PRAM中的通信通过处理器在共享内存中的读写实现，该类型的内存能够以统一的方式访问，即每个处理器对内存中任意位置的访问都使用统一的**常数时间**实现，这和现实计算机很不一样（访问大规模共享内存时耗费的时间不一致）。

### PRAM的变体

在相同的指令中期中，多个处理器读写多个共享内存单元会发生冲突，为解决冲突，出现了如下的几种PRAM变体：ER (exclusive read)，EW (exclusive write)，CR (concurrent read)，CW (concurrent write)。常见的组合有三种：

- **EREW**：独占读、独占写。任意周期内，不允许多个处理器在相同的共享内存单元中进行读写。
- **CREW**：并发读、独占写。
- **CRCW**：并发读、并发写。对于并发写入，有常见的数据保留形式：
  - Priority: 处理器本身的优先级决定
  - Arbitrary: 随机选取一个处理器的值写入
  - Common: 若所有的值都相等则写入，否则内存位置的值不变
  - Combining: 通过某种运算组合所有的冲突值再写入

### PRAM上的前缀和算法

问题描述：给定 $n$ 个数据，和一个该数据的二元运算符，假设为加法运算。在一台拥有 $p$ 个计算结点的PRAM上，并行计算前缀和。
其中数据已经存储在了共享内存 `A` 中，每个计算结点的寄存器用 `reg` 表示，目标是设计一个开销最优化的PRAM算法。

**串行分析**：使用一个计算结点求解前缀和问题

```c++
for (int i = 1; i < n; i += 1) A[i] += A[i-1];
```

计算复杂度为 $\mathcal{O}(n)$ 。

**并行分析**：使用 $p$ 个计算结点并行求解前缀和问题

当 $p=n$ 时，计算结点的数量和数据量相等，每个计算结点上处理一个数据。
可以使用分治递归的方式，将计算结点逐一合并。

```c++
//-- 算法 1 --//
// load data for every node
@parallel
for (int i = 0; i < p; i += 1) {
    reg[i] = A[i];
}

// total iteration num, merge by 2
for (int i = 0; i < ceil(log(p)); i += 1) {
    // the left nodes have been calculated
    int node_start_idx = pow(2, i);
    @parallel
    for (int j = node_start_idx; j < p; j += 1) {
        reg[j] += A[j - node_start_idx];
        A[j] = reg[j];
    }
}
```

总体的计算结构类似于二叉树：每一个结点都与左边相邻结点进行计算前缀和，第 $i$ 次迭代中，每 $2^i$ 个结点视为一个 merge 的结点，
因此一共需要 $\lceil \log_2(p) \rceil$ 次递归，即花费的时间为 $T(n,p)=\mathcal{O}(\log(p))$，
开销为 $C(n)=T(n,p)\times p=\mathcal{O}(\log(p)) \times p=\mathcal{O}(n \log(n))$，是对数线性的。

如果需要继续减小开销 $C=pT(n,p)$，则要么减小 $T(n,p)$，要么减小 $p$，降低运行时间比较困难，因此选择减少计算结点的数量 $p$，即 $p<n$ 方法如下

1. 我们有 $p<n$ 个计算结点，先将 $n$ 个数据均分到每个计算结点上，每个结点有 $n/p$ 个数据
2. 每个计算结点对本地内存的数据求解前缀和，花费的时间为 $T(n,p)=\mathcal{O}(n/p)$
3. 每个结点返回本地前缀和的最后一位结果，得到一共 $p$ 个数据
4. 对上述 $p$ 个数据执行算法1，花费的时间为 $T(n,p)=\mathcal{O}(\log (p))$，计算完成后依然得到长度为 $p$ 的前缀和 `A_p`
5. 将第4步得到的前缀和 `A_p[j]`，依次加到 `reg[j+1]` 上，`A_p` 的最后一位不用加，由于每个结点有 $n/p$ 个数据，因此花费的时间为 $T(n,p)=\mathcal{O}(n/p)$

综上所述，整个算法的时间为 $T(n,p)=\mathcal{O}(2n/p + \log (p))$，开销为 $C(n)=pT(n,p)=\mathcal{O}(2n+p\log (p))$，
当 $p=\frac{n}{\log (n)}$ 时，计算时间为对数，且开销为线性的。

```c++
//-- 算法 2 --//

// stage 1-3
// calculate prefix sum for every node
// each node contains k = n/p = log(n) data
k = n/p = log(n)
@parallel
for (int i = 0; i < p; i += 1) {
    for (int j = 1; j < k; j += 1) {
        // data index: i * num + offsets
        A[i*k+j] += A[i*k+j-1]
    }
}

// stage 4
// calculate prefix sum for rightmost values of every node
for (int i = 0; i < log(p); i += 1) {
    int node_start_idx = pow(2, i);
    @parallel
    for (int j = node_start_idx + 1; j < p; j += 1) {
        A[j*k-1] += A[(j - node_start_idx)*k-1]
    }
}

// stage 5
// add results
@parallel
for (int i = 1; i < p; i += 1) {
    // ignore the last value
    for (int j = 0; j < k-1; j += 1) {
        A[i*k+j] += A[i*k-1]
    }
}
```

### PRAM上的稀疏矩阵压缩算法

稀疏矩阵压缩算法可以利用前缀和算法。

问题描述：稀疏数组 `A` 中多个元素为 $0$，希望能通过并行算法压缩为非零数组 `V` 和对应的位置数组 `C`。

1. 构造和 `A` 等长的临时数组 `temp`，其中若 `temp[i] = 1 if A[i]!=0 else temp[i]=0`， 将数组 `A` 和临时数组 `temp` 均分到 $p=n/\log (n)$ 个计算结点上，并行生成临时数组和计算临时数组的前缀和
2. 求完前缀和的临时数组目前可以作为稀疏数组的 **地址列表**，接下来根据临时数组，并行索引 `A` 中对应地址，得到非零值和位置，写入 `V,C` 即可

分析：$T(n,p)=\theta(\log(n)), C(n)=pT(n,p)=\theta(\log(n))\times \theta(\frac{n}{\log(n)})=\theta(n)$

### 网络拓扑

互联网络的结点可能是交换机或处理器。几个概念：

- **度(degree)**：网络的度表示所有结点中邻居数目的最大值
- **对分宽度(bw)**：将网络分为二分图，两个分图间边的最小值
- **直径(diam)**：任意两个结点之间全部最短路径的最大值

在设计互联网络时，经常关注以下 **理想属性**：

- **常数度**：网络的度是常数，即与网络的规模无关。这个属性允许网络扩大到更大的规模而无需增加过多的连接数
- **小直径**：可以支持任意进程之间的高效通信
- **高对分宽度**：对分宽度越低，大量聚合的通信操作会变得更慢，它隐含的是网络的内部带宽

经典网络拓扑结构各属性的阶：

| topology    | degree                 | diam                      | bw                      |
| ----------- | ---------------------- | ------------------------- | ----------------------- |
| 线性排列    | $\mathcal{O}(1)$       | $\mathcal{O}(n)$          | $\mathcal{O}(1)$        |
| 2D网面/环面 | $\mathcal{O}(1)$       | $\mathcal{O}(\sqrt{n})$   | $\mathcal{O}(\sqrt{n})$ |
| 3D网面/环面 | $\mathcal{O}(1)$       | $\mathcal{O}(^3\sqrt{n})$ | $\mathcal{O}(n^{2/3})$  |
| 二叉树      | $\mathcal{O}(1)$       | $\mathcal{O}(\log(n))$    | $\mathcal{O}(1)$        |
| 超立方体    | $\mathcal{O}(\log(n))$ | $\mathcal{O}(\log(n))$    | $\mathcal{O}(n)$        |

