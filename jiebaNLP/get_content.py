import re

import requests

url = "http://yinji666.immusician.com"
headers = {}

ret = requests.get(url)
url_list = re.findall('<a href="(.*?)">', ret.text)[2: -4]


def get_content():
    for url_active in url_list:
        path = url + url_active
        content = requests.get(path).text
        yield (re.findall('<div class="col-md-8">(.*?)<div class="col-md-4">', content, re.S)[0], url_active)
