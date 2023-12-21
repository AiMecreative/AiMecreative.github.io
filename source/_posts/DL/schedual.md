---
title: DeepLearning | Schedual
author: Andrew-Rey
date: 2023-11-23 12:04:03
category: Dl
tag: 
- deep learning
- schedual
---


### 任务

1. 场景文本图像增强与识别（Scene Text Image Super-Resolution & Recognition ），这个任务是需要设计一个co-training的模型，能够既提升图像质量又提升下游识别器的识别性能，所以需要对场景文本图像超分辨率（这个任务的目标是放大场景图像图像的尺寸后（如32 x 128变为64 x 256），仍能保持良好的图像质量和文本识别模型的识别效果）以及场景文本图像识别具有一定的基础知识铺垫
2. 模型基本结构是统一的encoder，然后有两个decoder分别负责 超分和识别

### 相关论文

1. STISR：需要掌握的模型有20-ECCV-TSRN（创立这个任务的）、22-CVPR-TATT（一个比较好的学习代码的模型）、23-MM-STIRER
2. STR：需要掌握的模型有22-IJCAI-SVTR、22-ECCV-PARSeq、23-ICCV-CCD
3. Transformer与对比学习：李宏毅2021春机器学习课程视频：https://www.bilibili.com/video/BV1Wv411h7kN?p=49&vd_source=7e3e00e12a59319e12d36c03a368ada5 & 跟李沐学AI：https://www.bilibili.com/video/BV1C3411s7t9/?spm_id_from=333.788&vd_source=7e3e00e12a59319e12d36c03a368ada5  &  https://www.bilibili.com/video/BV19S4y1M7hm/?spm_id_from=333.788&vd_source=7e3e00e12a59319e12d36c03a368ada5

### 计划与安排

1. 目前的计划安排：
   1. 接下来一周阅读这两个方向的论文（每个方向1篇）并学习代码，并于一周后参与组内讨论，对论文进行分享
   2. 随后根据分享与讨论情况布置后续工作与任务安排
   3. 后续深造期间的研究方向以这个工作为契机了解场景文本图像相关的内容后再进行确定
   4. 毕设方面严卡节点：包括论文翻译、开题报告与答辩、中期、毕业论文（4月底-5月下旬需要撰写论文（3-4周）（即在此节点之前核心实验与算法需要跑完，写论文过程中可以继续增加消融实验），审核并修改（约需2轮，1周）），尽量提前

### 其他

1. 科研常用的工具：
   1. Typora：非常好用的Markdown文本编辑器
      1. https://github.com/Keldos-Li/typora-latex-theme Latex风格的基于Typora的md排版
   2. Mathpix：对公式进行截图并转换成Latex模板
   3. Axmath与Axglyph：国产的可视化公式编辑与画图软件，可插入office等
   4. [TablesGenerator](https://www.tablesgenerator.com/)：在线的表格转latex工具
   5. 网易有道词典：浮窗状态下可右键查询单词
   6. [PaperwithCode](https://paperswithcode.com/)：论文开源项目推荐与索引网站，包含各种任务的排行榜
   7. [Readpaper](https://readpaper.com/)：论文阅读、要点介绍与细节讨论
   8. 坚果云：多设备文件与数据的云备份与更新
   9. **Notion：关系型文档数据库**（重要，我们Group一般用这个进行交互）
      1. [一个硬核程序员向的notion任务规划导向的搭建](https://www.bilibili.com/video/BV1S541197f7?share_source=copy_web)
   10. everything：快速的电脑全局搜索工具
2. 有任何问题可以及时跟我沟通，我们的小组会一般是每周日下午2点30（需要尽量参加），薛老师大组会2周一次（一般是周二下午）

