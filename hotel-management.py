import mysql.connector as mysql

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
    myConnection=mysql.connect(host="localhost", user=userName, password=password)
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
    global database
    myConnection=mysql.connect(host="localhost", user=userName, password=password, database="hm")
    if myConnection:
        return myConnection
    else:
        print("\nMysql connection failed")
        myConnection.close()

#new user input deta module
def UserInput():
    global cid
    if myConnection:
        cursor=myConnection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS C_Details(CID VARCHAR(20), CNAME VARCHAR(30), C_ADDRESS VARCHAR(30), C_AGE VARCHAR(30),C_COUNTRY VARCHAR(30), P_NO VARCHAR(30), C_EMAIL VARCHAR(30))")
        cid=input("Write Customer Identyfication Number: ")
        name=input("Write Customer Name: ")
        address=input("Write Customer Address: ")
        age=input("Write Customer Age: ")
        nationality=input("Write Customer Country: ")
        phoneno=input("Write Customer Contact Number: ")
        email=input("Write Customer Email: ")
        sql="INSERT INTO C_Details VALUES(%s, %s, %s, %s, %s, %s, %s)"
        values=(cid, name, address, age, nationality, phoneno, email)
        cursor.execute(sql, values)
        cursor.execute("COMMIT")
        print("\n New Customer successfully added to system.")
        cursor.close()
    else:
        print("\nMysql Connection faild.")

#called only for testing purposes
mysqlConnectionCheck()
mysqlConnection()
UserInput()

#booking input date module

#rooms input rent module

#gaming input module

#fashion input module

#totalAmount module

#searching older bill module

#searching customer module

#main menu module
