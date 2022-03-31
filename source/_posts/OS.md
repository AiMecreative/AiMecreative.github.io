---
title: Operating System
date: today
mathjax: true
category: Computer Science
---

"This is the basic class for CS."

"And it is interesting. I mean if you can totally master it."

<!--more-->

# Concept
Framework of this chapter:
- basic concepts
- OS components
- OS services (Using components)
- System call (how to provide services)
- Structure
- virtual machine

These contents will be detailed written in the following chapters

## Operating system components
### :cherry_blossom:Process management
**process**: A process is a <font color=blue>program</font> in <font color=red>execution</font>.
- program has its own address space

{%note primary%}
### OS activities:
- Process creation and deletion
  - using **fork** system call
- Process suspension and resumption (挂起或恢复)
- Provision of mechanism for:
  - process synchronization (进程同步)
    - such as two processes should share a variable to achieve a task or job. And synchronization mechanism helps to finish this job in a proper order.
  - process communication (进程通信)
  - deadlock handling (死锁处理)
{%endnote%}

### :cherry_blossom:Main memory management
**memory**: Memory is a large array of words or bytes, each with its own address. It is a repository of quickly accessible data shared by the CPU and I/O devices.

**Main memory** or **primary storage** is a volatile storage device (掉电易失设备).

{%note primary%}
### OS activities:
- Keep track of which parts of memory are currently being used and by whom.
- Decide which processes to load when memory space becomes available (Job scheduling, 任务调度).
- Allocate and deallocate memory space as needed.
{%endnote%}

**Virtual memory**: Virtual memory allows programs to address memory from a logical point of view. This technique allows applications **regard** that they have a continuous address space rather than fragmented spaces from main memory to disk memory.
- without regard to the limits of physical memory.

### :cherry_blossom:File management
**file**: A file is a collection of related information defined by its creator. Commonly, files represent programs (both source and object form) and data.
- this a uniform logical view of information storage provided by OS.

{%note primary%}
### OS activities:
- File creation and deletion.
- Directory (can be seen as a special file) creation and deletion.
- Support of primitive for manipulating files and directories.
- Mapping files onto secondary storage.
  - for large files, how to map them onto secondary storage?
- File backup (备份) on stable (nonvolatile) storage media.
{%endnote%}

*Windows file management is related to storage, but Linux not. In Linux, every thing is file, having a unified form to access files.*

**Mount (挂载)**: create a mounting point, and this file is can be accessed using mounting point.

### :cherry_blossom:I/O system management
The I/O subsystem consists of:
- a buffer-caching system
- a general device-driver interface (a driver is a part of OS, specific for devices)
  - programmed I/O
  - interrupt I/O
  - DMA
- drivers for specific hardware devices

### :cherry_blossom:Secondary-storage (disk) management
**Secondary storage** is the principle on-line storage medium (线性存储介质) for both programs and data.
- disk
- Main memory is volatile and too small to accommodate all data and programs permanently, so the computer must provide secondary storage to back up main memory.

{%note primary%}
### OS activities;
- Free space management (which parts of disk are free and how to allocate these free blocks)
- Storage allocation
- Disk scheduling (磁盘调度)
  - 磁头移动, 请求分布在不同柱面上, 相应时需要磁头在不同不同柱面上切换, 经过算法, 设计磁头移动的最短距离 (有计算题).
{%endnote%}

### :cherry_blossom:Protection system
**Protection** refers to a mechanism for controlling access by programs, processes, or users to both system and user resources.
- distinguish between authorized and unauthorized usage.
- specify the controls to be imposed and means for enforcement.

Example:
In Linux, file access control: **rwx**, **owner**, **user(u)**, **group(g)**, **other(o)**

### :cherry_blossom:Command-interpreter system
**Command-interpreter system**(命令行解释系统): Interact with users, users can send instructions to OS.
- Shell
- its functions is to get and execute the next command statement.


## Operating system services
### :cherry_blossom:Core operating system services
From the view of an user:

**Program execution**
- load a program into memory and to run it
  - process management, memory management, disk management and so on.

**I/O operations**
- user programs cannot execute I/O operations directly, the OS must provide some means to perform I/O.

**File-system manipulation**
- programs capability to read, write, create and delete files

**Communication**
- exchange information between processes

**Error detection**
- ensure correct computing in CPU, memory hardware, I/O devices, user programs

### :cherry_blossom:Additional operating system functions
From a view of system:

This part is user for **efficient system operations**, not for helping users.
- Resource allocation
- Accounting
- Protection

