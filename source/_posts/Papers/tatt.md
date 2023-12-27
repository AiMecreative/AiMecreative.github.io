---
title: Paper | TATT
author: Andrew-Rey
date: 2023-12-02 14:03:59
mathjax: true
category: DL
tag: 
- deep learning
- TATT
- scene text
---

Paper name: A Text Attention Network for Spatial Deformation Robust Scene Text Image Super-resolution

<!--more-->

The mainly work contributed by this work is providing a noval method to do super-resolution(SR) on low-resolution(LR) scene-text image.

## Model Architecture

The proposed TATT architecture for STISR is shown as follow.

![TATT arch](fdbb9c26f4d7154424ecac6c3edf161.jpg)

***TPGB*** is short for *text prior guided blocks*, ***TPG*** is short for *text prior generator* and ***SRB*** is short for *sequential-recurrent block*.

- Input: low-resolution(LR) text images $Y\in \mathbb{R}^{h\times w\times 3}$
- Text prior generotor (TPG): usually *CRNN* model, input the LR images and output text prior, the recognition probability sequence.
- Convolution (CONV): inputs *low resolution images* and outputs the images features
- TP Interpreter (TPI): two inputs, one is the *text prior* and the other is the *image features*, the outputs is the *TP Map*, which can interpret the text prior into image features. *Attention-based* block.
- Text prior genertor block (TPGB): two inputs, one is the *image features* deliveryed by CNN, and the other is the *text prior map* deliveryed by TPI. Includes 5 *SRB* blocks.
  - Sequential residual block (SRB): proposed in *TSRN* model.
- Pixel shuffle: a method to up-sample the pixel, usually used in super-resolution (SR) tasks. Extend channel dimensions.

### Loss

The total loss is *image loss* adding *recognizer distill loss* 


## Model in codes

The most important function in this codes provided by the authors is `train` defined in `super_resolution.py`, which occupies 822 lines... with a chaotic logic but with no comment. However, we should read the codes to study the model deeply. 

### Data type initialization

There is a class named `AsterInfo` defined in `base.py` which is used not only for `ASTER` model, but also for any other CRNN-like models. This class defines vocabulary and some basic text-sequence parameters.

### Data stream while training

> The most important key to understand the whole model in codes is to grasp the **data stream** in calculations.

We can look up how the TATT model is invoked firstly:

```python
cascade_images, ret_mid = model_list[pick](
    images_lr if not self.args.for_cascading else cascade_images, 
    label_vecs_final.detach()  ## text embedding
)
```

Where the `images_lr` is the **LR images** loaded by `images_lr = self.torch_rotate_img(images_lr, arc, rand_offs)`, for an inversion mode, namely the variable `images_lr_ret` is generated by `images_lr_ret = self.torch_rotate_img(images_lr.clone(), -arc, rand_offs)`.

We continue to look up the parameter `label_vecs_final` and we find that this is calculated by `stu_model`, namely, CRNN model:

```python
stu_model = aster_student[tpg_pick]  ## namely, CRNN
aster_dict_lr = self.parse_crnn_data(cascade_images[:, :3, :, :] if not self.args.y_domain else images_lrraw[:, :3, :, :])
label_vecs_logits = stu_model(aster_dict_lr)
label_vecs = torch.nn.functional.softmax(label_vecs_logits, -1)
label_vecs_final = label_vecs.permute(1, 0, 2).unsqueeze(1).permute(0, 3, 1, 2)
```

Where the function `parse_crnn_data` is to interpolate the LR image (namely the `cascade_images`) into shape `(32, 100)` with `bicubic` interpolation, but the output of this function is a weighted addition image `0.299 * R + 0.587 * G + 0.114 * B` (grey-scale image). So this part outputs the **text priors**.

Continue to follow the data `cascade_images`, which is the output of TATT. Surely we find the loss next: `im_quality_loss = image_crit(cascade_images, images_hr)`, this calculates the <u>image quality loss</u>. The image quality loss includes two parts: *MSE* and *GradientPriorLoss(GPL)*. After a series of tricks (calculate the `loss_img_each`), the loss become *a part* of total loss.

So what's the total loss? There it is: `loss_im = loss_img + loss_recog_distill`.

- the first part `loss_img`: includes *image quality loss (MSE + GPL)* and ***TSSIM loss***, the second item will be introduced later.
- the second part `loss_recog_distill`: comes from *semantic loss* between student model and teacher model.

