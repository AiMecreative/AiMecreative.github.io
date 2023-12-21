---
title: DeepLearning | CRNN
author: Andrew-Rey
date: 2023-11-25 18:50:17
category: DL
tag: 
- Deep learning
- Model
- Scene Text Recognition
published: false
---

CRNN model has been widely used in scene-text recognition (STR) task. The contribution made by it is that it use CTC loss to train the model, which has many complex mathematical derivations.

<!--more-->

## Framework

The whole frame of CRNN is shown as follow:

![crnn](image.png)

- input: use preprocess models to detect texts in a scene and crop them out. Make the result of text detection as the input of the scene-text recognizer.
- convolutional layer: extract information/features of images
- recurrent layer: process the features
- transcription: translate the output of recurrent layer into predicted sequence

### Convolutional Layers

- resize the input image with shape $(32, 100)$
- use convolution and max pooling
- output feature maps with shape $(1, 26, 512)$
- divide the feature maps into 26 features sequences with shape $(1, 1, 512)$
  - one feature sequence maps to a <u>special location</u> of text image

### Recurrent Layers

- each feature sequence is input to a corresponding *Deep Bidirectional LSTM*
  - $T = 26$
- output is a matrix with shape $(26, 26)$, dim-0 stands for the characters number in considerring character set (e.g. alphabet has 26 characters), dim-1 stands for the input moment which is same with dim-2 in feature map of CNN

> **lexicon-based**: constrain the output: the ground-truth is limited, like spelling check
>
> **lexicon-free**: no limited output

### Transcription Layers


