import demjson
data = []
for line in open("../测试数据/补查处理结束1.txt", "r", encoding="utf8"):
    data.append(line)
count=0
for i in data:
    a = i.split("\t")
    print(a)
    json=demjson.decode(a[2])
    print(json['root']['text']+count.__str__())
    count=count+1
    # break

