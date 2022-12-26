---
title: CMakeTutorial
index_img: /index_imgs/cmake-tutorial.jpg
date: 2022-08-10 12:56:16
category: CS
---

CMake version: 3.x

<!--more-->

# Command Line

```cmake
# (configure step) create build dir, and generate build/Makefile -> generate Makefile
cmake -B build

# (build step) invoke building system and build the project in different OS -> generate executable file
cmake --build build -j4

# invoke building system to execute target "install"
cmake --build build --target install

# define configure variables, only use in configure step
# use -D
# set build type in configure step, the value will remain when invoked the second time unless delete build dir
cmake -B build -DCMAKE_BUILD_TYPE=Release

# Specify generator (generator: generate build system build rule from CMakeLists.txt)
# use -G
# generator Ninja, faster than Unix Makefile, generate *.ninja
cmake -B build -G Ninja
```

# CMakeLists.txt

**add source file**

(1). single file: main.cpp

```cmake
add_executable(main main.cpp)
```

or

```cmake
add_executable(main)
target_sources(main PUBLIC main.cpp)
```

(2). multiple files: main.cpp | other.cpp | other.h

```cmake
add_executable(main)
target_sources(main PUBLIC main.cpp other.cpp)
```

or **set** a new variable

```cmake
add_executable(main)
set(sources main.cpp other.cpp other.h)  # other.h can delete
target_sources(main PUBLIC ${sources})
```

or use **GLOB** to search all files in current dir

```cmake
add_executable(main)
file(GLOB sources CONFIGURE_DEPENDS *.cpp *.h)  # add CONFIGURE_DEPENDS to detect any change when next build
target_sources(main PUBLIC ${sources})
```

when we have a dir structure:

```text
mylib
  +----*.cpp
  +----*.h
*.cpp
*.h
```

no need to write all files:

```cmake
# add all file in current dir and mylib dir
add_executable(main)
aux_source_directory(. sources)
aux_source_directory(mylib sources)
target_sources(main PUBLIC ${sources})
```

or use **GLOB_RECURSE** to find all files recursely:

```cmake
add_executable(main)
file(GLOB_RECURSE sources CONFIGURE_DEPENDS *.cpp *.h)
target_sources(main PUBLIC ${sources})
```

**ERROR**: use GLOB_RECURSE will include *.cpp files in build dir.

**solution**: Add all source files in a dir named src

## Configure variables

**CMAKE_BUILD_TYPE**: type of build, **Release**, **Debug**, **MinSizeRel** and **RelWithDebInfo**, defualt: none (debug).

```cmake
set(CMAKE_BUILD_TYPE Release)
```

set default build type as Release to reach high performance: in the first three lines:

```cmake
if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()
```

```cmake
# Specify version of cmake
cmake_minimum_required(VERSION 3.22)

# set c++ standard
# don't modify CMAKE_CXX_FLAGS to add -std=c++17
set(CMAKE_CXX_STANDARD 17)

# if use the needed CXX standard defined.
set(CMAKE_CXX_STANDARD_REQUIRED ON)  # OFF default

# prevent features GCC only
set(CMAKE_CXX_EXTENSIONS OFF)

# set project info
project(project_name LANGUAGES language_list(such as C CXX ASM...))
```

## Linkable library

```cmake
add_executable(main mian.cpp mylib.cpp)
```

or generate a static library

```cmake
add_library(mylib STATIC mylib.cpp)  # create libmylib.a

add_executable(main main.cpp)

target_link_libraries(main PUBLIC mylib)
```

or generate dynamic lib

```cmake
add_library(mylib SHARED mylib.cpp)

add_executable(main main.cpp)

target_link_libraries(main PUBLIC mylib)
```

or use object lib, no *.a file, let CMake remember which objects files are created

```cmake
add_library(mylib OBJECT mylib.cpp)

add_executable(main main.cpp)

target_link_libraries(main PUBLIC mylib)
```

静态库问题: GCC会自行剔除没有引用符号的对象, 此时使用对象库避免, 从而不会自动剔除没引用到的对象文件, 绕开编译器不统一问题. 动态库也可以避免剔除没引用的对象文件, 但引入了运行时链接的麻烦.

