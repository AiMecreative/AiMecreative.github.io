---
title: Design Pattern | Creational
author: Andrew-Rey
date: 2023-10-15 10:14:10
category: SE
tag: 
- CS
- SE
- Java
- Disgn Pattern
---

> 使用设计模式是为了可重用代码，让代码更容易被他人理解，保证程序的可靠性和重用性

<!--more-->

> - 肯特·贝克和沃德·坎宁安：建筑设计思想 -> Smalltalk的图形用户接口生成
> - Erich Gamma改为适用于软件开发
> - James Coplien致力于C++开发，Advanced C++ Idioms
> - Gang of Four (Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides) 出版 Design Patterns - Elements of Reusable Object-Oriented Software

[ref](https://itbaima.net/document)


## 工厂方法模式

> 创建对象时，不直接使用`new`来创建对象，而是使用工厂方法模式
> - 程序中使用大量的`new`时，当某个对象/构造方法发生变化时，难以维护
> - 将频繁出现的对象创建，封装到一个工厂类中

**简单工厂模式**

```java
public class FruitFactory() {
    public Fruit getFruit(ID id) {
        if (id == 0) {return new Apple();}
        if (id == 1) {return new Peach();}
        ...
    }
}
```

- 当调用方添加新对象时，需要 **修改** 工厂代码
- 上述代码不符合 **开闭原则**：对扩展开放，对修改关闭
  - `FruitFactory`提供给调用方使用，应该对修改关闭，即不要修改工厂代码
  - 但是提供方可以对扩展开放

**工厂方法模式**

```java
public abstract class FruitFactory<T extends Fruit> {
    public abstract T getFruit();
}
public class AppleFactory extends FruitFactory<Apple> {
    @Override
    public Apple getFruit() {
        return new Apple();
    }
}
...
```

- 如果新增了新对象，调用方只需要自己添加对应的工厂并继承最高的工厂即可
- 使用者只需要关心如何使用对象，工厂屏蔽了对象的创建细节

## 抽象工厂模式

> 工厂方法模式只适用于简单对象，如果需要许多的产品族时会显得乏力

## 建造者模式

- `builder`
- 如果一个对象构造时用的参数过多，可以使用`builder`优雅地完成构造

```java
public class Student {
    int id;
    int age;
    int grade;
    String name;
    String college;
    String profession;
    List<String> awards;

    public Student(int id, int age, int grade, String name, String college, String profession, List<String> awards) {
        this.id = id;
        this.age = age;
        this.grade = grade;
        this.name = name;
        this.college = college;
        this.profession = profession;
        this.awards = awards;
    }
}
```
- 参数错位，构造方法太长

```java
public class Student {
		...

    //一律使用建造者来创建，不对外直接开放
    private Student(int id, int age, int grade, String name, String college, String profession, List<String> awards) {
        ...
    }

    public static StudentBuilder builder(){   //通过builder方法直接获取建造者
        return new StudentBuilder();
    }

    public static class StudentBuilder{   //这里就直接创建一个内部类
        //Builder也需要将所有的参数都进行暂时保存，所以Student怎么定义的这里就怎么定义
        int id;
        int age;
        int grade;
        String name;
        String college;
        String profession;
        List<String> awards;

        public StudentBuilder id(int id){    //直接调用建造者对应的方法，为对应的属性赋值
            this.id = id;
            return this;   //为了支持链式调用，这里直接返回建造者本身，下同
        }

        public StudentBuilder age(int age){
            this.age = age;
            return this;
        }
      
      	...

        public StudentBuilder awards(String... awards){
            this.awards = Arrays.asList(awards);
            return this;
        }
        
        public Student build(){    //最后我们只需要调用建造者提供的build方法即可根据我们的配置返回一个对象
            return new Student(id, age, grade, name, college, profession, awards);
        }
    }
}
```

- 最后可以使用链式调用完成对象的创建

```java
public static void main(String[] args) {
    Student student = Student.builder()   //获取建造者
            .id(1)    //逐步配置各个参数
            .age(18)
            .grade(3)
            .name("小明")
            .awards("ICPC-ACM 区域赛 金牌", "LPL 2022春季赛 冠军")
            .build();   //最后直接建造我们想要的对象
}
```

- 还包括 **协调者模式**

## 单例模式

> 一个类始终只有一个实例对象/直接使用类的静态方法

- 饿汉式单例
  - 类加载时将对象创建好
- 懒汉式单例
  - 延迟加载，需要时才创建
  - 线程不安全
    - 多线程不能保证只创建一次
    - 在创建实例的方法上加锁`synchronized`（但高并发效率较低）
    - 可以在判断实例是否创建的`if`语句内加锁
    - `volatile`保证线程可见

- 懒汉式+饿汉式
- 在懒汉式的内部创建内部类
  - 由静态内部类持有单例对象，根据类加载特性，仅使用外层类时，不会对静态内部类进行初始化

## 原型模式

> 原型对象作为模板，通过复制该对象来创建新对象

**浅拷贝**

- 基本数据类型将值赋值，引用类型只复制地址，指向的还是原来的对象

**深拷贝**

- 拷贝为一个全新的对象

**Java拷贝机制**

- `Cloneable`接口
  - 重写`clone`方法
  - 内层对象依然是引用的复制，用`==`进行地址比较
  - 应该在`clone`中处理成员变量