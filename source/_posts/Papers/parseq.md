---
title: Papers | PARSeq
author: Andrew-Rey
date: 2023-12-11 13:58:48
category: Paper
tag:
- Paper
- STR
---

STR 的方法里面经常会使用自回归的语言模型（ARLM），当然考虑到自回归的一些缺点和局限性，也有人采用外置的语言模型。但是外置的语言模型（external LM）是条件独立的（conditional independence），有时会将正确的预测结果修正为错误的结果。本文提出的PARSeq（Permuted Autoregressive Sequence）模型使用了Permutation Language Modeling和Weight Sharing来集成自回归语言模型。

<!--more-->

[代码](https://github.com/baudm/parseq)，[论文](https://arxiv.org/abs/2207.06966)

## Introduction

本文先介绍了什么是STR任务并说明该任务成果的应用场景和当前问题，并提出 **STR任务在某些情况下不能仅仅依靠image features来做推理，而是要依赖一定的language semantics**。STR网络中内置的语言模型一般是自回归的，不仅能够处理语言特征还能联合地处理图像特征。通常的自回归策略是<u>根据过去的时刻的预测值来预测当前时刻的值</u>： $P(\mathbf{y} | \mathbf{x})=\prod_{t=1}^{T} P(y_t | \mathbf{y}_{<t}, \mathbf{x})$ （其中 $\mathbf{y}$ 是一个长度为$T$的文本序列， $\mathbf{x}$ 是图像）。这样的自回归策略有两个缺点：

- 单向性：文本序列的预测要么从左到右，要么从右到左。预测结果和顺序有一定的关系。
- 推理的时候，输出的序列顺序和训练是一样的。

为了解决“单向”的问题，有人提出了 **ABINet** 的模型，它主要使用掩码的方式，在注意力层多加了一层掩码：$P(\mathbf{y} | \mathbf{x}) = \prod_{t=1}^{T}P(y_t | \mathbf{x})$，其中 $P(\mathbf{y}) = \prod_{t=1}^{T}P(y_t | \mathbf{y}_{t\neq 1})$，即在预测某个字符时，将其做掩码，用其余字符对掩码字符进行预测，这样的好处是能够 **利用双向** 的字符特征。但是在 ABINet 中，作者采用的是 independent LM，可以单独训练，不依赖于 image model，用于 *纠正* image model 的错误。但是当语言模型本身的预测结果就是错误的，又何谈 *纠错* 呢？于是为了利用image和text两种特征，ABINet 的作者又加了 fusion 模块，但本文作者认为这种方式带来了巨大的参数数量。

看了序列模型的综述，本文发现目前比较常用的、研究较多的一类模型是 *序列生成模型*，作者认为可以将这些模型结合context-free和context-aware后泛化在STR任务中。并且能将 *外部* 的语言模型转化为 *内部* 的。本文着重关注的是 Permutation Language Model (PLM)，后续本文会说明是如何改进PLM，让其更加适用于STR。本文提到：*PLM模型可以看作是自回归的一种泛化，能够使用 **共享的结构和权值集成** 多个自回归模型*。如下图所示

![permiutation](1703145646187.png)

本文类似这种方式，提出了用于STR任务的PARSeq（Permuted Autoregressive Sequence）模型，并且表现还不错。

## Related Work

本文在这一节主要从三个方面来总结STR的工作，分别是context-free STR, context-aware STR 和 generation from sequence model。

- context-free STR：直接从图片中预测字符串，每一个字符是概率独立的。缺点是low robust，于是大家开始利用语言模型来指导图片文本的识别
- context-ware STR：在图片的文字识别中加入语言模型作为指导，但是会出现两种方式：一种是所谓的external LM，也就是直接使用现有的语言模型，主要用于通过集成、迭代等方式提升预测的准去率；一种是internal LM，主要是跟着自己的模型一起训练。不过对于后者，传统的做法是使用monotonic and standard AR训练方式，PARSeq使用的是PLM方式。
- generation from sequence model：
  - autoregressive (one token at a time)
  - non-regressive (all token predicted at once)

## Permuted Autoregressive Sequence Models

在这一节中，会像大部分论文一样采用三段论：先介绍整体的模型架构，再介绍训练的方式，最后讨论如何运用训练好的模型做推理。