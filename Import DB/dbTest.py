import mysql.connector
from models.drawMap.tomapOne import toMap
from models import ParseToMatrix


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
        if str(i[1]).__contains__("root"):
            tree, level, map = ParseToMatrix.returnMatrix(i[1])
            toMap(map)
            for j in tree.index:
                print(j)
            break
if __name__ == '__main__':
    readToChapterMaTri("c16")