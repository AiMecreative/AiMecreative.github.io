---
title: DeepLearning | Diffusion Model
author: Andrew-Rey
date: 2023-12-08 10:54:32
mathjax: true
category: DL
tag:
- Deep learing
- Diffusion model
---

"The structure is already complete with the marble block, before I start my work. It is already there, I just have to chisel away the superfuous material." - Michelangelo

<!--more-->

> "雕塑已经在大理石里了, 我的工作只是把不要的部分拿掉." -- 米开朗琪罗

[reference](https://www.bilibili.com/video/BV14c411J7f2/?spm_id_from=333.337.search-card.all.click&vd_source=698de1256a0048d0fd59d2f1bc3e109b), 
[DDPM paper](https://arxiv.org/pdf/2006.11239.pdf),
[DDPM code](https://github.com/hojonathanho/diffusion),
[DDPM inference](https://arxiv.org/pdf/2208.11970.pdf)

## Diffusion Model

> Most of the diffusion models nowdays are similar to ***Denoise Diffusion Probability Model (DDPM)***, so the follow contents will take this base model as an example.

## diffusion Model Workflow

> **reverse process**: 
> 
> 1. give an image sampled from Gaussian noise that have the same shape with the final expected output
> 2. input this image into a ***Denoise*** module, and the output is a little denoised image
> 3. loop the step 2 until reaching the pointed times
> 4. you get the output image
>
> - the **Denoise** modules are marked from $num$ (pointed) to $1$, and the noise is inputed from $num$ to $1$
> - not only is the noise image inputed into denoise module, but also the **texts** and the **noise degree** are inputed
> - denoise module includes a **Noise Predictor** and a **Minus** operator

![reverse process in one Denoise](image-1.png)

> after add texts supervise signal, the module is

![texts supervised](image-4.png)

> **forward process (also known as *difussion process*)**:
>
> 1. give an real image
> 2. add noises to the image
> 3. loop the step 2
> 4. get the niosed image
>
> - the noise added in step number is the **groud truth** of the input image, the noise degree and the texts
> - the training set needs to be a image-text pair

![forward process](image-2.png)

> the training step is

![training step](image-3.png)


## Stabel Diffusion

The framework includes 3 parts

- **text encoder**: inputs the texts and outputs the vectors that descrip the texts
- **generation model**: mostly frequent use is the diffusion model, the input is noises and encoded texts, the outputs is an intermediate products image (compressed image that human can understand or not)
- **decoder**: the input is the intermediate products and the output is the image expected

The three modules are trained **respectively**

![stable diffusion](image-5.png)

### Text Encoder

> **Fréchet Inception Distance (FID)**: the metric to judge the performance of one image.
>
> - use a **pre-trained** CNN model
> - input the real image or generated image respectively
> - take out the **representation** (outputs of the last layer)
> - suppose the representation vectors submits to Gaussion distribution respectively, use Fréchet distance between the two distributions, smaller is better
> - a lots of samples are needed

> **Clip**: Contrastive Language-Image Pre-Training. Give the text-image paris, texts are inputed to a text encoder while the images are inputed to a image encoder
>
> - use this large model to judge if the generated image matches the texts
> - calculate the distance between encoded text vector and encoded image vector

### Decoder

Decoder can be trained without text labels.

- first method: use only images, small image and large image pairs, the smaller image is the input and larger image is the label
- second method: use **anto-encoder**, usually the output of the generation model is a *latent representation*. Input ground truth image to auto-encoder to get the latent representation, and input latent representation into the decoder

### Generation Model

Usually use the diffusion model as the generation model.

- **forward process**: input the ground truth image to the encoder and get the latent representation. Add noises to the latent representation. Loop for a pointed times. Use (noised latent representation, noise degree, texts) as the noise predictor's input and the added noises as the ground truth.
- **reverse process**: input the noises sampled from Gaussian distribution and the encoded texts to denoise module, output the latent representation.

## Principle of diffusion Model

> ***VAE model***: input the ground truth image and use a *encoder* to get the latent representation and input the latent representation to decoder to get the image.

![differences between VAE and diffusion model](image-6.png)

The training process is given by the follow algorithm

![training algorithm](image-7.png)

The $x_0$ is the clean image sampled from dataset and $t$ is sampled from a uniform distribution where $T$ is large. $\epsilon$ is sampled from the normal dsitribution.

Gradient calculation: $\alpha$ is defined later, the value of $\alpha$ decreases from $1$ to $T$. $\sqrt{\bar{\alpha_t}} x_0 + \sqrt{1 - \bar{\alpha_t}} \epsilon$ mixes the clean image and the noises. $\epsilon_{\theta}$ is a function with two parameters one is the mixed image and the other is $t$, which is called **noise predictor**. The ground truth is $\epsilon$. 

The inference process is given by the follow algorithm

![inference algorithm](image-8.png)

The image illustrate the steps of inference algprithm

![inference algorithm image version](image-9.png)

> 所有图片生成模型的 **共同目标** 是希望找到一个 **Network**, 从 **易于采样** 的分布中抽取样本, 并输出一个给定的分布形式. 通常这个 Network 会输入一段文字 (**Condition**). 训练的目标是使输出的分布和真实分布越接近越好.

Definition and mathematic symbols:

- Network: the parameters in network noted as $\theta$
- Generated distribution: noted as $P_{\theta}(x)$
- Real distribution: noted as $P_{data}(x)$

> **Maximum Likelihood Estimation**
>
> - Sample $\lbrace x^1, x^2, \cdots, x^m \rbrace$
> - *Assume* we can calculate $P_{\theta}(x^i)$: given $x^i$, we can calculate the probability generated by $P_{\theta}$
> - The target is $\theta^{\star} = \mathbf{argmax}_{\theta} \prod\limits_{i=1}^m P_{\theta}(x^i)$

$$
\begin{align*}
    \theta^{\star} &= \mathbf{argmax}_{\theta} \prod\limits_{i=1}^m P_{\theta}(x^i) \\
                   &= \mathbf{argmax}_{\theta} \log \prod\limits_{i=1}^m P_{\theta}(x^i) \\
                   &= \mathbf{argmax}_{\theta} \sum\limits_{i=1}^m \log P_{\theta}(x^i) \\
                   &\approx \mathbf{argmax}_{\theta} \sum\limits_{i=1}^m \mathbf{E}_{x\sim P_{data}} \lbrack \log P_{\theta}(x) \rbrack \\
                   &= \mathbf{argmax}_{\theta} \int\limits_{x} P_{data}(x) \log P_{\theta}(x) dx - \int\limits_{x} P_{data}(x) \log P_{data}(x) dx \\
                   &= \mathbf{argmax}_{\theta} \int\limits_{x} P_{data}(x) \log \frac{P_{\theta}(x)}{P_{data}(x)} dx \\
                   &= \mathbf{argmin}_{\theta} \mathbf{KL}(P_{data} || P_{\theta})
\end{align*}
$$

Where the item $\int\limits_{x} P_{data}(x) \log P_{data}(x) dx$ is not related to $\theta$. We can infer that **maximize likelihood is equivalent to minimize [KL divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence)**. (KL-divergence always greater or equal to 0)

- GAN model minimize some divergence
- VAE, diffusion model maximize likelihood

> **VAE example**: 
>
> The generated distribution can be written as $P_{\theta}(x) = \int\limits_{z} P(z) P_{\theta}(x | z)$, where $P(z)$ is the input known distribution such as Gaussian distrbution. VAE assmu that $P_{\theta} \propto \exp(- ||G(z) - x||)$ where $G(z)$ is the *mean* of $P_{\theta}(x)$ and is also the *output* of network
>
> VAE maximize the **lower bound** of $\log P_{\theta}(x)$ to get as greater $\log P_{\theta}$ as possible. Take $P$ as $P_{\theta}$ for short
>
$$
\begin{align*}
    \log P(x) &= \int\limits_z q(z | x) \log P(x) dz \\
              &= \int\limits_z q(z | x) \log (\frac{P(x)}{q(z | x)}\frac{q(z | x)}{P(x)}) dz \\
              &= \int\limits_z q(z | x) \log \frac{P(x)}{q(z | x)} dz + \int q(z | x) \log \frac{q(z | x)}{P(x)} dz \\
              &\geq \int \limits_z q(z | x) \log \frac{P(x)}{q(z | x)} dz \\
              &= \mathbb{E}_{q(z | x)} \lbrack \log \frac{P(x)}{q(z | x)} \rbrack
\end{align*}
$$
>
> where the item $\int q(z | x) \log \frac{q(z | x)}{P(x)} dz = \mathbf{KL}(q(z | x) || P(x)) \geq 0$, and the distribution $q(z | x)$ can be *any* distribution. In VAE, the distribution $q(z | x)$ is the *encoder*.
>
> The goal of VAE is to maximize the lower bound: $\mathbb{E}_{q(z | x)} \lbrack \log \frac{P(x)}{q(z | x)} \rbrack$

For DDPM, there are many *denoise* steps. One denoise is *one* step, after $T$ steps, DDPM produces the expected image. Every step of denoise produces one intermidiate product. So DDPM maximize the lower bound: $\mathbb{E}_{q(x_1 : x_T | x)} \lbrack \log \frac{P(x)}{q(z | x)} \rbrack$, where $q(x_1 : x_T)$ is the *diffusion process* not the encoder in VAE.

$$
q(x_1 : x_T)  = q(x_1 | x_0) q(x_2 | x_1) \cdots q(x_{T} | x_{T_1})
$$

**How to calculate the distribution** $q(x_{T} | x_{T_1})$. Define the hyper-parameters $\lbrace \beta_1, \beta_2, \cdots, \beta_T \rbrace$.

$$
x_t = \sqrt{1-\beta_t} x_{t - 1} + \sqrt{\beta_t} n_t,(\ where\ n_t\sim \mathcal{N}(\mathbf{0},\mathbf{I}))
$$

The noise sampling processes are independent to each other. If we want to calculate $q(x_t | x_0)$, there is a simpler way using iterative inference.

$$
x_2 = \sqrt{1-\beta_2} x_{1} + \sqrt{\beta_2} n_2, x_1 = \sqrt{1-\beta_1} x_{0} + \sqrt{\beta_1} n_1
$$

We combine the two steps: 

$$
\begin{align*}
    x_2 &= \sqrt{1-\beta_2} x_{1} + \sqrt{\beta_2} n_2 \\
        &= \sqrt{1 - \beta_2}\sqrt{1 - \beta_1} x_1 + \sqrt{1 - \beta_2}\sqrt{\beta_1}n_1 + \sqrt{\beta_2} n_2
\end{align*}
$$

The item $\sqrt{1 - \beta_2}\sqrt{\beta_1}n_1 + \sqrt{\beta_2} n_2$ is also a Gaussian distribution as $n_1,n_2$ are independent to each other. We denote them as $\sqrt{1-\sqrt{1-\beta_2}\sqrt{1-\beta_1}} n_3$, which means we can only sample *one* time, from $x_0$ to $x_2$. More generally, if we want to generate $x_t$, we need only sample *one* time from $\mathcal{N}(\mathbf{0}, \mathbf{I})$.x    

![infer-1](image-10.png)

![infer-2](image-12.png)

The middle item $D_{\mathbf{KL}}(q(x_T | x_0) || P(x_T))$ has no relation to the network parameter $\theta$. We mainly focus on the third item.

> calculate $q(x_{t-1} | x_t, x_0)$: given $x_0$ and $x_t$, calculate the $x_{t-1}$'s distribution. Using Bayes formula:
$$
q(x_{t - 1} | x_t, x_0) = \frac{q(x_{t}, x_{t - 1} | x_0)}{q(x_t | x_0)} = \frac{q(x_t | x_{t - 1}, x_0) q(x_{t - 1} | x_0)}{q(x_t | x_0)}
$$

![infer-3](image-13.png)

Whatever, the result is still a Gaussian distribution.

**How to minimize the expectation of KL-Divergence (the third part)**: We want to *minimize* the *expectation* of *KL-Divergence*, so as long as most of the *KL-Divergences* are small, the expectation will be probably small. The small divergence means *two distributions*' distance is small, the two distributions are *close* to each other. The first distribution, $q(x_{t-1} | x_t, x_0)$ is a ***fixed*** Gaussian distribution with known mean and variance which the second distribution $P_{\theta}(x_{t - 1} | x_t)$ is our ***denoise*** module that will be trained. **So we want to let the second distribution's mean close the fixed mean (if ignore the variance).**

The deonise model inputs $x_t$ and the value $t$, outputs the *mean* of distribution, expecting that the mean is close to the mean of $q(x_{t-1} | x_t, x_0)$. Infact, the parameters $\alpha,\beta$ are constants, the only part denoise should predict is the noise $n_t$ or $\epsilon_t$.