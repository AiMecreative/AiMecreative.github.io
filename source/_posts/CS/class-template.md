---
title: C++编程 | 类模板
date: 2023-02-28 20:21:43
tags:
- CS
- C++
categories: CS
author: Andrew-Rey
mathjax: true
---

"C++17类模板"

<!--more-->

> 编译器用于创建类的模板: 自动生成类
> 
> - 标准库
> - 类模板不是类, 是创建类的一种方式

> 实例
>
> - 编译器从类模板中生成的类, 在第一次使用模板类型声明变量是, 会创建类模板的一个实例, 以后定义同类型的变量时, 会使用已创建的第一个实例. 在创建类模板时, 也可以不同时声明变量.
> - 数据的组织 **独立于** 对象类型

## 类模板的定义

```c++
template<typename T1, typename T2, Type Arg1>
class ClassName {
    // template class definition
};
```

> **模板参数**
>
> - **类型参数** `typename`
>   - 实参总是类型: `int`, `float`...
> - **非类型参数** `Type`
>   - 实参是整数类型的字面量: `200`, `10`...
>   - 整数常量表达式
>   - 指向对象的指针或引用, 函数指针或空指针
> - **模板**
>   - 实参是类模板的一个实例

> 在模板定义中, 不需要使用完整的ID, 例如构造函数
>
> `ClassName<T1>();`可以写成`ClassName();`
>
> 不过在模板体的外部标识模板, 则必须使用模板ID (即在模板类外定义模板中的成员函数时需要显式写出ID)

**一个例子**

```C++
template<typename T1>
class PythonList {
private:
    int len_;
    int size_;
    T1* elements_;

public:
    explicit PythonList<T1>(size_t list_len);
    PythonList<T1>(const PythonList<T1>& python_list);
    ~PythonList();
    T1& operator[](size_t index);
    const T1& operator[](size_t index) const;
    PythonList<T1>& operator=(const PythonList<T1>& rhs_list);
    size_t get_len() const { return len_; }
    void allocate_double();
};
```

## 类模板成员函数的定义

> 若在模板类的内部定义, 实则为 **内联**

> **如何理解该语法**
>
> - 类模板的成员函数的外部定义本身就是函数模板, 即使成员函数不依赖类型参数.
> - 若函数没有在类内定义, 则它需要一个模板定义.
> - 定义函数模板中的参数列表必须与类模板参数列表相同.

例如

```c++
// 析构函数
template <typename T1>
PythonList<T1>::~PythonList<T1>() {
    delete [] elements_;
}

// 构造函数
template <typename T1>
PythonList<T1>::PythonList(size_t list_len)
    : len_(list_len), size_(FOLD * list_len), elements_(new T1(list_len)) {}

template <typename T1>
PythonList<T1>::PythonList(const PythonList<T1> &python_list)
    : PythonList{python_list.len_} {
  for (size_t i{}; i < len_; ++i) {
    elements_[i] = python_list.elements_[i];
  }
}

// 下标运算符
template <typename T1> T1 &PythonList<T1>::operator[](size_t index) {
  if (index >= len_) {
    throw std::out_of_range{"Index out of range: " + std::to_string(index)};
  }
  return elements_[index];
}

template <typename T1>
const T1 &PythonList<T1>::operator[](size_t index) const {
  if (index >= len_) {
    throw std::out_of_range{"Index out of range: " + std::to_string(index)};
  }
  return elements_[index];
}

// 赋值运算符
template <typename T1>
PythonList<T1> PythonList<T1>::operator=(const PythonList<T1>& rhs_list) {
    if (&rhs_list != this) {
        delete [] elements_;
        len_ = rhs_list.len_;
        size_ = rhs_list.size_;
        elements_ = new T1[len_];
        for (size_t i {}; i < size_; ++i) {
            elements_[i] = rhs_list.elements_[i];
        }
    }
    return *this;
}
```

> 第一行说明该函数为模板函数; 在限定成员函数时, 作用域需要带上模板ID
>
> 有时候需要**提供自己的拷贝构造(或析构)**, 因为涉及到动态内存分配时, 默认拷贝构造(或析构)有可能会出现负面效应
>
> 在赋值重载时, 需要 **检查左右操作数是否相等**, 否则会释放`this`指向的对象后再进行复制.

### 代码重复

> 在上述的定义中, `const`的重载和非`const`的重载模板函数代码重复, 代码重复不利于后续的维护
>
> - 对抗重复的方法: **函数, 模板, 基类**

**传统方法: 用`const`实现非`const`**

```c++
template <typename T1>
T1& PythonList<T1>::operator[](size_t index) {
    return const_cast<T1&>(static_cast<const PythonList<T1>&>(*this) [index]);
}
```

