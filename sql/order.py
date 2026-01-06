#  Salary ascending
import sqlite3
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
SELECT name, salary
FROM employees
ORDER BY salary ASC
""")
print(cursor.fetchall())
conn.close()

# output:
# [('Meena', 60000), ('John', 65000), ('Asha', 70000), ('Sara', 75000), ('Ravi', 80000)]
 