#Select specific columns
import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

for row in rows:
    print(row)
# print(rows)
conn.close()


# output:
# (1, 'Asha', 'AI', 70000)
# (2, 'Ravi', 'AI', 80000)
# (3, 'Meena', 'ML', 60000)
# (4, 'John', 'ML', 65000)
# (5, 'Sara', 'NLP', 75000)