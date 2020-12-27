import mysql.connector

#global variables
myConnection=""
cursor=""
userName=""
password=""
roomrent=0
foodbill=0
gamingbill=0
fashionbill=0
totalAmount=0
cid=""

#mysql connection module
def mysqlConnectionCheck():
    global myConnection
    global userName
    global password
    userName = input("\nMysql Server username: ")
    password = input("\nMysql Server password: ")
    myConnection=mysql.connector.connect(host="localhost", user=userName, password=password)
    if myConnection:
        print("You are connected!")
        cursor=myConnection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS HM")
        cursor.execute("COMMIT")
        cursor.close()
        return myConnection
    else:
        print("Check username and password!")

mysqlConnectionCheck()
