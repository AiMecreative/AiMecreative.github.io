---
title: hexo-github搭博客步骤
date: 2022-01-13 16:17:02
tags: 随笔
---

“大家有问题可以来问我，我可以帮你们去查。”

“就你家有网？”

<!--more-->


# hexo-github搭博客步骤
## 安装、环境配置（略）
## 连接本地库和远程库
以我为例

打开git bash
```java
mkdir D:/Documents/Repo/Blog  // 创建存放博客的空文件夹
cd D:/Documents/Repo/Blog  // 转到此文件夹
npm install -g hexo-cli  // 下 hexo
hexo init  // 此处会认定你的分支名为master，若想更换名字，见文末[1]代码
npm install
git init  // 生成.git隐藏文件夹
// 将自己的仓库设置为远端(remote),叫做origin
git remote add origin https:/ /github/your_user_name/your_user_name.github.io
// 将内容上传至本地库
git add --all
// 提交至暂存区(-m 后面接本次提交的注释)
git commit -m "initail commit"
// 将暂存区的内容同步至远端库
git push origin master
// hexo 生成网页内容 (generate)
hexo g
// hexo 部署网页内容 (deploy)
hexo d
// 运行服务器查看预览效果 (server)
hexo s
```
