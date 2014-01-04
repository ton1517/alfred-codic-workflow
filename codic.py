# -*- coding: utf-8 -*-

from urllib import quote
from urllib2 import Request, urlopen
import json
import sys
import re

import alfred

base_url = "http://codic.jp"
rm_mark_re = re.compile("</?mark>")
icon = alfred.storage.getLocalIfExists("icon.png")
headers = {"X-Requested-With": "XMLHttpRequest"}


def feedback_codic_suggestion(query):
    url = base_url + "/suggest?q=%s&dic=null" % quote(query)
    res = urlopen(Request(url, None, headers))
    j = json.loads(res.read())

    feedback = alfred.Feedback()

    for title, description, url in zip(j["titles"], j["descriptions"], j["urls"]):
        title = rm_mark_re.sub("", title)
        feedback.addItem(title=description, subtitle=title, icon=icon, arg=base_url+url)

    feedback.output()


if __name__ == "__main__":
    feedback_codic_suggestion(sys.argv[1])
