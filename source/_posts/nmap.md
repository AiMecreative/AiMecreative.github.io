---
title: Nmap基本使用
date: 2022-01-25
tags: 网络安全
---

"诸神之眼 ! "

"千万不要干坏事儿哦 ! "

<!--more-->

**本文内容主要来自:**

https://www.cnblogs.com/php09/p/10530057.html

https://www.cnblogs.com/machangwei-8/p/10353004.html

https://blog.csdn.net/Kris__zhang/article/details/106841466

# 原理

nmap拥有许多协议包.

Nmap 默认发送一个arp的ping数据包，来探测目标主机在1-1000范围内所开放的端口。

# 常用命令
格式:  
```nmap
nmap [Scan Type(s)] [Options] {target specification}
```

注意: 扫描的时候发现很多时候是没有结果的, 大部分情况的原因是防火墙, 如果觉得妨碍, 关了 (被扫描主机的防火墙) 就行.

命令:  

nmap target_ip  # 扫描目标ip

nmap ip_1 ip_2 ... ip_n  # 同时扫描多个ip

nmap xxx.xxx.x.xxx,xxx,...,xxx

nmap -vv ip  # 显示扫描的过程 (vividly)

nmap -p (range) <target IP>  # 指定扫描的端口号范围, 多个范围可以用','表示并集

nmap xxx.xxx.x.*  # 使用通配符扫描整个子网的IP

nmap -iL xxx.txt  # 扫描txt文件中的IP地址

nmap xxx.xxx.x.xxx-xxx  # 指定IP范围

nmap xxx.xxx.x.* --exclude xxx.xxx.x.xxx  # 排除不想扫描的IP, 可以是多个ip

nmap xxx.xxx.x.* --exludefile xxx.txt  # 排除不想扫描的IPlist.txt

nmap -A xxx.xxx.x.xxx  # 启用操作系统和版本检测，脚本扫描和路由跟踪功能

nmap -sP xxx.xxx.x.xxx  # Ping扫描, 效率高, 返回信息少

nmap -PN(or P0) xxx.xxx.x.xxx  # 无Ping扫描,可以躲避防火墙防护,可以在目标主机禁止ping的情况下使用 (依然可能被墙)

-PS: TCP SYN Ping扫描

-PA: TCP ACK Ping扫描

-PR: ARP Ping扫描

-n: 禁止反向解析

-T: 时序选项, -TO-T5. 用于IDS逃逸,0=>非常慢,1=>缓慢的,2=>文雅的,3=>普通的,4=>快速的,5=>急速的

-F: 快速扫描 (扫描端口数减少)

-f: 报文分段

**未完待续...**

对小白 **(指我)** 不友好的名词:

* 子网, 网段, 局域网, SYN, ACK, ARP, IDS, 报文, 