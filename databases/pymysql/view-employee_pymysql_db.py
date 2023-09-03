import pymysql

host_name = "localhost"
port_number = 3306
user_name = "root"
db_name = "testdb"

db = pymysql.connect(host=host_name, port=port_number, user=user_name, db=db_name)

print(f"Database '{db_name}' opened successfully")

cursor = db.cursor()

table_name = "employee"

sql = f"select * from {table_name} where income > '%d'" % 1000

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
    print("fname = %s, lname = %s, age = %d, sex = %s, income = %d" % (fname, lname, age, sex, income))
except pymysql.Error as e:
    print(f"An error occured (pymysql): {e}")
    print("Error: unable to fetch data")

db.close()
