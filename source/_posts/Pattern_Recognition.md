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

{%note primary%}
### preview:three classification ideas
- estimate the class conditional function
- estimate the posterior
- calculate the discriminant function directly
{%endnote%}

# Bayesian Decision Theory
## Basic Theory
### :cherry_blossom:Bayesian Formula
$$
P(\omega_i | \mathbf{x}) = \frac{P(\omega_i)p(\mathbf{x} | \omega_i)}{p(\mathbf{x})}
$$
Where $\omega_i(i = 1,\dots, c)$ is the category of research object. $\mathbf{x}$ is the **feature vector**, has $d$ dimensions. We call $P(\omega_i | \mathbf{x})$ **posterior**, $P(\omega_i)$ **prior probability** and $p(\mathbf{x} | \omega_i)$ **likelihood** of $\mathbf{x}$ in category $\omega_i$. Note that $p(\omega{x})$ is a constant, we call it **evidence coefficient**.
$$
p(\mathbf{x}) = \sum_{i = 1}^c P(\omega_i)p(\mathbf{x} | \omega_i)
$$

### :cherry_blossom:Loss function
We use 
$$
\lambda(\alpha_i | \omega_j)
$$
to describe the loss or penetrate we get since we take action $\alpha_i$ while the true category is $\omega_j$.

### :cherry_blossom:Class-Conditional Probability
We define the **class conditional probability** relative to the action $\alpha_i$
$$
R(\alpha_i | \mathbf{x}) = \sum_{j=1}^c \lambda(\alpha_i | \omega_j) P(\omega_j | \mathbf{x})
$$
So the **total risk** is defined as:
$$
R = \int_{feature\ space} R(\alpha_i | \mathbf{x}) p(\mathbf{x}) d\mathbf{x}
$$

### :cherry_blossom:The Decision Theory
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
 $$  
\begin{aligned}
R(\alpha_1 | \mathbf{x}) &= \lambda_{11} p(\omega_1 | \mathbf{x}) + \lambda_{12} p(\omega_2 | \mathbf{x})\\
R(\alpha_2 | \mathbf{x}) &= \lambda_{21} p(\omega_1 | \mathbf{x}) + \lambda_{22} p(\omega_2 | \mathbf{x})
\end{aligned}
   $$

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
 $$  
