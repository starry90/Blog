#! /usr/bin/env bash
set -e
set -u

if [ $# -lt 1 ]
then
    echo "example:" $0 "filename"
    exit
fi

local_time=`date +%Y-%m-%d`

new_file="_posts/${local_time}-$1.markdown"
echo "---" >> ${new_file}
echo "layout: post" >> ${new_file}
echo "title: \"$1\"" >> ${new_file}
echo "subtitle: \"\"" >> ${new_file}
echo "date: "${local_time} >> ${new_file}
echo "author: Starry" >> ${new_file}
echo "category: coding" >> ${new_file}
echo "tags: code" >> ${new_file}
echo "finished: true" >> ${new_file}
echo "---" >> ${new_file}
echo "" >> ${new_file}

cat ${new_file}