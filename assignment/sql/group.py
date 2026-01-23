# Average salary per department
import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()
cursor.execute("""
SELECT department, AVG(salary)
FROM employees
GROUP BY department
""")
print(cursor.fetchall())
conn.close()


# output:
# [('AI', 75000.0), ('ML', 62500.0), ('NLP', 75000.0)]

