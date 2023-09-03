import pymysql

host_name = "localhost"
port_number = 3306
user_name = "root"
db_name = "testdb"

db = pymysql.connect(host=host_name, port=port_number, user=user_name, db=db_name)

print(f"Database '{db_name}' opened successfully")

cursor = db.cursor()

cursor.execute("drop table if exists employee")

table_name = "employee"

sql = f"""create table {table_name} (
                first_name char(20) not null,
                last_name char(20),
                age int,
                sex char(1),
                income float)"""

cursor.execute(sql)

print(f"Table '{table_name}' created successfully")

db.close()
