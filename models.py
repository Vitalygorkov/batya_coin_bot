import sqlite3

conn = sqlite3.connect('bazasearch.db')
cur = conn.cursor()
# cur.execute("SELECT * FROM channels;")
# all_results = cur.fetchall()
cur.execute("""CREATE TABLE IF NOT EXISTS vidos(
   User TEXT PRIMARY KEY,
   Goals TEXT,
   prosm TEXT,
   Others TEXT);
""")
conn.commit()