After that, our optimizer comes on! `optimizer_G.zero_grad()`, which is also the necessary sentence in training. The next is backward propagation `loss_im.backward()`. The model uses `clip_grad_norm_` to prevent gradient explosion. The finally is taking a step `optimizer_G.step()`.

The above data-stream is for *one batch* when training.

### TPG block in code

**The text prior generator block uses CRNN** (can be customized in command argues, the default is CRNN) to extract the text priors.
And the TPG provides two model options, one is the default CRNN, and the other is "TPG"(infact, the CRNN). <u>And we take CRNN as an example, </u> namely the function `CRNN_init` defined in `base.py`, which uses the `CRNN` class defined in `crnn.py` not `Model` class defined in `crnn/model.py`.

### TSRN_TL_TRANS

The other parts of TATT aggregate to one TSRN-like model defined in `tsrn.py`. The initialization in train using `genertor_init()` function and the author put it into `model_list`.

```python
# model includes 1conv block, 5 srb blocks, 1 conv block, 1 upsample block
# defines TPS based STN block
model = tsrn.TSRN_TL_TRANS(
    scale_factor=self.scale_factor, 
    width=cfg.width, 
    height=cfg.height,
    STN=self.args.STN, 
    mask=self.mask, 
    srb_nums=self.args.srb,
    hidden_units=self.args.hd_u
)
```

Firstly we analysis the `forward` function.

- **TPS-based STN**: the input images use *TPS-based STN* to recover the text images to normal shape.
- **convolution with PReLU**: `block = {'1': self.block1(x)}` and `padding_feature = block['1']`
- **TPInterpreter**: in code, it is `infoGen`: `self.infoGen = TPInterpreter(text_emb, out_text_channels, output_size=(height//scale_factor, width//scale_factor))  # InfoGen(text_emb, out_text_channels)` and invoked by `tp_map, pr_weights = self.infoGen(padding_feature, text_emb)`. Its inputs are `padding_feature` and `text_emb` namely image feature and text prior respectively.
- **5 SRBs**: input image feature coming from convolution and TPMap coming from TPI, the final output is also image feature.
- **convolution with batch norm**
- **pixel shuffle**: namely, block 8.
- **tanh**: input the output of block-8.

#### *TPS-based STN

#### TPInterpreter

TPI module aims to ***interpret the text prior to the image feature*** so that the influence of *semantics* guidance can be exerted to the *correlated spatial position* in the image feature domain.
TPI module is transformer-based, the architecture is shown as follow:

![TPI arch](a6d4f983daa6580b91e674f83571322.jpg)

There are <u>two inputs</u> in TPI, one is the *text prior (with shape $(64, 37, 1, 26)$)* (in fact the shape is reshaped into $(64, 26, 37)$ later in forward function) and the other is image feature. Based on the analysis before, we claim that

- *text prior* comes from TPG module, which represents in code with the name `label_vecs_final`
- *image feature* comes from CONV module, which represent in code with the name `block1`

There are only one <u>output</u> in TPI, which is the *text prior map*, *TP map* for short.

There are another modules that are similar two a normal transformer. Firstly, the whole architeture of TPI is divided into **encoder** and **decoder**. *MSA* is short for *multi-head self attention*, *LN* is short for *layer norm*, *FFN* is short for *feed-forward network* and *MCA* is short for *multi-head cross attention*. The introduction of <u>attention</u> will be analysised later (not in this article).

But we concern the ***position encoding*** firstly, *FPE (Fixed Positional Encoding)* for text prior and *RPE (Recurrent Positional Encoding)* for image feature.

The `TPInterpreter` initialized with parameters:

```python
## definition of TPI
class TPInterpreter(nn.Module):
    def __init__(
        self,
        t_emb,
        out_text_channels,
        output_size=(16, 64),
        feature_in=64,
        # d_model=512,
        t_encoder_num=1,
        t_decoder_num=2,
    ): pass
```

- `text_emb = 37`
- `out_text_channels = 64`
- `output_size = (height//scale_factor, width//scale_factor) = (16, 64)`

For invoking, the `forward` function takes in two parameters `image_feature` and `tp_input` (text prior) and the outputs of TPI are `text_prior, pr_weights` where the first is the `TP map` we need:

```python
## definition of forward in TPI
def forward(self, image_feature, tp_input):
  pass
  return text_prior, pr_weights

## invoke in TATT model's forwrad function
tp_map, pr_weights = self.infoGen(padding_feature, text_emb)

## invoke of TATT model
cascade_images, ret_mid = model_list[pick](
    images_lr if not self.args.for_cascading else cascade_images, 
    label_vecs_final.detach()  ## text embedding
)
```

