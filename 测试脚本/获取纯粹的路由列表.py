import re

lis = []
with open("router.json", "r", encoding="utf-8") as f:
    for line in f:
        ret = re.search("r'(.*?)',", line)
        if ret:
            lis.append(ret.group(1))
    print(lis)

with open("locustfile.py", "a+", encoding="utf-8") as f:
    for i, router in enumerate(lis):
        f.write(f"    @task\n    def router{i}(self):\n        self.client.get('{router}')\n")
