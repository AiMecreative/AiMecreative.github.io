---
title: Pattern Recognition
date: 2022-2-28
mathjax: true
category: Artificial Intelligence
---

"This is really a great lesson."

"If there are no such many homework."

<!--more-->

# Introduction
## What is Patter Recognition?
- Pattern
  - the opposite of choas
- Recognition
  - Identification of a pattern as  a member of a category
  - <font color=blue>Classification</font>: category known $\Rightarrow$ assign proper class label for each pattern
  - <font color=blue>Clustering</font>: category unknown $\Rightarrow$ learn categories and group patterns
- Pattern Recognition
  - Perceive (理解): interact with the real-world
  - Process (处理): learn to distinguish patterns of interest
  - Prediction (预测): make sound and reasonable decisions about the categories

# Bayesian Decision Theory
## Basic Theory
### Bayesian Formula
$$
P(\omega_i | \mathbf{x}) = \frac{P(\omega_i)p(\mathbf{x} | \omega_i)}{p(\mathbf{x})}
$$
Where $\omega_i(i = 1,\dots, c)$ is the category of research object. $\mathbf{x}$ is the **feature vector**, has $d$ dimensions. We call $P(\omega_i | \mathbf{x})$ **posterior**, $P(\omega_i)$ **prior probability** and $p(\mathbf{x} | \omega_i)$ **likelihood** of $\mathbf{x}$ in category $\omega_i$. Note that $p(\omega{x})$ is a constant, we call it **evidence coefficient**.
$$
p(\mathbf{x}) = \sum_{i = 1}^c P(\omega_i)p(\mathbf{x} | \omega_i)
$$

### Loss function
We use 
$$
\lambda(\alpha_i | \omega_j)
$$
to describe the loss or penetrate we get since we take action $\alpha_i$ while the true category is $\omega_j$.

### Class-Conditional Probability
We define the **class conditional probability** relative to the action $\alpha_i$
$$
R(\alpha_i | \mathbf{x}) = \sum_{j=1}^c \lambda(\alpha_i | \omega_j) P(\omega_j | \mathbf{x})
$$
So the **total risk** is defined as:
$$
R = \int_{feature\ space} R(\alpha_i | \mathbf{x}) p(\mathbf{x}) d\mathbf{x}
$$

### The Decision Theory
**Bayesian Decision Theory**: In order to minimize the total risk $R$, for $i = 1, \dots, a$ we calculate the class-conditional probability
$$
R(\alpha_i | \mathbf{x}) = \sum_{j=1}^c \lambda(\alpha_i | \omega_j) p(\omega_j | \mathbf{x})
$$
and choose a proper action $\alpha_i$ to make the $R(\alpha_i | \mathbf{x})$ minimized.

## Two-class classification
The loss function is
$$
\lambda_{ij} \doteq \lambda(\alpha_i | \omega_j)
$$
And our class conditional function are:
<p>\[
\begin{aligned}
R(\alpha_1 | \mathbf{x}) &= \lambda_{11} p(\omega_1 | \mathbf{x}) + \lambda_{12} p(\omega_2 | \mathbf{x})\\
R(\alpha_2 | \mathbf{x}) &= \lambda_{21} p(\omega_1 | \mathbf{x}) + \lambda_{22} p(\omega_2 | \mathbf{x})
\end{aligned}
\]</p>

The decision is: if $R(\alpha_1 | \mathbf{x}) < R(\alpha_2 | \mathbf{x})$, then it means $\alpha_1$ takes smaller risk, and so we choose the action $\alpha_1$.

Using the posterior probability to describe is:
$$
(\lambda_{21} - \lambda_{11})P(\omega_1 | \mathbf{x}) > (\lambda_{12} - \lambda_{22})P(\omega_2 | \mathbf{x})
$$

Using the Bayes' Formula, converting the prior probability to posterior probability:
$$
(\lambda_{21} - \lambda_{11})p(\mathbf{x} | \omega_1)P(\omega_1) > (\lambda_{12} - \lambda_{22})p(\mathbf{x} | \omega_2)P(\omega_2)
$$

Or writing with fraction form:
$$
\frac{p(\mathbf{x} | \omega_1)}{p(\mathbf{x} | \omega_2)} > \frac{\lambda_{12} - \lambda_{22}}{\lambda_{21} - \lambda_{11}}\frac{P(\omega_2)}{P(\omega_1)}
$$

## The Minimum-error Classification
We define the minimum-error classification is a problem that uses the **symmetric loss** or **"0-1" loss**:
<p>\[
\lambda(\alpha_i | \omega_j) = \left\{\begin{aligned}
&0&\ &i=j,\\
&1&\ &i\neq j
\end{aligned}\right.\ \ \ i,j = 1,\dots,c
\]</p>

If you use this symmetric loss in a classification problem, you mean **all the error decisions make the same consequence**.

Our decision is made based on conditional risk:
<p>
\[
\begin{aligned}
R(\alpha_i | \omega_j) &= \sum_{j = 1}^c \lambda_{ij} P(\omega_j | \mathbf{x})\\
&= \sum_{i\neq j} 1 \cdot P(\omega_j | \mathbf{x})\\
&= 1 - P(\omega_i | \mathbf{x})
\end{aligned}  
\]
</p>

### Minimax Rule
I will not write this part until I make it clear...

## The Discriminant Function, Decision Surface Based on Gaussian Distribution
### Gaussian Distribution
<p>\[\begin{aligned}
\varphi(\mathbf{x}) = \frac{1}{(2\pi)^{\frac{d}{2}}|\Sigma|^{\frac{1}{2}}}exp(-\frac{1}{2}(\mathbf{x} - \mathbf{\mu})^T\Sigma^{-1}(\mathbf{x} - \mathbf{\mu}))
\end{aligned}\]</p>


**Ongoing update...**