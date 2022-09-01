---
title: AndroidBasic
date: 2022-09-01 15:59:05
category: Android
mathjax: true
---

"我只是想学kotlin而已"

"我不理解"

<!--more-->

# 布局
## Linear Layout

比较常用的属性:

```xml
android:id
android:layout_width
android:layout_height
android:background
android:layout_margin
android:layout_padding
android:layout_orientation
android:gravity  <!--相对位置-->
android:layout_weight  <!--将剩余内容平分-->
```

## Relative Layout

比较常用的属性:

```xml
android:layout_toLeftOf
androidLlayout_toRightOf
android:alignBottom
android:alignParentBottom
android:layout_below
```

# 控件
## Text View

可以实现 **文字大小, 颜色; 显示不下时使用...; 文字加icon; 中划线, 下划线; 跑马灯**

`kotlin`实现中划线要重写扩展方法`apply()`

```kotlin
my_text_view.apply {
    paintFlags = paintFlags or Paint.STRIKE_THRU_TEXT_FLAGS or Paint.ANTI_ALIAS_FLAG
}
```

## Material Button

谷歌给的`Button`控件, 继承了之前的`Button`

需要在`app/build.gradle`中添加依赖:

```gradle
    implementation group: 'com.google.android.material', name: 'material', version: '1.4.0'
```

还需要更换谷歌它指定的样式主题, 在`values/theme.xml`中将主题改为

```xml
    Theme.MaterialComponents.Light.NoActionBar
```

同步后便可以使用谷歌的`MaterialButton`, 不过为了修改属性, 用到了`app`和`tool`, 因此在相应的`activity`文件头添加:

```xml
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
```
以示礼貌

**重点**

按钮又不是摆设, 所以要设计相应的页面跳转, 也就是需要实现相应的`clickListener`

```kotlin
class ...

    private lateinit var mBtn: MaterialButton

    override fun onCreate ...

        mBtn = findViewById(R.id.button_name)
        mBtn.setOnClickListener() {
            startActivity(Intent(this, OtherActivity::class.java))
        }
```

接着是颜值比较高的选择栏设计: