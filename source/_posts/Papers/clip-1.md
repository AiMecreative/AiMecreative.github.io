---
title: Paper Reading | Learning Transferable Visual Models From Natural Language Supervision
author: Andrew-Rey
date: 2023-10-30 15:58:33
category: Paper
tag:
- clip
- paper
- DL
- Multimodule
---

- <u>Natural Language Supervision</u>
- <u>Learning Transferable Visual Models</u>

> 利用**自然语言的监督信号**来训练一个**泛化性能好**的视觉模型

<!--more-->

**abstract**

- 之前的视觉模型训练：先有一个**固定的、提前定义好的物体类别**集合，模型去预测这些定义好的类别来完成训练。
  - 收集数据集简单，模型训练简单
  - 有限制的监督信号，限制了模型本身的泛化性

- CLIP
  - 直接从自然语言得到监督信号
  - 范围广，语言描述过的物体就可以被识别到
  - 给定一张图片，给定一个句子，判断配对
  - 训练样本是图片和句子的配对
  - 数据集规模：4亿
  - 自监督
  - 多模态的对比学习
  - 自然语言用于引导模型做物体分类(prompt)
  - 能扩展到新的任务
  - 大多数迁移效果好
  - [开源了预训练模型，只公开了推理的代码，未公开预训练代码](https://github.com/openai/CLIP)

**my focus**

- text2image
  - Downstream task
  - forzen clip model and train generator
  - encode text

- text: poems
- images: height maps, grey-scale