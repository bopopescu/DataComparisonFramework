import mysql.connector

class mySqlConnector:
    servername = input("Enter the MySql Servername : ")

    username = input("Enter the UserName : ")
    password = input("Enter the Password : ")
    try:
        conn = mysql.connector.connect(host=servername, user=username, password=password)
        cur = conn.cursor()

    except mysql.connector.Error as err:
        print(err)
