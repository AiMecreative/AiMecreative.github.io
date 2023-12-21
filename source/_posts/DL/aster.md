---
title: DeepLearning | ASTER
author: Andrew-Rey
date: 2023-11-25 20:04:15
category: DL
tag:
- Deep learning
- Scene Text
published: false
---

ASTER model is an attention based model with rectifying function.

<!--more-->

## Framework

### Rectification Network

- Spatial Transformer Networks (STN, 2015)
  - transform on deformed image

- resize input images
  - downsampling
- localization network
  - input downsampled image
  - output control points (coordinates normalized into [0, 1] of texts in image that can cover texts)
- grid generator (use TPS)
  - get the map relation between control points and output control points (rectified image)
- sampler
  - the output of the sampler is $(32, 100)$ (assuming input into recognization network)
  - kernelize


### Recognition Network

> **encoder**: BiLSTM

> **decoder**: Attention based.
> Designed two decoders: inversion and forword, choose higher belief