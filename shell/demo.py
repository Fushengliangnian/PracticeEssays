#coding:utf-8
import json
import commands

(status, output) = commands.getstatusoutput('''sudo netstat -tlnp|grep 'mongod'|awk '{print $4}'|awk -F':' '{print $(NF)}'|sort -u|grep -v "^28"''')
outputs = output.split('\n')
ports = []
for port in  outputs:
    ports += [{'{#MONGOPORT}': port}]

print json.dumps({'data':ports},sort_keys=True,indent=4)