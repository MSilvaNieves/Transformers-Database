import sqlite3

conn = sqlite3.connect("TransformersDb.db")
cursor = conn.cursor()

query = conn.execute('select * from Transformers')

names = [description[0] for description in query.description]

t_Name = input("Please input " + names[1] + ": ")
t_Series = input("Please input " + names[2] + ": ")
t_Year = int(input("Please input " + names[3] + ": "))
t_Condition = input("Please input " + names[4] + ": ")
t_PreOwned = int(input("Please input " + names[5] + ": "))

data_entry = """INSERT INTO Transformers(name, series, year, condition, previously_owned) VALUES (?,?,?,?,?)"""

cursor.execute(data_entry, (t_Name, t_Series, t_Year, t_Condition, t_PreOwned))
conn.commit()
print("Info Recieved")
conn.close()