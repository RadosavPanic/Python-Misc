import sqlite3

conn = sqlite3.connect("test.db")

print("Database opened successfully")

cursor = conn.execute("select id, name, address, salary from COMPANY")

for row in cursor:
    print("-" * 20)
    print("id = ", row[0])
    print("name = ", row[1])
    print("address = ", row[2])
    print("salary = ", row[3])
    print("-" * 20)

print("Operation done successfully")

conn.close()
