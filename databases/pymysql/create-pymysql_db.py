import pymysql

db = pymysql.connect(host="localhost", port=3306, user="root", db="testdb")

print("Database opened successfully")

cursor = db.cursor()

cursor.execute("drop table if exists employee")

sql = """create table employee (
                first_name char(20) not null,
                last_name char(20),
                age int,
                sex char(1),
                income float)"""

cursor.execute(sql)

print("Database created successfully")

db.close()