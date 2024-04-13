from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from models import QuoteModel, get_db
from schema import Quote 
from typing import List
import random 

app = FastAPI()


@app.get("/")
def read_root():
	return {"message": "Go to /quotes/random/ to get your quotes of the day"}

@app.post ("/quotes", response_model=Quote)
def create_quote(quote: Quote, db: Session = Depends(get_db)):
	try:
		if not quote.content.strip():
			raise ValueError("Content is Required")
		new_quote = QuoteModel(content=quote.content)
		db.add(new_quote)
		db.commit()
		db.refresh(new_quote)
		return new_quote
	except ValueError as e:
		raise HTTPException(status_code=400, detail=str(e))

@app.get("/quotes/random/", response_model=Quote)
def get_random_quote (db: Session = Depends(get_db)):
	quote = db.query(QuoteModel).order_by(func.random()).first()
	if quote is None :
		raise HTTPException(status_code=404, detail="Quote not found")
	return quote

@app.get("/quotes", response_model=List[Quote])
def get_all_quotes(db: Session = Depends(get_db)):
	quotes = db.query(QuoteModel).all()
	return quotes

@app.put("/quotes/{quote_id}", response_model=Quote)
def update_quote(quote_id: int, quote: Quote, db: Session = Depends(get_db)):
	existing_quote = db.query(QuoteModel).filter(QuoteModel.id == quote_id).first()
	if not existing_quote:
		raise HTTPException(status_code=404, detail="Quote not found")
	if not quote.content.strip():
		raise HTTPException(status_code=404, detail="Content is required")
	existing_quote.content = quote.content
	db.commit()
	db.refresh(existing_quote)
	return existing_quote

@app.delete("/quotes/{quote_id}")
def delete_quote(quote_id: int, db: Session = Depends(get_db)):
	quote = db.query(QuoteModel).filter(QuoteModel.id == quote_id).first()
	if not quote:
		raise HTTPException(status_code=404, detail="Quote Not Found")
	db.delete(quote)
	db.commit()
	return {"message": "Quote Deleted Successfullny"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
	return JSONResponse(
		status_code=exc.status.code,
		content={"detail": exc.detail},
	)


if __name__ == "__main__":
	import uvicorn 
	from dotenv import load_dotenv 
	import os 

	load_dotenv()


	host = os.getenv("HOST")
	port = int(os.getenv("PORT"))

	uvicorn.run(app, host=host, port=port)

