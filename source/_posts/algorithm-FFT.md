---
title: 'algorithm:FFT'
date: 2022-04-06 16:08:39
tags: Algorithm
category: Algorithm
mathjax: true
---

"FFT是我见过最美的算法."

"说的好像你见过很多算法似的."

<!--more-->
# 多项式乘积问题
首先来思考这样的一个问题:

{%note primary%}
### Question 1
你有两个多项式函数:

$p(x)=2x^3+x+1$

$q(x)=x^2+4x+5$

应该如何计算它们的乘积?
{%endnote%}
当然, 我不是说要用笔算的方式, 而是用**计算机**. 显然这个问题我们在[小学二年级](https://space.bilibili.com/254463269/?spm_id_from=333.999.0.0)就写过的, 当初正在学习"数据结构"这门课, 如果没记错, 应该是用链表实现的.

但是, 就算是用链表实现, 那不也是和手算一样的原理吗?
- 将二者相乘
- 分配律
- 合并同类项

例如上面那个例子:
{%note primary%}
### solution 1
<p>
\[
    \begin{aligned}
        r(x) &= (2x^3+x+1)(x^2+4x+5) \\
        &= 2x^5+8x^4+10x^3+x^3+4x^2+5x+x^2+4x+5 \\
        &= 2x^5+8x^4+11x^3+5x^2+5x+5
    \end{aligned}
\]
</p>
{%endnote%}

(**???是什么动力让我深夜在这里口算多项式乘法???**)

显然, 如果一个 n 次多项式乘上一个 m 次多项式, 在合并同类项前应该有 $n\times m$ 次多项式, 这谁顶得住? 对于正常人类而言显然顶不住, 对于计算机而言, 时间复杂度是$O(n^2)$, 也是算比较大的开销了吧.

咋办?

# 点表示法
## 开始
有谁规定, 我多项式一定是用系数表示的?

好家伙, 你这样说我就摸不着头脑了, 难道除了系数表示还有其他表示方法吗?

首先, 多项式集合其实是构成了一个**线性空间**, 也就是说, 任意两个多项式进行线性运算 (加法和数乘) 后, 结果仍然是多项式. 事实上
$$
{1, x, x^2, \dots, x^n, \dots}
$$
构成了该空间的一组基, 将函数展开成 Taylor 级数便用了这组基作为基底, 基前面的系数也就是**坐标**.

其次, 对于一个 n 次多项式而言, 只要我们确定了它的坐标, 就能唯一确定这个多项式. **现在的问题是不知道坐标, 如何确定多项式.** 这里的巧妙之处就在于, 多项式函数是一个映射, 对于一个特定的 x, 总是能给出唯一一个值与之对应, 这不就是一个方程吗?
- 我给你一个 x, 你输出一个值, 同时由于多项式系数全部未知, 这就是一个关于 $n+1$个系数的方程

显然, 我需要$n+1$个不同的点来唯一确定我的系数. 这就是所谓的点表示法. 这样一来, 我们将这$n+1$个方程写成矩阵形式:

<p>
\[\left[
\begin{aligned}
p_0 \\
p_1 \\
\vdots \\
p_n
\end{aligned}\right]
=
\left[
\begin{aligned}
1\quad & x_0\quad & \dots\quad & x_0^n \\
1\quad & x_1\quad & \dots\quad & x_1^n \\
\vdots\quad & \vdots\quad & \quad & \vdots \\
1\quad & x_n\quad & \dots\quad & x_n^n
\end{aligned}
\right]
\left[
\begin{aligned}
c_0 \\
c_1 \\
\vdots \\
c_n
\end{aligned}\right]
\]
</p>

看到这里我终于理解了为什么在学高等代数时要突然讲一个**范德蒙德(Vandermonde)行列式**, 也就是这里的

<p>
\[
\left[
\begin{aligned}
1\quad & x_0\quad & \dots\quad & x_0^n \\
1\quad & x_1\quad & \dots\quad & x_1^n \\
\vdots\quad & \vdots\quad & \quad & \vdots \\
1\quad & x_n\quad & \dots\quad & x_n^n
\end{aligned}
\right]
\]
</p>

将上述矩阵定义为我们最喜欢的字母$A$. 

好, 既然这东西是范德蒙德行列式, 那我们可以知道它行列式$|A|=\prod_{0\leq j< i\leq n}(x_i-x_j)$不为 0, 也就是说, 这个矩阵是可逆的, 也就是当我们取 $n+1$ 个不同点时, 确实是可以使方程组有唯一解, 也就是 **$n+1$ 个点可以唯一表示一个 n 次多项式.**

## 乘法
**问题来了, 如何做乘法?**

我们有 n 次多项式和 m 次多项式做乘法, 得到的是一个 $n+m$ 次多项式, 那么我们只要找到 $n+m+1$ 个点即可, 也就是只要在 n 次多项式和 m 次多项式中分别找 $n + m + 1$ 个点, **这些点的横坐标 x 相等**, 再将对应的函数值相乘即可.

## 进一步
现在, 我们知道了如何用点表示多项式, 以及如何用点表示进行乘法运算. 但是仔细一想, 这种方法需要求解线性方程组, 这里的计算复杂度并不低. 也就是从系数表示法到点表示法的转化过程带来的计算复杂度还是很高的.

有什么方法可以进行简化吗?

先等一等, 我们先来梳理我们用点表示求多项式乘法的思路:
{%note primary%}
### MainIdea
- 将 n 次多项式和 m 次多项式分别从系数表示转化为点表示
- 对应点相乘
- 将得到的 $n+m+1$ 个点表示的多项式转化为系数表示
{%endnote%}

## 奇偶
先来考虑简单的情况:
{%note primary%}
### Question 2
多项式

$
p(x) = x^2
$

和多项式

$
q(x)=x^3
$

用点表示法相乘
{%endnote%}
那我们当然是按部就班地进行乘法啦~
- 由于结果是 5 次多项式, 因此对$p(x)$取 5 个点, 对$q(x)$取 5 个点.

**取点**, 说得轻巧, 做起来倒是挺犹豫的. 取什么样的点能满足要求呢? 或者~~得寸进尺地~~说, 什么样的点能让效率更高呢? **注意到二次函数是对称的**, 那我们是不是只要取正的 2 个点, 就能知道负的 2 个点, 另外加一个原点?

确实如此.

那三次多项式呢? 照理来说, 我们同样也是只要取一半的点就能知道另一半点的值(这里的"一半"针对正负而言), 只不过要在函数值上添加负号, 何必呢? 还不如干脆 **提出一个 x**, 然后不也变成了二次函数?

事实上, 一般而言, 我们要用点表示法表示多项式, 可以用如下方法:
{%note primary%}
### Method1
$$
p(x)=\sum_{i=1}^n c_ix^i=P_e(x)+P_o(x)=P_{e1}(x)+xP_{e2}(x)
$$
其中, $P_{ei}(x)$表示只含偶次的多项式函数, $P_o(x)$表示只含奇次的多项式.
{%endnote%}

这样, 我们只要在非负轴上取值就可以确定整个多项式, 取点的个数是 **原来的一半**.

甚至, 这里形成了一个 **递归** 算法: 分解后的$P_{ei}(x)$不也是一个关于 x 的多项式吗?! 那我继续啊, 把$P_{ei}(x)$继续分解啊, **大事化小, 小事化了.**

**等等!**

我们的$P_{ei}(x)$其实是$P_{ei}(x^2)$, 这里每个$x^2$都是**非负的**啊. 未来我们只能在非负轴取值了, 也就是说, 分解为偶次多项式后, **递归停止了**.

完蛋.

# 复数域分解
"山重水复疑无路, 柳暗花明又一村"

看到标题就已经知道要怎么做了. 既然在实数域上无法继续分解$P_{ei}(x^2)$, 那为何不去**复数域**呢? 

在复数域上我们可以快乐地进行递归.

如何个快乐法呢? 我们来细品:
{%note primary%}
### 偶次多项式在复平面上的根
为什么突然变成了 **求根**?

从第二节中"奇偶", 我们可以选取对称的点, 来减少选取点的个数(即原来的一半). 接着我们把任意 n 次多项式分解成两个偶次多项式, 偶次多项式的好处在于容易选取对称的点. 但是由于在实数范围内, 在对偶次多项式进行递归时会发生中断, 于是我们扩展至复数域讨论分解.

**方便起见**: 对于$x^0$, 我们取$x=1$作为特征点, 对于$x^2$, 我们取$x=1, x=-1, x=0$作为三个特征点, 那对于$x^4$, 我们应该怎样取点, 抛开$x=0$不谈, 令$x^4=1$, 由 **代数基本定理**, 该方程在复数域上有 4 个 **根**, 对于其它偶次多项式我们以此类推.

就这样, 我们找到了一个简单的方法寻找所有需要的点, 进行递归.

### 单位根
写到这里, 我也感觉有点吃力, 关键是为什么一定就取了令$x^{2k}=1$呢?

虽然但是, 确实是所谓的"**方便起见**", 这是因为, 取了"1", 我们可以在复平面上的单位圆上讨论这个问题.

在[小学二年级](https://space.bilibili.com/254463269/?spm_id_from=333.999.0.0)我们就知道, $x^{n}=1$的根可以用我们熟悉的$\omega$的幂来表示, 即
$$ 
\omega = e^{\frac{2k\pi}{n}i}\qquad(k=0,1,\dots,n-1)
$$
这些$n$个点在复平面单位圆上 **对称分布**. 每递归一次, 单位根的数量减少一半, 但保持对称性不变.

确实方便.
{%endnote%}

# 快速傅里叶变换(FFT)
终于能正式地介绍世界上最美丽的算法了: **快速傅里叶变换(FFT)**. FFT解决的是多项式从系数表示到点表示的过程中, 计算复杂度的问题.

## 框架

**分解:**

<p>
\[
p(x)=\sum_{k=0}^nc_kx^k=P_{e1}(x^2)+xP_{e2}(x^2):=[ \omega^0, \omega^1, \dots, \omega^n]
\]
</p>

**递归:**

<p>
\[
P_{e1}(x^2) = P^{\prime}_{e1}(x^4)+xP^{\prime}_{e2}(x^4):=[\omega^0, \omega^1, \dots, \omega^{n-1}]
\]
</p>

<p>
\[
P_{e2}(x^2) = P^{\prime}_{e1}(x^4)+xP^{\prime}_{e2}(x^4):=[\omega^0, \omega^1, \dots, \omega^{n-1}]
\]
</p>

**加和:**

<p>
\[
P(\omega^j)=P_{e1}(\omega^{j})+\omega^jP_{e2}(\omega^j)
\]
</p>

<p>
\[
P(\omega^{j+n/2})=P_{e1}(\omega^{j+n/2})+\omega^{j+n/2}P_{e2}(\omega^{j+n/2})
\]
</p>
$j\in[0,1,\dots, n/2+1]$  \\

**返回**$p(x)$

时间复杂度为: $O(nlog_2n)$

## 一些数学

{%note primary%}
对于 n 次多项式 $p(x)=\sum_{k=0}^n c_kx^k$, 我们给定$n+1$个点: $x_0, \dots, x_n$, 从而得到关于原多项式 $n+1$ 个系数的线性方程组:

<p>
\[
\left[
\begin{aligned}
p_0 \\
p_1 \\
\vdots \\
p_n
\end{aligned}\right]
=
\left[
\begin{aligned}
1\quad & x_0\quad & \dots\quad & x_0^n \\
1\quad & x_1\quad & \dots\quad & x_1^n \\
\vdots\quad & \vdots\quad & \quad & \vdots \\
1\quad & x_n\quad & \dots\quad & x_n^n
\end{aligned}
\right]
\left[
\begin{aligned}
c_0 \\
c_1 \\
\vdots \\
c_n
\end{aligned}\right]
\]
</p>

我们在复数域上考虑, 令
$$
x_k=\omega^k,\quad where\ \ \omega=e^{\frac{2k\pi}{n}}
$$
(这是因为, 我们希望多项式在复数域上考虑时, 我们可以在单位圆周上讨论. 其中$x_k$表示我们取的第 k 个点, 刚好与 $\omega^k$是对应的.)

则线性方程组可以化为:

<p>
\[
\left[
\begin{aligned}
p_0 \\
p_1 \\
\vdots \\
p_n
\end{aligned}\right]
=
\left[
\begin{aligned}[c]
1\quad      & 1\quad        & 1\quad                 & \dots\quad & 1 \\
1\quad      & \omega\quad   & \omega^2\quad          & \dots\quad & \omega^n \\
1\quad      & \omega^2\quad & \omega^4\quad          & \dots\quad & \omega^{2n} \\
\vdots\quad & \vdots\quad   & \vdots\quad       &            & \vdots \\
1\quad      & \omega^n\quad & \omega^{2n}\quad  & \dots\quad & \omega^{n\times n}
\end{aligned}
\right]
\left[
\begin{aligned}
c_0 \\
c_1 \\
\vdots \\
c_n
\end{aligned}\right]
\]
</p>

其中

<p>
\[
 \left[
\begin{aligned}[c]
1\quad      & 1\quad        & 1\quad                 & \dots\quad & 1 \\
1\quad      & \omega\quad   & \omega^2\quad          & \dots\quad & \omega^n \\
1\quad      & \omega^2\quad & \omega^4\quad          & \dots\quad & \omega^{2n} \\
\vdots\quad & \vdots\quad   & \vdots\quad       &            & \vdots \\
1\quad      & \omega^n\quad & \omega^{2n}\quad  & \dots\quad & \omega^{n\times n}
\end{aligned}
\right]   
\]
</p>

称为**离散傅里叶变换矩阵(DFT)**显然该矩阵是 **对称的** 且 **可逆**, 其逆矩阵为:

<p>
\[\frac{1}{n}
 \left[
\begin{aligned}[c]
1\quad      & 1\quad        & 1\quad                 & \dots\quad & 1 \\
1\quad      & \omega^{-1}\quad   & \omega^{-2}\quad          & \dots\quad & \omega^{-n} \\
1\quad      & \omega^{-2}\quad & \omega^{-4}\quad          & \dots\quad & \omega^{-2n} \\
\vdots\quad & \vdots\quad   & \vdots\quad       &            & \vdots \\
1\quad      & \omega^{-n}\quad & \omega^{-2n}\quad  & \dots\quad & \omega^{-n\times n}
\end{aligned}
\right]   
\]
</p>

并且, 该逆矩阵看起来和原矩阵 **一模一样!**
.
{%endnote%}

## 结束了?

当我们乐呵呵地把FFT转化为代码时, 开心的分解多项式, 然后选点, 相乘, **等等!** 你还没告诉我, 怎么从点表示转化回系数表示呢!

这就是FFT**对称**的魅力了. 由点求系数, 不过是矩阵求逆的过程:

<p>
\[
\left[
\begin{aligned}
c_0 \\
c_1 \\
\vdots \\
c_n
\end{aligned}\right]
=
\left[
\begin{aligned}[c]
1\quad      & 1\quad        & 1\quad                 & \dots\quad & 1 \\
1\quad      & \omega\quad   & \omega^2\quad          & \dots\quad & \omega^n \\
1\quad      & \omega^2\quad & \omega^4\quad          & \dots\quad & \omega^{2n} \\
\vdots\quad & \vdots\quad   & \vdots\quad       &            & \vdots \\
1\quad      & \omega^n\quad & \omega^{2n}\quad  & \dots\quad & \omega^{n\times n}
\end{aligned}
\right]^{-1}
\left[
\begin{aligned}
p_0 \\
p_1 \\
\vdots \\
p_n
\end{aligned}\right]
=\frac{1}{n}
 \left[
\begin{aligned}[c]
1\quad      & 1\quad        & 1\quad                 & \dots\quad & 1 \\
1\quad      & \omega^{-1}\quad   & \omega^{-2}\quad          & \dots\quad & \omega^{-n} \\
1\quad      & \omega^{-2}\quad & \omega^{-4}\quad          & \dots\quad & \omega^{-2n} \\
\vdots\quad & \vdots\quad   & \vdots\quad       &            & \vdots \\
1\quad      & \omega^{-n}\quad & \omega^{-2n}\quad  & \dots\quad & \omega^{-n\times n}
\end{aligned}
\right] 
\left[
\begin{aligned}
p_0 \\
p_1 \\
\vdots \\
p_n
\end{aligned}\right]
\]
</p>

显然, 由于DFT和DFT逆矩阵具有相似的形式, 我们完全可以用**同一个函数**完成快速傅里叶的正反变换!

# 后记-"对称, 万变不离其宗"
不会真有人会把这个没有图的文章看完吧?

相信我, 日后在这里补充图片的概率为
$$
p=lim_{x\rightarrow\infty}xsin (1/x)
$$
(糟糕, 好像出简单了)

另外, 在递归的地方, 觉得并没有讲清楚具体的步骤, 但是思想到位了. 日后也不想改了. 可能以后补一补应用场景之类的, 至于代码, 看情况吧.