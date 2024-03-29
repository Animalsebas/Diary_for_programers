import sqlite3
from sqlite3 import Error
from datetime import datetime
#Variables
loop = 1
#Functions
def get_date():
    now = datetime.now()
    global res_date
    res_date = str(now.day)+"/"+str(now.month)+"/"+str(now.year) 
def get_time():
    now = datetime.now()
    global res_time
    res_time = str(now.hour)+":"+str(now.minute)+":"+str(now.second)
def sql_table(db):
    cursorObj = db.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS Diary(id INTEGER PRIMARY KEY AUTOINCREMENT,date, time, entry)")
    db.commit()
def sql_connection():
    try:
        db = sqlite3.connect('./dbdfp.db')
        return db
    except Error:
        print(Error)
def sql_insert(db, data):
    cursorObj = db.cursor()
    cursorObj.execute("INSERT INTO Diary(date, time, entry) VALUES(?, ?, ?)", data)
    db.commit()
def get_entry():
    global res_entry
    res_entry = input("Entry:\n")
def search_by_date():
    print("Enter date: D/M/YYYY")
    selected_date = input()
    cursorObj = db.cursor()
    cursorObj.execute("SELECT * FROM Diary WHERE date="+"'"+str(selected_date)+"'")
    list_by_date = cursorObj.fetchall()
    if list_by_date != []:
        print(list_by_date)
    else:
        print("Not found")
def remove_entry():
    print("Enter date: D/M/YYYY")
    selected_date = input()
    cursorObj = db.cursor()
    cursorObj.execute("SELECT * FROM Diary WHERE date="+"'"+str(selected_date)+"'")
    list_by_date = cursorObj.fetchall()
    if list_by_date != []:
        print(list_by_date)
        print("Select index:")
        selected_index = input()
        cursorObj.execute("Delete FROM Diary WHERE id="+str(selected_index))
        db.commit()
        print("DELETED")
    else:
        print("Not found")
db = sql_connection()
sql_table(db)
print("DIARY FOR PROGRAMERS")
while loop == 1:
    print("Options: write, read, delete, exit")
    option = input()
    option = option.lower()
    if option == "write":
        get_entry()
        get_date()
        get_time()
        data = (str(res_date), str(res_time), str(res_entry))
        sql_insert(db, data)
    elif option == "read":
        search_by_date()
    elif option == "delete":
        remove_entry()
    elif option == "exit":
        loop = 0
    else:
        print("Not valid option")