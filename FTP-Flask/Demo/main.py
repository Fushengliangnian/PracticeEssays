# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-19 22:39
# @Author  : lidong@immusician.com
# @Site    :
# @File    : main.py
from flask import Flask, send_file


app = Flask(__name__)


@app.route("/")
def index():
    response = send_file("../../js/dd.epub")
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


@app.route("/js/dd.epub")
def de():
    response = send_file("../../js/dd.epub")
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


@app.route("/OEBPS/content.opf")
def d():
    response = send_file("../../js/d/OEBPS/content.opf")
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


if __name__ == '__main__':
    app.run(debug=True)
