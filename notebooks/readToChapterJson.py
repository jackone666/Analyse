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
    nameArra=[]
    cur = con.cursor()
    sql = "select id ," + col + ",name from mapjson"
    cur.execute(sql)
    result = cur.fetchall()
    for i in result:
        jsondata[str(i[0])]=i[1]
        nameArra.append(i[2])
    con.close()
    # print(nameMatrix)
    return jsondata,nameArra