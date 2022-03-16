---
title: Operating System
date: 2022-2-28
mathjax: true
category: Computer Science
---

"This is the basic class for CS."

"And it is interesting. I mean if you can totally master it."

<!--more-->

# Concept
## Operating system components
### Process management
**process**: A process is a program in execution.

OS activities:
- Process creation and deletion
- Process suspension and resumption
- Provision of mechanism for:
  - process synchronization (进程同步)
  - process communication (进程通信)
  - deadlock handling (死锁处理)

### Main memory management
**memory**: Memory is a large array of words or bytes, each with its own address. It is a repository of quickly accessible data shared by the CPU and I/O devices.

**Main memory** is a volatile storage device (掉电易失设备).

OS activities:
- Keep track of which parts of memory are currently being used and by whom.
- Decide which processes to load when memory space becomes available (Job scheduling, 任务调度).
- Allocate and deallocate memory space as needed.

**Virtual memory**: Virtual memory allows programs to address memory from a logical point of view. This technique allows applications **regard** that they have a continuous address space rather than fragmented spaces from main memory to disk memory.
- without regard to the limits of physical memory.

### File management
**file**: A file is a collection of related information defined by its creator. Commonly, files represent programs (both source and object form) and data.
- this a uniform logical view of information storage provided by OS.

OS activities:
- File creation and deletion.
- Directory creation and deletion.
- Support of primitive for manipulating files and directories.
- Mapping files onto secondary storage.
- File backup on stable (nonvolatile) storage media.

### I/O system management
### Secondary-storage management
### Protection system
### Command-interpreter system