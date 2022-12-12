import mysql.connector
if __name__ == '__main__':
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root", 
    )
    cursor = mydb.cursor()
    with open('./createtables/commands.sql', 'r') as commands:
        for line in commands:
            cursor.execute(str(line))
