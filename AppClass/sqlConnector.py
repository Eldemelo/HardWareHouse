import mysql.connector

class databaseAccess():
    def __init__(self):
        return
    
    def checkForDB():
        #TODO
        dbExists = False
        return dbExists


db = mysql.connector.connect(
    host = "localhost",
    user = "username",
    passwd = "password"
)

myCursor = db.cursor()

myCursor.execute("CREATE DATABASE ")