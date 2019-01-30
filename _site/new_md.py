#! /usr/bin/env python3
# coding = utf-8

import time
import os

file_name = "temp"
author = "Starry"
local_time = time.strftime("%Y-%m-%d", time.localtime())
temp_file = "_posts/%s-%s.markdown" % (local_time, file_name)
print (temp_file)

if os.path.exists(temp_file):
    os.remove(temp_file)

with open(temp_file, "w") as f:
    f.writelines("---\n")
    f.writelines("layout: post\n")
    f.writelines("title: \"%s\"\n" % file_name)
    f.writelines("subtitle: \"\"\n")
    f.writelines("date: " + local_time + "\n")
    f.writelines("author: %s\n" % author)
    f.writelines("category: coding\n")
    f.writelines("tags: code\n")
    f.writelines("finished: true\n")
    f.writelines("---\n\n\n")

with open(temp_file, "r") as f:
    print (f.read())
