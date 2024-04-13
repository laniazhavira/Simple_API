import sqlite3

def get_all_quotes():
	conn = sqlite3.connect('quotes.db')
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM quotes;")
	rows =cursor.fetchall()
	conn.close()
	return rows
