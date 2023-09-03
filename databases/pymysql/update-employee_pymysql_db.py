import pymysql

host_name = "localhost"
port_number = 3306
user_name = "root"
db_name = "testdb"

db = pymysql.connect(host=host_name, port=port_number, user=user_name, db=db_name)

print(f"Database '{db_name}' opened successfully")

cursor = db.cursor()

table_name = "employee"

sql = f"update {table_name} set age = age + 1 where sex = '%c'" % 'M'

try:
    cursor.execute(sql)
    db.commit()
    print(f"Operation done successfully (table: {table_name})")
except pymysql.Error as e:
    print(f"An error (pymysql) occurred: {e}")
    db.rollback()

db.close()
