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

#mysql connection established module
def mysqlConnection():
    global username
    global password
    global myConnection
    global cid
    myConnection=mysql.connector.connect(host="localhost", user=userName, password=password)
    if myConnection:
        return myConnection
    else:
        print("\nMysql connection failed")
        myConnection.close()

#new user input deta module

#booking input date module

#rooms input rent module

#gaming input module

#fashion input module

#totalAmount module

#searching older bill module

#searching customer module

#main menu module
