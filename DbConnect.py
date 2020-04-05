import cx_Oracle
myconn=cx_Oracle.connect('HR/Sumeet@localhost')
mycursor=myconn.cursor()
mycursor.execute("select * from employees")
result=mycursor.fetchall()
print (result)