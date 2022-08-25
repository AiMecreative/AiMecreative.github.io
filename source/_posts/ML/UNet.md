---
title: Image Semantic Segmentation based on UNet
date: 2022-08-21 10:50:30
category: ML
mathjax: true
---

"Semantic segmentation of images, use UNet model."

<!--more-->

# Abstract

In this project, we realized an basic UNet model and UNet++ model, then we put them on image semantic segmentation. Here we will show our basic theory of UNet and an improvement of it, and we provide part but main code of this program, finily, we give the result of segmentation images, loss-curve and accuracy-curve on both train and validation set.

The copyright of this program is owned by our team mentioned on the end.

# UNet Structure

The [paper](https://arxiv.org/abs/1505.04597) published in 2015 proposed a noval network structure, whose shape is similar with captal "U". The idea comes from FCNN. U-Net is one of the class of "Encoder-Decoder" structure.

![U-Net Structure](unet-structure.png)

The piror half of the network is "encoder". The input image passes covolution kernel, and then passes the pooling layer (or other dimension-decreasing layer). The opposite of that is the post part of UNet, the "decoder". The input of decoder is a sequence of feature maps that with highly contracted pixels. The output of the decoder (or the whole network) is an image with the same shape of input image, where each pixel has its own class.

In this project, we decreased the convolutional layers, making there are only two convolutional layer in each convolutional kernel as the dataset includes images with shape $128\times 256$.

## Operator Definitions

**Convolutional Kernel:**

We defined the basic convolutional kernel as following:

```python
self.layer = nn.Sequential(
    # in_channel, out_channel, kernel_size, stride, padding
    # batch size * channel * height * weight
    nn.Conv2d(C_in, C_out, kernel_size=(3, 3), stride=(1, 1), padding=1),  # 64 64 128 256
    nn.BatchNorm2d(C_out),
    nn.Dropout(0.2),
    nn.LeakyReLU(),

    nn.Conv2d(C_out, C_out, kernel_size=(3, 3), stride=(1, 1), padding=1),  # 64 64 128 256
    nn.BatchNorm2d(C_out),
    nn.Dropout(0.5),
    nn.LeakyReLU(),
```

It including two convolution operations.

**Down Sampling Kernel:**

As for downsampling kernel, we replaced conditional pooling layer to convolutional layer with stride equaling to 2, which means the shape will be shrunk to $\frac{1}{2}$ while remaining the same channels.

```python
self.Down = nn.Sequential(
    nn.Conv2d(C, C, kernel_size=(3, 3), stride=(2, 2), padding=1),  # 64 64 64 128
    nn.LeakyReLU()
        )
```

**Up Sampling Kernel:**

The basic structure of up-sampling contains only one convolutional layer with $1\times 1$ convolutional kernel size and half out-channel. The feature map should passes an interpolation layer before get in the convolutional layer.

```python
def __init__(self, C):
    super(UpSampling, self).__init__()
    # out-channel = 1/2 in-channel
    self.Up = nn.Conv2d(C, C // 2, kernel_size=(1, 1), stride=(1, 1))

    def forward(self, x, r):
    # neighbor interpolation
    up = F.interpolate(x, scale_factor=2, mode="nearest")
    x = self.Up(up)
    # concatenate the feature map in encoder and 
    # the feature map in corrsponding decoder layer, in channel dimension
    res = torch.cat((x, r), 1)
    return res
```

The interpolation mode we choose is "nearest". The function `torch.cat(dim=1)` is used to concatenate two feature maps in channel dimension.

## Network Definition

Based on the operators defined above, we link these blocks together like UNet structure.

```python
def __init__(self):
    super(UNet, self).__init__()

    # down sampling
    self.C1 = Conv(3, 64)
    self.D1 = DownSampling(64)
    self.C2 = Conv(64, 128)
    self.D2 = DownSampling(128)
    self.C3 = Conv(128, 256)
    self.D3 = DownSampling(256)
    self.C4 = Conv(256, 512)
    self.D4 = DownSampling(512)
    self.C5 = Conv(512, 1024)

    # up sampling
    self.U1 = UpSampling(1024)
    self.C6 = Conv(1024, 512)
    self.U2 = UpSampling(512)
    self.C7 = Conv(512, 256)
    self.U3 = UpSampling(256)
    self.C8 = Conv(256, 128)
    self.U4 = UpSampling(128)
    self.C9 = Conv(128, 64)

    self.C10 = torch.nn.Conv2d(64, 3, kernel_size=(3, 3), stride=(1, 1), padding=1)
    self.pred = torch.nn.Conv2d(3, 34, kernel_size=(1, 1), stride=(1, 1))
    self.Th = torch.nn.Sigmoid()
```

Like U-Net mentioned in that paper, we designed 4 layer deep network.

```python
def forward(self, x):
        # part 1: down sampling, decreasing dimension
        R1 = self.C1(x)
        R2 = self.C2(self.D1(R1))
        R3 = self.C3(self.D2(R2))
        R4 = self.C4(self.D3(R3))
        Y1 = self.C5(self.D4(R4))

        # part 2: up sampling, connect priori knowledge
        O1 = self.C6(self.U1(Y1, R4))
        O2 = self.C7(self.U2(O1, R3))
        O3 = self.C8(self.U3(O2, R2))
        O4 = self.C9(self.U4(O3, R1))

        # part 3: active function
        return self.Th(self.pred(self.C10(O4)))
```

As you can see, the difference between U-Net and other networks before U-Net is that, U-Net conbines the former infomation from encoder and current infomation from decoder.

# Code

During the training process, we want to keep some infomation of loss values and accuracy values on training set and validation set, so that we can analyze the variance.

In the function named `train()`, we take `optimizer` and `loss` as two parameters used in training process. The outputs of this function are loss and accuracy on both training set and validation set. If we get the data about training set and validation set, we can draw the curves. If both training and validation loss values decrease during training process, we can conclude that our model convergences and do not overfit on training set.

The train step code is show as following:

```python
self.model.train()
for batch in self.train_loader:
    batch_num += 1
    optimizer.zero_grad()
    rgbs, segs = batch
    s, _, m, n = segs.shape
    segs = torch.reshape(segs, (s, m, n))
    pred_segs = self.model(rgbs).to(self.device)
    loss_val = loss(pred_segs, segs)
    loss_val.backward()
    optimizer.step()
```

The data collecting code can be written as following:

**Statistic data of training set**

```python
for ... :
    with torch.no_grad():
        if batch_num % 5 == 0:
            logging.info(f"batch num {batch_num}, loss {loss_val}")
        # delete or add comments when needed
        train_loss += loss_val
        # statistic valid classified samples
        total_pix += s * m * n
        idx = torch.argmax(pred_segs, dim=1)
        train_valid_pix += torch.eq(idx, segs).sum().float().item()
torch.cuda.empty_cache()
epoch_acc = train_valid_pix / total_pix
train_epoch_loss.append(train_loss / batch_num)
train_epoch_acc.append(epoch_acc)
```

**Statistic data of validation set**

```python
self.model.eval()
with torch.no_grad():
    for valid_batch in self.valid_loader:
        valid_batch_num += 1
        rgbs, segs = valid_batch
        s, _, m, n = segs.shape
        segs = torch.reshape(segs, (s, m, n))
        pred_segs = self.model(rgbs).to(self.device)
        loss_val = loss(pred_segs, segs)
        valid_loss += loss_val
        valid_total_pix += s * m * n
        idx = torch.argmax(pred_segs, dim=1)
        valid_valid_pix += torch.eq(idx, segs).sum().float().item()
epoch_acc = valid_valid_pix / valid_total_pix
valid_epoch_loss.append(valid_loss / valid_batch_num)
valid_epoch_acc.append(epoch_acc)
```

The point you should pay attention to is that you should use `with torch.no_grad()` before you do some work that have no relations with training process, otherwise your GPU memory will be full or even overflow.

# Result

After a long time training, we get the satisfying result with U-Net model.

## Former Model

The "former model" infers the U-Net model, and you will see we used other upgraded model named "UNet++", which will be introduced later.

We output the segmentation results and their uncertainties.

![picture 1 result-UNet](pic1-unet.png)

## Model Upgrade

For some reason, we tried other U-Net-like model, Nested UNet, namely UNet++. It has a nested convolutional blocks like a pyramid and there is a chain passing connectivity between each convolutional block every layer.

![Neseted UNet](nested.png)

The black nodes are the same with U-Net model. The green nodes are what Nested UNet newly added. Both green and blue lines are skip pathways that pass connectivities from encoder to decoder.

The use of Nested UNet gave us a little improvement on final results.

![pictrue 1 result-Nested UNet](pic1-nested.png)

# Analysis

## U-Net

We analyzed the loss value and accuracy on both training and validation set:

![unet loss](unet_loss.png)

We find that after 100 epochs, the model has not convergenced yet, but the loss on validation decreases to the bottom. 

![unet accuracy](unet_acc.png)

From the accuracy curves, we find that both training set and validation set have increasing accuracy, which mean our model does not overfit.

## Nested UNet

Meanwhile, we analyzed the loss and accuracy of Nested UNet model on both training and validation set.

![nested loss](nested_loss.png)

We find that Nested UNet has a faster convergency speed than UNet. It uses only about 60 epochs. But to our superrise, we find that Neseted UNet comes to be overfitting after about only 20 epochs because the validation loss does not decrease anymore.

![nested accuracy](nested_acc.png)

The performance on validation accuracy stays the same with UNet model.