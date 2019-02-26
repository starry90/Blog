---
layout: post
title: "Linux下repo获取代码"
subtitle: ""
date: 2018-11-15
author: Starry
category: coding
tags: linux
finished: true
---

## 1.设置代理
```
export HTTP_PROXY=http://192.168.1.100:8888
export HTTPS_PROXY=http://192.168.1.100:8888
```

## 2.安装repo
```
sudo apt install repo
```

## 3.初始化repo
```
repo init
```
```
注：初始化需要从如下连接获取数据，需要翻墙或设置代理(参照第1步)
Get https://gerrit.googlesource.com/git-repo/clone.bundle
Get https://gerrit.googlesource.com/git-repo
```

## 4.获取代码
 ./repo_init.sh {develop group name} {Gerrit user name} {branch name}
```
./repo_init.sh client liudehua develop
```

repo_init.sh脚本源码如下
```
#!/usr/bin/env bash

PATH_REPO="~/bin/repo"
if [ -f ${PATH_REPO} ] ; then
    echo "repo download ..."
    mkdir -p ~/bin
    PATH=~/bin:$PATH
    curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
    chmod a+x ~/bin/repo
fi

if [ $# != 3 ] ; then
    echo "input develop name and user name and branch name, such as: ./repo_init.sh your-dev-group-name your-gerrit-name branch-name"
    exit 1;
fi

DEV_GROUP_NAME=$1
USER_NAME=$2
BRANCH_NAME=$3
HOST=192.168.1.39:29418
repo init -u ssh://${USER_NAME}@${HOST}/${DEV_GROUP_NAME}/platform --repo-url=ssh://${USER_NAME}@${HOST}/urepo --repo-branch=stable -b ${BRANCH_NAME} -m ${DEV_GROUP_NAME}.xml
repo sync
```