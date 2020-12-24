import sqlite3
from data import data, orders
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users(
    userid INTEGER PRIMARY KEY,
    fname TEXT,
    lname TEXT,
    gender TEXT) ;
    """)
conn.commit()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS orders(
    orderid INTEGER PRIMARY KEY,
    date TEXT,
    userid TEXT,
    total TEXT) ;
    """)
conn.commit()



cursor.executemany(
    """
    INSERT INTO users VALUES(?, ?, ?, ?);
    """, data
)
conn.commit()

cursor.executemany(
    """
    INSERT INTO orders VALUE (?, ?, ?, ?)
    """, orders
)
conn.commit()