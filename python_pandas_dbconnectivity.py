import mysql.connector as myc
'''pip install mysql-connector-python'''
connection = myc.connect(
    host ='localhost',
    user ='root',
    password ='Admin',
    database ='LMES'
)
if connection.is_connected():
    cursor=connection.cursor()
    cursor.execute('select * from python')
    result=cursor.fetchall()
    print(result)