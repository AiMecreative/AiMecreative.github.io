---
title: Full Stack | RuoYi-Vue
author: Andrew-Rey
date: 2023-11-04 14:20:10
category: SE
tag:
- Full stack
- Framework
- RuoYi
---

"a glance of RuoYi-vue framework"

[ref](https://www.bilibili.com/video/BV1HT4y1d7oA/?spm_id_from=333.337.top_right_bar_window_history.content.click&vd_source=698de1256a0048d0fd59d2f1bc3e109b)

<!--more-->

## configuration

- mysql configuration
  - use datagrip, run scrips in `sql/*.sql`
  - construct tables
  - !!IMPORTANT!! use `utf8` when creating your database
  - edit configuration file `ruoyi-admin/src/main/resources/application-druid.yml` to your database
- start redis server
  - in cmd: `redis-server`
  - edit configuration file `ruoyi-admin/src/main/resources/application.yml` to your server port
- start back-end
  - in `ruoyi-admin/` find `RuoYiApplication.java` and run it
  - success when visiting `http://localhost:8080`

![1699079331780](1699079331780.png)

- start front-end
  - download the dependencies
  - in `ruoyi-ui/`
  - `npm run dev`

![1699079479931](1699079479931.png)

> success when the validation code image appears -> front-back-end

## validation code

> the first interactions between front and back

> back-end generate a expr: such as `1+1=2` generate `1+1=?@2`, where `@` divides question and anwser
> - give `1+1=?` to front
> - store `2` in redis (会给前端传一份以确定是哪个key，放在隐藏域，用户提交表单)
> - confirm user input and redis anwser

### front-end

- cross-field
  - 反向代理，映射到后端

![1699081297521](1699081297521.png)

- 将`/dev-api`替换为空，再映射到`8080`
  - 例如：`http://localhost:80/dev-api/captchaImage` -> `http://localhost:8080/captchaImage`

### back-end

