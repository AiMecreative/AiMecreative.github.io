---
title: Full Stack | Quick Start
author: Andrew-Rey
date: 2023-10-12 18:51:22
category: SE
tag:
- SE
- Full Stack
- Springboot
- Vue
---

# Full-Stack Quick Start

SpringBoot + Vue development

- JavaEE: SpringBoot + MyBatis Plus
- Web front end: Vue + ElementUI

---

## configure environment

- jdk
- IDE: JetBrain IDEA
- auto build tool: maven
  - projects auto build 
  - dependencies manegement
  - standard development structure

**maven usage**

- edit local repo (default is under `user` dir)
- (optional) configure mirrors
- configure self downloaded maven with IDEA

![1697109448690](1697109448690.png)

## springboot

- intro
  - framework provided by Pivotal Team
  - convention Over Configuration(约定优于配置)
  - embedded server(Tomcat, Jetty; no war file, just jar)
  - simplify maven configuration
  - pure Java

## springboot

- SSM
  - Spring, Spring mvc, MyBatis
  - difficult to configure
- adv
  - quickly, simplely

**initialize Springboot**

- IDEA
  - Spring Initializer(maven based infact)
    - fill project information(group id & artifact id)
    - generate project on the [web](https://start.spring.io/), download it and load in
    - select jdk

**initialize Springboot**

- choose Maven project
- choose springboot version

![1697114528195](1697114528195.png)

**initialize Springboot**

- configure project information

![1697114538516](1697114538516.png)

**initialize Springboot**

- add dependencies (web app, choose spring web)

![1697114557959](1697114557959.png)

## coding springboot

- backend project: receive requests from brower
  - use Components

```java

@RestController
public class DemoController{}

```

**coding springboot**

- add controller member function

```java
// https://localhost:8080/demo
@GetMapping("/demo")
public String demo(){
    return "hello world";
}
```

**coding springboot**

- start the project(yes, no additional code in `main`)

![1697116224333](1697116224333.png)

**hot deployment**

- normal case: every time you modify the code, restart the project
- need hot-deployment
  - spring-boot-devtools component
    - listen the variations of classpath, trigger `Restart` class loader to reload the class
    - not every change needs to restart app (static res, view templates), use `spring.devtools.restart.exclude` to exclude the dirs/files

- add `dev-tools` dependency in `pow.xml`

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-devtools</artifactId>
    <optional>true</optional>
</dependency>
```

- add properties in `application.properties`

```properties
spring.devtools.restart.enabled = true
spring.devtools.restart.additional-paths = src/main/java
spring-devtools.restart.additional.exclude = static/**
```

## web development

- basic
  - [request methods](https://github.com/febobo/web-interview/issues/145): `get` request: usualy send request using address bar, only for aquiring resources; `post` request: commit entity to pointed resources, which changes the state or has sideffects on server, more secure (however both unsecure on the view of data transmition, using `https` to encrypt)
  - entity: usually the object

- spring-boot-starter-web: springboot provides an integrated frame of mvc, json, tomcat
  - webmvc: basic frame
  - json: data parser
  - tomcat: container dependency
  - **auto-configure when ticking spring web**

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

### controller

- Springboot provides `@Controller` and `@RestController` tags
  - receive & handle HTTP requests
  - `@Controller` tag: when requesting **page** and **data**, usually with `Thymeleaf` template engine (*no seperation between front and back ends*)
  - `@RestController` tag: when requesting **only data**, usually converting object into json formmat in default when return

**MVC frame**

![1697121109192](1697121109192.png)

- controller receives users' requests, fetches data from model and reture data to view

### router mapping

- receive user requests
- `@RequestMapping` tag: URL router mapping, defines http request-mapping rule, can be added on controller class or method
  - for class: whole router mapping will add this mapping rule
  - for method: only the method itself
  - properties:
    - `value`: url path, supports url templates, reg-expr, `@RequestMapping("/user")`
    - `method`: http request methods (get, post), also use: `@GetMapping, @PostMapping`
    - `consumes`: content-type for requests, e.g. application/json
    - `producer`: content-type for resposes (html, json)
    - `params, headers`: requests parameters and requests header

### parameters passing

- get parameters, such as `http://localhost:8080/demo?nickname=zhangsan` passing `zhangsan` to param: `nickname`
- `@RequestParam` tag: receiving parameters from http requests body or QueryString of url, omitted when request-parameter's name is the same with controller method
- `@PathVariable` tag: handle dynamic url, the value of url can be the parameters of controller handler
- `@RequestBody` tag: receives parameters from requestBody, handling data such as `application/json, application/xml`

```java
@RestController
public class DemoController {
  @RequestMapping(value="/demo", method=RequestMethod.GET)
  public String myDemo(String nickname, String phone) {
    return "nickname: " + nickname + " phone: " + phone;
  }
}
```

- my request: `http://localhost:8080/demo?nickname=xr&phone=123`
- output:

![1697123584376](1697123584376.png)

- now parameter mapping handles the situation where request-parameters conflict with method parameters

```java
@RestController
public class DemoController {
  @RequestMapping(value="/demo", method=RequestMethod.GET)
  public String myDemo(@RequestParam("nickname", required = false) String nickname, String phone) {
    return "nickname: " + nickname + " phone: " + phone;
  }
}
```