---
title: Math in a Mess | Automatic differentiation
author: Andrew-Rey
date: 2023-11-18 23:13:18
mathjax: true
category: Math
tag:
- Math
- differentiation
---

The automatic differentiation (AutoDiff) has been widely used in nerual network, which is a set techniques to evaluate the partial derivative of a function specified by a computer program. AutoDiff is distinct from symbolic differentiation and numerical differentiation. Symbolic differentiation suffers from being converted into computer programs while the numerical differentiation leads to round-off errors in the discretization process and cancellation.

<!--more-->

## Chain Rule

There are two ways to realize AutoDiff, but the main idea of automatic differentiation is ***chain rule***. Take function $f(g(x))$ as an example, the partial derivative w.r.t the independent variable $x$ is:

$$
\frac{\partial}{\partial x}f(g(x)) = \frac{\partial}{\partial g(x)} f(g(x)) \frac{\partial}{\partial x} g(x)
$$

For a more general form, considering a composite function of $x$, its partial drivative is:

$$
\frac{\partial f}{\partial x} = \frac{\partial f(w_n)}{\partial w_n(w_{n-1})}\frac{\partial w_n(w_{n-1})}{\partial w_{n-1}(w_{n-2})} \cdots \frac{\partial w_0(x)}{\partial x}
$$

The two type of AutoDiff:

- **forward accumulation**: inside to outside, $\frac{\partial w_0(x)}{\partial x} \rightarrow \frac{\partial f(w_n)}{\partial w_n(w_{n-1})}$. For **each** independent variable, a **separate pass is necessary**. So this method is more efficient for function $f:R^n \rightarrow R^m,n << m$.
- **reverse accumulation**: outside to inside, $\frac{\partial f(w_n)}{\partial w_n(w_{n-1})} \rightarrow \frac{\partial w_0(x)}{\partial x}$. This method evaluates the function first and calculates the derivatives w.r.t **all** independent variables in **an additional pass**. So this method is more efficient for function $f:R^n \rightarrow R^m,n >> m$.

### Computational Graph

The graph that shows the composition relations and orders of one function is computational graph. The detail structure of computational graph is shown as follow:

![1700323960325](1700323960325.png)

This graph represents the function:

```
f = w5
w5 = w3 + w4
w4 = a0 * w2
w3 = a1 * w1
w2 = w0
w1 = w0
w0 = x
```

## Forward Accumulation

- fix one variable that you want to perfrom differentiation on
- compute the derivative of each sub-expression recursively

$$
\begin{align}
    Step\ 1.&calculate\ \frac{\partial w_0}{\partial x} \\
    Step\ 2.&calculate\ \frac{\partial w_1}{\partial w_0} \\
    &... \\
    Step\ n.&calculate\ \frac{\partial w_n}{\partial w_{n-1}}
\end{align}
$$

Finally, calculate $\frac{\partial f}{\partial x} = \frac{\partial w_n}{\partial w_{n-1}} \cdots \frac{\partial w_0}{\partial x}$ where $w_n = f$. This is a **Bottom-up** method. Infact, $\frac{\partial w_i}{\partial x} = \sum_{j\in predecessors\ of\ i} \frac{\partial w_i}{\partial w_j} \dot{w_j}$ for a node satisfies $indegree \geq 1$. For multiple variable (say, the vector input), this can be matrix product (Jacobians).

Take the function $y=f(x_1, x_2)=x_1 x_2 + \sin x_1$ as an example, we want to know the derivative on the point $(x_1, x_2)$. Notation: $w_1 = x_1, w_2 = x_2, w_3 = w_1 w_2, w_4 = \sin w_1, w_5 = y$. We choose the independent variable $x_1$ as our target to perform differentation., which also called a *seed*. The seed values are **initialized** to:

$$
\begin{align}
    \dot{w_1} = \frac{\partial w_1}{\partial x_1} = \frac{\partial x_1}{\partial x_1} = 1 \\
    \dot{w_2} = \frac{\partial w_2}{\partial x_1} = \frac{\partial x_2}{\partial x_1} = 0
\end{align}
$$

As the *seed* values are set, the values propagate using the *chain rule*:

| Operations to compute value | Operations to compute derivative            |
| --------------------------- | ------------------------------------------- |
| $w_1 = x_1$                 | $\dot{w_1} = 1$ (seed)                      |
| $w_2 = x_2$                 | $\dot{w_2} = 0$ (seed)                      |
| $w_3 = w_1 w_2$             | $\dot{w_3} = \dot{w_1} w_2 + w_1 \dot{w_2}$ |
| $w_4 = \sin w_1$            | $\dot{w_4} = \dot{w_1} \cos w_1$            |
| $w_5 = w_3 + w_4$           | $\dot{w_5} = \dot{w_3} + \dot{w_4}$         |

So, once given the value of point $(x1, x2)$, we can know the derivative of $\partial f / \partial x_1$. If you want to know $\partial f / \partial x_2$, you should conduct the steps above <u>again</u> with the *seed* $\dot{w_1} = 0, \dot{w_2} = 1$.

The <u>computational graph</u> is

![forward](image.png)

## Reverse Accumulation

