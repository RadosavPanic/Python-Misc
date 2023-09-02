import sqlite3

conn = sqlite3.connect("test.db")

print("Database opened successfully")

conn.execute("""create table COMPANY
                (id int primary key not null,
                name text not null,
                age int not null,
                address char(50),
                salary real);
""")

print("Table created successfully")

conn.execute("insert into COMPANY (id, name, age, address, salary) values(1, 'Paul', 32, 'California', 20000.00)")
conn.execute("insert into COMPANY (id, name, age, address, salary) values(2, 'Allen', 25, 'Texas', 15000.00)")
conn.execute("insert into COMPANY (id, name, age, address, salary) values(3, 'Mark', 23, 'Norway', 20000.00)")

conn.commit()
print("Records created successfully")
conn.close()


