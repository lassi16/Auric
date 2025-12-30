from db import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT current_database();")
print("Database:", cur.fetchone())

cur.execute("SELECT current_schema();")
print("Schema:", cur.fetchone())

cur.close()
conn.close()
