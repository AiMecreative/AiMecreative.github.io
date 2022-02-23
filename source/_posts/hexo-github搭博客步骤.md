---
title: hexo-github搭博客步骤
date: 2022-01-13 16:17:02
tags: 随笔
category:
- SEU_Study
---

“大家有问题可以来问我，我可以帮你们去查。”

“就你家有网？”

<!--more-->


# hexo-github搭博客步骤
## 安装、环境配置（略）
## 连接本地库和远程库
_**(免责声明：首先说本人毫无使用git和hexo的经验，如果我敲的逻辑有问题或者解释完全错误，不要打我；其次如果按我这样写有问题，那我不管，反正我搭完了)**_
:stuck_out_tongue_winking_eye:

以我为例

打开git bash
```
mkdir D:/Documents/Repo/Blog  // 创建存放博客的空文件夹
cd D:/Documents/Repo/Blog  // 转到此文件夹
npm install -g hexo-cli  // 下 hexo
hexo init  // 此处会认定你的分支名为master，若想更换名字，见文末[1]代码
npm install
git init  // 生成.git隐藏文件夹
git remote add origin https:/ /github/your_user_name/your_user_name.github.io// 将自己的仓库设置为远端(remote),叫做origin
git add --all  // 将内容上传至本地库
git commit -m "initail commit"  // 提交至暂存区(-m 后面接本次提交的注释)
git push origin master  // 将暂存区的内容同步至远端库
hexo g  // hexo 生成网页内容 (generate)
hexo d  // hexo 部署网页内容 (deploy)
hexo s  // 运行服务器查看预览效果 (server)
```

## 附录
1. 更换分支名
```
git branch old_name new_name
```
2. 创建新的post文件
```
hexo new post "post_name"
```
