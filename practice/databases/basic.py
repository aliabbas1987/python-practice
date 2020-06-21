import mysql.connector;
connect = mysql.connector.connect(host="localhost",database='mydb',user='root',password='ali0786')
if connect.is_connected():
    print("connected to database")
    curser=connect.cursor()
    curser.execute("select * from emp")
    rows = curser.fetchall()
    for row in rows:
        print(row)
curser.close()
connect.close()