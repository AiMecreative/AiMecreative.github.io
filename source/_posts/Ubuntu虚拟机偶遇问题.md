---
title: Ubuntu虚拟机偶遇问题
date: 2022-01-25 10:42:43
tags: 随笔
category:
- SEU_Study
---

"一杯茶一根烟, 一个bug调一天."

"吸烟有害健康."

<!--more-->

# 网络问题
### 突然上不了网
2022.1.25这一天, 本来想下个 nmap , 突然告诉我下载失败, 提示信息显示的是 *暂时无法解析域名*

我就纳闷了, ping 了一下百度, 它告诉我 www.baidu.com 无法解析 ???

可是我昨天还可以解析的啊...

不管了, 85% 的问题都可以通过重启解决. 于是我把虚拟机和主机都分别重启了一遍, 温和地敲了密码, 耐心等了一会儿, 发现还是没有联网.

然后我查看了一下我的网卡配置:

```ifconfig```

??? 只显示了本地回环的IP. 

绝了.

然后在 settings 的 network 里面, 我本以为是把网络关了, 打开后发现甚至没有开关这个选项...

上网查! 结果自然是喜忧参半的.

喜, 是因为我找到了很多解决方案; 忧, 是因为我不是第一个发现这个 bug 的人.

**解决 :**  
* 删除NetworkManager缓存文件, 参考: https://www.cnblogs.com/liuhanxu/p/15550864.html

```bash
sudo service NetworkManager stop 
sudo rm /var/lib/NetworkManager/NetworkManager.state
sudo service NetworkManager start
```

然后就可以了, 我真无语.