## System call
An user how to use system services:

Normally, we write C code and define the ``main`` function, this is a *system call*, but has been packaged to a convenient-to-use API.

**System call** is an **interface** between a running program and the OS.
- generally available as assembly-language instructions. (汇编语言形式呈现)
- user programs (in **user mode**, ``mode bit=1``) send a ``system call`` to the OS (in **kernel mode**, ``mode bit=0``), and the OS execute the system call, then the OS returns (and change the mode bit to 1), finally the user programs continue to execute.
- Common in the OS
- Some language like ``C`` language and ``C++`` are defined to replace assembly-language for system programming, which allow system call to be made directly.

![system_call1](system_call1.png)

### :cherry_blossom:The implementation of system call
Typically, a number (index) associated with each system call.
- System call interface maintains a table indexed according to these numbers

The system call interface invokes intended system call in OS kernel and returns status of the system call and any return values. (系统调用的接口使用OS内核中的系统调用, 并返回系统调用状态和相应参数)

The caller need to know **nothing** about how the system call in implemented.
- just need to **obey API** and understand what OS will do as a result call.
- Most details of OS interface hidden from programmer by API
  - manage run-time support library <u>(set of functions built into libraries included with compiler)</u>

![system_call2](system_call2.png)

In this picture, ``open()`` function acts as an API, and ``open()`` gives a system call (in the function library) to OS (maybe in the library, ``open()`` function use other system functions to give a system call, because ``open()`` is just an <u>API</u> of system call functions). Then the OS look up this system call in its number table and then execute a specific system program (according to the index number). Finally, the OS returns the states.

### :cherry_blossom:Parameter passing in system call
Often, more information is required than simply identity of desired system call.

Three types:
- simplest: pass the parameters in ***registers***
  - maybe more parameters than registers
- Parameters stored in a ***block***, or *table*, in memory. and pass the block address to registers.
  - taken by Linux and Solaris
- Parameters placed, or <u>pushed</u> onto the ***stack*** by program and <u>popped</u> off the stack by the OS.

<u>Block and stack don't limit the number and the length of parameters.</u>

### :cherry_blossom:Types of system call
Five main types:
- process control
- file management
- device management
- information maintenance
- communication

**process management**
<center><b>Table 1: process management for major POSIX system</b></center>

|call|description|
|----|-----------|
|``pid=fork()``|create a child process identical to the parent (child is same with parents process)|
|``pid=waitpid(pid, &statloc, options)``|wait for a child to terminate|
|``s=execve(name, argv, environp)``|replace a process' core image, can be used with ``fork()`` to let child do another things but both from parents process|
|``exit(status)``|terminate process execution and return status|

**file management**
<center><b>Table 2: file management for major POSIX system</b></center>

|call|description|
|----|-----------|
|``fd=open(file, how, ...)``|open a file for reading, writing, or both, ``fd`` is 文件描述符|
|``s=close(fd)``|close an open file|
|``n=read(fd, buffer, nbytes)``|read data from a file into a buffer|
|``n=write(fd, buffer, nbytes)``|write data from a buffer to file|
|``position=lseek(fd, offset, whence)``|move the file pointer|
|``s=stat(name, &buf)``|get a file's status information|
|``mkdir()``|create a new directory|
|``rmdir()``|remove an empty directory|
|``link()``|create a new entry, name2, pointing to name2. (soft link)|
|``unlink()``|remove the directory entry|
|``mount()``|mount a file system|
|``unmount()``|unmount a file system|

**miscellaneous system call**

|call|description|
|----|-----------|
|``chdir()``|change working dir|
|``kill()``|send a <b>signal</b> to a process|
|``chmod()``|change a file's protection bits|
|``time()``|get the elapsed time since Jan 1, 1970|

## System structure
monolithic单体结构（一个进程）$\rightarrow$ 分层式 $\rightarrow$ 微内核结构（最核心的功能放在内核中）、模块化结构（linux）
### :cherry_blossom: UNIX
have no concept of **structure**, is **Single core structure.**

consists of two separable parts:
- system programs
- the kernel

### :cherry_blossom: Microkernel
assign only a few essential functions to the kernel
- address spaces
- interprocess communication (IPC)
- basic scheduling

{%note info%}
### Benefit and detriments
- reliable
- easy to extend
- secure
- communication occupies much space
{%endnote%}

### :cherry_blossom:Modules
most modern OS implement module method:

kernel is divided into different modules.

