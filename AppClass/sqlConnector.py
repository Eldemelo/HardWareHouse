import mysql.connector

# class for accessing the database
class databaseAccess():
    def __init__(self):
        return
    
    # Function to check if the database exists already
    def checkForDB():
        #TODO
        dbExists = False
        return dbExists

# Attempt to connect to the sql database
db = mysql.connector.connect(
    host = "localhost",
    user = "username",
    passwd = "password"
)

# Create cursor
myCursor = db.cursor()

# User cursor to perform queries
myCursor.execute("CREATE DATABASE ")