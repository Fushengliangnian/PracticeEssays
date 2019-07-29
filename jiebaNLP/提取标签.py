# -*- coding: utf-8 -*-
import re

import jieba.analyse

import get_content


for content, active_id in get_content.get_content():
    sentence = re.sub("<.*?>", "", content)
    ret = jieba.analyse.extract_tags(sentence, topK=20, withWeight=True, allowPOS=())
    active_id = active_id.split("/")[-1]
    key_words = ""
    for k, v in ret:
        if v > 0.05:
            key_words = key_words + k + "，"
    print(key_words, active_id)
    break
