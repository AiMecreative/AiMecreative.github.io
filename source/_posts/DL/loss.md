---
title: DeepLearning | Loss in Super-Resolution
author: Andrew-Rey
date: 2023-12-07 09:38:57
mathjax: true
category: DL
tag:
- Deep learning
- loss function
- super-resolution
---

The loss functions used in super-resolution tasks have differences from other tasks like speech recognition. The mainly reason is that not only should the researchers compare the distance of two or more image matrices, but also the image structure and other indices.

<!--more-->

## Peak signal-to-noise ratio (PSNR)

[reference](https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio)

**Definition:** the maximum possible power of a signal and the power of currupting noise that affects the fidelity of its representation.

- commomly used to <u>quantify reconstruction quality</u> for images and videos subjuct to *lossy compression*

For *monochrome* image $I$ with $m\times n$ size and its noise approximation $K$, $MSE$ is defined by

$$
MSE = \frac{1}{m n} \sum\limits_{i=0}^{m-1}\sum\limits_{j=0}^{n-1}[\mathit{I}(i,j)-\mathit{K}(i,j)]^2
$$

The $PSNR$ with $dB$ form is

$$
\begin{align*}
    PSNR &= 10 \cdot \log_{10} (\frac{MAX_I^2}{MSE}) \\
         &= 20 \cdot \log_{10} (\frac{MAX_I}{\sqrt{MSE}}) \\
         &= 20 \cdot \log_{10} (MAX_I) - 10 \cdot \log_{10} (MSE)
\end{align*}
$$

Where the $MAX_I$ is the maximum *possible* pixel value of image $I$, such as the image is represented with 8 bits per pixel, $MAX_I=255$.

- for 8-bit images, the common $PSNR$ ranges from $30dB$ to $50dB$, the higher the better
- apply this index under the *same* codec and the *same* content
- poorer performance compared  with other quality metrics

## Structural similarity index measure (SSIM)

