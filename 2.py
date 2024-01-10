import pymysql.cursors

class Database:
    
    def __init__(self):
        
        self.db     = pymysql.connect(host="localhost",user="root",password="",database="sansan_db")
        self.cursor = self.db.cursor()
        
    def query(self,q, value=None):
        if value is not None:
            self.cursor.execute(q,value)
        else:
            self.cursor.execute(q)
        
    def single(self):
        return self.cursor.fetchone()
    
    def multiple(self):
        return self.cursor.fetchall()
    
    def insert(self,nama,password,email):
        query = "INSERT INTO user (nama, password, email) VALUES (%s, %s, %s)"
        values = (nama,password,email )
        self.cursor.execute(query, values)
        self.db.commit()
    
    # def update(self):
    #     pass  
        
    # def delete(self):
    #     pass
    
# db = Database
# user_query = "SELECT * FROM user"
# user_data = db.query(user_query)
# data_user = db.multiple()
# for i in data_user:
#     print(i)


db = Database()
db.insert("sansan12","san12","san@gmail.com")
# user= db.query("SELECT * FROM user")
# data_user =db.multiple()
# for i in data_user:
#     print(i)
    
    
# parodi = db.query("SELECT * FROM parodi")
# data_parodi = db.multiple()
# for a in data_parodi:
#     print(a)
    

    