**C++17: `std::as_const()`(utility头文件)**

```c++
template <typename T1>
T1& PythonList<T1>::operator[](size_t index) {
    return const_cast<T1&>(std::as_const(*this)[index]);
}
```

### 异常安全性

1. 在赋值运算符重载的时候, 由于使用了`new`, 可能会出现`std::bad_alloc`异常
2. 在`elements_[i] = rhs_list.elements_[i];`可能会出现关于类型`T1`的赋值异常

> 当声明了`noexcept`后, 表示代码内部不发生异常, 使得编译器能做更多的优化, 例如大部分析构都隐式声明了`noexcept` cppreference [noexcept](https://en.cppreference.com/w/cpp/language/noexcept)

> 在以上的赋值运算符中使用 **复制后交换**

### 定义模板类注意

> - 成员函数模板与类模板的定义放在同一个文件中: 当编译器生成类模板时, 需要去使用函数模板, 所以在使用模板的源文件中, 这些成员函数的定义必须可用.

## 类模板实例化

```c++
PythonList<double> data {10};
```

> **编译器只编译程序使用的成员函数, 不会为某个模板参数的实例而一次性编译整个类**: 例如上述代码编译后的类中只有构造函数和析构函数.

> 声明对象类型的指针 **不会** 创建模板实例: `PythonList<std::string>* data_p;`

## 非类型的类模板参数

> 主要用于定义指定容器有效的值, 如数组的维数
>
> - **非类型参数只能是整数类型 (`size_t`, `long`), 枚举类型, 对象的指针或引用, 函数的指针或引用, 类成员的指针**
> - **当作常量**

```c++
template<typename T1, size_t size>
class ClassName {
    // definition
};

// 还有一些比较无语的
template<typename T1, T1 value> ... // 此时T1只能是模板的非类型参数所允许的类型
```

> **注意**
>
> 只有模板参数完全相同的情况下, 编译器才不会再次编译模板类; 任意一个不同, 编译器都会认为是不同的类, 后果是代码膨胀
>
> - 解决方法 (待定)

## 模板参数的默认值

> 与函数的默认参数类似
>
> - 如果某个模板参数有默认值, 则后续的参数也必须有默认值
> - 如果某个模板参数的实参被省略, 则后续的所有实参也必须省略
> - 不需要在成员函数的模板中指定默认值

```c++
template<typename T1 = int, int value = 10> ...
```

## 模板的显式实例化

```c++
template class ClassName<T1, 10, ...>
```

> 编译器会从模板中实例化所有的成员函数, 无论是否调用

## 类模板特化

模板的使用中有时候只对 **某些类型** 有用, 而不支持其他类型; 因此使用 **特化** 来处理某些特殊情况.

例如整型变量的相等和浮点型的比较并不相同, 这时可以使用模板的特化来处理.

> 对于类模板中的成员函数:
>
> - 如果成员函数是在类模板的外部定义的, 而不是在类模板体中定义的, 则可以提供函数模板的特化

**全特化**

即规定模板实现的所有模板参数

```c++
template<>
class PythonList<const char*>{};
```

> 特化的定义必须放在原有的定义或声明后面. 因为**指定了所有参数**, 所以是 **全特化**

**偏特化**

即只规定模板参数列表中的一部分模板参数

```c++
template<Type value>
class PythonList<const char*, value> {};
```

> `template`后的参数列表包含的是为这个模板特化的实例所指定的参数, 即**实例化时需要指定**`value`
>
> 模板名后面的尖括号指定原有类模板定义中的参数如何特化. **该参数列表必须与原来未特化的类模板个数相同**

> **指针类型的偏特化**
>
> 例如下面代码: `template`的第一个参数仍是`T1`, 但模板名后面可以跟着`T*`

```c++
template<typename T1, Type value>
class ClassName<T1*, value> {};
```

> **特化的选择**
>
> 当匹配给定特化的每个实参匹配多个特化时, 编译器会选择 **最特殊** 的一个特化.
>
> - 特殊是指有多个匹配, 如果符合A特化, 也符合B特化, 但反过来不行时, 则A比B更特殊 (A含于B)

## 在类模板中使用`static_assert()`

`static_assert()`接受两个参数, 第一个参数为`false`时, 输出第二个参数指定的消息. 第一个实参使用type_traits.h中的模板

![type_traits](type_traits.jpg)

## 类模板的友元

对于友元函数和友元类的情况与一般情况相同

> **模板友元**
>
> - 类模板的参数列表一般包含定义友元模板的所有参数
> - 如果类模板的一些参数在友元模板中没有, 则友元模板的实例会用于类模板的几个实例
> - 普通类若有友元模板, 则友元的每一个实例都是这个类的友元