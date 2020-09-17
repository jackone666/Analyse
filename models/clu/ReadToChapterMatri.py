import xlrd
import mysql.connector

from models import ParseToMatrix


# 一单元导图的矩阵
def readToChapterMaTri(col):
    con = mysql.connector.connect(
        host='localhost',
        port='3306',
        user="root",
        password="root",
        database="map"
    )
    cur = con.cursor()
    sql = "select name ,"+col+" from mapjson"
    cur.execute(sql)
    result = cur.fetchall()
    nameMatrix={}
    for i in result:
        # print(i)
        if str(i[1]).__contains__("root"):
            tree, level, map = ParseToMatrix.returnMatrix(i[1])
            nameMatrix[i[0]] = map
    con.close()
    # print(nameMatrix)
    return nameMatrix
