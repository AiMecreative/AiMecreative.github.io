---
title: 【算法】基本数据结构
date: 2023-06-13 13:21:13
tags:
    - CS
    - Algorithm
    - Data Structure
categories: CS
author: Andrew-Ray
mathjax: true
---

"基本数据结构"

<!--more-->

## 栈

> LIFO表

> C++数组模拟栈

```c++
int st[N];
// 这里使用 st[0] (即 *st) 代表栈中元素数量，同时也是栈顶下标

// 压栈 ：
st[++*st] = var1;

// 取栈顶 ：
int u = st[*st];

// 弹栈 ：注意越界问题, *st == 0 时不能继续弹出
if (*st) --*st;

// 清空栈
*st = 0;
```

## 队列

> FIFO表

> c++数组模拟队列

```c++
int q[SIZE], ql = 1, qr;

// 插入元素
q[++qr] = x;

// 删除元素
ql++;

// 访问队首
q[qr];

// 访问队尾
q[ql];

//清空队列
ql = 1;
qr = 0;
```

> 双栈模拟队列：两个栈模拟一个队列，队尾的栈为F，队首的栈为S
>
> - `push`：插入到栈F中
> - `pop`：如果S非空，让S弹栈；否则先把F的元素倒过来压入S中，然后让S弹栈

### 双端队列

> 可以在队首/队尾插入或删除元素的队列。相当于是栈与队列功能的结合。具体地，双端队列支持的操作有 4 个
>
> - 在队首插入一个元素
> - 在队尾插入一个元素
> - 在队首删除一个元素
> - 在队尾删除一个元素

### 循环队列

