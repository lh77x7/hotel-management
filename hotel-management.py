import mysql.connector as mysql

#global variables
myConnection=""
cursor=""
userName=""
password=""
roomRent=0
foodBill=0
gamingBill=0
fashionBill=0
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
        cursor=myConnection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS HM")
        cursor.execute("COMMIT")
        cursor.close()
        return myConnection
    else:
        print("Check username and password!")
#end module

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
#end module

#new user input data module
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
        phoneNr=input("Write Customer Contact Number: ")
        email=input("Write Customer Email: ")
        sql="INSERT INTO C_Details VALUES(%s, %s, %s, %s, %s, %s, %s)"
        values=(cid, name, address, age, nationality, phoneNr, email)
        cursor.execute(sql, values)
        cursor.execute("COMMIT")
        print("\n New Customer successfully added to system.")
        cursor.close()
    else:
        print("\nMysql Connection failed. Please try again.")
#end module

#booking input data module
def bookingData():
    global cid
    customer=searchCustomer()
    if myConnection:
        cursor=myConnection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS BOOKING_DATA(CID VARCHAR(20), CHECK_IN DATE, CHECK_OUT DATE)")
        checkIn=input("\nWrite Customer Check-in: [yy-mm-dd]: ")
        checkOut=input("\nWrite Customer Check-out: [yy-mm-dd]: ")
        sql="INSERT INTO BOOKING_DATA VALUES(%s, %s, %s)"
        values=(cid, checkIn, checkOut)
        cursor.execute(sql, values)
        cursor.execute("COMMIT")
        print("Check-in and check-out succeessully added.")
        cursor.close()
    else:
        print("\nMysql Connection failed. Please try again.")
#end module

#rooms input rent module
def rentingRooms():
    global cid
    customer=searchCustomer()
    if customer:
        global roomRent
        if myConnection:
            cursor=myConnection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS RENTING_ROOM(CID VARCHAR(20), ROOM_CHOICE INT, NR_OF_DAYS INT, NR_ROOM INT, ROOMRENT INT)")
            print("\nChoose room for you")
            print("1. Royal")
            print("2. Exclusive")
            print("3. Normal")
            print("4. Economy")
            roomChoice=int(input("Write your 1,2,3 or 4: "))
            roomNr=int(input("Write Customer Room Nr: "))
            nrOfDays=int(input("Write Number of Days: "))
            if roomChoice==1:
                roomRent=nrOfDays*1000
                print("\nRoyal Room Rent: ", roomRent)
            elif roomChoice==2:
                roomRent=nrOfDays*800
                print("\nExclusive Room Rent: ", roomRent)
            elif roomChoice==3:
                roomRent=nrOfDays*500
                print("\nNormal Room Rent: ", roomRent)
            elif roomChoice==4:
                roomRent=nrOfDays*250
                print("\nEconomy Room Rent: ", roomRent)
            else:
                print("Choice 1,2,3 or 4")
                return
            sql="INSERT INTO RENTING_ROOM VALUES(%s, %s, %s, %s)"
            values=(cid, roomChoice, roomNr, roomRent)
            cursor.close()
        else:
            print("\nMysql Connection failed. Please try again")
#end module

#food input module
def food():
    global cid
    customer=searchCustomer()
    if customer:
        global foodBill
        if myConnection:
            cursor=myConnection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS FOOD(CID VARCHAR(20), CUSINE VARCHAR(30), QUANTITY VARCHAR(30), BILL VARCHAR(30))")
            print("\n1. Vegetarian \n2. Non-Vegetarian \n3. Mixed")
            foodChoice=int(input("Write your choice: "))
            quantity=int(input("Write quantity: "))
            if foodChoice==1:
                print("\nYou ordered vegatarian food")
                foodBill=quantity*300
            elif foodChoice==2:
                print("\nYou ordered non-vegatarian food")
                foodBill=quantity*500
            elif foodChoice==3:
                print("\nYou ordered mixed food")
                foodBill=quantity*700
            else:
                print("You can only choice 1,2 or 3")
                return
            sql="INSERT INTO FOOD VALUES(%s, %s, %s, %s)"
            values=(cid, foodChoice, quantity, foodBill)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")
            print("\nYour total bill is: ", foodBill)
            print("\nEnjoy your meal!")
            cursor.close()
        else:
            print("\nMysql Connection failed. Please try again.")
#end module

#gaming input module
def gaming():
    global cid
    customer=searchCustomer()
    if customer:
        global gamingBill
        if myConnection:
            cursor=myConnection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS GAMING(CID VARCHAR(20), GAMES VARCHAR(30), HOURS VARCHAR(30), GAMING_BILL VARCHAR(30))")
            print("\n1. Video games\n2. Bowling\n3. Snooker\n4. Table" "tennis\n5. Exit")
            selectedGame=int(input("Select your game: "))
            gamingHours=int(input("How many hours you play: "))
            if selectedGame==1:
                print("You selected video games")
                gamingBill=gamingHours*50
            elif selectedGame==2:
                print("You selected bowling")
                gamingBill=gamingHours*100
            elif selectedGame==3:
                print("Your selected snooker")
                gamingBill=gamingHours*150
            elif selectedGame==4:
                print("You selected table tennis")
                gamingBill=gamingHours*200
            else:
                print("You can only choice 1,2,3 or 4")
                return
            sql="INSERT INTO GAMING VALUES(%s, %s, %s, %s)"
            values=(cid, selectedGame, gamingHours, gamingBill)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")
            print("\nYour gaming bill for ", gamingHours, " is: ", gamingBill)
            cursor.close()
        else:
            print("\nMysql Connection failed. Please try again.")
