import sqlite3
from datetime import datetime

DB_NAME = "expenses.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       amount REAL,
                       category TEXT,
                       date TEXT)''')
    conn.commit()
    conn.close()

def add_expense(amount, category):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)",
                   (amount, category, date))
    conn.commit()
    conn.close()

def fetch_expenses():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT amount, category, date FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return rows
