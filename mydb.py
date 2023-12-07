import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Isolante1950@',
    auth_plugin='mysql_native_password',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE teste")

print("Al Done!")