#end module

#fashion input module
def fashion():
    global cid
    customer=searchCustomer()
    if customer:
        global fashionBill
        if myConnection:
            cursor=myConnection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS FASHION(CID VARCHAR(20), DRESS VARCHAR(20), AMOUNT VARCHAR(30), BILL VARCHAR(30))")
            print("1. Pants\n2. Socks\n3. T-Shirts\n4. Trausers")
            selectedClothes=int(input("Write your choice: "))
            quantity=int(input("How many you want to buy: "))
            if selectedClothes==1:
                fashionBill=quantity*20
                fashionName='Pants'
            elif selectedClothes==2:
                fashionBill=quantity*30
                fashionName='Socks'
            elif selectedClothes==3:
                fashionBill=quantity*40
                fashionName='T-shirts'
            elif selectedClothes==4:
                fashionBill=quantity*50
                fashionName='Trausers'
            else:
                print("Choose option 1,2,3 or 4")
                return
            sql="INSERT INTO FASHION VALUES(%s, %s, %s, %s)"
            values=(cid, selectedClothes, quantity, fashionBill)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")
            print("You selected ", quantity, fashionName)
            print("Bill: ", fashionBill)
            cursor.close()
        else:
            print("\nMysql Connection failed. Please try again.")
#end module

#totalAmount module
def totalAmount():
    global cid
    customer=searchCustomer()
    if customer:
        global totalAmount
        global roomRent
        global foodBill
        global fashionBill
        global gamingBill
        if myConnection:
            cursor=myConnection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS TOTAL(CID VARCHAR(20), C_NAME VARCHAR(30), ROOMRENT INT, FOOD_BILL INT, GAMING_BILL INT, FASHION_BILL INT, TOTALAMOUNT INT)")
            sql="INSERT INTO TOTAL VALUES(%s, %s, %s, %s, %s, %s, %s)"
            name=input("Write Customer Name: ")
            totalAmount=roomRent + foodBill + fashionBill + gamingBill
            values=(cid, name, roomRent, foodBill, gamingBill, fashionBill, totalAmount)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")
            cursor.close()
            print("\n----------Customer Billing--------------")
            print("\nCustomer Name: ", name)
            print("\nRoom Rent: ", roomRent)
            print("\nFood Bill: ", foodBill)
            print("\nGaming Bill: ", gamingBill)
            print("------------------------------------------")
            print("\nTotal cash: ", totalAmount, " Euro.")
            cursor.close()
        else:
            print("\nMysql Connection failed")
#end module

#searching older bill module
def searchOldBill():
    global cid
    customer=searchCustomer()
    if customer:
        if myConnection:
            cursor=myConnection.cursor()
            sql="SELECT * FROM TOTAL WHERE CID=%s"
            cursor.execute(sql, (cid,))
            data=cursor.fetchall()
            if data:
                print(data)
            else:
                print("\nRecord Not Found. Please try again.")
                cursor.close()
        else:
            print("\nMysql Connetion failed.")
    else:
        print("\nSomething went wrong. Please try again.")
#end module

#searching customer module
def searchCustomer():
    global cid
    if myConnection:
        cursor=myConnection.cursor()
        cid=input("Write Customer id: ")
        sql="SELECT * FROM C_Details WHERE CID=%s"
        cursor.execute(sql,(cid,))
        data=cursor.fetchall()
        if data:
            print(data)
            return True
        else:
            print("Not Found Data. Try again")
            return False
        cursor.close()
    else:
        print("\nSomething went wrong. Please try again")
#end module

#main menu module
print("-----------------------------------------------")
print("Hotel management system")
print("-----------------------------------------------")
myConnection=mysqlConnectionCheck()
if myConnection:
    mysqlConnection()
    while(True):
        print("\n1. Write Customer Data\n2. Write Booking Data"
        "\n3. Calculate Room Rent \n4. Calculate Restaurant Bill"
        "\n5. Calculate Gaming Bill \n6. Calculate Fashion Bill"
        "\n7. Display Customer Data \n8. Generate Total Bill Amount"
        "\n9. Generate Old Bill \n10. Exit")
        choice=int(input("Write Your Choice: "))
        if choice==1:
            UserInput()
        elif choice==2:
            bookingData()
        elif choice==3:
            rentingRooms()
        elif choice==4:
            food()
        elif choice==5:
            gaming()
        elif choice==6:
            fashion()
        elif choice==7:
            searchCustomer()
        elif choice==8:
            totalAmount()
        elif choice==9:
            searchOldBill()
        elif choice==10:
            break
        else:
            print("Please select 1,2,3,4,5,6,7,8,9 or 10")
else:
    print("\nMysql Connection failed.")
#end module
