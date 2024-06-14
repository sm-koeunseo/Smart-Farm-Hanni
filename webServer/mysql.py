import pymysql

try:
    db = pymysql.connect(host='127.0.0.1', user='test', password='test', db='test', charset='utf8')
    cursor = db.cursor()

    sql = "select * from user"
    cursor.execute(sql)

    results = cursor.fetchall() # get all row
    #cursor.fetchone() # get one row
    #cursor.fetchmany(n) # get n row

    for row in results:
        print (row)

    #db.commit()
except pymysql.MySQLError as e:
    print(f"Error: {e}")
    
finally:
    db.close()