层次化不明显；可以动态对内核进行装载和删除内核模块

## Virtual machine
treats hardware and the OS kernel as though they were all hardware (对物理资源抽象，即抽象层，在抽象层能实现虚拟机)

**management application:**
- type 1: built on hardware
  - use hardware directly
  - usually used in data center or service
- type 2: built on the OS
  - lower performance (性能)
  - lower security
  - usually used on PC

# Process
## Concept of process
### :cherry_blossom: What is a process?
- A program in execution
- An instance(实例) of a program running on a computer
  - 同样代码跑两遍，是不同的进程
- The entity(实体) that can be assigned to(指派) and executed on a processor
- A unit of activity characterized by the execution of a sequence of in instructions, a current state, and an associated set of system resources(一系列指令执行，状态(如wait, execution, ready)，有资源)

### :cherry_blossom:Process in memory
- **text** 代码段(``addr=0``)
  - code
  - codes are complied and stored here
- **data** 数据段
  - ``global`` data
  - ``static`` data
- **heap** 堆
  - ``new()``
  - ``delete()``
- **stack** 栈(``addr=max``)
  - local function invoking
  - local variables calling

**example**:
```C
int x = 1;
int main()
{
  int a;
  static int b;
  f1();
  int* pointer = NULL;
  pointer = int new();
  return 0;
}
```
``x`` and ``b`` are in ``data`` sector; ``a`` and ``f1()`` are in ``stack``; ``pointer`` points to a space of ``heap``.

HINT: there is a <u>flexible space</u> between **heap** and **stack**.


### :cherry_blossom:Process elements
1. program code (possible shared)
2. a set of data
3. a number of attributes describing the state of the process

### :cherry_blossom:Trace of the process
The behavior of an individual process is shown by **listing the sequence of instructions** the are executed. (指令按序执行)

This list is called a **trace**.

**Dispatcher** is a small program which switches the processor from one process to another. (进程切换)

## User-view of process
### :cherry_blossom:Process creation
The OS builds a data structure to manage the process.
- Traditionally, the OS create all processes
- But it can be useful to let a running process create another
  - This action is called **process spawning** (进程派生)
    - Parent process is the original, creating processes
    - Child process is the new process
    - Parent process create child process, and child processes create other processes, **forming a tree of process**.

- Execution (can be set manually)
  - parent processes and child processes execute concurrently (同时执行).
  - parents wait when children terminate

HINT: the children just copy a status of parent

|command|description|
|-------|-----------|
|``fork``|system call creates new <b>same</b> process|
|``exec``|system call used after a ``fork`` to replace the process' memory space with a <b>new program</b>|

{%note primary%}
### The differences using ``fork()`` in parents and children processes
1. fork返回给child_pid在两个进程中不一样. 在父进程中``fork()``的返回值大于零, 即子进程的编号; 在子进程中``fork()``的返回值是0.

2. 可以理解为父进程在``fork()``的初期产生了子进程, 此时子进程拿到的返回值是初始化的返回值 0, 在父进程即将结束``fork()``时, 父进程拿到了被赋值的返回值. 因此在子进程中不会再次执行``fork()``, 而执行其后面的内容.

3. 子进程不会再次执行父进程先前的内容, 只是创建时与父进程处于相同的状态.

4. 父子进程执行的先后顺序取决于 OS 的调度

{%endnote%}

**example 1:**
```C
pid = fork();
if (pid < 0)
{
  fprintf(stdrr, "fork failed")
  exit(-1);
}
else if (pid == 0)  // child process
{
  execlp("/bin/ls", "ls", NULL);  // replace with a new command
}
else  // parent process
{
  wait(NULL);
  printf("children complete");
  exit(0);
}
```

**example 2:**
```C
/*in file fork.c:*/
int main()
{
  pid_t child_pid;
  
  printf("the main program ID is %d\n", (int)getpid());

  child_pid = fork();
  if (child != 0)
  {
    printf("this is the parent process, with ID is %d\n", (int)getpid());
    printf("the child's process ID is %d\n", (int)child_pid);
  }
  else
  {
    printf("this is the child process, with ID %d\n", (int)getpid());
  }

  return 0;
}
```
And the running result is:

### :cherry_blossom:Process termination
Process executes last statement and asks the OS to delete it. (``exit()``)
- Output data from child to parents (via``wait()``)
- Process' resources are de-allocated (收回) by the OS

Parents may terminate the execution of children processes. (``abort()``)

