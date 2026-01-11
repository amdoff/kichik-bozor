import sqlite3

conn = sqlite3.connect("marketplace.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price TEXT
)
""")

conn.commit()

def add_product(name, price):
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    conn.commit()

def get_products():
    cursor.execute("SELECT name, price FROM products")
    return cursor.fetchall()
