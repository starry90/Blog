---
layout: post
title: "Android Spanned各种用法"
subtitle: ""
date: 2019-07-16
author: Starry
category: coding
tags: android spanned
finished: true
---

## 解析文字中的URL（超链接）

```
String content = "内容中的http://www.baidu.com会成为可单击跳转的超链接";
Spannable spannable = Spannable.Factory.getInstance().newSpannable(content);
//设置识别URL（超链接）
Linkify.addLinks(spannable, Linkify.WEB_URLS);
URLSpan[] urlSpans = spannable.getSpans(0, spannable.length(), URLSpan.class);
for (URLSpan urlSpan : urlSpans) {
    Log.e(TAG, "URL: " + urlSpan.getURL());
}
```

## TextView设置可点击文字中的URL（超链接）

```
TextView tv_demo_link = findViewById(R.id.tv_demo_link);
//设置URL（超链接）可点击
tv_demo_link.setMovementMethod(LinkMovementMethod.getInstance());
String content = "内容中的http://www.baidu.com会成为可单击跳转的超链接";
Spannable spannable = Spannable.Factory.getInstance().newSpannable(content);
//设置识别URL（超链接）
Linkify.addLinks(spannable, Linkify.WEB_URLS);
tv_demo_link.setText(spannable);
```