import mysql.connector
import xlrd

dataXlsx = xlrd.open_workbook('../data/cbj-导图处理结束.xlsx')
table = dataXlsx.sheet_by_name("Sheet1")
data = []
rowsNum = table.nrows
for i in range(1, rowsNum):
    rowsData = []
    for j in range(0, 19):
        colData = table.cell(i, j).value
        # print(colData)
        rowsData.append(colData)
        # print(rowsData)
    data.append(tuple(rowsData))
# 以数组的形式填充数据
con = mysql.connector.connect(
    host='localhost',
    port='3306',
    user="root",
    password="root",
    database="map"
)
cur = con.cursor()
sql = "INSERT INTO mapjson(id,name,sid,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16) " \
      "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
for i in data:
    # print(i)
    cur.execute(sql, i)
    con.commit()
con.close()
# print("成功插入%d条数据,最后一条的id为:%d" % (cur.rowcount, cur.lastrowid))
