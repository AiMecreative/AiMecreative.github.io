---
title: Design Pattern | OOD
author: Andrew-Rey
date: 2023-10-14 22:51:29
category: SE
tag:
- SE
- CS
- Java
- Design Pattern
---

> 项目的可维护性和可复用性，项目规范，团队开发

<!--more-->

## 单一职责原则

> 一个对象应该只包含单一职责，并且该职责被完整地封装在一个类中
> - 用于控制类的粒度大小

```python
class People(object):
    def coding(): pass
    def riding(): pass
    def cooking(): pass
    ...
```

- 臃肿：修改任意行为都会修改`People`类
- `People`拥有 **不止一个引起它变化的原因** 

```python
class Programmer(object): pass
class Rider(object): pass
class Chef(object): pass
```

- 类的 **粒度更细**，根据不同业务划分，采用单一职责原则，高内聚低耦合

## 开闭原则

> 软件实体应当对扩展开放，对修改关闭
> - 扩展开放：对提供方而言
> - 修改关闭：对调用方而言

```python
from abc import ABCMeta, abstractmethod

# define abstract class or interface
class IProgrammer(metaclass=ABCMeta):
    @abstractmethod
    def coding(): pass

class JavaProgrammer(IProgrammer): 
    # override
    def coding():
        java()

class PythonProgrammer(IProgrammer):
    # override
    def coding():
        python()
```

- 将不同程序员写代码抽象为一个统一的接口/抽象类，不进行实现
  - 扩展开放：开放了统一的接口`coding`，不同程序员自由决定如何编程
  - 修改关闭：具体程序员如何重写`coding`是自己负责，不受别人干扰

## 里氏替换原则

> 所有引用基类的地方必须能透明使用其子类的对象（子类能扩展父类的功能）
> - 子类可以实现父类的抽象方法，但不能覆盖父类的非抽象方法（既然是继承于父类，子类已经不具有父类的原本行为了，如果有这样的需求，一是可以取消继承，二是可以重新写一个方法）
> - 子类可以增加自己特有的方法
> - 当子类方法重载父类方法时，方法的前置条件（入参）要比父类更加宽松
> - 当子类方法重载父类方法时，方法的后置条件（返回值）要比父类更加严格或一样

## 依赖倒转原则

> 高层模块不依赖于底层模块，它们都应该依赖抽线。抽象不应依赖于细节，细节应该依赖于抽象
> - Spring框架

```python
class UserMapper(object): 
    # use CRUD
    pass
class UserService(object):
    # use methods in UserMapper
    user_mapper = UserMapper()
class UserController(object):
    # use methods in UserService
    user_service = UserService()
```

- 上述代码结构好，但是如果底层逻辑（例如`UserService`）发生改变，则上层逻辑也要跟着改变，层次分明但 **耦合度高**

```python
from abc import ABCMeta, abstractmethod

class UserMapper(metaclass=ABCMeta): 
    # provides abstract interfaces only
    pass
class UserMapperImpl(UserMapper):
    # implements interfaces of UserMapper
    pass
class UserService(metaclass=ABCMeta):
    # provides abstract interfaces only
    pass
class UserServiceImpl(UserService):
    # use dependency injection to instantiate UserMapper such as:
    self.user_mapper = None
    def set_user_mapper(user_mapper: UserMapper): pass
class UserController():
    # use dependency injection to instantiate UserService such as:
    self.user_service = None
    def set_user_service(user_service: UserService): pass
```

- 如果修改了底层逻辑（例如`UserService`），只需要修改其实现类（`UserServiceImpl`）即可，上层逻辑由依赖注入完成
- 上层只需要知道接口中定义了什么方法然后使用即可，具体操作内容由接口的实现类完成
- 使用了 **依赖注入**
- 降低了类之间的耦合度

## 接口隔离原则

> 客户端不应依赖那些它不需要的接口
> - 对接口的细化
> - 定义接口时要注意接口的粒度

## 合成复用原则

> 优先使用对象组合，而不是通过继承来达到复用的目的
> - 核心是委派
> - 在一个新的对象里面使用一些已有的对象，使之成为新对象的一部分，新的对象通过向这些对象的委派达到已有功能复用的目的

- 继承可以实现复用，但
  - 耦合度高
  - 子类得到父类细节（某些字段或方法），不安全

- 组合实现复用
  - 考虑函数传参，用的时候才传参
  - 考虑成为成员变量，构造时指定

## 迪米特法则/最少知识原则

> 每一个软件单位对其它单位都只有最少的知识，而且局限于那些与本单位密切相关的软件单位
> - 一个模块与其它模块交互越少越好
> - 降低耦合度

```python
def main_task():
    my_secret = Secret()
    test = Test()
    # test_start may need one of the property of Secret
    test.test_start(my_secret)

# in Test
def test_start(my_secret: Secret):
    print(my_secret.sth)
```

- `test_start`参数改为`sth: Something`减少与其它功能模块的交互