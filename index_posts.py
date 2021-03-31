#!/usr/bin/env python3

from os import listdir
from urllib.parse import quote
import json
"""
Get a markdown file, parse it up, create a JSON data structure.
We want something like:
id - url
title - title
tags - tags
body - the body of the post
"""

markdownfiles = [ filename for filename in listdir("content") if filename.endswith("md") ]

for a_file in markdownfiles:
    search_data = {}
    search_data['id'] = "http://thebooze.ninja/" + quote(a_file).replace(".md", ".html")

    f = open("content/"+a_file, "r")
    filecontents = f.readlines()
    f.close()

    # the front matter is always the first 7 lines
    front_matter = filecontents[0:6]
    remainder = filecontents[7:]
    search_data['title'] = front_matter[0].split(":")[1].strip()
    tags = front_matter[3].split(" ")[1].split(",")
    search_data['tags'] = [tag.strip() for tag in tags]
    search_data['body'] = "".join([line.strip() for line in remainder])

    f = open("search_data/"+a_file.replace(".md", ".json"), "w")
    f.write(json.dumps(search_data))
    f.close()

    """
    TODO:
    """