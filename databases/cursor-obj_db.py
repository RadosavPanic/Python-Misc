import sqlite3

conn = sqlite3.connect("test2.db")
cursor = conn.cursor()

cursor.execute("create table stocks(date text, trans text, symbol text, qty real, price real)")
cursor.execute("insert into stocks values('2023-04-20', 'buy', 'micro', 100, 35.14)")

conn.commit()
conn.close()

conn = sqlite3.connect("test2.db")
cursor = conn.cursor()

symb = ('micro',)

cursor.execute("select * from stocks where symbol=?", symb)
print(cursor.fetchone())

purchases = [('2023-03-28', 'buy', 'ibm', 1000, 45.00),
             ('2023-04-05', 'buy', 'msft', 1000, 72.00),
             ('2023-04-06', 'sell', 'ibm', 500, 53.00)]

cursor.executemany("insert into stocks values (?,?,?,?,?)", purchases)
for row in cursor.execute("select * from stocks order by price"):
    print(row)

