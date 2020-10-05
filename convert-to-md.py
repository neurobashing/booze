#!/usr/bin/env python3

import re
import sys
import os
from pprint import pprint

"""
open file
change first line to Title:
remove second line
get rid of leading : from the rest of the front matter
the rest of the file is OK
"""

file_to_open = sys.argv[1]

if not file_to_open:
    print("enter the filename")
    sys.exit()

f = open(file_to_open, "r")
filecontents = f.readlines()
f.close()

new_filecontents = []

# get rid of the title line thing
if "#" in filecontents[1]:
    del filecontents[1]
title = filecontents[0]  # we'll need the title later, bc it's reused in the front matter

# we have to transform the front matter a little.
front_matter = filecontents[1:7]
front_matter_dict = {}
for item in front_matter:
    item_parts = item.split(":")
    if item_parts[0] == "":
        del item_parts[0]
    if item_parts[0] == "date":
        front_matter_dict["Date: "] = ":".join(item_parts[1:]).strip()
    else:
        fixed_key = item_parts[0].title() + ": "
        front_matter_dict[fixed_key] = "".join(item_parts[1:]).strip()
del front_matter_dict["Status: "]
front_matter_dict["Summary: "] = title.strip()
front_matter_dict["Title: "] = title.strip()

for k,v in front_matter_dict.items():
    new_filecontents.append(k + v + "\n")

new_filecontents.append("\n")    
for item in filecontents[8:]:
    new_filecontents.append(item)

# delete sole \n lines?
filestring = "".join(new_filecontents)

if not os.path.isfile(file_to_open.replace(".rst", ".md")):
    f = open(file_to_open.replace(".rst", ".md"), "w")
    f.write(filestring)
    f.close()
