---
title: 【从零开始的C++】IDE安装和配置
date: 2023-09-19 00:54:18
tags: 
- CS
- 助教
- C++
Author: AndrewRey
category: CS
---
"第0节课"

<!--more-->

> 前前言：只适用于Windows

> 前言：建议使用VisualStudio2019，可以有一个舒适的coding环境~~（来自个人偏见）~~，当然DEV-C++的优点在于简单方便，VS有点笨重了
>
> - 欢迎大家折腾VSCode，可以熟悉CMake构建工程
> - 初学还是建议VisualStudio

> **啥是IDE**
>
> - IDE：Integrated Development Environment，集成开发环境
> - 集成了 **编辑器（理解为打字的界面）**、 **编译**、 **调试**等主要功能
> - 当然也集成了一些代码高亮、自动补全等功能
> - 目的是提高coding体验

### 准备工作

- 在SEU文档云（群里面的链接）里面下载想用的IDE安装包
- **不要下载到C盘（选择安装路径时，点击“浏览”，然后选择除了C盘以外的盘进行安装）**
  - 比如下载到D:/LoveCpp/vs这个路径下面
- 貌似VisualStudio2010也在网盘里面（就是那个2G多的文件，可以不用下载，以后特殊情况可能用到，但问题不大）

### VisualStudio2019安装和配置

> 对应压缩包 `vs_enterprise__2019.zip`

可以参考网站：[这个](https://blog.csdn.net/InnerPeaceHQ/article/details/121716088)

- 解压，文件夹里面是这个东西

![1695057304137](1695057304137.png)

- 管理员权限运行即可（会有对话框，同意即可）
- 运行后会有一个VS的弹窗，点击继续即可
- 继续后出现如下界面

![1695057447568](1695057447568.png)

- 下面开始安装C++环境

![1695057753734](1695057753734.png)

- 点击安装后只需要耐心等待（下面那个VS不用管，那是我之前装的）

![1695057843665](1695057843665.png)

- **安装完成后需要重启**

> 重启后，安装完成，可以在开始目录/搜索框中找到VS，打开即可

![1695058038603](1695058038603.png)

- 如果出现了登陆界面，可以选择以后再说，也可以用微软账户登陆

**恭喜你，到此为止，你已经成功安装了VisualStudio2019！！！**

### Dev-C++安装

> 对应文件 `Dev-Cpp 5.11 TDM-GCC 4.9.2 Setup.exe`

- 直接运行exe可执行文件，得到如下界面，并选择English点击OK

![1695058487870](1695058487870.png)

- 然后会出现一个协议，想看就看一下，点击I Agree

![1695058532086](1695058532086.png)

- 出现下图，直接继续Next

![1695058637180](1695058637180.png)

- 选择Browse浏览，选择一个除了C盘以外的路径安装，然后点击Install安装
- 安装完成后点击Finish，然后打开DEV-C++

![1695058832613](1695058832613.png)

- 语言选择简体中文，其它默认即可

**恭喜你成功安装了Dev-C++！！！**

### Hello World!——第一个程序

> **一件重要的事情**
>
> - 在除了C盘的其它盘（比如D盘）创建一个文件夹，专门用于存放C++项目，比如下面这个文件结构：
>
> ```
> +-D:
>   |
>   +-CppProjects
>         |
>         +-project0
>         |    |
>         |    +-some-project-files...
>         +-project1
>         +-project2
>         +-...
> ```

#### 在VisualStudio2019里面写代码！

> 强烈建议看这个[教程](https://blog.csdn.net/BaoITcore/article/details/129440505)，一定要注意，选择项目位置的时候选用 **我们在上面两行中创建的文件夹（不是教程中的C盘路径），路径中不能含有中文（不然以后会出现一些神秘的错误）**
>
> - 示例位置：D:/CppProjects/project0

> 所以是不是输出了HelloWorld呢？

#### 在DEV-C++里面写代码！

> 建议看这个[教程](http://c.biancheng.net/view/462.html)，里面的代码使用与上面VS教程中一样的代码，并将保存的文件命名为 `xxx.cpp`（也就是以cpp为后缀）

### 觉得不好玩？

不如把下面这几个代码贴过去看看？

> 快速排序算法

```c++
#include <iostream>
#include <vector>


int hhh(std::vector<int> &a, int left, int right) {
  auto i = left;
  auto j = right;
  auto key = a[left];

  while(i != j) {
    while(i < j && a[j] >= key) j--;
    while(i < j && a[i] <= key) i++;
    std::swap(a[i], a[j]);
  }
  std::swap(a[left], a[i]);                              
  return i;
}

void qs(std::vector<int> &a, int left, int right) {
  if( left >= right ) return;
  auto i = hhh(a, left, right);
  qs(a, left, i - 1);
  qs(a, i + 1, right);
}

void pr(std::vector<int> a) {
  for (auto v: a) {
    std::cout << v << ", ";
  }
  std::cout << std::endl;
}

int main() {
  std::vector<int> vec {5, 10, 9, 3, 20, 1, 0, -5, -10};
  std::cout << "former array is:" << std::endl;
  pr(vec);
  qs(vec, 0, vec.size() - 1);
  std::cout << "now array is:" << std::endl;
  pr(vec);
  return 0;
}

```

输出结果是这样的：

![1695061391905](1695061391905.png)

可以看见原本凌乱的数组被从小到大排好了序。

> 感兴趣的话可以查看[这个博客](https://www.cnblogs.com/MAKISE004/p/16909610.html)
