import mysql.connector
def readToChapterJson(col):
    jsondata={}
    con = mysql.connector.connect(
        host='localhost',
        port='3306',
        user="root",
        password="root",
        database="map"
    )
    cur = con.cursor()
    sql = "select name ," + col + " from mapjson"
    cur.execute(sql)
    result = cur.fetchall()
    for i in result:
        jsondata[i[0]]=i[1]
    con.close()
    # print(nameMatrix)
    return jsondata