[reference](https://en.wikipedia.org/wiki/Structural_similarity)

**Definition:** $SSIM$ is used for measuring the similarity between two images. This metric is a *full reference metric*, which means this measurement or prediction of image quality is based on an *initial uncompressed or distortion-free* image as a reference.

- The difference with other techniques such as MSE or PSNR is that these approaches estimate absolute errors. Structural information is the idea that the pixels have strong inter-dependencies especially when they are spatially close. These dependencies carry important information about the structure of the objects in the visual scene.

For luminance $l$, contrast $c$ and structure $s$, the individual formulas between samples $x,y$ are $l(x,y)=\frac{2\mu_x \mu_y + c_1}{\mu_x^2  +\mu_y^2 + c_1}, c(x,y)=\frac{2\sigma_x \sigma_y + c_2}{\sigma_x^2 + \sigma_y^2 + c_2}, s(x,y)=\frac{\sigma_{xy} + c_3}{\sigma_x \sigma_y + c_3}$ where $c_3 = c_2 / 2$, and the $SSIM$ is

$$
SSIM(x,y)=l(x,y)^{\alpha} c(x,y)^{\beta} s(x,y)^{\gamma}
$$

Setting the $\alpha, \beta, \gamma$ to $1$, the $SSIM$ can be calculated by

$$
SSIM(x,y)=\frac{(2\mu_x\mu_y + c_1)(2\sigma_{xy} + c_2)}{(\mu_x^2 + \mu_y^2 + c_1)(\sigma_x^2 + \sigma_y^2 + c_2)}
$$

- the constants $c_i$ is used to stablize the division with weak denominator.
  - $c_1=(k_1 L)$, $c_2=(k_2 L)$, where $L$ is the dynamic range of pixel values (such as $2^8 - 1=255$ with 8-bit image)
- not satisfies triangle inequality or non-negativity, thus is not a distance function 
  - under certain conditions, $SSIM$ can be converted into a normalized root $MSE$ measure which is a *distance function*. 
- the *square* of it is *not convex* but a ***locally convex*** and *quasiconvex*

## Connectionist temporal classification (CTC)

[reference-1](https://www.cs.toronto.edu/~graves/icml_2006.pdf), [reference-2](https://distill.pub/2017/ctc/)

The task of CTC is

> given two sequences one is the input $\mathbf{X}=[x_1, x_2, \cdots, x_T]$ and the other is the output $\mathbf{Y}=[y_1, y_2, \cdots, y_U]$, our aim is to find a mapping from the set of $\mathbf{X}$ to the set of $\mathbf{Y}$
>
> - the length of $\mathbf{X}$ and $\mathbf{Y}$ can vary; no corrspondence of the elements between two sequences; the input and the output may be disalignment

CTC handles the task. The output of CTC is the *probability distribution* of all possible $\mathbf{Y}$ 's and we can use the distribution to *infer* the most likely sequence.

**Loss function**: for a given input, we want to train our model to maximize the probability it assigns to right answers.

$$
Y^{\star} = \mathbf{argmax}_Y P(Y | X)
$$

CTC is an alignment-free method. The total loss is conducted on a ***union*** of alphbet $L$ and a *blank* symbol $\epsilon$, namely the input and the output is the subset of $L\cup \lbrace\epsilon\rbrace$. This map function is conducted by the following 3 steps:

![alignment](image.png)

Usually, the CTC loss divides the input sequence into small strides based on *time-step* (if for an image, the time step is a small width) and outputs a probability distribution for *every* time-step. The whole output of the input sequence/image forms a probability matrix with the shape $a\times l$, where $a$ is the size of the union set of alphabet and blank $L\cup \lbrace\epsilon\rbrace$ and $l$ is the sequence length.

![probability of sequence](image-1.png)

The math form is $p(Y | X) = \sum\limits_{A\in \mathcal{A}_{X,Y}}\prod\limits_{t=1}^T p_t(a_t | X)$

- $p(Y | X)$: the CTC conditional probability
- $\sum_{A\in\mathcal{A}_{X,Y}}$: marginalizes over the set of valid alignments
- $\prod\limits_{t=1}^T p_t(a_t | X)$: computing the probability for a single alignment step-by-step

### Dynamic programming solution

> If we aren’t careful, the CTC loss can be very expensive to compute. We could try the straightforward approach and compute the score for each alignment summing them all up as we go. The problem is there can be a massive number of alignments. For most problems this would be too slow.

But we can conduct DP algorithm to solve this problem. * The key insight is that if two alignments have reached the same output at the same step, then we can merge them.*

![dp algorithm](image-2.png)

There are no need to calculate all paths' probabilities, which is computation consuming. Considerring the order of input and output, we introduce a new output sequence noted $\mathbf{Z}=\lbrack \epsilon, y_1, \epsilon, y_2, \epsilon, \cdots, \epsilon, y_U, \epsilon \rbrack$, namely inserting the blank $\epsilon$ between every two neighboring characters including the head and the tail.

There are two cases in the whole paths map between neighboring time step.

- **case 1** is that for $t-th$ step character, the preceding nodes include three possible statuses: the $\epsilon$, the *same* character and the character *different* from it.
- **case 2** is that for $t-th$ step character, the current node is *in recurrent*, so the preceding nodes include two possible statuses: the $\epsilon$ and the *same* character.

![path map](image-3.png)

For the formula form, we define the symbol $\alpha_{s,t}$ as the CTC loss of the subsequence $\mathbf{Z}_{1:s}$ after $t$ input time steps.

- **case 1** formula: $\alpha_{s,t} = (\alpha_{(s-1,t-1)} + \alpha_{s,t-1}) \times p_t(z_s | X)$, where the factor means *the CTC probability of the two valid subsequences after $t-1$ input steps* and the later probability means *the probability of the current character at input step $t$*
- **case 2** formula: $\alpha_{s,t} = (\alpha_{(s-2,t-1)} \alpha_{(s-1,t-1)} + \alpha_{s,t-1}) \times p_t(z_s | X)$

Note that there are ***two valid start states and two valid end states***, so the compelete probability is ***the sum of the final two nodes.***
