import mysql.connector;

def deleteEmp(id):
    connect = mysql.connector.connect(host="localhost",database='mydb',user='root',password='ali0786')
    if connect.is_connected():
        print("connected to database")
        curser=connect.cursor()
        str = "delete from emp where empID='%d'"
        args=(id)
        try:
            curser.execute(str % args)
            connect.commit()
            print('Employee Deleted')
        except:
            print("something went wrong")
            connect.rollback()
        finally:
            curser.close()
            connect.close()

empID=input("Enter Employee ID= ")
deleteEmp(empID)