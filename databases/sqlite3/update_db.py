import sqlite3

conn = sqlite3.connect("test.db")
print("Database opened successfully")

conn.execute("update COMPANY set salary = 25000.00 where id = 1")

conn.commit()
print("Total number of rows updated : ", conn.total_changes)

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