> 使用数组模拟队列会导致一个问题：随着时间的推移，整个队列会向数组的尾部移动，一旦到达数组的最末端，即使数组的前端还有空闲位置，再进行入队操作也会导致溢出（这种数组里实际有空闲位置而发生了上溢的现象被称为「假溢出」）。
> 
> 解决假溢出的办法是采用循环的方式来组织存放队列元素的数组，即将数组下标为 0 的位置看做是最后一个位置的后继。（数组下标为 x 的元素，它的后继为 (x + 1) % SIZE）。这样就形成了循环队列。
>
> [来自OIWiki](https://oi-wiki.org/ds/queue/)

## 链表

### 单向链表

```c++
struct Node {
  int value;
  Node *next;
};
```

> **删除结点p**
>
> 实际上是删除p+1：将p+1的值赋给p，p的next指向p的next的next，删除p+1

### 双向链表

```c++
struct Node {
  int value;
  Node *left;
  Node *right;
};
```

### 单向循环链表

> 将单向链表的头尾相连接。**注意**： 插入数据时要判断原链表是否为空；为空则自身循环，不为空则正常插入
>
> - 为空则插入的数据`node`的指针和链表指针都指向自己
> - 不为空则和单向链表一致

### 双向循环链表

> 插入数据时，注意要修改左右指针

### 异或链表

> 本质上还是双向链表：利用按位异或的值，仅用一个指针的内存大小实现双向链表的功能
>
> - 在结点`node`中定义`lr = left_addr ^ right_addr`
> - 访问`left`：`lr ^ right_addr`
> - 访问`right`：`lr ^ left_addr`
>
> 异或自反：`A ^ B ^ B = A ^ (B ^ B) = A ^ 0 = A`

## 哈希表

$$key\rightarrow value$$

> 哈希函数：把key映射到索引空间，`f(key)`是一个可以作为数组下标的整数
>
> - 整数为key：使用整数作为key的时候，如果整数范围小，直接将key作为索引；若范围较大（ $10^9$ ）则 **一般把键值模一个较大的质数作为索引** $f(x)=x\ mod\ M$ 作为哈希函数
> - 字符串为key：先将字符串哈希，再将哈希结果作为key：**可以把字符串当作长度为n的进制为127的数**（ $x=s_0*127^0+s_1*127^1+\cdots+s_n*127^n$ ），将得到的 $x$ 对 $2^{64}$ 取模（`unsigned long long`最大值）。
>   - 容易冲突
>   - 使用双哈希：选取两个大质数，当两个字符串的哈希值对两个大质数模相等时，才认为相等。

### 冲突

> **拉链法**：在每个存放数据的地方开一个链表，如果有多个键值索引到同一个地方，则放到链表内部即可。如果索引的范围是 $1\cdots M$ ，哈希表的大小为 $N$ ，则一次插入或查询的期望比较次数为 $O(\frac{N}{M})$

> **闭散列法**：把所有记录直接存储在散列表中，如果冲突则以某种规则检查
>
> - 线性探查法：在d处冲突，则依次检查d+1，d+2.

## 并查集

> [参考](https://zhuanlan.zhihu.com/p/93647900)

> 用于管理元素所属集合的数据结构，实现为一个森林，每棵树表示一个集合，节点表示对应集合中的元素
>
> - 合并：合并两个元素的所属集合
> - 查询：查询某个元素所属集合（查询根节点），用于判断两个元素是否在同一集合

> 结构：一个数组，存储每个元素的父结点

> 初始化：初始时，每个结点以自己作为父结点

```c++
int fa[MAXN];
inline void init(int n) {
    for (int i = 1; i <= n; ++i)
        fa[i] = i;
}
```

> **合并：**先找到两个结点的根节点，然后将某一个设置为根节点（下面的代码将j的父结点设置为i的父结点）

```c++
inline void merge(int i, int j) {
    fa[find(i)] = find(j);
}
```

> **查询：**两个结点是否在同一个集合取决于根节点是否相同（递归往上查询）

```c++
int find(int x) {
    if(fa[x] == x) return x;
    else return find(fa[x]);
}
```

![并查集构建结果](dsu.png)

### 路径压缩

> 由于构建以后的深度可能比较深，会影响查询的效率，因此可以考虑路径压缩，把属于该集合的元素直接连接到根结点。
>
> 压缩这一步是在查询的时候顺便解决的

```c++
size_t dsu::find(size_t x) { return pa[x] == x ? x : pa[x] = find(pa[x]); }
```

### 启发式合并

> 将节点较少或深度较少的树连接到另一棵

### 删除

> 可以将其根节点设置为自己（为了保证删除的都是叶子结点，可以将其副本作为根节点）

### 移动

> 将副本作为根节点

### 复杂度

> 时间复杂度：$O(\alpha(n))$，$\alpha$是阿克曼函数反函数，增长极其缓慢

> 空间复杂度：$O(n)$

### 带权并查集

> 在并查集的边上定义某种权值、以及这种权值在路径压缩时产生的运算，从而解决更多的问题

### 应用

[OIWiki](https://oi-wiki.org/topic/dsu-app)

## 堆

### 二叉堆

> - 完全二叉树
> - 父亲的权值不小于儿子的权值（大根堆）
> - 由堆性质，树根存的是最大值（`getmax` 操作就解决了）

> **插入**
>
> - 最下一层最右边的叶子之后插入
> - **向上调整**：如果这个结点的权值大于它父亲的权值，就交换，重复此过程直到不满足或者到根
> - $O(log(n))$

> **删除**
>
> - 删除根节点：考虑插入操作的逆过程，设法将根结点移到最后一个结点，然后直接删掉。通常采用的方法是，把根结点和最后一个结点直接交换
> - **向下调整**：在该结点的儿子中，找一个最大的，与该结点交换，重复此过程直到底层  
> - $O(log(n))$

```c++
// 向上调整
void up(int x) {
  while (x > 1 && h[x] > h[x / 2]) {
    swap(h[x], h[x / 2]);
    x /= 2;
  }
}
// 向下调整
void down(int x) {
  while (x * 2 <= n) {
    t = x * 2;
    if (t + 1 <= n && h[t + 1] > h[t]) t++;
    if (h[t] <= h[x]) break;
    std::swap(h[x], h[t]);
    x = t;
  }
}
```

> **建堆**
>
> - **向下调整**：从叶子开始，逐个向下调整
> - $O(n)$
> - 由于叶子节点不用调整，因此可以从$n/2$的地方开始调整

```c++
void build_heap_2() {
  for (i = n; i >= 1; i--) down(i);
}
```

### 配对堆

> - 支持插入，查询/删除最小值，合并，修改元素
> - 可并堆
> - 基于势能分析
> - 不能可持久化
> - 带权多叉树
> - 满足堆的性质：每个节点的值都小于或等于他的所有孩子（小根堆）
> - 不一定是完全的
> - child-sibling表示法

![配对堆](pairingheap1.png)

```c++
struct Node {
  T v;  // T为权值类型
  Node *child, *sibling;
  // child 指向该节点第一个儿子，sibling 指向该节点的下一个兄弟。
  // 若该节点没有儿子/下个兄弟则指针指向 nullptr。
};
```

> **child-sibling表示法**：
> 一个节点的所有儿子节点形成一个单向链表。每个节点储存第一个儿子的指针，即链表的头节点；和他的右兄弟的指针

> **查询最小值**：直接返回根节点（权值）

> **合并**
>
> - 找到两个根节点的较小者，将较大的根节点作为其孩子插入进去
> - 孩子链表按插入时间排序，最右边的节点最早成为父节点的孩子，最左边最近成为孩子

![配对堆的合并](pairingheap3.png)

```c++
Node* meld(Node* x, Node* y) {
  // 若有一个为空则直接返回另一个
  if (x == nullptr) return y;
  if (y == nullptr) return x;
  if (x->v > y->v) std::swap(x, y);  // swap后x为权值小的堆，y为权值大的堆
  // 将y设为x的儿子
  y->sibling = x->child;
  x->child = y;
  return x;  // 新的根节点为 x
}
```

> **插入**：把新元素视为一个配对堆即可

> **删除最小值（根节点）**
>
> - 删除根节点
> - 把根节点的孩子们两两配对合并
> - 将新产生的森林从右向左（旧的向新的方向）合并
> - 下面的代码已经保证了顺序

```c++
Node* delete_min(Node* x) {
  Node* t = merges(x->child);
  delete x;  // 如果需要内存回收
  return t;
}

// x是左部的节点，c是右部的节点，每次合并保证右部都已经合并（递归实现）
// x与相邻的右部sibling节点合并，再与右部节点合并
Node* merges(Node* x) {
  if (x == nullptr || x->sibling == nullptr)
    return x;  // 如果该树为空或他没有下一个兄弟，就不需要合并了，return。
  Node* y = x->sibling;                // y 为 x 的下一个兄弟
  Node* c = y->sibling;                // c 是再下一个兄弟
  x->sibling = y->sibling = nullptr;   // 拆散
  return meld(merges(c), meld(x, y));  // 核心部分
}
```

> **减小一个元素的值**：基本思路是，当减小一个元素的值时，由于是小根堆，该元素对应的子树仍然满足配对堆的性质，因此（如果修改元素后，该元素与父母节点不满足性质）可以将子树剖出来，再与原来的树合并
>
> - **注意：**为了剖离子树，可能会用到双向链表

> **增大一个元素的值**：以该节点为根的子树剖出来，然后删去它的最小值（该节点），插入该节点修改后的值，最后与原堆合并

> **均摊复杂度**
>
> - `meld`: $O(log(n)),O(1),O(2^{2\sqrt{loglogn}})$
> - `delete-min`: $O(log(n))$
> - `decrease-key`: $O(log(n)),O(2^{2\sqrt{loglogn}})$

### 左偏树

> - 可并堆
> - 有很多应用

> **二叉树`dist`的定义**
>
> - `dist`不是深度
> - 外节点：左孩子/右孩子节点为空
> - 外节点的`dist`定义为1
> - 不是外节点的`dist`为其到子树中最近的外节点的距离+1
> - 空节点的`dist`定义为0

> **左偏树定义**
>
> - 二叉树
> - 满足堆性质
> - 每个左孩子的dist大于等于右孩子的dist
>   - 因此左偏树每个节点的dist都等于其右儿子的dist加一

![左偏树](leftist-tree.png)

> **合并**：合并两个堆时，由于要满足堆性质，先取值较小（小根堆）的那个根作为合并后堆的根节点，然后将这个根的左儿子作为合并后堆的左儿子，递归地合并其右儿子与另一个堆，作为合并后的堆的右儿子。为了满足左偏性质，合并后若左儿子的 \mathrm{dist} 小于右儿子的 \mathrm{dist}，就交换两个儿子。[原文](https://oi-wiki.org/ds/leftist-tree/#%E6%A0%B8%E5%BF%83%E6%93%8D%E4%BD%9C%E5%90%88%E5%B9%B6merge)

```c++
int merge(int x, int y) {
  if (!x || !y) return x | y;  // 若一个堆为空则返回另一个堆
  if (t[x].val > t[y].val) swap(x, y);  // 取值较小的作为根
  t[x].rs = merge(t[x].rs, y);          // 递归合并右儿子与另一个堆
  if (t[t[x].rs].d > t[t[x].ls].d)
    swap(t[x].ls, t[x].rs);   // 若不满足左偏性质则交换左右儿子
  t[x].d = t[t[x].rs].d + 1;  // 更新dist
  return x;
}
```

## ST表

> **可重复贡献问题**
> 对于某个运算`opt`，如果 $x\ opt\ x=x$ ，则对应的 **区间查询** 是一个可重复贡献问题
>
> - 最大值：RMQ问题（区间最大/最小值）
> - 最大公因数：GCD

> **问题**
> 给定n个数，有m个询问，每次询问需要给出区间 $[l,r]$ 的最大值

> **ST表（Sparse Table）**：可以 $\Theta(nlog(n))$ 预处理，$\Theta(1)$ 回答询问，不支持修改元素