Some situations of this:
- Child has executed allocated resources
- Task assigned to child is non  longer required
- Parent is exiting
  - OS does not allow child to continue if its parent terminates
  - Cascading termination (级联终止)
  - HINT: 父进程结束不代表子进程必须结束

### :cherry_blossom:Code block
**creating process:**

``int fork(void);``
- create a new process that is exact copy of current one
- returns process ID of new process in parent
- return 0 is child

``int waitpid(int pid, int *stat, int opt);``
- pid: process **to wait for**, or -1 for any
- stat: will contain exit value, or signal
- opt: usually 0 or WNOHANG (?what's this)
- return: process ID or -1 if error

**deleting process:**

``void exit(int status);``
- current process ceases to exit
- status shows up in waitpid(shifted)
- by convention, status of 0 is successful, non-zero is error

``int kill(int pid, int sig);``
- sends signal ``sig`` tp to process ``pid``
- ``sig=SIGTERM``: most common value, kills process by default
- application can catch ti for "cleanup"
- ``sig=SIGKILL``: stronger, kills process always

**running programs:**

``int execve(char *prog, char **argv, char **envp);``

``int execlp(char *prog, char *arg, ...);``

## Kernel view of process (using Process Control Block, PCB)
**Main problem: How to manage such many process?**

For traditional UNIX process: process is an abstraction of OS, which represents what is needed to run a program.
- often called a "HeavyWeightProcess"
- while a thread is called "轻量级"

This **traditional** process has two parts:
1. sequential program execution stream. (now is thread)
   1. code executed as a sequential stream of execution (thread)
   2. includes states of CPU registers
2. protected resources
   1. main memory state
   2. IO state

### :cherry_blossom:Process Elements
- identifier
- state
- priority
- program counter (in fact has many registers, not only the PC)
- memory pointers
- context data
- IO status information
- accounting information
- and so on

### :cherry_blossom:Implementing process
内核如何实现一个进程? 管理一个进程?

**keep a data structure for each process**
- <font color=red><b>process control block (PCB)</b></font>
- called "proc" in Unix and "task_struct" in Linux

**track states of process** ----"Process State"
- running, waiting, ready...

**includes information necessary to run**
- registers, virtual memory mapping, open files...

**Various other data about the process**
- such as user/groups...

{%note info%}
PCB is also a **snapshot** of a process, saving all status of a process.
{%endnote%}

### :cherry_blossom:Process states
**new**: the process is being created

**ready**: the process is waiting to be assigned to a processor

**running**: instructions are being executed

**waiting**: the process is waiting for some event to occur

**terminated**: the process has finished execution

The process switching graph is shown as following:


![process_state](process_state.jpg)

The CPU switch from process to process:

![state_switch](switch_state.jpg)

when to switch processes:
- interrupt
- trap
  - current process running is wrong
- system call

switch steps:
- save context of processor including program counter and other registers
- update the PCB that is currently in the Running state
- move the PCB to appropriate queue
- select another process for execution
- update the PCB of the process selected
- update memory-management data structures
- restore context of the selected process

### :cherry_blossom:Process scheduling queues
**Job queue**: set of all processes in the system

**Ready queue**: set of all processes residing in main memory, **ready** and waiting to execute

**Device queue**: set of processes **waiting** for an I/O device

{%note primary%}
Process migration between the various queue.
{%endnote%}

![queue_switch](queue_switch.jpg)

### :cherry_blossom:Scheduler
**Long-term scheduler(Job scheduler)**: select which processes should be loaded into memory for execution.

**Short-term scheduler(CPU scheduler)**: selects which process should be executed next and allocates CPU

Short-term scheduler is invoked very frequently (milliseconds----must be fast)

Long-term scheduler is invoked very infrequently (seconds, minutes----may be slow)

The long-term scheduler controls the *degree of multiprogramming*
- IO-bound process: spends more time doing IO than computations, many shout CPU bursts
- CPU-bound process: spends more time doing computations, few very long CPU burst

We also have **Medium-term scheduler**

## Inter-process communication
### :cherry_blossom:Cooperating process
Independent process cannot affect or be affected by the execution of another process.

Cooperation process can affect or be affected by the execution of another process.

{%note primary%}
### Advantages
- information sharing
- computation speed-up
- modularity
- convenience
{%endnote%}

### :cherry_blossom:Communication models
**message model**
- smaller data exchange
- inter-computer communication (跨机的通信)
- system call with kernel

**shared memory**
- Maximum speed/memory
- convenience of communication
- protection and synchronization
- routine memory access without kernel intervention
