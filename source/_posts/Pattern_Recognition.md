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
R(\alpha_i | \mathbf{x}) = \sum_{j=1}^c \lambda(\alpha_i | \omega_j) p(\omega_j | \mathbf{x})
$$

So the **total risk** is defined as:
$$
R = \int_{feature\ space} R(\alpha_i | \mathbf{x}) p(\mathbf{x}) d\mathbf{x}
$$

**Ongoing update...**