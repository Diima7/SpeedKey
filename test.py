import sqlite3


conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("SELECT * FROM keys")
print(c.fetchone())
