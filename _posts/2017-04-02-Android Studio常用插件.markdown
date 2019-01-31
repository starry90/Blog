---
layout: post
title: "Android Studio常用插件"
subtitle: ""
date: 2017-04-02
author: Starry
category: coding
tags: android
finished: true
---

[简书地址](https://www.jianshu.com/p/840b93fe84fe)

Android Studio插件安装：File —> Settings —> Plugins，搜索关键字即可安装。

## 0，.ignore   [github地址](https://github.com/hsz/idea-gitignore)
在项目视图中着色忽略的文件，如下：
![ignore.png](../images/android/plugin.png)

## 1，Android ButterKnife Zelezny   [github地址](https://github.com/avast/android-butterknife-zelezny)
用于生成ButterKnife注解绑定View的代码
```
右击Activity里setContentView里的布局文件 —> Generate... —> Generate ButterKnife Injections
```

## 2，GsonFormat [github地址](https://github.com/zzz40500/GsonFormat)
用于根据json生成实体类
```
在实体类内部右击 —> Generate...  —> GsonFormat
```

## 3，Android Parcelable code generator
用于生成实现Parcelable接口要实现的代码
```
在实体类内部右击 —> Generate...  —> Parcelable
```

## 4，SelectorChapek for Android   [github地址](https://github.com/inmite/android-selector-chapek)
用于根据命名规范的图片生成Selector，注意必须有_normal和_pressed后缀的图片
```
右击图片所在的drawable文件夹 —> Generate Android Selectors
```

## 5，Markdown Navigator    [github地址](https://github.com/vsch/idea-multimarkdown)
>**[Markdown](http://daringfireball.net/projects/markdown) language support for IntelliJ platform**
**A Markdown plugin** with GFM and a **matching** preview style.
**Get Markdown Navigator [enhanced edition](http://vladsch.com/product/markdown-navigator) to unlock all productivity features.**
