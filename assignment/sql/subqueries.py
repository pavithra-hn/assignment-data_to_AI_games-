#  Salary greater than average
import sqlite3
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
""")
print(cursor.fetchall())
conn.close()

# output:
# [('Ravi', 80000), ('Sara', 75000)]