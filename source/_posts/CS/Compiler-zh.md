---
title: Compiler-zh
date: 2022-09-05 16:23:27
category: CS
---

"编译原理网课"

"B站大学不用交学费!!!"

<!--more-->

# 引论

**编译**: 由高级语言转化为低级语言

**解释**: 接受高级语言的 **一个语句输入**, 进行解释并执行, 立刻得到执行结果, 然后再接受下一句.

- 不产生目标文件, 直观易懂, 结构简单, 易于人机对话
- 但效率低: 没有目标文件, 每次运行相当于要重新解释

**编译的两个转换形式**

- 编译 - 运行
  - 先编译产生机器语言, 生成目标文件(.exe), 在运行时添加参数
- 编译 - 汇编 - 运行
  - 编译后产生汇编语言, 生成目标文件(.obj), 汇编语言汇编后产生机器语言

**编译过程**

源程序 -> Lexical analyzer -> Syntax analyzer -> Semmantic Analyzer -> Intermediate code generation -> Optimization -> Code generation -> Target

symbol table management, error handler

## 词法分析 Lexical Analysis

扫描源程序, 识别一个个 **单词lexeme**, 并进行 **分类token** (包括: keyword, constant, identifier, operator, separator). 转化后的格式为 <token-name, attr-value>, 前者为token, 后者为 **指向符号表的指针**.

描述词法规则的有效工具是 **正规式**和**有限自动机**

## 语法分析 Syntax Analysis

把单词符号组成各类各类的语法单位, 如短语, 句子, 过程, 程序等

方法: 

- derive:
  - 最右推导: 每次将最右的部分按照规则进行转化
  - 最左推导:
- reduce: 推导的逆过程
  - 最左归约: 最右推导的逆过程
  - 最右归约: 最左推导的逆过程

计算机处理方法: **语法树**

## 语义分析 Semmantic Ananlysis

审查源程序有无语义错误, 为代码生成阶段收集类型信息. 重要的一步是 **类型检查**

## 中间代码生成 Intermediate Code Generation

中间代码设计原则

- 容易生成
- 容易翻译为目标代码

中间代码形式: 四元式, 三元式, 逆波兰式

- 四元式: <运算符, 操作数1, 操作数2, 结果>

## 优化 Optimization

原则: **等价变换**

主要方面: 公共子表达式的提取, 合并已知量, 删除无用语句, 循环优化

## 目标代码生成 Code Generation

将经过优化的中间代码转化为特定机器上的低级语言

目标代码的形式:

- 绝对指令代码: 可立即执行的目标代码, 纯粹的0-1代码.
- 汇编指令代码: 汇编语言程序, 需要通过汇编程序汇编后才能运行, 能和物理机隔离.
- 可重定位指令代码: 先将各目标模块连接起来, 确定变量, 常数在主存中的位置, 装入主存后才能成为可以运行的绝对指令代码, 而后还需要进行 **链接**.

## 表格管理 Symbol Table Management

用来记录源程序的各种信息和编译过程中的各种状况.

与编译前三段有关的表格有: 符号表, 常数表, 标号表, 分程序入口表, 中间代码表
<!-- 
### 符号表

| name | information |
|------|-------------|
| m | 整型, 变量地址 |
| n | 整型, 变量地址 |

### 常数表

|value|
|-----|
|1|
|4|

### 标号表

|name|information|
|----|-----------|
|xx|某句话|

*某句话是在 -->

## 错误处理 Error Handler

如果源程序出错, 编译程序应该设法发现错误, 并报告给用户.

## 其他概念

**趟/遍 pass**: 将源程序从头到尾扫描一遍, 做相应的加工处理, 并生成相应的中间代码和目标代码. 多遍扫描可以节省内存空间, 提高目标代码质量, 使编译的逻辑结构更清楚, 但编译时间长, 因此 no free launch.

因此在一遍编译中:

源程序 -> 编译程序 -> 目标代码

**编译程序的编写**

- 直接用机器语言
- 用汇编语言编写, 编译程序的核心部分常用汇编语言编写
  - 编译程序怎么生成? 编译程序是用汇编语言编写的, 汇编语言经过汇编后即可生成编译程序(可执行), 再利用这个编译程序将自己的源代码变为目标代码.
