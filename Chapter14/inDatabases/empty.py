# # SQLite 存進去資料到資料庫裡面
# import sqlite3

# conn = sqlite3.connect("datafile.db")
# cursor = conn.cursor()
# cursor.execute("""create table people (id integer primary key, name text, count integer)""")
# cursor.execute("""insert into people (name, count) values (?, ?)""", ('Bob', 25))
# cursor.execute("""insert into people (name, count) values (:username, :usercount)""", {"username" : "Test" , "usercount" : 10})
# cursor.execute("""insert into people (name, count) values (:username, :usercount)""", {"username" : "Test1" , "usercount" : 11})
# cursor.execute("""insert into people (name, count) values (:username, :usercount)""", {"username" : "Test2" , "usercount" : 12})
# cursor.execute("""insert into people (name, count) values (:username, :usercount)""", {"username" : "Test3" , "usercount" : 13})

# conn.commit()
# conn.close()

# # 讀取資料庫裏面的資訊 都是tuple方式給的

# conn = sqlite3.connect("datafile.db")
# cursor = conn.cursor()

# # result = cursor.execute("select * from people where name = 'Frank'")
# # # print(result.fetchall()) #全部
# # # print(result.fetchone()) #第一筆
# # print(result.fetchmany(2)) #這是可以拿到幾筆的意思

# # 刪除
# # cursor.execute("""delete from people where name = 'Bob'""")

# # 更新的方法
# # cursor.execute("""update people set count = :usercount where name = :username""", {"username" : "Bob" , "usercount" : 39})
# result = cursor.execute("select * from people")
# print(result.fetchall())

# conn.commit()
# conn.close()

##################################################################################################################################################################

# 可以查詢目前資料庫有誰 然後這樣查是有風險的
# 我可以在input那裡輸入 1' OR '1'='1 這樣可以查到所有人
# select * from people where name = '1' OR '1'='1' # '1' OR '1'='1'這個會變成True 然後就等於是select * from people 

# import sqlite3
# conn = sqlite3.connect("datafile.db")
# name = input("Please type the name you want to search : ")
# cursor = conn.cursor()
# result = cursor.execute("""select * from people where name = '{}'""".format(name))
# print(result.fetchall())
# conn.close()

##################################################################################################################################################################

# # 防止出現可能被攻擊 改這樣比較好
# import sqlite3
# conn = sqlite3.connect("datafile.db")
# name = input("Please type the name you want to search : ")
# cursor = conn.cursor()
# # result = cursor.execute("""select * from people where name = :username""", {"username" : name})
# result = cursor.execute("""select * from people where name = ?""", (name,))
# print(result.fetchall())
# conn.close()

##################################################################################################################################################################
# 下支影片中，錄影當下下載的SQL Alchemy的版本是1.4.22版，但目前的版本跟錄影當下的不相容。因此，當下載SQL Alchemy時，要使用：

# pip install sqlalchemy==1.4.22

# 這個指令。另外，下面的影片「Alembic」也是一樣，需要使用

# pip install alembic==1.7.7

# 這個指令來安裝特定版本，這樣就可以了。
##################################################################################################################################################################
# # ORM的做法

# from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
# from sqlalchemy.orm import sessionmaker

# dbPath = 'datafile.db'
# engine = create_engine('sqlite:///%s' %dbPath)
# metadata = MetaData(engine)
# people = Table('people', metadata, Column('id', Integer, primary_key = True), Column('name', String), Column('count', Integer))
# Session = sessionmaker(bind=engine)
# session = Session()
# metadata.create_all(engine)

# # # 這邊是插入的
# # insert_statement = people.insert().values(name = 'Bob', count = 66)
# # insert_statement = people.insert()
# # session.execute(insert_statement, [
# #     {'name': 'TTQ', 'count' : 35},
# #     {'name': 'PPPQ', 'count' : 40}
# # ])
# # session.commit()

# # update
# session.execute(people.update().values(count=105).where(people.c.name == 'Frank'))

# # result = session.execute(select([people]))
# result = session.execute(select([people]).where(people.c.name == 'Frank'))
# for row in result:
#     print(row)

##################################################################################################################################################################
# # class obj 比較合理

from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dbPath = 'datafile.db'
engine = create_engine('sqlite:///%s' %dbPath)
metadata = MetaData(engine)
people = Table('people', metadata, Column('id', Integer, primary_key = True), Column('name', String), Column('count', Integer))

Base = declarative_base()
class People (Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key = True)
    name = Column('name', String)
    count = Column('count', Integer)


Session = sessionmaker(bind=engine)
session = Session()
metadata.create_all(engine)

# # 這邊是新增
# new1 = People(name = 'QQ', count = 54)
# new2 = People(name = 'QQ1', count = 54)
# new3 = People(name = 'QQ2', count = 54)
# new4 = People(name = 'QQ3', count = 54)

# session.add(new1)
# session.add(new2)
# session.add(new3)
# session.add(new4)

# # 這邊是update
# frank = session.query(People).filter_by(name = 'Frank').first()
# frank.count = 99
# session.add(frank)

# 這邊是delete
# frank = session.query(People).filter_by(name = 'Frank').first()
# session.delete(frank)

session.commit()

for r in session.query(People).all():
    print(r.id, r.name, r.count)