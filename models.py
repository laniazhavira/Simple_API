from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///quotes.db")
conn = engine.connect()
metadata = MetaData()

metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class QuoteModel(Base):
	__tablename__ = 'quotes'

	id = Column(Integer, primary_key=True, index=True)
	content = Column(String, nullable=False)

def ro_dict(self):
	return{"id": self.id, "content": self.content}

def get_db():
	db =SessionLocal()
	try:
		yield db 
	finally:
		db.close()
