import os
import re

from flask import Flask, render_template, request, redirect

import regex_converter

app = Flask(__name__)
app.url_map.converters['re'] = regex_converter.RegexConverter


@app.route("/<re('/w+'):path>")
def index(path):
    print(path)
    path = request.args.get("path")
    if path:
        return redirect(f"/{path}")
    listdir = os.listdir("..")
    for index, dir in enumerate(listdir):
        if not re.search("\.", dir):
            listdir[index] = dir + "/"
    return render_template("index.html", listdir=listdir)


@app.route(r"/file/<re('\w+'):path>")
def get_child(path):
    print("child_dir: ", path)
    listdir = os.listdir(f"../{path}")
    # return str(listdir)
    return "ojbk"


@app.before_request
def get_path():
    path = request.path
    print(path)
    print(request.args)
    return


if __name__ == '__main__':
    app.run(debug=True)
