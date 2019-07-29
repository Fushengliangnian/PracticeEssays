import re


class Request(object):
    def __init__(self, environ):
        self.environ = environ.decode("utf8")
        self._heard, self._body = self.environ.split("\r\n\r\n", 1)
        self.method, self._path, self.http = self.environ.split("\r\n", 1)[0].split(" ")

    def get_path(self):
        _, path, queries = re.split("(/.*?)\?", self._path)
        return path, queries

    @property
    def path(self):
        if "?" not in self._path:
            return self._path
        return self.get_path()[0]

    @property
    def heard(self):
        heard_list = self._heard.split("\r\n")
        dic = {}
        for heard in heard_list:
            try:
                k, v = heard.split(": ", 1)
                dic[k] = v
            except ValueError:
                pass
        return dic

    @property
    def form(self):
        ret = re.split("----------------------------\d+", self._body)
        data = {}
        for i in ret:
            try:
                k, v = re.findall('name="(.*?)"\r\n\r\n(.*?)\r\n', i)[0]
                data[k] = v
            except IndexError:
                pass
        return data

    @property
    def query(self):
        data = {}
        queries = self.get_path()[1]
        for query in queries.split("&"):
            k, v = query.split("=")
            data[k] = v
        return data


if __name__ == '__main__':
    "".split()
