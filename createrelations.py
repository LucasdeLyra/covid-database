import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root", 
    database='refined'
)
cursor = mydb.cursor()
with open('./fk_set/commands.sql', 'r') as commands:
    for line in commands:
        cursor.execute(str(line))
