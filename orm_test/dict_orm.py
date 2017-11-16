from sqlalchemy.types import TypeDecorator
from sqlalchemy import Column, Table, Integer
import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from dbconn import DB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dict(TypeDecorator):
	
	impl = sqlalchemy.String()
	
	def process_bind_param(self,value,dialect):
		if value is not None:
			value = json.dumps(value)

                return value

	def process_result_value(self,value,dialect):
		if value is not None:
			value = json.loads(value)
		
		return value




class DictTable(Base):
	__tablename__ = "dicttable"

        id = Column(Integer,primary_key=True)
        d = Column(Dict())

        def __init__(self, d={}):
                    self.d = d

if __name__ == "__main__":
    db = DB()
    Base.metadata.create_all(db.eng)
    session = db.get_session()
    item = {"thing":"thang"}
    s = DictTable(d=item)
    session.add(s)
    session.commit()