```cmake
# no specify variable in add_library()
set(BUILD_SHARED_LIBS ON)  # default OFF

add_library(mylib mylib.cpp)
```

**HINT** 静态库常常被认为直接链接到可执行文件上. 因此在动态库中不要链接静态库. 很呆. 地址会变. 当然**解决方法**是: 要么转化为对象库, 要么让静态库变成地址无关的代码PIC

```cmake
# set global property
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

add_library(otherlib STATIC otherlib.cpp)

add_library(mylib SHARED mylib.cpp)
target_link_libraries(mylib PUBLIC otherlib)

add_executable(main main.cpp)
target_link_libraries(main PUBLIC mylib)
```

or set local property

```cmake
# set local property
add_library(otherlib STATIC otherlib.cpp)
set_property(TARGET otherlib PROPERTY POSITION_INDEPENDENT_CODE ON)

add_library(mylib SHARED mylib.cpp)
target_link_libraries(mylib PUBLIC otherlib)

add_execuable(main main.cpp)
target_link_libraries(main PUBLIC mylib)
```

## Attributes of objects
设置单属性: `set_property(TARGET ... PROPERTY ...)`;

设置多属性: `set_target_properties(file_name PROPERTIES properties_list)`

**HINT**: 以上命令在`add_executable`后有效.

设置全局属性 (改变属性的默认值): `set(CMAKE_XXX)`, 在`add_executable`前设置.

> 如果需要在Windows下面使用动态库 (Windows对动态链接不友好), 则需要在定义和声明添加:
> **Deffinition:**
> ```cpp
> #include <cstdio>
> 
> #ifdef _MSC_VER
> __declspec(dllexport)
> #endif
> void sayy_hello(){}
> ```
> **Declaration:**
> ```cpp
> #pragma once
> 
> #ifdef _MSC_VER
> __declspec(dllimport)
> #endif
> void say_hello();
> ```
> 然后CMakeLists.txt这样写:
> ```cmake
> # In Main dir
> cmake_minimum_required(VERSION 3.22)
> add_subdirectory(mylib)  # add sub module
> add_executable(main main.cpp)
> target_link_libraries(main PUBLIC mylib)
> 
> # In sub module dir
> add_library(mylib SHARED mylib.cpp mylib.h)
> ```
> 然后Windows极有可能会报错: 运行时找不到dll; 原因是dll和exe不在同一目录 (Windows只会查找exe所在目录和PATH). 
> - 把dll添加到PATH环境变量
> - 或者dll和dll其他的所有依赖dll, 全部拷贝到exe同一目录
> 
> 这是因为CMake把main放在build下, 而mylib放在build/mylib/mylib.dll

因此重定向输出路径, 改变mylib属性, 让.dll文件输出到 **PROJECT_BINARY_DIR** 里面.
```cmake
set_property(TARGET mylib PROPERTY RUNTIME_OUTPUT_DIRECTORY_(DEBUG | RELEASE | NONE) | ARCHIVE_OUTPUT_DIRECTORY | LIBRARY_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR})
```

## Externel library
In Linux: feel free to link externel libraries. (/usr/lib/...) But Windows can't. Linux can also include head file directly (/usr/include/...).

**HINT:** CMake 的分隔符永远是 "/", 即使是Windows, CMake会自动转化.

More general method:
```cmake
find_package(package_name REQUIRED)
```

没听懂, 以后补, 以后也不想补.

## Variables and Outputs

output some log infomation when running `cmake -B build`, used for debugging.
```cmake
message("log info")
```

```cmake
message(STATUS "status info")  # -- prefix
```

```cmake
message(WARNING "warning info")  # yellow
```

```cmake
message(SEND_ERROR "error info")  # send error log but continue to run

message(FATAL_ERROR "error info")  # print error and stop running
```

## Variable and Cache
重复执行`cmake -B build`: 第一次较慢, 将环境的检测存入缓存, 第二次以及以后直接查看缓存内容. 因此某些错误可以通过删除 **./build/CMakeCache.txt**解决. 当然也可以删了整个build文件夹重新编译, 慢一点而已.
