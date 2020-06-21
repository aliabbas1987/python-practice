import mysql.connector;
connect = mysql.connector.connect(host="localhost",database='mydb',user='root',password='ali0786')
if connect.is_connected():
    print("connected to database")
    curser=connect.cursor()
    try:
        curser.execute("insert into emp values(3,'Mohammad',100)")
        connect.commit()
        print('Employee Added')
    except:
        connect.rollback()
    
curser.close()
connect.close()