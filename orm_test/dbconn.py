from Credentials import *
from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine.url import URL 
from sqlalchemy.orm import sessionmaker


class DB():

    def __init__(self,hostname='10.128.0.7',credentials='cred.yml',db='bubbles',port=49162):
	self.hostname = hostname
	self.cred = Credentials(credentials).get()
	self.db = db
	self.port = port
    
	#Create Connection information
        conn_url = {'drivername':'postgres',
		    'username'  : self.cred['user'],
		    'password'  : self.cred['password'],
		    'host'  : self.hostname,
		    'port'      : self.port,
		    'database'  : self.db
		   } 
	self.eng = create_engine(URL(**conn_url),client_encoding='utf8')
	self.meta = MetaData(bind=self.eng,reflect=True)

    def get_eng(self):
	return self.eng

    def get_meta(self):
	return self.meta   

    def get_session(self):
	Session = sessionmaker(bind=self.eng)
	return Session()

    def close(self):
	self.eng.close()


    

