---
layout: post
title: "RecyclerView使用时遇到的问题"
subtitle: ""
date: 2017-02-28
author: Starry
category: coding
tags: android recyclerview
finished: true
---

[简书地址](https://www.jianshu.com/p/490691084fb9)

#### 1，定位到列表中指定位置
```
List：
ListView.selection(position);

RecyclerView：
 ((LinearLayoutManager)RecyclerView.getLayoutManager()).scrollToPositionWithOffset(position, 0);

```
#### 2，RecyclerView删除Item
```
lists.remove(position); //把数据从list中remove掉
notifyItemRemoved(position);//显示动画
notifyDataSetChanged();//刷新列表
```

#### 3，有一个常见的坑就是”闪屏问题”。

这个问题的描述是：当Item视图中有图片和文字，当更新文字并调用notifyItemChanged()时，文字改变的同时图片会闪一下。这个问题的原因是当调用notifyItemChanged()时，会调用DefaultItemAnimator的animateChangeImpl()执行change动画，该动画会使得Item的透明度从0变为1，从而造成闪屏。

解决办法很简单，在RecyclerView.setAdapter(mAdapter)之前，禁用change动画
```
((SimpleItemAnimator)RecyclerView.getItemAnimator()).setSupportsChangeAnimations(false);
RecyclerView.setAdapter(mAdapter);
```

####  4，[Positions in RecyclerView:](https://developer.android.google.cn/reference/android/support/v7/widget/RecyclerView.html)

>RecyclerView introduces an additional level of abstraction between the RecyclerView.Adapter and RecyclerView.LayoutManager to be able to detect data set changes in batches during a layout calculation. This saves LayoutManager from tracking adapter changes to calculate animations. It also helps with performance because all view bindings happen at the same time and unnecessary bindings are avoided.

>For this reason, there are two types of position related methods in RecyclerView:

>* layout position: Position of an item in the latest layout calculation. This is the position from the LayoutManager's perspective.
>* adapter position: Position of an item in the adapter. This is the position from the Adapter's perspective.

>These two positions are the same except the time between dispatching adapter.notify* events and calculating the updated layout.

>Methods that return or receive *LayoutPosition* use position as of the latest layout calculation (e.g. getLayoutPosition(), findViewHolderForLayoutPosition(int)). These positions include all changes until the last layout calculation. You can rely on these positions to be consistent with what user is currently seeing on the screen. For example, if you have a list of items on the screen and user asks for the 5th element, you should use these methods as they'll match what user is seeing.

>The other set of position related methods are in the form of *AdapterPosition*. (e.g. getAdapterPosition(), findViewHolderForAdapterPosition(int)) You should use these methods when you need to work with up-to-date adapter positions even if they may not have been reflected to layout yet. For example, if you want to access the item in the adapter on a ViewHolder click, you should use getAdapterPosition(). Beware that these methods may not be able to calculate adapter positions if notifyDataSetChanged() has been called and new layout has not yet been calculated. For this reasons, you should carefully handle NO_POSITION or null results from these methods.

>When writing a RecyclerView.LayoutManager you almost always want to use layout positions whereas when writing an RecyclerView.Adapter, you probably want to use adapter positions.

#### 4.Error:(40, 5) 错误: 方法不会覆盖或实现超类型的方法 xxx/BaseRecyclerAdapter.java

Error:(40, 5) 错误 xxx不是抽象的, 并且未覆盖xxx中的抽象方法onBindViewHolder(BaseRecyclerAdapter.ViewHolder,int)
```
public abstract class BaseRecyclerAdapter<T> extends RecyclerView.Adapter<BaseRecyclerAdapter.RecyclerViewHolder> {

    ......

    @Override
    public void onBindViewHolder(RecyclerViewHolder holder, int position) {}

    ......
}
```
改成
```
public abstract class BaseRecyclerAdapter<T> extends RecyclerView.Adapter<BaseRecyclerAdapter.RecyclerViewHolder> {

    ......

    @Override
    public void onBindViewHolder(BaseRecyclerAdapter.RecyclerViewHolder holder, int position) {}

    ......
}
```
将onBindViewHolder方法的holder参数显示指定为BaseRecyclerAdapter.RecyclerViewHolder，就编译通过了
