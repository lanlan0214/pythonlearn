# # pip install alembic
# # alembic init alembic 這個要在當前資料夾用
# # 在alembic.ini裡面找 sqlalchemy.url = driver://user:pass@localhost/dbname 然後改成 sqlalchemy.url = sqlite:///datafile.db
# # alembic revision -m "create an address table"
# #  alembic upgrade head
# # alembic downgrade -1

from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect

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

inspecter = inspect(engine)
print(inspecter.get_table_names())