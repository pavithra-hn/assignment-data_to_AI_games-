#Count employees per department
import sqlite3
conn = sqlite3.connect("company.db")
cursor = conn.cursor()
cursor.execute("""
SELECT department, COUNT(*)
FROM employees
GROUP BY department
""")
print(cursor.fetchall())
conn.close()

# output:
# [('AI', 2), ('ML', 2), ('NLP', 1)]