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

SpringBoot + Vue development

- JavaEE: SpringBoot + MyBatis Plus
- Web front end: Vue + ElementUI

<!--more-->>

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

### static resources visit

- put self static resources here
- visit by `http://localhost:8080/test.png`

![1697173796277](1697173796277.png)

- modify static path pattern: add `spring.mvc.static-path-pattern=/images/**` to `application.properties`

### upload files

- front end form
  - modify `enctype="multipart/form-data"`, otherwise can't upload files
- `tomcat` limits the size of files by default:
  - single file < `1MB`
  - single request < `10MB`
  - modify the size

```properties
spring.servlet.multipart.max-file-size=10MB
spring.servlet.multipart.max-request-size=10MB
```

- receiver data-type: `MultipartFile`
- receiver writing method: `transferTo`

**attention:** the parameter name should be same with front end form name

### interceptor

> situation: use every function after login
> judge login state in ANY controller -> code repeating
> extract to intercepter

- authority checking
- performance monitoring
- general behaviour: reading cookie to get user information and put it to request

- Springboot interface: `HandlerInterceptor`
  - `preHandle`
  - `postHandle`
  - `afterCompletion`

![1697177213073](1697177213073.png)

**how to define**

- extend from system `HandlerInterceptor`
- override parents' method used, usually `preHandle`
- register interceptor

```java
// in com.example.demo.interceptor.LonginInterceptor
public class LoginInterceptor implements HandlerInterceptor {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        System.out.println("LoginInterceptor");
        return true;
    }
}

// in com.example.demo.config.WebConfig
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        // interceptor for the path /user/**
        registry.addInterceptor(new LoginInterceptor()).addPathPatterns("/user/**");
    }
}
```

## build RESTful serve

- framework rule
- popular website software service framework designing style
- basic rule, style

- every URI maps a kind of resource
- `GET` for acquiring resources, `POST` for creating/updating resources, `PUT` for updating resources, `DELETE` for deleting resources

**HTTP method**

![1697178943507](1697178943507.png)

- just a **style**, not standard requirements

**HTTP state code**

- 1xx: info
- 2xx: success
- 3xx: redirection
- 4xx: client error
- 5xx: server error

**how to write RESTful API**

- use tags
- for RESTful framework: every address corresponds a resource, so URI is suggested to be no-verb, pure nouns, and these nouns should conrresponds to database's sheet
  - pass parameters using address: `@PathVariable in id`

**Swagger**

- generate API document
  - description
  - debugging
  - dynamically

- configuration:

```xml

<!--in pow.xml-->
<dependency>
  <groupId>io.springfox</groupId>
  <artifactId>springfox-swagger2</artifactId>
  <version>2.9.2</version>
</dependency>

<dependency>
  <groupId>io.springfox</groupId>
  <artifactId>springfox-swagger-ui</artifactId>
  <version>2.9.2</version>
</dependency>
```

```properties
spring.mvc.pathmatch.matching-strategy=ant_path_matcher
```

- visit: `http://localhost:8080/swagger-ui.html`

**use swagger notation(tag) add methods docs**