The `image_lr` is passed into `infoGen` after a convolution operation, and the `label_vecs_final` is passed into `infoGen` directly and returns the `tp_map, pr_weights` to TATT model. TATT model uses `tp_map` later in *SRB* blocks to guide SR.

> Now analysis the details in `forward` and `__init__`:
> 
> - `forward`: we catch the data stream firstly in this function, and find the definitions in initialization function.
>   - The `image_feature` is reshaped into $(16\times 64, N, 64)$ firstly (`flatten operation`, where 16:width, 64:height, N: batch size, 64:channels). And it's passed into `InfoTransformer` later directly.
>   - The `tp_input` is reshaped into $(64, 26, 37)$ firstly, and goes to the `PReLU` activation and a `fully connected` layer which are used for projection.
>   - Defines `PositionalEncoding`
>   - Passes all those variables into `InfoTransformer`
>   - returns `text_prior` (text prior map namely)

**>> InfoTransformer**

Defined in `transformer_v2.py`, which <u>mainly realizes the TPI module</u>. Its `forward` function is `def forward(self, src, mask, query_embed, pos_embed, tgt=None, text_prior=None, spatial_size=(16, 64)): pass`.

- `src`: reshaped text prior, namely the `tp_input` with shape $(64, 26, 37)$
- `mask`: with shape $(64, 26)$
- `query_emb`: `self.init_factor.weight` namely, which is `nn.Embedding(1024, 64).weight`
- `pos_emb`: `x_pos` passed in TPI, the result of `PositionalEncoding`
- `tgt`: `x_im` namely the `image_feature` with shape $(16\times 64, N, 64)$

After entering the `forward`, `query_emb` is *firstly* passed into `GRU` to encode.

- why call `query_emb`: because in decoder, this variable is passed into a multi-head cross attention module and acts as the query.

Different from normal transformer, this transformer has only <u>1 layer</u> of encoders and <u>2 layers</u> of decoders.

**>>> InfoTransformer.encoder**

`self.encoder = TransformerEncoder(encoder_layer, num_encoder_layers, encoder_norm)`, use `TransformerEncoderLayer` and `LayerNorm`.

- `TransformerEncoderLayer`: ***adds positional encoding and the original tensor***, use `forward_post` function, same with the architecture image. The ***FPE*** realized with `PositionalEncoding`. [Positional Encoding ref.](https://zhuanlan.zhihu.com/p/338592312)

**>>> InfoTransformer.decoder**

`self.decoder = TransformerDecoder(decoder_layer, num_decoder_layers, decoder_norm,return_intermediate=return_intermediate_dec)`, use `TransformerDecoderLayer_TP` and `LayerNorm`. The invoking: `hs = self.decoder(tgt, memory, memory_key_padding_mask=mask, pos=pos_embed, query_pos=query_embed)`

- `TransformerDecoderLayer_TP`: the input `query_embed` has been encoded in `GRU`, `memory` is the output of `encoder`, `pos_embed` is the text prior positional encoding, `tgt` is the image feature.

#### SRB

SRB block is firstly proposed in <u>*Scene Text Image Super-Resolution in the Wild*</u>, where the SR task on scene text image is firstly proposed. The architecture of SRB is shown as follow:

![SRB](13a2cc443e1599f3b5c488d318af722.jpg)

However, the *BiLSTM* block is replaced by *GRU* block in this work.

#### Pixel Shuffle

Up-sample in *channel* dimmension.

### SSIM Loss

SSIM (Structure Similarity Index) loss is used to compare the similarity between two images, which is sensitive to local structure variance. The loss can be divided into 3 parts: illuminance, contrast ratio and structure, the formulas are:

$$
illuminance(x, y) = \frac{2\mu_x\mu_y + c_1}{\mu_x^2 + \mu_y^2 + c_1}, contrast(x ,y) = \frac{2\sigma_x\sigma_y + c_2}{\sigma_x^2 + \sigma_y^2 + c_2}, structure(x ,y) = \frac{\sigma_{xy} + c_3}{\sigma_x\sigma_y + c_3}
$$

The combination of the 3 parts is our SSIM loss.

$$
SSIM(x ,y) = \frac{(2\mu_x\mu_y + c_1)(2\sigma+c_2)}{(\mu_x^2 + \mu_y^2 + c_1)(\sigma_x^2 + \sigma_y^2 + c_2)}
$$