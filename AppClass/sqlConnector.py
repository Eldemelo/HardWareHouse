import mysql.connector



db = mysql.connector.connect(
    host = "localhost",
    user = "username",
    passwd = "password"
)

myCursor = db.cursor()

myCursor.execute("CREATE DATABASE ")