[swagger tag usage](https://linkis.apache.org/zh-CN/docs/latest/development/swwager/)

- swagger convinent front end developer to look up the apis
- another important thing: swagger page can send requests to debug the apis

> **recommend**
> springboot 3.0+ is recommended to use `springdoc`

## MyBatis Plus (DB configuration)

**ORM**

- Object relation mapping
  - handle OOP objects -> DB storage or DB storage -> OOP objects

![1697182386692](1697182386692.png)

- MyBatis: ORM frame
- MyBatis-Plus: simpified MyBatis
  - use component: `mapper`
  - db-related operations: in `mapper` package

**configuration**

- add dependencies(`pow.xml`)
  - mybatis-plus
  - mysql
  - connection pool

```xml
<!--		mybatis-plus dependency-->
<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>3.0.1</version>
</dependency>

<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.5.2</version>
</dependency>

<!--		mysql driver-->
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>5.1.47</version>
</dependency>

<!--		sql connection pool-->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid-spring-boot-starter</artifactId>
    <version>1.1.20</version>
</dependency>
```

- global configuration(`application.properties`)

```properties
spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/mydb?userSSL=false
spring.datasource.username=root
spring.datasource.password=root
mybatis-plus.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl
```

- create MySQL data DB, schema and Tables

![1697187931126](1697187931126.png)

- add tags on Activation Class (main class): `@MapperScan("com.example.demo.mapper")`, scan mapper packages before running

- create mapper interface, and implemented by MyBatis (use `@Mapper` tag on the interface, meaning this is a component, it will use Dynamic Proxy to instanciate an object with `@Autowired`. And all sql sentences are finished by tags)

```java
@Mapper
public interface UserMapper {
    // add declarations, impl by Mybatis
    // query all users
    // find in user db (named mydb), configured in application.properties
    @Select("select * from user")
    public List<User> query();

    // return type stand for the number of records be inserted
    @Insert("insert into user values (#{id}, #{username}, #{password}, #{gender})")
    public int insert(User user);
}
```

- for a more simply form, namely use MyBatis-Plus, that's all:
  - attention that the class name should be the same with your database table name, unless you use [tags](https://baomidou.com/pages/223848/#tablename)

```java
@Mapper
public interface UserMapper extends BaseMapper<User> {}
```

- use the mapper to edit database data
  - create controller `UserController` (we have created `User` entity before)

```java
@RestController
public class UserController {

    @Autowired
    private UserMapper userMapper;
    @GetMapping("/user")
    public List<User> query() {
        return userMapper.query();
    }

    @PostMapping("/user")
    public String insert(User user) {
        var state = userMapper.insert(user);
        if (state <= 0) {
            return "insert fail";
        }
        return "insert success";
    }
}
```

  - where `@Autowired` is an injection method, which helps to instanciate UserMapper

## Axios

> a frame of front-end requesting
> - front-end needs data, browser sends HTTP requests to server to fetch data, Vue bonds data
> - based on `Ajax`, `promise`
> - use `XMLHttpRequests` to send web requests, convert `json` data automatically
`npm install axios`

[帮助文档](https://axios-http.com/docs/intro)

### send web requests

**send `GET` requests**

```JavaScript
axios.get('/user?ID=12345')
  .then(function(response) {
    // handle successful situations
    console.log(response);
  })
  .catch(function(error) {
    // handle failures
    console.log(error);
  })
  .then(function() {
    // always execute
  });

// the same with:

axios.get('/user', {
    params: {
      ID: 12345
    }
  })
  .then(function(response) {
    // handle successful situations
    console.log(response);
  })
  .catch(function(error) {
    // handle failures
    console.log(error);
  })
  .then(function() {
    // always execute
  });
```

**send `POST` requests**

```JavaScript
// request body is the second parameter
axios.post('/user', {
    firstName: 'xxx',
    lastName: 'xxx'
  })
  .then(function(response) {
    // handle successful situations
    console.log(response);
  })
  .catch(function(error) {
    // handle failures
    console.log(error);
  })
  .then(function() {
    // always execute
  });
```

### when to send requests

`created:function(){}`: invoked when creating the components

`mounted:function(){}`: invoked when mounting the components

**cross-domain**

- usually appears in front-back end separation projects
- **same-origin-policy**: the basic and core security function of browsers
  - same-origin, i.e. same-domain, where two page have the same protocol, host and port
- **cross-domain**: request url appears when any of protocol, host and port is different from current page url
  - can't read cross-domain cookies
  - can't send `Ajax` requests to cross-domain addresses
- **authorization** to solve cross-domain questions
  - CORS(cross-origin resource sharing): designed by W3C
  - simple requests/complex requests
  - back-end server realize CORS interfaces

for single controller: `@CrossOrigin`

for global controler: add configuration class 

- send requests when the component is created:

```JavaScript
// use arrow function: "this" points to parents' "this", able to visit parameters of parents "tableData"
created:function(){
  axios.get("http://localhost:8088/user/findAll").then((response)=>{
    this.tableData = response.data
  })
},
data() {
  return {
    tableData: []
  }
}
```

**set base url**

- `axios.defualts.baseURL = 'http://api.com'`
- `app.config.globalProperties.$http = axios`