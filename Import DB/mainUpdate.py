import mysql
from mysql import connector


def update(con, studentId, chapter, data):
    i = (data, studentId)
    sql = "update mapjson set c"+chapter+"=%s where id=%s"
    cur = con.cursor()
    cur.execute(sql, i)
    con.commit()


data = []
for line in open("../测试数据/补查未知.txt", "r", encoding="utf8"):
    data.append(line)
con = mysql.connector.connect(
    host='localhost',
    port='3306',
    user="root",
    password="root",
    database="map"
)
for i in data:
    a = i.split("\t")
    update(con, a[1], a[0], a[2])
con.close()