- 用高级语言编写, 普遍采用的方法.
  - 例如用C语言写成的编译程序, 则先用C语言的编译器将C源程序编译为exe, 再用于分析其他语言, 也可以是C语言.
- 自编译
  - 先编写一个很小的编译程序的核心, 再由这个核心逐渐去分析, 编译其他代码.
- 编译工具: LEX(词法分析), YACC(语法分析)
- 移植: 同种语言的编译程序在不同类型的机器之间移植

# 编译基础

高级语言是一个记号系统. 

- 语法
- 语义

**语法** 包括 **词法规则** 和 **语法规则**

- 词法规则: 判断每一个"单词"是否正确, 规定了哪些符号是是单词符号(最基本结构; 常数, 标识符, 基本字, 算符, 界限符等); 用正规式和有限自动机描述和分析
- 语法规则: 结合单词是否是语言中的语法单位(表达式), 规定如何用单词形成语法单位, 包括表达式, 子句, 语句, 函数, 过程, 程序等.

**语义** 给出单词符号和语法符号的意义, 大多数编译程序使用基于属性文法的语法制导翻译方法来分析语义.

重点是正规文法, 上下文无关文法及其对应的有限自动机和下推自动机.

## 一些概念

**字母表**: 符号的非空有穷集合, 用$V, \Sigma$表示. 所使用的符号均出自字符表.

**符号**: 语言中最基本的不可再分的单位.

**符号串**: 字符表中符号组成的有穷序列. **空串** 用$\epsilon$表示.

**句子**: 字母表上符合某种规则构成的串

**语言**: 字母表上句子的集合

*小写字母表示符号, 大写字母表示集合, 希腊字母表示符号串.

### 运算

**连接(乘积)运算**

$$
\begin{aligned}
  A &= \{\alpha_1, \alpha_2, \cdots\} \\
  B &= \{\beta_1, \beta_2, \cdots\} \\
  def:\quad AB &= \{\alpha \beta | \alpha\in A\ and\ \beta\in B\}
\end{aligned}
$$
其中$A,B$是串集.
规定: $A^0=\{\epsilon\}$. 注意该运算 **非可交换**. 例子: $\alpha$表示`if ()`, $\beta$表示`then()`.

**闭包**

$$
A^\star=A^0\cup A^1 \cup A^2 \cup \cdots
$$

由A上所有符号组成的所有串的集合.

**正闭包**

$$
A^{+} = A^1 \cup A^2 \cup A^3 \cup \cdots = A^\star - {\epsilon}
$$

**文法**

描述语言的语法结构规则

- **非终结符**: 出现在规则的左部, 用"<>"括起来或用大写字母表示, 表示一定语法概念的词, 用$V_N$表示
- **终结符**: 语言中不可以再分割的字符串, 用$V_T$表示
- **开始符号**: 表示所定义的语法范畴的非终结符, 表示该文法中最大的一个语法成分 (?比如说一个句子)
- **产生式**: 是用来定义符号串之间关系的一组语法规则, $A\rightarrow \alpha$
- **推导**: 推导是从开始符号开始, 通过产生式的右部取代左部, 最终产生语言的一个句子的过程.
  - **最左推导**: 每次使用一个规则, 以其右部取代符号串最左的非终结符.
- **归约**: 推导的逆过程, 从给定的源语言的一个句子开始, 通过规则的左部取代右部, 最终达到开始符号的过程.
  - **最左归约**: 最常采用
- **句型**: 从文法的开始符号$S$开始, 每步推导(包括0步推导)所得到的字符串$\alpha$. 记作$S\rightarrow^\star \alpha, where\ \alpha\in (V_N \cup V_T)^\star$
  - **句子**: 仅含终结符的句型, 若能归约为开始符号, 则该句子是正确的
- **语言**: 语言是由开始符号$S$通过1步或1步以上推导所得的句子的集合, 记为$L(G)=\{\alpha|S\rightarrow^+\alpha,\alpha\in V_T^*\}$
- **文法规则的递归定义**: 非终结符的定义中包含了非终结符自身

## 文法与语言的形式定义
Chomsky对文法的定义: 文法G是一个四元组$(V_N, V_T, P, S)$, 其中$P$是文法规则的集合, $S$是开始符号

**0型文法**

