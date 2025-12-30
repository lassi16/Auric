from db import get_connection

with open("schema.sql", "r") as f:
    schema = f.read()

conn = get_connection()
cur = conn.cursor()
cur.execute(schema)
conn.commit()

cur.close()
conn.close()

print("Database schema created successfully")
