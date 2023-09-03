import pymysql

host_name = "localhost"
port_number = 3306
user_name = "root"
db_name = "testdb"

db = pymysql.connect(host=host_name, port=port_number, user=user_name, db=db_name)

print(f"Database '{db_name}' opened successfully")

cursor = db.cursor()

table_name = "login"

cursor.execute(f"drop table if exists {table_name}")

sql = f"""create table {table_name} (
                      username char(20) not null, 
                      password char(20) not null)"""

cursor.execute(sql)

print(f"Table '{table_name}' created successfully")

