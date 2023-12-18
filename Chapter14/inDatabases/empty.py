# SQLite 存進去資料到資料庫裡面
import sqlite3

conn = sqlite3.connect("datafile.db")
cursor = conn.cursor()
cursor.execute("""create table people (id integer primary key, name text, count integer)""")
cursor.execute("""insert into people (name, count) values (?, ?)""", ('Bob', 25))
cursor.execute("""insert into people (name, count) values (:username, :usercount)""", {"username" : "Frank" , "usercount" : 27})

conn.commit()
conn.close()

# 讀取資料庫裏面的資訊
