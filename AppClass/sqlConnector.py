import mysql.connector
import pyodbc

# class for accessing the database
class databaseAccess():
    def __init__(self):
        return
    
    # Function to check if the database exists already
    def checkForDB():
        #TODO
        dbExists = False
        return dbExists

# Attempt to connect to the sql database - mysql
'''db = mysql.connector.connect(
    host = "localhost",
    user = "username",
    passwd = "password"
)
'''

# pyodbc connection variables - pb
connect_str = (
        r'Driver=SQL Server;'
        r'Server=192.168.70.80;'
        r'Database=INVENTORY;'
        r'Trusted_Connection=yes')
# connect pyodbc with variables
cnexion = pyodbc.connect(connect_str)

# Create cursor (mysql)
# myCursor = db.cursor()

# Create cursor (pyodbc)
myCursor = cnexion

# User cursor to perform queries
myCursor.execute("CREATE DATABASE ")