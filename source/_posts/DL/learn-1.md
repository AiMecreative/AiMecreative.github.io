---
title: DeepLearning | Quick Start I
author: Andrew-Rey
date: 2023-11-24 10:54:38
category: DL
tag:
- deep learning
- tutorial
- lhy-ML
---

The first lecture that all ai-beginner should to take.

[video](https://www.bilibili.com/video/BV1Wv411h7kN/?p=3&spm_id_from=pageDriver&vd_source=698de1256a0048d0fd59d2f1bc3e109b)

<!--more-->

## Introduction

> deep learning aims to finding a *function*.

- classification
- regression
- structured

The general step to do machine learning:

- **write down the function model** *with unknown parameters*
  - need *domain knowledge*
- **define *loss* from training data**, *loss* is a function of <u>parameters</u> in your model
  - how good a set of parameters are
  - calculate from training data
  - visuaization: error surface
- **optimization** your loss with *gradient descent*

> **gradient descent**:
> $w^{\star}, b^{\star}=\arg\min_{w,b} Loss$ compute the derivative $\frac{\partial L}{\partial w}|_{w=w^0}$ where $w^0$ is picked randomly.
> Use the *learning rate* to stand for the step width: $w^1 \leftarrow w^0 - \eta \frac{\partial L}{\partial w}|_{w=w^0}$. Then, update $w$ until reaches a threshold (such as the max iteration count or minimum updation)

The above three steps is **train**.

### Model

**model bias**: comes from unreasonable model.

How to construct a reasonable model or how to fit the model functions are the main problems in ML/DL. The most common idea is to use the combination of *function units* to fit the model. Such as the *sigmoid* function.

> **piecewise linear**: $constant + \sum c_i sigmoid(b_i + w_i x)$. This can simulate lots of functions (including <u>piecewise linear constructed with lots of small line segements</u> and <u>curve functions</u> which can be divided into many piecewise linear)

$$
c \cdot Sigmoid(b+ w x) = c\frac{1}{1 + e^{-(b + w x)}}
$$

- $w$: change slopes
- $b$: shift
- $c$: change height

For multi-features (suppose $j$ festures): $y = const + \sum_i c_i sigmoid(b_i + \sum_j w_{ij} x) = const + c^T \sigma(\mathbf{b} + W \mathbf{x})$

![sigmoid-matrix](image-2.png)

*Sigmoid* function is also called ***Activation function***.

### Loss and Optimization

Concatenate $W, b, c, const$ into a vector (for matrix $W$, concatenate its rows or colums into a vector) named $\theta$. Optimiza the loss function and calculate the parameter $\theta$:

$$
\theta^{\star} = \arg\min_{\theta} L
$$

Note $\mathbf{g}$ for gradient: $\mathbf{g_i} = \triangledown L(\theta^i)$, update the $\theta$ using $\theta_{i+1} \leftarrow \theta_i - \eta \mathbf{g_i}, \mathbf{g}_{i+1}=\triangledown L(\theta_{i+1})$. Stop updating when converging.

**Train with large dataset**: divide dataset into *batches*, update $\theta$ on each batch; The process that all batches have been seen is named *epoch*.

### More activation functions

**ReLU**: Rectified Linear Unit: $ReLU(b + w x) = \max(0, b + w x)$

Same as *sigmoid*, *ReLU* is also an ***activation function***

### More layers

note $a = ReLU(\mathbf{b}+W \mathbf{x})$, continue the same work: $a^{\prime} = ReLU(\mathbf{b^{\prime} + W^{\prime}\mathbf{a}})$ and so on... The whole thing we do just now can be show as follow:

![multi-layer](image-1.png)

You can see the loss decreases more than just one layer.

Each activation function dubbed ***Neuron***, one layer neurons overlays another one build the ***Neural Network*** or you can also say many ***hidden layers*** build the ***Deep Learning***.

> **overfitting**: sometimes, the deeper network brings overfitting problem.