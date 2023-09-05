---
title: 【数学杂记】空间
date: 2022-03-20 01:20:10
category: Math
tags:
  - Math
mathjax: true
---

"内积空间和度量空间有什么区别? Hilbert空间是什么? 它与线性空间的关系是什么?"

"我已经晕了."

<!--more-->

# 数域
\\(P\\)是包含0, 1的数集, 且对 \\(P\\)中任意两个数的加减乘除运算封闭, 则称 \\(P\\)是一个数域.

# 线性空间
在数域的基础上, 我们提出线性空间的概念:

给定数域 \\(P\\) , 和集合 \\(V\\). 有如下映射:
$$
+:V\times V\rightarrow V
$$
$$
\cdot:P\times V\rightarrow V
$$
且 (\\(V, P, +, \cdot\\)) 满足**八条基本性质**, 则\\(V\\)称为一个线性空间.

# 赋范空间
<u>赋范空间是定义在线性空间之上的.</u>

定义在数域 \\(P\\) 的线性空间 \\(V\\) 存在如下映射:
$$
||\cdot||:  V\rightarrow R
$$
且该映射满足: 正定, 齐次, 三角不等式. 则 \\(V\\) 是一个赋范空间, 其中映射 \\(||\cdot||\\) 称为范数.

# 内积空间
<u>内积空间是定义在线性空间之上的.</u>

定义在数域 \\(P\\) 的线性空间 \\(V\\) 存在如下映射:
$$
\cdot:  V\times V\rightarrow R
$$
则 \\(V\\) 是一个内积空间.

定义了内积后, 我们可以讨论向量 (即线性空间的元素) 间的长度和夹角, 并进一步讨论正交性等.

注意: 内积本身具有自然定义的范数, 即内积可以诱导出范数, \\(||x||=\sqrt{(x,x)}\\), 因此内积空间含于赋范空间.

# 度量空间
度量空间是某个具有距离函数的集合. 该函数定义的是集合内所有元素的距离, 即集合上的某种度量, 即:

给定**集合**\\(V\\), 有映射:
$$
d:V\times V\rightarrow \mathbf{R}
$$
满足:
<p>\[
\begin{aligned}
&d(x,y)\geq0\quad (d(x,y)=0\Leftrightarrow x=0,y=0)\\
&d(x,y)=d(y,x)\\
&d(x,y)\leq d(x,z)+d(z,y)
\end{aligned}
\]</p>

注意: 此处并未要求线性结构.

**注意: 赋范空间一定可以诱导出度量空间, 因此赋范空间含于度量空间**

# 完备空间
完备空间又称 Cauchy 空间. <u>完备空间是定义在度量空间之上的.</u>

若度量空间 \\(M\\) 中所有的柯西序列都收敛在 \\(M\\) 中的一点, 则 \\(M\\) 是一个完备空间.

# Hilbert空间
在**内积空间**的基础上增添**完备性条件**, 即得到**Hilbert空间**.

# 总结
范数运算+向量空间=(线性)赋范空间

(线性)赋范空间 + 内积运算=内积空间

(线性)赋范空间 + 完备性 = Banach 空间

内积空间 + 完备性 = Hilbert 空间

内积空间 + 完备性 + 有限维 = Euclidean 空间

# References
zhihu:

https://www.zhihu.com/question/332144499/answer/731866608

https://www.zhihu.com/question/42312263/answer/699451330

wikipedia:

https://en.wikipedia.org/wiki/Complete_metric_space

https://en.wikipedia.org/wiki/Metric_space

https://en.wikipedia.org/wiki/Cauchy_sequence

https://en.wikipedia.org/wiki/Cauchy_sequence

https://en.wikipedia.org/wiki/Cauchy_sequence

https://en.wikipedia.org/wiki/Normed_vector_space