\lambda(\alpha_i | \omega_j) = \left\{\begin{aligned}
&0&\ &i=j,\\
&1&\ &i\neq j
\end{aligned}\right.\ \ \ i,j = 1,\dots,c
   $$

If you use this symmetric loss in a classification problem, you mean **all the error decisions make the same consequence**.

Our decision is made based on conditional risk:
 $$
  
\begin{aligned}
R(\alpha_i | \omega_j) &= \sum_{j = 1}^c \lambda_{ij} P(\omega_j | \mathbf{x})\\
&= \sum_{i\neq j} 1 \cdot P(\omega_j | \mathbf{x})\\
&= 1 - P(\omega_i | \mathbf{x})
\end{aligned}  
  
 $$

### :cherry_blossom:Minimax Rule
I will not write this part until I make it clear...

## The Discriminant Function, Decision Surface Based on Gaussian Distribution
### :cherry_blossom:Gaussian Distribution
 $$  \begin{aligned}
\varphi(\mathbf{x}) = \frac{1}{(2\pi)^{\frac{d}{2}}|\Sigma|^{\frac{1}{2}}}exp(-\frac{1}{2}(\mathbf{x} - \mathbf{\mu})^T\Sigma^{-1}(\mathbf{x} - \mathbf{\mu}))
\end{aligned}   $$

### :cherry_blossom:Discriminant Function
The discriminant function is defined as: we choose $i^{th}$ class, if
$$
g_i(x)>g_j(x)
$$
for $\forall j\neq i$. And $g_i(x)$ is called discriminant function.

Based on minimum-error classification, the discriminant function can be written as:
 $$
  
\begin{aligned}
g_i(x)&=-P(\omega_i|x) \\
&=P(\omega_i|x) \\
&=p(x|\omega_i)P(\omega_i)\ (Bayes' Formula) \\
&=lnp(x|\omega_i)+lnP(\omega_i)
\end{aligned}
  
 $$
where the "=" means "equivalent" or "the same to".

Specially, if it's a two-class classification:
$$
g(x)=g_1(x)-g_2(x)
$$
or
$$
g(x)=P(\omega_1|x)-P(\omega_2|x)
$$
or
$$
g(x)=ln\frac{p(x|\omega_1)}{p(x|\omega_2)}+ln\frac{P(\omega_1)}{P(\omega_2)}
$$
Correspondingly, we have **decision boundary** and **decision region**.

### :cherry_blossom:Minimum total risk based on Gaussian distribution: Discriminant Function, Discriminant Boundary
On this section, we discuss the situation that **the likelihood submits Gaussian distribution** and **the loss is "0-1" loss**.

 $$
  
p(x|\omega_i)=\frac{1}{(2\pi)^{d/2} |\Sigma_i| ^ {1/2}}exp(-\frac{1}{2}(x-\mu_i)^T\Sigma_i^{-1}(x-\mu_i))
  
 $$

$$
\lambda(\alpha_i|\omega_j) = I(i\neq j)
$$

$$
g_i(x)=lnp(x|\omega_i)+lnP(\omega_i)=-\frac{1}{2}(x-\mu_i)^T \Sigma_i^{-1}(x-\mu_i)-\frac{d}{2}ln2\pi-\frac{1}{2}ln|\Sigma|+lnP(\omega_i)
$$

:triangular_flag_on_post:<b>Minimum distance classifier</b>

:blue_heart:**case 1a:** suppose all prior probabilities are the same

$$
P(\omega_i)=1/c\ \ \forall i \in (1,c)
$$

and all features have no relationships with others and all classes have the same covariance matrices

$$
\Sigma_i=\sigma^2I\ \ \forall i \in (1,c)
$$

Discriminant function:

 $$
  
\begin{aligned}
  g_i(x)&=-\frac{1}{2}(x-\mu_i)^T\Sigma_i^{-1}(x-\mu_i)+constant \\
  g_i(x)&=-\frac{1}{2\sigma^2}(x-\mu_i)^T(x-\mu_i)\ \ \ (Euclidean\ distance) \\
  g_i(x)&=-\frac{1}{2\sigma^2}(x^Tx-2\mu_i^Tx+\mu_i^T\mu_i) \\
\end{aligned}
  
 $$

$x^Tx$ is independent with $\forall i$, so $x^Tx$ is a constant when considering $i$.

 $$
  
g_i(x)=\frac{1}{\sigma^2}\mu_i^Tx-\frac{1}{2\sigma^2}\mu_i^T\mu_i
  
 $$

this is a **linear discriminant machine**.

Discriminant boundary:

 $$
  
g_i=g_j  
  
 $$

 $$
  
  \begin{aligned}
&\frac{1}{\sigma^2}\mu_i^Tx-\frac{1}{2\sigma^2}\mu_i^T\mu_i=
\frac{1}{\sigma^2}\mu_j^Tx-\frac{1}{2\sigma^2}\mu_j^T\mu_j \\
&\frac{1}{\sigma^2}(\mu_i^T-\mu_j^T)x - \frac{1}{2\sigma^2}(\mu_i^T + \mu_j^T)(\mu_i - \mu_j)=0 \\
&\frac{1}{\sigma^2}(\mu_i-\mu_j)^T(x-\frac{1}{2}(\mu_i + \mu_j))  =0 \\
\end{aligned}
  
 $$

{%note primary%}
so the discriminant boundary must pass the point $x=\frac{1}{2}(\mu_i + \mu_j)$, and is vertical with $(\mu_i-\mu_j)$
{%endnote%}

:blue_heart:**case 1b:** suppose all prior probabilities are the same:

$$
P_i=1/c
$$

and all covariance are the same, but features have relationships with each other:

$$
\Sigma_i=\Sigma
$$

Discriminant function:
 $$
  
\begin{aligned}
&g_i(x)=-\frac{1}{2}(x-\mu_i)^T\Sigma_i^{-1}(x-\mu_i)-\frac{1}{2}ln|\Sigma_i|+constant \\
&g_i(x)=-\frac{1}{2}(x-\mu_i)^T\Sigma_i^{-1}(x-\mu_i)-\frac{1}{2}ln|\Sigma| \\
&g_i(x)=-\frac{1}{2}(x-\mu_i)^T\Sigma_i^{-1}(x-\mu_i)\ \ \ (Mahalanobis\ distance) \\
&g_i(x)=2\mu_i^T\Sigma^{-1}x-\mu_i^T\Sigma^{-1}\mu_i \\
\end{aligned}
  
 $$

this is also a **linear discriminant machine**.

Discriminant boundary:

 $$
  
(\Sigma^{-1}(\mu_i-\mu_j))^T(x-\frac{\mu_i+\mu_j}{2})=0
  
 $$

{%note primary%}
the boundary crosses the middle point of $\mu_i$ and $\mu_j$, but is not vertical with $\mu_i-\mu_j$ as $\Sigma$ provides a rotation with $\mu_i-\mu_j$.
{%endnote%}

:blue_heart:**case 2a:** suppose $P(\omega_i)$ are not the same, while all features have no relationships with others and all classes have the same covariance matrices

$$
\Sigma_i=\sigma^2I\ \ \forall i \in (1,c)
$$

Discriminant function:

 $$
  
  g_i(x)=2\mu_i^Tx-\mu_i^T\mu_i+2\sigma^2lnP(\omega_i)
  
 $$

this is a **linear discriminant machine**

Discriminant boundary:

 $$
  
(\mu_i-\mu_j)^T(x-\frac{\mu_i+\mu_j}{2}-\frac{\sigma^2}{||\mu_i-\mu_j||^2}ln\frac{P(\omega_i)}{P(\omega_j)}(\mu_i-\mu_j))  
  
 $$

if $P(\omega_i)>P(\omega_j)$, then 
 $$  
\frac{\sigma^2}{||\mu_i-\mu_j||^2}ln\frac{P(\omega_i)}{P(\omega_j)}(\mu_i-\mu_j))>0
   $$
 , it will cross a point that is closer to $\mu_j$.

:blue_heart:**case 2b:** suppose $P(\omega_i)$ are not the same, while covariance are the same, but features have relationships with each other:

$$
\Sigma_i=\Sigma
$$

Discriminant function:

 $$
  
g_i(x)=(\Sigma\mu_i)^Tx-\frac{1}{2}\mu_i^T\Sigma^{-1}\mu_i+lnP(\omega_i)  
  
 $$

this is a **linear discriminant machine**

Discriminant boundary:

 $$
  
  (\Sigma(\mu_i-\mu_j))^T(x-\frac{1}{2}(\mu_i+\mu_j)-\frac{ln[P(\omega_i)/P(\omega_j)]}{(\mu_i-\mu_j)^T\Sigma(\mu_i-\mu_j)}(\mu_i-\mu_j))
  
 $$

:blue_heart:**case 3:** suppose that $P(\omega_i)$ are not the same as well as covariance matrices, then the discriminant function is a quadric function. The discriminant boundary will be more various.


# Maximum Likelihood estimation and Bayesian estimation
In the chapter 2, we suppose the likelihood function $p(x|\omega)$ is known, but it impossible to know about it in the daily life or experiments, so we must estimate the likelihood function. Generally speaking, we have two methods to solve this problem: the one is **parameter estimation** and the other is **non-parameter estimation**.

In **parameter estimation**, we will give a prior model of likelihood function of $x$ with unknown parameters, and what we should do is estimating the parameters using the data set.

## Maximum Likelihood estimation
Use the **parameterized form** of class-conditional density function (likelihood):

$$
p(x|\omega_i, \theta_i)
$$

As we solve all classes' parameters **respectively**, we can simplify the denotation as:

$$
P(D|\theta)
$$

where $D$ means the data set of class $\omega_i$.

samples are i.i.d:

 $$
  
p(D|\theta_i)=\prod_{k=1}^n p(x_k|\theta)
  
 $$

and the ML estimation method asks we to find a suitable $\theta$ to maximize $p(D|\theta)$, which means:

 $$
  
\theta = argmax_{\theta} p(D|\theta)  
  
 $$

if we know $\theta$, we will know $p(x|\omega_i,\theta_i)$(just to traverse all categories and calculate $\theta_i$), and then we can train classifiers based on Bayesian decision thm.

So how to solve $\theta = argmax_{\theta} p(D|\theta)$:

log-likelihood function:

 $$
  
\ell(\theta)=\sum_{k=1}^n lnp(x_k|\theta)  
  
 $$

maximizing $p(D|\theta)$ is the same with maximizing log-likelihood. So, calculate the gradient of $\theta$:

$$
\frac{\partial}{\partial \theta}\ell(\theta)
$$

**we will discuss the Gaussian situation:**

### :cherry_blossom:ML Gaussian Case: $\mu$ is unknown

As $\Sigma$ is know, so 

$$
\theta=\mu
$$

 $$
  
\begin{aligned}
\ell(\theta)&=\sum_{k=1}^n lnp(x_k|\theta) \\
&=\sum_{k=1}^n -\frac{1}{2}(x_k-\mu)^T\Sigma^{-1}(x_k-\mu)-ln(2\pi)^{d/2}|\Sigma|^{1/2} \\
\end{aligned}
  
 $$

Gradient:

 $$
  
\begin{aligned}
\ell^{\prime}(\theta)&=\sum_{k=1}^n 2\Sigma^{-1}x_k-2\Sigma^{-1}\mu \\
\end{aligned}
  
 $$

let

$$
\ell(\theta)=0
$$

we get:

$$
\hat{\mu} = \frac{1}{n}\sum_{k=1}^n x_k
$$

### :cherry_blossom:ML Gaussian Case: $\mu$ and $\Sigma$ are unknown
1. for only one feature (1-dim case):
we have:
$$
\hat{\mu} = \frac{1}{n}\sum_{k=1}^n x_k
$$
and
$$  
\hat{\Sigma} = \hat{\sigma} = \frac{1}{n}\sum_{k=1}^n(x_k-\hat{\mu})^2
$$

2. for multi-feature (multi-dim case):

$$  
\hat{\mu} = \frac{1}{n}\sum_{k=1}^n x_k  
$$

$$ 
\hat{\Sigma} = \frac{1}{n}\sum_{k=1}^n(x_k-\hat{\mu})(x_k-\hat{\mu})^T 
$$

{%note primary%}
$\hat{\mu}$ is unbiased estimation, $\hat{\Sigma}$ is not.

But $\frac{n}{n-1}\hat{\Sigma}$ is unbiased estimation.
{%endnote%}


## Bayesian estimation
**We suppose our parameter $\theta$ submits to a prior distribution, and our goal is to estimation $\theta$'s distribution with given data set and prior distribution**.

Some notions:

prior probability $P(\theta)$

posterior $p(\theta|D)$

likelihood $p(x|D)(i.e.p(x|\omega))$

Two important relations:

$$
p(x|D) = \int p(x,\theta|D)d\theta = \int p(x|\theta)p(\theta|D)d\theta\qquad(1)
$$

$$
  \begin{aligned}
  p(\theta|D)&=\frac{p(D|\theta)P(\theta)}{\int p(D|\theta)P(\theta)d\theta} \\
  &=\alpha p(D|\theta)P(\theta) \\
  &=\alpha\prod_{k=1}^n p(x_k|\theta)P(\theta)\qquad(2)
  \end{aligned}
 $$

**Ongoing update...**