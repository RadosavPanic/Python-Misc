import pymysql

host_name = "localhost"
port_number = 3306
user_name = "root"
db_name = "testdb"

db = pymysql.connect(host=host_name, port=port_number, user=user_name, db=db_name)

print(f"Database '{db_name}' opened successfully")

cursor = db.cursor()

table_name = "employee"

sql = f"""insert into {table_name}(first_name, last_name, age, sex, income)
                     values('%s', '%s', '%d', '%s', '%d')""" % ('John', 'Doe', 23, 'M', 2000)

try:
    cursor.execute(sql)
    db.commit()
    print(f"Operation done successfully (table: {table_name})")
except pymysql.Error as e:
    print(f"An error (pymysql) occurred: {e}")
    db.rollback()


db.close()


