import json
import os
import uuid

from locust import web
from locust import runners
from locust.main import find_locustfile, load_locustfile
from flask import render_template, Flask, request, redirect

app = Flask(__name__)
PATH_BASE = "/Users/mac/PycharmProjects/TorndoDemo/测试工具/"


@app.route("/add_router", methods=["POST", "GET"])
def add_router():
    if request.method == "POST":
        name = request.form.get("name")
        if not name:
            name = uuid.uuid4()
        url = request.form.get("url")
        if not url:
            return "url 必填"
        data = request.form.get("data")
        if not data:
            data = {}
        path = os.path.join(PATH_BASE, "locustfile.py")
        with open(path, "a+", encoding="utf8") as f:
            f.write(f"    @task\n    def {name}(self):\n        self.client.get('{url}', data={data})\n")
        docstring, locusts = load_locustfile(path)
        locust_classes = list(locusts.values())
        runners.locust_runner = runners.LocalLocustRunner(locust_classes, None)
        return redirect("/")
    return render_template("add_router.html")


if __name__ == '__main__':
    app.run(port=9999)
