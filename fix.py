#!/usr/bin/env python

import re
import sys
import os

file_to_open = sys.argv[1]

if not file_to_open:
    print("enter the filename")
    sys.exit()

f = open(file_to_open, "r")
filecontents = "".join(f.readlines())
f.close()

filecontents = re.sub(r"---\n", "", filecontents)
filecontents = re.sub(r"author:\n- admin\n", r"author: admin\n", filecontents)
filecontents = re.sub(r"slug: '([a-zA-Z0-9\-]*)'\n", r"slug: \1\n", filecontents)
filecontents = re.sub(r"date: '([0-9\-\:\s]*)'\n", r"date: \1\n", filecontents)
filecontents = re.sub(r"tags: '([a-zA-Z0-9\-,]*)'\n", r"tags: \1\n", filecontents)

f2 = open(file_to_open + ".new", "w")
f2.write(filecontents)
f2.close()

os.rename(file_to_open, file_to_open + ".bak")
os.rename(file_to_open + ".new", file_to_open)
