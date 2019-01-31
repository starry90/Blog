---
layout: post
title: "Android Studio JNI调用"
subtitle: ""
date: 2017-03-29
author: Starry
category: coding
tags: android
finished: true
---

[简书地址](https://www.jianshu.com/p/7ea781e6b261)

## [下载地址](https://developer.android.google.cn/ndk/downloads/index.html)

>https://developer.android.google.cn/ndk/guides/index.html

>原生开发工具包 (NDK) 是一组可让您在 Android 应用中利用 C 和 C++ 代码的工具。 可用以从您自己的源代码构建，或者利用现有的预构建库。

>NDK 不适用于大多数初学的 Android 编程者，对许多类型的 Android 应用没什么价值。 因为它不可避免地会增加开发过程的复杂性，所以通常不值得使用。 但如果您需要执行以下操作，它可能很有用：

>从设备获取卓越性能以用于计算密集型应用，例如游戏或物理模拟。
重复使用您自己或其他开发者的 C 或 C++ 库。

## 编译环境

gradle 2.1
```
dependencies {
        classpath 'com.android.tools.build:gradle:2.1.0'
    }
```
NDK版本
>android-ndk-r13b-windows-x86_64
>[谷歌中国下载](https://developer.android.google.cn/ndk/downloads/index.html)



Android Studio 2.0版本
```
设置NDK目录
File —> Project Structure —> SDK Location —> Android NDK location
```

## 环境配置

1，在项目根目录下的gradle.properties文件里添加
```
android.useDeprecatedNdk=true
```

2，在项目根目录下的local.properties文件里添加ndk的目录
```
ndk.dir=D\:\\work\\android-ndk-r13b-windows-x86_64
```
3，在项目app目录下的build.gradle文件里添加如下片段
```
android {
    ...

    defaultConfig {
        ...

        ndk {
            moduleName "Sample" //模块名称，对应的动态链接库名称libSample
            ldLibs = ["log"] //在JNI打log 必须加上log,否则会报错log函数未定义
        }

    }
}
```

## 编译工程

1，创建一个类，编写本地方法，加载so库
```
package com.starry.jni;

public class JNISample {

    static {
        System.loadLibrary("Sample");
    }

    public native String getString();
}
```

2，生成头文件，打开Android Studio Terminal窗口（左下角），输入以下指令
```
cd  app/src/main/java  //进入到java目录
javah -jni com.starry.jni.JNISample //生成 点h文件
```
3，新建jni目录，右键工程下的app目录 —> Folder —> JNI Folder —> New Android Component —> Finish，默认是会在app/src/main目录下生成jni目录

4，把第二步生成的com_starry_jni_JNISample.h文件拷贝至第三步生成的jni目录下

5，右键jni目录，New —> C/C++ Source File，新建与头文件相同名称的cpp文件com_starry_jni_JNISample.cpp，完整代码如下
```
#include "com_starry_jni_JNISample.h"

JNIEXPORT jstring JNICALL Java_com_starry_jni_JNISample_getString (JNIEnv *env, jobject obj){

    return env -> NewStringUTF("我来自JNI");
}
```
6，在Activity里调用，代码如下
```
...
JNISample jniSample = new JNISample();
String string = jniSample.getString();
...
```
7，重新编译下工程或直接布署代码到手机上，成功就会在app/build/intermediates/ndk/debug/lib目录下生成相应的so库文件

8，[示例代码下载](https://github.com/starry90/JNI-Sample)


注：

1，JNISample类里边不能用中文件字符

2，我的NDK是从官网下载的，使用Android Studio提供的NDK死活编译不过

3，cpp文件和h文件名称可以自定义，但是最好按照ndk生成的格式命名，方法命名必须按照生成的头文件里的规范命名（Java\_包名\_类名\_方法名称）

4，D:\work\android-ndk-r13b-windows-x86_64\platforms\android-22\arch-arm\usr\include目录里包含了ndk开发所有使用到的头文件，做jni开发可以查看jni.h头文件里提供函数。

5，点击右上角Gradle —> 当前项目 —> app —> Tasks —> Build —> assembleRelease，打包完成，.so文件会自动拷贝到lib目录下，不需要手动拷贝
