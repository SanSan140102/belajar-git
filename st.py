import pymysql.cursors

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="sansan_db"
)

mycursor = mydb.cursor()

sql = "INSERT INTO user (nama, email,password) VALUES (%s, %s,%s)"
val = ("John", "Highway 21@gmail.com","jhon123")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "berhsail di insert.")
