---
title: Machine Learning
date: 2022-3-1
mathjax: true
category: Artificial Intelligence
---

"In fact, I have no idea if I can finish this blog."

"You can."

<!--more-->

# Introduction
## Definitioin of ML
1. Using the way of computing, experience to generate a model and predict the future data.

2. ML is study of algorithsms that:
- imporve their performance <font color=orange>P</font>
- at some task <font color=orange>T</font>
- with experiences <font color=orange>E</font>

<P, T, E> constitute a "well-defined" learning problem.

## Terminologies
- date set
- sample
- feature
- feature space
- feature vector (not same as eigenvector)
- training
- training set
- testing set
- hypothesis (corresponding with a learnt model)
- learner
- prediction
- label
- label space
- classification
- regression
- clustering
- supervised learning
- unsupervised learning
- generalization
  - sample size
  - model complexity
- inductive bias (归纳偏好)
- under-fitting
- over-fitting

## Two Basic Rules
### Occam's razor rule
*if there are many corresponding hypothesises to our observing objects, then choose the simpliest one.*

of course, <font color=orange>the best model is who have a better generalization ability</font>.

### No Free Lunch Theorem
*no matter how your learning algorithsms are, they have the same expectation ability*

NFL tells us we should discuss our model in <font color=orange>specific situation</font>.

The mathematical proof:

considering the binary classification task and the true goal function can be anyone who satisfys $\mathcal{X}\mapsto\{0,1\}$, so our function space is $\{0, 1\}^{|\mathcal{X}|}$. Add all errors for any function $f$ submiting the uniform distribution.
<p>\[
\begin{aligned}
\sum_f E_{ote}(\mathfrak{L}_a | X,f) =& \sum_f\sum_h\sum_{x\in\mathcal{X}-X}P(\boldsymbol{x})\mathbb{I}(h(\boldsymbol{x})\neq f(\boldsymbol{x}))P(h|X, \mathfrak{L}_a) \\
=& \sum_{x\in\mathcal{X}-X}P(\boldsymbol{x})\sum_h P(h|X,\mathfrak{L}_a)\sum_f\mathbb{I}(h(\boldsymbol{x})\neq f(\boldsymbol{x})) \\
=& \sum_{x\in\mathcal{X}-X}P(\boldsymbol{x})\sum_h P(h|X,\mathfrak{L}_a)\frac{1}{2}2^{|\mathcal{X}|} \\
=& \frac{1}{2}2^{|\mathcal{X}|}\sum_{x\in\mathcal{X}-X}P(\boldsymbol{x})\sum_h P(h|X,\mathfrak{L}_a) \\
=& \frac{1}{2}2^{|\mathcal{X}|}\sum_{x\in\mathcal{X}-X}P(\boldsymbol{x})\cdot\boldsymbol{1}
\end{aligned}
\]</p>

$\mathcal{X}$ represents the sample space, $\mathcal{H}$ represents the hypothesis space, which are all <font color=orange> discrete </font>.

$P(h|X,\mathfrak{L}_a)$ represents the probability of algrithsm $\mathfrak{L}_a$ constructs the hypothesis $h$ based on the training data $X$.

the function $f$ represents our <font color=orange> true </font> goal function.

$E_{ote}$ represents the error when our model using testing data set (e.i. $\mathcal{X}-X$)

$\mathbb{I}(\cdot)$ is instruction function, which is equal to 1 when $\cdot$ happens and 0 when doesn't happen.

# Evaluation and Choise of Models
