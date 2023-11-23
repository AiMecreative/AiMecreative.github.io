---
title: Deep Learning | Data driven approach
author: Andrew-Rey
date: 2023-11-20 15:33:14
category: DL
tag:
- Deep Learning
---

The first course for every ai-learner. Course CS231N provided by Stanford.

<!--more-->

## Data driven methods

> **semantic gap**: from the number tensors, computer is hard to predicting the category of an image, namely the *semantic* of the image. Once the image change its field of view for the same thing, huge number of pixels are changed but the semantic remains.

> **illumination**: sometimes the image maybe taken in a poor light environment, the image recognization algrithm should be robust to it.

> **deformation**: the objects in an image may deform.

> **occlusion**: the object may be recognized though some parts are occluded.

> **backgroud clutter**: the textures is similar to background.

> **intraclass variation**: same category has diferences in intraclass.

The main idea is that <u>use large data to train a model that has good performance on test set.</u>

- spend much of the time on *training* while little time on test (train on data centers and test on mobile devices)
- for small learning task, its nessecery to ues *k-folder* method to split the data set; for large learning task, such as deep learning, just split the data set into *train, validation and test* sets.Train set is used to train a model, validation set is used to select hyperparameters and test set is used to judge performance.

