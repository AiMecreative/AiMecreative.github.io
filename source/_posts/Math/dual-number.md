---
title: Math | Dual Number
author: Andrew-Rey
date: 2023-11-16 16:18:11
mathjax: true
category: Math
tag:
- Math
- Number Theory
---

Given two real numbers $a, b$ and defines a symbol $\epsilon$ satisfying $\epsilon^2 = 0$ while $\epsilon \neq 0$,
the number $a + b \epsilon$ is called ***Dual number***.

<!--more-->

## Differentiation

The most interesting part (in my opinion) is the differentiation of dual number functions. And it's is the base of auto-differentiation used in `tensorflow` or `pytorch`.

Considering a function $f(x)$ where $x$ is a real number. In the space of dual number, our $x$ can be represented as $x = a + b \epsilon$ where $\epsilon^2 = 0$. In real space, we can use $Taylor$ expansion on $f(x)$:

$$
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(x_0)}{n!} (x - x_0)^n
$$

Use $x = a + b \epsilon$ to replace the $x$ in $f(x)$, and use $Taylor$ expansion again:

$$
f(x) = f(a+b\epsilon) = f(a) + f^{\prime}(a)(a + b\epsilon - a) + f^{\prime\prime}(a)(a + b\epsilon - a)^2 + \cdots
$$

And the amazing place is the definition of $\epsilon$ which satisfies $\epsilon^2 = 0$ while $\epsilon \neq 0$, so the expansion can be written as:

$$
\begin{align}
    f(x) &= f(a + b\epsilon) \\
    &= \sum_{n=0}^{\infty} \frac{f^(n)(a)}{n!} (a + b\epsilon - a)^n \\
    &= f(a) + f^{\prime}(a) b\epsilon + \sum_{n=2}^{\infty} \frac{f^(n)(a)}{n!} (b\epsilon)^n \\
    &= f(a) + f^{\prime}(a) b\epsilon
\end{align}
$$

> **Note:** replace the independent variable in real-function with there dual number representation, the function can be represented by the form of dual number where the first item is the real-form of itself and ***the second item is its derivative.***