又称短语文法或者无限制文法. $P$中产生式$\alpha\rightarrow\beta,\alpha\in V^+=(V_N\cup V_T)^+$, $\alpha$至少含有一个非终结符,$\beta\in V^\star$.

- 对产生式限制最少
- 图灵机
- 可递归可枚举

**1型文法**

$P$中产生式$\alpha\rightarrow\beta$, 除可能有$S\rightarrow \epsilon$外均有$|\beta|\geq|\alpha|$, 若有$S\rightarrow\epsilon$, 规定$S$不能出现在产生式的右部.

等价定义: $P$中产生式$\alpha\rightarrow\beta$除了可能有$S\rightarrow\epsilon$外均有$\alpha S \beta \rightarrow \alpha \gamma \beta, \alpha, \beta \in V^\star, A\in V^n, \gamma\in V^+$.

{%note info%}
对非终结符进行替换时, 必须考虑上下文, 并且一般不允许替换为$\epsilon$, 除非是开始符号产生$\epsilon$.
{%endnote%}

**2型文法**

$P$中产生式具有形式$A\rightarrow\beta, A\in V_N, \beta\in V^\star$. 要求产生式左边只有一个非终结符.

不必考虑上下文, 上下文无关文法.

识别2型文法的自动机称为下推自动机

**3型文法**

$P$中产生式具有形式$A\rightarrow \alpha B, A\rightarrow \alpha$或者$A \rightarrow B\alpha, A\rightarrow \alpha, A,B\in V_N, \alpha\in V_T^\star$. 也称为正规文法, (左|右)线性文法, 识别3型文法的自动机称为有限自动机.

{%note info%}
词法分析和语法分析中对产生式的限制: 1)不产生$P\rightarrow P$, 2)产生式中出现的任何非终结符必须有用, 能经过若干步推导出终结符
{%endnote%}

**一些例子**

**例1** 语言$L=\{\omega|\omega\in(a,b)^\star$且$\omega$中含有个数相同的$a,b\}$, 构造生成该语言的文法:

$$
\begin{align*}
  S&\rightarrow\epsilon \\
  S&\rightarrow aA\\
  S&\rightarrow bB\\
  A&\rightarrow aAA | bS\\
  B&\rightarrow aS | bBB
\end{align*}
$$

解释: 要么以$a$开头, 要么以$b$开头, 后面跟着符号串. 对于符号串$A$, 如果以$b$开头, 则后面跟着$ab$个数相等的符号串, 如果仍然以$a$开头, 此时后面必须还要至少出现两次$b$.

或者

$$
\begin{align*}
  S&\rightarrow\epsilon\\
  S&\rightarrow aSbS\\
  S&\rightarrow bSaS
\end{align*}
$$

解释: 若以$a$开头, 则在字符串的某个位置必然出现一个$b$, 而这两个$a,b$中间是$ab$个数相等的的字符串, b后面也是$ab$个数相等的符号串.

**例2** 设$L=\{\omega | \omega\in(0,1)^\star$且$1$的个数为偶数个$\}$, 构造生成该语言的文法:

可以先列出看一下:

$$
\omega\in\{\epsilon, 0, 11, 011, 101, 110,\cdots\}
$$

然后:

$$
\begin{align*}
  S&\rightarrow\epsilon\\
  S&\rightarrow 0S\\
  S&\rightarrow 1A\\
  A&\rightarrow 1S | 0A
\end{align*}
$$

## 文法的构造与简化

### 简化

同一语言可以产生不同的文法, 选择产生式最少, 最符合语言特征的文法来描述; 有些产生式对推导不起作用, 包括: **推导中永远用不到, 永远导不出终结符的, 形如$P\rightarrow P$的...**

**一些例子**

**例1** 简化文法:

$$
\begin{align*}
  S&\rightarrow Be\\
  S&\rightarrow Ee\\
  A&\rightarrow Ae\\
  A&\rightarrow e\\
  A&\rightarrow A\\
  B&\rightarrow Ce\\
  B&\rightarrow Af\\
  C&\rightarrow Cf\\
  D&\rightarrow f
\end{align*}
$$

显然应该保留0236.

### 构造

**构造无$\epsilon$产生式的上下文无关文法**

满足: $P$中要么不含有$\epsilon$产生式, 要么只有$S\rightarrow\epsilon$, 且若$S\rightarrow\epsilon$, 则$S$不出现在任何产生式右部.