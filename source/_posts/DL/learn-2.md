---
title: DeepLearning | Quick Start II
author: Andrew-Rey
date: 2023-11-24 14:16:26
category: DL
tag:
- Deep learning
- tutorial
- lhy-ML
---

Is it must be overfitting when the loss is not small? Infact there are two possible reasons for this situation. The one is model bias and the other is the poor optimization.

<!--more-->

## Questions when training

### Big loss when training

> Notice that this situation appears in ***training*** step

If you get the big loss when training the network, one prossible reason is the model bias, which means you may try other bigger model with more elasticity; the other reason is the optimizer works poor.

How two judge the two situation? If you get bigger loss ***not only*** in test set, ***but also*** in train set compared to a smaller model, the most possible reason is the weak optimizer.

![big loss](image.png)

### Overfitting

Small loss in training set but big in testing set.

Solutions:

- Expend the training data
  - collect more training data
  - data augmentation (must be suitable for the training task)
- Constrain the model, decrease the flexibility
  - less parameters (less neuron)
  - shareing parameters
  - less features
  - early stop
  - regularization
  - dropout

### Model selection

Cross validation: split your training set into validation set and training set, use validation set to select model

- k-folder method

### Optimization

Gradient nears to zero but loss still big, maybe the model is still on the ***critical point*** (gradient equals to zero, not only the local minima but also the saddle point).

Suppose the loss function is zero at point $\theta^{\prime}$, use Taylor formula to estimate the value of loss around point $\theta$

$$
L(\theta) \approx L(\theta^{\prime}) + (\theta - \theta^{\prime})^T L^{\prime}(\theta^{\prime}) +  (\theta - \theta^{\prime})^T \mathbf{H}  (\theta - \theta^{\prime})
$$

where $\mathbf{H}$ is the *Hessian* matrix $H_{ij}=\frac{\partial}{\partial \theta_i \partial \theta_j}L(\theta)$.

Considerring that the *gradient* is zero, namely $L^{\prime}(\theta^{\prime}) = 0$

$$
L(\theta) \approx L(\theta^{\prime}) + v^T \mathbf{H} v
$$

where $v = \theta - \theta^{\prime}$. <u>For all</u> $v$:

- if $v^T \mathbf{H} v > 0$, namely $\mathbf{H}$ is *positive definite* (all eigen values are above zero): $L(\theta) > L(\theta^{\prime})$, which means the point $\theta^{\prime}$ is a ***local minima***
- if $v^T \mathbf{H} v < 0$, namely $\mathbf{H}$ is *negtive definite* (all eigen values are below zero): $L(\theta) < L(\theta^{\prime})$, which means the point $\theta^{\prime}$ is a ***local maxima***
- if sometimes $v^T \mathbf{H} v > 0$ while sometimes $v^T \mathbf{H} v < 0$, the point is a ***saddle point***

So ***one way*** to judge the type of criticle point is to calculate all the eigen value of Hessian and see the sign of them

- escape saddle point: the loss can be updated (continue to decrease) towards the eigen vector's direction: $L(\theta) \approx L(\theta^{\prime}) + v^T \mathbf{H} v = L(\theta^{\prime}) + \lambda ||\mathbf{u}||$ where $\mathbf{u}$ is the eigen vector for the *positive* eigen value

> *local minima* and *saddle point*:
>
> - Which one appears more frequently in the practice? There is a hypothesis. Suppose a local minima for a 1-dimmension independent variable, such as the quadratic function, it has a local minima. But put it to the 2-dimmension space, the local minima may convert into a saddle point. So the hypothesis is that if there is a local minima point, it can be converted into a saddle point in an enough high space. The big model nowadays has millons of parameters in loss function, so there must be lots of saddle point that gradient equaling to zero but can being decreased. The saddle points are more common.

> **batch**: divide all training set into small *batches*, for ***every batch***, calculate the loss gradient, update parameters. The process that all batches had been seen is called an ***epoch***. ***Shuffle*** all batches after one epoch. Why use batch? Decreasing the noise steps when updating the parameters and the parallel calculation.
