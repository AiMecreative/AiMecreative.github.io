---
title: 'Paper | Revisiting STR: A Data Perspective'
author: Andrew-Rey
date: 2023-12-26 11:26:36
mathjax: true
category: Paper
tag:
- STR
- Paper
- Data perspective
---

本文做了一个调研: 使用13个STR模型在6个目前常用的benchmark进行测试, 结论是随着时间的推移, 模型的识别能力越来越强, 甚至将各个模型集成以后只有 2.91% 的图片不能被正确识别. 这样的结果"无疑"是在宣告这个领域的终结. 但同样也引人深思: 目前的benchmark是否能足够推动未来进步 (也就是当前数据集还能否展现模型能力); 当前accuracy的饱和是否真的意味着STR已经被解决了.

<!--more-->

[论文](https://arxiv.org/pdf/2307.08723v2.pdf), [代码](https://github.com/Mountchicken/Union14M)

## Introduction

目前比较常用的训练和衡量STR模型的方式是 **先在人造数据集(Synthetic dataset)上进行训练, 再在6个真实数据集(Real benchmark)上做评估**. 目前在STR上的一些进展可以从下图看出

![progress](image.png)

可以发现模型的准确率已经接近"饱和". 这个现象引出了两个问题

- 当前benchmark是否足够推动未来STR的进步
- 准确率的饱和是否宣告STR已经被解决

对于第一个问题, 本文选择13个代表性模型(CTC-based, attention-based and language model-based), 用6个STR benchmark 衡量其表现能力并 **找出它们的联合误差(joint errors)**. 而本文从 <u>数据角度</u>, 着重关注那些 **被错误识别的图片**, 并将其进行分类, 分析结果如下:

![error analysis](image-1.png)

而这写类型的图片也反映了当前STR模型所面临的困难. 因此本文的最大贡献在于 **基于这些被错误识别的类型, 构建了一个真实场景的数据集Union14M**, 这个数据集包含了广泛的真实场景, 可以更加完善和细致地衡量STR模型的效果. 它包含了 $10M$ 的 <u>无标签</u> 图片(Union14M-U)和 $4M$ 的 <u>有标签</u> 图片(Union14M-L). 用Union14M-L测试上述13个STR模型后发现表现一般( $66.53\%$ acc), 即使它们在6个常用benchmark上有 $87.03\%$ 的准确率. 说明上述模型在真实场景下的竞争力比较一般, 尤其是 *curve text, multi-oriented text, context-less text, artistic text, multi-words text salient text and incomplete text*. 通过这样的对比, 作者认为STR "is far from being solved".

本文推测, 造成这样结果的原因可能是数据问题, 也就是 **模型不能很好地利用数据**. 因此为了能从数据角度解决STR, 本文提出了一种可以充分利用 **无标签** 数据的方式. 具体是使用自监督的预训练方式 **(self-supervised pre-training)** 训练 **Vision Transformer-based** STR 模型, 再在不同的真实标签上fine tune, 即可达到和SOTA类似的效果.

## Appendix

### Synthetic dataset VS Real dataset
