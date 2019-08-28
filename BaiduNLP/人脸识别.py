# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-26 20:08
# @Author  : lidong@immusician.com
# @Site    :
# @File    : 人脸识别.py
import requests, base64


def get_ass_token():
    url = 'https://aip.baidubce.com/oauth/2.0/token?' \
          'grant_type=client_credentials' \
          '&client_id=Aku7VXauCzOte9Ojrd2iDeUp' \
          '&client_secret=tgkVmsz4VKyRGNj4jQBSRPhItZu9eeUh'
    response = requests.post(url)  # 获取响应
    res = response.json()
    return res.get('access_token')


# img = input('')

with open("./1.png", 'rb') as f:
    raw = f.read()
base = base64.b64encode(raw)
base = base.decode('utf-8')
data = [{'image': base,
         'image_type': 'BASE64',
         'face_field': 'age,beauty,expression,face_shape,gender,glasses,landmark,race,quality,face_type'}]
header = {'Content-Type': 'application/json'}
url = f'https://aip.baidubce.com/rest/2.0/face/v3/faceverify?access_token={get_ass_token()}'
res = requests.post(url, headers=header, json=data)
print(res.json())


