import os

lis = os.listdir("/Users/mac/Desktop/piano_bac/piano/")
for filename in lis:
    file_list = filename.split(".")
    pro = file_list[-1]
    name = file_list[0]
    if pro != "json":
        continue
    os.popen(f"/Users/mac/opt/mongodb-osx-x86_64-4.0.5/bin/mongoimport -d testDemo -c {name} --file /Users/mac/Desktop/piano_bac/piano/{filename}")
