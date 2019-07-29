# from flask import Flask
# from flask import request, redirect
# import requests
# # from ip import ips
# import time, re
# import flask
#
# # auth, ip_port = ips()
#
# # app = Flask(__name__,static_folder="static")
# app = Flask(__name__)
#
# header = {}
#
#
# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>', methods=['GET', 'POST', "PATCH", "OPTIONS", "PUT"])
# def catch_all(path):
#     # print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
#     print(path)
#     if path.startswith("txnS03.do"):
#         print("22222222222")
#     host = 'http://wsjs.saic.gov.cn/'
#     target_url = host + path
#     dic = {}
#     headers = request.headers
#     print(request.args, 9999)
#     for i in headers:
#         dic[i[0]] = i[1]
#     # dic["Proxy-Authorization"] = auth
#     dic['host'] = 'wsjs.saic.gov.cn'
#
#     # proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
#     r = requests.request(request.method, url=target_url, headers=dic)
#
#     resp = flask.Response(r.content)
#     for k, v in r.headers.items():
#         resp.headers[k] = v
#     resp.headers['Access-Control-Allow-Origin'] = '*'
#     # resp.headers['Proxy-Authorization'] = auth
#     resp.headers.remove('Content-Length')
#     # resp.headers.remove('Vary')
#     # resp.headers.remove('X-Via-JSL')
#     # resp.headers.remove('X-Cache')
#     # resp.headers.remove('Date')
#     # resp.headers.remove('Pragma')
#     # resp.headers.remove('Cache-Control')
#     # resp.headers.remove('Expires')
#     resp.headers.remove('Content-Encoding')
#
#     return resp
#
#
# if __name__ == '__main__':
#     app.run("0.0.0.0", 5000, debug=True)


from contextlib import closing
import requests
from flask import Flask, request, Response

app = Flask(__name__)


@app.before_request
def before_request():
    url = "http://wsjs.saic.gov.cn/"
    print(url, 999)
    method = request.method
    data = request.data or request.form or None
    headers = dict()
    for name, value in request.headers:
        if not value or name == 'Cache-Control':
            continue
        headers[name] = value

    with closing(
        requests.request(method, url, headers=headers, data=data, stream=True)
    ) as r:
        resp_headers = []
        for name, value in r.headers.items():
            if name.lower() in ('content-length', 'connection',
                                'content-encoding'):
                continue
            resp_headers.append((name, value))
        return Response(r, status=r.status_code, headers=resp_headers)


app.run(port=8007, debug=True)
