import pymysql.cursors

db_url = "localhost"
db_user = "root"
db_password = ""
db_name = "sansan_db"

db = pymysql.connect(host=db_url,user=db_user,password=db_password,database=db_name)

cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print(f"DATABASE VERSION : {data}")

cursor.execute("SELECT Nama,Nik,Nama_prodi,Matkul FROM mahasiswa  JOIN parodi on mahasiswa.prodi_id=parodi.prodi_id JOIN mata_kuliah ON mahasiswa.matkul_id=mata_kuliah.Matkul_id  WHERE  mahasiswa.Nama =%s","sinta")
data = cursor.fetchone()
print(data)
    
    
# sql_insert = "INSERT INTO user(Nama,email,Password,no_telpon) VALUES (%s,%s,%s,%s)"
# values     = ("pan","pan12@gmail.com","21","08126778")
# try:
#     cursor.execute(sql_insert,values)
#     db.commit()
#     print("data berhasil di insert")
    
# except pymysql.Error as e:
#     db.rollback()
#     print(f"error:{e}")
    
    
    
#  sql_update = "UPDATE user SET nama=%s,email=%s,password=%s,no_telpon=%s WHERE user_id=%s"
# values_update=("san","san","san","1234",3)

# try:
#     cursor.execute(sql_update,values_update)
#     db.commit()
#     print("data berhasil di update")
    
# except pymysql.Error as e:
#     db.rollback()
#     print(f"error:{e}")
    
    
# sql_delete = "DELETE FROM `user` WHERE user_id=%s"
# values_delete= (1)
# try:
#     cursor.execute(sql_delete,values_delete)
#     db.commit()
#     print("data berhasil di delete")
    
# except pymysql.Error as e:
#     db.rollback()
#     print(f"error:{e}")




