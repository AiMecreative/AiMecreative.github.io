---
title: Compilers
date: 2022-07-04 18:17:40
catagory: CS
mathjax: true
---

"From Stanford CS143: Compilers"

<!--more-->

# Intro
## Differences between Compilers and Interpreters
Compilers: get a new program, **off-line**

- **input**: your program
- **output**: executable pragram (assembling, byte code)
  - **input**: data
  - **output**: result

![compiler1](compiler1.png)

![compiler2](compiler2.png)

interpreters: get the same program, **on-line**
- **input**: your pragram, data
- **output**: result

![interpreter1](interpreter1.png)

## Struct
### Lexical Analyzer
The **lexical analyzer** reads the stream of characters making up the source program and groups the characters into meaningful sequences called **lexeme**. The output is **token**. <*token-name, attribute-value*>

![lexeme1](lexeme1.png)

### Syntax Analyzer (Parsing)
The **syntax analyzer** use the components of the tokens produced by the lexical analyzer to create a **tree-like** intermediate representation that depicts the **grammatical strucure** of the token stream.

Interior nodes represent the operations and the children nodes represent the arguments of the operation. 

![syntax1](syntax1.png)

### Semantic Analyzer
The **semantic analyzer** uses the syntax tree and the information in the symbol table to check the source program for semantic consistency with language definetion. The important thing is **type checking**. (check the each operation has matching operands)

- sometimes exits coercion convension

![semantic1](semantic1.png)

The syntax tree is one form of intermediate representations. Many compilers generate an explicit low-level or machine-like intermediate representations for easier translation into target code.

![inter1](inter1.png)

- This is called *three-address code*

### Optimizer
The **optimizer** is used to imporve the intermediate representation to get better target code.

- Better: faster, shorter or less power

![opt1](opt1.png)

The compilers deduce that the conversion from integer to floating point can be done eliminated.

### Code Generator

The **code generator** maps the intermediate representations of the source program into target code. (If the target code is machine language, then the registers or memory locations are selected for each variable used by the program)

- The crucial aspect of the code generator is the judicious assignment of registers to hold variables.

![gen1](gen1.png)

### Symbol Table

The **symbol tabel** is a data structure containing a record for each variable name, with fields for attributes of the name.

- allows compiler to find, store and retrieve record name quickly.

### Some Other Definition
**pass**: Activities from several phases may be grouped together into a **pass** that reads an input file and writes an output file.

### Classification of Languages

Imperative: specifies *how* a computation is to be done, there is a notion of program state and statements that change the state.

- C, C++, C#, Java

Decarative: specifies *what* a computation is to be done

- Functional language: ML, Haskell
- Constraint logic language: Prolog

Von Neumann: computational model is based on von Neumann computer architechure.

- FORTRAN, C

object-oriented: consists a collection of objects that interact with each other.

- C++, C#, Java

Scripting: interpreted language with high-level operators designed for "gluing together" computations. Often shorter than equivalent programs written in language like C.

- Python, Ruby, Purl, JavaScript


