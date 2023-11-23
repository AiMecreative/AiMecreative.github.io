---
title: Deep Learning | k-NN
author: Andrew-Rey
date: 2023-11-23 10:27:04
category: Deep Learning
tag:
- knn
- deep learning
---

k-NN is a data driven approch to do classification task. Its train process is just to ***remenber*** the whole train set while its validate/test set is to measure the metric between the given sample and train set, the category is the *nearest*.

<!--more-->

### k-NN

**metric**

- L1: sum of absolute value of differences on each element: $d_1(a, b)=\sum |a_i - b_i|$, where $a,b$ are tensors
- L2: Euclid distence: $d_2(a, b)=\sqrt{\sum (a_i - b_i)^2}$, where $a ,b$ are tensors

**k-nearest neighbor**

- use the nearest sample point to decide the category of test sample
- sensitive to noise

**k-n neighbors**

- use the $n-th$ nearest sample points to decide the category using *voting*.

**drawbacks**

- large *train* data density
  - the best is to cover the whole sample space
- curse of dimensionality
  - calculation increases exponentially while the features increase linearly