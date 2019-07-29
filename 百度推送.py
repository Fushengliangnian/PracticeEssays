import requests

url = "http://data.zz.baidu.com/urls?site=yinji666.immusician.com&token=po7X39hRVSVXeHeY"
headers = {
    "User-Agent": "curl/7.12.1",
    "Content-Type": "text/plain"
}
data = {
    "urls": ["http://yinji666.immusician.com/active/175"]
}

response = requests.post(url=url, headers=headers, data=data)
print(response.status_code)
print(response.json())
print(response.content)
