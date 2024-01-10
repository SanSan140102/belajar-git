import pymysql

class Database:

    def __init__(self, host="localhost", user="root", password="", database="sansan_db"):
        self.db = pymysql.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.db.cursor()

    def execute(self, query, values=None):
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

    def fetch_one(self):
        return self.cursor.fetchone()

    def fetch_all(self):
        return self.cursor.fetchall()

    def commit(self):
        self.db.commit()

    def close(self):
       self.db.close()

class User:
    def __init__(self):
        self.db = Database()

    def insert(self, name, email, password, no_telp):
        query = "INSERT INTO users (nama, email, password, no_telp) VALUES (%s, %s, %s, %s)"
        values = (name, email, password, no_telp)
        self.db.execute(query, values)
        self.db.commit()

    def update(self, user_id, name, email, password, no_telp):
        query = "UPDATE users SET nama=%s, email=%s, password=%s, no_telp=%s WHERE user_id=%s"
        values = (name, email, password, no_telp, user_id)
        self.db.execute(query, values)
        self.db.commit()


    def delete(self, user_id):
        query = "DELETE FROM user WHERE user_id=%s"
        values = (user_id,)
        self.db.execute(query, values)
        self.db.commit()
        print("berhasil delete")

    def get_user(self, user_id):
        query = "SELECT * FROM users WHERE user_id=%s"
        values = (user_id,)
        self.db.execute(query, values)
        return self.db.fetch_one()

    def get_all_users(self):
        query = "SELECT * FROM user"
        self.db.execute(query)
        return self.db.fetch_all()

user = User()
# user.insert("fadil", "fadil21", "fadil@gmail.com", "123456789")
# print(user.get_all_users())
user.insert()
user.update()
user.delete(3)



